# Syllabus — Analyse ordinale des systèmes complexes avec Systemic Tau / RECD

| Champ | Valeur |
|-------|--------|
| **Plateforme** | Academy Learning Tau · Systemic Tau Platform (STP) v1.0 |
| **Format** | Cours court intensif · **6 semaines** |
| **Niveau** | 2ᵉ / 3ᵉ cycle (master / doctorat) ou spécialisation professionnelle avec base quantitative |
| **Modalité** | Hybride ou présentiel + laboratoire computationnel (app Streamlit + CLI optionnelle) |
| **Charge estimée** | **4–5 h/semaine** (≈ 2 h lecture/théorie + 2–3 h Lab/rédaction) · **24–30 h** au total |
| **Langues de l’app** | Espagnol (source), English, Français |
| **Version du syllabus** | 1.1 · 2026 |
| **Document** | Handout `08_syllabus_6_semanas` · usage académique avec citation |

---

## 1. Description du cours

Ce cours forme à **formuler, exécuter et documenter** une analyse de **réorganisation relationnelle** sur des séries temporelles multivariées au moyen de :

1. **Systemic Tau (τ_s)** — thermomètre de couplage ordinal entre canaux ;  
2. **RECD ordinal emboîté (Φ₁–Φ₃ + excess3)** — grammaire de coïncidence, persistance et synergie irréductible ;  
3. **Lecture duale** — contraste systématique avec les **EWS classiques** (variance, AR(1)) ;  
4. **Nuls par surrogates** (phase-shuffle / IAAFT) et **reproductibilité** (hash SHA-256, Methods, export MD/JSON).

L’**ancre empirique de référence** est le protocole **CCTP** (cardiologie computationnelle / pré-FV, cohorte pilote et démos SDDB). Les autres applications (épidémiologie, neurosciences, écologie, climat, éducation, physiologie du sommeil, finance, dynamique sociale) sont traitées comme **transfert méthodologique** avec maturité empirique explicite — non comme promesses prédictives de produit.

**Ce n’est pas** un cours sur un dispositif médical, une alerte épidémiologique opérationnelle, le trading ou le scoring social.

---

## 2. Compétences de sortie

À la réussite du cours, l’étudiant·e sera capable de :

| # | Compétence (observable) |
|---|-------------------------|
| C1 | **Définir** une question relationnelle (« le couplage entre X et Y se réorganise-t-il autour d’un événement ? ») distincte d’une question purement univariée (« la variance monte-t-elle ? »). |
| C2 | **Sélectionner** variables, événement (le cas échéant), preset de domaine et paramètres (W, stride, m, θ₃, n_surr) de façon justifiée. |
| C3 | **Calculer** τ_s en fenêtre glissante et le panel RECD (Φ₁–Φ₃, excess3, T_recd) dans le Lab ou via CLI. |
| C4 | **Comparer** le panel relationnel à var/AR1 (lecture duale) et interpréter concordance, mixte ou quietude. |
| C5 | **Tester sous nul** le contraste Δτ_s avec des surrogates et rapporter p_surr sans réduire le rapport à un seul p-valeur. |
| C6 | **Documenter** des Methods reproductibles (paramètres, seed, hash, limites du domaine) et borner les claims à la maturité empirique. |
| C7 | **Transférer** la même grammaire vers un second domaine en énonçant ce qui change (proxy, W, jargon) et ce qui ne change pas (ontologie de la méthode). |

**Compétence intégratrice (livrable final) :** un *portfolio* avec rapport de lecture duale + export MD/JSON + Methods + checklist signée, évalué avec la grille de la §7.

---

## 3. Prérequis

**Obligatoires**

- Séries temporelles ou statistique intermédiaire (moyenne, variance, corrélation ; idées de processus stochastique).  
- Lecture de graphiques scientifiques et de tableaux de métriques.  
- Usage basique d’un navigateur et d’un environnement local ou hébergé de l’app.

**Recommandés (non bloquants)**

- Python basique ou familiarité Jupyter (piste CLI/notebooks).  
- Notions de systèmes complexes ou d’EWS / critical slowing down.  
- Piste cardio : vocabulaire minimal ECG/RR (formation clinique non exigée).

