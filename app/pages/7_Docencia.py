from __future__ import annotations

import sys
from pathlib import Path

_APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_APP))
from components.bootstrap import ensure_stp_path  # noqa: E402

ROOT = ensure_stp_path(__file__)

import streamlit as st
from stp.i18n.core import t

from components.bootstrap import import_ui
from components.pdf_ui import lazy_pdf_download

(
    page_link,
    callout,
    feature_card,
    footer,
    learning_goals,
    page_header,
    section_header,
) = import_ui(
    "page_link",
    "callout",
    "feature_card",
    "footer",
    "learning_goals",
    "page_header",
    "section_header",
)
from stp.education.curriculum import (
    RUBRIC_CRITERIA,
    RUBRIC_EXCELLENT,
    RUBRIC_MAX,
    RUBRIC_PASS,
    export_rubric_markdown,
    list_weeks,
    score_rubric,
)
from stp.education.handouts import get_handout, render_handout_bytes

try:
    from stp.education.handouts import pdf_available, render_handout_pdf_bytes
except ImportError:  # pragma: no cover — stale Streamlit module cache
    import importlib
    import sys as _sys

    for _name in list(_sys.modules):
        if _name == "stp.education.handouts" or _name.startswith(
            "stp.education.handouts."
        ):
            del _sys.modules[_name]
    importlib.invalidate_caches()
    from stp.education.handouts import pdf_available, render_handout_pdf_bytes  # type: ignore

st.set_page_config(page_title=t("docencia.page_title"), page_icon="🌀", layout="wide")

page_header(
    t("docencia.title_full"),
    subtitle=t("docencia.subtitle_full"),
    eyebrow=t("docencia.eyebrow_full"),
    icon="🎓",
)

learning_goals(
    [t("docencia.goal_1_full"), t("docencia.goal_2_full"), t("docencia.goal_3_full")]
)

tab_overview, tab_week, tab_rubric = st.tabs(
    [t("docencia.tab_overview"), t("docencia.tab_week"), t("docencia.tab_rubric")]
)

