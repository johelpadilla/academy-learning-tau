"""Ensure Streamlit pages import *this* repo's ``stp`` package.

Failure modes we defend against:

1. Editable install pointing at an old scratch tree (wrong path).
2. Streamlit hot-reload reusing a stale ``stp.*`` module (dev only).
3. Streamlit reusing a stale ``components.ui`` after UI helpers were added
   (classic ``ImportError: cannot import name 'link_action_card'``).

By default we only fix ``sys.path`` once per process. Full module purge
runs only when ``STP_DEV_RELOAD=1`` so production/class sessions keep
imports (and ``@st.cache_data``) warm — *except* when a cached module is
clearly missing required symbols, in which case we drop it once.
"""

from __future__ import annotations

import importlib
import os
import sys
from pathlib import Path
from typing import Any

_PATH_READY = False

# Symbols that must exist on a healthy components.ui (post-UX redesign).
# If Streamlit still holds a pre-redesign module, import of Home/Lab crashes.
_UI_REQUIRED_ATTRS: tuple[str, ...] = (
    "link_action_card",
    "verdict_panel",
    "action_card",
    "render_hero",
    "page_header",
    "sidebar_nav",
)

_HANDOUTS_REQUIRED_ATTRS: tuple[str, ...] = (
    "pdf_available",
    "render_handout_pdf_bytes",
)


def _purge_modules(*prefixes: str) -> None:
    """Delete ``sys.modules`` entries matching exact names or prefixes."""
    for name in list(sys.modules):
        for pref in prefixes:
            if name == pref or name.startswith(pref + "."):
                del sys.modules[name]
                break
    importlib.invalidate_caches()


def _module_missing_attrs(mod_name: str, required: tuple[str, ...]) -> bool:
    mod = sys.modules.get(mod_name)
    if mod is None:
        return False
    return any(not hasattr(mod, attr) for attr in required)


def _purge_stale_ui_and_stp(root: Path) -> None:
    """Drop wrong-tree or half-loaded modules that break page imports."""
    # Wrong ``stp`` tree (editable install elsewhere)
    stp_mod = sys.modules.get("stp")
    if stp_mod is not None and getattr(stp_mod, "__file__", None):
        try:
            stp_root = Path(stp_mod.__file__).resolve().parents[2]
            if stp_root != root:
                _purge_modules("stp")
        except Exception:
            pass

    # Hot-reload: handouts PDF helpers added after first import
    if _module_missing_attrs("stp.education.handouts", _HANDOUTS_REQUIRED_ATTRS):
        _purge_modules("stp.education.handouts")
        # parent package may cache the old submodule reference
        edu = sys.modules.get("stp.education")
        if edu is not None and hasattr(edu, "handouts"):
            try:
                delattr(edu, "handouts")
            except Exception:
                pass

    # Hot-reload: components.ui redesigned (link_action_card, verdict_panel, …)
    if _module_missing_attrs("components.ui", _UI_REQUIRED_ATTRS):
        _purge_modules("components.ui")
        # hero re-exports from ui — drop if present so it rebinds
        if "components.hero" in sys.modules:
            _purge_modules("components.hero")


def import_ui(*names: str) -> tuple[Any, ...]:
    """Import symbols from ``components.ui``, recovering once from a stale cache.

    Prefer this over a bare ``from components.ui import …`` on pages that
    depend on helpers added after a Streamlit process started.
    """
    if not names:
        return ()
    try:
        from components import ui as ui_mod
    except Exception:
        _purge_modules("components.ui", "components.hero")
        from components import ui as ui_mod

    missing = [n for n in names if not hasattr(ui_mod, n)]
    if missing:
        _purge_modules("components.ui", "components.hero")
        from components import ui as ui_mod
        missing = [n for n in names if not hasattr(ui_mod, n)]
        if missing:
            raise ImportError(
                f"components.ui missing {missing!r} after reload "
                f"(file={getattr(ui_mod, '__file__', '?')})"
            )
    return tuple(getattr(ui_mod, n) for n in names)


_DEPS_CHECKED = False


def check_runtime_deps() -> list[str]:
    """Return names of missing *required* third-party packages (empty = OK)."""
    missing: list[str] = []
    for name in ("numpy", "pandas", "yaml", "pydantic"):
        try:
            __import__(name)
        except Exception:
            missing.append(name)
    # SciPy preferred (τ_s uses it); pure-NumPy fallback exists in tau_s.
    try:
        __import__("scipy")
    except Exception:
        missing.append("scipy (fallback Kendall-τ active if NumPy ok)")
    return missing


def ensure_stp_path(page_file: str | Path) -> Path:
    """
    Insert ``<repo>/src`` (and ``app/``) at the front of ``sys.path``.

    Returns the repository root.
    """
    global _PATH_READY, _DEPS_CHECKED

    page = Path(page_file).resolve()
    # pages live in app/pages/*.py → parents[2] = repo root
    # Home.py lives in app/ → parents[1] = repo root
    if page.parent.name == "pages":
        root = page.parents[2]
    else:
        root = page.parents[1]
    src = (root / "src").resolve()
    src_s = str(src)
    app_s = str((root / "app").resolve())

    if not _PATH_READY:
        for p in (src_s, app_s):
            while p in sys.path:
                sys.path.remove(p)
        sys.path.insert(0, src_s)
        sys.path.insert(0, app_s)
        _PATH_READY = True
    else:
        # Keep this tree first without thrashing path order every rerun
        if sys.path[:2] != [src_s, app_s]:
            for p in (src_s, app_s):
                while p in sys.path:
                    sys.path.remove(p)
            sys.path.insert(0, src_s)
            sys.path.insert(0, app_s)

    # Dev only: force re-import from disk after editing core sources
    if os.environ.get("STP_DEV_RELOAD", "").strip() in {"1", "true", "TRUE", "yes"}:
        _purge_modules("stp", "components.ui", "components.hero")

    try:
        _purge_stale_ui_and_stp(root)
    except Exception:
        pass

    # Always prefer this tree's UI strings (bust stale i18n if locales changed)
    try:
        from stp.i18n.core import clear_catalog_cache  # type: ignore

        # Lightweight: mtime is in the cache key; clear only if another stp tree was first
        import stp  # type: ignore

        stp_root = Path(stp.__file__).resolve().parents[2]
        if stp_root != root:
            clear_catalog_cache()
    except Exception:
        pass

    # One-shot soft warning on Streamlit Cloud when the scientific stack is incomplete.
    if not _DEPS_CHECKED:
        _DEPS_CHECKED = True
        missing = check_runtime_deps()
        hard = [m for m in missing if not m.startswith("scipy")]
        if hard:
            try:
                import streamlit as st

                st.error(
                    "**Runtime dependencies missing:** "
                    + ", ".join(hard)
                    + ". On Streamlit Community Cloud set **Python 3.12** "
                    "(Advanced settings → redeploy) and ensure "
                    "`requirements.txt` installs `numpy`, `pandas`, `scipy`."
                )
            except Exception:
                pass
        elif any(m.startswith("scipy") for m in missing):
            try:
                import streamlit as st

                st.warning(
                    "SciPy not importable — using NumPy Kendall-τ fallback. "
                    "Prefer Python **3.11 or 3.12** on Streamlit Cloud "
                    "(not 3.14) and reboot the app."
                )
            except Exception:
                pass

    return root
