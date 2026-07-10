# Guide de lecture duale — Relationnel vs EWS classiques

| Champ | Valeur |
|-------|--------|
| **Document** | Handout 06 · Lecture duale |
| **Public** | Étudiants de Lab et auteurs de rapports courts |
| **Règle d’or** | Un seul panneau ne suffit jamais pour une conclusion de systèmes |
| **Version** | 1.1 · 2026 |

---

## Objectifs d’apprentissage

1. Structurer un rapport à deux panneaux (relationnel + classique).  
2. Classer les résultats en quatre motifs archétypaux avec prose défendable.  
3. Remplir le modèle de paragraphe de remise avec chiffres et portée.

---

## 1. Qu’est-ce que la lecture duale

Présenter **en parallèle** :

| Colonne A — Relationnel (noyau STP) | Colonne B — Classique (contrôle) |
|-------------------------------------|----------------------------------|
| τ_s(t), Δτ_s | Variance en fenêtre |
| excess3, Δexcess3, Φ₃ | AR(1) / autocorrélation |
| p_surr (phase-shuffle / IAAFT) | Autres EWS univariées si utilisées |
| Événement et design pre/post | Même événement / même W si possible |

La plateforme calcule les deux dans le Lab. L’**interprétation humaine** déclare concordance ou discordance.

---

## 2. Quatre motifs typiques (modèles)

### A. Forte concordance

- Relationnel : |Δ| notable + p_surr bas  
- Classique : var et/ou AR1 bougent aussi vers l’événement  

**Texte modèle :**  
*« Les panneaux relationnel et classique indiquent un changement vers t=… ; le null phase-shuffle n’explique pas Δτ_s (p=…). Interprétation bornée au design … et à la maturité du domaine …. »*

### B. Relationnel oui, classique ambigu

- Relationnel : signal  
- Classique : plat ou contradictoire  

**Texte modèle :**  
*« Le panneau univarié est ambigu ; la réorganisation ordinale (Δτ_s=…, Δexcess3=…) est le résultat principal sous null d’indépendance croisée. Cohérent avec des transitions multivariées où le CSD univarié échoue. »*

### C. Classique oui, relationnel non

- Var/AR1 montent ; τ_s stable ; p_surr élevé  

**Texte modèle :**  
*« Il y a ralentissement/amplitude univariée sans évidence de réorganisation ordinale croisée sous ce design. Aucune détection relationnelle n’est revendiquée. »*

### D. Quasi-nul (contrôle)

- Comme `synthetic_ar_noise`  

**Texte modèle :**  
*« Contrôle : |Δτ_s| petit ; compatible avec l’absence de transition conçue. »*

---

## 3. Modèle de paragraphe pour remises (copier et remplir)

```
Design. Série T×N = …×… ; domaine = … ; W=…, stride=…, m=…, delay=… ;
événement à t=… (ou partition exploratoire moitié/moitié).
Surrogates : méthode=…, n=…, seed=….

Résultats relationnels. Δτ_s = … ; mean_excess3 = … ; Δexcess3 = … ;
p_surr(τ_s) = … [optionnel p_surr(excess3)=…].

Résultats classiques. Δvar ≈ … ; comportement AR1 : ….

Lecture duale. Concordance / discordance / quietude : ….
Portée. Maturité du domaine : … ; limites : pas d’usage clinique/opérationnel.
Reproductibilité. repro_hash = ….
```

---

## 4. Erreurs de lecture duale

| Erreur | Pourquoi cela échoue |
|--------|----------------------|
| Cacher le panneau classique s’il « gêne » | Sélection de résultats |
| Déclarer une « prédiction » à partir d’un p bas | p ≠ valeur prédictive externe |
| Mélanger des W différentes entre panneaux sans le dire | Incomparabilité |
| Utiliser une démo synthétique comme évidence de domaine réel | Mauvaise catégorie de claim |
| Ignorer le signe context-dependent | Un Δ négatif peut être une vraie réorganisation |
| Rapporter seulement Φ₃ quand excess3 est le signal | Artefact de seuil |

---

## 5. Grille rapide (0–2 par item)

1. Question scientifique explicite  
2. Design (événement / partition) déclaré  
3. Métriques relationnelles complètes  
4. Panneau classique rapporté  
5. Nulls et n_surr  
6. Conclusion bornée + hash  

**Maximum 12.** Une remise de Lab solide ≥ 9.

---

## 6. Mini-exemples (une ligne)

| Scénario | Ligne duale |
|----------|-------------|
| Switch logistique couplé | Grand Δ relationnel, p bas ; classique peut ou non concorder — rapporter les deux |
| AR indépendants | Petit Δ, p haut ; classique calme — contrôle null réussi |
| Démo cardio | Énoncer les limites d’échantillon ; ne pas revendiquer de prédiction certifiée |

---

*Guide de lecture duale STP v1.1 · coller dans le LMS avec le syllabus.*
