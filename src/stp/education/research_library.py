"""Research library: classified catalog of authored publications and local files.

The curated catalog lives in ``content/evidencia/research_library.yaml``.
Policy (v1.1+): only works with a **public DOI** (Zenodo or Preprints.org)
are listed; local drafts without DOI are excluded.

Binary files (PDF/DOCX) stay outside the git tree under a configurable
publications directory (default: ``~/Investigaciones/Publicaciones``).
Remote users can still open ``https://doi.org/<doi>`` without local files.

Environment overrides (first match wins):
  - ``STP_PUBLICATIONS_DIR``
  - settings / catalog ``root_path``
"""

from __future__ import annotations

import os
import unicodedata
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any, Iterable, Sequence

import yaml

from stp.config.settings import ROOT

_CATALOG_REL = Path("content") / "evidencia" / "research_library.yaml"
_DEFAULT_ROOTS = (
    Path("/Users/johelpadilla/Investigaciones/Publicaciones"),
    Path.home() / "Investigaciones" / "Publicaciones",
)

_DOC_EXTS = {".pdf", ".docx", ".doc", ".md", ".txt", ".html"}


@dataclass(frozen=True)
class LibraryItem:
    """One classified work in the research library."""

    id: str
    title: str
    authors: str = "Padilla-Villanueva, J."
    year: int | None = None
    collection: str = "other"
    type: str = "article"
    domain: str = "theory"
    topics: tuple[str, ...] = ()
    status: str = "reference"
    language: str = "en"
    format: str = "pdf"
    file: str = ""
    doi: str | None = None
    url: str | None = None
    summary: str = ""
    summary_es: str = ""
    related: tuple[str, ...] = ()
    sort_order: int = 999
    featured: bool = False
    # runtime
    available: bool = False
    path: Path | None = None
    size_bytes: int = 0
    orphan: bool = False

    def size_label(self) -> str:
        if self.size_bytes <= 0:
            return "—"
        mb = self.size_bytes / (1024 * 1024)
        if mb >= 1:
            return f"{mb:.1f} MB"
        kb = self.size_bytes / 1024
        return f"{kb:.0f} KB"

    def display_summary(self, lang: str = "es") -> str:
        if lang.startswith("es") and self.summary_es:
            return self.summary_es
        return self.summary or self.summary_es or ""


@dataclass(frozen=True)
class CollectionMeta:
    id: str
    label_es: str
    label_en: str
    label_fr: str
    description_es: str = ""
    description_en: str = ""
    description_fr: str = ""
    order: int = 50

    def label(self, lang: str = "es") -> str:
        lang = (lang or "es")[:2]
        if lang == "en":
            return self.label_en or self.label_es
        if lang == "fr":
            return self.label_fr or self.label_en or self.label_es
        return self.label_es or self.label_en


def catalog_path() -> Path:
    return ROOT / _CATALOG_REL


def publications_root(override: str | Path | None = None) -> Path | None:
    """Resolve directory that holds the binary corpus."""
    if override:
        p = Path(override).expanduser().resolve()
        return p if p.is_dir() else None
    env = os.environ.get("STP_PUBLICATIONS_DIR", "").strip()
    if env:
        p = Path(env).expanduser().resolve()
        if p.is_dir():
            return p
    # catalog may declare root_path
    data = _raw_catalog()
    declared = (data.get("root_path") or "").strip()
    if declared:
        p = Path(declared).expanduser().resolve()
        if p.is_dir():
            return p
    for cand in _DEFAULT_ROOTS:
        if cand.is_dir():
            return cand.resolve()
    return None


@lru_cache(maxsize=4)
def _raw_catalog() -> dict[str, Any]:
    path = catalog_path()
    if not path.exists():
        return {}
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except Exception:
        return {}
    return data if isinstance(data, dict) else {}


def clear_library_cache() -> None:
    _raw_catalog.cache_clear()
    list_library.cache_clear()


def _as_tuple(val: Any) -> tuple[str, ...]:
    if not val:
        return ()
    if isinstance(val, str):
        return (val,)
    return tuple(str(x) for x in val)


def _resolve_file(root: Path, rel: str) -> Path | None:
    """Resolve a relative file under root; tolerate NFC/NFD filename variants."""
    if not rel:
        return None
    root = root.resolve()
    candidates = [
        root / rel,
        root / Path(rel).name,
        root / unicodedata.normalize("NFC", rel),
        root / unicodedata.normalize("NFD", rel),
        root / unicodedata.normalize("NFC", Path(rel).name),
        root / unicodedata.normalize("NFD", Path(rel).name),
    ]
    for cand in candidates:
        try:
            resolved = cand.resolve()
            resolved.relative_to(root)
        except (ValueError, OSError):
            continue
        if resolved.is_file():
            return resolved
    # Fallback: match by basename ignoring unicode form
    want = unicodedata.normalize("NFC", Path(rel).name)
    try:
        for p in root.rglob("*"):
            if not p.is_file():
                continue
            if unicodedata.normalize("NFC", p.name) == want:
                return p.resolve()
    except OSError:
        pass
    return None


