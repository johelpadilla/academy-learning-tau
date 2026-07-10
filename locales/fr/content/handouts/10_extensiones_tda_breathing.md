# Extensions opérationnelles — Breathing window et TDA / Betti

| Champ | Valeur |
|-------|--------|
| **Document** | Handout 10 · Extensions |
| **Public** | Étudiants de Lab (semaines 3–6) et enseignants |
| **Statut** | **Opérationnel** dans le Lab STP (pas « en développement ») |
| **Rôle** | Extension pédagogique du noyau τ_s + RECD + EWS + surrogates |
| **Version** | 1.1 · 2026 |

---

## Objectifs d’apprentissage

1. Séparer le **claim du noyau** du **contraste d’extension**.  
2. Interpréter W(t) adaptative sans inventer de couplage.  
3. Rapporter β₀/β₁ avec le bon backend (`ripser` vs `vr_skeleton`).  
4. Garder les claims de niveau thèse sur le noyau de lecture duale ordinale.

---

## 1. Message clé

| Couche | Composants | Claim principal ? |
|--------|------------|-------------------|
| **Noyau** | τ_s, RECD/excess3, EWS classiques, surrogates, hash | Oui |
| **Extensions** | Breathing window, TDA β₀/β₁, mémoire ordinale | Complément / contraste |

Le Lab **ne dépend pas** de TDA ni du breathing pour fonctionner. Quand ils sont activés, ils apparaissent sous **Extensions**, dans le rapport et dans Methods.

---

## 2. Breathing window

### Idée

En régimes volatils, une grande W fixe **lisse trop** la transition.  
Breathing mappe la **volatilité locale** vers une taille de fenêtre impaire :

- haute volatilité → **W plus courte** (plus réactif)  
- régime stable → **W plus longue** (plus lisse)

### Comment l’utiliser dans le Lab

1. Activer **Breathing window** (défaut en Full).  
2. Exécuter.  
3. Onglet Extensions ou axe secondaire sur τ_s : série **W(t)**.  
4. Documenter la plage W observée (p.ex. W∈[21–101]).

### Lecture honnête

Breathing change la **résolution temporelle** de τ_s. Il n’invente pas de couplage : si le contrôle AR reste plat, ne forcez pas un récit.

### Reporting

Énoncer : activé/désactivé, plage W observée, et si le Δ primaire vient d’une course à W fixe ou breathing.

---

## 3. TDA / Betti en fenêtres

### Idée

Dans chaque fenêtre, construire un **point cloud** (delay embedding multivarié) et résumer les nombres de Betti :

- **β₀** — composantes connexes (le cloud se fragmente-t-il ou s’unifie-t-il ?)  
- **β₁** — cycles (structure « à trous » / 1-squelette)

### Backends

| Backend | Quand | Notes |
|---------|-------|-------|
| **ripser** | Si `pip install systemic-tau-platform[tda]` | Persistance classique |
| **VR 1-skeleton** | Toujours (fallback) | β₀ = composantes ; β₁ = \|E\|−\|V\|+β₀ |

Les deux sont des **proxys pédagogiques** de topologie d’état. Ce ne sont pas un pipeline TDA multi-échelle de production.

### Comment l’utiliser dans le Lab

1. Activer **TDA / Betti**.  
2. Exécuter (plus coûteux que τ_s seul ; Fast+TDA sur démos courtes ou Full).  
3. Onglet Extensions : courbes β₀(t), β₁(t) + marqueur d’événement.  
4. Métriques : mean/Δ β₀, β₁ et `tda_backend` dans JSON/rapport.

### Lecture duale élargie

| Question | Outil |
|----------|-------|
| L’ordre partagé se réorganise-t-il ? | τ_s, excess3 |
| Le panneau univarié bouge-t-il ? | var / AR1 |
| La topologie du cloud d’états change-t-elle ? | β₀ / β₁ |
| Le Δ relationnel est-il résiduel sous null croisé ? | p_surr |

**Ne remplacez pas** la colonne relationnelle par la TDA. Utilisez la TDA pour **contraster**.

---

## 4. Mémoire ordinale (bref)

La MI symbolique lag-1 et cross-MI estiment la **persistance d’information ordinale**.  
Rapporter comme extension ; ne pas traiter comme graphe causal.

---

## 5. CLI

```bash
# Extensions on (aussi défaut avec --mode full)
stp analyze data.csv --domain synthetic --breathing --tda -o report.md --json out.json

stp analyze data.csv --mode full -o report.md
```

---

## 6. Checklist de remise avec extensions

- [ ] Claim principal basé sur τ_s / excess3 / p_surr (+ EWS)  
- [ ] Breathing/TDA déclarés comme extension  
- [ ] Backend TDA rapporté (`ripser` ou `vr_skeleton`)  
- [ ] Plage W si breathing  
- [ ] Hash de la course  
- [ ] Pas de promesses cliniques/opérationnelles basées sur β₁ seul  

---

## 7. Erreurs fréquentes

| Erreur | Correction |
|--------|------------|
| « La TDA n’est pas encore prête » | Elle est opérationnelle comme extension ; mettez à jour l’app |
| Publier seulement β₁ | Ajouter la lecture duale du noyau |
| Confondre le fallback VR avec ripser multi-échelle | Citer le backend |
| Activer TDA sur d’énormes séries sans subsample | Utiliser Fast ou démos du catalogue |
| Traiter les changements de W breathing comme « preuve de couplage » | Résolution ≠ structure |

---

## 8. Conseil niveau thèse

Un chapitre de thèse défendable :

1. Mène avec lecture duale relationnelle + nulls.  
2. Utilise les extensions en sous-section de **sensibilité / contraste**.  
3. Énonce versions logicielles et backends.  
4. Garde la maturité de domaine explicite.

---

*Handout extensions STP v1.1 · Breathing + TDA opérationnels dans le Lab*
