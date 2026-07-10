from __future__ import annotations

import sys
from pathlib import Path

_APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_APP))
from components.bootstrap import ensure_stp_path  # noqa: E402

ROOT = ensure_stp_path(__file__)

import streamlit as st

from components.illustrations import show_illustration
from components.micro_labs import render_micro_lab
from components.ui import page_link, footer, learning_goals, page_header
from stp.config.settings import DOMAIN_PRESETS
from stp.domains import domain_label
from stp.domains.voice import render_situated_example
from stp.education.content_loader import read_markdown
from stp.i18n.core import t

st.set_page_config(page_title=t("fundamentos.page_title"), page_icon="🌀", layout="wide")

page_header(
    t("fundamentos.title"),
    subtitle=t("fundamentos.subtitle"),
    eyebrow=t("fundamentos.eyebrow"),
    icon="📘",
)

learning_goals(
    [t("fundamentos.goal_1"), t("fundamentos.goal_2"), t("fundamentos.goal_3")]
)

# Domain lens: situated examples / jargon while teaching abstract Tau
_lens_domains = [d for d in DOMAIN_PRESETS.keys() if d != "synthetic"] + ["synthetic"]
if "fund_domain_lens" not in st.session_state:
    st.session_state["fund_domain_lens"] = st.session_state.get("lab_domain", "cardiology")
    if st.session_state["fund_domain_lens"] not in DOMAIN_PRESETS:
        st.session_state["fund_domain_lens"] = "cardiology"

st.markdown(f"### {t('fundamentos.domain_lens_header')}")
st.caption(t("fundamentos.domain_lens_help"))
lens_domain = st.selectbox(
    t("fundamentos.domain_lens_select"),
    _lens_domains,
    index=_lens_domains.index(st.session_state["fund_domain_lens"])
    if st.session_state["fund_domain_lens"] in _lens_domains
    else 0,
    format_func=lambda k: domain_label(k),
    key="fund_domain_lens",
)
st.session_state["lab_domain"] = lens_domain  # keep Lab deep-link coherent

tabs = st.tabs(
    [
        t("fundamentos.tab_1"),
        t("fundamentos.tab_2"),
        t("fundamentos.tab_3"),
        t("fundamentos.tab_4"),
        t("fundamentos.tab_5"),
        t("fundamentos.tab_6"),
    ]
)

files = [
    ("fundamentos", "01_tau.md"),
    ("fundamentos", "02_ews_limits.md"),
    ("fundamentos", "03_recd_levels.md"),
    ("fundamentos", "04_excess3.md"),
    ("fundamentos", "05_csd.md"),
    ("fundamentos", "06_filosofia.md"),
]

tab_illustrations = [
    "tau_relational",
    "dual_reading",
    "recd_nested",
    "excess3",
    "dual_reading",
    "chronos_kairos",
]

# One micro-lab topic per theoretical module
micro_topics = ["tau", "ews", "recd", "excess3", "csd", "philosophy"]

# Domain-situated callout key per tab
_example_fields = [
    "example_tau",
    "classic_gloss",
    "example_recd",
    "excess_gloss",
    "example_dual",
    "jargon_note",
]
_example_headers = [
    "domain_voice_ui.example_tau_h",
    "domain_voice_ui.example_dual_h",
    "domain_voice_ui.example_recd_h",
    "domain_voice_ui.example_recd_h",
    "domain_voice_ui.example_dual_h",
    "domain_voice_ui.jargon",
]

for tab, parts, illus, topic, ex_field, ex_h in zip(
    tabs, files, tab_illustrations, micro_topics, _example_fields, _example_headers
):
    with tab:
        show_illustration(illus)
        # Full sentences for visitors — never raw i18n keys
        st.info(render_situated_example(lens_domain, ex_field, ex_h))
        st.markdown(read_markdown(*parts))
        st.divider()
        render_micro_lab(topic, domain=lens_domain)

st.sidebar.markdown(
    f'<div class="stp-sidebar-section">{t("common.suggested_path")}</div>',
    unsafe_allow_html=True,
)
st.sidebar.markdown(t("fundamentos.sidebar_path"))
try:
    from stp.education.handouts import render_handout_bytes

    st.download_button(
        t("fundamentos.dl_fund"),
        data=render_handout_bytes("fundamentos_compilado"),
        file_name="stp_fundamentos_compilado.md",
        mime="text/markdown",
        width="stretch",
    )
    st.download_button(
        t("fundamentos.dl_theory"),
        data=render_handout_bytes("teoria"),
        file_name="stp_03_teoria_tau_recd.md",
        mime="text/markdown",
        width="stretch",
    )
except Exception:
    pass

page_link("pages/2_Matematica.py", label=t("nav.next_math"), icon="📐")
page_link("pages/4_Laboratorio.py", label=t("nav.practice_lab"), icon="🔬")
page_link("pages/8_Materiales.py", label=t("nav.materials"), icon="📦")

footer()