**Logiciel**

- Academy Learning Tau (Streamlit) avec catalogue de démos.  
- Optionnel : CLI `stp analyze` / `stp serve` (même noyau).  
- Export : Markdown, JSON ; PDF via Pandoc si le LMS l’exige.

---

## 4. Carte du cours ↔ modules de l’app

| Semaine | Modules STP | Handouts prioritaires |
|---------|-------------|------------------------|
| 1 | Fondements (EWS, CSD) · Lab (EWS / synthétique seulement) | Éthique · Guide rapide · Fondements 02/05 |
| 2 | Mathématiques · Lab (τ_s, hash) | Math pratique · Théorie τ_s |
| 3 | Fondements RECD/excess3 · Lab | Lecture duale · Cheatsheet Lab |
| 4 | Domaines (cardio) · Preuves · Lab Full | Domaine cardiologie · Checklist |
| 5 | Domaines (transfert) · Lab | Fiche du domaine choisi · FAQ |
| 6 | Lab export · Matériels · Enseignement | Éthique (révision) · Pack étudiant |

---

## 5. Programme hebdomadaire détaillé

Charge indicative par semaine : **lecture 90–120 min · Lab 90–120 min · rédaction 30–60 min**.

### Semaine 1 — EWS classiques, CSD et limites du panel univarié

| Élément | Contenu |
|---------|---------|
| **Objectifs** | Expliquer var et AR(1) comme EWS ; énoncer au moins deux échecs conceptuels (ambiguïté de signe, univarié vs relationnel) ; citer la portée éthique du logiciel. |
| **Théorie** | Fondements · onglets EWS et CSD ; handout *Éthique et portée*. |
| **Lab** | Dataset `synthetic_coupled_logistic` ou `synthetic_ar_noise`. Observer var/AR1 ; lecture duale complète pas encore exigée. |
| **Livrable formatif** | Essai court (≈ 1 page) : *« Quand une hausse de variance ne répond-elle pas à la question du système ? »* |
| **Critère de succès** | Distingue EWS classiques et réorganisation relationnelle ; n’affirme aucune prédiction clinique. |

### Semaine 2 — Motifs ordinaux Bandt–Pompe et Systemic Tau (τ_s)

| Élément | Contenu |
|---------|---------|
| **Objectifs** | Définir les symboles Bandt–Pompe (m=3) ; interpréter τ_s comme couplage ordinal fenêtré ; enregistrer le **repro_hash**. |
| **Théorie** | Fondements · τ_s ; Mathématiques (sandbox m=3) ; illustrations amplitude vs réorganisation. |
| **Lab** | `synthetic_coupled_logistic` · preset `synthetic` · mode Fast · W/stride cohérents · n_surr ≥ 8. Comparer à `synthetic_ar_noise` (contrôle quasi-nul). |
| **Livrable formatif** | Capture ou tableau : Δτ_s, p_surr (le cas échéant), hash ; 5 lignes d’interprétation *sans* sur-revendication. |
| **Critère de succès** | Explique pourquoi le contrôle AR/noise ne doit pas « ressembler » à un switch de couplage. |

### Semaine 3 — RECD emboîté, excess3 et lecture duale

| Élément | Contenu |
|---------|---------|
| **Objectifs** | Décrire Φ₁–Φ₃ et le rôle d’**excess3** sous bruit ; appliquer le protocole de lecture duale (concordance / mixte / quietude). |
| **Théorie** | Fondements · RECD et excess3 ; handouts *Lecture duale* et *Théorie τ_s + RECD*. |
| **Lab** | Même synthétique ou cardio-like en Fast ; panel RECD ; dual summary ; **ne pas** fonder le claim principal sur les seules extensions TDA/breathing. |
| **Livrable formatif** | Mini-rapport (1–2 p.) : question, paramètres, lecture duale, une phrase de portée. |
| **Critère de succès** | Traite excess3 comme primaire si Φ₃ binaire s’éteint ; compare à var/AR1. |

### Semaine 4 — Ancre empirique : cardiologie CCTP / pré-FV

