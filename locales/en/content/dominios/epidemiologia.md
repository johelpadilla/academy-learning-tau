# Domain: Epidemiology — dengue and hyper-persistence

### Learning outcomes
1. Transfer the τ_s + RECD grammar from cardio to a socio-ecological system.
2. Explain why var/AR1 confuse seasonality with outbreak proximity.
3. State a falsifiable hypothesis about ordinal cases–climate coherence.

**Maturity:** ★★★★☆ — mature narrative and preprints; CCTP remains the platform star cohort.

---

## 1. Scientific context

**Dengue** is a socio-ecological system forced by climate, *Aedes* vector, immunity and mobility. Weekly incidence shows **outbreaks**, plateaus and sometimes **hyper-persistence**: the system stays stuck in high-transmission regimes longer than simple noise models predict. Puerto Rico and DengAI-style series (San Juan / Iquitos) are natural labs for epidemiological early warning.

---

## 2. Why the classical panel is not enough

- Incidence is **discrete, noisy and seasonal**; var/AR1 confuse seasonality with outbreak proximity.
- The “system” is not only `cases(t)`: it is **cases–climate–vector coupling**.
- Univariate thresholds alert **late** or with many false positives.
- Predictive ML can hit the number while **hiding** the reorganization mechanism.

---

## 3. Value of τ_s + RECD

| Contribution | Content |
|--------------|----------|
| Multivariate ordinal | \(X = [z(\mathrm{cases}), z(\mathrm{temp}), z(\mathrm{precip}), \ldots]\) |
| Ordinal hyper-persistence | Φ₂ (sustained relations) and Tau persistence layers |
| RECD | Outbreak “clock”: ticks when joint configuration becomes synergistic |
| Comparability | Same language as cardiology/ecology → systems science, not epi silo |

---

## 4. Example data on the platform

- `dengue_like_demo` — synthetic outbreak with designed ordinal switch.
- Variables: cases, temperature, precipitation (z-scored).
- Pedagogical outbreak windows (high percentile or historical labels).

---

## 5. Design card (uniform schema)

| Field | Value |
|-------|--------|
| **Proxy** | \(X=[z(\mathrm{cases}), z(\mathrm{temp}), z(\mathrm{precip})]\) |
| **Event** | Outbreak onset / high-transmission regime start |
| **Lab preset** | `epidemiology` · domain-default W/stride · m=3 · dual reading required |
| **Primary demos** | `dengue_like_demo` |
| **Maturity** | High (transfer; not operational surveillance) |

### Allowed phrases (examples)
- Ordinal cases–climate coherence rises before incidence peak under this design…
- Methodological transfer from CCTP grammar; not an operational nowcast.
- Seasonality-aware nulls / surrogates must be reported.

### Forbidden phrases (v1.0)
- Operational outbreak alarm for public health agencies
- Replaces epidemiological surveillance systems
- Causal proof of a real city’s outbreak from the demo alone

---

## 6. Guided exercise

1. Lab → `dengue_like_demo` → epidemiology preset → Fast.
2. Dual table: Δτ_s, excess3, var/AR1, p_surr.
3. One paragraph: what is analogous to the cardio “event”, what is **not** claimed.

---

## 7. References

- Author dengue Tau/RECD preprints (2025–2026).
- DengAI DrivenData; vector-borne EWS literature.
