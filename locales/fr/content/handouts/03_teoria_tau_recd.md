# Théorie — Tau systémique, RECD et lecture duale

| Champ | Valeur |
|-------|--------|
| **Document** | Handout 03 · Théorie |
| **Public** | Postgraduate · enseignants · lecteurs des papers du paradigme |
| **Usage** | Complète les Fondements dans l’app ; imprimable / LMS |
| **Version** | 1.1 · 2026 |
| **Prérequis** | Séries temporelles intermédiaires ; corrélation et processus |

---

## Objectifs d’apprentissage

1. Énoncer la **question relationnelle** de τ_s face à la question univariée des EWS.  
2. Décrire le pipeline fenêtre → motifs ordinaux → τ_s(t) → RECD/excess3.  
3. Interpréter p_surr sous *phase-shuffle* sans réduire l’évidence à un seul p.  
4. Appliquer la **lecture duale** (concordance / discordance / quietude).  
5. Borner les revendications selon la **maturité empirique** du domaine.

---

## 1. La question scientifique

Les *early warning signals* (EWS) classiques, motivées par le *critical slowing down* (CSD ; Scheffer et al.), demandent essentiellement :

> Combien chaque variable bouge-t-elle ? La récupération après perturbation ralentit-elle ?

**Tau systémique (τ_s)** pose une autre question :

> **Comment la structure d’ordre partagée entre les variables du système se réorganise-t-elle autour d’un changement de régime ?**

Dans les systèmes vivants et socio-écologiques, la transition est souvent un **changement de loi relationnelle** (couplage, synergie, habitudes de co-ordre), pas seulement un ralentissement univarié. D’où τ_s **ordinal** et **relationnel**.

### 1.1 Ce que τ_s n’est pas

| Confusion fréquente | Clarification postgraduate |
|---------------------|----------------------------|
| « Kendall-τ avec marketing » | Partage un substrat de rangs, mais opère en **fenêtres**, est multivarié, se couple à l’horloge RECD et se lit sous nulls de dépendance croisée. |
| « Causalité / Transfer Entropy » | TE demande la prédiction directionnelle A→B. τ_s demande la réorganisation de structure conjointe. Elles sont **complémentaires**. |
| « Prédit mort / épidémie / crise » | Cadre de **recherche et d’enseignement**. Pas un dispositif certifié. |
| « Remplace la physiologie / l’épidémiologie » | Fournit un **observable de couplage** ; ne remplace pas le savoir de domaine. |

---

## 2. Observables, fenêtre et définition opérationnelle

Soit \(X \in \mathbb{R}^{T \times N}\) avec \(N \ge 2\) (ou un proxy bivarié légitime, p.ex. \(z(\mathrm{RR}),\, z(|\Delta\mathrm{RR}|)\) dans le motif CCTP).

Dans une fenêtre de longueur \(W\) avec pas `stride` :

1. Construire des **motifs d’ordre** locaux (Bandt–Pompe / rangs) avec \(m\) et \(\tau\).  
2. Résumer la **cohérence ordinale croisée** en un scalaire \(\tau_s(t)\).  
3. La trajectoire \(\tau_s(t)\) peut accélérer, s’inverser ou se stabiliser lors d’une réorganisation — **pas nécessairement** quand la variance univariée monte.

**Définition pédagogique (Lab v1.0) :** \(\tau_s\) se relie à un résumé (p.ex. moyenne de coefficients de rang par paires dans la fenêtre) de la structure ordinale partagée. La revendication scientifique porte sur la **dynamique de réorganisation** (Δ, nulls, lecture duale), non sur un seul coefficient statique.

### 2.1 Paramètres typiques (presets v1.0)

| Domaine | W | stride | θ₃ (indicatif) | Note |
|---------|---|--------|----------------|------|
| Cardiologie | 101 | 5 | 0.08 | Ancre empirique CCTP |
| Épidémiologie | 13 | 1 | 0.10 | Séries souvent courtes |
| Neurosciences / sommeil | 51 | 2 | 0.10 | Multi-canal |
| Écologie | 25 | 1 | 0.10 | Transfert méthodologique |
| Climat / social / finance | 21 | 1 | 0.10 | Sandbox / maturité basse–moyenne |
| Éducation (cohorte) | 17 | 1 | 0.10 | Méta-pédagogie |
| Synthétique | 31 | 2 | 0.10 | Contrôles de conception |

Documentez toujours W, stride, m, delay et θ₃ ; le **`repro_hash`** les scelle.

---

## 3. RECD — horloge extramentale discrète

**RECD** formalise un temps émergent du système (**Kairos**) distinct de l’index du CSV (**Chronos**).

### 3.1 Niveaux de conjonction ordinale

| Niveau | Idée formelle-intuitive | Piège d’interprétation |
|--------|-------------------------|------------------------|
| **Φ₁** | Coïncidence de symboles entre paires en \(t\) | Φ₁ élevé ≠ « émergence » |
| **Φ₂** | Persistance de relations par paires (≥ \(d\) pas ; typ. d=4) | Habitude relationnelle, pas un flash |
| **Φ₃** | Indicateur binaire de synergie au-dessus de θ₃ | Peut rester à 0 sous bruit |
| **excess3** | Proxy **continu** de synergie irréductible | Métrique primaire en régimes bruités (CCTP) |

