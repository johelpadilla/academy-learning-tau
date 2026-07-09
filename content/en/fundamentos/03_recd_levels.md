# RECD: Three Levels of Ordinal Conjunctions (Φ₁, Φ₂, Φ₃)

## What is the RECD?

The **Discrete Extramental Clock (RECD)** postulates that extramental time is not a Newtonian absolute continuum (*Chronos*), but rather a **discrete and fractal sequence of ordinal conjunctions** that emerges in the chaotic range (\(|\tau_s| < 0.41\)), governed by the Feigenbaum constant (\(\delta \approx 4.6692016\)).

This construction is hierarchical and stepped into **four main ontological levels** (Level 0 to Level 3). Each higher level **adds irreducibility**: it does not negate the lower one; it encompasses it and emerges from it without requiring an external temporal substrate.

---

## Level 0 — Local Micro-conjunctions

**Idea:** Corresponds to the elementary ordinal concordances between pairs of system components.
- Formulation: \( C_{ij}^{(0)} = \tau_k(r_i, r_j) \)
- At this level, **time does not yet exist**; only timeless ordinal relations exist.

---

## Level 1 — Systemic Conjunctions (Φ₁)

**Idea:** Do two or more variables share the **same ordinal symbol** at the same instant?

After Bandt–Pompe embedding (dimension \(m\), delay \(\tau\)), each variable \(i\) produces a symbol \(\pi_t^{(i)}\) (one of \(m!\) permutations).

\[
\Phi_1(t) = \frac{2}{N(N-1)} \sum_{i < j} \mathbf{1}\!\left(\pi_t^{(i)} = \pi_t^{(j)}\right)
\]

- Range: \([0,1]\).
- Interpretation: fraction of pairs "in the same order pattern".
- Ontology: Only when the systemic conjunction enters the chaotic range (\(|\tau_s| < 0.41\)) does the **first temporal conjunction** \(t_1\) activate (the first "tick" of the extramental clock).

**Analogy:** Several musicians play the same rhythmic figure in the same measure, either by chance or weak coupling.

---

## Level 2 — Hierarchy of Ordinal Scales (Φ₂)

**Idea:** Punctual equality is not enough; what matters is a **relationship** (equal, greater, lesser between symbols) that **persists** for at least \(d\) steps.

For each pair \((i,j)\):

1. Encode the relationship \(R_t^{ij} \in \{\mathrm{EQ},\mathrm{GT},\mathrm{LT}\}\).
2. In a retrospective window of length \(d\), measure if the current relationship dominates (fraction ≥ threshold, e.g., 0.75).
3. Aggregate and normalize by the number of pairs → \(\Phi_2(t)\).

- Typical parameter: \(d = 4\).
- Ontology: Each new systemic conjunction generates a complete renormalization of the system. The intervals between "ticks" are compressed exponentially according to the Feigenbaum constant: \(\Delta t_k = (1/\delta^k) \times (1/|\tau_s|)\). It is a **fractal-stochastic** structure.

**Analogy:** They don't just coincide in one measure; they maintain a **leadership or rhythmic mirroring** over several measures.

---

## Level 3 — Global Emergent Time (Φ₃)

**Idea:** A joint configuration appears that **cannot be reduced** to coincidences or persistent pairs. It is a computable proxy for **synergy / irreducibility**.

Operationally (local window of symbols):

1. Joint entropy of the tuple \((\pi^1,\ldots,\pi^N)\).
2. Marginal entropies and average pairwise MI (Mutual Information).
3. **Synergistic excess** ≈ total correlation − contribution explainable by pairs.
4. Optional: *joint surprise* (configurations more frequent than expected under independence).

\[
\texttt{excess3}(t) \approx \text{combination of synergy and joint surprise}
\]

\[
\Phi_3(t) = \mathbf{1}\{\texttt{excess3}(t) > \theta_3\}
\]

- Typical θ₃: ~0.10 in synthetics; **0.08** recalibrated in noisy cardiac RR.
- In real physiology, the **continuous excess (excess3)** is usually more robust than the binary rate of "high Level 3".

**Analogy:** The orchestra is not just coordinated by pairs: a **collective gesture** emerges (an "instant" with its own identity) that cannot be deduced from each music stand separately.

---

## Clock Accumulation and Regime Weights

The complete extramental time is built as the hierarchical sum via the recurrence equation:
\[
t_{k+1} = t_k + g(\tau_s(t_k)) \cdot \Delta t_k
\]

where \(g(\tau_s)\) is the **universal gating function**. This level is the only one macroscopically observable.

Qualitative behavior of the gating function \(g(\tau_s)\):

| Regime | Value \(g(\tau_s)\) | Ontological Effect |
|---------|---------------------|-------------------|
| Order / Stability (\(\tau_s \ge +0.50\)) | +1 | Stable and predictable advance (*Chronos*). |
| Chaotic Range (\(\|\tau_s\| < 0.41\)) | (δ-1)/δ × (0.41 - \|\tau_s\|) / 0.41 | Continuous but fractal-stochastic advance (*Kairos*). |
| Antisynchronization (\(\tau_s \le -0.41\)) | -1 | Arrest or local retrocausality (anti-chronology). |

**Central Thesis:** The ontological hierarchy demonstrates that extramental time is a **higher-order emergent** property, built bottom-up from ordinal correlations in the chaotic range, refuting Newtonian absolute time.

---

## Summary Table

| Level | Name | What it measures | Numerical proxy | Ontological weight |
|-------|--------|----------|----------------|-----------------|
| 1 | Coincidence | Symbol equality | Φ₁ ∈ [0,1] | Low |
| 2 | Persistent relation | Stable relations ≥ d | Φ₂ ∈ [0,1] | Medium |
| 3 | Emergence | Irreducible synergy | excess3, Φ₃ | High |

## Falsifiable Hypotheses (Experimental Design)

1. **H1:** Φ₃ / excess3 increase (in magnitude or frequency) in post-threshold vs. baseline regimes.
2. **H2:** The relative contribution of Level 3 grows with λ.
3. **H3:** Large ticks of ΔRECD align with known transitions better than a Φ₁-only clock.
4. **H4:** In surrogates that destroy cross-dependence, Φ₂ and Φ₃ collapse to noise.

These hypotheses structure both the platform's Lab and the CCTP / nested time papers.
