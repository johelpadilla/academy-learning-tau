# Systemic Tau Platform — Manuel utilisateur

| Champ | Valeur |
|-------|--------|
| **Document** | Handout 02 · Manuel utilisateur |
| **Public** | Étudiants, enseignants, chercheurs (usage local) |
| **Portée** | Interface Streamlit + CLI `stp` |
| **Niveau** | Opération professionnelle de laboratoire computationnel |
| **Version** | 1.1 · 2026 |

---

## 1. Installation et démarrage

### 1.1 Prérequis

- Python **3.10+** (3.11–3.12 recommandé)  
- Environnement virtuel isolé  
- Dépendances du projet (`pip install -e .` ou `requirements.txt`)  
- TDA optionnel : `pip install systemic-tau-platform[tda]` (ripser)

### 1.2 Lancer l’interface

Depuis la racine du dépôt :

```bash
streamlit run app/Home.py
# ou
stp serve
```

Ouvrez l’URL locale (par défaut `http://localhost:8501`).

### 1.3 Notes d’environnement

- Si vous éditez le paquet `stp` pendant l’exécution, rechargez ou redémarrez.  
- Le bootstrap priorise le `src/` du dépôt pour éviter des installs éditables obsolètes.  
- Variables d’environnement seulement si le déploiement l’exige (p.ex. `STP_PUBLICATIONS_DIR`).

---

## 2. Carte de l’application

| Page | Fonction pédagogique | Livrable typique |
|------|----------------------|------------------|
| **Home** | Portée du noyau, deep-links | Lecture des limites |
| **Fondements** | τ_s, EWS, RECD, excess3, CSD, philosophie | Micro-labs + théorie |
| **Mathématiques** | Carte formelle + sandbox Bandt–Pompe | Exercice d’alphabet ordinal |
| **Domaines** | Maturité empirique + fiches | Choix de proxy et W |
| **Laboratoire** | Pipeline complet et exports | Rapport dual + hash |
| **Parcours d’apprentissage** | Séquence, glossaire, FAQ | Auto-évaluation |
| **Évidence** | Ancre CCTP / démos | Lecture de cohorte pilote |
| **Bibliothèque** | Corpus local de publications | Téléchargement classé |
| **Enseignement** | Syllabus 6 semaines et grille | Conception de cours |
| **Matériaux** | Packs téléchargeables | LMS / impression |

L’UI des plans commerciaux **ne fait pas** partie du noyau éducatif v1.0.

---

## 3. Laboratoire — protocole professionnel

### 3.1 Chargement des données

| Voie | Usage | Précaution |
|------|-------|------------|
| **Catalogue** | Démos synthétiques et samples | *Ground truth* de **conception**, pas une cohorte |
| **CSV propre** | Séries numériques T×N | Encodage, manquants, ≥2 canaux utiles |
| **Deep-link** | Depuis Domaines / Home | Vérifier domaine et preset |

Métadonnées fréquentes : `domain`, preset (W, stride, m, θ₃), `event_index` / `event_fraction`, `variables`, `ground_truth`.

### 3.2 Domaine, événement et design

1. Choisir le **domaine**.  
2. Marquer un **index d’événement** si l’onset est connu.  
3. Sans événement : partition **1ʳᵉ moitié vs 2ᵉ** — design **exploratoire** : le déclarer.  
4. Ne pas déplacer l’événement *post hoc* pour « améliorer » le p sans le rapporter.

### 3.3 Paramètres du noyau

| Paramètre | Rôle | Bonne pratique |
|-----------|------|----------------|
| `window` (W) | Longueur de fenêtre de τ_s | Commencer par le **preset de domaine** |
| `stride` | Pas entre fenêtres | Documenter le chevauchement |
| `m`, `delay` | Embedding Bandt–Pompe | v1.0 typique : m=3, delay=1 |
| `theta3` | Seuil de Φ₃ | 0.08 cardio ; ~0.10 autres |
| `n_surrogates` | Répliques du null | Cours 4–8 ; citer ≥50 |
| `surrogate_method` | `phase_shuffle` / `iaaft` | Défaut phase-shuffle |
| `mode` | `fast` / `full` | Full avant de citer un p |
| Breathing / TDA / Mémoire | Extensions | Ne remplacent pas le noyau |