En données réelles, **mean_excess3** et **Δexcess3** sont souvent plus informatifs que le bit Φ₃.

L’avance de l’horloge (ΔRECD) est modulée par l’intensité de réorganisation \(\lambda\) (liée en pratique à \(|\tau_s|\) et au régime).

### 3.2 Chronos vs Kairos

| Concept | Sens opérationnel dans STP |
|---------|----------------------------|
| Chronos | Index temporel d’échantillonnage (ligne CSV) |
| Kairos | Temps pondéré par les ticks de réorganisation (RECD) |

Ne confondez pas « l’événement est à t=500 » (Chronos) et « l’horloge du système a accéléré » (Kairos).

---

## 4. Surrogates — le null relationnel

Question : *le Δ observé est-il compatible avec l’indépendance croisée en préservant les spectres univariés ?*

| Méthode | Préserve | Rompt | Usage v1.0 |
|---------|----------|-------|------------|
| **Phase-shuffle** (défaut) | Spectre par canal (approx.) | Dépendance croisée | Null relationnel naturel |
| **IAAFT** (optionnel) | Spectre + histogramme (itératif) | Dépendance croisée (plus strict) | Mode full / sensibilité |

### 4.1 Lecture conjointe effet × null

| Δ (effet) | p_surr | Lecture postgraduate |
|-----------|--------|----------------------|
| Grand | Bas (p.ex. ≤0.05) | Candidat à structure relationnelle résiduelle |
| Grand | Haut | Ne revendiquez pas la détection ; revoir W, preprocess, N |
| Petit | Bas | Petit effet stable — prudence de domaine |
| Petit | Haut | Compatible avec le null ; utile comme **contrôle** |

**Ne publiez jamais** le p seul sans taille d’effet, design, n_surr, seed et maturité du domaine.

---

## 5. Lecture duale (obligatoire en enseignement et remises sérieuses)

Tout résultat sérieux se présente en **deux colonnes** :

1. **Panneau relationnel :** τ_s, RECD, excess3, p_surr.  
2. **Panneau classique :** var, AR(1) ou autres EWS univariées sous le même design.

### 5.1 Pourquoi c’est méthodologiquement nécessaire

- Les EWS classiques peuvent être ambiguës si la transition est multivariée.  
- τ_s peut bouger quand var/AR1 n’« alertent » pas — et inversement.  
- La science utile déclare **concordance, discordance ou quietude**.

### 5.2 Signe *context-dependent*

Δτ_s ou Δexcess3 peuvent **monter ou baisser** vers un événement selon le régime. L’évidence se joue sur magnitude, concordance, nulls et récit de domaine — pas sur un panneau universel « positif = mauvais ».

---

## 6. Maturité empirique (v1.0)

| Niveau | Domaines / matériaux | Implication pour les claims |
|--------|----------------------|-----------------------------|
| **Ancre** | Cardiologie CCTP / SDDB (pilote documenté) | Claims plus forts, encore de recherche ; N limité |
| **Transfert** | Épidémiologie (narratif + démos) | Hypothèses transferables ; valider hors plateforme |
| **Sandbox pédagogique** | Climat, éducation, social, sommeil, finance, synthétiques | *Ground truth* de **conception** ; enseignent la méthode |

**Règle d’or :** ne vendez pas la force du pilote cardio comme validation de polarisation sociale ou de trading.

---

## 7. Reproductibilité et citation

Chaque course du Lab produit un **`repro_hash`** (SHA-256). Pour citer un nombre :

1. Paper/preprint de domaine.  
2. Logiciel (STP v1.0 / bibliothèques alignées).  
3. Dataset original et licence.  
4. Hash de la course + Methods exportés.

---

## 8. Glossaire minimal

| Terme | Définition opérationnelle |
|-------|---------------------------|
| **τ_s** | Thermomètre de réorganisation relationnelle ordinale en fenêtres |
| **RECD** | Horloge de ticks de réorganisation (Kairos) |
| **excess3** | Synergie ordinale continue (primaire sous bruit) |
| **Bandt–Pompe** | Alphabet de m! motifs d’ordre (m=3 → 6) |
| **EWS** | Signaux précoces univariés (panneau de contrôle) |
| **CSD** | *Critical slowing down* (cadre classique) |
| **p_surr** | Extrémalité du Δ sous null de surrogates |

---

## 9. Lectures de contexte (non exhaustif)

- Bandt & Pompe — entropy de permutation / motifs ordinaux.  
- Scheffer et al. — transitions critiques / CSD / EWS.  
- Nulls spectraux (randomisation de phase) et IAAFT.  
- Papers/preprints de domaine (p.ex. CCTP).  
- Documentation des datasets (PhysioNet SDDB, etc.).

---

## 10. Auto-contrôle théorique (5 items)

1. Puis-je énoncer la question de τ_s sans le mot « prédit » ?  
2. Pourquoi excess3 peut-il importer plus que Φ₃ ?  
3. Que rompt et que préserve le phase-shuffle ?  
4. Qu’est-ce qu’une discordance relationnelle–classique légitime ?  
5. Quelle revendication **ne puis-je pas** faire avec une démo synthétique ?

---

*Handout théorique STP v1.1 · complète l’app · usage académique avec citation.*