def _item_from_dict(
    raw: dict[str, Any],
    *,
    root: Path | None,
    orphan: bool = False,
) -> LibraryItem:
    rel = str(raw.get("file") or raw.get("path") or "").strip()
    path: Path | None = None
    available = False
    size = 0
    if rel and root is not None:
        path = _resolve_file(root, rel)
        if path is not None:
            available = True
            size = path.stat().st_size
    fmt = str(raw.get("format") or (Path(rel).suffix.lstrip(".") if rel else "pdf") or "pdf")
    return LibraryItem(
        id=str(raw.get("id") or Path(rel).stem or "item"),
        title=str(raw.get("title") or rel or "Untitled"),
        authors=str(raw.get("authors") or "Padilla-Villanueva, J."),
        year=int(raw["year"]) if raw.get("year") not in (None, "") else None,
        collection=str(raw.get("collection") or "other"),
        type=str(raw.get("type") or "article"),
        domain=str(raw.get("domain") or "theory"),
        topics=_as_tuple(raw.get("topics") or raw.get("tags")),
        status=str(raw.get("status") or "reference"),
        language=str(raw.get("language") or "en"),
        format=fmt.lower(),
        file=rel,
        doi=(str(raw["doi"]) if raw.get("doi") else None),
        url=(str(raw["url"]) if raw.get("url") else None),
        summary=str(raw.get("summary") or ""),
        summary_es=str(raw.get("summary_es") or raw.get("summary") or ""),
        related=_as_tuple(raw.get("related")),
        sort_order=int(raw.get("sort_order") or 999),
        featured=bool(raw.get("featured") or False),
        available=available,
        path=path,
        size_bytes=size,
        orphan=orphan,
    )


def list_collections(lang: str = "es") -> list[CollectionMeta]:
    data = _raw_catalog()
    out: list[CollectionMeta] = []
    for c in data.get("collections") or []:
        if not isinstance(c, dict) or not c.get("id"):
            continue
        out.append(
            CollectionMeta(
                id=str(c["id"]),
                label_es=str(c.get("label_es") or c.get("label") or c["id"]),
                label_en=str(c.get("label_en") or c.get("label") or c["id"]),
                label_fr=str(c.get("label_fr") or c.get("label_en") or c.get("label") or c["id"]),
                description_es=str(c.get("description_es") or c.get("description") or ""),
                description_en=str(c.get("description_en") or c.get("description") or ""),
                description_fr=str(c.get("description_fr") or c.get("description_en") or ""),
                order=int(c.get("order") or 50),
            )
        )
    out.sort(key=lambda x: (x.order, x.id))
    return out


def collection_label(collection_id: str, lang: str = "es") -> str:
    for c in list_collections(lang):
        if c.id == collection_id:
            return c.label(lang)
    return collection_id


@lru_cache(maxsize=8)
def list_library(include_orphans: bool = True) -> tuple[LibraryItem, ...]:
    """Return all catalog items (+ optional unscanned orphans on disk)."""
    data = _raw_catalog()
    root = publications_root()
    items: list[LibraryItem] = []
    seen_files: set[str] = set()

    def _norm_name(s: str) -> str:
        return unicodedata.normalize("NFC", s.replace("\\", "/"))

    for raw in data.get("items") or []:
        if not isinstance(raw, dict):
            continue
        it = _item_from_dict(raw, root=root)
        items.append(it)
        if it.file:
            seen_files.add(_norm_name(it.file))
            seen_files.add(_norm_name(Path(it.file).name))
        if it.path is not None:
            try:
                rel_on_disk = it.path.relative_to(root.resolve()).as_posix()
                seen_files.add(_norm_name(rel_on_disk))
                seen_files.add(_norm_name(it.path.name))
            except (ValueError, OSError):
                pass

    if include_orphans and root is not None:
        for path in sorted(root.rglob("*")):
            if not path.is_file():
                continue
            if path.name.startswith("."):
                continue
            if path.suffix.lower() not in _DOC_EXTS:
                continue
            rel = path.relative_to(root).as_posix()
            if _norm_name(rel) in seen_files or _norm_name(path.name) in seen_files:
                continue
            items.append(
                _item_from_dict(
                    {
                        "id": f"orphan_{path.stem}"[:64],
                        "title": path.stem.replace("_", " "),
                        "file": rel,
                        "format": path.suffix.lstrip("."),
                        "collection": "unclassified",
                        "type": "document",
                        "domain": "other",
                        "status": "unclassified",
                        "year": None,
                        "summary_es": "Archivo detectado en el directorio de publicaciones, aún sin ficha curada.",
                        "summary": "File found in the publications directory, not yet curated.",
                        "sort_order": 9000,
                    },
                    root=root,
                    orphan=True,
                )
            )

    items.sort(key=lambda x: (x.sort_order, x.year or 0, x.title.lower()))
    return tuple(items)


