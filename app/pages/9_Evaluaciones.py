"""Module evaluations, auto-grading, account and progress."""

from __future__ import annotations

import sys
from pathlib import Path

_APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_APP))
from components.bootstrap import ensure_stp_path  # noqa: E402

ROOT = ensure_stp_path(__file__)

import streamlit as st
from stp.education.accounts import record_quiz_attempt, set_task
from stp.education.assessments import (
    attempt_payload,
    compute_course_grade,
    get_module,
    list_modules,
    module_summary_row,
    pass_threshold_pct,
    score_answers,
)
from stp.i18n.core import get_lang, t

from components.auth import (
    activity_label,
    get_progress,
    is_logged_in,
    refresh_progress,
    render_login_register_forms,
    sync_checklist_from_session,
    update_progress,
)
from components.ui import callout, footer, learning_goals, page_header, page_link, section_header

st.set_page_config(page_title=t("eval.page_title"), page_icon="✅", layout="wide")

page_header(
    t("eval.title"),
    subtitle=t("eval.subtitle"),
    eyebrow=t("eval.eyebrow"),
    icon="✅",
)

learning_goals(
    [t("eval.goal_1"), t("eval.goal_2"), t("eval.goal_3")]
)

lang = get_lang()
thr = pass_threshold_pct()
modules = list_modules()

# —— Account ——
section_header(t("eval.account_header"))
callout(t("eval.account_callout"))
logged = render_login_register_forms()

if not logged:
    st.info(t("eval.login_required"))
    page_link("pages/7_Docencia.py", label=t("nav.syllabus_docencia"), icon="🎓")
    page_link("pages/5_Ruta_Aprendizaje.py", label=t("nav.learning_path"), icon="🗺️")
    footer()
    st.stop()

progress = get_progress()
if progress is None:
    st.error(t("eval.progress_missing"))
    footer()
    st.stop()

# Keep learning-path checkboxes in sync when student returns
progress = sync_checklist_from_session(progress)

# —— Course grade ——
section_header(t("eval.grade_header"))
course = compute_course_grade(progress.best_scores)
g1, g2, g3, g4 = st.columns(4)
with g1:
    if course.weighted_pct is None:
        st.metric(t("eval.metric_course"), "—")
    else:
        st.metric(
            t("eval.metric_course"),
            f"{course.weighted_pct:.1f}%",
            delta=t("eval.metric_provisional") if not course.ready else t("eval.metric_final"),
        )
with g2:
    st.metric(
        t("eval.metric_modules"),
        f"{len(course.completed_modules)}/{len(course.completed_modules) + len(course.missing_modules)}",
    )
with g3:
    st.metric(t("eval.metric_threshold"), f"{thr:.0f}%")
with g4:
    checklist_done = sum(1 for v in progress.checklist.values() if v)
    st.metric(t("eval.metric_checklist"), str(checklist_done))

if course.weighted_pct is not None:
    if course.ready:
        st.success(t("eval.grade_ready", pct=f"{course.weighted_pct:.1f}"))
    else:
        st.info(
            t(
                "eval.grade_provisional",
                pct=f"{course.weighted_pct:.1f}",
                missing=", ".join(course.missing_modules) or "—",
            )
        )
else:
    st.caption(t("eval.grade_empty"))

st.markdown(t("eval.weights_blurb"))

# Summary table
rows = []
for m in modules:
    best = progress.best_scores.get(m.id)
    n_att = len(progress.quiz_attempts.get(m.id) or [])
    rows.append(module_summary_row(m, best, n_att, lang))

import pandas as pd

df = pd.DataFrame(
    [
        {
            t("eval.col_week"): r["week"],
            t("eval.col_module"): r["title"],
            t("eval.col_weight"): f"{r['weight_pct']}%",
            t("eval.col_questions"): r["n_questions"],
            t("eval.col_best"): "—" if r["best_pct"] is None else f"{r['best_pct']:.1f}%",
            t("eval.col_attempts"): r["attempts"],
            t("eval.col_status"): t(f"eval.status_{r['status']}"),
        }
        for r in rows
    ]
)
st.dataframe(df, hide_index=True, width="stretch")

# —— Module exams ——
section_header(t("eval.modules_header"))
callout(t("eval.modules_callout", thr=f"{thr:.0f}"))

module_ids = [m.id for m in modules]
labels = {
    m.id: f"S{m.week} · {m.localized_title(lang)} ({m.weight * 100:.0f}%)" for m in modules
}
selected = st.selectbox(
    t("eval.select_module"),
    options=module_ids,
    format_func=lambda mid: labels.get(mid, mid),
    key="eval_module_select",
)
mod = get_module(selected)
if mod is None:
    st.warning(t("eval.module_missing"))
