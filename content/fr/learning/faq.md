# Foire aux Questions (Réponses Approfondies)

## Le Tau Systémique n'est-il qu'un tau de Kendall avec du marketing ?

Non. La parenté avec les statistiques de rang (Kendall et consorts) est réelle dans le **substrat ordinal**, mais l'objet de τ_s est la **dynamique de réorganisation du couplage** dans des fenêtres, souvent multi-échelles et couplées au RECD. Un coefficient de corrélation de rang statique ne définit ni une horloge ni des niveaux Φ₁–Φ₃.

## Pourquoi le signe de Δτ_s / Δexcess3 n'est-il pas toujours positif ?

Parce que la métrique mesure la **réorganisation**, et non la "proximité d'un seuil dans un potentiel 1D". Dans la FV (Fibrillation Ventriculaire), la FA ou le pacing, le système peut **gagner ou perdre** de la structure synergique selon le contexte. La preuve repose sur la **magnitude + les surrogates + la concordance**, pas sur un signe universel.

## Puis-je l'utiliser avec une seule variable ?

Le cœur est multivarié (N≥2). Si vous n'avez qu'une seule série, la plateforme peut construire un proxy \(X=[z(x), z(|\Delta x|)]\) (modèle CCTP). C'est un compromis légitime, pas de la magie : cela rend explicite la relation niveau-variation.

## Cela permet-il de prédire la mort subite ou une épidémie de dengue ?

**Pas en tant que dispositif clinique/opérationnel certifié.** C'est un cadre de recherche et d'enseignement. Toute utilisation prospective nécessite une validation externe, un calibrage des seuils et une gouvernance éthique.

## En quoi diffère-t-il de la Transfer Entropy (Entropie de Transfert) ?

La TE estime le **flux d'information directionnel**. RECD/excess3 estiment les **niveaux de conjonction ordinale et de synergie** orientés vers une horloge émergente. Ils sont complémentaires : le Lab Full peut afficher les deux.

## Pourquoi Bandt–Pompe et pas SAX ou d'autres symboles ?

Par souci de parcimonie, d'invariance monotone et pour un écosystème mature (entropie de permutation, articles du paradigme). SAX ou d'autres alphabets sont des extensions possibles ; ils ne sont pas le standard du pilote CCTP.

## Que dois-je citer ?

1. L'article/preprint du domaine que vous utilisez (ex. CCTP pour la cardio).
2. Le logiciel (`systemictau`, `nested-recd`, cette plateforme).
3. Le jeu de données original (PhysioNet, LTER, etc.).
