# Domain: Computational cardiology — pre-VF and SDDB

### Learning outcomes
1. Explain why var/AR1 can be ambiguous before ventricular fibrillation (VF).
2. Describe the proxy \(X=[z(\mathrm{RR}), z(|\Delta\mathrm{RR}|)]\) and CCTP presets.
3. Apply the **dual-reading** protocol to a cardio-like case or SDDB sample.

**Empirical maturity in v1.0:** ★★★★★ (platform maximum) — CCTP pilot N=10.

---

## 1. Scientific context

**Sudden cardiac death** via **ventricular fibrillation (VF)** remains hard to anticipate from surface ECG. Holter records from the *Sudden Cardiac Death Holter Database* (SDDB, PhysioNet) are among the few public resources with hours of pre-event dynamics and a documented VF onset.

The **Cardiac Critical Transitions Protocol (CCTP)** applies Systemic Tau and ordinal RECD to **RR-interval** series to characterize relational reorganization of heart-rate dynamics **before** spontaneous VF.

**Guiding question:** not “does variance rise?”, but “does the relation between RR level and beat-to-beat variation reorganize?”.

---

## 2. Why classical metrics are insufficient here

In the CCTP cohort (N=10 high-quality records):

| Finding | Implication |
|---------|-------------|
| RR variance often **increases** | “CSD-like” signature present |
| AR(1) frequently **decreases** | Naive CSD fails |
| Intermittent pacing / AF in some records | “Noise” is clinical context, not blind garbage |

Interpreting only var/AR1 yields confusing readings or **conceptual false negatives**.

---

## 3. Differential value of τ_s + RECD

| Ingredient | Role in CCTP | In Lab v1.0 |
|------------|--------------|-------------|
| Proxy \(X = [z(\mathrm{RR}),\, z(\|\Delta\mathrm{RR}\|)]\) | Minimal physiologically motivated multivariate | Auto if 1 column; cardio-like simulates it |
| τ_s (W=101, stride=5) | Ordinal level–variability coupling | Preset `cardiology` |
| Φ₁–Φ₃ + **excess3** | Symbolic structure; excess3 primary under noise | RECD tab + metrics |
| Phase-shuffle | Cross-dependence null | n surrogates slider |
| Context-dependent sign | Reorganization, not a sign dogma | Interpret Δ + p + context |

**Key pilot finding (documented):**  
Δτ_s and Δexcess3 are significant in most records under surrogates, with **sign concordance in 8/10** cases, even when the classical panel is ambiguous.

---

## 4. Platform example datasets

| Resource | Role in the Lab |
|----------|-----------------|
| Sample `sddb_rr_38_demo.csv` | Strong signal / reference case |
| Sample `sddb_rr_51_demo.csv` | Intermittent pacing — quality flags and preset limits |
| **Cardio-like demo** generator | CCTP flow without PhysioNet dependency |

Typical columns: `rr_ms`, `abs_drr`, `z_rr`, `z_abs_drr`. Event: VF onset index (`vfon`) when available.

---

## 5. Design card (uniform schema)

| Field | Value |
|-------|--------|
| **Proxy** | \(X=[z(\mathrm{RR}), z(\|\Delta\mathrm{RR}\|)]\) |
| **Event** | VF onset (`vfon`) or approach window |
| **Lab preset** | `cardiology` · W≈101 · stride≈5 · θ₃≈0.08 · m=3 |
| **Primary demos** | `sddb_rr_38_demo`, `sddb_rr_51_demo`, cardio-like |
| **Maturity** | Very high (CCTP anchor) |

### Allowed phrases (examples)
- “Relational reorganization significant vs phase-shuffle under this design…”
- “Classical panel ambiguous (var↑, AR1↓); relational panel moves in the approach…”
- “Not a clinical alarm device; N and sample limits apply.”

### Forbidden phrases (v1.0)
- “Predicts VF / validated real-time alarm”
- “Certified medical device / ICU decision support”
- “Causally proves sudden death risk for a patient”

---

## 6. Guided interpretation checklist

1. **Quality:** excess interpolation, pacing, artefacts?  
2. **Relational panel:** baseline vs approach τ_s; mean excess3 and Δ.  
3. **Nulls:** phase-shuffle p for Δτ_s (and excess3 if computed).  
4. **Classical panel:** var and AR1 — confirm, stay quiet, or contradict?  
5. **Concordance:** do τ_s and excess3 move together?  
6. **Bounded closing sentence** with non-clinical scope.

---

## 7. 20-minute exercise

1. Lab → **Cardio-like demo** → cardiology preset → Fast, n_surr=8.  
2. Table: Δτ_s, mean excess3, Δexcess3, p_surr, qualitative var/AR1.  
3. Write 4 dual-reading lines.  
4. (Optional) Compare samples 38 vs 51.

---

## 8. References

- Padilla-Villanueva — CCTP/SDDB (Zenodo 10.5281/zenodo.21270699).  
- Goldberger et al., PhysioNet / SDDB.  
- Greenwald (1986) — SDDB basis.  
- In platform: **Evidence** + **Core scope** (Learning path).
