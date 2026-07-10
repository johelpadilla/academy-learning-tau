# Fondements — Niveaux RECD emboîtés (Φ₁–Φ₃)

| Champ | Valeur |
|-------|--------|
| **Module** | Fondements 03 |
| **Niveau** | Postgraduate |
| **Version** | 1.1 · 2026 |

---

## Objectifs d’apprentissage

1. Définir Φ₁, Φ₂, Φ₃ et excess3 de façon opérationnelle.  
2. Distinguer Chronos (index CSV) et Kairos (horloge RECD).  
3. Préférer excess3 continu à Φ₃ binaire sous bruit.

---

## 1. Pourquoi une horloge ?

τ_s est un **thermomètre** de réorganisation relationnelle.  
**RECD** accumule la réorganisation en **ticks** discrets, donnant au système un temps émergent (Kairos) distinct du temps d’échantillonnage (Chronos).

---

## 2. Grammaire emboîtée

| Niveau | Idée | Prudence |
|--------|------|----------|
| **Φ₁** | Coïncidence de symboles par paires en t | Élevé ≠ émergence |
| **Φ₂** | Persistance de relations par paires (≥ d pas) | Habitude, pas flash |
| **Φ₃** | Synergie binaire au-dessus de θ₃ | Peut rester 0 sous bruit |
| **excess3** | Synergie irréductible continue | Primaire en régimes bruités |

ΔRECD est modulé par l’intensité de réorganisation λ (souvent liée à |τ_s|).

---

## 3. Standard de reporting

Rapporter :

- mean_excess3 et Δexcess3 (continu primaire) ;  
- occupation de Φ₃ si utilisée ;  
- valeur de θ₃ ;  
- lien à la trajectoire τ_s et au design d’événement.

---

## 4. Micro-contrôle

Expliquer en trois phrases pourquoi Φ₃=0 n’implique pas « pas de synergie » lorsque excess3 bouge.

---

*Fondements 03 · STP v1.1*