else:
    st.markdown(f"**{mod.localized_title(lang)}**")
    st.markdown(mod.localized_description(lang))
    if mod.competencies:
        st.caption(t("eval.competencies", codes=", ".join(mod.competencies)))

    best = progress.best_scores.get(mod.id)
    if best is not None:
        st.caption(t("eval.best_so_far", pct=f"{best:.1f}"))

    with st.form(f"quiz_form_{mod.id}"):
        answers: dict[str, str] = {}
        for i, q in enumerate(mod.questions, start=1):
            st.markdown(f"**{i}. {q.localized_prompt(lang)}**")
            choices = q.localized_choices(lang)
            # radio with empty default via index=None if supported
            opts = [c[0] for c in choices]
            fmt = {c[0]: c[1] for c in choices}
            choice = st.radio(
                label=f"q_{q.id}",
                options=opts,
                format_func=lambda cid, f=fmt: f.get(cid, cid),
                key=f"ans_{mod.id}_{q.id}",
                label_visibility="collapsed",
                horizontal=False,
            )
            answers[q.id] = choice or ""
            st.divider()

        submit = st.form_submit_button(t("eval.submit_quiz"), type="primary")

    if submit:
        result = score_answers(mod, answers)
        payload = attempt_payload(mod, result, answers, lang=lang)
        progress = record_quiz_attempt(progress, mod.id, payload)
        update_progress(progress)
        # store last result for feedback panel
        st.session_state["eval_last_result"] = {
            "module_id": mod.id,
            "pct": result.pct,
            "score": result.score,
            "max_score": result.max_score,
            "passed": result.passed,
            "per_question": result.per_question,
        }
        st.rerun()

    last = st.session_state.get("eval_last_result")
    if last and last.get("module_id") == mod.id:
        section_header(t("eval.feedback_header"))
        if last["passed"]:
            st.success(
                t(
                    "eval.result_pass",
                    score=f"{last['score']:.0f}",
                    max=f"{last['max_score']:.0f}",
                    pct=f"{last['pct']:.1f}",
                )
            )
        else:
            st.warning(
                t(
                    "eval.result_fail",
                    score=f"{last['score']:.0f}",
                    max=f"{last['max_score']:.0f}",
                    pct=f"{last['pct']:.1f}",
                    thr=f"{thr:.0f}",
                )
            )
        # per-question feedback with explanations
        for q in mod.questions:
            pq = next(
                (x for x in last["per_question"] if x["question_id"] == q.id),
                None,
            )
            if not pq:
                continue
            mark = "✅" if pq["correct"] else "❌"
            with st.expander(f"{mark} {q.localized_prompt(lang)[:80]}…"):
                if pq["correct"]:
                    st.markdown(t("eval.answer_correct"))
                else:
                    st.markdown(
                        t(
                            "eval.answer_wrong",
                            given=pq["given"] or "—",
                            expected=pq["expected"],
                        )
                    )
                exp = q.localized_explanation(lang)
                if exp:
                    st.markdown(f"*{exp}*")

        # refresh course grade after attempt
        progress = refresh_progress() or progress
        course = compute_course_grade(progress.best_scores)
        if course.weighted_pct is not None:
            st.info(
                t(
                    "eval.course_after",
                    pct=f"{course.weighted_pct:.1f}",
                    state=t("eval.metric_final") if course.ready else t("eval.metric_provisional"),
                )
            )

# —— Tasks (manual deliverables) ——
section_header(t("eval.tasks_header"))
st.markdown(t("eval.tasks_blurb"))
task_defs = [
    ("t_w1_essay", t("eval.task_w1")),
    ("t_w2_table", t("eval.task_w2")),
    ("t_w3_mini", t("eval.task_w3")),
    ("t_w4_report", t("eval.task_w4")),
    ("t_w5_transfer", t("eval.task_w5")),
    ("t_w6_portfolio", t("eval.task_w6")),
]
status_opts = ["todo", "doing", "done"]
for tid, label in task_defs:
    cur = (progress.tasks.get(tid) or {}).get("status", "todo")
    cols = st.columns([3, 1.2, 2])
    with cols[0]:
        st.markdown(f"**{label}**")
    with cols[1]:
        new_st = st.selectbox(
            label,
            options=status_opts,
            index=status_opts.index(cur) if cur in status_opts else 0,
            format_func=lambda s: t(f"eval.task_status_{s}"),
            key=f"task_st_{tid}",
            label_visibility="collapsed",
        )
    with cols[2]:
        note = st.text_input(
            t("eval.task_note"),
            value=(progress.tasks.get(tid) or {}).get("note", ""),
            key=f"task_note_{tid}",
            label_visibility="collapsed",
            placeholder=t("eval.task_note_ph"),
        )
    prev = progress.tasks.get(tid) or {}
    if new_st != prev.get("status") or note != prev.get("note", ""):
        progress = set_task(progress, tid, new_st, note=note)
        update_progress(progress)

# —— Activity log ——
section_header(t("eval.activity_header"))
log = list(reversed(progress.activity_log[-40:]))
if not log:
    st.caption(t("eval.activity_empty"))
else:
    for entry in log:
        action = activity_label(str(entry.get("action", "")))
        ts = str(entry.get("ts", ""))[:19]
        detail = entry.get("detail") or {}
        extra = ""
        if "module_id" in detail:
            extra = f" · {detail.get('module_id')}"
            if "pct" in detail:
                extra += f" · {detail['pct']}%"
        if "task_id" in detail:
            extra = f" · {detail.get('task_id')} → {detail.get('status', '')}"
        st.markdown(f"`{ts}` — **{action}**{extra}")

if st.button(t("eval.refresh_progress")):
    refresh_progress()
    st.rerun()

st.divider()
page_link("pages/5_Ruta_Aprendizaje.py", label=t("nav.learning_path"), icon="🗺️")
page_link("pages/7_Docencia.py", label=t("nav.syllabus_docencia"), icon="🎓")
page_link("pages/4_Laboratorio.py", label=t("nav.practice_lab"), icon="🔬")
footer()
