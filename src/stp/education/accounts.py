"""Local student accounts and progress records (no cloud backend).

Credentials and progress live under ``data/student_records/`` as JSON.
Passwords use PBKDF2-HMAC-SHA256 (stdlib only). Suitable for classroom
laptops / local servers — not a multi-tenant SaaS auth system.
"""

from __future__ import annotations

import hashlib
import json
import re
import secrets
import threading
import uuid
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from stp.config.settings import ROOT

RECORDS_DIR = ROOT / "data" / "student_records"
USERS_INDEX = RECORDS_DIR / "users_index.json"

_PBKDF2_ITERS = 200_000
_USERNAME_RE = re.compile(r"^[a-zA-Z0-9_.@+-]{3,64}$")
_lock = threading.RLock()


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def ensure_records_dir() -> Path:
    RECORDS_DIR.mkdir(parents=True, exist_ok=True)
    return RECORDS_DIR


def _hash_password(password: str, salt: bytes | None = None) -> tuple[str, str]:
    if salt is None:
        salt = secrets.token_bytes(16)
    dk = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, _PBKDF2_ITERS
    )
    return salt.hex(), dk.hex()


def _verify_password(password: str, salt_hex: str, hash_hex: str) -> bool:
    try:
        salt = bytes.fromhex(salt_hex)
    except ValueError:
        return False
    _, candidate = _hash_password(password, salt=salt)
    return secrets.compare_digest(candidate, hash_hex)


def normalize_username(username: str) -> str:
    return (username or "").strip().lower()


def validate_username(username: str) -> str | None:
    u = normalize_username(username)
    if not _USERNAME_RE.match(u):
        return "invalid_username"
    return None


def validate_password(password: str) -> str | None:
    if not password or len(password) < 6:
        return "password_short"
    if len(password) > 128:
        return "password_long"
    return None


@dataclass
class UserRecord:
    user_id: str
    username: str
    display_name: str
    password_salt: str
    password_hash: str
    created_at: str
    last_login: str | None = None
    lang_pref: str = "es"

    def public_dict(self) -> dict[str, Any]:
        return {
            "user_id": self.user_id,
            "username": self.username,
            "display_name": self.display_name,
            "created_at": self.created_at,
            "last_login": self.last_login,
            "lang_pref": self.lang_pref,
        }


@dataclass
class StudentProgress:
    user_id: str
    username: str
    display_name: str
    checklist: dict[str, bool] = field(default_factory=dict)
    # module_id -> list of attempt dicts
    quiz_attempts: dict[str, list[dict[str, Any]]] = field(default_factory=dict)
    # best % per module
    best_scores: dict[str, float] = field(default_factory=dict)
    activity_log: list[dict[str, Any]] = field(default_factory=list)
    # free-form task marks (e.g. lab deliverables)
    tasks: dict[str, dict[str, Any]] = field(default_factory=dict)
    updated_at: str = field(default_factory=_utc_now)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "StudentProgress":
        return cls(
            user_id=str(data.get("user_id", "")),
            username=str(data.get("username", "")),
            display_name=str(data.get("display_name", "")),
            checklist=dict(data.get("checklist") or {}),
            quiz_attempts={
                k: list(v) for k, v in (data.get("quiz_attempts") or {}).items()
            },
            best_scores={
                k: float(v) for k, v in (data.get("best_scores") or {}).items()
            },
            activity_log=list(data.get("activity_log") or []),
            tasks={k: dict(v) for k, v in (data.get("tasks") or {}).items()},
            updated_at=str(data.get("updated_at") or _utc_now()),
        )


def _read_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return default


