"""Portable Lab workspace ZIP (series + params + result + report + hash)."""

from __future__ import annotations

import io
import json
import zipfile
from datetime import datetime, timezone
from typing import Any

import numpy as np
import pandas as pd

from stp.config.settings import AnalysisParams
from stp.core.pipeline import AnalysisResult, result_to_jsonable
from stp.reports.markdown_report import render_markdown_report, render_methods_only


def build_workspace_zip(
    X: np.ndarray,
    meta: dict[str, Any],
    params: AnalysisParams | dict[str, Any],
    result: AnalysisResult,
    *,
    source_label: str | None = None,
) -> bytes:
    """Build a self-contained workspace archive for download / hand-in."""
    Xa = np.asarray(X, dtype=np.float64)
    if Xa.ndim == 1:
        Xa = Xa.reshape(-1, 1)

    vars_ = list(meta.get("variables") or result.variables or [])
    if len(vars_) != Xa.shape[1]:
        vars_ = [f"x{i}" for i in range(Xa.shape[1])]

    if isinstance(params, AnalysisParams):
        params_dict = params.model_dump()
    else:
        params_dict = dict(params)

    manifest = {
        "format": "academy-learning-tau-workspace",
        "version": "1.0",
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source_label": source_label or meta.get("title") or meta.get("source") or "workspace",
        "domain": result.domain,
        "repro_hash": result.repro_hash,
        "event_index": result.event_index,
        "n_samples": int(Xa.shape[0]),
        "n_vars": int(Xa.shape[1]),
        "variables": vars_,
    }

    df = pd.DataFrame(Xa, columns=vars_)
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("manifest.json", json.dumps(manifest, indent=2, ensure_ascii=False))
        zf.writestr("series.csv", df.to_csv(index=False))
        zf.writestr(
            "meta.json",
            json.dumps(meta, indent=2, ensure_ascii=False, default=str),
        )
        zf.writestr("params.json", json.dumps(params_dict, indent=2, ensure_ascii=False))
        zf.writestr(
            "result.json",
            json.dumps(result_to_jsonable(result), indent=2, ensure_ascii=False),
        )
        zf.writestr(
            "report.md",
            render_markdown_report(result, domain=result.domain),
        )
        zf.writestr("methods.txt", render_methods_only(result))
        zf.writestr("REPRO_HASH.txt", f"{result.repro_hash}\n")
        # compact metrics table for quick LMS paste
        m = result.metrics or {}
        metrics_lines = ["metric,value"]
        for k, v in m.items():
            metrics_lines.append(f"{k},{v}")
        zf.writestr("metrics.csv", "\n".join(metrics_lines) + "\n")

    return buf.getvalue()


def workspace_filename(result: AnalysisResult) -> str:
    short = (result.repro_hash or "run")[:8]
    dom = (result.domain or "lab").replace(" ", "_")
    return f"alt_workspace_{dom}_{short}.zip"
