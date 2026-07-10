# Domain: Climate and hydrology — drought and hydro-climatic regimes

### Learning outcomes
1. Connect classical critical-threshold (CSD) literature to multivariate ordinals.
2. Distinguish a level shift (more heat) from temp–precip–soil relational reorganization.
3. State a falsifiable drought-latent hypothesis without operational forecast claims.

**Maturity:** ★★★☆☆ — Strong pedagogy and CSD bridge; not a climate forecast product.

---

## 1. Scientific context

Droughts and hydro-climatic flips are studied with temperature, precipitation and soil moisture. Classical early warning asks: is the system approaching an irreversible dry regime? The τ_s question is complementary: **how do relations reorder** among those variables under a shared drought latent?

---

## 2. Why the classical panel is not enough

- Seasonality confounds var/AR1.
- A single drought index collapses multivariate structure.
- The “event” is often a **regime**, not a point instant.

---

## 3. Value of τ_s + RECD

| Contribution | Content |
|--------------|----------|
| Climate triad | \(X = [\mathrm{temp}, \mathrm{precip}, \mathrm{soil}]\) |
| Reorganization | Drought latent couples channels that were nearly seasonal/independent |
| Comparability | Same language as lakes (ecology) and outbreaks (epidemiology) |

---

## 4. Example data on the platform

- `climate_drought_demo`: synthetic with marked dry-regime start.
- Designed ground truth shared latent post-event (not real satellite data in v1.0).

---

## 5. Design card (uniform schema)

| Field | Value |
|-------|--------|
| **Proxy** | \(X=[\mathrm{temp}, \mathrm{precip}, \mathrm{soil}]\) |
| **Event** | Onset of dry regime / drought latent activation |
| **Lab preset** | `climate` · dual reading mandatory |
| **Primary demos** | `climate_drought_demo` |
| **Maturity** | Medium — teaching emphasis |

### Allowed phrases (examples)
- Relational reorganization under designed drought latent…
- Pedagogical transfer; not official drought alerts.

### Forbidden phrases (v1.0)
- Official drought forecast / agency alert system
- Guaranteed prediction of irreversible aridification

---

## 6. Guided exercise

Lab → climate_drought_demo → dual paragraph + maturity sentence.

---

## 7. References

- Scheffer et al., critical transitions / CSD.
- Drought indices (SPI, SPEI) as univariate contrast.
