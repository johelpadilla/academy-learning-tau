"""Interactive 60-second micro-labs for theoretical modules (Fundamentos)."""

from __future__ import annotations

import numpy as np
import pandas as pd
import streamlit as st

from stp.core.ews_classical import classical_ews_bundle
from stp.core.ordinal import bandt_pompe_symbols
from stp.core.recd_levels import compute_recd_from_conjunctions
from stp.core.tau_s import compute_tau_s, ensure_multivariate
from stp.data.generators import coupled_logistic
from stp.domains.voice import domain_gloss_bundle, domain_label_safe
from stp.i18n.core import is_unresolved_key, t


def _seeded_series(coupling: float, T: int = 420, seed: int = 3) -> np.ndarray:
    return coupled_logistic(
        T=T,
        coupling=float(coupling),
        switch_at=T // 2,
        seed=seed,
    )


def _domain_bridge(domain: str | None, field: str) -> None:
    """Append a short domain-voiced bridge after a micro-lab result."""
    if not domain:
        return
    gloss = domain_gloss_bundle(domain)
    text = gloss.get(field) or gloss.get("lab_coach") or ""
    if text and not is_unresolved_key(text):
        label = domain_label_safe(domain)
        st.caption(f"🧭 **{label}:** {text}")


def render_micro_lab(topic: str, domain: str | None = None) -> None:
    """Render one micro-lab. ``topic`` ∈ tau | ews | recd | excess3 | csd | philosophy."""
    st.markdown(f"#### {t('fundamentos.micro_title')}")
    st.caption(t("fundamentos.micro_blurb"))

    if topic == "tau":
        _lab_tau(domain)
    elif topic == "ews":
        _lab_ews(domain)
    elif topic == "recd":
        _lab_recd(domain)
    elif topic == "excess3":
        _lab_excess3(domain)
    elif topic == "csd":
        _lab_csd(domain)
    elif topic == "philosophy":
        _lab_philosophy(domain)
    else:
        st.info(t("fundamentos.micro_unknown", topic=topic))


def _lab_tau(domain: str | None = None) -> None:
    c1, c2 = st.columns([1, 2])
    with c1:
        coupling = st.slider(
            t("fundamentos.micro_tau_coupling"),
            0.0,
            0.55,
            0.22,
            0.05,
            key="ml_tau_c",
            help=t("fundamentos.micro_tau_coupling_help"),
        )
        window = st.select_slider(
            t("fundamentos.micro_window"),
            options=[21, 31, 41, 51],
            value=31,
            key="ml_tau_w",
        )
    X = _seeded_series(coupling)
    tau, centers = compute_tau_s(X, window=int(window), stride=2)
    mid = int(X.shape[0] // 2)
    with c2:
        st.line_chart(pd.DataFrame({"x0": X[:, 0], "x1": X[:, 1]}))
    st.line_chart(pd.DataFrame({"t": centers, "tau_s": tau}).set_index("t"))
    pre = float(np.nanmean(tau[centers < mid])) if np.any(centers < mid) else float("nan")
    post = float(np.nanmean(tau[centers >= mid])) if np.any(centers >= mid) else float("nan")
    st.success(
        t(
            "fundamentos.micro_tau_out",
            pre=pre,
            post=post,
            d=post - pre,
            c=coupling,
        )
    )
    _domain_bridge(domain, "example_tau")
    _domain_bridge(domain, "tau_gloss")


def _lab_ews(domain: str | None = None) -> None:
    st.markdown(t("fundamentos.micro_ews_prompt"))
    coupling = st.slider(
        t("fundamentos.micro_tau_coupling"),
        0.05,
        0.55,
        0.35,
        0.05,
        key="ml_ews_c",
    )
    X = _seeded_series(coupling, T=500)
    w, stride = 41, 2
    tau, t_cent = compute_tau_s(X, window=w, stride=stride)
    ews = classical_ews_bundle(X, window=w, stride=stride)
    # normalize for visual dual panel
    def _z(a: np.ndarray) -> np.ndarray:
        a = np.asarray(a, dtype=float)
        s = np.nanstd(a)
        return (a - np.nanmean(a)) / s if s > 1e-12 else a * 0.0

    df = pd.DataFrame(
        {
            "t": ews["centers"],
            "var_z": _z(ews["variance"]),
            "ar1_z": _z(ews["ar1"]),
        }
    ).set_index("t")
    df2 = pd.DataFrame({"t": t_cent, "tau_s_z": _z(tau)}).set_index("t")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"**{t('fundamentos.micro_ews_classical')}**")
        st.line_chart(df)
    with c2:
        st.markdown(f"**{t('fundamentos.micro_ews_tau')}**")
        st.line_chart(df2)
    st.info(t("fundamentos.micro_ews_note"))
    _domain_bridge(domain, "classic_gloss")
    _domain_bridge(domain, "example_dual")


