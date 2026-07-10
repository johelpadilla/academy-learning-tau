# Domaine : Neurosciences — crises épileptiques (style CHB-MIT)

### Objectifs d’apprentissage
1. Traiter l’EEG multicanal comme un système relationnel avec événement annoté.
2. Contraster le CSD par canal avec la co-ordination ordinale (τ_s / RECD).
3. Énoncer le périmètre non clinique de toute interprétation pré-ictale.

**Maturité:** ★★★☆☆ — Pipeline prêt ; profondeur empirique en consolidation (sous CCTP).

---

## 1. Contexte scientifique

Les **crises épileptiques** sont des transitions de régime de la dynamique corticale. L’EEG multicanal est le prototype à nombreuses variables, événements annotés et intérêt **pré-ictal**. CHB-MIT (PhysioNet) fournit des enregistrements pédiatriques ; la plateforme utilise des extraits traités ou synthétiques pre-ictal-like.

---

## 2. Pourquoi le panneau classique ne suffit pas

- Un seul canal peut ne pas montrer de CSD clair.
- Artéfacts et sommeil confondent var/AR1.
- La transition est **spatialement distribuée** : la signature est dans la **synchronisation de motifs**.

---

## 3. Valeur de τ_s + RECD

- Multivarié : bandpowers ou enveloppes de 4–8 canaux/bandes.
- Φ₁–Φ₃ capturent la **co-ordination symbolique** pré-ictale.
- excess3 comme proxy de configuration de réseau irréductible.
- Comparer avec des indices de sync classiques (PLV, etc.) en mode Full si disponible.

---

## 4. Données d’exemple sur la plateforme

- `eeg_like_demo` — transition de couplage conçue entre canaux.
- Scripts de téléchargement sous ToS PhysioNet pour extraits réels.

---

## 5. Fiche de conception (schéma uniforme)

| Field | Value |
|-------|--------|
| **Proxy** | \(X=[\mathrm{bandpower}_1,\ldots,\mathrm{bandpower}_k]\) or channel envelopes |
| **Événement** | Onset de crise / marqueur pré-ictal (annoté ou conçu) |
| **Preset Lab** | `neuroscience` · m=3 · dual reading; extensions optional |
| **Démos principales** | `eeg_like_demo` |
| **Maturité** | Medium–high (pedagogical + emerging empirical) |

### Phrases autorisées (exemples)
- La co-ordination ordinale change vers l’événement conçu/annoté…
- Grammaire ictale de jouet pour l’entraînement méthodologique ; pas un prédicteur de crise.

### Phrases interdites (v1.0)
- Dispositif validé de prédiction de crises
- Aide à la décision clinique pour unités d’épilepsie

---

## 6. Exercice guidé

Lab → `eeg_like_demo` → neuroscience → paragraphe de lecture duale + disclaimer non clinique.

---

## 7. Références

- CHB-MIT PhysioNet ; littérature de prédiction de crises ; cadre Tau ordinal.
