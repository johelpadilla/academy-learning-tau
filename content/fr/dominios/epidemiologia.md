# Domaine : Épidémiologie — Dengue et Hyper-persistance

## 1. Contexte Scientifique

La **dengue** est un système socio-écologique contraint par le climat, le vecteur (*Aedes*), l'immunité et la mobilité humaine. Les séries d'incidence hebdomadaire montrent des **épidémies**, des plateaux et parfois une **hyper-persistance** : le système reste "bloqué" dans des régimes de transmission élevés plus longtemps que ne le prédirait un simple modèle de bruit.

Porto Rico et les séries de type **DengAI** (San Juan / Iquitos) sont des laboratoires naturels pour l'alerte précoce épidémiologique.

## 2. Pourquoi les EWS Classiques Échouent ou Sont Insuffisants

- L'incidence est **discrète, bruyante et saisonnière** ; la variance et l'AR(1) confondent la saisonnalité avec la proximité d'une épidémie.
- Le "système" n'est pas unilinéaire : il nécessite l'intégration de **modèles d'ordre fractionnaire** (où la mémoire des œufs dormants retarde le système) ou l'évaluation explicite du couplage *cas–climat–vecteur*.
- Les seuils univariés échouent systématiquement face au bruit biologique urbain.
- Les modèles prédictifs ML ou SEIR classiques (d'ordre entier) souffrent d'"oubli", masquant les véritables points de bifurcation et de réorganisation relationnelle profonde.

## 3. Valeur Différentielle de τ_s + RECD

| Apport | Contenu |
|--------|-----------|
| Multivarié ordinal | \(X = [z(\mathrm{cases}), z(\mathrm{temp}), z(\mathrm{precip}), \ldots]\) |
| Hyper-persistance | Capture les retards fractionnaires dus à la latence/mémoire biologique du vecteur. |
| Antisynchronisation Vectorielle | Capacité unique à détecter la divergence en antiphase (\(\tau_s \le -0.41\)) entre un climat favorable et des populations décimées par fumigation. |
| RECD (Horloge Épidémique) | Remplace le temps chronologique par un **temps épidémiologique effectif** ; des "tics" asymétriques marquent la réorganisation et permettent des prévisions anticipées (4-6 semaines). |

## 4. Jeu de Données d'Exemple

- DengAI San Juan hebdomadaire (échantillon de la plateforme).
- Variables : cas, température, précipitations (z-score).
- Annotation pédagogique des fenêtres d'épidémie (percentile élevé ou étiquettes historiques).

## 5. Interprétation

- Rechercher l'entrée dans la **véritable plage chaotique (\(|\tau_s| < 0.41\))**, qui statistiquement **précède les pics de population avec une anticipation de 4 à 6 semaines**.
- Identifier les régimes de **forte synchronisation (\(\tau_s \ge +0.50\))**, caractéristiques des périodes stables post-intervention vectorielle.
- Étudier les périodes d'**antisynchronisation (\(\tau_s \le -0.41\))**, où se produit une *rétrocausalité locale* : le climat augmente la pression, mais la densité larvaire est réduite de force, inversant temporairement l'horloge épidémiologique.
- Contraster empiriquement que l'imputation de données manquantes dans les zones marginales ne détruit pas les invariants ordinaux.

## 6. Références

- Preprints de l'auteur sur la dengue Tau/RECD (2025–2026).
- DengAI DrivenData ; littérature sur l'alerte précoce dans les maladies à transmission vectorielle.
