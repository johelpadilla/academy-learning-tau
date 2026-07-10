# Domaine : Épidémiologie — dengue et hyper-persistance

### Objectifs d’apprentissage
1. Transférer la grammaire τ_s + RECD du cardio à un système socio-écologique.
2. Expliquer pourquoi var/AR1 confondent saisonnalité et proximité d’épidémie.
3. Formuler une hypothèse falsifiable sur la cohérence ordinale cases–climat.

**Maturité:** ★★★★☆ — récit et preprints matures ; CCTP reste la cohorte phare de la plateforme.

---

## 1. Contexte scientifique

La **dengue** est un système socio-écologique forcé par le climat, le vecteur *Aedes*, l’immunité et la mobilité. L’incidence hebdomadaire montre des **épidémies**, des plateaux et parfois une **hyper-persistance**. Porto Rico et les séries type DengAI (San Juan / Iquitos) sont des laboratoires naturels d’alerte précoce.

---

## 2. Pourquoi le panneau classique ne suffit pas

- L’incidence est **discrète, bruyante et saisonnière** ; var/AR1 confondent saisonnalité et brote.
- Le « système » n’est pas seulement `cases(t)` : c’est le **couplage** cases–climat–vecteur.
- Les seuils univariés alertent **tard** ou avec beaucoup de faux positifs.
- Le ML prédictif peut viser le nombre tout en **occultant** le mécanisme de réorganisation.

---

## 3. Valeur de τ_s + RECD

| Apport | Contenu |
|--------|----------|
| Multivarié ordinal | \(X = [z(\mathrm{cases}), z(\mathrm{temp}), z(\mathrm{precip}), \ldots]\) |
| Hyper-persistance ordinale | Φ₂ (relations soutenues) et couches de persistance Tau |
| RECD | « Horloge » de l’épidémie : ticks quand la configuration conjointe devient synergique |
| Comparabilité | Même langage que cardio/écologie → science des systèmes |

---

## 4. Données d’exemple sur la plateforme

- `dengue_like_demo` — épidémie synthétique avec bascule ordinale conçue.
- Variables : cases, température, précipitation (z-score).
- Fenêtres d’épidémie pédagogiques (percentile élevé ou labels historiques).

---

## 5. Fiche de conception (schéma uniforme)

| Field | Value |
|-------|--------|
| **Proxy** | \(X=[z(\mathrm{cases}), z(\mathrm{temp}), z(\mathrm{precip})]\) |
| **Événement** | Début d’épidémie / régime de transmission élevée |
| **Preset Lab** | `epidemiology` · domain-default W/stride · m=3 · dual reading required |
| **Démos principales** | `dengue_like_demo` |
| **Maturité** | High (transfer; not operational surveillance) |

### Phrases autorisées (exemples)
- La cohérence ordinale cases–climat monte avant le pic d’incidence sous ce design…
- Transfert méthodologique depuis la grammaire CCTP ; pas un nowcast opérationnel.
- Les nulls / surrogates tenant compte de la saisonnalité doivent être rapportés.

### Phrases interdites (v1.0)
- Alarme opérationnelle d’épidémie pour les agences de santé publique
- Remplace les systèmes de surveillance épidémiologique
- Preuve causale d’une épidémie urbaine réelle à partir du seul demo

---

## 6. Exercice guidé

1. Lab → `dengue_like_demo` → preset epidemiology → Fast.
2. Tableau dual : Δτ_s, excess3, var/AR1, p_surr.
3. Un paragraphe : ce qui est analogue à l’« événement » cardio, ce qui **n’est pas** affirmé.

---

## 7. Références

- Preprints dengue Tau/RECD de l’auteur (2025–2026).
- DengAI DrivenData ; littérature EWS vectorielles.
