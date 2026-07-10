# Foundations — Classical EWS and their limits

| Field | Value |
|-------|--------|
| **Module** | Foundations 02 |
| **Level** | Graduate |
| **Version** | 1.1 · 2026 |

---

## Learning outcomes

1. Define variance and AR(1) as classical early warning signals.  
2. State at least three failure modes of purely univariate EWS.  
3. Explain why dual reading is required, not optional.

---

## 1. Classical frame (CSD)

*Critical slowing down* (CSD) suggests that near some bifurcations a system recovers more slowly from perturbations. Empirically this often appears as:

- rising **variance** in a rolling window;  
- rising **lag-1 autocorrelation** (AR(1) coefficient);  
- sometimes other univariate indicators (skewness, spectral reddening).

These remain **valuable controls**. STP does not discard them.

---

## 2. Limits that motivate τ_s

| Limit | Consequence |
|-------|-------------|
| Univariate focus | Misses pure reorganization of coupling |
| Sign ambiguity | Variance can rise for many non-critical reasons |
| Spatial/multivariate transitions | Local channels may not “slow” while relations reorganize |
| Observation process | Noise, sampling, nonstationarity confound EWS |
| Threshold temptation | “Alert” language without external validation |

---

## 3. Pedagogical rule

In STP Lab:

- Always compute **classical EWS in parallel**.  
- Never hide an inconvenient classical panel.  
- Declare concordance, discordance, or quiet.

---

## 4. Micro-lab prompt

On `synthetic_coupled_logistic` and `synthetic_ar_noise`, compare var/AR1 vs Δτ_s. Write four lines of dual reading.

---

*Foundations 02 · STP v1.1*
