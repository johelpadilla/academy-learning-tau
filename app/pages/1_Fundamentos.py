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

st.set_page_config(page_title=f"{t('fund_title')} | STP", page_icon="🌀", layout="wide")
inject_css()

st.title(t("fund_title"))
st.caption(t("fund_caption"))

tabs = st.tabs([
    t("fund_tab1"),
    t("fund_tab2"),
    t("fund_tab3"),
    t("fund_tab4"),
    t("fund_tab5"),
    t("fund_tab6")
])

files = [
    ("fundamentos", "01_tau.md"),
    ("fundamentos", "02_ews_limits.md"),
    ("fundamentos", "03_recd_levels.md"),
    ("fundamentos", "04_excess3.md"),
    ("fundamentos", "05_csd.md"),
    ("fundamentos", "06_filosofia.md"),
]

for tab, parts in zip(tabs, files):
    with tab:
        st.markdown(read_markdown(*parts))

st.sidebar.markdown(t("sidebar_in_this_section"))
st.sidebar.markdown(f"""
{t("fund_sb1")}
{t("fund_sb2")}
{t("fund_sb3")}
{t("fund_sb4")}
{t("fund_sb5")}
{t("fund_sb6")}
""")
