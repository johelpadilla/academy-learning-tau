"""Module quizzes, auto-scoring, and course-grade aggregation.

Question bank: ``content/learning/assessments.yaml`` (multilingual prompts).
Weights align with syllabus §6.1 (formatives 15% split across m1–m3;
cardio 30%; transfer 25%; portfolio quiz 30%).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

from stp.config.settings import CONTENT_DIR
from stp.i18n.core import get_lang

ASSESSMENTS_PATH = CONTENT_DIR / "learning" / "assessments.yaml"

# Syllabus §6.1 default weights (sum = 1.0)
DEFAULT_WEIGHTS: dict[str, float] = {
    "m1": 0.05,
    "m2": 0.05,
    "m3": 0.05,
    "m4": 0.30,
    "m5": 0.25,
    "m6": 0.30,
}

MODULE_ORDER: tuple[str, ...] = ("m1", "m2", "m3", "m4", "m5", "m6")


@dataclass
class Choice:
    id: str
    text: dict[str, str]


@dataclass
class Question:
    id: str
    type: str  # mcq
    points: float
    prompt: dict[str, str]
    choices: list[Choice]
    correct: str
    explanation: dict[str, str] = field(default_factory=dict)

    def localized_prompt(self, lang: str) -> str:
        return _pick(self.prompt, lang)

    def localized_choices(self, lang: str) -> list[tuple[str, str]]:
        return [(c.id, _pick(c.text, lang)) for c in self.choices]

    def localized_explanation(self, lang: str) -> str:
        return _pick(self.explanation, lang)


@dataclass
class ModuleAssessment:
    id: str
    week: int
    title: dict[str, str]
    description: dict[str, str]
    competencies: list[str]
    questions: list[Question]
    weight: float

    def localized_title(self, lang: str) -> str:
        return _pick(self.title, lang)

    def localized_description(self, lang: str) -> str:
        return _pick(self.description, lang)

    @property
    def max_score(self) -> float:
        return float(sum(q.points for q in self.questions))


@dataclass
class GradeResult:
    score: float
    max_score: float
    pct: float
    per_question: list[dict[str, Any]]
    passed: bool
    threshold_pct: float


@dataclass
class CourseGrade:
    module_best_pct: dict[str, float]
    weighted_pct: float | None
    completed_modules: list[str]
    missing_modules: list[str]
    weights: dict[str, float]
    ready: bool  # all weighted modules attempted


def _pick(d: dict[str, str] | None, lang: str) -> str:
    if not d:
        return ""
    lang = (lang or "es")[:2]
    for key in (lang, "es", "en", "fr"):
        if key in d and d[key]:
            return str(d[key])
    return next(iter(d.values()), "") if d else ""


def clear_assessment_cache() -> None:
    load_assessment_bank.cache_clear()


@lru_cache(maxsize=4)
def load_assessment_bank(path_str: str | None = None) -> dict[str, Any]:
    path = Path(path_str) if path_str else ASSESSMENTS_PATH
    if not path.exists():
        return {"modules": [], "pass_threshold_pct": 70, "weights": DEFAULT_WEIGHTS}
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return data if isinstance(data, dict) else {}


def _parse_module(raw: dict[str, Any], weights: dict[str, float]) -> ModuleAssessment:
    mid = str(raw["id"])
    questions: list[Question] = []
    for q in raw.get("questions") or []:
        choices = [
            Choice(id=str(c["id"]), text=dict(c.get("text") or {}))
            for c in (q.get("choices") or [])
        ]
        questions.append(
            Question(
                id=str(q["id"]),
                type=str(q.get("type") or "mcq"),
                points=float(q.get("points") or 1),
                prompt=dict(q.get("prompt") or {}),
                choices=choices,
                correct=str(q.get("correct") or ""),
                explanation=dict(q.get("explanation") or {}),
            )
        )
    return ModuleAssessment(
        id=mid,
        week=int(raw.get("week") or 0),
        title=dict(raw.get("title") or {}),
        description=dict(raw.get("description") or {}),
        competencies=[str(c) for c in (raw.get("competencies") or [])],
        questions=questions,
        weight=float(weights.get(mid, raw.get("weight") or 0.0)),
    )


def list_modules() -> list[ModuleAssessment]:
    bank = load_assessment_bank()
    weights = dict(DEFAULT_WEIGHTS)
    weights.update({str(k): float(v) for k, v in (bank.get("weights") or {}).items()})
    mods = [_parse_module(m, weights) for m in (bank.get("modules") or [])]
    order = {mid: i for i, mid in enumerate(MODULE_ORDER)}
    mods.sort(key=lambda m: (order.get(m.id, 99), m.week, m.id))
    return mods


def get_module(module_id: str) -> ModuleAssessment | None:
    mid = str(module_id)
    for m in list_modules():
        if m.id == mid:
            return m
    return None


def pass_threshold_pct() -> float:
    bank = load_assessment_bank()
    return float(bank.get("pass_threshold_pct") or 70)


def course_weights() -> dict[str, float]:
    bank = load_assessment_bank()
    w = dict(DEFAULT_WEIGHTS)
    w.update({str(k): float(v) for k, v in (bank.get("weights") or {}).items()})
    return w


def score_answers(
    module: ModuleAssessment,
    answers: dict[str, str],
    *,
    threshold_pct: float | None = None,
) -> GradeResult:
    """Auto-grade MCQ answers. ``answers`` maps question_id → choice_id."""
    thr = pass_threshold_pct() if threshold_pct is None else float(threshold_pct)
    per: list[dict[str, Any]] = []
    score = 0.0
    max_score = 0.0
    for q in module.questions:
        max_score += q.points
        given = str(answers.get(q.id, "") or "").strip()
        ok = given == q.correct
        if ok:
            score += q.points
        per.append(
            {
                "question_id": q.id,
                "correct": ok,
                "given": given,
                "expected": q.correct,
                "points": q.points if ok else 0.0,
                "max_points": q.points,
            }
        )
    pct = (100.0 * score / max_score) if max_score > 0 else 0.0
    return GradeResult(
        score=score,
        max_score=max_score,
        pct=round(pct, 2),
        per_question=per,
        passed=pct >= thr,
        threshold_pct=thr,
    )


def compute_course_grade(
    best_scores: dict[str, float],
    *,
    weights: dict[str, float] | None = None,
) -> CourseGrade:
    """Weighted average of best module percentages (0–100).

    Modules with no attempt are treated as missing; the weighted score uses
    only completed modules renormalized when not all are done, and
    ``ready`` is True only when every weighted module has a score.
    """
    w = dict(weights or course_weights())
    # only known modules
    w = {k: float(v) for k, v in w.items() if v > 0}
    completed: list[str] = []
    missing: list[str] = []
    module_best: dict[str, float] = {}
    for mid in MODULE_ORDER:
        if mid not in w:
            continue
        if mid in best_scores and best_scores[mid] is not None:
            module_best[mid] = float(best_scores[mid])
            completed.append(mid)
        else:
            missing.append(mid)

    if not completed:
        return CourseGrade(
            module_best_pct=module_best,
            weighted_pct=None,
            completed_modules=completed,
            missing_modules=missing,
            weights=w,
            ready=False,
        )

    # Full formula when all present; else provisional renormalized average
    if not missing:
        total_w = sum(w[m] for m in completed)
        weighted = sum(module_best[m] * w[m] for m in completed) / total_w
        ready = True
    else:
        total_w = sum(w[m] for m in completed)
        weighted = sum(module_best[m] * w[m] for m in completed) / total_w
        ready = False

    return CourseGrade(
        module_best_pct=module_best,
        weighted_pct=round(float(weighted), 2),
        completed_modules=completed,
        missing_modules=missing,
        weights=w,
        ready=ready,
    )


def attempt_payload(
    module: ModuleAssessment,
    result: GradeResult,
    answers: dict[str, str],
    *,
    lang: str | None = None,
) -> dict[str, Any]:
    from datetime import datetime, timezone

    return {
        "ts": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "module_id": module.id,
        "week": module.week,
        "score": result.score,
        "max_score": result.max_score,
        "pct": result.pct,
        "passed": result.passed,
        "threshold_pct": result.threshold_pct,
        "answers": dict(answers),
        "per_question": result.per_question,
        "lang": (lang or get_lang())[:2],
        "weight": module.weight,
    }


def module_summary_row(
    module: ModuleAssessment,
    best_pct: float | None,
    attempts: int,
    lang: str,
) -> dict[str, Any]:
    thr = pass_threshold_pct()
    status = "pending"
    if best_pct is not None:
        status = "passed" if best_pct >= thr else "failed"
    return {
        "id": module.id,
        "week": module.week,
        "title": module.localized_title(lang),
        "weight_pct": round(module.weight * 100, 1),
        "max_score": module.max_score,
        "n_questions": len(module.questions),
        "best_pct": best_pct,
        "attempts": attempts,
        "status": status,
        "competencies": module.competencies,
    }
