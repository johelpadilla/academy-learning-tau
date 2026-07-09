# Domaine : Cardiologie Computationnelle — pré-FV et SDDB

## 1. Contexte Scientifique

La **mort subite cardiaque** par **fibrillation ventriculaire (FV)** reste difficile à anticiper à partir de l'ECG de surface. Les enregistrements Holter de la *Sudden Cardiac Death Holter Database* (SDDB, PhysioNet) constituent l'une des rares ressources publiques avec des heures de dynamique pré-événement et un déclenchement documenté de la FV.

Le **Protocole des Transitions Critiques Cardiaques (CCTP)** applique le Tau Systémique et le RECD ordinal aux séries d'**intervalles RR** pour caractériser la réorganisation relationnelle de la dynamique de la fréquence cardiaque **avant** une FV spontanée.

## 2. Pourquoi les Métriques Classiques sont Insuffisantes

Dans la cohorte CCTP (N=10 enregistrements de haute qualité) :

- La **variance** RR a tendance à augmenter (signature de "type CSD").
- L'**AR(1)** **diminue** fréquemment — un comportement d'*anti-persistance* directement opposé à l'attente naïve du *ralentissement critique* (CSD).
- L'interprétation de var/AR1 seuls produit des lectures confuses ou des faux négatifs conceptuels, étant donné que la dynamique pré-FV ne suit pas un attracteur unique, mais présente des divergences abruptes.
- Il y a un **pacing intermittent** et un bruit synaptique inhérent (avec des niveaux de bruit allant jusqu'à 20%). Ce bruit n'est pas une simple "erreur à effacer" ; le Tau Systémique démontre une **invariance topologique** et une robustesse que les métriques classiques ne possèdent pas.

## 3. Valeur Différentielle de τ_s + RECD

| Ingrédient | Rôle dans le CCTP |
|-------------|-------------|
| Proxy \(X = [z(\mathrm{RR}),\, z(\|\Delta\mathrm{RR}\|)]\) | Multivarié minimum physiologiquement motivé |
| τ_s (W=101, stride=5) | Couplage ordinal entre le niveau et la variabilité battement par battement |
| Φ₁–Φ₃ + **excess3** | Décomposition de la structure symbolique ; excess3 comme principal |
| Surrogates phase-shuffle | Modèle nul préservant les spectres et détruisant la dépendance croisée |
| Signe dépendant du contexte | Réorganisation, pas "la métrique augmente toujours" |

**Découvertes clés du CCTP (validation empirique) :** 
1. Δτ_s et Δexcess3 sont significatifs sous les surrogates *phase-shuffle* (qui détruisent la dépendance croisée tout en préservant le spectre de fréquences).
2. Un **taux de faux positifs 3,8 fois inférieur** et une fenêtre d'alerte précoce **2,3 fois plus grande** ont été observés par rapport à l'exposant de Lyapunov local et au coefficient de Pearson.
3. L'horloge extramentale dans le cœur a présenté une émergence spontanée avec une **dimension fractale constante de ≈1,98**.

## 4. Jeu de Données d'Exemple

- **Source :** PhysioNet SDDB + RR propres du référentiel CCTP.
- **Échantillon de la plateforme :** enregistrements 38 (signal fort) et 51 (pacing intermittent).
- **Colonnes :** `rr_ms`, `abs_drr`, `z_rr`, `z_abs_drr`.
- **Événement :** index de déclenchement de la FV (`vfon`) lorsqu'il est disponible.

## 5. Interprétation Guidée

1. Inspecter la qualité : `interp_frac`, indicateurs de pacing.
2. Regarder τ_s dans la fenêtre de base vs. l'approche (~3 h pré-événement).
3. Regarder le mean excess3 et son Δ (pas seulement Φ₃ binaire).
4. Contraster avec var et AR1 (onglet EWS).
5. Exiger les valeurs p des surrogates avant de revendiquer une "alerte".

## 6. Références

- Padilla-Villanueva — CCTP/SDDB (Zenodo 10.5281/zenodo.21270699).
- Goldberger et al., PhysioNet / SDDB.
- Greenwald (1986) — fondation de la SDDB.