def _lab_recd(domain: str | None = None) -> None:
    coupling = st.slider(
        t("fundamentos.micro_tau_coupling"),
        0.0,
        0.5,
        0.25,
        0.05,
        key="ml_recd_c",
    )
    X = ensure_multivariate(_seeded_series(coupling, T=360))
    recd = compute_recd_from_conjunctions(X, m=3, delay=1, d=4, theta3=0.10, phi_window=31)
    df = pd.DataFrame(
        {
            "phi1": recd["phi1"],
            "phi2": recd["phi2"],
            "phi3": recd["phi3"],
        }
    )
    st.line_chart(df)
    st.caption(t("fundamentos.micro_recd_cap"))
    _domain_bridge(domain, "example_recd")


def _lab_excess3(domain: str | None = None) -> None:
    coupling = st.slider(
        t("fundamentos.micro_tau_coupling"),
        0.0,
        0.5,
        0.3,
        0.05,
        key="ml_ex_c",
    )
    theta3 = st.slider("θ₃", 0.05, 0.25, 0.10, 0.01, key="ml_ex_th")
    X = ensure_multivariate(_seeded_series(coupling, T=360))
    recd = compute_recd_from_conjunctions(
        X, m=3, delay=1, d=4, theta3=float(theta3), phi_window=31
    )
    ex = np.asarray(recd["excess3"], dtype=float)
    mid = len(ex) // 2
    st.line_chart(pd.DataFrame({"excess3": ex}))
    st.success(
        t(
            "fundamentos.micro_ex_out",
            mean=float(np.nanmean(ex)),
            d=float(np.nanmean(ex[mid:]) - np.nanmean(ex[:mid])),
            th=theta3,
        )
    )
    _domain_bridge(domain, "excess_gloss")


def _lab_csd(domain: str | None = None) -> None:
    st.markdown(t("fundamentos.micro_csd_prompt"))
    noise = st.slider(
        t("fundamentos.micro_csd_noise"),
        0.05,
        0.8,
        0.25,
        0.05,
        key="ml_csd_n",
    )
    rng = np.random.default_rng(11)
    T = 400
    # Do not name this `t` — it shadows the i18n helper `t(...)`.
    time_idx = np.arange(T)
    # slow critical-slowing-like ramp in variance of primary series
    base = np.sin(time_idx / 18.0)
    vol = 0.15 + noise * (time_idx / T) ** 2
    x = base + rng.normal(0, 1, size=T) * vol
    y = 0.3 * x + rng.normal(0, 0.4, size=T)
    X = np.column_stack([x, y])
    ews = classical_ews_bundle(X, window=51, stride=2)
    tau, centers = compute_tau_s(X, window=51, stride=2)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"**{t('fundamentos.micro_csd_var')}**")
        st.line_chart(pd.DataFrame({"t": ews["centers"], "var": ews["variance"]}).set_index("t"))
    with c2:
        st.markdown("**τ_s**")
        st.line_chart(pd.DataFrame({"t": centers, "tau_s": tau}).set_index("t"))
    st.info(t("fundamentos.micro_csd_note"))
    _domain_bridge(domain, "example_dual")


def _lab_philosophy(domain: str | None = None) -> None:
    st.markdown(t("fundamentos.micro_phil_prompt"))
    show_event = st.checkbox(t("fundamentos.micro_phil_event"), value=True, key="ml_phil_ev")
    X = _seeded_series(0.28, T=400)
    tau, centers = compute_tau_s(X, window=31, stride=2)
    mid = X.shape[0] // 2
    d_tau = float(np.nanmean(tau[centers >= mid]) - np.nanmean(tau[centers < mid]))
    # Bandt–Pompe alphabet richness pre/post on first channel
    pre_s = bandt_pompe_symbols(X[:mid, 0], m=3, delay=1)
    post_s = bandt_pompe_symbols(X[mid:, 0], m=3, delay=1)
    n_pre = len(set(pre_s.tolist()))
    n_post = len(set(post_s.tolist()))
    m1, m2, m3 = st.columns(3)
    m1.metric("Δτ_s (mitad)", f"{d_tau:+.4f}")
    m2.metric(t("fundamentos.micro_phil_pat_pre"), f"{n_pre}")
    m3.metric(t("fundamentos.micro_phil_pat_post"), f"{n_post}")
    if show_event:
        st.caption(t("fundamentos.micro_phil_event_on", t0=mid))
    else:
        st.caption(t("fundamentos.micro_phil_event_off"))
    st.warning(t("fundamentos.micro_phil_caution"))
    _domain_bridge(domain, "jargon_note")
    _domain_bridge(domain, "maturity_phrase")
