# Domain: Neuroscience — Epileptic Seizures (CHB-MIT)

## 1. Context

**Epileptic seizures** are regime transitions in cortical dynamics. Multichannel EEG is the prototype of a system where:

- there are many variables (channels/bands),
- the event is annotated,
- the clinical interest is the **pre-ictal** state.

CHB-MIT (PhysioNet) offers pediatric records with seizure annotations.

## 2. Limits of Classical EWS

- A single channel may not show clear CSD.
- Artifacts and sleep confound var/AR1.
- The transition is **spatially distributed**: the signature lies in the **synchronization of patterns**, not just in the power of one channel.

## 3. Tau + RECD Contribution

- Multivariate: bandpowers or envelopes of 4–8 channels/bands.
- Φ₁–Φ₃ capture pre-ictal **symbolic co-ordination**.
- excess3 as a proxy for irreducible network configuration.
- Comparison with classical TE and standard synchronization indices (PLV, etc.) in Full mode.

## 4. Dataset

- Pre-ictal-like synthetic or processed extract (the raw CHB-MIT is not redistributed in full).
- Download scripts under PhysioNet ToS.

## 5. Maturity

**Medium-High** in platform v1: pipeline ready; empirical evidence undergoing consolidation (less mature than CCTP).

## 6. References

- CHB-MIT PhysioNet; seizure prediction literature; the paradigm's ordinal framework.
