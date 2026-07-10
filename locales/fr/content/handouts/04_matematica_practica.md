# Mathématiques pratiques — Bandt–Pompe, τ_s et RECD

| Champ | Valeur |
|-------|--------|
| **Document** | Handout 04 · Mathématiques pratiques |
| **Public** | Après le guide rapide ; sandbox Math / Lab |
| **Objectif** | Calculer et interpréter sans sauter l’alphabet ordinal |
| **Niveau** | Méthodes quantitatives postgraduate |
| **Version** | 1.1 · 2026 |

---

## Objectifs d’apprentissage

1. Construire des symboles Bandt–Pompe pour m=3 et expliquer l’invariance monotone.  
2. Énoncer le pipeline opérationnel de \(X\) vers τ_s et RECD/excess3.  
3. Décrire le phase-shuffle comme null de dépendance croisée.  
4. Compléter la checklist numérique avant toute revendication publique.

---

## 1. Ordre d’apprentissage (ne sautez pas d’étapes)

| # | Bloc | Une phrase | Où |
|---|------|------------|-----|
| 1 | Bandt–Pompe | m! motifs d’ordre locaux | Mathématiques (sandbox) |
| 2 | τ_s | Thermomètre relationnel en fenêtres | Lab |
| 3 | Φ₁–Φ₃ + excess3 | Horloge emboîtée et synergie | Fondements + Lab |
| 4 | EWS classiques | Panneau univarié de contrôle | Lab |
| 5 | Surrogates | Nulls de dépendance croisée | Lab (`n_surr`) |
| 6 | Breathing / mémoire / TDA | Extensions opérationnelles | Lab · mode Full |

**Règle :** si vous ne pouvez pas dessiner Bandt–Pompe au tableau, n’interprétez pas excess3.

---

## 2. Notation

| Symbole | Signification | Typique v1.0 |
|---------|---------------|--------------|
| \(X\in\mathbb{R}^{T\times N}\) | Série multivariée | N≥2 |
| \(m,\tau\) | Dimension et délai ordinal | m=3, delay=1 |
| \(W\), stride | Fenêtre et pas | voir presets |
| \(\Phi_1,\Phi_2,\Phi_3\) | Niveaux de conjonction | [0,1] / binaire |
| excess3 | Synergie continue | primaire sous bruit |
| \(\theta_3\) | Seuil de Φ₃ | 0.08 cardio ; ~0.10 autres |
| \(\lambda\) | Intensité de réorganisation | liée à \|τ_s\| |
| p_surr | p de surrogate pour Δ | rapporter méthode + n |

---

## 3. Bandt–Pompe en 90 secondes

Pour une fenêtre de m points avec délai \(\tau\) :

1. Prendre \(x_t, x_{t+\tau},\ldots,x_{t+(m-1)\tau}\).  
2. Ordonner les valeurs : le **motif de rangs** est un symbole dans \(\{0,\ldots,m!-1\}\).  
3. Avec m=3 il y a **6** symboles.

### Propriété clé

Invariance sous transformations **strictement monotones**. Après un preprocess honnête, le paradigme est robuste aux échelles différentes entre canaux.

### Exercice au tableau

Série : `3, 1, 4, 2` avec m=3, delay=1.

- Triplet (3,1,4) → motif de permutation.  
- Triplet (1,4,2) → autre symbole.  
Comptez les fréquences sur une fenêtre plus longue dans le sandbox.

### Égalités (ties)

Définissez et rapportez une politique de rupture d’égalité. Des ties non documentés sont un défaut de méthodes.

---

## 4. Des symboles à τ_s (intuition opérationnelle)

1. Chaque canal est symbolisé (Bandt–Pompe).  
2. Dans la fenêtre, mesurer **cohérence / réorganisation** entre canaux.  
3. Obtenir \(\tau_s(t)\) au fil du temps.  
4. Avec un **événement**, calculer Δ pre/post ; sinon 1ʳᵉ vs 2ᵉ moitié (déclarer le design exploratoire).

