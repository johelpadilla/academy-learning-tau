from __future__ import annotations

import json
import sys
from pathlib import Path

# Prefer this repo's src/ over a stale editable install elsewhere
_APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_APP))
from components.bootstrap import ensure_stp_path  # noqa: E402

ROOT = ensure_stp_path(__file__)

import numpy as np
import pandas as pd
import streamlit as st

from components.bootstrap import import_ui
from components.illustrations import show_illustration
from components.lab_cache import cached_load_dataset, run_lab_cached
from components.workspace import build_workspace_zip, workspace_filename

(
    empty_state,
    footer,
    interpret_box,
    lab_stepper,
    learning_goals,
    page_header,
    section_header,
    verdict_panel,
) = import_ui(
    "empty_state",
    "footer",
    "interpret_box",
    "lab_stepper",
    "learning_goals",
    "page_header",
    "section_header",
    "verdict_panel",
)

from stp.config import settings as _settings
from stp.config.settings import AnalysisParams, DOMAIN_PRESETS

# Defensive: hot-reload / stale modules must not crash the Lab
DOMAIN_LABELS = getattr(
    _settings,
    "DOMAIN_LABELS",
    {
        "cardiology": "Cardiología",
        "epidemiology": "Epidemiología",
        "neuroscience": "Neurociencia",
        "ecology": "Ecología",
        "finance": "Finanzas",
        "climate": "Clima e hidrología",
        "social": "Dinámica social",
        "education": "Aprendizaje colectivo",
        "physiology": "Fisiología del sueño",
        "synthetic": "Sintético",
    },
)
from stp.core.pipeline import result_to_jsonable
from stp.i18n.core import t
from stp.data.catalog import dataset_title, list_datasets
from stp.domains import (
    domain_gloss_bundle,
    domain_hint,
    domain_label,
    estimate_runtime_seconds,
    get_adapter,
    render_domain_voice_markdown,
)
from stp.reports.markdown_report import render_markdown_report, render_methods_only
from stp.core.tda_betti import has_ripser
from stp.visualization.series_plots import (
    plot_breathing,
    plot_dual_summary,
    plot_ews_comparison,
    plot_recd_panel,
    plot_series,
    plot_tau,
    plot_tda_betti,
)

st.set_page_config(page_title=t("lab.page_title"), page_icon="🌀", layout="wide")

page_header(
    t("lab.title"),
    subtitle=t("lab.subtitle"),
    eyebrow=t("lab.eyebrow"),
    icon="🔬",
)

learning_goals([t("lab.goal_1"), t("lab.goal_2"), t("lab.goal_3")])


# ---------------------------------------------------------------------------
# Helpers: params from catalog / domain
# ---------------------------------------------------------------------------
def _preset_for(domain: str) -> dict:
    return DOMAIN_PRESETS.get(domain, DOMAIN_PRESETS["synthetic"])


def apply_params_from_meta(meta: dict, domain: str) -> None:
    """Write widget session keys from catalog ``default_params`` + domain preset."""
    preset = _preset_for(domain)
    dp = meta.get("default_params") or {}
    st.session_state["lab_window"] = int(dp.get("window", preset["window"]))
    st.session_state["lab_stride"] = int(dp.get("stride", preset["stride"]))
    st.session_state["lab_theta3"] = float(dp.get("theta3", preset["theta3"]))
    st.session_state["lab_m"] = int(dp.get("m", preset.get("m", 3)))
    st.session_state["lab_seed"] = int(dp.get("seed", meta.get("seed", 42)))
    # keep n_surrogates / mode if already chosen
    if "lab_mode" not in st.session_state:
        st.session_state["lab_mode"] = "fast"
    if "lab_n_surr" not in st.session_state:
        st.session_state["lab_n_surr"] = 8 if st.session_state["lab_mode"] == "fast" else 24


def ensure_param_defaults(domain: str) -> None:
    if "lab_window" not in st.session_state:
        apply_params_from_meta({}, domain)


