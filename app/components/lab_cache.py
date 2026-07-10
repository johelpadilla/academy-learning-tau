"""Cached data load + analysis for the Lab (Streamlit edge only).

Core library stays pure; cache lives in ``app/`` as required by SPEC.
"""

from __future__ import annotations

from typing import Any

import numpy as np
import streamlit as st

from stp.config.settings import AnalysisParams
from stp.core.pipeline import AnalysisResult, run_analysis
from stp.data.catalog import load_dataset


@st.cache_data(show_spinner=False, ttl=3600, max_entries=64)
def cached_load_dataset(dataset_id: str) -> tuple[np.ndarray, dict[str, Any]]:
    """Load catalog dataset (array + meta). Meta may contain non-hashable bits — return copy-friendly."""
    X, meta = load_dataset(dataset_id)
    return np.asarray(X, dtype=np.float64), dict(meta)


@st.cache_data(show_spinner=False, ttl=3600, max_entries=32)
def _cached_run(
    x_digest: str,
    X: np.ndarray,
    params_json: str,
    event_index: int | None,
    domain: str,
    variables: tuple[str, ...],
) -> AnalysisResult:
    """Internal cache entry. ``x_digest`` stabilizes keys when Streamlit hashes large arrays."""
    del x_digest  # used only for cache key differentiation / readability
    params = AnalysisParams.model_validate_json(params_json)
    return run_analysis(
        np.asarray(X, dtype=np.float64),
        params,
        event_index=event_index,
        domain=domain,
        variables=list(variables) if variables else None,
    )


def _digest_X(X: np.ndarray) -> str:
    arr = np.ascontiguousarray(X, dtype=np.float64)
    # cheap stable fingerprint (shape + sample of bytes + checksum)
    h = hash((arr.shape, arr.strides, float(np.nansum(arr)), float(np.nanmean(arr))))
    return f"{arr.shape}:{h & 0xFFFFFFFF:08x}"


def run_lab_cached(
    X: np.ndarray,
    params: AnalysisParams,
    *,
    event_index: int | None = None,
    domain: str = "generic",
    variables: list[str] | None = None,
) -> AnalysisResult:
    """Run analysis with ``@st.cache_data`` when inputs repeat (common in class demos)."""
    Xa = np.asarray(X, dtype=np.float64)
    vars_t = tuple(variables or [])
    return _cached_run(
        _digest_X(Xa),
        Xa,
        params.model_dump_json(),
        int(event_index) if event_index is not None else None,
        str(domain or "generic"),
        vars_t,
    )


def clear_lab_caches() -> None:
    cached_load_dataset.clear()
    _cached_run.clear()
