# Theory — Systemic Tau, RECD, and dual reading

| Field | Value |
|-------|--------|
| **Document** | Handout 03 · Theory |
| **Audience** | Graduate students · instructors · paradigm paper readers |
| **Use** | Complements in-app Foundations; printable / LMS |
| **Version** | 1.1 · 2026 |
| **Prerequisites** | Intermediate time series; correlation and stochastic processes |

---

## Learning outcomes

1. State the **relational question** of τ_s versus the univariate EWS question.  
2. Describe the pipeline window → ordinal patterns → τ_s(t) → RECD/excess3.  
3. Interpret p_surr under phase-shuffle without reducing evidence to a single p-value.  
4. Apply **dual reading** (concordance / discordance / quiet).  
5. Bound claims by domain **empirical maturity**.

---

## 1. The scientific question

Classical *early warning signals* (EWS), motivated by *critical slowing down* (CSD; Scheffer et al.), essentially ask:

> How much does each variable move? Does recovery from perturbations slow down?

**Systemic Tau (τ_s)** asks something else:

> **How does the shared order structure among system variables reorganize around a regime change?**

In living and socio-ecological systems, transitions are often a **change of relational law** (coupling, synergy, co-order habits), not only univariate slowing. Hence τ_s is **ordinal** (order patterns) and **relational** (across channels).

### 1.1 What τ_s is not

| Common confusion | Graduate clarification |
|------------------|------------------------|
| “Kendall-τ with marketing” | Shares a rank substrate, but operates in **windows**, is multivariate, couples to the RECD clock, and is read under cross-dependence nulls. |
| “Causality / Transfer Entropy” | TE asks directional prediction A→B. τ_s asks joint structure reorganization. They are **complementary**. |
| “Predicts death / outbreak / crash” | **Research and teaching** frame. Not a certified device or operational alert. |
| “Replaces physiology / epidemiology” | Supplies a **coupling observable**; it does not replace domain knowledge. |

---

## 2. Observables, window, and operational definition

Let \(X \in \mathbb{R}^{T \times N}\) with \(N \ge 2\) (or a legitimate bivariate proxy, e.g. \(z(\mathrm{RR}),\, z(|\Delta\mathrm{RR}|)\) in the CCTP pattern).

In a window of length \(W\) with step `stride`:

1. Build local **order patterns** (Bandt–Pompe / ranks) with parameters \(m\) (dimension) and \(\tau\) (delay).  
2. Summarize **cross-ordinal coherence** into a scalar \(\tau_s(t)\) over time.  
3. The trajectory \(\tau_s(t)\) may accelerate, reverse, or stabilize when the system reorganizes — **not necessarily** when univariate variance rises.

**Pedagogical definition (v1.0 Lab):** educationally, \(\tau_s\) relates to a summary (e.g. mean pairwise rank coefficients in-window) of shared ordinal structure. The scientific claim is about **reorganization dynamics** (Δ, nulls, dual reading), not a single static coefficient.

### 2.1 Typical parameters (v1.0 presets)

| Domain | W | stride | θ₃ (indicative) | Note |
|--------|---|--------|-----------------|------|
| Cardiology | 101 | 5 | 0.08 | CCTP empirical anchor |
| Epidemiology | 13 | 1 | 0.10 | Often short series |
| Neuroscience / sleep | 51 | 2 | 0.10 | Multi-channel |
| Ecology | 25 | 1 | 0.10 | Method transfer |
| Climate / social / finance | 21 | 1 | 0.10 | Sandbox / low–mid maturity |
| Education (cohort) | 17 | 1 | 0.10 | Meta-pedagogy |
| Synthetic | 31 | 2 | 0.10 | Design controls |

Always document W, stride, m, delay, and θ₃; **`repro_hash`** seals them.

---

## 3. RECD — discrete extramental clock

**RECD** (*Relational / Discrete Extramental Clock*) formalizes emergent system time (**Kairos**) distinct from the CSV index (**Chronos**).

### 3.1 Nested ordinal conjunction levels

| Level | Formal-intuitive idea | Interpretation trap |
|-------|----------------------|---------------------|
| **Φ₁** | Pairwise symbol coincidence at \(t\) | High Φ₁ ≠ “emergence” |
| **Φ₂** | Persistence of pairwise relations (≥ \(d\) steps; typ. d=4) | Relational habit, not a flash |
| **Φ₃** | Binary synergy indicator above θ₃ | May stay 0 under noise |
| **excess3** | **Continuous** proxy of irreducible synergy | Primary metric in noisy regimes (CCTP) |

