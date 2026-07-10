from __future__ import annotations

import sys
from pathlib import Path

_APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_APP))
from components.bootstrap import ensure_stp_path  # noqa: E402

ROOT = ensure_stp_path(__file__)

import streamlit as st
from stp.i18n.core import t
from stp.domains import domain_gloss_bundle, domain_label, render_domain_voice_markdown

from components.ui import page_link, callout, footer, learning_goals, page_header, section_header
from stp.education.content_loader import read_markdown

st.set_page_config(page_title=t("dominios.page_title"), page_icon="🌀", layout="wide")

page_header(
    t("dominios.title"),
    subtitle=t("dominios.subtitle"),
    eyebrow=t("dominios.eyebrow"),
    icon="🌐",
)

learning_goals(
    [t("dominios.goal_1"), t("dominios.goal_2"), t("dominios.goal_3")]
)

domains = [
    {
        "name": "Cardiología",
        "key": "cardiology",
        "file": "cardiologia.md",
        "icon": "🫀",
        "maturity_key": "very_high",
        "maturity_cls": "high",
        "data_key": "cardiology",
        "lab_dataset": "sddb_rr_38_demo",
    },
    {
        "name": "Epidemiología",
        "key": "epidemiology",
        "file": "epidemiologia.md",
        "icon": "🦠",
        "maturity_key": "high",
        "maturity_cls": "high",
        "data_key": "epidemiology",
        "lab_dataset": "dengue_like_demo",
    },
    {
        "name": "Neurociencia",
        "key": "neuroscience",
        "file": "neurociencia.md",
        "icon": "🧠",
        "maturity_key": "med_high",
        "maturity_cls": "med",
        "data_key": "neuroscience",
        "lab_dataset": "eeg_like_demo",
    },
    {
        "name": "Ecología",
        "key": "ecology",
        "file": "ecologia.md",
        "icon": "🌿",
        "maturity_key": "med",
        "maturity_cls": "med",
        "data_key": "ecology",
        "lab_dataset": "ecology_like_demo",
    },
    {
        "name": "Clima e hidrología",
        "key": "climate",
        "file": "clima.md",
        "icon": "🏜️",
        "maturity_key": "med",
        "maturity_cls": "med",
        "data_key": "climate",
        "lab_dataset": "climate_drought_demo",
    },
    {
        "name": "Aprendizaje colectivo",
        "key": "education",
        "file": "educacion.md",
        "icon": "🎓",
        "maturity_key": "med",
        "maturity_cls": "med",
        "data_key": "education",
        "lab_dataset": "education_cohort_demo",
    },
    {
        "name": "Dinámica social",
        "key": "social",
        "file": "social.md",
        "icon": "🗣️",
        "maturity_key": "low_med",
        "maturity_cls": "low",
        "data_key": "social",
        "lab_dataset": "social_polarization_demo",
    },
    {
        "name": "Fisiología del sueño",
        "key": "physiology",
        "file": "fisiologia.md",
        "icon": "😴",
        "maturity_key": "med",
        "maturity_cls": "med",
        "data_key": "physiology",
        "lab_dataset": "sleep_fragmentation_demo",
    },
    {
        "name": "Finanzas",
        "key": "finance",
        "file": "finanzas.md",
        "icon": "📈",
        "maturity_key": "med",
        "maturity_cls": "low",
        "data_key": "finance",
        "lab_dataset": "finance_like_demo",
    },
]

# Localize names, blurbs, maturity labels, data source chips
for _d in domains:
    _d["name"] = domain_label(_d["key"])
    _bk = f"domain_blurbs.{_d['key']}"
    _bv = t(_bk)
    _d["blurb"] = _bv if _bv != _bk else _d.get("blurb", "")
    _mk = _d.get("maturity_key", "med")
    _d["maturity"] = t(f"maturity.{_mk}")
    _dk = f"domain_data.{_d.get('data_key', _d['key'])}"
    _dv = t(_dk)
    _d["data"] = _dv if _dv != _dk else _d.get("data", "")

section_header(t("dominios.map_header"))
st.markdown(t("dominios.map_intro"))
callout(t("dominios.anchor_callout"))
with st.expander(t("dominios.legend_header"), expanded=True):
    st.markdown(t("dominios.legend_body"))

# Two rows of domain cards
row1 = domains[:5]
row2 = domains[5:]
for row in (row1, row2):
    cols = st.columns(len(row))
    for col, d in zip(cols, row):
        with col:
            st.markdown(
                f"""
                <div class="stp-domain-card">
                  <div class="dom-icon">{d['icon']}</div>
                  <h3>{d['name']}</h3>
                  <span class="stp-pill {d['maturity_cls']}">{d['maturity']}</span>
                  <span class="stp-pill purple">{d['data']}</span>
                  <p class="stp-muted" style="margin-top:0.65rem;">{d['blurb']}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

section_header(t("dominios.synth_header"))
callout(t("dominios.synth_callout"))

section_header(t("dominios.detail_header"))
choice = st.selectbox(
    t("dominios.select"),
    [d["name"] for d in domains],
    format_func=lambda n: f"{next(d['icon'] for d in domains if d['name']==n)}  {n}",
)
selected = next(d for d in domains if d["name"] == choice)
callout(
    t(
        "dominios.ref_callout",
        data=selected["data"],
        maturity=selected["maturity"],
    )
)

with st.container():
    st.markdown(read_markdown("dominios", selected["file"]))

_sel_voice = domain_gloss_bundle(selected["key"])
section_header(t("dominios.voice_header"))
st.markdown(render_domain_voice_markdown(selected["key"]))
st.markdown(f"**{t('dominios.voice_jargon')}**")
st.info(_sel_voice.get("jargon_note", ""))
st.success(_sel_voice.get("example_dual", ""))

section_header(t("dominios.open_header"))
st.markdown(t("dominios.open_body", name=selected["name"]))
b1, b2 = st.columns(2)
with b1:
    page_link(
        "pages/4_Laboratorio.py",
        label=t("dominios.lab_preset", name=selected["name"]),
        icon="🔬",
        query_params={"domain": selected["key"], "dataset": selected["lab_dataset"]},
    )
with b2:
    page_link(
        "pages/4_Laboratorio.py",
        label=t("dominios.lab_empty"),
        icon="📂",
    )

page_link(
    "pages/4_Laboratorio.py",
    label=t("dominios.try_lab"),
    icon="🔬",
    query_params={"domain": selected["key"], "dataset": selected["lab_dataset"]},
)
page_link("pages/6_Evidencia.py", label=t("nav.evidence_cctp"), icon="📑")
footer()
