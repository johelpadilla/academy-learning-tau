"""Domain voice: domain-specific jargon and templates for Tau / RECD pedagogy.

Spanish is the source of truth in locales/*/ui.json under ``domain_voice.<domain>``.
Missing fields fall back to generic ``interp.*`` strings so the UI never crashes.

UI helpers never display raw catalog keys (e.g. ``domain_voice.cardiology.example_tau``);
visitors always see full sentences in the active language.
"""

from __future__ import annotations

from typing import Any

from stp.i18n.core import get_lang, is_unresolved_key, t

# Domains with full voice packs (must match DOMAIN_PRESETS + generic)
VOICE_DOMAINS: tuple[str, ...] = (
    "cardiology",
    "epidemiology",
    "neuroscience",
    "ecology",
    "finance",
    "climate",
    "social",
    "education",
    "physiology",
    "synthetic",
    "generic",
)

# Fields expected in each domain_voice pack (for tests / docs)
VOICE_FIELDS: tuple[str, ...] = (
    "variables",
    "event_name",
    "tau_gloss",
    "excess_gloss",
    "classic_gloss",
    "bullet_dtau",
    "bullet_excess",
    "event_on",
    "event_off",
    "summary_concord",
    "summary_quiet",
    "summary_mixed",
    "lab_coach",
    "example_tau",
    "example_dual",
    "example_recd",
    "jargon_note",
    "methods_note",
    "maturity_phrase",
)


def normalize_domain(domain: str | None) -> str:
    d = (domain or "generic").strip().lower()
    if d in VOICE_DOMAINS:
        return d
    if d in ("cardio", "cardiac"):
        return "cardiology"
    if d in ("epi", "epidemiology"):
        return "epidemiology"
    if d in ("neuro", "eeg"):
        return "neuroscience"
    if d in ("eco", "lake"):
        return "ecology"
    if d in ("fin", "markets"):
        return "finance"
    if d in ("sleep",):
        return "physiology"
    return "generic"


def voice_key(domain: str, field: str) -> str:
    return f"domain_voice.{normalize_domain(domain)}.{field}"


def voice_t(
    domain: str,
    field: str,
    *,
    lang: str | None = None,
    fallback: str | None = None,
    **kwargs: Any,
) -> str:
    """Translate a domain_voice field; optional explicit fallback string or key."""
    lang = lang or get_lang()
    key = voice_key(domain, field)
    val = t(key, lang=lang, **kwargs)
    if not is_unresolved_key(val, key):
        return val
    # try generic domain pack
    gkey = voice_key("generic", field)
    gval = t(gkey, lang=lang, **kwargs)
    if not is_unresolved_key(gval, gkey):
        return gval
    if fallback is not None:
        if fallback.startswith("interp.") or fallback.startswith("domain_"):
            fb = t(fallback, lang=lang, **kwargs)
            if not is_unresolved_key(fb, fallback):
                return fb
            return fallback if not fallback.startswith(("interp.", "domain_")) else ""
        return fallback
    # Never leak machine keys into student-facing UI
    return ""


def has_voice(domain: str, field: str = "tau_gloss", lang: str | None = None) -> bool:
    key = voice_key(domain, field)
    val = t(key, lang=lang or get_lang())
    return not is_unresolved_key(val, key)


def domain_label_safe(domain: str, lang: str | None = None) -> str:
    """Human domain name; never a raw key."""
    try:
        from stp.domains.adapters import domain_label

        return domain_label(domain)
    except Exception:
        return normalize_domain(domain)


def domain_gloss_bundle(domain: str, lang: str | None = None) -> dict[str, str]:
    """Glosses + labels for Lab / Fundamentos side panels."""
    lang = lang or get_lang()
    d = normalize_domain(domain)
    fields = (
        "variables",
        "event_name",
        "tau_gloss",
        "excess_gloss",
        "classic_gloss",
        "lab_coach",
        "example_tau",
        "example_dual",
        "example_recd",
        "jargon_note",
        "methods_note",
        "maturity_phrase",
    )
    return {f: voice_t(d, f, lang=lang) for f in fields}


