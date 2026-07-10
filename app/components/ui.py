"""Shared Streamlit UI helpers — design system for Systemic Tau Platform."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import streamlit as st

from stp.i18n.core import LANG_LABELS, SUPPORTED_LANGS, get_lang, set_lang, t


def page_link(
    page: str,
    label: str,
    *,
    icon: str | None = None,
    query_params: dict[str, Any] | None = None,
    **kwargs: Any,
) -> None:
    """Multipage link that never crashes outside a full multipage session.

    Streamlit's ``page_link`` raises ``KeyError: url_pathname`` when a page
    is executed in isolation (AppTest, direct script). Fall back to caption.
    """
    try:
        link_kwargs: dict[str, Any] = dict(kwargs)
        if icon:
            link_kwargs["icon"] = icon
        if query_params:
            link_kwargs["query_params"] = query_params
        st.page_link(page, label=label, **link_kwargs)
    except (KeyError, Exception):
        prefix = f"{icon} " if icon else ""
        extra = ""
        if query_params:
            qs = "&".join(f"{k}={v}" for k, v in query_params.items())
            extra = f" · `{page}?{qs}`"
        st.caption(f"{prefix}{label}{extra}")


def inject_css() -> None:
    """Inject design-system CSS once per page render."""
    css_path = Path(__file__).resolve().parents[1] / "assets" / "css" / "custom.css"
    if css_path.exists():
        st.markdown(
            f"<style>{css_path.read_text(encoding='utf-8')}</style>",
            unsafe_allow_html=True,
        )


def language_selector() -> str:
    """Sidebar language control. Spanish is the source language."""
    current = get_lang()
    labels = [f"{LANG_LABELS[c]} ({c})" for c in SUPPORTED_LANGS]
    idx = list(SUPPORTED_LANGS).index(current) if current in SUPPORTED_LANGS else 0
    choice = st.sidebar.selectbox(
        t("lang.label"),
        options=list(range(len(SUPPORTED_LANGS))),
        format_func=lambda i: labels[i],
        index=idx,
        key="stp_lang_select",
        help=t("lang.help"),
    )
    lang = SUPPORTED_LANGS[int(choice)]
    if lang != current:
        set_lang(lang)
        st.rerun()
    set_lang(lang)
    return lang


# Multipage nav: 4 role-based sections (not a flat 11-item list).
# Icons: emoji only in sidebar chrome (Streamlit page_link); feature cards use
# geometric marks elsewhere so blocks never mix systems.
_SIDEBAR_SECTIONS: tuple[tuple[str, tuple[tuple[str, str, str], ...]], ...] = (
    (
        "nav.section_learn",
        (
            ("Home.py", "nav.home", "🏠"),
            ("pages/1_Fundamentos.py", "nav.fundamentos", "📘"),
            ("pages/2_Matematica.py", "nav.matematica", "📐"),
            ("pages/5_Ruta_Aprendizaje.py", "nav.ruta", "🗺️"),
            ("pages/9_Evaluaciones.py", "nav.evaluaciones", "✅"),
        ),
    ),
    (
        "nav.section_do",
        (
            ("pages/3_Dominios.py", "nav.dominios", "🌐"),
            ("pages/4_Laboratorio.py", "nav.laboratorio", "🔬"),
        ),
    ),
    (
        "nav.section_evidence",
        (
            ("pages/6_Evidencia.py", "nav.evidencia", "📑"),
            ("pages/10_Biblioteca.py", "nav.biblioteca", "📚"),
        ),
    ),
    (
        "nav.section_teach",
        (
            ("pages/7_Docencia.py", "nav.docencia", "🎓"),
            ("pages/8_Materiales.py", "nav.materiales", "📦"),
        ),
    ),
)


def sidebar_nav() -> None:
    """Translated multipage menu grouped into Learn / Do / Evidence / Teach."""
    for section_key, pages in _SIDEBAR_SECTIONS:
        st.sidebar.markdown(
            f'<div class="stp-sidebar-section">{t(section_key)}</div>',
            unsafe_allow_html=True,
        )
        for page, label_key, icon in pages:
            label = t(label_key)
            try:
                st.sidebar.page_link(page, label=label, icon=icon)
            except (KeyError, Exception):
                # AppTest / isolated page execution
                st.sidebar.caption(f"{icon} {label}")


def sidebar_brand() -> None:
    """Brand + language + translated page menu in the sidebar."""
    name = t("common.brand_name")
    sub = t("common.brand_sub")
    st.sidebar.markdown(
        f"""
        <div class="stp-sidebar-brand">
          <div class="logo">
            <div class="mark">τ</div>
            <div>
              <div class="name">{name}</div>
              <div class="sub">{sub}</div>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    language_selector()
    sidebar_nav()
    try:
        from components.auth import render_auth_sidebar

        render_auth_sidebar()
    except Exception:
        # Auth module optional during early boot / isolated tests
        pass


