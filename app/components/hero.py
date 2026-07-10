"""Backward-compatible re-exports. Prefer: from components.ui import ..."""

from __future__ import annotations

from .ui import (  # noqa: F401
    action_card,
    callout,
    empty_state,
    feature_card,
    footer,
    inject_css,
    lab_stepper,
    link_action_card,
    metrics_strip,
    nav_card,
    page_header,
    render_hero,
    section_header,
    sidebar_brand,
    verdict_panel,
)

__all__ = [
    "action_card",
    "callout",
    "empty_state",
    "feature_card",
    "footer",
    "inject_css",
    "lab_stepper",
    "link_action_card",
    "metrics_strip",
    "nav_card",
    "page_header",
    "render_hero",
    "section_header",
    "sidebar_brand",
    "verdict_panel",
]
