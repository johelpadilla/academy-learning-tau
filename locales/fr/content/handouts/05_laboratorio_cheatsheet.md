# Cheat-sheet du Laboratoire STP

| Champ | Valeur |
|-------|--------|
| **Document** | Handout 05 · Cheat-sheet Lab |
| **Usage** | Imprimer une face · garder à côté de l’écran en cours |
| **Niveau** | Opérations de labo postgraduate |
| **Version** | 1.1 · 2026 |

---

## Flux

```
Données (catalogue | CSV) → Domaine + événement → Paramètres → Analyser
    → Séries · τ_s · RECD · EWS · Extensions (BW/TDA) · lecture duale
    → Export MD/JSON/Methods + hash
```

**Extensions (opérationnelles) :** cases Breathing / TDA / Mémoire — actives par défaut en mode **Full**.

---

## Presets (W / stride / θ₃)

| Domaine | W | stride | θ₃ |
|---------|---|--------|-----|
| Cardiologie | 101 | 5 | 0.08 |
| Épidémiologie | 13 | 1 | 0.10 |
| Neuro / sommeil | 51 | 2 | 0.10 |
| Écologie | 25 | 1 | 0.10 |
| Climat / social / finance | 21 | 1 | 0.10 |
| Éducation | 17 | 1 | 0.10 |
| Synthétique | 31 | 2 | 0.10 |

m=3, delay=1 par défaut en v1.0. Documentez tout écart.

---

## Démos que l’étudiant doit connaître

| ID | Pour quoi |
|----|-----------|
| `synthetic_coupled_logistic` | Signal fort (contrôle positif) |
| `synthetic_ar_noise` | Quasi-nul (contrôle négatif) |
| `sddb_rr_38_demo` | Ancre cardio (si sample présent) |
| `dengue_like_demo` | Transfert épi |
| `education_cohort_demo` | Méta-pédagogie |
| `climate_drought_demo` | Jouet CSD climatique |

---

## Lecture rapide des sorties

| Sortie | Question à laquelle elle répond |
|--------|----------------------------------|
| τ_s(t) | Quand le couplage ordinal se réorganise-t-il ? |
| Δτ_s | Combien a changé pre/post (ou moitié/moitié) ? |
| excess3 / Δ | La synergie irréductible bouge-t-elle ? |
| Φ₃ | A-t-elle franchi le seuil ? (peut rester 0) |
| p_surr | Le Δ est-il extrême sous null d’indépendance croisée ? |
| var / AR1 | Le panneau classique raconte-t-il la même histoire ? |
| W(t) | Résolution breathing (si actif) |
| β₀ / β₁ | Proxy topologique du cloud d’états (si TDA) |
| hash | Puis-je régénérer cette course ? |

---

## Surrogates (indicatif)

| Usage | n_surr |
|-------|--------|
| Démo en cours | 4–8 |
| Exploration sérieuse | 20–50 |
| À citer | ≥50 + sensibilité à la seed |

Défaut : **phase_shuffle**. IAAFT pour un null plus strict (plus lent).

---

## Export minimal d’une remise

1. `rapport.md`  
2. `resultat.json`  
3. Paragraphe Methods  
4. Hash copié dans le PDF/LMS  
5. Paragraphe de lecture duale (Handout 06)

---

## Formulations interdites (sans évidence)

- « Prédit la mort subite / l’épidémie / le crash. »  
- « p<0.05 donc le système s’effondre. »  
- « Démo finance ⇒ stratégie de trading. »  
- « Démo polarisation ⇒ vérité sociale. »  
- « Le pilote CCTP valide le climat / la classe. »

---

## Formulations autorisées (avec nuances)

- « Δτ_s = … ; p_surr = … sous phase-shuffle (n=…, seed=…). »  
- « Le panneau EWS était ambigu / concordant à …. »  
- « Démo synthétique avec *ground truth* de conception ; pas une cohorte clinique. »  
- « Maturité du domaine : … ; l’extrapolation exige une validation externe. »  
- « Métrique continue primaire : mean_excess3 / Δexcess3 (Φ₃ resté à 0). »

---

## Raccourcis mentaux de qualité

1. Contrôle positif et négatif dans la même séance ?  
2. Événement déclaré (ou moitié/moitié exploratoire) ?  
3. Preset ou W justifiée ?  
4. Lecture duale écrite ?  
5. Hash + Methods présents ?  
6. Claims bornés par la maturité ?

Si l’un échoue, la remise n’est pas prête.

---

*STP Lab cheat-sheet v1.1*
