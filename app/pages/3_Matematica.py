from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "app"))

import math

import numpy as np
import streamlit as st

from components.hero import inject_css
from stp.core.ordinal import bandt_pompe_symbols
from stp.core.pipeline import run_analysis
from stp.config.settings import AnalysisParams
from stp.data.synthetic_generators import coupled_logistic
from stp.education.content_loader import read_markdown
from stp.visualization.series_plots import plot_recd_panel, plot_tau
from locales import t

st.set_page_config(page_title=f"{t('math_title')} | STP", page_icon="🌀", layout="wide")
inject_css()

st.title(t("math_title"))
st.markdown(read_markdown("matematica", "overview.md"))

st.subheader(t("math_sandbox"))
m = st.slider(t("math_m"), 2, 5, 3)
delay = st.slider(t("math_delay"), 1, 5, 1)
x = np.sin(np.linspace(0, 12, 200)) + 0.1 * np.random.default_rng(0).normal(size=200)
sym = bandt_pompe_symbols(x, m=m, delay=delay)
c1, c2 = st.columns(2)
with c1:
    st.line_chart(x)
    st.caption(t("math_demo_series"))
with c2:
    st.bar_chart(np.bincount(sym, minlength=math.factorial(m)))
    st.caption(t("math_hist", m_fact=math.factorial(m)))

st.subheader(t("math_demo"))
mode = st.radio(t("math_mode"), ["fast", "full"], horizontal=True, index=0)
if st.button(t("math_btn_demo"), type="primary"):
    X = coupled_logistic(T=600, coupling=0.2, switch_at=300, seed=7)
    params = AnalysisParams(window=51, stride=2, mode=mode, n_surrogates=4 if mode == "fast" else 20)
    with st.spinner(t("math_calc")):
        result = run_analysis(X, params)
    st.success(t("math_hash", hash=result.repro_hash[:16]))
    st.plotly_chart(plot_tau(result), width="stretch")
    st.plotly_chart(plot_recd_panel(result), width="stretch")
    st.json(result.metrics)

with st.expander(t("math_expander")):
    st.markdown(t("math_exp_text"))