### Contrôles mentaux

- **Contrôle positif :** logistiques couplés avec switch → grand |Δτ_s|.  
- **Contrôle quasi-nul :** AR indépendants → petit |Δτ_s|.  
- Si votre démo « appliquée » ressemble à l’AR, ne forcez pas un récit de réorganisation.

---

## 5. RECD et excess3 (formules en mots)

### Φ₁
Fraction normalisée de paires partageant le **même symbole** à t. Base statistique ; insuffisante seule.

### Φ₂
Relations par paires qui **persistent** au moins \(d\) pas (typ. d=4). Habitudes, pas des éclairs.

### excess3
Proxy continu de **synergie irréductible**. Alimente la décision de Φ₃.

### Φ₃
1 si excess3 > θ₃ ; sinon 0. Sous bruit, peut rester éteint pendant qu’excess3 bouge : **rapportez le continu**.

### ΔRECD
Accumulation de ticks de réorganisation modulés par le régime. Opérationnalise Chronos vs Kairos.

---

## 6. Surrogates — mathématiques du null

**Phase-shuffle indépendant par canal**

1. FFT du canal.  
2. Aléatoriser les phases.  
3. IFFT → densité spectrale approx. préservée, dépendance croisée détruite.

Si le Δ des données est extrême vs la distribution des Δ de surrogates, p_surr est bas : évidence que la structure **croisée** compte.

**IAAFT** itère aussi sur l’histogramme d’amplitudes ; plus coûteux ; utile en mode full.

### Standard de reporting

Méthode, n_surr, seed, quel Δ testé (τ_s et/ou excess3), politique uni/bilatérale si pertinente.

---

## 7. Checklist numérique avant un claim

- [ ] N ≥ 2 (ou proxy documenté)  
- [ ] W et stride justifiés  
- [ ] m, delay fixés et rapportés  
- [ ] Événement ou partition exploratoire **déclarée**  
- [ ] Δτ_s et Δexcess3 avec signe et magnitude  
- [ ] p_surr avec n_surr et méthode  
- [ ] Panneau EWS en parallèle  
- [ ] Hash et Methods exportés  

---

## 8. Erreurs mathématiques fréquentes

| Erreur | Correction |
|--------|------------|
| Lire τ_s comme corrélation de Pearson | C’est ordinal–relationnel en fenêtres |
| Publier seulement Φ₃ | Préférer excess3 + Φ₃ |
| n_surr = 2 pour un paper | Utiliser des dizaines + sensibilité à la seed |
| Comparer des domaines avec W différents sans le dire | L’échelle temporelle de l’horloge change |
| Traiter des démos synthétiques comme cohortes de terrain | *Ground truth* de conception ≠ évidence de terrain |
| Cacher la politique de ties / manquants | Méthodes incomplètes |

---

## 9. Complexité (ordre de grandeur)

| Bloc | Ordre de coût |
|------|---------------|
| Bandt–Pompe univarié | \(O(T \cdot m \log m)\) (m=3 bon marché) |
| Φ₁ | \(O(T \cdot N^2)\) |
| Φ₂ | \(O(T \cdot N^2 \cdot d)\) |
| excess3 | croît avec les fenêtres de comptage ; N petit, m=3 faisable |
| Surrogates | × n_surr le coût de la métrique |

---

## 10. Fast vs Full (politique numérique)

| Bloc | Fast (cours / exploration) | Full (type paper) |
|------|----------------------------|-------------------|
| τ_s + RECD | Oui | Oui |
| EWS classiques | Oui | Oui |
| Surrogates | n≈8 | n≥50 (recommandé) |
| TDA Betti | Optionnel | Oui (défaut Full) |
| Breathing | Optionnel | Oui (défaut Full) |

**Règle :** explorer en Fast ; confirmer en Full avant de citer un p-valeur.

---

*Handout de mathématiques pratiques STP v1.1 · à utiliser avec le sandbox Mathématiques.*
