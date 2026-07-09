from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "app"))

import streamlit as st

from components.hero import inject_css
from stp.education.content_loader import read_markdown
from stp.education.glossary import search_glossary
from locales import t

st.set_page_config(page_title=f"{t('ruta_title')} | STP", page_icon="🌀", layout="wide")
inject_css()

st.title(t("ruta_title"))

levels = {
    t("ruta_l1"): [
        t("ruta_l1_1"),
        t("ruta_l1_2"),
        t("ruta_l1_3"),
    ],
    t("ruta_l2"): [
        t("ruta_l2_1"),
        t("ruta_l2_2"),
        t("ruta_l2_3"),
        t("ruta_l2_4"),
    ],
    t("ruta_l3"): [
        t("ruta_l3_1"),
        t("ruta_l3_2"),
        t("ruta_l3_3"),
        t("ruta_l3_4"),
    ],
}

for level, items in levels.items():
    with st.expander(t("ruta_nivel", level=level), expanded=(level == t("ruta_l1"))):
        for i, item in enumerate(items):
            key = f"lp_{level}_{i}"
            st.checkbox(item, key=key)

st.subheader(t("ruta_glos"))
q = st.text_input(t("ruta_search"), "")
for term in search_glossary(q):
    with st.expander(term.get("term", "?")):
        st.markdown(f"**{term.get('short','')}**")
        st.markdown(term.get("long", ""))
        st.caption(f"Nivel: {term.get('level', '—')}")

st.subheader(t("ruta_faq"))
st.markdown(read_markdown("learning", "faq.md"))