### 3.4 Exécution et interprétation (ordre recommandé)

1. Séries brutes + marqueur d’événement.  
2. Trajectoire τ_s(t) et Δτ_s.  
3. Panneau RECD : Φ₁–Φ₃, excess3, Δexcess3.  
4. Panneau EWS classiques (var, AR1).  
5. p_surr et méthode de surrogate.  
6. Extensions (si actives) : W(t), β₀/β₁, mémoire.  
7. Lecture duale écrite (modèle Handout 06).  
8. Export MD / JSON / Methods + `repro_hash`.

### 3.5 Exports

| Fichier | Contenu | Usage |
|---------|---------|-------|
| Rapport `.md` | Narratif + métriques + méthodes | LMS / relecture |
| `result.json` | Séries et métriques sérialisables | Réanalyse |
| Methods | Paragraphe prêt pour articles | Corps du rapport |
| `repro_hash` | Sceau SHA-256 | Intégrité académique |

---

## 4. Catalogue de démos (orientation enseignante)

| ID | Domaine | Rôle pédagogique |
|----|---------|------------------|
| `synthetic_coupled_logistic` | synthétique | Contrôle **positif** |
| `synthetic_ar_noise` | synthétique | Contrôle **quasi-nul** |
| `cardiac_like_demo` / `sddb_rr_*` | cardiologie | Proxy CCTP / sample |
| `dengue_like_demo` | épidémiologie | Épidémie + climat (transfert) |
| `eeg_like_demo` | neurosciences | Lock-in de canaux |
| `ecology_like_demo` | écologie | Bloom / nutriments |
| `climate_drought_demo` | climat | Régime de sécheresse (jouet CSD) |
| `education_cohort_demo` | éducation | Cohorte / classe (méta-pédagogie) |
| `social_polarization_demo` | social | Polarisation (démo, pas vérité sociale) |
| `sleep_fragmentation_demo` | physiologie | Fragmentation circadienne |
| `finance_like_demo` | finance | Régime de vol — **pas de trading** |

**Règle de revendication :** démo synthétique ⇒ *ground truth* de conception. Ne la présentez pas comme évidence empirique de domaine réel.

---

## 5. CLI

```bash
stp analyze chemin/donnees.csv \
  --domain epidemiology \
  --window 13 --stride 1 \
  --mode full \
  -o sortie/rapport.md \
  --json sortie/resultat.json

stp analyze data.csv --domain synthetic --breathing --tda -o report.md
stp serve
```

Voir `stp analyze -h` pour les flags à jour.

---

## 6. Reproductibilité (standard postgraduate)

1. Fixer `seed` avec les surrogates.  
2. Exporter MD + JSON de toute course citée.  
3. Citer le dataset original **et** le logiciel.  
4. Ne pas réutiliser un hash de démo synthétique comme cohorte clinique.  
5. Après mise à jour du code, re-courir et comparer les hashs.  
6. Enregistrer W, stride, m, θ₃, n_surr, méthode de null et partition d’événement.

---

## 7. Dépannage

| Symptôme | Vérifier |
|----------|----------|
| `ImportError` STP | `pip install -e .` et redémarrer Streamlit |
| Page blanche | Bootstrap vers le bon dépôt ; rechargement forcé |
| Δτ_s ≈ 0 partout | Contrôle AR ? W énorme ? Mauvaises variables ? |
| Φ₃ toujours 0 | Courant sous bruit ; rapporter **excess3** continu |
| p_surr instable | Augmenter n_surr ; fixer seed ; ne pas citer n=2 |
| CSV échoue | Non numérique, encodage, N effectif < 2 |
| TDA lent | Séries démo ou Fast ; ripser optionnel |

---

## 8. Éthique opérationnelle (résumé)

- Recherche et **enseignement**, pas certification clinique/opérationnelle.  
- Maturité empirique différente par domaine ; ne pas extrapoler la force du pilote CCTP.  
- Données tierces : licences et éthique locale (IRB si applicable).  
- Détail : handout *Éthique et portée*.

---

*Manuel utilisateur STP v1.1 · matériel téléchargeable pour cours et autoformation professionnelle.*