| Élément | Contenu |
|---------|---------|
| **Objectifs** | Appliquer le proxy \(X=[z(\mathrm{RR}), z(\|\Delta\mathrm{RR}\|)]\) et le preset `cardiology` (p.ex. W≈101, stride=5, θ₃≈0.08) ; rédiger une lecture duale avec **voix de domaine** et disclaimers cliniques. |
| **Théorie** | Domaines · Cardiologie ; Preuves (pilote CCTP N=10, limites) ; jargon RR, FV, Holter, SDDB. |
| **Lab** | Préféré : `cardiac_like_demo`. Si samples présents : `sddb_rr_38_demo` (signal fort) et optionnel `sddb_rr_51_demo` (pacing / difficulté). Événement = marqueur d’onset s’il existe. |
| **Sommatif partiel (30 % du portfolio)** | Rapport dual 2–3 pages : métriques, p_surr, panel classique, phrases permises vs interdites, hash. |
| **Critère de succès** | Aucun claim d’« alarme FV » ou de dispositif ; maturité CCTP explicitée. |

### Semaine 5 — Transfert de domaine (un seul domaine non-cardio)

| Élément | Contenu |
|---------|---------|
| **Objectifs** | Réutiliser la grammaire τ_s/RECD dans **un** domaine de transfert ; contraster maturité empirique et jargon ; justifier le preset. |
| **Choix (un)** | `dengue_like_demo` (épi) · `eeg_like_demo` (neuro) · `ecology_like_demo` · `climate_drought_demo` · `education_cohort_demo` · `sleep_fragmentation_demo` · `social_polarization_demo` · `finance_like_demo` (**transfert méthodologique seulement** ; claims de trading **interdits**). |
| **Théorie** | Fiche domaine dans Domaines + lentille de domaine dans Fondements (exemples situés). |
| **Lab** | Preset du domaine ; Fast ou Full selon la charge ; n_surr documenté. |
| **Sommatif partiel (25 % du portfolio)** | Mini-rapport de transfert (1–2 p.) : analogue d’événement, proxy utilisé, ce qui **n’est pas** affirmé. |
| **Critère de succès** | Maturité et limites du domaine choisi visibles dans la conclusion. |

### Semaine 6 — Surrogates, extensions, éthique, portfolio et peer review

| Élément | Contenu |
|---------|---------|
| **Objectifs** | Affiner les nuls (phase-shuffle vs IAAFT) ; décider si les extensions (breathing, TDA, mémoire) apportent un *contraste* sans remplacer le noyau ; remettre le portfolio complet ; peer review avec grille. |
| **Théorie** | Éthique (révision) ; handout *Extensions* ; FAQ (signe dépendant du contexte, N=1, « est-ce que ça prédit… ? »). |
| **Lab** | Ré-analyse du cas sem. 4 ou 5 ; mode Full optionnel ; export **MD + JSON + Methods** ; checklist d’analyse signée. |
| **Sommatif final (45 % du portfolio)** | Portfolio : (1) rapport principal, (2) rapport de transfert ou annexe, (3) exports + hash, (4) checklist, (5) réflexion éthique (½ p.). |
| **Critère de succès** | Grille §7 ≥ seuil ; claims bornés ; reproductibilité vérifiable. |

---

## 6. Évaluation

### 6.0 Évaluations dans la plateforme (auto-notées)

L’app inclut la page **Évaluations** (`pages/9_Evaluaciones.py`) :

- **Compte étudiant local** (inscription / connexion ; progression dans `data/student_records/`, pas de SaaS cloud).  
- **Quiz QCM par module** (semaines 1–6), notation automatique, seuil par défaut **70 %**, rattrapages avec **meilleure** note conservée.  
- **Note de cours pondérée** avec les mêmes poids que §6.1 (formatifs 5 %+5 %+5 %, S4 30 %, S5 25 %, S6 30 %).  
- **Suivi des livrables** (état des essais/rapports) et **journal d’activité**.  
- La checklist du **Parcours d’apprentissage** se synchronise avec le compte si session ouverte.  
- Textes de compte, UI et banque de questions en **ES / EN / FR**.