def filter_library(
    items: Sequence[LibraryItem] | None = None,
    *,
    collection: str | None = None,
    domain: str | None = None,
    type_: str | None = None,
    status: str | None = None,
    year: int | None = None,
    language: str | None = None,
    available_only: bool = False,
    featured_only: bool = False,
    query: str = "",
    topics: Iterable[str] | None = None,
) -> list[LibraryItem]:
    """Filter catalog items for UI / CLI."""
    pool = list(items if items is not None else list_library())
    topics_set = {t.lower() for t in (topics or []) if t}

    def ok(it: LibraryItem) -> bool:
        if collection and it.collection != collection:
            return False
        if domain and it.domain != domain:
            return False
        if type_ and it.type != type_:
            return False
        if status and it.status != status:
            return False
        if year is not None and it.year != year:
            return False
        if language and it.language != language:
            return False
        if available_only and not it.available:
            return False
        if featured_only and not it.featured:
            return False
        if topics_set and not topics_set.intersection(t.lower() for t in it.topics):
            return False
        if query.strip():
            q = query.strip().lower()
            blob = " ".join(
                [
                    it.title,
                    it.authors,
                    it.summary,
                    it.summary_es,
                    it.collection,
                    it.domain,
                    it.type,
                    " ".join(it.topics),
                    it.doi or "",
                    it.file,
                ]
            ).lower()
            if q not in blob:
                return False
        return True

    return [it for it in pool if ok(it)]


def get_item(item_id: str) -> LibraryItem | None:
    for it in list_library():
        if it.id == item_id:
            return it
    return None


def library_stats(items: Sequence[LibraryItem] | None = None) -> dict[str, Any]:
    pool = list(items if items is not None else list_library())
    by_collection: dict[str, int] = {}
    by_domain: dict[str, int] = {}
    by_type: dict[str, int] = {}
    available = 0
    for it in pool:
        by_collection[it.collection] = by_collection.get(it.collection, 0) + 1
        by_domain[it.domain] = by_domain.get(it.domain, 0) + 1
        by_type[it.type] = by_type.get(it.type, 0) + 1
        if it.available:
            available += 1
    return {
        "total": len(pool),
        "available": available,
        "missing_files": len(pool) - available,
        "by_collection": dict(sorted(by_collection.items(), key=lambda kv: (-kv[1], kv[0]))),
        "by_domain": dict(sorted(by_domain.items(), key=lambda kv: (-kv[1], kv[0]))),
        "by_type": dict(sorted(by_type.items(), key=lambda kv: (-kv[1], kv[0]))),
        "root": str(publications_root() or ""),
    }


def read_item_bytes(item_id: str, max_bytes: int = 80_000_000) -> bytes | None:
    """Load file bytes for download (size-capped)."""
    it = get_item(item_id)
    if not it or not it.path or not it.path.is_file():
        return None
    size = it.path.stat().st_size
    if size > max_bytes:
        raise ValueError(f"File too large to stream in UI ({size} bytes): {it.file}")
    return it.path.read_bytes()


def mime_for(item: LibraryItem) -> str:
    ext = (item.format or "").lower()
    return {
        "pdf": "application/pdf",
        "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "doc": "application/msword",
        "md": "text/markdown",
        "txt": "text/plain",
        "html": "text/html",
    }.get(ext, "application/octet-stream")


def group_by_collection(
    items: Sequence[LibraryItem] | None = None,
    lang: str = "es",
) -> list[tuple[CollectionMeta | None, list[LibraryItem]]]:
    """Group items in catalog collection order; unknown collections last."""
    pool = list(items if items is not None else list_library())
    metas = {c.id: c for c in list_collections(lang)}
    order = {c.id: c.order for c in metas.values()}
    buckets: dict[str, list[LibraryItem]] = {}
    for it in pool:
        buckets.setdefault(it.collection, []).append(it)
    keys = sorted(buckets.keys(), key=lambda k: (order.get(k, 500), k))
    out: list[tuple[CollectionMeta | None, list[LibraryItem]]] = []
    for k in keys:
        out.append((metas.get(k), buckets[k]))
    return out
