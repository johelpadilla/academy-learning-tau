# Frequently asked questions (deep answers)

| Field | Value |
|-------|--------|
| **Document** | FAQ · graduate-level answers |
| **Version** | 1.1 · 2026 |
| **Use** | Downloadable handout + Learning path |

These answers target real graduate-level and peer-review misunderstandings — not marketing FAQ.

---

## A. Concepts

### Is Systemic Tau just Kendall tau with marketing?

No. Kinship with rank statistics is real in the **ordinal substrate**, but the object of τ_s is the **dynamics of coupling reorganization** in windows, often multi-scale and tied to RECD. A static rank correlation does not define a clock or Φ₁–Φ₃ levels.

### How does it differ from Transfer Entropy?

| | Transfer Entropy | τ_s + RECD / excess3 |
|--|------------------|----------------------|
| Question | How much does A improve prediction of B? | How does joint ordinal structure reorganize and advance the clock? |
| Direction | Explicitly directional | Relational / synergistic (not a causal graph) |
| Use in v1.0 | Full-horizon | Lab core |

They are **complementary**. Do not substitute one for the other in a paper without justifying the question.

### Why Bandt–Pompe rather than SAX or other symbols?

Parsimony, monotone invariance, and a mature ecosystem (permutation entropy, paradigm papers). SAX and other alphabets are possible extensions; they are **not** the CCTP pilot standard nor the v1.0 core.

### What is “context-dependent sign”?

It means **Δτ_s or Δexcess3 may rise or fall** toward an event depending on regime (e.g. AF, pacing, outbreak phase). Evidence is played on: (1) change magnitude, (2) concordance among metrics, (3) surrogate p-values, (4) domain narrative — not a universal “always positive = bad” sign.

---

## B. Data and practice

### Can I use it with a single variable?

The core is multivariate (N≥2). If you only have one series, the platform builds a proxy  
\(X=[z(x), z(|\Delta x|)]\) (CCTP pattern). It is a **legitimate and explicit** compromise, not magic: it makes the level–variation relation visible.

### Which window W should I use?

Start from the **domain preset** (cardio: 101; dengue/synthetic: ~13). Then:

- W too small → noise, unstable p-values.  
- W too large → smooths the transition and “arrives late”.  
Document W in the report; the hash includes it.

### How many surrogates are enough?

| Use | Indicative n_surr |
|-----|-------------------|
| Class / demo | 4–8 (Fast) |
| Serious exploration | 20–50 |
| Result to cite | ≥50 and seed sensitivity |

Phase-shuffle **preserves per-channel spectra** and **breaks cross-dependence**: the natural null for “is the signal really relational?”.

### How do I read p_surr together with Δ?

- **Large Δ + low p:** candidate relational effect.  
- **Large Δ + high p:** do not claim detection; revisit preprocess and W.  
- **Small Δ + low p:** small but stable effect — interpret with domain caution.  
- **Never** publish p alone without effect size and context.

---

## C. Evidence and ethics

### Does this predict sudden death or a dengue outbreak?

**Not as a certified clinical/operational device.** It is a research and teaching frame. Any prospective use requires external validation, threshold calibration, and ethical governance.

### What does the current core cover?

- Full pipeline τ_s + RECD + EWS + surrogates + hash.  
- **CCTP/SDDB N=10** pilot with documented findings (ambiguous classical panel; significant relational; concordance 8/10 in the domain narrative).  
- Foundations, glossary, domains, Lab, and 6-week syllabus.  
- Samples and generators to reproduce analysis *logic* without PhysioNet.  
- Research library catalog for local publications.

Detail: **Core scope** (Learning path) or the Home expander.

### What should I cite?

1. Domain paper/preprint (e.g. CCTP for cardio).  
2. Software (`systemictau`, `nested-recd`, this platform v1.0).  
3. Original dataset (PhysioNet, LTER, DengAI, etc.).  
4. Lab **`repro_hash`** if you report a concrete run number.

---

## D. Product and software limits

### Why does Φ₃ sometimes “not fire”?

Because it is a **binary indicator** with threshold θ₃. Under noisy data continuous **excess3** can move clearly while Φ₃ stays zero. In CCTP the primary metric is mean_excess3 / Δexcess3.

### Are TDA and Breathing Window ready?

**Yes, as operational Lab extensions** (v1.0+):

| Extension | What it does in the Lab | Backend |
|-----------|-------------------------|---------|
| **Breathing window** | W adapts to local volatility when computing τ_s | Native (always) |
| **TDA / Betti** | β₀/β₁ curves in windows on a delay-embedding cloud | `ripser` if installed; else **Vietoris–Rips 1-skeleton** |
| **Ordinal memory** | Lag-1 symbolic MI and cross-MI | Native |

**How to enable:** **Full** mode (boxes on by default) or tick boxes in Fast. Results tab **Extensions**. CLI: `--breathing --tda`.

**What they are not:** they do not replace τ_s + RECD + EWS + surrogates. A main thesis claim **should not** rest only on pedagogical β₁ of the proxy.

### Do I need to install ripser?

No. Without ripser the Lab uses a Betti proxy from the VR 1-skeleton. With `pip install systemic-tau-platform[tda]`, ripser is used when available.

### Are Academic/Professional plans active?

Plans UI is **not part of the v1.0 educational core**. Locally, Lab and downloadable materials work without a payments backend. Do not confuse commercial positioning with scientific limits of local code.

---

## E. New domains and pedagogy

### Why are there “classroom”, “polarization”, or “drought” demos?

Because STP is **pedagogical** software: they practice the same ordinal grammar on familiar or classical systems (CSD), with **design ground truth**. They are not field evidence nor predictive products.

### Which demo on day one?

1. `synthetic_coupled_logistic` (strong signal).  
2. `synthetic_ar_noise` (near-null).  
3. Then an applied domain **with maturity disclaimer** (e.g. dengue-like or education_cohort).

### Where do I download PDF/Markdown for the LMS?

App page **Materials**: quick guide, manual, theory, cheat-sheet, checklist, syllabus, FAQ, glossary, student/teacher packs.

### What is the Research Library?

A curated catalog of local publications (configurable path / `STP_PUBLICATIONS_DIR`) classified by collections. It provides download of corpus binaries without bloating git. It does not replace Lab dual reading or external validation.

---

*STP FAQ v1.1 · graduate-level reference*
