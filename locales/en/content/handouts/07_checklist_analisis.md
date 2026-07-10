# Analysis checklist — Lab submission / short report

| Field | Value |
|-------|--------|
| **Document** | Handout 07 · Analysis checklist |
| **Use** | Mark every item before submit; if N/A, justify in one line |
| **Scoring** | Optional self-score /12 aligned with dual-reading rubric |
| **Version** | 1.1 · 2026 |

---

## A. Question and scope

- [ ] Scientific question in one sentence (relational reorganization, not “predict X”)  
- [ ] Domain and **empirical maturity** declared  
- [ ] Synthetic demo vs real data distinguished  
- [ ] Ethical limits (not clinical / not operational) mentioned  
- [ ] Complementary vs competing methods stated if relevant (e.g. TE not substituted silently)

## B. Data

- [ ] Source (catalog ID / CSV / PhysioNet / …)  
- [ ] Dimensions T × N  
- [ ] Variables used and why (adapter / theory)  
- [ ] Preprocess (z-score, RR–|ΔRR| proxy, missingness, ties)  
- [ ] Third-party license / ToS respected  
- [ ] Anonymization / IRB note if human data outside demos

## C. Design

- [ ] Event marked **or** exploratory partition declared  
- [ ] Domain preset or justification of W, stride, m, θ₃  
- [ ] Surrogate seed fixed  
- [ ] Fast/full mode and n_surr aligned with the claim  
- [ ] No undisclosed post-hoc event hunting

## D. Numerical results

- [ ] Δτ_s (sign + magnitude)  
- [ ] mean_excess3 and Δexcess3  
- [ ] p_surr and method (phase-shuffle / IAAFT)  
- [ ] At least one classical EWS in parallel  
- [ ] Figures: series+event, τ_s, RECD/excess3, EWS  
- [ ] Extensions (if used): W range and/or β₀/β₁ + backend

## E. Interpretation

- [ ] Dual reading (concordance / discordance / quiet)  
- [ ] Φ₃ not over-interpreted when excess3 is the signal  
- [ ] Context-dependent sign considered  
- [ ] Comparison with control (AR or baseline) if applicable  
- [ ] Claims bounded to design and maturity

## F. Reproducibility and delivery

- [ ] `repro_hash` copied  
- [ ] Markdown export  
- [ ] JSON export (if required)  
- [ ] Methods paragraph  
- [ ] Citations: software + dataset + domain paper  

---

## Optional self-assessment

| Criterion (0–2) | Score |
|-----------------|-------|
| Question and scope | |
| Data and design | |
| Metrics + nulls | |
| Dual reading | |
| Bounded writing | |
| Hash / exports | |
| **Total /12** | |

**Guideline:** ≥9 for a solid Lab submission; 12 only if complete and honest about limits.

---

## Instructor spot-checks (3 questions)

1. Can the student re-run and match the hash?  
2. Is the claim category correct (demo / pilot / transfer)?  
3. Would a referee understand what was *not* claimed?

---

*STP checklist v1.1 · printable*
