"""Six-week curriculum map: readings, Lab deep-links, quizzes, deliverables.

Used by Docencia and Ruta “Week N” views. Aligns with syllabus handout 08
and ``content/learning/assessments.yaml`` module ids m1–m6.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from stp.i18n.core import t


@dataclass(frozen=True)
class LabDeepLink:
    dataset: str
    domain: str
    label_key: str = "curriculum.lab_open"


@dataclass(frozen=True)
class WeekSpec:
    week: int
    module_id: str  # m1..m6
    weight: float
    title_key: str
    goals_keys: tuple[str, ...]
    reading_keys: tuple[str, ...]  # ui keys listing readings
    handout_ids: tuple[str, ...]
    lab: LabDeepLink
    deliverable_key: str
    quiz_note_key: str = "curriculum.quiz_note"


WEEKS: tuple[WeekSpec, ...] = (
    WeekSpec(
        week=1,
        module_id="m1",
        weight=0.05,
        title_key="curriculum.w1_title",
        goals_keys=("curriculum.w1_g1", "curriculum.w1_g2", "curriculum.w1_g3"),
        reading_keys=("curriculum.w1_r1", "curriculum.w1_r2", "curriculum.w1_r3"),
        handout_ids=("etica", "guia_rapida"),
        lab=LabDeepLink("synthetic_coupled_logistic", "synthetic", "curriculum.w1_lab"),
        deliverable_key="curriculum.w1_deliv",
    ),
    WeekSpec(
        week=2,
        module_id="m2",
        weight=0.05,
        title_key="curriculum.w2_title",
        goals_keys=("curriculum.w2_g1", "curriculum.w2_g2", "curriculum.w2_g3"),
        reading_keys=("curriculum.w2_r1", "curriculum.w2_r2", "curriculum.w2_r3"),
        handout_ids=("matematica", "teoria"),
        lab=LabDeepLink("synthetic_coupled_logistic", "synthetic", "curriculum.w2_lab"),
        deliverable_key="curriculum.w2_deliv",
    ),
    WeekSpec(
        week=3,
        module_id="m3",
        weight=0.05,
        title_key="curriculum.w3_title",
        goals_keys=("curriculum.w3_g1", "curriculum.w3_g2", "curriculum.w3_g3"),
        reading_keys=("curriculum.w3_r1", "curriculum.w3_r2", "curriculum.w3_r3"),
        handout_ids=("lectura_dual", "teoria", "cheatsheet"),
        lab=LabDeepLink("synthetic_coupled_logistic", "synthetic", "curriculum.w3_lab"),
        deliverable_key="curriculum.w3_deliv",
    ),
    WeekSpec(
        week=4,
        module_id="m4",
        weight=0.30,
        title_key="curriculum.w4_title",
        goals_keys=("curriculum.w4_g1", "curriculum.w4_g2", "curriculum.w4_g3"),
        reading_keys=("curriculum.w4_r1", "curriculum.w4_r2", "curriculum.w4_r3"),
        handout_ids=("checklist", "lectura_dual", "etica"),
        lab=LabDeepLink("sddb_rr_38_demo", "cardiology", "curriculum.w4_lab"),
        deliverable_key="curriculum.w4_deliv",
    ),
    WeekSpec(
        week=5,
        module_id="m5",
        weight=0.25,
        title_key="curriculum.w5_title",
        goals_keys=("curriculum.w5_g1", "curriculum.w5_g2", "curriculum.w5_g3"),
        reading_keys=("curriculum.w5_r1", "curriculum.w5_r2", "curriculum.w5_r3"),
        handout_ids=("etica", "cheatsheet"),
        lab=LabDeepLink("dengue_like_demo", "epidemiology", "curriculum.w5_lab"),
        deliverable_key="curriculum.w5_deliv",
    ),
    WeekSpec(
        week=6,
        module_id="m6",
        weight=0.30,
        title_key="curriculum.w6_title",
        goals_keys=("curriculum.w6_g1", "curriculum.w6_g2", "curriculum.w6_g3"),
        reading_keys=("curriculum.w6_r1", "curriculum.w6_r2", "curriculum.w6_r3"),
        handout_ids=("etica", "extensiones", "checklist", "syllabus"),
        lab=LabDeepLink("sddb_rr_38_demo", "cardiology", "curriculum.w6_lab"),
        deliverable_key="curriculum.w6_deliv",
    ),
)


def list_weeks() -> list[WeekSpec]:
    return list(WEEKS)


def get_week(n: int) -> WeekSpec | None:
    for w in WEEKS:
        if w.week == n:
            return w
    return None


def get_week_by_module(module_id: str) -> WeekSpec | None:
    for w in WEEKS:
        if w.module_id == module_id:
            return w
    return None


# ---------------------------------------------------------------------------
# Lab report rubric 0–2 × 6 = 12 (syllabus §6.2)
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class RubricCriterion:
    id: str
    title_key: str
    l0_key: str
    l1_key: str
    l2_key: str


RUBRIC_CRITERIA: tuple[RubricCriterion, ...] = (
    RubricCriterion(
        "scientific_q",
        "rubric.c1_title",
        "rubric.c1_0",
        "rubric.c1_1",
        "rubric.c1_2",
    ),
    RubricCriterion(
        "params",
        "rubric.c2_title",
        "rubric.c2_0",
        "rubric.c2_1",
        "rubric.c2_2",
    ),
    RubricCriterion(
        "core_metrics",
        "rubric.c3_title",
        "rubric.c3_0",
        "rubric.c3_1",
        "rubric.c3_2",
    ),
    RubricCriterion(
        "ews_parallel",
        "rubric.c4_title",
        "rubric.c4_0",
        "rubric.c4_1",
        "rubric.c4_2",
    ),
    RubricCriterion(
        "bounded_claim",
        "rubric.c5_title",
        "rubric.c5_0",
        "rubric.c5_1",
        "rubric.c5_2",
    ),
    RubricCriterion(
        "repro",
        "rubric.c6_title",
        "rubric.c6_0",
        "rubric.c6_1",
        "rubric.c6_2",
    ),
)

RUBRIC_PASS = 9
RUBRIC_EXCELLENT = 11
RUBRIC_MAX = 12


def score_rubric(scores: dict[str, int]) -> dict[str, Any]:
    """scores: criterion_id -> 0|1|2."""
    total = 0
    detail: list[dict[str, Any]] = []
    for c in RUBRIC_CRITERIA:
        s = int(scores.get(c.id, 0))
        s = max(0, min(2, s))
        total += s
        detail.append({"id": c.id, "score": s, "title": t(c.title_key)})
    return {
        "total": total,
        "max": RUBRIC_MAX,
        "passed": total >= RUBRIC_PASS,
        "excellent": total >= RUBRIC_EXCELLENT,
        "detail": detail,
    }


def export_rubric_markdown(
    scores: dict[str, int],
    *,
    student: str = "",
    notes: str = "",
    lang: str | None = None,
) -> str:
    """Export filled 0–2 rubric as Markdown for LMS upload."""
    result = score_rubric(scores)
    lines = [
        f"# {t('rubric.export_title', lang=lang)}",
        "",
        f"**{t('rubric.export_student', lang=lang)}:** {student or '—'}",
        f"**{t('rubric.export_total', lang=lang)}:** {result['total']} / {result['max']}",
        f"**{t('rubric.export_status', lang=lang)}:** "
        + (
            t("rubric.status_excellent", lang=lang)
            if result["excellent"]
            else (
                t("rubric.status_pass", lang=lang)
                if result["passed"]
                else t("rubric.status_fail", lang=lang)
            )
        ),
        f"**{t('rubric.export_threshold', lang=lang)}:** ≥ {RUBRIC_PASS} / {RUBRIC_MAX}",
        "",
        "| # | " + t("rubric.col_criterion", lang=lang) + " | 0 | 1 | 2 | "
        + t("rubric.col_score", lang=lang)
        + " |",
        "|---:|---|:-:|:-:|:-:|:-:|",
    ]
    for i, c in enumerate(RUBRIC_CRITERIA, 1):
        s = int(scores.get(c.id, 0))
        s = max(0, min(2, s))
        marks = [" ", " ", " "]
        marks[s] = "✓"
        lines.append(
            f"| {i} | {t(c.title_key, lang=lang)} | {marks[0]} | {marks[1]} | {marks[2]} | **{s}** |"
        )
    lines.append("")
    lines.append(f"## {t('rubric.export_descriptors', lang=lang)}")
    lines.append("")
    for c in RUBRIC_CRITERIA:
        lines.append(f"### {t(c.title_key, lang=lang)}")
        lines.append(f"- **0:** {t(c.l0_key, lang=lang)}")
        lines.append(f"- **1:** {t(c.l1_key, lang=lang)}")
        lines.append(f"- **2:** {t(c.l2_key, lang=lang)}")
        lines.append("")
    if notes.strip():
        lines.append(f"## {t('rubric.export_notes', lang=lang)}")
        lines.append("")
        lines.append(notes.strip())
        lines.append("")
    lines.append(f"*{t('rubric.export_footer', lang=lang)}*")
    lines.append("")
    return "\n".join(lines)