# ---------------------------------------------------------------------------
# Overview (legacy syllabus content)
# ---------------------------------------------------------------------------
with tab_overview:
    section_header(t("docencia.comp_header"))
    callout(t("docencia.comp_callout"))

    section_header(t("docencia.syl_header"))
    st.markdown(t("docencia.syl_table"), unsafe_allow_html=True)

    section_header(t("docencia.rubric_header"))
    st.markdown(t("docencia.rubric_body"))

    section_header(t("docencia.export_header"))
    d1, d2, d3 = st.columns(3)
    with d1:
        st.download_button(
            t("docencia.dl_syllabus"),
            data=render_handout_bytes("syllabus"),
            file_name="stp_08_syllabus_6_semanas.md",
            mime="text/markdown",
            type="primary",
            width="stretch",
        )
    with d2:
        st.download_button(
            t("docencia.dl_teacher"),
            data=render_handout_bytes("pack_docente"),
            file_name="stp_pack_docente.md",
            mime="text/markdown",
            width="stretch",
        )
    with d3:
        st.download_button(
            t("docencia.dl_student"),
            data=render_handout_bytes("pack_estudiante"),
            file_name="stp_pack_estudiante.md",
            mime="text/markdown",
            width="stretch",
        )

    if pdf_available():
        st.caption(t("materiales.pdf_ok"))
        p1, p2, p3 = st.columns(3)
        for col, hid, label_key, fname in (
            (p1, "syllabus", "docencia.dl_syllabus_pdf", "stp_08_syllabus_6_semanas.pdf"),
            (p2, "pack_docente", "docencia.dl_teacher_pdf", "stp_pack_docente.pdf"),
            (p3, "pack_estudiante", "docencia.dl_student_pdf", "stp_pack_estudiante.pdf"),
        ):
            with col:
                # Lazy: do not run Pandoc for 3 packs on every Docencia load
                lazy_pdf_download(
                    hid,
                    file_name=fname,
                    key=f"doc_{hid}",
                    label=t(label_key),
                    render_pdf=render_handout_pdf_bytes,
                )
    else:
        st.caption(t("materiales.pdf_unavailable"))

    page_link("pages/8_Materiales.py", label=t("nav.full_materials"), icon="📦")
    page_link("pages/9_Evaluaciones.py", label=t("nav.evaluaciones"), icon="✅")
    page_link(
        "pages/4_Laboratorio.py",
        label=t("docencia.open_week2"),
        icon="🔬",
        query_params={"dataset": "synthetic_coupled_logistic", "domain": "synthetic"},
    )

    section_header(t("docencia.mat_header"))
    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown(
            feature_card(
                t("docencia.card_md_t"),
                t("docencia.card_md_b"),
                icon="📝",
                accent="navy",
            ),
            unsafe_allow_html=True,
        )
    with m2:
        st.markdown(
            feature_card(
                t("docencia.card_lab_t"),
                t("docencia.card_lab_b"),
                icon="🔬",
                accent="teal",
            ),
            unsafe_allow_html=True,
        )
    with m3:
        st.markdown(
            feature_card(
                t("docencia.card_code_t"),
                t("docencia.card_code_b"),
                icon="⚙️",
                accent="purple",
            ),
            unsafe_allow_html=True,
        )

    section_header(t("docencia.lic_header"))
    st.markdown(t("docencia.lic_table"), unsafe_allow_html=True)

    section_header(t("docencia.nb_header"))
    notebooks = [
        ("01", "bandt_pompe_intro", t("docencia.nb_01")),
        ("02", "tau_s_sliding", t("docencia.nb_02")),
        ("03", "recd_levels_excess3", t("docencia.nb_03")),
        ("04", "cctp_record38", t("docencia.nb_04")),
        ("05", "surrogates_nulls", t("docencia.nb_05")),
    ]
    for num, slug, desc in notebooks:
        st.markdown(
            f"""
            <div class="stp-card" style="margin-bottom:0.5rem;padding:0.85rem 1.1rem;">
              <span class="stp-pill">NB {num}</span>
              <strong style="color:#1A2332;margin-left:0.35rem;">{slug}.ipynb</strong>
              <span class="stp-muted"> — {desc}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    callout(t("docencia.nb_note"))

# ---------------------------------------------------------------------------
# Week N view
# ---------------------------------------------------------------------------
with tab_week:
    section_header(t("curriculum.week_header"))
    weeks = list_weeks()
    labels = {w.week: f"S{w.week} · {t(w.title_key)}" for w in weeks}
    choice = st.selectbox(
        t("curriculum.week_select"),
        options=[w.week for w in weeks],
        format_func=lambda n: labels[n],
        key="docencia_week_select",
    )
    w = next(x for x in weeks if x.week == choice)

    st.markdown(f"### {t(w.title_key)}")
    st.caption(
        f"{t('curriculum.week_weight')}: **{w.weight * 100:.0f}%** · "
        f"module `{w.module_id}`"
    )

    section_header(t("curriculum.week_goals"))
    for gk in w.goals_keys:
        st.markdown(f"- {t(gk)}")

    section_header(t("curriculum.week_readings"))
    for rk in w.reading_keys:
        st.markdown(f"- {t(rk)}")

    section_header(t("curriculum.week_handouts"))
    hcols = st.columns(min(3, max(1, len(w.handout_ids))))
    for col, hid in zip(hcols, w.handout_ids):
        with col:
            try:
                h = get_handout(hid)
                st.markdown(f"**{h.title}**")
                st.download_button(
                    t("materiales.dl_short"),
                    data=render_handout_bytes(hid),
                    file_name=h.filename,
                    mime="text/markdown",
                    key=f"doc_week_h_{choice}_{hid}",
                    width="stretch",
                )
            except KeyError:
                st.caption(hid)

    section_header(t("curriculum.week_lab"))
    st.markdown(t(w.lab.label_key))
    page_link(
        "pages/4_Laboratorio.py",
        label=t("curriculum.week_lab"),
        icon="🔬",
        query_params={"dataset": w.lab.dataset, "domain": w.lab.domain},
    )

    section_header(t("curriculum.week_quiz"))
    callout(t(w.quiz_note_key))
    page_link("pages/9_Evaluaciones.py", label=t("curriculum.open_quiz"), icon="✅")

    section_header(t("curriculum.week_deliv"))
    st.markdown(t(w.deliverable_key))
    page_link("pages/8_Materiales.py", label=t("curriculum.open_materials"), icon="📦")

# ---------------------------------------------------------------------------
# Editable rubric
# ---------------------------------------------------------------------------
with tab_rubric:
    section_header(t("rubric.interactive_header"))
    callout(t("rubric.interactive_callout"))

    student = st.text_input(t("rubric.student_name"), key="rubric_student")
    scores: dict[str, int] = {}
    for c in RUBRIC_CRITERIA:
        with st.expander(t(c.title_key), expanded=True):
            st.caption(f"**0** — {t(c.l0_key)}")
            st.caption(f"**1** — {t(c.l1_key)}")
            st.caption(f"**2** — {t(c.l2_key)}")
            scores[c.id] = st.radio(
                t("rubric.score_label"),
                options=[0, 1, 2],
                horizontal=True,
                key=f"rubric_score_{c.id}",
            )

    notes = st.text_area(t("rubric.notes"), key="rubric_notes", height=100)
    result = score_rubric(scores)

    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric(t("rubric.total_metric"), f"{result['total']} / {RUBRIC_MAX}")
    with m2:
        if result["excellent"]:
            st.success(t("rubric.status_excellent"))
        elif result["passed"]:
            st.success(t("rubric.status_pass"))
        else:
            st.warning(t("rubric.status_fail"))
    with m3:
        st.caption(f"≥ {RUBRIC_PASS} · excellent ≥ {RUBRIC_EXCELLENT}")

    md = export_rubric_markdown(scores, student=student, notes=notes)
    st.download_button(
        t("rubric.export_md"),
        data=md.encode("utf-8"),
        file_name="stp_rubrica_lab.md",
        mime="text/markdown",
        type="primary",
        key="rubric_export_md",
    )
    if pdf_available():
        from stp.education.handouts import markdown_to_pdf

        # Cache by content so we never re-run Pandoc on every tab render
        cache_key = "stp_pdf_cache::rubric_export"
        content_key = "stp_pdf_cache::rubric_md"
        if (
            st.session_state.get(content_key) == md
            and st.session_state.get(cache_key)
        ):
            st.download_button(
                t("materiales.download_pdf"),
                data=st.session_state[cache_key],
                file_name="stp_rubrica_lab.pdf",
                mime="application/pdf",
                key="rubric_export_pdf",
            )
        elif st.button(
            t("materiales.prepare_pdf"),
            key="rubric_prep_pdf",
            width="stretch",
        ):
            with st.spinner(t("materiales.preparing_pdf")):
                pdf = markdown_to_pdf(md, title=t("rubric.export_title"))
            if pdf:
                st.session_state[cache_key] = pdf
                st.session_state[content_key] = md
                st.rerun()
            else:
                st.warning(t("materiales.pdf_failed"))

footer()
