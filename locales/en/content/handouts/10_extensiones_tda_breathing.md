# Operational extensions — Breathing window and TDA / Betti

| Field | Value |
|-------|--------|
| **Document** | Handout 10 · Extensions |
| **Audience** | Lab students (weeks 3–6) and instructors |
| **Status** | **Operational** in STP Lab (not “under development”) |
| **Role** | Pedagogical extension of core τ_s + RECD + EWS + surrogates |
| **Version** | 1.1 · 2026 |

---

## Learning outcomes

1. Separate **core claim** from **extension contrast**.  
2. Interpret adaptive W(t) without inventing coupling.  
3. Report β₀/β₁ with the correct backend (`ripser` vs `vr_skeleton`).  
4. Keep thesis-level claims on the ordinal dual-reading core.

---

## 1. Key message

| Layer | Components | Main claim? |
|-------|------------|-------------|
| **Core** | τ_s, RECD/excess3, classical EWS, surrogates, hash | Yes |
| **Extensions** | Breathing window, TDA β₀/β₁, ordinal memory | Complement / contrast |

The Lab **does not depend** on TDA or breathing to function. When enabled, they appear under **Extensions**, in the report, and in Methods.

---

## 2. Breathing window

### Idea

In volatile regimes, a large fixed W **oversmooths** the transition.  
Breathing maps **local volatility** to an odd window size:

- high volatility → **shorter W** (more reactive)  
- stable regime → **longer W** (smoother)

### How to use in the Lab

1. Enable **Breathing window** (default in Full).  
2. Run.  
3. Extensions tab or secondary axis on τ_s: series **W(t)**.  
4. Document observed W range (e.g. W∈[21–101]).

### Honest reading

Breathing changes the **temporal resolution** of τ_s. It does not invent coupling: if the AR control stays flat, do not force a narrative.

### Reporting

State: enabled/disabled, observed W range, and whether primary Δ used fixed-W or breathing run.

---

## 3. TDA / Betti in windows

### Idea

In each window build a **point cloud** (multivariate delay embedding) and summarize Betti numbers:

- **β₀** — connected components (does the cloud fragment or unify?)  
- **β₁** — cycles (“holes” / 1-skeleton structure)

### Backends

| Backend | When | Notes |
|---------|------|-------|
| **ripser** | If `pip install systemic-tau-platform[tda]` | Classical persistence |
| **VR 1-skeleton** | Always (fallback) | β₀ = components; β₁ = \|E\|−\|V\|+β₀ |

Both are **pedagogical proxies** of state topology. They are not a production multi-scale TDA pipeline.

### How to use in the Lab

1. Enable **TDA / Betti**.  
2. Run (costlier than τ_s alone; Fast+TDA on short demos or Full).  
3. Extensions tab: β₀(t), β₁(t) + event marker.  
4. Metrics: mean/Δ β₀, β₁ and `tda_backend` in JSON/report.

### Expanded dual reading

| Question | Tool |
|----------|------|
| Does shared order reorganize? | τ_s, excess3 |
| Does the univariate panel move? | var / AR1 |
| Does state-cloud topology change? | β₀ / β₁ |
| Is relational Δ residual under cross-null? | p_surr |

**Do not** replace the relational column with TDA. Use TDA to **contrast**: sometimes β₁ moves when var is ambiguous; sometimes it adds nothing.

---

## 4. Ordinal memory (brief)

Symbolic lag-1 MI and cross-MI estimate **persistence of ordinal information**.  
Report as extension; do not treat as a causal graph.

---

## 5. CLI

```bash
# Extensions on (also default with --mode full)
stp analyze data.csv --domain synthetic --breathing --tda -o report.md --json out.json

stp analyze data.csv --mode full -o report.md
```

---

## 6. Submission checklist with extensions

- [ ] Main claim based on τ_s / excess3 / p_surr (+ EWS)  
- [ ] Breathing/TDA declared as extension  
- [ ] TDA backend reported (`ripser` or `vr_skeleton`)  
- [ ] W range if breathing  
- [ ] Run hash  
- [ ] No clinical/operational promises based on β₁ alone  

---

## 7. Common errors

| Error | Correction |
|-------|------------|
| “TDA is not ready yet” | It is operational as extension; update the app |
| Publish only β₁ | Add core dual reading |
| Confuse VR fallback with multi-scale ripser | Cite the backend |
| Enable TDA on huge series without subsample | Use Fast or catalog demos |
| Treat breathing W changes as “proof of coupling” | Resolution ≠ structure |

---

## 8. Thesis-level advice

A defensible thesis chapter typically:

1. Leads with relational dual reading + nulls.  
2. Uses extensions in a **sensitivity / contrast** subsection.  
3. States software versions and backends.  
4. Keeps domain maturity explicit.

---

*STP extensions handout v1.1 · Breathing + TDA operational in the Lab*