def go_step(n: int) -> None:
    st.session_state["lab_step"] = int(n)
    st.rerun()


# ---- UI mode + step bootstrap ----
if "lab_ui_mode" not in st.session_state:
    st.session_state["lab_ui_mode"] = "novice"
if "lab_step" not in st.session_state:
    st.session_state["lab_step"] = 1

# ---- Deep-link / session bootstrap ----
qp = st.query_params
if "dataset" in qp and "lab_bootstrapped" not in st.session_state:
    try:
        X0, meta0 = cached_load_dataset(qp["dataset"])
        dom0 = meta0.get("domain", "synthetic")
        st.session_state["lab_X"] = X0
        st.session_state["lab_meta"] = meta0
        st.session_state["lab_domain"] = dom0
        st.session_state["lab_event"] = meta0.get("event_index")
        st.session_state["lab_event_label"] = meta0.get("event_label") or t("common.event")
        st.session_state["lab_has_data"] = True
        st.session_state["lab_bootstrapped"] = True
        st.session_state["lab_source_label"] = meta0.get("title", qp["dataset"])
        apply_params_from_meta(meta0, dom0)
        st.session_state["lab_step"] = 2
    except Exception as e:
        st.warning(t("lab.query_fail", err=e))

if "domain" in qp and "lab_domain_qp" not in st.session_state:
    d = qp["domain"]
    if d in DOMAIN_PRESETS:
        st.session_state["lab_domain"] = d
        st.session_state["lab_domain_qp"] = d

# Mode selector (always visible)
um1, um2 = st.columns([2, 3])
with um1:
    ui_mode = st.radio(
        t("lab.ui_mode"),
        ["novice", "expert"],
        horizontal=True,
        format_func=lambda m: t("lab.ui_novice") if m == "novice" else t("lab.ui_expert"),
        key="lab_ui_mode",
        help=t("lab.ui_mode_help"),
    )
with um2:
    if ui_mode == "novice":
        st.caption(t("lab.ui_novice_cap"))
    else:
        st.caption(t("lab.ui_expert_cap"))

if ui_mode == "novice":
    # keep illustrations light
    show_illustration("pipeline")
else:
    show_illustration("pipeline")
    show_illustration("dual_reading")

# ---- State ----
X = st.session_state.get("lab_X")
domain = st.session_state.get("lab_domain", "synthetic")
event_index = st.session_state.get("lab_event")
event_label = st.session_state.get("lab_event_label", t("common.event"))
result = st.session_state.get("lab_result")
has_result = result is not None
has_data = X is not None

# Clamp step when state changes
step = int(st.session_state.get("lab_step", 1))
if has_result and step < 4 and st.session_state.get("lab_force_results"):
    step = 4
    st.session_state["lab_step"] = 4
if not has_data and step > 1:
    # allow step 1 only until data exists — except viewing old results
    if not has_result:
        step = 1
        st.session_state["lab_step"] = 1

lab_stepper(active=step, has_data=has_data, has_result=has_result)

# Quick jump chips (optional navigation)
j1, j2, j3, j4 = st.columns(4)
with j1:
    if st.button(f"1 · {t('lab.step_data')}", width="stretch", disabled=(step == 1)):
        go_step(1)
with j2:
    if st.button(
        f"2 · {t('lab.step_params')}",
        width="stretch",
        disabled=(step == 2 or not has_data),
    ):
        go_step(2)
with j3:
    if st.button(
        f"3 · {t('lab.step_run')}",
        width="stretch",
        disabled=(step == 3 or not has_data),
    ):
        go_step(3)
with j4:
    if st.button(
        f"4 · {t('lab.step_results')}",
        width="stretch",
        disabled=(step == 4 or not has_result),
    ):
        go_step(4)

ensure_param_defaults(domain)

