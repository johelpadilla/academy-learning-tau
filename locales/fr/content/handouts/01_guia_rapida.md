# Systemic Tau Platform — Guide de démarrage rapide

| Champ | Valeur |
|-------|--------|
| **Document** | Handout 01 · Guide rapide |
| **Niveau** | Postgraduate / spécialisation · première séance |
| **Temps** | 15–25 minutes jusqu’à une première expérience documentée |
| **Plateforme** | Academy Learning Tau · STP v1.0 |
| **Version** | 1.1 · 2026 |

---

## 1. Objet scientifique (une phrase)

Enseigner à **formuler, calculer et documenter** une analyse de **réorganisation relationnelle ordinale** — Systemic Tau (τ_s) + RECD/excess3 — en **lecture duale** face aux *early warning signals* (EWS) classiques (variance, AR(1)), sous nulls de dépendance croisée (surrogates), avec **reproductibilité** (hash SHA-256).

**Ce n’est pas** un dispositif clinique certifié, une alerte épidémiologique opérationnelle, ni un moteur de trading ou de scoring social.

---

## 2. Objectifs d’apprentissage

À la fin de la séance, vous pourrez :

1. Distinguer une question **relationnelle** d’une question **uniquement univariée**.  
2. Exécuter un contrôle positif et un contrôle quasi-nul dans le Laboratoire.  
3. Rapporter Δτ_s, p_surr et au moins une EWS classique en parallèle.  
4. Exporter Markdown + Methods + `repro_hash`.

---

## 3. Parcours en 5 étapes (UI)

| Étape | Où | Action de niveau postgraduate |
|-------|-----|-------------------------------|
| 1 | **Home** | Lire la portée du noyau : prêt / extension / non-revendications. |
| 2 | **Fondements** | τ_s vs EWS ; RECD Φ₁–Φ₃ ; excess3 ; CSD comme cadre classique. |
| 3 | **Mathématiques** | Sandbox Bandt–Pompe (m=3 → 6 symboles) ; ne sautez pas l’alphabet ordinal. |
| 4 | **Laboratoire** | Catalogue → Analyser → lecture duale → Exporter. |
| 5 | **Évidence / Bibliothèque** | Ancre CCTP/SDDB et corpus de publications ; ne pas généraliser à l’aveugle. |

---

## 4. Première expérience (protocole minimal)

1. Ouvrez **Laboratoire**.  
2. Catalogue → `synthetic_coupled_logistic` (switch de couplage avec *ground truth* de conception).  
3. Domaine **Synthétique** · mode **Fast** · `n_surr` 4–8 · graine fixée.  
4. Observez |Δτ_s| et p_surr ; comparez au contrôle `synthetic_ar_noise` (quasi-nul).  
5. Téléchargez le rapport **Markdown**, le paragraphe **Methods** et copiez le **`repro_hash`**.

**Questions de clôture (3–5 lignes) :**

- Le Δ du logistique couplé reste-t-il extrême sous *phase-shuffle* ?  
- Le panneau EWS (var/AR1) concorde, se tait ou contredit ?  
- Quelle revendication **ne doit pas** être faite à partir d’une démo synthétique ?

---

## 5. Contrôles mentaux avant interprétation

| Contrôle | Pourquoi c’est important |
|----------|--------------------------|
| N ≥ 2 (ou proxy RR + \|ΔRR\| documenté) | Le noyau est relationnel |
| Preset de domaine avant de retoucher W | Évite le *p-hacking* de fenêtre |
| Lecture duale obligatoire | Un seul panneau ne suffit pas |
| p_surr + taille d’effet | Ne publiez jamais le p seul |
| Signe *context-dependent* | Hausse ou baisse peut être une vraie réorganisation |
| Maturité du domaine | Démo ≠ cohorte ; cardio ≠ climat |

---

## 6. Carte des matériaux téléchargeables

| Document | Usage dans le cours |
|----------|---------------------|
| Manuel utilisateur | Opération Lab + CLI |
| Théorie τ_s + RECD | Cadre conceptuel postgraduate |
| Mathématiques pratiques | Notation, Bandt–Pompe, nulls |
| Cheat-sheet du Lab | Presets et formulations autorisées |
| Lecture duale | Modèles de rapport |
| Checklist d’analyse | Remise / auto-évaluation /12 |
| Syllabus 6 semaines | Conception du cours et grille |
| Éthique et portée | Revendications honnêtes |
| Extensions (Breathing / TDA) | Complément, pas substitut du noyau |
| FAQ + Glossaire | Malentendus de relecture par les pairs |

---

## 7. CLI (optionnel)

```bash
stp serve
stp analyze donnees.csv --domain cardiology -o rapport.md --json resultat.json
```

---

## 8. Citation minimale d’une course

1. Logiciel : Systemic Tau Platform v1.0.  
2. Jeu de données (ID catalogue ou source originale).  
3. Article/preprint de domaine le cas échéant.  
4. `repro_hash` de la course citée.

---

*Matériel pédagogique STP v1.1 · usage académique avec citation · ne remplace pas la validation externe ni l’éthique institutionnelle.*
