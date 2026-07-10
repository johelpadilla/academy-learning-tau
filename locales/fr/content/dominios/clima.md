# Domaine : Climat et hydrologie — sécheresse et régimes hydro-climatiques

### Objectifs d’apprentissage
1. Relier la littérature des seuils critiques (CSD) aux ordinaux multivariés.
2. Distinguer un changement de niveau (plus de chaleur) d’une réorganisation temp–précip–sol.
3. Formuler une hypothèse falsifiable de latent de sécheresse sans claim de forecast opérationnel.

**Maturité:** ★★★☆☆ — Pédagogie forte et pont CSD ; pas un produit de forecast climatique.

---

## 1. Contexte scientifique

Sécheresses et bascules hydro-climatiques s’étudient avec température, précipitation et humidité du sol. L’alerte classique demande : le système approche-t-il un régime sec irréversible ? La question τ_s est complémentaire : **comment se réordonnent les relations** sous un latent de sécheresse partagé ?

---

## 2. Pourquoi le panneau classique ne suffit pas

- La saisonnalité confond var/AR1.
- Un seul indice de sécheresse effondre la structure multivariée.
- L’« événement » est souvent un **régime**, pas un instant ponctuel.

---

## 3. Valeur de τ_s + RECD

| Apport | Contenu |
|--------|----------|
| Triade climatique | \(X = [\mathrm{temp}, \mathrm{precip}, \mathrm{soil}]\) |
| Réorganisation | Le latent de sécheresse couple des canaux auparavant quasi saisonniers |
| Comparabilité | Même langage que lacs (écologie) et épidémies |

---

## 4. Données d’exemple sur la plateforme

- `climate_drought_demo` : synthétique avec début de régime sec marqué.
- Vérité terrain conçue (latent partagé post-événement ; pas de données satellitaires réelles en v1.0).

---

## 5. Fiche de conception (schéma uniforme)

| Field | Value |
|-------|--------|
| **Proxy** | \(X=[\mathrm{temp}, \mathrm{precip}, \mathrm{soil}]\) |
| **Événement** | Début du régime sec / activation du latent de sécheresse |
| **Preset Lab** | `climate` · dual reading mandatory |
| **Démos principales** | `climate_drought_demo` |
| **Maturité** | Medium — teaching emphasis |

### Phrases autorisées (exemples)
- Réorganisation relationnelle sous latent de sécheresse conçu…
- Transfert pédagogique ; pas d’alertes officielles de sécheresse.

### Phrases interdites (v1.0)
- Forecast officiel de sécheresse / système d’alerte d’agence
- Prédiction garantie d’aridification irréversible

---

## 6. Exercice guidé

Lab → climate_drought_demo → paragraphe dual + phrase de maturité.

---

## 7. Références

- Scheffer et al., transitions critiques / CSD.
- Indices de sécheresse (SPI, SPEI) comme contraste univarié.