# ============================================================
# Step 1 — Datos
# ============================================================
if step == 1:
    section_header(t("lab.step_data"), number="1")
    st.markdown(t("lab.data_blurb"))

    source_opts = [t("lab.source_catalog"), t("lab.source_csv")]
    source = st.radio("src", source_opts, horizontal=True, label_visibility="collapsed")

    if source == t("lab.source_catalog"):
        all_ds = list_datasets(available_only=False)
        usable = []
        for d in all_ds:
            if d.get("generator") or d.get("path"):
                usable.append(d)
        by_dom: dict[str, list] = {}
        for d in usable:
            by_dom.setdefault(d.get("domain", "synthetic"), []).append(d)

        cdom, cds = st.columns([1, 2])
        with cdom:
            dom_keys = sorted(by_dom.keys())
            idx0 = dom_keys.index(domain) if domain in dom_keys else 0
            domain = st.selectbox(
                t("lab.domain"),
                dom_keys,
                index=idx0,
                format_func=lambda k: domain_label(k),
            )
        with cds:
            options = by_dom.get(domain, [])
            labels = [f"{d['id']} — {dataset_title(d)}" for d in options]
            pick = (
                st.selectbox(
                    t("lab.dataset"),
                    range(len(options)),
                    format_func=lambda i: labels[i],
                )
                if options
                else None
            )

        if options and pick is not None:
            ds = options[pick]
            st.caption(
                f"{ds.get('ground_truth') or ds.get('maturity', '')} · "
                f"license: {ds.get('license', '—')}"
            )
            if ds.get("default_params"):
                dp = ds["default_params"]
                st.caption(
                    t(
                        "lab.catalog_defaults",
                        window=dp.get("window", "—"),
                        stride=dp.get("stride", "—"),
                        m=dp.get("m", "—"),
                        theta3=dp.get("theta3", "—"),
                    )
                )
            if st.button(t("lab.load_dataset"), type="primary"):
                X, meta = cached_load_dataset(ds["id"])
                st.session_state["lab_X"] = X
                st.session_state["lab_meta"] = meta
                st.session_state["lab_domain"] = meta.get("domain", domain)
                st.session_state["lab_event"] = meta.get("event_index")
                st.session_state["lab_event_label"] = meta.get("event_label") or (
                    "switch / event"
                    if meta.get("event_index") is not None
                    else t("common.event")
                )
                st.session_state["lab_has_data"] = True
                st.session_state["lab_source_label"] = meta.get("title", ds["id"])
                st.session_state.pop("lab_result", None)
                apply_params_from_meta(meta, meta.get("domain", domain))
                st.session_state["lab_step"] = 2
                st.rerun()

    else:
        up = st.file_uploader(t("lab.csv_upload"), type=["csv"])
        domain = st.selectbox(
            t("lab.domain_preset"),
            list(DOMAIN_PRESETS.keys()),
            index=list(DOMAIN_PRESETS.keys()).index(domain)
            if domain in DOMAIN_PRESETS
            else 0,
            format_func=lambda k: domain_label(k),
        )
        st.caption(domain_hint(domain))
        with st.expander(t("lab.domain_voice_panel"), expanded=False):
            st.markdown(render_domain_voice_markdown(domain))
        if up is not None:
            df = pd.read_csv(up)
            num = df.select_dtypes(include=[np.number])
            st.dataframe(num.head(8), width="stretch")
            adapter = get_adapter(domain)
            suggested = [c for c in adapter.suggested_columns if c in num.columns]
            default_cols = (
                suggested[:3] if suggested else list(num.columns)[: min(3, num.shape[1])]
            )
            cols = st.multiselect(
                t("lab.vars"),
                list(num.columns),
                default=default_cols,
                help=t("lab.vars_help"),
            )
            use_event = st.checkbox(t("lab.mark_event"), value=False)
            ev = None
            if use_event:
                ev = st.number_input(
                    t("lab.event_index"),
                    min_value=0,
                    max_value=max(0, len(num) - 1),
                    value=len(num) // 2,
                    step=1,
                )
                event_label = st.text_input(
                    t("lab.event_label"), value=t("common.event")
                )
            if len(cols) >= 1 and st.button(t("lab.use_csv"), type="primary"):
                bundle = adapter.prepare(
                    df, columns=cols, event_index=int(ev) if use_event else None
                )
                st.session_state["lab_X"] = bundle.X
                st.session_state["lab_domain"] = domain
                st.session_state["lab_event"] = bundle.event_index
                st.session_state["lab_event_label"] = (
                    event_label if use_event else t("common.event")
                )
                st.session_state["lab_meta"] = {
                    "variables": bundle.variables,
                    "source": up.name,
                    "title": up.name,
                    "default_params": dict(_preset_for(domain)),
                }
                st.session_state["lab_has_data"] = True
                st.session_state["lab_source_label"] = up.name
                st.session_state.pop("lab_result", None)
                apply_params_from_meta(
                    st.session_state["lab_meta"], domain
                )
                st.session_state["lab_step"] = 2
                st.rerun()
        else:
            empty_state(t("lab.empty_csv"), "📄")

    # preview if already has data
    X = st.session_state.get("lab_X")
    event_index = st.session_state.get("lab_event")
    event_label = st.session_state.get("lab_event_label", t("common.event"))
    meta = st.session_state.get("lab_meta") or {}
    vars_ = meta.get("variables") or []
    if X is not None:
        with st.expander(t("lab.preview"), expanded=True):
            st.plotly_chart(
                plot_series(
                    X,
                    title=st.session_state.get("lab_source_label", "Serie"),
                    event_index=event_index,
                    event_label=event_label,
                    names=vars_ if vars_ else None,
                ),
                width="stretch",
            )
            n_vars = X.shape[1] if X.ndim > 1 else 1
            ev_txt = (
                t("lab.with_event", t=event_index)
                if event_index is not None
                else t("lab.no_event")
            )
            st.caption(
                t(
                    "lab.shape_cap",
                    n=X.shape[0],
                    v=n_vars,
                    domain=st.session_state.get("lab_domain", domain),
                    ev=ev_txt,
                )
            )
        if st.button(t("lab.next_params"), type="primary", width="stretch"):
            go_step(2)

