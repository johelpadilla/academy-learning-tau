from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "app"))

import streamlit as st

from components.hero import inject_css
from stp.education.content_loader import read_markdown
from locales import t

st.set_page_config(page_title=f"{t('doc_title')} | STP", page_icon="🌀", layout="wide")
inject_css()

st.title(t("doc_title"))

st.markdown(read_markdown("docencia", "overview.md"))
