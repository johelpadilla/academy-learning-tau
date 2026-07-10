"""Module quizzes, auto-grading, and local student accounts."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from stp.education import accounts as acc
from stp.education.assessments import (
    clear_assessment_cache,
    compute_course_grade,
    course_weights,
    get_module,
    list_modules,
    score_answers,
)


@pytest.fixture(autouse=True)
def _isolated_records(tmp_path, monkeypatch):
    """Point student records at a temp directory for every test."""
    records = tmp_path / "student_records"
    records.mkdir()
    monkeypatch.setattr(acc, "RECORDS_DIR", records)
    monkeypatch.setattr(acc, "USERS_INDEX", records / "users_index.json")
    clear_assessment_cache()
    yield
    clear_assessment_cache()


def test_list_modules_six_weeks():
    mods = list_modules()
    assert len(mods) == 6
    assert [m.id for m in mods] == ["m1", "m2", "m3", "m4", "m5", "m6"]
    assert abs(sum(course_weights().values()) - 1.0) < 1e-6
    for m in mods:
        # Postgraduate bank: 8–10 items per module (v1.1+)
        assert len(m.questions) >= 8, m.id
        assert m.max_score >= 8
        assert m.localized_title("es")
        assert m.localized_title("en")
        assert m.localized_title("fr")
        for q in m.questions:
            assert q.correct in {c.id for c in q.choices}
            assert q.localized_prompt("es")
            assert q.localized_prompt("en")
            assert q.localized_prompt("fr")


def test_score_all_correct_and_all_wrong():
    m = get_module("m1")
    assert m is not None
    good = {q.id: q.correct for q in m.questions}
    bad = {
        q.id: next(c.id for c in q.choices if c.id != q.correct)
        for q in m.questions
    }
    r_ok = score_answers(m, good)
    r_bad = score_answers(m, bad)
    assert r_ok.pct == 100.0
    assert r_ok.passed
    assert r_ok.score == m.max_score
    assert r_bad.pct == 0.0
    assert not r_bad.passed
    assert all(x["correct"] for x in r_ok.per_question)
    assert not any(x["correct"] for x in r_bad.per_question)


def test_course_grade_weights():
    # only m4 at 100% → provisional weighted uses only completed weights
    g = compute_course_grade({"m4": 100.0})
    assert g.weighted_pct == 100.0
    assert not g.ready
    assert "m1" in g.missing_modules

    full = {mid: 80.0 for mid in ["m1", "m2", "m3", "m4", "m5", "m6"]}
    g2 = compute_course_grade(full)
    assert g2.ready
    assert g2.weighted_pct == 80.0

    # formatives low, summatives high
    mixed = {
        "m1": 60.0,
        "m2": 60.0,
        "m3": 60.0,
        "m4": 100.0,
        "m5": 100.0,
        "m6": 100.0,
    }
    g3 = compute_course_grade(mixed)
    # 0.15*60 + 0.85*100 = 9 + 85 = 94
    assert abs(g3.weighted_pct - 94.0) < 0.05


def test_create_login_progress(tmp_path):
    user, err = acc.create_account("alice@course.edu", "secret1", display_name="Alice")
    assert err is None and user is not None
    assert user.username == "alice@course.edu"

    # duplicate
    _, err2 = acc.create_account("alice@course.edu", "other12")
    assert err2 == "username_taken"

    bad, err3 = acc.authenticate("alice@course.edu", "wrongpassword")
    assert bad is None and err3 == "invalid_credentials"

    ok, err4 = acc.authenticate("alice@course.edu", "secret1")
    assert err4 is None and ok is not None
    assert ok.user_id == user.user_id

    prog = acc.load_progress(user.user_id)
    assert prog is not None
    assert prog.username == "alice@course.edu"

    m = get_module("m2")
    answers = {q.id: q.correct for q in m.questions}
    result = score_answers(m, answers)
    from stp.education.assessments import attempt_payload

    payload = attempt_payload(m, result, answers, lang="es")
    prog = acc.record_quiz_attempt(prog, m.id, payload)
    assert prog.best_scores["m2"] == 100.0
    assert len(prog.quiz_attempts["m2"]) == 1

    prog = acc.set_checklist_item(prog, "lp_basic_0", True)
    assert prog.checklist["lp_basic_0"] is True

    prog = acc.set_task(prog, "t_w4_report", "doing", note="draft")
    assert prog.tasks["t_w4_report"]["status"] == "doing"

    # persistence on disk
    path = acc._progress_path(user.user_id)
    assert path.exists()
    raw = json.loads(path.read_text(encoding="utf-8"))
    assert raw["best_scores"]["m2"] == 100.0
    assert any(e["action"] == "quiz_submit" for e in raw["activity_log"])


def test_password_validation():
    assert acc.validate_password("12345") == "password_short"
    assert acc.validate_username("ab") == "invalid_username"
    assert acc.validate_username("good_user") is None
