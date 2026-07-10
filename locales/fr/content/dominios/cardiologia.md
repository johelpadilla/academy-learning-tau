# Domaine : Cardiologie computationnelle — pré-FV et SDDB

### Objectifs d’apprentissage
1. Expliquer pourquoi var/AR1 peuvent être ambigus avant une fibrillation ventriculaire (FV).
2. Décrire le proxy \(X=[z(\mathrm{RR}), z(|\Delta\mathrm{RR}|)]\) et les presets CCTP.
3. Appliquer le protocole de **lecture duale** à un cas cardio-like ou un sample SDDB.

**Maturité empirique v1.0 :** ★★★★★ (maximum de la plateforme) — pilote CCTP N=10.

---

## 1. Contexte scientifique

La **mort subite cardiaque** par **fibrillation ventriculaire (FV)** reste difficile à anticiper depuis l’ECG de surface. Les Holter de la *Sudden Cardiac Death Holter Database* (SDDB, PhysioNet) sont parmi les rares ressources publiques avec des heures de dynamique pré-événement et un onset de FV documenté.

Le **Cardiac Critical Transitions Protocol (CCTP)** applique le Tau systémique et le RECD ordinal à des séries d’**intervalles RR** pour caractériser la réorganisation relationnelle de la dynamique de fréquence cardiaque **avant** une FV spontanée.

**Question guide :** non pas « la variance monte-t-elle ? », mais « la relation entre le niveau de RR et sa variation battement à battement se réorganise-t-elle ? ».

---

## 2. Pourquoi les métriques classiques sont insuffisantes ici

Dans la cohorte CCTP (N=10 enregistrements de haute qualité) :

| Constat | Implication |
|---------|-------------|
| La variance de RR **augmente** souvent | Signature « type CSD » présente |
| L’AR(1) **diminue** fréquemment | Le CSD naïf échoue |
| Pacing intermittent / FA dans certains enregistrements | Le « bruit » est du contexte clinique |

Interpréter seulement var/AR1 produit des lectures confuses ou des **faux négatifs conceptuels**.

---

## 3. Valeur différentielle de τ_s + RECD

| Ingrédient | Rôle dans CCTP | Dans le Lab v1.0 |
|------------|----------------|------------------|
| Proxy \(X = [z(\mathrm{RR}),\, z(\|\Delta\mathrm{RR}\|)]\) | Multivarié minimal physiologiquement motivé | Auto si 1 colonne ; cardio-like le simule |
| τ_s (W=101, stride=5) | Couplage ordinal niveau–variabilité | Preset `cardiology` |
| Φ₁–Φ₃ + **excess3** | Structure symbolique ; excess3 primaire | Onglet RECD + métriques |
| Phase-shuffle | Null de dépendance croisée | Curseur n surrogates |
| Signe dépendant du contexte | Réorganisation, pas dogme de signe | Interpréter Δ + p + contexte |

**Résultat clé du pilote (documenté) :**  
Δτ_s et Δexcess3 sont significatifs dans la plupart des enregistrements sous surrogates, avec **concordance de signe 8/10**, même quand le panneau classique est ambigu.

---

## 4. Jeux de données d’exemple

| Ressource | Fonction dans le Lab |
|-----------|----------------------|
| Sample `sddb_rr_38_demo.csv` | Signal fort / cas de référence |
| Sample `sddb_rr_51_demo.csv` | Pacing intermittent — flags de qualité |
| Générateur **Cardio-like demo** | Flux CCTP sans dépendre de PhysioNet |

Colonnes typiques : `rr_ms`, `abs_drr`, `z_rr`, `z_abs_drr`. Événement : index d’onset de FV (`vfon`) si disponible.

---

## 5. Fiche de conception (schéma uniforme)

| Champ | Valeur |
|-------|--------|
| **Proxy** | \(X=[z(\mathrm{RR}), z(\|\Delta\mathrm{RR}\|)]\) |
| **Événement** | Onset de FV (`vfon`) ou fenêtre d’approche |
| **Preset Lab** | `cardiology` · W≈101 · stride≈5 · θ₃≈0.08 · m=3 |
| **Démos principales** | `sddb_rr_38_demo`, `sddb_rr_51_demo`, cardio-like |
| **Maturité** | Très élevée (ancre CCTP) |

### Phrases autorisées (exemples)
- « Réorganisation relationnelle significative vs phase-shuffle sous ce design… »
- « Panneau classique ambigu (var↑, AR1↓) ; le relationnel bouge dans l’approche… »
- « Pas un dispositif d’alarme clinique ; limites de N et d’échantillon s’appliquent. »

### Phrases interdites (v1.0)
- « Prédit la FV / alarme temps réel validée »
- « Dispositif médical certifié / aide à la décision en réanimation »
- « Prouve causalement le risque de mort subite pour un patient »

---

## 6. Checklist d’interprétation

1. **Qualité :** interpolation excessive, pacing, artéfacts ?  
2. **Panneau relationnel :** τ_s basal vs approche ; mean excess3 et Δ.  
3. **Nulls :** p phase-shuffle pour Δτ_s (et excess3 si calculé).  
4. **Panneau classique :** var et AR1 — confirment, se taisent ou contredisent ?  
5. **Concordance :** τ_s et excess3 bougent-ils ensemble ?  
6. **Phrase de clôture bornée** sans claim clinique.

---

## 7. Exercice de 20 minutes

1. Lab → **Cardio-like demo** → preset cardiology → Fast, n_surr=8.  
2. Tableau : Δτ_s, mean excess3, Δexcess3, p_surr, var/AR1 qualitatif.  
3. Rédiger 4 lignes de lecture duale.  
4. (Optionnel) Comparer samples 38 vs 51.

---

## 8. Références

- Padilla-Villanueva — CCTP/SDDB (Zenodo 10.5281/zenodo.21270699).  
- Goldberger et al., PhysioNet / SDDB.  
- Greenwald (1986).  
- Dans la plateforme : **Evidence** + **Périmètre du noyau**.
