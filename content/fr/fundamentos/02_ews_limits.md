# Le Problème des Signaux d'Alerte Précoce Classiques

## La Promesse des EWS Classiques

La théorie des **transitions critiques** prédit qu'à l'approche d'un point de bifurcation, de nombreux systèmes présentent un *ralentissement critique* (Critical Slowing Down - CSD) : la récupération après des perturbations devient plus lente. Dans les séries temporelles univariées, cela se traduit souvent par :

| Métrique | Signature attendue près de la transition |
|---------|----------------------------------------|
| Variance | ↑ augmentation |
| Autocorrélation Lag-1 (AR1) | ↑ s'approche de 1 |
| Spectre de puissance | plus d'énergie dans les basses fréquences |
| DFA / Hurst | plus grande mémoire à long terme |

Ces métriques se sont avérées utiles en écologie, en climatologie et dans certains modèles synthétiques. Le problème se pose dans les **systèmes vivants réels, bruyants et multivariés**.

## Où Ils Échouent en Pratique

### 1. Hypothèse Univariée / CSD Simple

De nombreuses transitions biologiques ne se comportent **pas** comme un potentiel unique avec un paramètre de contrôle qui glisse en douceur. Le cœur, le cerveau ou une épidémie réorganisent des **réseaux de relations**. La variance d'une seule série peut augmenter, diminuer ou rester inchangée, tandis que la **structure croisée** change fondamentalement.

### 2. Signes Inversés ou Non Informatifs

Dans le pilote CCTP sur le Holter pré-FV (SDDB) :

- La **variance** a tendance à augmenter (signature "classique").
- L'**AR(1)** **chute** fréquemment — contrairement au CSD naïf.
- τ_s et excess3 capturent la **direction de la réorganisation relationnelle**, qui dépend du **contexte** (pas toujours le même signe).

Interpréter "l'AR1 n'a pas augmenté ⇒ pas d'alerte" serait un faux négatif méthodologique.

### 3. Sensibilité aux Non-linéarités Monotones et à l'Échelle

Les métriques basées sur les moments (moyenne, variance) dépendent de l'échelle et des transformations. Les mesures **ordinales** sont invariantes aux transformations monotones et s'alignent mieux avec le concept de "modèle d'ordre" du système.

### 4. Confusion Entre Bruit, Pacing et Pathologie

Dans les ECG réels, il y a du pacing intermittent, de la FA (Fibrillation Auriculaire) et des artefacts d'annotation. Les EWS univariés réagissent à tout cela. Un cadre relationnel + des indicateurs de qualité permettent de **conserver** les cas difficiles sans détruire le signal (comme dans le CCTP).

### 5. Absence d'une Théorie du "Temps du Système"

Les EWS classiques vivent dans le temps de l'horloge du laboratoire (secondes, semaines). Ils ne modélisent pas le **temps interne** du système : à quel moment un instant significatif de réorganisation "avance". Le RECD cible précisément cette lacune.

## Tableau Comparatif (Pédagogique)

| Critère | EWS Classiques | Tau Systémique + RECD |
|----------|--------------|----------------------|
| Unité d'Analyse | Univariée (typique) | Multivariée / relationnelle |
| Observables | Moments, corrélations linéaires | Modèles ordinaux, conjonctions |
| Hypothèse de Trajectoire | CSD générique | Réorganisation relationnelle (signe contextuel) |
| Temps | Chronologique externe | RECD (temps extramental discret) |
| Validation Nulle | Bootstrap simple | Surrogates de phase / IAAFT brisant la dépendance croisée |
| Interprétabilité | Moyenne | Élevée (Φ₁–Φ₃, excess3) |

## Message Clé

> Les EWS classiques ne sont pas "faux" : ils sont **incomplets** pour les systèmes où la transition est une **réorganisation des relations**, et non un simple ralentissement d'une variable.

Le Tau Systémique et le RECD ne remplacent pas la physique des bifurcations ; ils **complètent le tableau de bord** avec des observables alignés sur cette réorganisation.
