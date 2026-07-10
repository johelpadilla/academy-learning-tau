# Fondements — Tau systémique (τ_s)

| Champ | Valeur |
|-------|--------|
| **Module** | Fondements 01 |
| **Niveau** | Postgraduate |
| **Version** | 1.1 · 2026 |
| **Handouts liés** | Théorie · Mathématiques pratiques · Lecture duale |

---

## Objectifs d’apprentissage

1. Énoncer la question scientifique de τ_s en une phrase sans « prédire ».  
2. Contraster la mesure ordinale–relationnelle avec l’amplitude/ralentissement univarié.  
3. Lister les éléments de design requis (N, W, événement, nulls) pour un Δτ_s défendable.

---

## 1. Objet scientifique

**Tau systémique (τ_s)** mesure comment la **structure d’ordre partagée** entre les variables d’un système multivarié se réorganise dans le temps. Elle ne demande pas d’abord l’ampleur des fluctuations de chaque canal, mais comment les **relations d’ordre** entre canaux changent autour d’un basculement de régime.

Opérationnellement (pipeline pédagogique Lab v1.0) :

1. Série multivariée \(X\in\mathbb{R}^{T\times N}\) (ou proxy bivarié documenté).  
2. Fenêtres glissantes de longueur \(W\) avec pas `stride`.  
3. Motifs ordinaux locaux (Bandt–Pompe / rangs).  
4. Résumé de cohérence ordinale croisée → \(\tau_s(t)\).  
5. Contraste Δ (pre/post événement ou moitié/moitié) sous nulls de surrogates.

---

## 2. Pourquoi ordinal et relationnel ?

| Propriété | Implication |
|-----------|-------------|
| Ordinal | Robuste aux transforms strictement monotones |
| Relationnel | Cible la réorganisation du couplage, pas seulement le CSD univarié |
| En fenêtres | Capture la dynamique, pas un coefficient statique unique |
| Sensible au null | Le phase-shuffle teste la structure croisée résiduelle |

---

## 3. Ce que τ_s n’est pas

- Pas un simple renommage marketing du Kendall-τ statique.  
- Pas la Transfer Entropy (prédiction directionnelle).  
- Pas un prédicteur certifié d’événements cliniques ou de marché.  
- Pas un substitut de la théorie de domaine.

---

## 4. Lire τ_s en pratique

Toujours avec :

1. Taille d’effet (magnitude et signe de Δτ_s).  
2. Panneau EWS classique (lecture duale).  
3. p_surr + méthode + n_surr + seed.  
4. Énoncé de maturité de domaine.  
5. `repro_hash`.

**Signe context-dependent :** hausse ou baisse de τ_s peuvent indiquer une réorganisation selon le régime.

---

## 5. Micro-contrôle

- [ ] J’explique τ_s sans revendiquer la prédiction.  
- [ ] Je sais pourquoi N≥2 (ou proxy) est requis.  
- [ ] Je ne publierai pas p sans Δ et design.

---

*Fondements 01 · STP v1.1*
