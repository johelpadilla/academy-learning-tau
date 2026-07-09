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

st.set_page_config(page_title=f"{t('migr_title')} | STP", page_icon="🧠", layout="wide")

st.markdown(r"""
<style>
    .stp-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(0, 0, 0, 0.05);
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    }
    .gradient-text {
        background: linear-gradient(90deg, #1E3A8A, #00C6FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .quote-box {
        border-left: 5px solid #00C6FF;
        padding-left: 15px;
        color: #4B5563;
        font-style: italic;
        margin: 1.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

st.markdown(f"<h1 class='gradient-text'>{t('migr_title')}</h1>", unsafe_allow_html=True)

st.markdown(read_markdown("paradigma", "migracion.md"), unsafe_allow_html=True)
