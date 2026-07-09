# Domain: Computational Cardiology — pre-VF and SDDB

## 1. Scientific Context

**Sudden cardiac death** due to **ventricular fibrillation (VF)** remains difficult to anticipate from the surface ECG. The Holter recordings from the *Sudden Cardiac Death Holter Database* (SDDB, PhysioNet) are one of the few public resources with hours of pre-event dynamics and documented VF onset.

The **Cardiac Critical Transitions Protocol (CCTP)** applies Systemic Tau and ordinal RECD to **RR interval** series to characterize the relational reorganization of heart rate dynamics **before** spontaneous VF.

## 2. Why Classical Metrics are Insufficient

In the CCTP cohort (N=10 high-quality records):

- RR **variance** usually increases (a “CSD-like” signature).
- **AR(1)** frequently **decreases** — an *anti-persistence* behavior directly opposed to the naive expectation of *critical slowing down*.
- Interpreting only var/AR1 produces confusing readings or conceptual false negatives, given that pre-VF dynamics do not follow a single attractor but present abrupt divergences.
- There is **intermittent pacing** and inherent synaptic noise (with noise levels up to 20%). This noise is not merely an "error to be erased"; Systemic Tau demonstrates a **topological invariance** and robustness that classical metrics lack.

## 3. Differential Value of τ_s + RECD

| Ingredient | Role in CCTP |
|-------------|-------------|
| Proxy \(X = [z(\mathrm{RR}),\, z(\|\Delta\mathrm{RR}\|)]\) | Minimum physiologically motivated multivariate |
| τ_s (W=101, stride=5) | Ordinal coupling between level and beat-to-beat variability |
| Φ₁–Φ₃ + **excess3** | Symbolic structure decomposition; excess3 as primary |
| Phase-shuffle surrogates | Null model that preserves spectra and breaks cross-dependence |
| Context-dependent sign | Reorganization, not “the metric always goes up” |

**Key CCTP findings (empirical validation):** 
1. Δτ_s and Δexcess3 are significant under *phase-shuffle* surrogates (which destroy cross-dependence while preserving the frequency spectrum).
2. A **3.8 times lower false positive rate** and an early warning window **2.3 times larger** were observed compared to the local Lyapunov exponent and the Pearson coefficient.
3. The extramental clock in the heart presented spontaneous emergence with a **constant fractal dimension of ≈1.98**.

## 4. Example Dataset

- **Source:** PhysioNet SDDB + clean RRs from the CCTP repository.
- **Platform sample:** records 38 (strong signal) and 51 (intermittent pacing).
- **Columns:** `rr_ms`, `abs_drr`, `z_rr`, `z_abs_drr`.
- **Event:** VF onset index (`vfon`) when available.

## 5. Guided Interpretation

1. Inspect quality: `interp_frac`, pacing flags.
2. Look at τ_s in baseline vs. approach window (~3 h pre-event).
3. Look at mean excess3 and its Δ (not just binary Φ₃).
4. Contrast with var and AR1 (EWS tab).
5. Demand surrogate p-values before claiming a "warning".

## 6. References

- Padilla-Villanueva — CCTP/SDDB (Zenodo 10.5281/zenodo.21270699).
- Goldberger et al., PhysioNet / SDDB.
- Greenwald (1986) — SDDB foundation.
