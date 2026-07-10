"""Domain voice packs: jargon-aware dual reading and locale parity."""

from __future__ import annotations

import json

import pytest

from stp.config.settings import DOMAIN_PRESETS
from stp.core.interpretation import interpret_dual_reading, methods_paragraph
from stp.config.settings import AnalysisParams
from stp.domains.voice import (
    VOICE_DOMAINS,
    VOICE_FIELDS,
    domain_gloss_bundle,
    has_voice,
    normalize_domain,
    render_domain_voice_markdown,
    voice_t,
)
from stp.i18n.core import SUPPORTED_LANGS, clear_catalog_cache, locales_dir, set_lang, t


@pytest.fixture(autouse=True)
def _reset_lang():
    clear_catalog_cache()
    set_lang("es")
    yield
    set_lang("es")
    clear_catalog_cache()


def test_voice_domains_cover_presets():
    for d in DOMAIN_PRESETS:
        assert d in VOICE_DOMAINS
    assert "generic" in VOICE_DOMAINS


def test_normalize_domain_aliases():
    assert normalize_domain("cardio") == "cardiology"
    assert normalize_domain("EEG") == "neuroscience"
    assert normalize_domain("unknown_xyz") == "generic"


def test_voice_fields_present_all_langs():
    for lang in SUPPORTED_LANGS:
        data = json.loads((locales_dir() / lang / "ui.json").read_text(encoding="utf-8"))
        dv = data["domain_voice"]
        for domain in VOICE_DOMAINS:
            assert domain in dv, f"{lang} missing {domain}"
            for field in VOICE_FIELDS:
                assert field in dv[domain], f"{lang}.{domain} missing {field}"
                assert isinstance(dv[domain][field], str) and dv[domain][field].strip()


def test_cardio_voice_differs_from_generic_es():
    set_lang("es")
    cardio = interpret_dual_reading(
        {"delta_tau_s": 0.06, "delta_excess3": 0.04, "mean_excess3": 0.12},
        {"tau_s": {"p_value": 0.01}},
        event_index=200,
        domain="cardiology",
        lang="es",
    )
    generic = interpret_dual_reading(
        {"delta_tau_s": 0.06, "delta_excess3": 0.04, "mean_excess3": 0.12},
        {"tau_s": {"p_value": 0.01}},
        event_index=200,
        domain="generic",
        lang="es",
    )
    assert "RR" in cardio["summary"] or "RR" in cardio["bullets"][0]
    assert cardio["summary"] != generic["summary"]
    assert "domain_voice" in cardio["flags"]
    assert cardio["voice"]["tau_gloss"]
    assert "SDNN" in cardio["voice"]["tau_gloss"] or "RR" in cardio["voice"]["tau_gloss"]


def test_epi_and_finance_voice_jargon():
    set_lang("es")
    epi = interpret_dual_reading(
        {"delta_tau_s": 0.05, "delta_excess3": 0.03, "mean_excess3": 0.1},
        None,
        event_index=50,
        domain="epidemiology",
        lang="es",
    )
    fin = interpret_dual_reading(
        {"delta_tau_s": 0.05, "delta_excess3": 0.03, "mean_excess3": 0.1},
        None,
        event_index=50,
        domain="finance",
        lang="es",
    )
    joined_e = " ".join([epi["summary"], *epi["bullets"]])
    joined_f = " ".join([fin["summary"], *fin["bullets"]])
    assert any(w in joined_e.lower() for w in ("brote", "incidencia", "vigilancia", "cases", "epi"))
    assert any(w in joined_f.lower() for w in ("mercado", "trading", "volatilidad", "régimen", "regimen"))
    assert "inversión" in joined_f or "trading" in joined_f or "ilustrativo" in joined_f


def test_voice_localizes_en_fr():
    metrics = {"delta_tau_s": 0.07, "delta_excess3": 0.05, "mean_excess3": 0.2}
    surr = {"tau_s": {"p_value": 0.02}}
    es = interpret_dual_reading(metrics, surr, 100, "cardiology", lang="es")
    en = interpret_dual_reading(metrics, surr, 100, "cardiology", lang="en")
    fr = interpret_dual_reading(metrics, surr, 100, "cardiology", lang="fr")
    assert es["summary"] != en["summary"]
    assert en["summary"] != fr["summary"]
    assert "clinical" in en["summary"].lower() or "VF" in en["summary"] or "RR" in en["bullets"][0]
    assert "clinique" in fr["summary"].lower() or "FV" in fr["summary"] or "RR" in fr["bullets"][0]


def test_methods_includes_domain_note():
    p = AnalysisParams(window=101, stride=5, n_surrogates=4)
    text = methods_paragraph(p, domain="cardiology", event_index=10, n=4, repro_hash="xyz", lang="es")
    assert "cardiology" in text
    assert "CCTP" in text or "RR" in text
    assert "xyz" in text


def test_gloss_bundle_and_markdown():
    set_lang("es")
    g = domain_gloss_bundle("ecology")
    assert "clorofila" in g["variables"].lower() or "fósforo" in g["variables"].lower() or "P" in g["variables"]
    md = render_domain_voice_markdown("ecology")
    assert "τ_s" in md or "tau" in md.lower()
    assert has_voice("ecology", "tau_gloss")
    assert voice_t("ecology", "lab_coach")
    # Never leak catalog keys to visitors
    assert "domain_voice." not in md
    assert "domain_voice_ui." not in md


def test_situated_example_is_human_readable():
    from stp.domains.voice import render_situated_example

    set_lang("es")
    text = render_situated_example("cardiology", "example_tau", "domain_voice_ui.example_tau_h")
    assert "domain_voice" not in text
    assert "Cardiolog" in text or "cardiolog" in text.lower() or "Dominio" in text
    assert "RR" in text or "latido" in text.lower()
    assert "diagnóstico" in text.lower() or "alarma" in text.lower() or "no" in text.lower()
    # Headers must be full phrases, not keys
    assert "example_tau_h" not in text


def test_voice_t_never_returns_raw_key():
    set_lang("es")
    missing = voice_t("cardiology", "field_that_does_not_exist_xyz")
    assert missing == "" or not missing.startswith("domain_voice.")


def test_ui_chrome_keys():
    for lang in SUPPORTED_LANGS:
        set_lang(lang)
        for key in (
            "domain_voice_ui.panel_header",
            "domain_voice_ui.example_tau_h",
            "domain_voice_ui.why_here",
            "domain_voice_ui.math_unchanged",
            "lab.domain_voice_panel",
            "fundamentos.domain_lens_header",
            "dominios.voice_header",
        ):
            val = t(key)
            assert val != key, f"{lang}: unresolved {key}"
