# Domaine : Systèmes complexes / finance — régimes de volatilité

### Objectifs d’apprentissage
1. Relier les bascules de régime de volatilité à des questions de couplage ordinal.
2. Contraster les métriques de vol classiques réactives avec la lecture duale.
3. Imposer une frontière éthique stricte non-trading.

**Maturité:** ★★★☆☆ — Domaine de transfert avancé optionnel sur le parcours.

---

## 1. Contexte scientifique

Les marchés exhibent des **changements de régime de volatilité**, contagion et synchronisation d’actifs. Ce ne sont pas des systèmes biologiques, mais ils partagent des **transitions de couplage** multivariées.

---

## 2. Pourquoi le panneau classique ne suffit pas

- Vol réalisée, VIX, corrélations rolling sont souvent **réactifs**.
- Le ML de régime (HMM, etc.) peut prédire sans offrir une décomposition ordinale type Φ₁–Φ₃.

---

## 3. Valeur de τ_s + RECD

- Proxy : \(X = [z(r_t), z(\sigma_t^{\mathrm{RV}})]\) ou multi-actifs de rangs.
- Détecter la **co-ordination de motifs rendement/vol** avant des régimes de stress.
- Exercice avancé de transferabilité du paradigme.

---

## 4. Données d’exemple sur la plateforme

- `finance_like_demo` — bascule de régime de vol conçue.
- Optionnel externe : indice journalier + vol réalisée 21j (fourni par l’utilisateur).

---

## 5. Fiche de conception (schéma uniforme)

| Field | Value |
|-------|--------|
| **Proxy** | \(X=[z(r_t), z(\sigma_t^{\mathrm{RV}})]\) |
| **Événement** | Bascule de régime de volatilité / onset de stress (conçu ou défini par l’utilisateur) |
| **Preset Lab** | `finance` · methodological transfer only |
| **Démos principales** | `finance_like_demo` |
| **Maturité** | Medium — optional advanced; **no investment advice** |

### Phrases autorisées (exemples)
- Transfert méthodologique du couplage ordinal vers une démo de régime de vol…
- Usage strictement éducatif / recherche méthodologique.

### Phrases interdites (v1.0)
- Signal de trading / alpha / conseil d’investissement
- Système d’algo-trading certifié

---

## 6. Exercice guidé

Lab → finance_like_demo → lecture duale + phrase de clôture non-trading explicite.

---

## 7. Références

- Littérature des régimes de volatilité ; handout d’éthique STP § disclaimer finance.
