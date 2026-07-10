# Systemic Tau Platform — Quick-start guide

| Field | Value |
|-------|--------|
| **Document** | Handout 01 · Quick-start guide |
| **Level** | Graduate / professional specialization · first session |
| **Time** | 15–25 minutes to a documented first experiment |
| **Platform** | Academy Learning Tau · STP v1.0 |
| **Material version** | 1.1 · 2026 |

---

## 1. Scientific purpose (one sentence)

Teach how to **formulate, compute, and document** an analysis of **ordinal relational reorganization** — Systemic Tau (τ_s) + RECD/excess3 — in **dual reading** against classical *early warning signals* (variance, AR(1)), under cross-dependence nulls (surrogates), with **reproducibility** (SHA-256 hash).

**Not** a certified clinical device, operational outbreak alert, trading engine, or social scoring system.

---

## 2. Learning outcomes

By the end of this session you can:

1. Distinguish a **relational** question from a **purely univariate** question.  
2. Run a positive control and a near-null control in the Laboratory.  
3. Report Δτ_s, p_surr, and at least one classical EWS in parallel.  
4. Export Markdown + Methods + `repro_hash`.

---

## 3. Five-step path (UI)

| Step | Where | Graduate-level action |
|------|--------|------------------------|
| 1 | **Home** | Read core scope: ready vs extension vs non-claims. |
| 2 | **Foundations** | τ_s vs EWS; RECD Φ₁–Φ₃; excess3; CSD as classical frame. |
| 3 | **Mathematics** | Bandt–Pompe sandbox (m=3 → 6 symbols); do not skip the ordinal alphabet. |
| 4 | **Laboratory** | Catalog → Analyze → dual reading → Export. |
| 5 | **Evidence / Library** | CCTP/SDDB empirical anchor and publication corpus; do not over-generalize. |

---

## 4. First experiment (minimal protocol)

1. Open **Laboratory**.  
2. Catalog → `synthetic_coupled_logistic` (coupling switch with design ground truth).  
3. Domain **Synthetic** · mode **Fast** · `n_surr` 4–8 · fixed seed.  
4. Observe |Δτ_s| and p_surr; compare with control `synthetic_ar_noise` (near-null).  
5. Download the **Markdown** report, **Methods** paragraph, and copy **`repro_hash`**.

**Closing questions (3–5 lines):**

- Does the coupled-logistic Δ remain extreme under phase-shuffle?  
- Does the EWS panel (var/AR1) agree, stay silent, or contradict?  
- Which claim **must not** be made from a synthetic demo?

---

## 5. Mental controls before interpretation

| Control | Why it matters |
|---------|----------------|
| N ≥ 2 (or documented RR + \|ΔRR\| proxy) | Core is relational |
| Domain preset before hand-tuning W | Avoids window *p-hacking* |
| Dual reading required | One panel is not enough |
| p_surr + effect size | Never publish p alone |
| Context-dependent sign | Rise or fall can be real reorganization |
| Domain maturity | Demo ≠ cohort; cardio ≠ climate |

---

## 6. Downloadable materials map

| Document | Course use |
|----------|------------|
| User manual | Lab + CLI operations |
| Theory τ_s + RECD | Graduate conceptual frame |
| Practical mathematics | Notation, Bandt–Pompe, nulls |
| Lab cheat-sheet | Presets and allowed phrasing |
| Dual-reading guide | Report templates |
| Analysis checklist | Submission / self-score /12 |
| 6-week syllabus | Course design and rubric |
| Ethics & scope | Honest claims |
| Extensions (Breathing / TDA) | Complement, not substitute for the core |
| FAQ + Glossary | Peer-review misunderstandings |

---

## 7. CLI (optional)

```bash
stp serve
stp analyze data.csv --domain cardiology -o report.md --json result.json
```

---

## 8. Minimal citation for a run

1. Software: Systemic Tau Platform v1.0.  
2. Dataset (catalog ID or original source).  
3. Domain paper/preprint if applicable.  
4. `repro_hash` of the cited run.

---

*STP teaching material v1.1 · academic use with citation · does not replace external validation or institutional ethics review.*
