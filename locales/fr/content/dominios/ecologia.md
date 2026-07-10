# Domaine : Écologie des écosystèmes — eutrophisation des lacs

### Objectifs d’apprentissage
1. Relier la littérature CSD des lacs aux observables ordinaux multivariés.
2. Traiter nutriments–Chl-a–DO comme une triade relationnelle.
3. Transférer le langage méthodologique physiologie ↔ écologie sans overclaim.

**Maturité:** ★★★☆☆ — Pédagogie forte ; profondeur empirique à étendre en v1.x.

---

## 1. Contexte scientifique

Les lacs peu profonds peuvent basculer d’un état **clair oligotrophe** à un état **turbide eutrophe** (Scheffer et al.). Les séries de chlorophylle-a, nutriments et oxygène dissous capturent cette transition.

---

## 2. Pourquoi le panneau classique ne suffit pas

Ce domaine est le **foyer historique** des EWS de CSD. Elles fonctionnent dans beaucoup de modèles et certains lacs. Elles échouent ou se débattent quand la saisonnalité est forte, la gestion humaine change les nutriments, ou la transition est un changement de **réseau trophique**.

---

## 3. Valeur de τ_s + RECD

- Même langage relationnel que la physiologie : le lac « coordonne » nutriments–Chl-a–DO.
- RECD offre une horloge d’**événements de réorganisation écologique**.
- Permet le **transfert méthodologique** cœur ↔ lac.

---

## 4. Données d’exemple sur la plateforme

- `ecology_like_demo` — séries mensuelles type Mendota (chla, tp, do, temp en z-score).
- Annotation de régime si seuil historique de Chl-a.

---

## 5. Fiche de conception (schéma uniforme)

| Field | Value |
|-------|--------|
| **Proxy** | \(X=[\mathrm{chla}, \mathrm{tp}, \mathrm{do}, \mathrm{temp}]\) (z-scored) |
| **Événement** | Bascule clair → turbide / onset de bloom |
| **Preset Lab** | `ecology` · dual reading vs classical CSD panel |
| **Démos principales** | `ecology_like_demo` |
| **Maturité** | Medium (strong teaching bridge to CSD literature) |

### Phrases autorisées (exemples)
- Réorganisation relationnelle autour d’une bascule de régime conçue ou historique…
- Transfert de méthode depuis CCTP ; pas une alarme opérationnelle de gestion de lac.

### Phrases interdites (v1.0)
- Produit opérationnel d’alerte d’eutrophisation
- Preuve causale pour un lac réel à partir du seul demo

---

## 6. Exercice guidé

Lab → ecology_like_demo → comparer la lecture duale à une histoire univariée de variance de Chl-a.

---

## 7. Références

- Scheffer, *Critical Transitions in Nature and Society*.
- Publications de données NTL LTER.