# ============================================================
# Step 2 — Parámetros
# ============================================================
elif step == 2:
    section_header(t("lab.step_params"), number="2")
    X = st.session_state.get("lab_X")
    domain = st.session_state.get("lab_domain", "synthetic")
    event_index = st.session_state.get("lab_event")
    event_label = st.session_state.get("lab_event_label", t("common.event"))
    meta = st.session_state.get("lab_meta") or {}
    vars_ = meta.get("variables") or []
    ensure_param_defaults(domain)
    preset = _preset_for(domain)

    st.markdown(
        t(
            "lab.preset_line",
            label=domain_label(domain),
            window=st.session_state.get("lab_window", preset["window"]),
            stride=st.session_state.get("lab_stride", preset["stride"]),
            theta3=st.session_state.get("lab_theta3", preset["theta3"]),
            m=st.session_state.get("lab_m", preset.get("m", 3)),
            hint=domain_hint(domain),
        )
    )
    _voice = domain_gloss_bundle(domain)
    st.info(
        t(
            "lab.how_to_read_domain",
            domain=domain_label(domain),
            variables=_voice.get("variables", "—"),
            event=_voice.get("event_name", "—"),
            coach=_voice.get("lab_coach", ""),
        )
    )
    with st.expander(t("lab.domain_voice_panel"), expanded=(ui_mode == "novice")):
        st.markdown(render_domain_voice_markdown(domain))
        st.markdown(f"**{t('lab.domain_example_header')}**")
        st.markdown(_voice.get("example_dual", ""))

    if X is not None:
        with st.expander(t("lab.preview"), expanded=False):
            st.plotly_chart(
                plot_series(
                    X,
                    title=st.session_state.get("lab_source_label", "Serie"),
                    event_index=event_index,
                    event_label=event_label,
                    names=vars_ if vars_ else None,
                ),
                width="stretch",
            )
            # event adjust
            oe1, oe2 = st.columns(2)
            with oe1:
                new_ev_on = st.checkbox(
                    t("lab.adjust_event"),
                    value=event_index is not None,
                    key="adj_ev",
                )
            with oe2:
                if new_ev_on:
                    event_index = st.number_input(
                        t("lab.t_event"),
                        0,
                        max(0, X.shape[0] - 1),
                        value=int(event_index)
                        if event_index is not None
                        else X.shape[0] // 2,
                        key="ev_num",
                    )
                    st.session_state["lab_event"] = int(event_index)
                else:
                    st.session_state["lab_event"] = None
                    event_index = None

    p1, p2, p3 = st.columns([1, 1, 2])
    with p1:
        mode = st.radio(
            t("lab.mode"),
            ["fast", "full"],
            horizontal=True,
            help=t("lab.mode_help"),
            key="lab_mode",
        )
    with p2:
        surr_method = st.selectbox(
            t("lab.null"),
            ["phase_shuffle", "iaaft"],
            format_func=lambda x: t("lab.phase_shuffle")
            if x == "phase_shuffle"
            else t("lab.iaaft"),
            help=t("lab.null_help"),
            key="lab_surr_method",
        )
    with p3:
        n_surr_default = 8 if mode == "fast" else 24
        if ui_mode == "novice":
            n_surr = n_surr_default
            st.session_state["lab_n_surr"] = n_surr
        else:
            n_surr = st.session_state.get("lab_n_surr", n_surr_default)
        eta_params = {
            "window": int(st.session_state.get("lab_window", preset["window"])),
            "stride": int(st.session_state.get("lab_stride", preset["stride"])),
            "n_surrogates": int(st.session_state.get("lab_n_surr", n_surr_default)),
            "surrogate_method": surr_method,
        }
        n_s = int(X.shape[0]) if X is not None else 800
        n_v = int(X.shape[1]) if X is not None and X.ndim > 1 else 2
        eta = estimate_runtime_seconds(
            n_s, n_v, {**eta_params, "n_surrogates": eta_params["n_surrogates"]}
        )
        st.info(t("lab.eta", eta=eta, mode=mode, surr=surr_method))

    if ui_mode == "novice":
        st.info(t("lab.novice_params_note"))
        # expose seed only
        st.number_input(t("lab.seed"), 0, 10_000, key="lab_seed")
        window = int(st.session_state["lab_window"])
        stride = int(st.session_state["lab_stride"])
        theta3 = float(st.session_state["lab_theta3"])
        m = int(st.session_state["lab_m"])
        n_surr = int(st.session_state.get("lab_n_surr", n_surr_default))
        include_breathing = False
        include_tda = False
        include_memory = False
        st.session_state["lab_breathing"] = False
        st.session_state["lab_tda"] = False
        st.session_state["lab_memory"] = False
        st.markdown(
            t(
                "lab.novice_summary",
                window=window,
                stride=stride,
                m=m,
                theta3=theta3,
                n_surr=n_surr,
                surr=surr_method,
            )
        )
    else:
        c1, c2, c3, c4 = st.columns(4)
        c1.number_input(t("lab.window"), 5, 301, step=2, key="lab_window")
        c2.number_input(t("lab.stride"), 1, 50, key="lab_stride")
        c3.number_input(t("lab.theta3"), 0.01, 0.5, step=0.01, format="%.2f", key="lab_theta3")
        c4.number_input(t("lab.seed"), 0, 10_000, key="lab_seed")

        m1, m2, m3, m4 = st.columns(4)
        # select_slider with key needs options; set via session
        if "lab_m" not in st.session_state:
            st.session_state["lab_m"] = int(preset.get("m", 3))
        m1.select_slider(t("lab.m_bp"), options=[2, 3, 4, 5], key="lab_m")
        if "lab_n_surr" not in st.session_state:
            st.session_state["lab_n_surr"] = n_surr_default
        m2.slider(t("lab.n_surr"), 0, 50, key="lab_n_surr")
        with m3:
            if "lab_breathing" not in st.session_state:
                st.session_state["lab_breathing"] = mode == "full"
            if "lab_tda" not in st.session_state:
                st.session_state["lab_tda"] = mode == "full"
            st.checkbox(t("lab.breathing"), key="lab_breathing", help=t("lab.breathing_help"))
            st.checkbox(t("lab.tda"), key="lab_tda", help=t("lab.tda_help"))
        with m4:
            if "lab_memory" not in st.session_state:
                st.session_state["lab_memory"] = mode == "full"
            st.checkbox(t("lab.memory"), key="lab_memory", help=t("lab.memory_help"))
            tda_note = t("lab.tda_ripser") if has_ripser() else t("lab.tda_vr")
            st.caption(t("lab.tda_backend", note=tda_note))

        window = int(st.session_state["lab_window"])
        stride = int(st.session_state["lab_stride"])
        theta3 = float(st.session_state["lab_theta3"])
        m = int(st.session_state["lab_m"])
        n_surr = int(st.session_state["lab_n_surr"])
        include_breathing = bool(st.session_state.get("lab_breathing"))
        include_tda = bool(st.session_state.get("lab_tda"))
        include_memory = bool(st.session_state.get("lab_memory"))

    # How to read metrics (always)
    with st.expander(t("lab.how_to_read"), expanded=(ui_mode == "novice")):
        st.markdown(t("lab.how_to_read_body"))

    b1, b2 = st.columns(2)
    with b1:
        if st.button(t("lab.back_data"), width="stretch"):
            go_step(1)
    with b2:
        if st.button(t("lab.next_run"), type="primary", width="stretch"):
            go_step(3)

