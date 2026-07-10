# Dual-reading guide — Relational vs classical EWS

| Field | Value |
|-------|--------|
| **Document** | Handout 06 · Dual reading |
| **Audience** | Lab students and short-report authors |
| **Golden rule** | One panel is never enough for a systems conclusion |
| **Version** | 1.1 · 2026 |

---

## Learning outcomes

1. Structure a dual-panel report (relational + classical).  
2. Classify results into four archetypal patterns with defensible prose.  
3. Fill the submission paragraph template with numbers and scope.

---

## 1. What dual reading is

Present **in parallel**:

| Column A — Relational (STP core) | Column B — Classical (control) |
|----------------------------------|--------------------------------|
| τ_s(t), Δτ_s | Windowed variance |
| excess3, Δexcess3, Φ₃ | AR(1) / autocorrelation |
| p_surr (phase-shuffle / IAAFT) | Other univariate EWS if used |
| Event and pre/post design | Same event / same W when possible |

The platform computes both in the Lab. **Human interpretation** declares concordance or discordance.

---

## 2. Four typical patterns (templates)

### A. Strong concordance

- Relational: notable |Δ| + low p_surr  
- Classical: var and/or AR1 also move toward the event  

**Model text:**  
*“Both the relational and classical panels indicate change toward t=…; the phase-shuffle null does not explain Δτ_s (p=…). Interpretation is bounded to design … and domain maturity ….”*

### B. Relational yes, classical ambiguous

- Relational: signal  
- Classical: flat or contradictory  

**Model text:**  
*“The univariate panel is ambiguous; ordinal reorganization (Δτ_s=…, Δexcess3=…) is the main finding under a cross-independence null. This is coherent with multivariate transitions where univariate CSD fails.”*

### C. Classical yes, relational no

- Var/AR1 rise; τ_s stable; high p_surr  

**Model text:**  
*“There is univariate slowing/amplitude without evidence of cross-ordinal reorganization under this design. No relational detection is claimed.”*

### D. Near-null (control)

- As in `synthetic_ar_noise`  

**Model text:**  
*“Control: small |Δτ_s|; compatible with absence of a designed transition.”*

---

## 3. Submission paragraph template (copy and fill)

```
Design. Series T×N = …×…; domain = …; W=…, stride=…, m=…, delay=…;
event at t=… (or exploratory half/half partition).
Surrogates: method=…, n=…, seed=….

Relational findings. Δτ_s = …; mean_excess3 = …; Δexcess3 = …;
p_surr(τ_s) = … [optional p_surr(excess3)=…].

Classical findings. Δvar ≈ …; AR1 behavior: ….

Dual reading. Concordance / discordance / quiet: ….
Scope. Domain maturity: …; limits: not clinical/operational use.
Reproducibility. repro_hash = ….
```

---

## 4. Dual-reading errors

| Error | Why it fails |
|-------|--------------|
| Hide the classical panel if “inconvenient” | Result selection |
| Declare “prediction” from a low p | p ≠ external predictive value |
| Mix different W across panels silently | Incomparability |
| Use synthetic demo as real-domain evidence | Wrong claim category |
| Ignore context-dependent sign | Negative Δ can be real reorganization |
| Report only Φ₃ when excess3 is the signal | Threshold artifact |

---

## 5. Quick rubric (0–2 each item)

1. Explicit scientific question  
2. Design (event / partition) declared  
3. Complete relational metrics  
4. Classical panel reported  
5. Nulls and n_surr  
6. Bounded conclusion + hash  

**Maximum 12.** A decent Lab submission ≥ 9.

---

## 6. Mini examples (one line each)

| Scenario | Dual line |
|----------|-----------|
| Coupled logistic switch | Relational large Δ, low p; classical may or may not agree — report both |
| Independent AR | Small Δ, high p; classical quiet — successful null control |
| Cardio demo | State sample limits; do not claim certified prediction |

---

*STP dual-reading guide v1.1 · paste into the LMS with the syllabus.*
