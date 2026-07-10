"""Systemic Tau (τ_s) — lightweight educational implementation.

This is a transparent, windowed rank-coupling measure suitable for the
platform Lab. When the full ``systemictau`` package is installed, callers
may prefer that implementation for paper-level parity.
"""

from __future__ import annotations

import numpy as np

try:
    from scipy.stats import kendalltau as _scipy_kendalltau
except ImportError:  # pragma: no cover — Cloud mis-install / exotic Python
    _scipy_kendalltau = None  # type: ignore[assignment]


def _kendalltau_numpy(a: np.ndarray, b: np.ndarray) -> tuple[float, float]:
    """Fallback Kendall-τ (O(n²)) when SciPy is unavailable at import time."""
    a = np.asarray(a, dtype=float).ravel()
    b = np.asarray(b, dtype=float).ravel()
    n = len(a)
    if n < 2:
        return 0.0, 1.0
    conc = disc = 0
    for i in range(n - 1):
        da = a[i + 1 :] - a[i]
        db = b[i + 1 :] - b[i]
        prod = da * db
        conc += int(np.sum(prod > 0))
        disc += int(np.sum(prod < 0))
    denom = conc + disc
    if denom == 0:
        return 0.0, 1.0
    return float(conc - disc) / float(denom), 1.0


def kendalltau(a: np.ndarray, b: np.ndarray):
    """Kendall-τ with SciPy when present, pure NumPy fallback otherwise."""
    if _scipy_kendalltau is not None:
        return _scipy_kendalltau(a, b)
    return _kendalltau_numpy(a, b)


def _zscore(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    s = np.nanstd(x)
    if s < 1e-12:
        return np.zeros_like(x)
    return (x - np.nanmean(x)) / s


def pairwise_mean_kendall(window: np.ndarray) -> float:
    """Mean absolute Kendall-τ across all pairs in a (W, N) window."""
    W, N = window.shape
    if N < 2 or W < 3:
        return 0.0
    vals = []
    for i in range(N):
        for j in range(i + 1, N):
            a, b = window[:, i], window[:, j]
            mask = np.isfinite(a) & np.isfinite(b)
            if mask.sum() < 3:
                continue
            tau, _ = kendalltau(a[mask], b[mask])
            if np.isfinite(tau):
                vals.append(float(tau))
    return float(np.mean(vals)) if vals else 0.0


def ensure_multivariate(X: np.ndarray) -> np.ndarray:
    """Ensure (T, N≥2). Univariate ``(T,)`` or ``(T, 1)`` → ``[x, |Δx|]`` proxy."""
    X = np.asarray(X, dtype=float)
    if X.ndim == 1:
        dx = np.abs(np.diff(X, prepend=X[0]))
        return np.column_stack([X, dx])
    if X.ndim != 2:
        raise ValueError("X must be (T,) or (T, N)")
    if X.shape[1] == 0:
        raise ValueError("X must have at least one variable")
    if X.shape[1] == 1:
        x = X[:, 0]
        dx = np.abs(np.diff(x, prepend=x[0]))
        return np.column_stack([x, dx])
    return X


def compute_tau_s(
    X: np.ndarray,
    window: int = 101,
    stride: int = 5,
    zscore: bool = True,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Sliding-window Systemic Tau proxy.

    Returns
    -------
    tau_s : ndarray
        Series of mean pairwise Kendall-τ in each window (signed coupling).
    centers : ndarray
        Window center indices in original time.
    """
    X = ensure_multivariate(X)
    T, N = X.shape
    if N < 2:
        raise ValueError("Need at least 2 variables (or a univariate series to expand)")

    if zscore:
        X = np.column_stack([_zscore(X[:, i]) for i in range(N)])

    if window > T:
        window = max(5, T // 2 * 2 + 1)  # keep odd-ish small window

    taus = []
    centers = []
    for start in range(0, T - window + 1, stride):
        w = X[start : start + window]
        taus.append(pairwise_mean_kendall(w))
        centers.append(start + window // 2)

    return np.asarray(taus, dtype=float), np.asarray(centers, dtype=int)


def try_systemictau(X: np.ndarray, window: int = 101) -> np.ndarray | None:
    """Optional parity path with the full systemictau package."""
    try:
        import systemictau as st  # type: ignore

        taus_global, _ = st.compute_taus(X, window_size=window)
        return np.asarray(taus_global, dtype=float)
    except Exception:
        return None