# ============================================================
# Step 3 — Run
# ============================================================
elif step == 3:
    section_header(t("lab.step_run"), number="3")
    X = st.session_state.get("lab_X")
    domain = st.session_state.get("lab_domain", "synthetic")
    event_index = st.session_state.get("lab_event")
    meta = st.session_state.get("lab_meta") or {}
    vars_ = meta.get("variables") or []
    ensure_param_defaults(domain)
    preset = _preset_for(domain)

    mode = st.session_state.get("lab_mode", "fast")
    surr_method = st.session_state.get("lab_surr_method", "phase_shuffle")
    window = int(st.session_state.get("lab_window", preset["window"]))
    stride = int(st.session_state.get("lab_stride", preset["stride"]))
    theta3 = float(st.session_state.get("lab_theta3", preset["theta3"]))
    m = int(st.session_state.get("lab_m", preset.get("m", 3)))
    seed = int(st.session_state.get("lab_seed", 42))
    n_surr_default = 8 if mode == "fast" else 24
    n_surr = int(st.session_state.get("lab_n_surr", n_surr_default))
    if ui_mode == "novice":
        include_breathing = include_tda = include_memory = False
        n_surr = n_surr_default
    else:
        include_breathing = bool(st.session_state.get("lab_breathing", False))
        include_tda = bool(st.session_state.get("lab_tda", False))
        include_memory = bool(st.session_state.get("lab_memory", False))

    st.markdown(
        t(
            "lab.run_summary",
            domain=domain_label(domain),
            window=window,
            stride=stride,
            m=m,
            mode=mode,
            n_surr=n_surr,
            surr=surr_method,
        )
    )

    if X is None:
        st.warning(t("lab.need_data"))
        if st.button(t("lab.back_data")):
            go_step(1)
    else:
        col_back, col_run = st.columns([1, 2])
        with col_back:
            if st.button(t("lab.back_params"), width="stretch"):
                go_step(2)
        with col_run:
            run_clicked = st.button(
                t("lab.run_btn"), type="primary", width="stretch"
            )

        if run_clicked:
            params = AnalysisParams(
                window=int(window),
                stride=int(stride),
                m=int(m),
                delay=int(preset.get("delay", 1)),
                d_persist=int(preset.get("d_persist", 4)),
                theta3=float(theta3),
                n_surrogates=int(n_surr),
                mode=mode,
                seed=int(seed),
                include_ews=True,
                include_breathing=bool(include_breathing),
                include_tda=bool(include_tda),
                include_memory=bool(include_memory),
                surrogate_method=surr_method,  # type: ignore[arg-type]
            )
            with st.status(t("lab.status_run"), expanded=True) as status:
                st.write(t("lab.step1"))
                st.write(t("lab.step2b") if include_breathing else t("lab.step2"))
                st.write(t("lab.step3"))
                st.write(t("lab.step4"))
                st.write(t("lab.step5", method=surr_method, n=n_surr))
                st.write(t("lab.step6") if include_tda else t("lab.step6_skip"))
                st.write(t("lab.step7") if include_memory else t("lab.step7_skip"))
                result = run_lab_cached(
                    X,
                    params,
                    event_index=int(event_index) if event_index is not None else None,
                    domain=domain,
                    variables=vars_ if vars_ else None,
                )
                st.write(t("lab.step8"))
                status.update(label=t("lab.status_done"), state="complete")

            st.session_state["lab_result"] = result
            st.session_state["lab_params_used"] = params.model_dump()
            st.session_state["lab_domain"] = domain
            st.session_state["lab_flash"] = t("lab.flash_ok", hash=result.repro_hash)
            st.session_state["lab_step"] = 4
            st.session_state["lab_force_results"] = True
            st.rerun()

