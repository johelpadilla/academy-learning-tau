# The Concept of “Level 3 Excess” (excess3)

## Definition

**excess3** is a **continuous proxy of irreducible ordinal synergy** within a local window of multivariate symbols. It answers the question:

> How much joint structure is there **above** what would be explained by the variables separately and their pairwise interactions?

It is not a causality test. It is a **symbolic irreducibility gauge** aligned with the ontology of RECD's Level 3.

## Construction (Outline)

Given the symbol matrix \(S \in \{0,\ldots,m!-1\}^{T \times N}\) (Bandt–Pompe):

1. In a window of length \(w\):
   - Estimate \(H(\pi^1,\ldots,\pi^N)\) (joint entropy).
   - Estimate \(\sum_i H(\pi^i)\) (marginals).
   - Estimate the average pairwise MI.
2. Approximate total correlation: \(TC \approx \sum_i H_i - H_{\mathrm{joint}}\).
3. Subtract a pairwise contribution (transparent heuristic) → **residual synergy**.
4. (Optional) Add **joint surprise**: joint configurations more frequent than expected under independent marginals.
5. Combine (e.g., \(0.6\cdot\mathrm{syn} + 0.4\cdot\mathrm{surprise}\)) → **excess3(t)**.

The binary version of Level 3 is simply:

\[
\Phi_3(t) = \mathbf{1}\{\mathrm{excess3}(t) > \theta_3\}
\]

## Why Prefer the Continuous Metric in Real Data

In the CCTP cardiac pilot (noisy RR, N=10 SDDB records):

- Baseline excess3 ≈ 0.30–0.35; during approach it can rise towards ~0.43 (e.g., record 38).
- With high thresholds, the "high Level 3" **rate** may stay at zero even though the **excess3 delta** is highly significant.
- That is why the primary metric in the paper is **mean_excess3** (and its Δ), not just `high_level3_rate`.

**Platform's Pedagogical Rule:**

| Situation | Use |
|-----------|------|
| Clean synthetic series | Binary Φ₃ + excess3 |
| Physiology / noisy field | **Continuous excess3** as primary |
| Institutional reports | Both + surrogate intervals / p-values |

## Interpretation of Signs and Deltas

Like τ_s, the **sign of Δexcess3** is **context-dependent**:

- An increase may indicate the **emergence of joint configuration** pre-transition.
- A decrease may indicate a **collapse or simplification** of synergistic structure (e.g., paced regimes or distinct terminal states).

What is scientifically relevant in CCTP is not that it "always goes up", but rather:

1. **Magnitude of change** baseline → approach.
2. **Sign concordance** with Δτ_s.
3. **Significance** against phase-shuffle surrogates (which preserve univariate spectra but break cross-dependence).

## Analogy

If Φ₁ is "singing the same note" and Φ₂ is "maintaining a stable duet," excess3 is the residual of a **polyphony** that cannot be factored into solos or duets. When that residual changes in a sustained way, the system is rewriting its **joint grammar**.

## Relationship with Other Approaches

| Approach | Closeness to excess3 | Difference |
|---------|-------------------|------------|
| Classical Transfer Entropy | Medium | TE is directional and usually real-valued, not necessarily nested ordinal |
| Total correlation / PID | High | excess3 is a surgical proxy oriented to RECD, not a full PID decomposition |
| TDA (Betti) | Complementary | TDA sees cloud topology; excess3 sees temporal symbolic synergy |
| ML features | Low | excess3 is interpretable and falsifiable with surrogates |

## Recommended Parameters (Platform v1.0)

| Domain | θ₃ | w_φ | Notes |
|---------|-----|-----|-------|
| Cardio RR | 0.08 | 101 | recalibrated CCTP |
| Weekly Dengue | 0.10 | 13 | theoretical default |
| Synthetics | 0.10 | 13 | Feigenbaum sweeps |
| EEG bandpower | 0.08–0.12 | explore | high sensitivity to preprocessing |
