"""Systemic Tau Platform — Home."""

from __future__ import annotations

import streamlit as st

from components.hero import render_hero
from locales import t

st.set_page_config(
    page_title="Systemic Tau Platform",
    page_icon="🌀",
    layout="wide",
    initial_sidebar_state="expanded",
)

render_hero()

st.markdown(t("home_audience"))

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(
        f"""
        <div class="stp-card">
          <h3>{t("home_card1_title")}</h3>
          <p class="stp-muted">{t("home_card1_text")}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with c2:
    st.markdown(
        f"""
        <div class="stp-card">
          <h3>{t("home_card2_title")}</h3>
          <p class="stp-muted">{t("home_card2_text")}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with c3:
    st.markdown(
        f"""
        <div class="stp-card">
          <h3>{t("home_card3_title")}</h3>
          <p class="stp-muted">{t("home_card3_text")}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")
st.subheader(t("home_domain_title"))
domain = st.selectbox(
    t("home_domain_sel"),
    options=[
        "Cardiología (SDDB / pre-FV)",
        "Epidemiología (Dengue)",
        "Neurociencia (Epilepsia / EEG)",
        "Ecología (Eutrofización de lagos)",
        "Finanzas (regímenes de volatilidad)",
    ],
    index=0,
)
st.session_state["domain_interest"] = domain
st.info(t("home_domain_info", domain=domain))

st.subheader(t("home_quick_links"))
a, b, c, d = st.columns(4)
a.page_link("pages/1_Fundamentos.py", label=t("home_ql_fund"), icon="📘")
b.page_link("pages/3_Matematica.py", label=t("home_ql_math"), icon="📐")
c.page_link("pages/5_Laboratorio.py", label=t("home_ql_lab"), icon="🔬")
d.page_link("pages/6_Evidencia.py", label=t("home_ql_ev"), icon="📑")

m1, m2, m3, m4 = st.columns(4)
m1.metric(t("home_m1"), "5")
m2.metric(t("home_m2"), "3")
m3.metric(t("home_m3"), "N=10")
m4.metric(t("home_m4"), "1.0.0")

with st.expander(t("home_about")):
    st.markdown(t("home_about_text"))
