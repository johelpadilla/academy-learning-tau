"""Lazy PDF download controls — never block page load on Pandoc."""

from __future__ import annotations

from typing import Callable

import streamlit as st

from stp.i18n.core import t


def lazy_pdf_download(
    handout_id: str,
    *,
    file_name: str,
    key: str,
    label: str | None = None,
    render_pdf: Callable[[str], bytes | None] | None = None,
) -> None:
    """Two-step PDF: prepare on click, then download from session cache.

    Streamlit ``download_button`` needs bytes at render time. Generating every
    PDF on each page load freezes Materiales/Docencia when Pandoc is installed.
    """
    if render_pdf is None:
        from stp.education.handouts import render_handout_pdf_bytes

        render_pdf = render_handout_pdf_bytes

    cache_key = f"stp_pdf_cache::{handout_id}"
    btn_label = label if label is not None else t("materiales.download_pdf")
    cached = st.session_state.get(cache_key)

    if cached:
        st.download_button(
            btn_label,
            data=cached,
            file_name=file_name,
            mime="application/pdf",
            key=f"dl_pdf_{key}",
            width="stretch",
        )
        return

    if st.button(
        t("materiales.prepare_pdf"),
        key=f"prep_pdf_{key}",
        width="stretch",
    ):
        with st.spinner(t("materiales.preparing_pdf")):
            try:
                pdf = render_pdf(handout_id)
            except Exception as exc:  # pragma: no cover — pandoc/env failures
                st.error(t("materiales.gen_error", err=exc))
                return
        if pdf:
            st.session_state[cache_key] = pdf
            st.rerun()
        else:
            st.warning(t("materiales.pdf_failed"))
