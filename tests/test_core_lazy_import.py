"""Multipage-safe lazy core package + Kendall-τ fallback."""

from __future__ import annotations

import importlib
import sys

import numpy as np


def test_core_init_does_not_eagerly_load_pipeline():
    """Importing stp.core must not force pipeline (avoids Cloud deadlocks)."""
    for name in list(sys.modules):
        if name == "stp.core" or name.startswith("stp.core."):
            del sys.modules[name]
    importlib.invalidate_caches()

    import stp.core as core

    assert "stp.core.pipeline" not in sys.modules
    # Attribute access loads on demand
    run_analysis = core.run_analysis
    assert callable(run_analysis)
    assert "stp.core.pipeline" in sys.modules


def test_kendalltau_fallback_matches_sign():
    from stp.core.tau_s import _kendalltau_numpy, kendalltau

    rng = np.random.default_rng(0)
    a = rng.normal(size=40)
    b = a + 0.1 * rng.normal(size=40)
    t_fb, _ = _kendalltau_numpy(a, b)
    t_main, _ = kendalltau(a, b)
    assert abs(float(t_fb) - float(t_main)) < 0.15
    assert t_fb > 0.5


def test_compute_tau_s_without_eager_pipeline():
    from stp.core.tau_s import compute_tau_s

    rng = np.random.default_rng(1)
    X = rng.normal(size=(200, 3))
    tau, centers = compute_tau_s(X, window=31, stride=5)
    assert len(tau) == len(centers)
    assert len(tau) > 5
