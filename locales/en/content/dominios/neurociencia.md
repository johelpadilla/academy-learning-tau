# Domain: Neuroscience — epileptic seizures (CHB-MIT style)

### Learning outcomes
1. Treat multichannel EEG as a relational system with an annotated event.
2. Contrast channel-wise CSD with ordinal co-ordination (τ_s / RECD).
3. State non-clinical scope for any pre-ictal interpretation.

**Maturity:** ★★★☆☆ — Medium–high pipeline readiness; empirical depth consolidating (below CCTP).

---

## 1. Scientific context

**Epileptic seizures** are regime transitions in cortical dynamics. Multichannel EEG is the prototype where many variables (channels/bands) exist, events are annotated, and clinical interest is **pre-ictal**. CHB-MIT (PhysioNet) provides pediatric records with seizure annotations; the platform uses processed or synthetic pre-ictal-like extracts (raw CHB-MIT is not fully redistributed).

---

## 2. Why the classical panel is not enough

- A single channel may not show clear CSD.
- Artefacts and sleep confuse var/AR1.
- The transition is **spatially distributed**: the signature is in **pattern synchronization**, not one channel’s power alone.

---

## 3. Value of τ_s + RECD

- Multivariate: bandpowers or envelopes of 4–8 channels/bands.
- Φ₁–Φ₃ capture **symbolic co-ordination** pre-ictal.
- excess3 as proxy of irreducible network configuration.
- Compare with classical sync indices (PLV, etc.) in Full mode when available.

---

## 4. Example data on the platform

- `eeg_like_demo` — designed coupling transition between channels.
- Download scripts under PhysioNet ToS when using real extracts.

---

## 5. Design card (uniform schema)

| Field | Value |
|-------|--------|
| **Proxy** | \(X=[\mathrm{bandpower}_1,\ldots,\mathrm{bandpower}_k]\) or channel envelopes |
| **Event** | Seizure onset / pre-ictal marker (annotated or designed) |
| **Lab preset** | `neuroscience` · m=3 · dual reading; extensions optional |
| **Primary demos** | `eeg_like_demo` |
| **Maturity** | Medium–high (pedagogical + emerging empirical) |

### Allowed phrases (examples)
- Ordinal co-ordination changes toward the designed/annotated event…
- Toy ictal grammar for method training; not a seizure predictor.

### Forbidden phrases (v1.0)
- Validated seizure prediction device
- Clinical decision support for epilepsy monitoring units

---

## 6. Guided exercise

Lab → `eeg_like_demo` → neuroscience → dual reading paragraph + non-clinical disclaimer.

---

## 7. References

- CHB-MIT PhysioNet; seizure prediction literature; ordinal Systemic Tau framework.
