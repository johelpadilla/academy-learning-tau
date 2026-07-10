# Foire aux questions (réponses approfondies)

| Champ | Valeur |
|-------|--------|
| **Document** | FAQ · réponses de niveau postgraduate |
| **Version** | 1.1 · 2026 |
| **Usage** | Handout téléchargeable + Parcours d’apprentissage |

Ces réponses ciblent de vrais malentendus de postgraduate et de relecture par les pairs — pas une FAQ marketing.

---

## A. Concepts

### La Tau systémique n’est-elle qu’un Kendall tau avec marketing ?

Non. La parenté avec les statistiques de rangs est réelle dans le **substrat ordinal**, mais l’objet de τ_s est la **dynamique de réorganisation du couplage** en fenêtres, souvent multi-échelle et couplée au RECD. Une corrélation de rangs statique ne définit ni horloge ni niveaux Φ₁–Φ₃.

### En quoi diffère-t-elle de la Transfer Entropy ?

| | Transfer Entropy | τ_s + RECD / excess3 |
|--|------------------|----------------------|
| Question | Combien A améliore-t-elle la prédiction de B ? | Comment la structure ordinale conjointe se réorganise-t-elle et l’horloge avance-t-elle ? |
| Direction | Explicitement directionnelle | Relationnelle / synergique (pas un graphe causal) |
| Usage v1.0 | Horizon Full | Noyau du Lab |

Elles sont **complémentaires**. Ne substituez pas l’une à l’autre dans un paper sans justifier la question.

### Pourquoi Bandt–Pompe plutôt que SAX ou d’autres symboles ?

Parsimonie, invariance monotone, et écosystème mature (entropie de permutation, papers du paradigme). SAX et d’autres alphabets sont des extensions possibles ; ce **ne sont pas** le standard du pilote CCTP ni le noyau v1.0.

### Qu’est-ce que le « signe context-dependent » ?

Cela signifie que **Δτ_s ou Δexcess3 peuvent monter ou baisser** vers un événement selon le régime (p.ex. FA, pacing, phase d’épidémie). L’évidence se joue sur : (1) magnitude du changement, (2) concordance entre métriques, (3) p-valeurs sous surrogates, (4) récit de domaine — pas sur un panneau universel « toujours positif = mauvais ».

---

## B. Données et pratique

### Puis-je l’utiliser avec une seule variable ?

Le noyau est multivarié (N≥2). Si vous n’avez qu’une série, la plateforme construit un proxy  
\(X=[z(x), z(|\Delta x|)]\) (motif CCTP). C’est un compromis **légitime et explicite**, pas de la magie : il rend visible la relation niveau–variation.

### Quelle fenêtre W dois-je utiliser ?

Commencez par le **preset de domaine** (cardio : 101 ; dengue/synthétique : ~13). Ensuite :

- W trop petite → bruit, p-valeurs instables.  
- W trop grande → lisse la transition et « arrive tard ».  
Documentez W dans le rapport ; le hash l’inclut.

### Combien de surrogates suffisent ?

| Usage | n_surr indicatif |
|-------|------------------|
| Cours / démo | 4–8 (Fast) |
| Exploration sérieuse | 20–50 |
| Résultat à citer | ≥50 et sensibilité à la seed |

Le phase-shuffle **préserve les spectres par canal** et **rompt la dépendance croisée** : le null naturel pour « le signal est-il vraiment relationnel ? ».

### Comment lire p_surr avec Δ ?

- **Grand Δ + p bas :** candidat à effet relationnel.  
- **Grand Δ + p haut :** ne revendiquez pas la détection ; revoir preprocess et W.  
- **Petit Δ + p bas :** petit effet stable — prudence de domaine.  
- **Ne publiez jamais** le p seul sans taille d’effet et contexte.

---

## C. Évidence et éthique

### Cela prédit-il la mort subite ou une épidémie de dengue ?

**Pas comme dispositif clinique/opérationnel certifié.** C’est un cadre de recherche et d’enseignement. Tout usage prospectif exige validation externe, calibration de seuils et gouvernance éthique.