def _mount_auth_topbar() -> None:
    """Login chip in the top-right of the main pane (all pages)."""
    try:
        from components.auth import render_auth_topbar

        render_auth_topbar()
    except Exception:
        pass


def render_hero(
    title: str = "Systemic Tau Platform",
    tagline: str = "Paradigma Tau Sistémico: de la teoría a la práctica",
    badge: str = "v1.0 · Educational & Research",
    description: str | None = None,
    meta_badges: list[str] | None = None,
) -> None:
    inject_css()
    sidebar_brand()
    _mount_auth_topbar()
    desc = description or (
        "Plataforma premium para fundamentos, matemática, dominios y laboratorio "
        "interactivo de Tau Sistémica + RECD (Φ₁–Φ₃, excess3)."
    )
    badges = meta_badges or [
        t("home.badge_core"),
        t("home.badge_cctp"),
        t("home.badge_surr"),
        t("home.badge_domains"),
    ]
    meta_html = "".join(
        f'<span class="stp-badge{" stp-badge-solid" if i == 0 else ""}">{b}</span>'
        for i, b in enumerate(badges)
    )
    st.markdown(
        f"""
        <div class="stp-hero">
          <div class="stp-badge">{badge}</div>
          <h1>{title}</h1>
          <p class="tagline">{tagline}</p>
          <p class="desc">{desc}</p>
          <div class="stp-hero-meta">
            {meta_html}
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def page_header(
    title: str,
    subtitle: str = "",
    eyebrow: str = "",
    icon: str = "",
) -> None:
    """Consistent page title block used across multipage app."""
    inject_css()
    sidebar_brand()
    _mount_auth_topbar()
    eye = f"{icon} {eyebrow}".strip() if icon or eyebrow else ""
    eye_html = f'<div class="eyebrow">{eye}</div>' if eye else ""
    sub_html = f'<p class="subtitle">{subtitle}</p>' if subtitle else ""
    st.markdown(
        f"""
        <div class="stp-page-header">
          {eye_html}
          <h1>{title}</h1>
          {sub_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def section_header(title: str, number: str | int | None = None) -> None:
    num_html = f'<span class="stp-section-num">{number}</span>' if number is not None else ""
    st.markdown(
        f"""
        <div class="stp-section">
          {num_html}
          <h2>{title}</h2>
          <div class="line"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def feature_card(title: str, body: str, icon: str = "", accent: str = "teal") -> str:
    icon_html = f'<span class="icon">{icon}</span>' if icon else ""
    return f"""
    <div class="stp-card stp-card-accent {accent}">
      {icon_html}
      <h3>{title}</h3>
      <p class="stp-muted">{body}</p>
    </div>
    """


def nav_card(title: str, body: str, icon: str = "◉") -> str:
    return f"""
    <div class="stp-nav-card">
      <div class="icon">{icon}</div>
      <h3>{title}</h3>
      <p class="stp-muted">{body}</p>
    </div>
    """


def action_card(title: str, body: str, icon: str = "◉", accent: str = "teal") -> str:
    """Visual face of a primary door (Study / Analyze / Teach). Geometric icons only."""
    return f"""
    <div class="stp-action-card stp-action-card--{accent}">
      <div class="mark">{icon}</div>
      <h3>{title}</h3>
      <p class="stp-muted">{body}</p>
    </div>
    """


def link_action_card(
    page: str,
    title: str,
    body: str,
    *,
    icon: str = "◉",
    accent: str = "teal",
    cta: str | None = None,
) -> None:
    """Primary door: visual card + full-width page_link as one control."""
    label = cta if cta is not None else t("home.start_open")
    # Marker class on a zero-height anchor so CSS can style the following page_link
    st.markdown(
        f"""
        <div class="stp-action-card-wrap" data-accent="{accent}">
          {action_card(title, body, icon=icon, accent=accent)}
        </div>
        """,
        unsafe_allow_html=True,
    )
    try:
        st.page_link(page, label=f"→  {label}")
    except (KeyError, Exception):
        st.caption(f"→ {label} · `{page}`")


def verdict_panel(
    title: str,
    summary: str,
    metrics: list[tuple[str, str]],
    *,
    caution: str = "",
) -> None:
    """Lab run verdict: one glance before detail tabs."""
    cells = "".join(
        f'<div class="stp-verdict-metric"><div class="val">{v}</div><div class="lbl">{l}</div></div>'
        for l, v in metrics
    )
    caution_html = (
        f'<p class="stp-verdict-caution">{caution}</p>' if caution else ""
    )
    st.markdown(
        f"""
        <div class="stp-verdict">
          <div class="stp-verdict-kicker">{t("lab.verdict_header")}</div>
          <h3>{title}</h3>
          <p class="stp-verdict-summary">{summary}</p>
          <div class="stp-verdict-metrics">{cells}</div>
          {caution_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def metrics_strip(items: list[tuple[str, str]]) -> None:
    """items: list of (value, label)."""
    cells = "".join(
        f'<div class="stp-metric"><div class="val">{v}</div><div class="lbl">{l}</div></div>'
        for v, l in items
    )
    st.markdown(f'<div class="stp-metrics">{cells}</div>', unsafe_allow_html=True)


def callout(text: str) -> None:
    st.markdown(f'<div class="stp-callout">{text}</div>', unsafe_allow_html=True)


def learning_goals(items: list[str], title: str | None = None) -> None:
    """Pedagogical goals box at the top of a page/section."""
    title = title if title is not None else t("common.learning_goals")
    lis = "".join(f"<li>{item}</li>" for item in items)
    st.markdown(
        f"""
        <div class="stp-learn">
          <div class="title">{title}</div>
          <ul>{lis}</ul>
        </div>
        """,
        unsafe_allow_html=True,
    )


def tip(text: str, label: str | None = None) -> None:
    """Inline note. Prefer scientific labels (Nota, Alcance, Interpretación).

    Avoid teacher-facing metalanguage (\"Para el aula\", \"Honestidad pedagógica\",
    \"Enseñe…\") — write the claim itself, not instructions about how to teach it.
    """
    label = label if label is not None else t("common.note")
    st.markdown(
        f'<div class="stp-tip"><strong>{label}:</strong> {text}</div>',
        unsafe_allow_html=True,
    )


def achieve_card(title: str, body: str, status: str | None = None) -> str:
    status = status if status is not None else t("common.operational")
    low = status.lower()
    cls = "partial" if any(
        k in low
        for k in ("parcial", "partial", "partiel", "roadmap", "desarrollo", "extensión", "extension")
    ) else ""
    return f"""
    <div class="stp-achieve">
      <div class="status {cls}">{status}</div>
      <h4>{title}</h4>
      <p>{body}</p>
    </div>
    """


def interpret_box(title: str, steps: list[str]) -> None:
    lis = "".join(f"<li>{s}</li>" for s in steps)
    st.markdown(
        f"""
        <div class="stp-interpret">
          <h4>{title}</h4>
          <ol>{lis}</ol>
        </div>
        """,
        unsafe_allow_html=True,
    )


def empty_state(message: str, icon: str = "📂") -> None:
    st.markdown(
        f"""
        <div class="stp-empty">
          <div class="icon">{icon}</div>
          <div>{message}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def footer() -> None:
    """Institutional footer strip (shared by all pages)."""
    st.markdown(
        f'<div class="stp-footer">{t("common.footer")}</div>',
        unsafe_allow_html=True,
    )


def lab_stepper(active: int = 1, has_data: bool = False, has_result: bool = False) -> None:
    """Visual progress for Lab: 1 Data · 2 Parameters · 3 Run · 4 Results."""
    labels = [
        t("lab.step_data"),
        t("lab.step_params"),
        t("lab.step_run"),
        t("lab.step_results"),
    ]
    chips = []
    for i, label in enumerate(labels, start=1):
        if i == active:
            cls = "active"
        elif i < active or (i == 1 and has_data) or (i == 4 and has_result):
            cls = "done"
        else:
            cls = ""
        chips.append(
            f'<span class="stp-step-chip {cls}"><span class="n">{i}</span>{label}</span>'
        )
    st.markdown(f'<div class="stp-steps">{"".join(chips)}</div>', unsafe_allow_html=True)
