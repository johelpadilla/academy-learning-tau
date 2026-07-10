"""Domain adapters (cardiology, epidemiology, ...) and domain voice pedagogy."""

from stp.domains.adapters import (
    ADAPTERS,
    domain_hint,
    domain_label,
    estimate_runtime_seconds,
    get_adapter,
)
from stp.domains.base import DomainAdapter, DomainBundle
from stp.domains.voice import (
    VOICE_DOMAINS,
    VOICE_FIELDS,
    domain_gloss_bundle,
    normalize_domain,
    render_domain_voice_markdown,
    voice_t,
)

__all__ = [
    "ADAPTERS",
    "DomainAdapter",
    "DomainBundle",
    "VOICE_DOMAINS",
    "VOICE_FIELDS",
    "domain_gloss_bundle",
    "domain_hint",
    "domain_label",
    "estimate_runtime_seconds",
    "get_adapter",
    "normalize_domain",
    "render_domain_voice_markdown",
    "voice_t",
]
