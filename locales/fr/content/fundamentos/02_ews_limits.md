# Fondements — EWS classiques et leurs limites

| Champ | Valeur |
|-------|--------|
| **Module** | Fondements 02 |
| **Niveau** | Postgraduate |
| **Version** | 1.1 · 2026 |

---

## Objectifs d’apprentissage

1. Définir variance et AR(1) comme signaux précoces classiques.  
2. Énoncer au moins trois modes de défaillance des EWS purement univariées.  
3. Expliquer pourquoi la lecture duale est requise, non optionnelle.

---

## 1. Cadre classique (CSD)

Le *critical slowing down* (CSD) suggère qu’à proximité de certaines bifurcations un système récupère plus lentement des perturbations. Empiriquement cela apparaît souvent comme :

- **variance** croissante en fenêtre glissante ;  
- **autocorrélation lag-1** (coefficient AR(1)) croissante ;  
- parfois d’autres indicateurs univariés.

Ces contrôles restent **précieux**. STP ne les écarte pas.

---

## 2. Limites qui motivent τ_s

| Limite | Conséquence |
|--------|-------------|
| Focus univarié | Rate une pure réorganisation de couplage |
| Ambiguïté de signe | La variance monte pour bien des raisons non critiques |
| Transitions multivariées | Les canaux locaux peuvent ne pas « ralentir » |
| Processus d’observation | Bruit, échantillonnage, non-stationnarité |
| Tentation de seuil | Langage d’« alerte » sans validation externe |

---

## 3. Règle pédagogique

Dans le Lab STP :

- Toujours calculer les **EWS classiques en parallèle**.  
- Ne jamais cacher un panneau classique gênant.  
- Déclarer concordance, discordance ou quietude.

---

## 4. Invite de micro-lab

Sur `synthetic_coupled_logistic` et `synthetic_ar_noise`, comparer var/AR1 vs Δτ_s. Écrire quatre lignes de lecture duale.

---

*Fondements 02 · STP v1.1*
