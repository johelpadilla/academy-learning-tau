# Domaine : Dynamique sociale — polarisation (modèle jouet)

### Objectifs d’apprentissage
1. Voir une cascade de polarisation comme réorganisation ordinale opinions + interaction.
2. Séparer l’usage pédagogique de tout claim de prédiction sociale/politique.
3. Contraster avec le contrôle AR : sans latent partagé, |Δτ_s| est souvent petit.

**Maturité:** ★★☆☆☆ — Démo conceptuelle. Pas de cohorte sociale validée sur la plateforme.

---

## 1. Contexte scientifique

Dans des modèles simples d’opinion, deux pôles et une intensité d’interaction peuvent passer d’un régime « pluraliste bruyant » à un régime **anti-corrélé** à forte interaction. C’est un changement de **structure relationnelle**.

---

## 2. Pourquoi le panneau classique ne suffit pas

- Pas de données réelles de réseaux sociaux en v1.0.
- Aucune prétention à prédire élections, conflits ou viralité.
- La démo existe pour **enseigner la grammaire** τ_s / RECD dans les systèmes collectifs.

---

## 3. Valeur de τ_s + RECD

- Variables : `opinion_a`, `opinion_b`, `interaction`.
- Post-événement : un latent de polarisation force A ≈ −B et gonfle l’interaction.
- La lecture duale demande si le Δ est résiduel face aux surrogates d’indépendance croisée.

---

## 4. Données d’exemple sur la plateforme

- `social_polarization_demo` (généré sur la plateforme, événement marqué).

---

## 5. Fiche de conception (schéma uniforme)

| Field | Value |
|-------|--------|
| **Proxy** | \(X=[\mathrm{opinion\_a}, \mathrm{opinion\_b}, \mathrm{interaction}]\) |
| **Événement** | Début de cascade de polarisation (conçu) |
| **Preset Lab** | `social` · pedagogical only |
| **Démos principales** | `social_polarization_demo` |
| **Maturité** | Low–medium (conceptual transfer) |

### Phrases autorisées (exemples)
- La cascade jouet montre une réorganisation ordinale sous latent conçu…
- Enseignement critique de sciences sociales computationnelles avec disclaimer explicite.

### Phrases interdites (v1.0)
- Prédit élections / conflits / viralité
- Preuve causale de polarisation réelle

---

## 6. Exercice guidé

Comparer social_polarization_demo vs synthetic_ar_noise en lecture duale.

---

## 7. Références

- Modèles jouets de dynamique d’opinion ; littérature critique CSS.
