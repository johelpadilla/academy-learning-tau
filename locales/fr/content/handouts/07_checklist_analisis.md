# Checklist d’analyse — remise Lab / rapport court

| Champ | Valeur |
|-------|--------|
| **Document** | Handout 07 · Checklist d’analyse |
| **Usage** | Cocher chaque item avant envoi ; si N/A, justifier en une ligne |
| **Score** | Auto-évaluation optionnelle /12 alignée sur la grille de lecture duale |
| **Version** | 1.1 · 2026 |

---

## A. Question et portée

- [ ] Question scientifique en une phrase (réorganisation relationnelle, pas « prédire X »)  
- [ ] Domaine et **maturité empirique** déclarés  
- [ ] Démo synthétique vs données réelles distingués  
- [ ] Limites éthiques (pas clinique / pas opérationnel) mentionnées  
- [ ] Méthodes complémentaires vs concurrentes énoncées si pertinent (p.ex. TE non substituée silencieusement)

## B. Données

- [ ] Source (ID catalogue / CSV / PhysioNet / …)  
- [ ] Dimensions T × N  
- [ ] Variables utilisées et pourquoi (adapter / théorie)  
- [ ] Preprocess (z-score, proxy RR–|ΔRR|, manquants, ties)  
- [ ] Licence / ToS de tiers respectée  
- [ ] Note d’anonymisation / IRB si données humaines hors démos

## C. Design

- [ ] Événement marqué **ou** partition exploratoire déclarée  
- [ ] Preset de domaine ou justification de W, stride, m, θ₃  
- [ ] Seed de surrogates fixée  
- [ ] Mode fast/full et n_surr alignés sur le claim  
- [ ] Pas de chasse d’événement *post hoc* non déclarée

## D. Résultats numériques

- [ ] Δτ_s (signe + magnitude)  
- [ ] mean_excess3 et Δexcess3  
- [ ] p_surr et méthode (phase-shuffle / IAAFT)  
- [ ] Au moins une EWS classique en parallèle  
- [ ] Figures : séries+événement, τ_s, RECD/excess3, EWS  
- [ ] Extensions (si utilisées) : plage W et/ou β₀/β₁ + backend

## E. Interprétation

- [ ] Lecture duale (concordance / discordance / quietude)  
- [ ] Φ₃ non surinterprété si excess3 est le signal  
- [ ] Signe context-dependent considéré  
- [ ] Comparaison à un contrôle (AR ou baseline) si applicable  
- [ ] Claims bornés au design et à la maturité

## F. Reproductibilité et livraison

- [ ] `repro_hash` copié  
- [ ] Export Markdown  
- [ ] Export JSON (si exigé)  
- [ ] Paragraphe Methods  
- [ ] Citations : logiciel + dataset + paper de domaine  

---

## Auto-évaluation optionnelle

| Critère (0–2) | Note |
|---------------|------|
| Question et portée | |
| Données et design | |
| Métriques + nulls | |
| Lecture duale | |
| Écriture bornée | |
| Hash / exports | |
| **Total /12** | |

**Repère :** ≥9 pour une remise Lab solide ; 12 seulement si complet et honnête sur les limites.

---

## Contrôles rapides de l’enseignant (3 questions)

1. L’étudiant peut-il re-courir et retrouver le hash ?  
2. La catégorie de claim est-elle correcte (démo / pilote / transfert) ?  
3. Un rapporteur comprendrait-il ce qui **n’a pas** été revendiqué ?

---

*Checklist STP v1.1 · imprimable*
