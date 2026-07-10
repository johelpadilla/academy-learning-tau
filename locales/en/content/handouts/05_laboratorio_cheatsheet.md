# STP Laboratory cheat-sheet

| Field | Value |
|-------|--------|
| **Document** | Handout 05 · Lab cheat-sheet |
| **Use** | Print single-sided · keep beside the monitor in class |
| **Level** | Graduate lab operations |
| **Version** | 1.1 · 2026 |

---

## Flow

```
Data (catalog | CSV) → Domain + event → Parameters → Analyze
    → Series · τ_s · RECD · EWS · Extensions (BW/TDA) · dual reading
    → Export MD/JSON/Methods + hash
```

**Extensions (operational):** Breathing / TDA / Memory checkboxes — on by default in **Full** mode.

---

## Presets (W / stride / θ₃)

| Domain | W | stride | θ₃ |
|--------|---|--------|-----|
| Cardiology | 101 | 5 | 0.08 |
| Epidemiology | 13 | 1 | 0.10 |
| Neuro / sleep | 51 | 2 | 0.10 |
| Ecology | 25 | 1 | 0.10 |
| Climate / social / finance | 21 | 1 | 0.10 |
| Education | 17 | 1 | 0.10 |
| Synthetic | 31 | 2 | 0.10 |

m=3, delay=1 by default in v1.0. Document any deviation.

---

## Demos every student should know

| ID | Purpose |
|----|---------|
| `synthetic_coupled_logistic` | Strong signal (positive control) |
| `synthetic_ar_noise` | Near-null (negative / control) |
| `sddb_rr_38_demo` | Cardio anchor (if sample present) |
| `dengue_like_demo` | Epi transfer |
| `education_cohort_demo` | Meta-pedagogy |
| `climate_drought_demo` | Climate CSD toy |

---

## Quick reading of outputs

| Output | Question it answers |
|--------|---------------------|
| τ_s(t) | When does ordinal coupling reorganize? |
| Δτ_s | How much changed pre/post (or half/half)? |
| excess3 / Δ | Is irreducible synergy moving? |
| Φ₃ | Did it cross threshold? (may stay 0) |
| p_surr | Is Δ extreme under cross-independence null? |
| var / AR1 | Does the classical panel tell the same story? |
| W(t) | Breathing resolution (if on) |
| β₀ / β₁ | State-cloud topology proxy (if TDA on) |
| hash | Can I regenerate this run? |

---

## Surrogates (indicative)

| Use | n_surr |
|-----|--------|
| In-class demo | 4–8 |
| Serious exploration | 20–50 |
| To be cited | ≥50 + seed sensitivity |

Default: **phase_shuffle**. IAAFT for a stricter null (slower).

---

## Minimal submission export

1. `report.md`  
2. `result.json`  
3. Methods paragraph  
4. Hash copied into PDF/LMS  
5. Dual-reading paragraph (Handout 06)

---

## Forbidden phrases (without evidence)

- “Predicts sudden death / the outbreak / the crash.”  
- “p<0.05 therefore the system collapses.”  
- “Finance demo ⇒ trading strategy.”  
- “Polarization demo ⇒ social truth.”  
- “CCTP pilot validates climate / classroom claims.”

---

## Allowed phrases (with nuance)

- “Δτ_s = …; p_surr = … under phase-shuffle (n=…, seed=…).”  
- “The EWS panel was ambiguous / concordant at ….”  
- “Synthetic demo with design ground truth; not a clinical cohort.”  
- “Domain maturity: …; extrapolation requires external validation.”  
- “Primary continuous metric: mean_excess3 / Δexcess3 (Φ₃ stayed 0).”

---

## Quality mental shortcuts

1. Positive and negative control in the same session?  
2. Event declared (or exploratory half/half)?  
3. Preset or justified W?  
4. Dual reading written?  
5. Hash + Methods present?  
6. Claims bounded by maturity?

If any fail, the submission is not ready.

---

*STP Lab cheat-sheet v1.1*
