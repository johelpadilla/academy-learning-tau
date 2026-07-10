# Foundations — Systemic Tau (τ_s)

| Field | Value |
|-------|--------|
| **Module** | Foundations 01 |
| **Level** | Graduate |
| **Version** | 1.1 · 2026 |
| **Related handouts** | Theory · Practical mathematics · Dual reading |

---

## Learning outcomes

1. State the scientific question of τ_s in one sentence without “predict”.  
2. Contrast ordinal–relational measurement with univariate amplitude/slowing.  
3. List required design elements (N, W, event, nulls) for a defensible Δτ_s.

---

## 1. Scientific object

**Systemic Tau (τ_s)** measures how the **shared order structure** among variables of a multivariate system reorganizes over time. It does not primarily ask how large each channel’s fluctuations are, but how **relations of order** among channels change around a regime shift.

Operationally (Lab v1.0 education pipeline):

1. Multivariate series \(X\in\mathbb{R}^{T\times N}\) (or a documented bivariate proxy).  
2. Sliding windows of length \(W\) with step `stride`.  
3. Local ordinal patterns (Bandt–Pompe / ranks).  
4. Summary of cross-ordinal coherence → \(\tau_s(t)\).  
5. Contrast Δ (pre/post event or half/half) under surrogate nulls.

---

## 2. Why ordinal and relational?

| Property | Implication |
|----------|-------------|
| Ordinal | Robust to strictly monotone transforms; focuses on order, not scale |
| Relational | Targets coupling reorganization, not only univariate CSD |
| Windowed | Captures dynamics, not a single static coefficient |
| Null-aware | Phase-shuffle tests residual cross-structure |

---

## 3. What τ_s is not

- Not a marketing rename of static Kendall-τ alone.  
- Not Transfer Entropy (directional prediction).  
- Not a certified predictor of clinical or market events.  
- Not a substitute for domain theory (physiology, epi, climate…).

---

## 4. Reading τ_s in practice

Always with:

1. Effect size (Δτ_s magnitude and sign).  
2. Classical EWS panel (dual reading).  
3. p_surr + method + n_surr + seed.  
4. Domain maturity statement.  
5. `repro_hash`.

**Context-dependent sign:** rise or fall of τ_s may both indicate reorganization depending on regime.

---

## 5. Micro-check

- [ ] I can explain τ_s without claiming prediction.  
- [ ] I know why N≥2 (or proxy) is required.  
- [ ] I will not publish p without Δ and design.

---

*Foundations 01 · STP v1.1*
