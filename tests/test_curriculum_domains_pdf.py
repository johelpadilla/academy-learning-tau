"""Curriculum week map, domain parity EN/FR, rubric export, optional PDF."""

from __future__ import annotations

from pathlib import Path

from stp.config.settings import CONTENT_DIR
from stp.education.content_loader import read_markdown
from stp.education.curriculum import (
    RUBRIC_CRITERIA,
    RUBRIC_MAX,
    RUBRIC_PASS,
    export_rubric_markdown,
    get_week,
    list_weeks,
    score_rubric,
)
from stp.education.handouts import markdown_to_pdf, pdf_available, render_handout


def test_six_weeks_map():
    weeks = list_weeks()
    assert len(weeks) == 6
    assert [w.week for w in weeks] == [1, 2, 3, 4, 5, 6]
    assert abs(sum(w.weight for w in weeks) - 1.0) < 1e-6
    w4 = get_week(4)
    assert w4 is not None
    assert w4.module_id == "m4"
    assert w4.lab.domain == "cardiology"
    assert w4.lab.dataset


def test_rubric_score_and_export():
    scores = {c.id: 2 for c in RUBRIC_CRITERIA}
    r = score_rubric(scores)
    assert r["total"] == RUBRIC_MAX
    assert r["passed"] and r["excellent"]

    low = {c.id: 1 for c in RUBRIC_CRITERIA}
    r2 = score_rubric(low)
    assert r2["total"] == 6
    assert not r2["passed"]
    assert r2["total"] < RUBRIC_PASS

    md = export_rubric_markdown(scores, student="Test Student", notes="ok")
    assert "12" in md
    assert "Test Student" in md
    assert "Pregunta" in md or "Scientific" in md or "Question" in md


def test_domain_parity_min_size_and_schema():
    """EN/FR domain cards must be postgraduate-depth, not stubs."""
    files = sorted((CONTENT_DIR / "dominios").glob("*.md"))
    assert len(files) >= 9
    for f in files:
        es = f.read_text(encoding="utf-8")
        assert len(es) > 1000, f.name
        assert "Proxy" in es or "proxy" in es.lower() or "Ficha de diseño" in es

        for lang in ("en", "fr"):
            body = read_markdown("dominios", f.name, lang=lang)
            assert len(body) > 1500, f"{lang}/{f.name} still stub-sized"
            # Uniform schema markers
            low = body.lower()
            assert "proxy" in low
            assert "preset" in low or "lab" in low
            # Allowed / forbidden claim discipline
            assert (
                "allowed" in low
                or "forbidden" in low
                or "autoris" in low
                or "interdit" in low
                or "permit" in low
                or "prohib" in low
            )


def test_pdf_pipeline_smoke():
    if not pdf_available():
        return
    pdf = markdown_to_pdf("# STP test\n\nHello **PDF**.\n", title="STP test")
    # May be None if LaTeX missing; when present must be PDF
    if pdf is not None:
        assert pdf.startswith(b"%PDF")
        assert len(pdf) > 500


def test_syllabus_handout_still_renders():
    text = render_handout("syllabus")
    assert len(text) > 3000
    assert "C1" in text or "competenc" in text.lower()
