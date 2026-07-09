# The Problem with Classical Early Warning Signals

## The Promise of Classical EWS

The theory of **critical transitions** predicts that as a system approaches a bifurcation point, many systems exhibit *critical slowing down* (CSD): the recovery from perturbations becomes slower. In univariate time series, this often translates to:

| Metric | Expected Signature Near Transition |
|---------|----------------------------------------|
| Variance | ↑ increase |
| Lag-1 Autocorrelation (AR1) | ↑ approaching 1 |
| Power Spectrum | more energy at lower frequencies |
| DFA / Hurst | greater long-range memory |

These metrics have been useful in ecology, climate studies, and some synthetic models. The problem arises in **real, noisy, and multivariate living systems**.

## Where They Fail in Practice

### 1. Univariate / Simple CSD Assumption

Many biological transitions do **not** behave like a single potential with a smoothly sliding control parameter. The heart, the brain, or an epidemic reorganize **networks of relationships**. The variance of a single series may rise, fall, or remain unchanged, while the **cross-structure** fundamentally shifts.

### 2. Inverted or Non-informative Signs

In the CCTP pilot on pre-VF Holter (SDDB):

- The **variance** tends to rise (the "classical" signature).
- The **AR(1)** frequently **drops** — opposite to naive CSD.
- τ_s and excess3 capture the **direction of the relational reorganization**, which is **context-dependent** (not always the same sign).

Interpreting "AR1 did not rise ⇒ no warning" would be a methodological false negative.

### 3. Sensitivity to Monotonic Nonlinearities and Scale

Moment-based metrics (mean, variance) depend on scale and transformations. **Ordinal** measures are invariant to monotonic transformations and align better with the concept of the system's "order pattern."

### 4. Confusion Between Noise, Pacing, and Pathology

In real ECGs, there is intermittent pacing, AF, and annotation artifacts. Univariate EWS react to all of these. A relational framework + quality flags allows us to **retain** difficult cases without destroying the signal (as in CCTP).

### 5. Lack of a "System Time" Theory

Classical EWS live in the time of the laboratory clock (seconds, weeks). They do not model the system's **internal time**: when a significant moment of reorganization "advances." The RECD specifically targets this gap.

## Comparative Table (Pedagogical)

| Criterion | Classical EWS | Systemic Tau + RECD |
|----------|--------------|----------------------|
| Unit of Analysis | Univariate (typical) | Multivariate / relational |
| Observables | Moments, linear correlations | Ordinal patterns, conjunctions |
| Pathway Hypothesis | Generic CSD | Relational reorganization (contextual sign) |
| Time | External chronological | RECD (discrete extramental time) |
| Null Validation | Simple Bootstrap | Phase / IAAFT surrogates breaking cross-dependence |
| Interpretability | Medium | High (Φ₁–Φ₃, excess3) |

## Key Message

> Classical EWS are not "wrong": they are **incomplete** for systems where the transition is a **reorganization of relationships**, not just the slowing down of a single variable.

Systemic Tau and RECD do not replace bifurcation physics; they **complete the instrument panel** with observables aligned to that reorganization.
