"""Load Markdown educational content."""

from __future__ import annotations

from pathlib import Path

import streamlit as st
from stp.config.settings import CONTENT_DIR


def get_active_lang() -> str:
    """Gets the active language from session state, defaults to Spanish."""
    # Attempt to use st.session_state, fallback to 'es' if outside of a Streamlit context
    try:
        return st.session_state.get("lang", "es")
    except Exception:
        return "es"


def read_markdown(*parts: str) -> str:
    lang = get_active_lang()
    path = CONTENT_DIR.joinpath(lang, *parts)
    # Fallback to Spanish if the translation is not yet available
    if not path.exists():
        path = CONTENT_DIR.joinpath("es", *parts)
    if not path.exists():
        return f"_Contenido no encontrado: `{path.relative_to(CONTENT_DIR)}`_"
    return path.read_text(encoding="utf-8")


def list_section(section: str) -> list[Path]:
    lang = get_active_lang()
    d = CONTENT_DIR / lang / section
    if not d.exists():
        d = CONTENT_DIR / "es" / section
    if not d.exists():
        return []
    return sorted(d.glob("*.md"))
