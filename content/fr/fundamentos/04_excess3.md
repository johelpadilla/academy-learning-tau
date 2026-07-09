# Le Concept d'"Excès de Niveau 3" (excess3)

## Définition

L'**excess3** est un **proxy continu de la synergie ordinale irréductible** dans une fenêtre locale de symboles multivariés. Il répond à la question :

> Quelle est la quantité de structure conjointe **au-delà** de ce qui serait expliqué par les variables séparément et leurs interactions par paires ?

Ce n'est pas un test de causalité. C'est une **jauge d'irréductibilité symbolique** alignée sur l'ontologie du Niveau 3 du RECD.

## Construction (Schéma)

Étant donné la matrice de symboles \(S \in \{0,\ldots,m!-1\}^{T \times N}\) (Bandt–Pompe) :

1. Dans une fenêtre de longueur \(w\) :
   - Estimer \(H(\pi^1,\ldots,\pi^N)\) (entropie conjointe).
   - Estimer \(\sum_i H(\pi^i)\) (marginales).
   - Estimer la MI moyenne par paires.
2. Corrélation totale approchée : \(TC \approx \sum_i H_i - H_{\mathrm{joint}}\).
3. Soustraire une contribution par paire (heuristique transparente) → **synergie résiduelle**.
4. (Optionnel) Ajouter la **surprise conjointe** (joint surprise) : configurations conjointes plus fréquentes que prévu sous l'indépendance des marginales.
5. Combiner (ex. \(0.6\cdot\mathrm{syn} + 0.4\cdot\mathrm{surprise}\)) → **excess3(t)**.

La version binaire du Niveau 3 est simplement :

\[
\Phi_3(t) = \mathbf{1}\{\mathrm{excess3}(t) > \theta_3\}
\]

## Pourquoi Préférer la Métrique Continue dans les Données Réelles

Dans le pilote cardiaque CCTP (RR bruyant, N=10 enregistrements SDDB) :

- excess3 de base ≈ 0,30–0,35 ; pendant l'approche, il peut monter vers ~0,43 (ex. enregistrement 38).
- Avec des seuils élevés, le **taux** de "Niveau 3 élevé" peut rester à zéro même si le **delta d'excess3** est très significatif.
- C'est pourquoi la métrique principale de l'article est le **mean_excess3** (et son Δ), et pas seulement le `high_level3_rate`.

**Règle Pédagogique de la Plateforme :**

| Situation | Utiliser |
|-----------|------|
| Séries synthétiques propres | Φ₃ binaire + excess3 |
| Physiologie / terrain bruyant | **excess3 continu** comme principal |
| Rapports institutionnels | Les deux + intervalles / valeurs p des surrogates |

## Interprétation des Signes et des Deltas

Tout comme τ_s, le **signe de Δexcess3** dépend du **contexte** :

- Une augmentation peut indiquer l'**émergence d'une configuration conjointe** pré-transition.
- Une diminution peut indiquer un **effondrement ou une simplification** de la structure synergique (ex. régimes stimulés ou états terminaux distincts).

Ce qui est scientifiquement pertinent dans le CCTP n'est pas qu'il "augmente toujours", mais plutôt :

1. **Ampleur du changement** de la ligne de base → approche.
2. **Concordance de signe** avec Δτ_s.
3. **Significativité** par rapport aux surrogates "phase-shuffle" (qui préservent les spectres univariés mais détruisent la dépendance croisée).

## Analogie

Si Φ₁ est "chanter la même note" et Φ₂ est "maintenir un duo stable", excess3 est le résidu d'une **polyphonie** qui ne peut être factorisée en solos ou en duos. Lorsque ce résidu change de manière soutenue, le système est en train de réécrire sa **grammaire conjointe**.

## Relation avec d'Autres Approches

| Approche | Proximité avec excess3 | Différence |
|---------|-------------------|------------|
| Transfer Entropy (Entropie de Transfert) classique | Moyenne | La TE est directionnelle et souvent à valeurs réelles, pas nécessairement ordinale imbriquée |
| Total correlation / PID | Élevée | excess3 est un proxy chirurgical orienté vers le RECD, et non une décomposition PID complète |
| TDA (Betti) | Complémentaire | La TDA voit la topologie du nuage de points ; excess3 voit la synergie symbolique temporelle |
| Caractéristiques ML (Machine Learning) | Faible | excess3 est interprétable et réfutable avec des surrogates |

## Paramètres Recommandés (Plateforme v1.0)

| Domaine | θ₃ | w_φ | Notes |
|---------|-----|-----|-------|
| Cardio RR | 0.08 | 101 | recalibré CCTP |
| Dengue (hebdomadaire) | 0.10 | 13 | défaut théorique |
| Synthétiques | 0.10 | 13 | balayages (sweeps) de Feigenbaum |
| Puissance de bande EEG | 0.08–0.12 | à explorer | forte sensibilité au prétraitement |
