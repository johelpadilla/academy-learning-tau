# Domain: Epidemiology — Dengue and Hyper-persistence

## 1. Scientific Context

**Dengue** is a socio-ecological system forced by climate, vector (*Aedes*), immunity, and human mobility. Weekly incidence series show **outbreaks**, plateaus, and sometimes **hyper-persistence**: the system gets "stuck" in elevated transmission regimes longer than a simple noise model would predict.

Puerto Rico and **DengAI**-like series (San Juan / Iquitos) are natural laboratories for epidemiological early warning.

## 2. Why Classical EWS Fail or Fall Short

- Incidence is **discrete, noisy, and seasonal**; variance and AR(1) confuse seasonality with proximity to an outbreak.
- The "system" is not unilinear: it requires integrating **fractional-order models** (where the memory of quiescent eggs delays the system) or explicitly evaluating the *cases–climate–vector* coupling.
- Univariate thresholds systematically fail in the face of urban biological noise.
- Predictive ML or classical SEIR (integer order) models suffer from "forgetfulness", obscuring true bifurcation points and profound relational reorganization.

## 3. Differential Value of τ_s + RECD

| Contribution | Content |
|--------|-----------|
| Ordinal multivariate | \(X = [z(\mathrm{cases}), z(\mathrm{temp}), z(\mathrm{precip}), \ldots]\) |
| Hyper-persistence | Captures fractional delays due to vector latency/biological memory. |
| Vectorial Antisynchronization | Unique capacity to detect antiphase divergence (\(\tau_s \le -0.41\)) between favorable climate and populations decimated by fumigation. |
| RECD (Epidemic Clock) | Replaces chronological time with an **effective epidemiological time**; asymmetric "ticks" mark reorganization and allow advanced predictions (4-6 weeks). |

## 4. Example Dataset

- DengAI San Juan weekly (platform sample).
- Variables: cases, temperature, precipitation (z-score).
- Pedagogical annotation of outbreak windows (high percentile or historical labels).

## 5. Interpretation

- Look for entry into the **genuine chaotic range (\(|\tau_s| < 0.41\))**, which statistically **precedes population peaks with an anticipation of 4-6 weeks**.
- Identify regimes of **strong synchronization (\(\tau_s \ge +0.50\))**, characteristic of stable post-vector intervention periods.
- Study periods of **antisynchronization (\(\tau_s \le -0.41\))**, where *local retrocausality* occurs: the climate increases the pressure, but larval density is forcibly reduced, temporarily reversing the epidemiological clock.
- Empirically contrast that missing data imputation in marginal areas does not destroy ordinal invariants.

## 6. References

- Author's dengue Tau/RECD preprints (2025–2026).
- DengAI DrivenData; early warning literature on vector-borne diseases.