Les quiz **complètent** (ne remplacent pas) la grille 0–2 du rapport Lab (§6.2) : l’enseignant fixe le poids relatif quiz auto vs livrables qualitatifs.

### 6.1 Structure suggérée

| Composante | Poids | Moment |
|------------|-------|--------|
| Formatives (sem. 1–3) | 15 % | Feedback rapide ; quiz S1–S3 dans l’app + essais |
| Rapport dual cardio (sem. 4) | 30 % | Sommatif · quiz S4 + rapport |
| Mini-rapport de transfert (sem. 5) | 25 % | Sommatif · quiz S5 + mini-rapport |
| Portfolio final + peer review (sem. 6) | 30 % | Sommatif (inclut 15 % peer si l’enseignant l’active) · quiz S6 |

*L’enseignant peut fusionner 4+5+6 en un seul portfolio (100 %) pour des offres très courtes.*

### 6.2 Grille Lab / rapport (6 critères × 0–2 = **12 points**)

| # | Critère | 0 | 1 | 2 |
|---|---------|---|---|---|
| 1 | **Question scientifique** | Absente ou confond univarié/relationnel | Question claire mais design/événement faible | Question relationnelle + coupure/événement justifiés |
| 2 | **Paramètres et preset** | Défauts non justifiés | Preset correct, faible justification W/m/θ₃ | Preset + W/stride/m/θ₃/n_surr/seed documentés |
| 3 | **Métriques noyau** | Δτ_s ou excess3 manquants | Δ sans p_surr ni contexte | Δτ_s, mean/Δ excess3, p_surr (ou n_surr=0 déclaré) |
| 4 | **EWS en parallèle** | Pas de panel classique | Mentionne var/AR1 sans intégration | Lecture duale explicite (confirme / se tait / contredit) |
| 5 | **Conclusion bornée** | Sur-revendication (clinique, trading, prédiction) | Conclusion partielle, réserves faibles | Claims alignés sur la maturité + phrase de non-portée |
| 6 | **Reproductibilité** | Ni hash ni params | Hash **ou** Methods incomplets | Hash + Methods + export utilisable par un pair |

**Seuil de réussite de la pratique :** ≥ **9 / 12**.  
**Excellent :** ≥ 11 / 12 et peer review utile (si applicable).

### 6.3 Phrases de rendu (orientation)

| Permises (exemples) | Interdites dans le cours v1.0 |
|---------------------|-------------------------------|
| « Réorganisation relationnelle significative vs phase-shuffle sous ce design… » | « Prédit la FV / l’épidémie / le krach » |
| « Panel classique ambigu (var↑, AR1↓) ; le relationnel bouge dans l’approche… » | « Dispositif d’alarme clinique validé » |
| « Transfert pédagogique vers dengue-like ; pas un nowcast opérationnel » | « Signal de trading / alpha » |
| « Démo avec vérité terrain de switch ; calibre la lecture duale » | « Preuve causale de polarisation sociale réelle » |

---

## 7. Datasets du catalogue (v1.0)

### Contrôles (semaines 1–2)

| ID | Rôle |
|----|------|
| `synthetic_coupled_logistic` | Contrôle **positif** (switch de couplage) |
| `synthetic_ar_noise` | Contrôle **quasi-nul** / bruit |

### Ancre cardio (semaine 4)

| ID | Rôle |
|----|------|
| `cardiac_like_demo` | Flux CCTP sans dépendance PhysioNet |
| `sddb_rr_38_demo` | Sample démo signal fort (si dans `data/samples/`) |
| `sddb_rr_51_demo` | Sample pacing / plus difficile |

### Transfert (semaine 5) — en choisir **un**

| ID | Domaine |
|----|---------|
| `dengue_like_demo` | Épidémiologie |
| `eeg_like_demo` | Neurosciences |
| `ecology_like_demo` | Écologie |
| `climate_drought_demo` | Climat / hydrologie |
| `education_cohort_demo` | Apprentissage collectif |
| `sleep_fragmentation_demo` | Physiologie du sommeil |
| `social_polarization_demo` | Dynamique sociale (jouet) |
| `finance_like_demo` | Finance (**méthode seulement** ; pas de trading) |

