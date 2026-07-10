# Practical mathematics — Bandt–Pompe, τ_s, and RECD

| Field | Value |
|-------|--------|
| **Document** | Handout 04 · Practical mathematics |
| **Audience** | Readers past the quick-start; Math sandbox / Lab users |
| **Goal** | Compute and interpret without skipping the ordinal alphabet |
| **Level** | Graduate quantitative methods |
| **Version** | 1.1 · 2026 |

---

## Learning outcomes

1. Construct Bandt–Pompe symbols for m=3 and explain monotone invariance.  
2. State the operational pipeline from \(X\) to τ_s and RECD/excess3.  
3. Describe phase-shuffle as a cross-dependence null.  
4. Complete the numerical checklist before any public claim.

---

## 1. Learning order (do not skip steps)

| # | Block | One sentence | Where |
|---|-------|--------------|-------|
| 1 | Bandt–Pompe | m! local order patterns | Mathematics (sandbox) |
| 2 | τ_s | Relational thermometer in windows | Lab |
| 3 | Φ₁–Φ₃ + excess3 | Nested clock and synergy | Foundations + Lab |
| 4 | Classical EWS | Univariate control panel | Lab |
| 5 | Surrogates | Cross-dependence nulls | Lab (`n_surr`) |
| 6 | Breathing / memory / TDA | Operational Lab extensions | Lab · Full mode |

**Rule:** if you cannot draw Bandt–Pompe on a board, do not interpret excess3.

---

## 2. Notation

| Symbol | Meaning | Typical v1.0 |
|--------|---------|--------------|
| \(X\in\mathbb{R}^{T\times N}\) | Multivariate series | N≥2 |
| \(m,\tau\) | Ordinal dimension and delay | m=3, delay=1 |
| \(W\), stride | Window and step | see presets |
| \(\Phi_1,\Phi_2,\Phi_3\) | Conjunction levels | [0,1] / binary |
| excess3 | Continuous synergy | primary under noise |
| \(\theta_3\) | Φ₃ threshold | 0.08 cardio; ~0.10 others |
| \(\lambda\) | Reorganization intensity | tied to \|τ_s\| |
| p_surr | Surrogate p-value for Δ | report method + n |

---

## 3. Bandt–Pompe in 90 seconds

For an m-point window with delay \(\tau\):

1. Take \(x_t, x_{t+\tau},\ldots,x_{t+(m-1)\tau}\).  
2. Rank-order the values: the **rank pattern** is a symbol in \(\{0,\ldots,m!-1\}\).  
3. With m=3 there are **6** symbols.

### Key property

Invariance under **strictly monotone** transforms (unit changes or “stretching” the signal do not change order). After honest preprocessing, the paradigm is robust to scale mismatches across channels.

### Board exercise

Series: `3, 1, 4, 2` with m=3, delay=1.

- Triplet (3,1,4) → permutation pattern.  
- Triplet (1,4,2) → another symbol.  
Count frequencies over a longer window in the app sandbox.

### Ties

Define and report a tie-breaking policy (jitter, mid-rank, or drop). Unreported ties are a methods defect.

---

## 4. From symbols to τ_s (operational intuition)

1. Each channel is symbolized (Bandt–Pompe).  
2. Within the window, measure **coherence / reorganization** across channels (not only univariate entropy).  
3. Obtain \(\tau_s(t)\) over time.  
4. With a marked **event**, compute pre/post Δ; otherwise first vs second half (declare exploratory design).

### Mental controls

- **Positive control:** coupled logistics with switch → large |Δτ_s|.  
- **Near-null control:** independent AR → small |Δτ_s|.  
- If your “applied” demo looks like AR noise, do not force a reorganization narrative.

---

## 5. RECD and excess3 (formulas in words)

### Φ₁

Normalized fraction of variable pairs sharing the **same symbol** at time t. Statistical base; insufficient alone.

### Φ₂

Pairwise relations (e.g. EQ/GT/LT) that **persist** at least \(d\) steps (typical d=4). Habits, not flashes.

### excess3

Continuous proxy of **irreducible synergy**: joint structure not reducible to independent pairs. Feeds the Φ₃ decision.

### Φ₃

1 if excess3 > θ₃; else 0. Under noisy series it may stay off while excess3 moves: **report the continuous metric**.

### ΔRECD

Accumulation of reorganization ticks modulated by regime. Operationalizes Chronos (index) vs Kairos (event-weighted time).

---

## 6. Surrogates — mathematics of the null

**Independent phase-shuffle per channel**

1. FFT of the channel.  
2. Randomize phases.  
3. IFFT → approximately same spectral density, destroyed cross-dependence.

If the data Δ is extreme versus the surrogate Δ distribution, p_surr is low: evidence that **cross** structure matters.

**IAAFT** iterates to match amplitude histogram as well; more costly; useful in full mode.

### Reporting standard

State: method, n_surr, seed, which Δ was tested (τ_s and/or excess3), and one-sided vs two-sided policy if relevant.

---

## 7. Numerical checklist before a claim

- [ ] N ≥ 2 (or documented proxy)  
- [ ] W and stride justified (preset or sensitivity)  
- [ ] m, delay fixed and reported  
- [ ] Event or exploratory partition **declared**  
- [ ] Δτ_s and Δexcess3 with sign and magnitude  
- [ ] p_surr with n_surr and method  
- [ ] Parallel EWS panel  
- [ ] Hash and Methods exported  

---

## 8. Common mathematical errors

| Error | Correction |
|-------|------------|
| Read τ_s as Pearson correlation | It is ordinal–relational in windows |
| Publish only Φ₃ | Prefer excess3 + Φ₃ |
| n_surr = 2 for a paper | Use tens + seed sensitivity |
| Compare domains with different W silently | Clock time scale changes |
| Treat synthetic demos as field cohorts | Design ground truth ≠ field evidence |
| Hide ties / missing data policy | Methods incomplete |

---

## 9. Complexity (order-of-magnitude)

| Block | Cost order |
|-------|------------|
| Univariate Bandt–Pompe | \(O(T \cdot m \log m)\) (m=3 is cheap) |
| Φ₁ | \(O(T \cdot N^2)\) |
| Φ₂ | \(O(T \cdot N^2 \cdot d)\) |
| excess3 | grows with counting windows; small N, m=3 is feasible |
| Surrogates | × n_surr metric cost |

---

## 10. Fast vs Full (numerical policy)

| Block | Fast (teaching / explore) | Full (paper-like) |
|-------|---------------------------|-------------------|
| τ_s + RECD | Yes | Yes |
| Classical EWS | Yes | Yes |
| Surrogates | n≈8 | n≥50 (recommended) |
| TDA Betti | Optional | Yes (default Full) |
| Breathing | Optional | Yes (default Full) |

**Rule:** explore in Fast; confirm in Full before citing a p-value.

---

*STP practical mathematics handout v1.1 · use with the Mathematics sandbox.*
