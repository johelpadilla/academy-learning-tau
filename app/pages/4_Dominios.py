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

st.set_page_config(page_title=f"{t('dom_title')} | STP", page_icon="🌀", layout="wide")
inject_css()

st.title(t("dom_title"))
st.markdown(t("dom_intro"))

domains = [
    (t("dom_d1_name"), "cardiologia.md", t("dom_d1_mat"), "SDDB / CCTP"),
    (t("dom_d2_name"), "epidemiologia.md", t("dom_d2_mat"), "Dengue PR / DengAI"),
    (t("dom_d3_name"), "neurociencia.md", t("dom_d3_mat"), "CHB-MIT"),
    (t("dom_d4_name"), "ecologia.md", t("dom_d4_mat"), "Lake Mendota / LTER"),
    (t("dom_d5_name"), "finanzas.md", t("dom_d5_mat"), "S&P 500"),
]

cols = st.columns(5)
for col, (name, _, maturity, data) in zip(cols, domains):
    with col:
        st.markdown(
            f"""
            <div class="stp-card">
              <h3>{name}</h3>
              <p class="stp-muted"><b>{t("dom_maturity")}</b> {maturity}<br/><b>{t("dom_data")}</b> {data}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown("---")
choice = st.selectbox(t("dom_preview"), [d[0] for d in domains])
fname = dict((d[0], d[1]) for d in domains)[choice]
st.markdown(read_markdown("dominios", fname))