Les données tierces (p.ex. PhysioNet/SDDB) restent soumises à leurs conditions d’usage.

---

## 8. Matériels et lectures

### Packs téléchargeables (page Matériels)

- **Pack étudiant :** guide rapide, théorie, maths, cheatsheet, lecture duale, checklist, FAQ, éthique.  
- **Pack enseignant :** syllabus (ce document), éthique, manuel, packs théorie/lab, FAQ, glossaire.  
- Fiches de domaine et Fondements compilés dans l’app.

### Lectures scientifiques (l’enseignant en choisit 1–2)

- Travaux CCTP et EWS classiques cités sous **Preuves**.  
- Elles ne remplacent pas la pratique Lab.

### CLI (piste avancée optionnelle)

```bash
stp analyze data.csv --domain cardiology -o report.md --json result.json
stp serve
```

---

## 9. Politiques du cours

### 9.1 Éthique et portée

- Le handout *Éthique et portée du noyau* est obligatoire avant claims publics ou rendus sem. 4–6.  
- Le logiciel est de **recherche et d’enseignement**, non un produit clinique ou financier réglementé.  
- La **maturité empirique** est asymétrique : cardio (CCTP) > démos synthétiques de transfert.

### 9.2 Intégrité académique

- Exports et hashes doivent correspondre aux runs de l’étudiant·e (ou de l’équipe déclarée).  
- Citer le logiciel STP et les références de domaine utilisées.  
- Interdit de présenter des démos synthétiques comme données cliniques ou de surveillance réelles non étiquetées.

### 9.3 Travail en équipe

- Optionnel en binômes (sem. 4–6) ; chaque membre doit pouvoir expliquer les Methods et le hash.  
- Peer review sem. 6 : en aveugle ou semi-aveugle selon le LMS.

### 9.4 Variantes de calendrier

| Variante | Ajustement |
|----------|------------|
| **Intensif 4 semaines** | Fusionner 1–2 et 5–6 ; un seul rapport + transfert bref. |
| **Séminaire 8 semaines** | Ajouter une semaine de discussion d’articles et une semaine d’extensions TDA/breathing comme contraste. |
| **Atelier Lab 2 jours** | Compresser sem. 2–4 ; grille réduite (critères 3–6). |

---

## 10. Notes pour l’enseignant

1. **Pédagogie et falsification** avant les promesses de produit : valorisez un contrôle quasi-nul bien interprété.  
2. Temps explicite pour les **contrôles synthétiques** (sem. 2) avant l’ancre cardio.  
3. En sem. 4, sans samples SDDB, `cardiac_like_demo` suffit pour la compétence.  
4. Finance et social : cadrer comme **bacs à sable de grammaire**, jamais comme prédiction.  
5. Extensions (TDA, breathing, mémoire) : opt-in Full ; le claim principal reste τ_s + excess3 + dual + nul.  
6. Utilisez la **voix de domaine** (jargon dans l’interprétation et les Fondements) pour transférer le concept sans changer les maths.  
7. Évaluez la qualité du **bornage** du claim avant la magnitude de |Δ|.  
8. Langue : app et handouts en ES/EN/FR ; choisissez une langue de rendu par cohorte.

---

## 11. Citation suggérée

Si vous utilisez ce syllabus et la plateforme en enseignement ou en recherche, citez Academy Learning Tau / Systemic Tau Platform et les références scientifiques du domaine (p.ex. CCTP pour le cardio) listées sous Preuves dans l’app et dans `CITATION.cff`.

---

## 12. Contact et amélioration continue

- Issues et retours académiques via le dépôt du projet.  
- Collaboration pédagogique / adapters de domaine : voir le README du dépôt.  
- Ce syllabus est un **document vivant** : alignez toujours les IDs de datasets et presets sur la version STP installée.

---

*Syllabus STP v1.1 · Academy Learning Tau · usage académique avec citation · ne constitue pas un conseil clinique, épidémiologique opérationnel ni financier.*
