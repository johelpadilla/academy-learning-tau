# Domain: Ecosystem ecology — lake eutrophication

### Learning outcomes
1. Link classical CSD lake literature to multivariate ordinal observables.
2. Treat nutrients–Chl-a–DO as a relational triad.
3. Transfer method language between physiology and ecology without overclaim.

**Maturity:** ★★★☆☆ — Strong pedagogy; empirical depth to expand in v1.x.

---

## 1. Scientific context

Shallow lakes can jump from a **clear oligotrophic** to a **turbid eutrophic** state (Scheffer et al.). Series of chlorophyll-a, nutrients and dissolved oxygen capture that transition at monthly/annual scales (e.g. NTL LTER, Lake Mendota-like demos).

---

## 2. Why the classical panel is not enough

This domain is the **historical home** of CSD EWS. They work in many models and some lakes. They fail or are debated when seasonality is strong, human management alters nutrients, or the transition is a **food-web** change rather than a single indicator.

---

## 3. Value of τ_s + RECD

- Same relational language as physiology: the lake “coordinates” nutrients–Chl-a–DO.
- RECD offers a clock of **ecological reorganization events**.
- Enables **methodological transfer** heart ↔ lake (unifying thesis of the platform).

---

## 4. Example data on the platform

- `ecology_like_demo` — Mendota-like monthly series (chla, tp, do, temp z-scored).
- Regime annotation when a historical Chl-a threshold exists.

---

## 5. Design card (uniform schema)

| Field | Value |
|-------|--------|
| **Proxy** | \(X=[\mathrm{chla}, \mathrm{tp}, \mathrm{do}, \mathrm{temp}]\) (z-scored) |
| **Event** | Clear → turbid regime flip / bloom onset |
| **Lab preset** | `ecology` · dual reading vs classical CSD panel |
| **Primary demos** | `ecology_like_demo` |
| **Maturity** | Medium (strong teaching bridge to CSD literature) |

### Allowed phrases (examples)
- Relational reorganization around a designed or historical regime flip…
- Method transfer from CCTP; not an operational lake management alarm.

### Forbidden phrases (v1.0)
- Operational eutrophication early-warning product
- Causal proof for a specific real lake from demo alone

---

## 6. Guided exercise

Lab → ecology_like_demo → compare dual reading to a univariate Chl-a variance story.

---

## 7. References

- Scheffer, *Critical Transitions in Nature and Society*.
- NTL LTER data publications.