In real data, **mean_excess3** and **Δexcess3** are often more informative than the Φ₃ bit.

Clock advance (ΔRECD) is modulated by reorganization intensity \(\lambda\) (in practice tied to \(|\tau_s|\) and regime).

### 3.2 Chronos vs Kairos (for reports)

| Concept | Operational meaning in STP |
|---------|----------------------------|
| Chronos | Sampling time index (CSV row) |
| Kairos | Time weighted by reorganization ticks (RECD) |

Do not confuse “the event is at t=500” (Chronos) with “the system clock accelerated” (Kairos).

---

## 4. Surrogates — the relational null

Question: *Is the observed Δ compatible with cross-independence while preserving univariate spectra?*

| Method | Preserves | Breaks | v1.0 use |
|--------|-----------|--------|----------|
| **Phase-shuffle** (default) | Per-channel spectrum (approx.) | Cross-dependence | Natural relational null |
| **IAAFT** (optional) | Spectrum + histogram (iterative) | Cross-dependence (stricter) | Full mode / sensitivity |

### 4.1 Joint reading of effect × null

| Δ (effect) | p_surr | Graduate reading |
|------------|--------|------------------|
| Large | Low (e.g. ≤0.05) | Candidate residual relational structure |
| Large | High | Do not claim detection; revisit W, preprocess, N |
| Small | Low | Small but stable effect — domain caution |
| Small | High | Compatible with null; useful as a **control** |

**Never** publish p alone without effect size, design (event/partition), n_surr, seed, and domain maturity.

---

## 5. Dual reading (required in teaching and serious submissions)

Present every serious result in **two columns**:

1. **Relational panel:** τ_s, RECD, excess3, p_surr.  
2. **Classical panel:** var, AR(1) or other univariate EWS under the same design.

### 5.1 Why it is methodologically necessary

- Classical EWS can be ambiguous when the transition is multivariate.  
- τ_s may move when var/AR1 do not “alert” — and vice versa.  
- Useful science declares **concordance, discordance, or quiet**, rather than hiding the awkward panel.

### 5.2 Context-dependent sign

Δτ_s or Δexcess3 may **rise or fall** toward an event depending on regime (AF, pacing, outbreak phase, drought type, cohort crisis). Evidence is played on magnitude, concordance, nulls, and domain narrative — not a universal “positive = bad” sign.

---

## 6. Empirical maturity (v1.0)

| Level | Domains / materials | Claim implication |
|-------|---------------------|-------------------|
| **Anchor** | Cardiology CCTP / SDDB (documented pilot) | Stronger claims, still research; limited N |
| **Transfer** | Epidemiology (narrative + demos) | Transferable hypotheses; validate outside |
| **Pedagogical sandbox** | Climate, education, social, sleep, finance, synthetics | **Design** ground truth; teach the method |

**Golden rule:** do not sell cardio pilot strength as validation of social polarization or trading.

---

## 7. Reproducibility and citation

Each Lab run produces a **`repro_hash`** (SHA-256) sealing parameters and a data fingerprint. To cite a number:

1. Domain paper/preprint.  
2. Software (STP v1.0 / aligned paradigm libraries).  
3. Original dataset and license.  
4. Run hash + exported Methods.

---

## 8. Minimal glossary

| Term | Operational definition |
|------|------------------------|
| **τ_s** | Sliding ordinal–relational reorganization thermometer |
| **RECD** | Reorganization-tick clock (Kairos) |
| **excess3** | Continuous ordinal synergy (primary under noise) |
| **Bandt–Pompe** | Alphabet of m! order patterns (m=3 → 6) |
| **EWS** | Univariate early warnings (control panel) |
| **CSD** | *Critical slowing down* (classical frame) |
| **p_surr** | Extremeness of Δ under surrogate null |

Full glossary: *Glossary* handout or Learning path.

---

## 9. Contextual readings (non-exhaustive)

- Bandt, C. & Pompe, B. — permutation entropy / ordinal patterns.  
- Scheffer, M. et al. — critical transitions / CSD / EWS.  
- Spectral nulls (phase randomization) and IAAFT literature.  
- Domain papers/preprints (e.g. CCTP in computational cardiology).  
- Dataset documentation (PhysioNet SDDB, etc.).

---

## 10. Theory self-check (5 items)

1. Can I state τ_s’s question in one sentence without the word “predict”?  
2. Do I know why excess3 may matter more than Φ₃?  
3. What does phase-shuffle break and preserve?  
4. What is a legitimate relational–classical discordance?  
5. Which claim **cannot** be made from a synthetic demo?

---

*STP theory handout v1.1 · complements the app · academic use with citation.*
