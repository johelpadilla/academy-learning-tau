"""UI string catalogs and language state.

Spanish (``es``) is the source of truth. Missing keys fall back to Spanish,
then to the key itself so the UI never crashes.
"""

from __future__ import annotations

import json
import os
import threading
from functools import lru_cache
from pathlib import Path
from typing import Any

SUPPORTED_LANGS: tuple[str, ...] = ("es", "en", "fr")
LANG_LABELS: dict[str, str] = {
    "es": "Español",
    "en": "English",
    "fr": "Français",
}

_DEFAULT = "es"
_tls = threading.local()


def _repo_root() -> Path:
    # src/stp/i18n/core.py → parents[3] = repo root
    return Path(__file__).resolve().parents[3]


def locales_dir() -> Path:
    return _repo_root() / "locales"


def _normalize(lang: str | None) -> str:
    if not lang:
        return _DEFAULT
    lang = str(lang).strip().lower()[:2]
    return lang if lang in SUPPORTED_LANGS else _DEFAULT


def get_lang() -> str:
    """Resolve language: thread override → Streamlit session → env → es."""
    override = getattr(_tls, "lang", None)
    if override:
        return _normalize(override)
    try:
        import streamlit as st

        if hasattr(st, "session_state") and "stp_lang" in st.session_state:
            return _normalize(st.session_state["stp_lang"])
    except Exception:
        pass
    return _normalize(os.environ.get("STP_LANG", _DEFAULT))


def set_lang(lang: str) -> str:
    """Set language for current Streamlit session and thread."""
    lang = _normalize(lang)
    _tls.lang = lang
    try:
        import streamlit as st

        st.session_state["stp_lang"] = lang
    except Exception:
        pass
    os.environ["STP_LANG"] = lang
    return lang


def clear_catalog_cache() -> None:
    _load_catalog_cached.cache_clear()


def _catalog_mtime(lang: str) -> float:
    path = locales_dir() / lang / "ui.json"
    try:
        return path.stat().st_mtime if path.exists() else -1.0
    except OSError:
        return -1.0


@lru_cache(maxsize=16)
def _load_catalog_cached(lang: str, mtime: float) -> dict[str, Any]:
    """Load catalog; ``mtime`` is part of the cache key so edits bust stale text."""
    path = locales_dir() / lang / "ui.json"
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return data if isinstance(data, dict) else {}


def _load_catalog(lang: str) -> dict[str, Any]:
    return _load_catalog_cached(lang, _catalog_mtime(lang))


def _dig(tree: dict[str, Any], key: str) -> Any:
    cur: Any = tree
    for part in key.split("."):
        if not isinstance(cur, dict) or part not in cur:
            return None
        cur = cur[part]
    return cur


def is_unresolved_key(text: str | None, key: str | None = None) -> bool:
    """True when a translation call failed and left a machine key visible."""
    if not text:
        return True
    s = str(text).strip()
    if key and s == key:
        return True
    # Common failure modes: raw dotted catalog paths leaked into the UI
    if s.startswith("domain_voice.") or s.startswith("domain_voice_ui."):
        return True
    if s.startswith("fundamentos.") or s.startswith("lab.") or s.startswith("auth."):
        return True
    return False


def t(key: str, lang: str | None = None, **kwargs: Any) -> str:
    """Translate UI key. Fallback: requested lang → es → key."""
    lang = _normalize(lang or get_lang())
    val = _dig(_load_catalog(lang), key)
    if val is None and lang != _DEFAULT:
        val = _dig(_load_catalog(_DEFAULT), key)
    if val is None:
        return key if not kwargs else key
    if not isinstance(val, str):
        val = str(val)
    if kwargs:
        try:
            return val.format(**kwargs)
        except (KeyError, ValueError):
            return val
    return val


def tf(key: str, **kwargs: Any) -> str:
    """Alias for ``t`` with format kwargs (readability at call sites)."""
    return t(key, **kwargs)