def _write_json(path: Path, data: Any) -> None:
    ensure_records_dir()
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(
        json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    tmp.replace(path)


def _load_index() -> dict[str, Any]:
    ensure_records_dir()
    data = _read_json(USERS_INDEX, {"users": {}})
    if not isinstance(data, dict):
        return {"users": {}}
    data.setdefault("users", {})
    return data


def _save_index(index: dict[str, Any]) -> None:
    _write_json(USERS_INDEX, index)


def _progress_path(user_id: str) -> Path:
    safe = re.sub(r"[^a-zA-Z0-9_-]", "", user_id)[:64]
    return RECORDS_DIR / f"progress_{safe}.json"


def create_account(
    username: str,
    password: str,
    display_name: str = "",
    lang_pref: str = "es",
) -> tuple[UserRecord | None, str | None]:
    """Register a new user. Returns (user, error_code)."""
    err = validate_username(username)
    if err:
        return None, err
    err = validate_password(password)
    if err:
        return None, err
    u = normalize_username(username)
    name = (display_name or u).strip()[:80]
    with _lock:
        index = _load_index()
        if u in index["users"]:
            return None, "username_taken"
        salt_hex, hash_hex = _hash_password(password)
        user = UserRecord(
            user_id=uuid.uuid4().hex,
            username=u,
            display_name=name,
            password_salt=salt_hex,
            password_hash=hash_hex,
            created_at=_utc_now(),
            last_login=_utc_now(),
            lang_pref=lang_pref[:2],
        )
        index["users"][u] = asdict(user)
        _save_index(index)
        progress = StudentProgress(
            user_id=user.user_id,
            username=user.username,
            display_name=user.display_name,
        )
        log_activity(progress, "register", {"username": u})
        save_progress(progress)
        return user, None


def authenticate(
    username: str, password: str
) -> tuple[UserRecord | None, str | None]:
    u = normalize_username(username)
    if not u or not password:
        return None, "invalid_credentials"
    with _lock:
        index = _load_index()
        raw = index["users"].get(u)
        if not raw:
            return None, "invalid_credentials"
        if not _verify_password(
            password, raw.get("password_salt", ""), raw.get("password_hash", "")
        ):
            return None, "invalid_credentials"
        raw["last_login"] = _utc_now()
        index["users"][u] = raw
        _save_index(index)
        user = UserRecord(**{k: raw[k] for k in UserRecord.__dataclass_fields__ if k in raw})
        progress = load_progress(user.user_id)
        if progress is None:
            progress = StudentProgress(
                user_id=user.user_id,
                username=user.username,
                display_name=user.display_name,
            )
        log_activity(progress, "login", {})
        save_progress(progress)
        return user, None


def get_user_by_id(user_id: str) -> UserRecord | None:
    with _lock:
        index = _load_index()
        for raw in index["users"].values():
            if raw.get("user_id") == user_id:
                return UserRecord(
                    **{k: raw[k] for k in UserRecord.__dataclass_fields__ if k in raw}
                )
    return None


def load_progress(user_id: str) -> StudentProgress | None:
    path = _progress_path(user_id)
    with _lock:
        data = _read_json(path, None)
    if not data or not isinstance(data, dict):
        return None
    return StudentProgress.from_dict(data)


def save_progress(progress: StudentProgress) -> None:
    progress.updated_at = _utc_now()
    # cap activity log
    if len(progress.activity_log) > 500:
        progress.activity_log = progress.activity_log[-500:]
    with _lock:
        _write_json(_progress_path(progress.user_id), progress.to_dict())


def log_activity(
    progress: StudentProgress,
    action: str,
    detail: dict[str, Any] | None = None,
) -> None:
    progress.activity_log.append(
        {
            "ts": _utc_now(),
            "action": action,
            "detail": detail or {},
        }
    )


def set_checklist_item(
    progress: StudentProgress, key: str, done: bool
) -> StudentProgress:
    progress.checklist[key] = bool(done)
    log_activity(progress, "checklist", {"key": key, "done": bool(done)})
    save_progress(progress)
    return progress


def set_task(
    progress: StudentProgress,
    task_id: str,
    status: str,
    note: str = "",
    meta: dict[str, Any] | None = None,
) -> StudentProgress:
    progress.tasks[task_id] = {
        "status": status,
        "note": (note or "")[:500],
        "meta": meta or {},
        "updated_at": _utc_now(),
    }
    log_activity(
        progress,
        "task",
        {"task_id": task_id, "status": status},
    )
    save_progress(progress)
    return progress


def record_quiz_attempt(
    progress: StudentProgress,
    module_id: str,
    attempt: dict[str, Any],
) -> StudentProgress:
    """Store attempt and update best score. ``attempt`` must include pct, score, max_score."""
    mid = str(module_id)
    progress.quiz_attempts.setdefault(mid, []).append(attempt)
    # keep last 20 attempts per module
    progress.quiz_attempts[mid] = progress.quiz_attempts[mid][-20:]
    pct = float(attempt.get("pct", 0.0))
    prev = float(progress.best_scores.get(mid, 0.0))
    if pct >= prev:
        progress.best_scores[mid] = pct
    log_activity(
        progress,
        "quiz_submit",
        {
            "module_id": mid,
            "score": attempt.get("score"),
            "max_score": attempt.get("max_score"),
            "pct": pct,
        },
    )
    save_progress(progress)
    return progress


def list_usernames() -> list[str]:
    with _lock:
        index = _load_index()
        return sorted(index["users"].keys())
