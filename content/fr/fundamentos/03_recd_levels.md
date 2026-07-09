# RECD : Trois Niveaux de Conjonctions Ordinales (Φ₁, Φ₂, Φ₃)

## Qu'est-ce que le RECD ?

L'**Horloge Extramentale Discrète (RECD)** postule que le temps extramental n'est pas un continuum absolu newtonien (*Chronos*), mais plutôt une **séquence discrète et fractale de conjonctions ordinales** qui émerge dans la plage chaotique (\(|\tau_s| < 0.41\)), régie par la constante de Feigenbaum (\(\delta \approx 4.6692016\)).

Cette construction est hiérarchique et échelonnée en **quatre niveaux ontologiques principaux** (Niveau 0 à Niveau 3). Chaque niveau supérieur **ajoute de l'irréductibilité** : il ne nie pas le niveau inférieur ; il l'englobe et en émerge sans nécessiter de substrat temporel externe.

---

## Niveau 0 — Micro-conjonctions Locales

**Idée :** Correspond aux concordances ordinales élémentaires entre des paires de composantes du système.
- Formulation : \( C_{ij}^{(0)} = \tau_k(r_i, r_j) \)
- À ce niveau, **le temps n'existe pas encore** ; seules existent des relations ordinales intemporelles.

---

## Niveau 1 — Conjonctions Systémiques (Φ₁)

**Idée :** Deux variables ou plus partagent-elles le **même symbole ordinal** au même instant ?

Après l'intégration (embedding) de Bandt–Pompe (dimension \(m\), délai \(\tau\)), chaque variable \(i\) produit un symbole \(\pi_t^{(i)}\) (l'une des \(m!\) permutations).

\[
\Phi_1(t) = \frac{2}{N(N-1)} \sum_{i < j} \mathbf{1}\!\left(\pi_t^{(i)} = \pi_t^{(j)}\right)
\]

- Plage : \([0,1]\).
- Interprétation : fraction de paires "dans le même modèle d'ordre".
- Ontologie : Ce n'est que lorsque la conjonction systémique entre dans la plage chaotique (\(|\tau_s| < 0.41\)) que la **première conjonction temporelle** \(t_1\) s'active (le premier "tic" de l'horloge extramentale).

**Analogie :** Plusieurs musiciens jouent la même figure rythmique dans la même mesure, soit par hasard, soit par couplage faible.

---

## Niveau 2 — Hiérarchie des Échelles Ordinales (Φ₂)

**Idée :** L'égalité ponctuelle ne suffit pas ; ce qui importe, c'est une **relation** (égale, supérieure, inférieure entre les symboles) qui **persiste** pendant au moins \(d\) étapes.

Pour chaque paire \((i,j)\) :

1. Coder la relation \(R_t^{ij} \in \{\mathrm{EQ},\mathrm{GT},\mathrm{LT}\}\).
2. Dans une fenêtre rétrospective de longueur \(d\), mesurer si la relation actuelle domine (fraction ≥ seuil, ex. 0,75).
3. Agréger et normaliser par le nombre de paires → \(\Phi_2(t)\).

- Paramètre typique : \(d = 4\).
- Ontologie : Chaque nouvelle conjonction systémique génère une renormalisation complète du système. Les intervalles entre les "tics" se compressent exponentiellement selon la constante de Feigenbaum : \(\Delta t_k = (1/\delta^k) \times (1/|\tau_s|)\). C'est une structure **fractale-stochastique**.

**Analogie :** Ils ne coïncident pas seulement dans une mesure ; ils maintiennent un **leadership ou un effet miroir rythmique** sur plusieurs mesures.

---

## Niveau 3 — Temps Émergent Global (Φ₃)

**Idée :** Une configuration conjointe apparaît qui **ne peut être réduite** à des coïncidences ou à des paires persistantes. C'est un proxy calculable pour la **synergie / l'irréductibilité**.

Opérationnellement (fenêtre locale de symboles) :

1. Entropie conjointe du n-uplet \((\pi^1,\ldots,\pi^N)\).
2. Entropies marginales et MI (Information Mutuelle) moyenne par paires.
3. **Excès synergique** ≈ corrélation totale − contribution explicable par les paires.
4. Optionnel : *joint surprise* (configurations plus fréquentes que prévu sous indépendance).

\[
\texttt{excess3}(t) \approx \text{combinaison de synergie et de surprise conjointe}
\]

\[
\Phi_3(t) = \mathbf{1}\{\texttt{excess3}(t) > \theta_3\}
\]

- θ₃ typique : ~0.10 dans les synthétiques ; **0.08** recalibré dans le RR cardiaque bruyant.
- En physiologie réelle, l'**excès continu (excess3)** est généralement plus robuste que le taux binaire de "Niveau 3 élevé".

**Analogie :** L'orchestre n'est pas seulement coordonné par paires : un **geste collectif** émerge (un "instant" avec sa propre identité) qui ne peut être déduit de chaque pupitre séparément.

---

## Accumulation de l'Horloge et Poids par Régime

Le temps extramental complet est construit comme la somme hiérarchique via l'équation de récurrence :
\[
t_{k+1} = t_k + g(\tau_s(t_k)) \cdot \Delta t_k
\]

où \(g(\tau_s)\) est la **fonction de porte universelle** (gating function). Ce niveau est le seul observable macroscopiquement.

Comportement qualitatif de la fonction de porte \(g(\tau_s)\) :

| Régime | Valeur \(g(\tau_s)\) | Effet Ontologique |
|---------|---------------------|-------------------|
| Ordre / Stabilité (\(\tau_s \ge +0.50\)) | +1 | Avancée stable et prévisible (*Chronos*). |
| Plage Chaotique (\(\|\tau_s\| < 0.41\)) | (δ-1)/δ × (0.41 - \|\tau_s\|) / 0.41 | Avancée continue mais fractale-stochastique (*Kairos*). |
| Antisynchronisation (\(\tau_s \le -0.41\)) | -1 | Arrêt ou rétrocausalité locale (anti-chronologie). |

**Thèse Centrale :** La hiérarchie ontologique démontre que le temps extramental est une propriété **émergente d'ordre supérieur**, construite de bas en haut à partir de corrélations ordinales dans la plage chaotique, réfutant le temps absolu newtonien.

---

## Tableau Récapitulatif

| Niveau | Nom | Ce qu'il mesure | Proxy numérique | Poids ontologique |
|-------|--------|----------|----------------|-----------------|
| 1 | Coïncidence | Égalité des symboles | Φ₁ ∈ [0,1] | Faible |
| 2 | Relation persistante | Relations stables ≥ d | Φ₂ ∈ [0,1] | Moyen |
| 3 | Émergence | Synergie irréductible | excess3, Φ₃ | Élevé |

## Hypothèses Réfutables (Design Expérimental)

1. **H1 :** Φ₃ / excess3 augmentent (en magnitude ou en fréquence) dans les régimes post-seuil par rapport aux lignes de base.
2. **H2 :** La contribution relative du Niveau 3 augmente avec λ.
3. **H3 :** Les grands "tics" de ΔRECD s'alignent mieux avec les transitions connues qu'une horloge uniquement Φ₁.
4. **H4 :** Dans les surrogates qui détruisent la dépendance croisée, Φ₂ et Φ₃ s'effondrent vers le bruit.

Ces hypothèses structurent à la fois le Laboratoire de la plateforme et les articles sur le CCTP / temps imbriqué.
