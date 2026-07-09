from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "app"))

import streamlit as st
import yaml

from components.hero import inject_css
from stp.config.settings import CONTENT_DIR
from locales import t

st.set_page_config(page_title=f"{t('ev_title')} | STP", page_icon="🌀", layout="wide")
inject_css()

st.title(t("ev_title"))

lang = st.session_state.get("lang", "es")
path = CONTENT_DIR / lang / "evidencia" / "publications.yaml"
# Fallback to ES
if not path.exists():
    path = CONTENT_DIR / "es" / "evidencia" / "publications.yaml"

data = yaml.safe_load(path.read_text(encoding="utf-8")) if path.exists() else {}

st.subheader(t("ev_sub1"))
for pub in data.get("publications", []):
    with st.container():
        st.markdown(f"### {pub.get('title')}")
        st.caption(
            f"{pub.get('authors')} · {pub.get('year')} · {pub.get('type')} · {t('ev_domain')} {pub.get('domain')}"
        )
        if pub.get("doi"):
            st.markdown(f"DOI: `{pub['doi']}`")
        for h in pub.get("highlights", []):
            st.markdown(f"- {h}")
        st.markdown("---")

st.subheader(t("ev_sub2"))
rows = data.get("comparison_matrix", [])
if rows:
    st.dataframe(rows, use_container_width=True)

st.info(t("ev_info"))