### Que couvre le noyau actuel ?

- Pipeline complet τ_s + RECD + EWS + surrogates + hash.  
- Pilote **CCTP/SDDB N=10** avec résultats documentés (panneau classique ambigu ; relationnel significatif ; concordance 8/10 dans le récit de domaine).  
- Fondements, glossaire, domaines, Lab et syllabus de 6 semaines.  
- Samples et générateurs pour reproduire la *logique* d’analyse sans PhysioNet.  
- Catalogue de bibliothèque de recherche pour publications locales.

Détail : **Portée du noyau** (Parcours d’apprentissage) ou l’expander Home.

### Que dois-je citer ?

1. Paper/preprint du **domaine** (p.ex. CCTP pour le cardio).  
2. Logiciel (`systemictau`, `nested-recd`, cette plateforme v1.0).  
3. Dataset original (PhysioNet, LTER, DengAI, etc.).  
4. Le **`repro_hash`** du Lab si vous rapportez un chiffre concret d’une course.

---

## D. Produit et limites logicielles

### Pourquoi Φ₃ « ne s’allume » parfois pas ?

Parce que c’est un **indicateur binaire** avec seuil θ₃. Sous données bruitées le continu **excess3** peut bouger clairement pendant que Φ₃ reste à zéro. Dans CCTP la métrique primaire est mean_excess3 / Δexcess3.

### TDA et Breathing Window sont-ils prêts ?

**Oui, comme extensions opérationnelles du Lab** (v1.0+) :

| Extension | Ce qu’elle fait dans le Lab | Backend |
|-----------|----------------------------|---------|
| **Breathing window** | W s’adapte à la volatilité locale pour τ_s | Natif (toujours) |
| **TDA / Betti** | Courbes β₀/β₁ en fenêtres sur un cloud de delay-embedding | `ripser` si installé ; sinon **1-squelette Vietoris–Rips** |
| **Mémoire ordinale** | MI symbolique lag-1 et cross-MI | Natif |

**Activation :** mode **Full** (cases actives par défaut) ou cases en Fast. Onglet **Extensions**. CLI : `--breathing --tda`.

**Ce qu’elles ne sont pas :** elles ne remplacent pas τ_s + RECD + EWS + surrogates. Un claim principal de thèse **ne devrait pas** reposer seulement sur β₁ pédagogique du proxy.

### Dois-je installer ripser ?

Non. Sans ripser le Lab utilise un proxy de Betti du 1-squelette VR. Avec `pip install systemic-tau-platform[tda]`, ripser est utilisé quand disponible.

### Les plans Academic/Professional sont-ils actifs ?

L’UI des plans **ne fait pas partie du noyau éducatif v1.0**. En local, Lab et matériaux téléchargeables fonctionnent sans backend de paiements. Ne confondez pas le positionnement commercial avec les limites scientifiques du code local.

---

## E. Nouveaux domaines et pédagogie

### Pourquoi des démos « classe », « polarisation » ou « sécheresse » ?

Parce que STP est un logiciel **pédagogique** : elles font pratiquer la même grammaire ordinale sur des systèmes familiers ou classiques (CSD), avec *ground truth* de **conception**. Ce ne sont ni des évidences de terrain ni des produits prédictifs.

### Quelle démo le premier jour ?

1. `synthetic_coupled_logistic` (signal fort).  
2. `synthetic_ar_noise` (quasi-nul).  
3. Puis un domaine appliqué **avec disclaimer de maturité**.

### Où télécharger PDF/Markdown pour le LMS ?

Page **Matériaux** de l’app : guide rapide, manuel, théorie, cheat-sheet, checklist, syllabus, FAQ, glossaire, packs étudiant/enseignant.

### Qu’est-ce que la Bibliothèque de recherche ?

Un catalogue curaté de publications locales (chemin configurable / `STP_PUBLICATIONS_DIR`) classées par collections. Il fournit le téléchargement des binaires du corpus sans gonfler git. Elle ne remplace ni la lecture duale du Lab ni la validation externe.

---

*FAQ STP v1.1 · référence de niveau postgraduate*