def _ui(key: str, lang: str | None = None, **kwargs: Any) -> str:
    """domain_voice_ui string; empty if unresolved (caller supplies plain fallback)."""
    full = f"domain_voice_ui.{key}" if not key.startswith("domain_voice_ui.") else key
    val = t(full, lang=lang, **kwargs)
    if is_unresolved_key(val, full):
        return ""
    return val


def render_domain_voice_markdown(domain: str, lang: str | None = None) -> str:
    """Markdown block for Lab coach / Fundamentos domain lens (always human text)."""
    lang = lang or get_lang()
    g = domain_gloss_bundle(domain, lang=lang)
    label = domain_label_safe(domain, lang=lang)
    header = _ui("panel_header", lang) or "Cómo se habla de Tau en este dominio"
    vars_l = _ui("variables", lang) or "Variables típicas"
    event_l = _ui("event", lang) or "Evento / corte de interés"
    math_note = _ui("math_unchanged", lang) or (
        "La matemática de τ_s es la misma en todos los dominios; "
        "lo que cambia es qué variables y qué pregunta científica interpreta el número."
    )
    lines = [
        f"**{header} — {label}**",
        "",
        f"- **{vars_l}:** {g.get('variables') or '—'}",
        f"- **{event_l}:** {g.get('event_name') or '—'}",
        f"- **τ_s:** {g.get('tau_gloss') or '—'}",
        f"- **excess3:** {g.get('excess_gloss') or '—'}",
        f"- **EWS clásicas (var, AR1…):** {g.get('classic_gloss') or '—'}",
        "",
    ]
    if g.get("lab_coach"):
        lines.append(f"*{g['lab_coach']}*")
        lines.append("")
    if g.get("maturity_phrase"):
        lines.append(f"_{g['maturity_phrase']}_")
        lines.append("")
    lines.append(f"_{math_note}_")
    return "\n".join(lines)


def render_situated_example(
    domain: str,
    field: str,
    header_key: str,
    *,
    lang: str | None = None,
) -> str:
    """Full student-facing callout for Fundamentos tabs.

    Always returns readable markdown — never catalog keys like
    ``domain_voice_ui.example_tau_h`` or ``domain_voice.cardiology.example_tau``.
    """
    lang = lang or get_lang()
    label = domain_label_safe(domain, lang=lang)
    raw_header_key = (
        header_key
        if header_key.startswith("domain_voice_ui.")
        else f"domain_voice_ui.{header_key}"
    )
    header = t(raw_header_key, lang=lang)
    if is_unresolved_key(header, raw_header_key):
        # Plain fallbacks by field intent
        fallbacks = {
            "example_tau": "Qué mide τ_s en este dominio (en palabras simples)",
            "example_dual": "Cómo se lee un resultado aquí",
            "example_recd": "Qué aportan RECD y excess3 en este contexto",
            "classic_gloss": "Qué no basta mirar solo (señales clásicas)",
            "excess_gloss": "Qué aporta excess3 aquí",
            "jargon_note": "Vocabulario del campo",
        }
        header = fallbacks.get(field, "Ejemplo situado en este dominio")

    body = voice_t(domain, field, lang=lang)
    if not body:
        body = _ui("missing_body", lang, domain=label) or (
            f"No hay un ejemplo redactado para «{label}» en este idioma. "
            "Pruebe otro dominio o vuelva a cargar la página."
        )

    in_dom = _ui("in_domain", lang, domain=label) or f"Dominio de referencia: **{label}**"
    math_note = _ui("math_unchanged", lang) or (
        "La fórmula de τ_s no cambia entre dominios; cambia la interpretación."
    )
    why = _ui("why_here", lang) or (
        "Este recuadro traduce la idea abstracta del módulo a un ejemplo del dominio "
        "que eligió arriba. No es un diagnóstico ni un pronóstico automático."
    )

    return (
        f"**{header}**\n\n"
        f"{in_dom}\n\n"
        f"{why}\n\n"
        f"{body}\n\n"
        f"_{math_note}_"
    )