# ============================================================
# Step 4 — Results
# ============================================================
elif step == 4:
    result = st.session_state.get("lab_result")
    X = st.session_state.get("lab_X")
    event_label = st.session_state.get("lab_event_label", t("common.event"))
    meta = st.session_state.get("lab_meta") or {}
    domain = st.session_state.get("lab_domain", "synthetic")

    if result is None:
        empty_state(t("lab.empty_run"), "▶")
        if st.button(t("lab.back_params")):
            go_step(2 if X is not None else 1)
    else:
        flash = st.session_state.pop("lab_flash", None)
        if flash:
            st.success(flash)
        section_header(t("lab.results_header"), number="4")

        # ---- Verdict first (one glance), then detail tabs ----
        interp = result.interpretation or {}
        pval = result.surrogate_stats.get("tau_s", {}).get("p_value", None)
        verdict_panel(
            title=interp.get("title", t("lab.tab_dual")),
            summary=interp.get("summary", "") or t("lab.results_header"),
            metrics=[
                ("Δτ_s", f"{result.metrics['delta_tau_s']:.4f}"),
                ("mean excess3", f"{result.metrics['mean_excess3']:.4f}"),
                ("Δexcess3", f"{result.metrics['delta_excess3']:.4f}"),
                (
                    t("lab.verdict_p"),
                    f"{pval:.3f}" if pval is not None else "—",
                ),
            ],
            caution=interp.get("caution", "") or "",
        )

        ext_bits = []
        if result.memory:
            ext_bits.append(
                t(
                    "lab.mem_cap",
                    mi=result.metrics.get("ordinal_mi_lag1", 0),
                    cmi=result.metrics.get("ordinal_cross_mi", 0),
                )
            )
        if result.tda:
            ext_bits.append(
                t(
                    "lab.tda_cap",
                    backend=result.metrics.get("tda_backend", "—"),
                    db0=result.metrics.get("delta_beta0", 0),
                    db1=result.metrics.get("delta_beta1", 0),
                )
            )
        if result.breathing_windows is not None:
            w = result.breathing_windows
            ext_bits.append(
                t("lab.bw_cap", wmin=int(np.min(w)), wmax=int(np.max(w)))
            )
        if ext_bits:
            st.caption(" · ".join(ext_bits))

        tab_reading, tab_dual, tab_tau, tab_recd, tab_ews, tab_ext, tab_export = st.tabs(
            [
                t("lab.tab_reading"),
                t("lab.tab_dual"),
                t("lab.tab_tau"),
                t("lab.tab_recd"),
                t("lab.tab_ews"),
                t("lab.tab_ext"),
                t("lab.tab_export"),
            ]
        )

        with tab_reading:
            interpret_box(
                interp.get("title", t("lab.tab_dual")),
                [interp.get("summary", "")]
                + list(interp.get("bullets") or [])
                + [interp.get("caution", "")],
            )
            voice = interp.get("voice") or domain_gloss_bundle(domain)
            with st.expander(t("domain_voice_ui.results_voice"), expanded=True):
                st.markdown(
                    f"- **τ_s:** {voice.get('tau_gloss', '')}\n"
                    f"- **excess3:** {voice.get('excess_gloss', '')}\n"
                    f"- **EWS:** {voice.get('classic_gloss', '')}\n\n"
                    f"{voice.get('jargon_note', '')}"
                )
                if voice.get("example_dual"):
                    st.markdown(f"**{t('lab.domain_example_header')}**")
                    st.info(voice["example_dual"])
            with st.expander(t("lab.how_to_read"), expanded=(ui_mode == "novice")):
                st.markdown(t("lab.how_to_read_body"))
                st.markdown(render_domain_voice_markdown(domain))

        with tab_dual:
            st.plotly_chart(plot_dual_summary(result), width="stretch")
        with tab_tau:
            st.plotly_chart(
                plot_tau(
                    result, event_index=result.event_index, event_label=event_label
                ),
                width="stretch",
            )
        with tab_recd:
            st.plotly_chart(
                plot_recd_panel(
                    result, event_index=result.event_index, event_label=event_label
                ),
                width="stretch",
            )
        with tab_ews:
            st.plotly_chart(
                plot_ews_comparison(
                    result, event_index=result.event_index, event_label=event_label
                ),
                width="stretch",
            )
        with tab_ext:
            st.markdown(t("lab.ext_blurb"))
            e1, e2 = st.columns(2)
            with e1:
                st.plotly_chart(
                    plot_breathing(result, event_index=result.event_index),
                    width="stretch",
                )
            with e2:
                st.plotly_chart(
                    plot_tda_betti(result, event_index=result.event_index),
                    width="stretch",
                )
            if not result.tda and result.breathing_windows is None:
                st.info(t("lab.ext_off"))
        with tab_export:
            md = render_markdown_report(result, domain=result.domain)
            methods = render_methods_only(result)
            payload = result_to_jsonable(result)
            params_used = st.session_state.get("lab_params_used") or result.params

            d0, d1, d2, d3 = st.columns(4)
            if X is not None:
                try:
                    zbytes = build_workspace_zip(
                        X,
                        meta,
                        params_used if isinstance(params_used, AnalysisParams) else result.params,
                        result,
                        source_label=st.session_state.get("lab_source_label"),
                    )
                    d0.download_button(
                        t("lab.dl_zip"),
                        data=zbytes,
                        file_name=workspace_filename(result),
                        mime="application/zip",
                        type="primary",
                        width="stretch",
                        help=t("lab.dl_zip_help"),
                    )
                except Exception as e:
                    d0.error(str(e))
            d1.download_button(
                t("lab.dl_md"),
                data=md,
                file_name="stp_report.md",
                mime="text/markdown",
                width="stretch",
            )
            d2.download_button(
                t("lab.dl_methods"),
                data=methods,
                file_name="stp_methods.txt",
                mime="text/plain",
                width="stretch",
            )
            d3.download_button(
                t("lab.dl_json"),
                data=json.dumps(payload, indent=2),
                file_name="stp_result.json",
                mime="application/json",
                width="stretch",
            )
            st.markdown(f"##### {t('lab.repro_header')}")
            st.code(result.repro_hash, language="text")
            st.markdown(f"##### {t('lab.methods_copy')}")
            st.code(methods, language="markdown")
            with st.expander(t("lab.metrics_json")):
                st.json(result.metrics)

        nav1, nav2, nav3 = st.columns(3)
        with nav1:
            if st.button(t("lab.back_params"), width="stretch"):
                go_step(2)
        with nav2:
            if st.button(t("lab.back_data"), width="stretch"):
                go_step(1)
        with nav3:
            if st.button(t("lab.rerun_same"), type="primary", width="stretch"):
                go_step(3)

footer()
