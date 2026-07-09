# Mathematics of the Paradigm — Map

This section of the platform details the computational blocks. Pedagogical order:

1. **Ordinal Patterns (Bandt–Pompe)** — the alphabet.
2. **Systemic Tau (τ_s)** — the relational thermometer.
3. **Adaptive Window (Breathing Window)** — the observation rhythm.
4. **RECD Φ₁–Φ₃ + excess3** — the clock and its levels *(see Fundamentals)*.
5. **TDA + Betti Numbers (Tier 4)** — topology of the state cloud.
6. **Ordinal Memory** — symbolic TE / rank MI.
7. **Surrogates** — IAAFT and phase-shuffle as null models.

## Common Notation

| Symbol | Meaning |
|---------|-------------|
| \(X \in \mathbb{R}^{T\times N}\) | Multivariate series |
| \(m, \tau\) | Bandt–Pompe dimension and delay |
| \(W\), stride | τ_s window and step |
| \(\Phi_1,\Phi_2,\Phi_3\) | Conjunction levels |
| excess3 | Continuous synergy proxy |
| \(\lambda\) | Regime intensity / reorganization |
| \(\alpha_k(\lambda)\) | ΔRECD weights |

## Indicative Complexity

- Univariate Bandt–Pompe: \(O(T \cdot m \log m)\) (or \(O(T)\) with fixed m=3 and numba).
- Φ₁: \(O(T \cdot N^2)\).
- Φ₂: \(O(T \cdot N^2 \cdot d)\).
- Φ₃ / excess3: \(O((T/w) \cdot w \cdot \mathrm{counting\ cost})\); with \(m=3\), small \(N\) is feasible.
- Surrogates: × n_surr the cost of the chosen metric.

## Fast vs Full Mode

| Block | Fast | Full |
|--------|------|------|
| τ_s + RECD | Yes | Yes |
| Classical EWS | Yes | Yes |
| Surrogates | n=8 | n≥50 |
| TDA Betti | No | Yes |
| Ordinal memory | No | Yes |
