"""Core analysis package.

Keep this ``__init__`` *lazy*: Streamlit multipage can import several
``stp.core.*`` modules concurrently. Eager imports of ``pipeline`` here
used to cause ``_DeadlockError`` on Community Cloud when one page failed
mid-import (e.g. missing ``scipy``) while others loaded.
"""

from __future__ import annotations

from typing import Any

__all__ = [
    "AnalysisResult",
    "run_analysis",
    "compute_tau_s",
    "compute_recd_from_conjunctions",
    "bandt_pompe_symbols",
    "multivariate_symbols",
]

_LAZY: dict[str, tuple[str, str]] = {
    "AnalysisResult": ("stp.core.pipeline", "AnalysisResult"),
    "run_analysis": ("stp.core.pipeline", "run_analysis"),
    "compute_tau_s": ("stp.core.tau_s", "compute_tau_s"),
    "compute_recd_from_conjunctions": (
        "stp.core.recd_levels",
        "compute_recd_from_conjunctions",
    ),
    "bandt_pompe_symbols": ("stp.core.ordinal", "bandt_pompe_symbols"),
    "multivariate_symbols": ("stp.core.ordinal", "multivariate_symbols"),
}


def __getattr__(name: str) -> Any:
    target = _LAZY.get(name)
    if target is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    mod_name, attr = target
    import importlib

    mod = importlib.import_module(mod_name)
    value = getattr(mod, attr)
    globals()[name] = value
    return value
