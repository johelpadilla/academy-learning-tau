# Domaine : Physiologie du sommeil — fragmentation circadienne

### Objectifs d’apprentissage
1. Étendre l’intuition cardio (RR) à une triade sommeil : HRV · activité · température.
2. Observer un changement de driver (circadien propre → fragmentation haute fréquence).
3. Comparer la maturité : CCTP est l’ancre ; le sommeil est un pont physiologique.

**Maturité:** ★★★☆☆ — Démo synthétique alignée sur des idées d’architecture du sommeil.

---

## 1. Contexte scientifique

L’architecture du sommeil coordonne variables autonomiques et comportementales. Quand le driver circadien se fragmente, ce n’est pas seulement « plus de bruit » : les **relations ordinales** se réorganisent.

---

## 2. Pourquoi le panneau classique ne suffit pas

- La cardiologie (CCTP/SDDB) fournit la cohorte de référence de la plateforme.
- Le sommeil offre un second système physiologique pour pratiquer le même langage sans claims cliniques.

---

## 3. Valeur de τ_s + RECD

- Triade proxy avec événement de fragmentation conçu (~70 %).
- Lecture duale vs histoires univariées d’« indice de fragmentation ».

---

## 4. Données d’exemple sur la plateforme

- `sleep_fragmentation_demo` — événement de fragmentation marqué.

---

## 5. Fiche de conception (schéma uniforme)

| Field | Value |
|-------|--------|
| **Proxy** | \(X=[\mathrm{HRV}, \mathrm{activity}, \mathrm{temp}]\) |
| **Événement** | Début de fragmentation circadienne (~70 % de la série) |
| **Preset Lab** | `physiology` · Fast for teaching |
| **Démos principales** | `sleep_fragmentation_demo` |
| **Maturité** | Medium — pedagogical physiological transfer |

### Phrases autorisées (exemples)
- Réorganisation relationnelle sous fragmentation de sommeil conçue…
- Pas un dispositif médical de scoring du sommeil.

### Phrases interdites (v1.0)
- Diagnostic clinique du sommeil
- Claim de dispositif médical

---

## 6. Exercice guidé

Lab → sleep_fragmentation_demo → dual + contraste de maturité avec la cardiologie.

---

## 7. Références

- Littérature d’architecture du sommeil ; CCTP comme ancre de maturité.
