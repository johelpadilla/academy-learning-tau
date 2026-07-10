#!/usr/bin/env python3
"""One-shot content upgrade: domain parity EN/FR + expanded assessment bank.

Run from repo root:
  .venv/bin/python scripts/upgrade_evaluator_fixes.py
"""

from __future__ import annotations

import copy
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
LOCALES = ROOT / "locales"

# ---------------------------------------------------------------------------
# Domain packs — postgraduate schema (proxy, event, maturity, claims, Lab)
# ---------------------------------------------------------------------------

DOMAINS: dict[str, dict] = {
    "cardiologia.md": {
        "en": """# Domain: Computational cardiology — pre-VF and SDDB

### Learning outcomes
1. Explain why var/AR1 can be ambiguous before ventricular fibrillation (VF).
2. Describe the proxy \(X=[z(\\mathrm{RR}), z(|\\Delta\\mathrm{RR}|)]\) and CCTP presets.
3. Apply the **dual-reading** protocol to a cardio-like case or SDDB sample.

**Empirical maturity in v1.0:** ★★★★★ (platform maximum) — CCTP pilot N=10.

---

## 1. Scientific context

**Sudden cardiac death** via **ventricular fibrillation (VF)** remains hard to anticipate from surface ECG. Holter records from the *Sudden Cardiac Death Holter Database* (SDDB, PhysioNet) are among the few public resources with hours of pre-event dynamics and a documented VF onset.

The **Cardiac Critical Transitions Protocol (CCTP)** applies Systemic Tau and ordinal RECD to **RR-interval** series to characterize relational reorganization of heart-rate dynamics **before** spontaneous VF.

**Guiding question:** not “does variance rise?”, but “does the relation between RR level and beat-to-beat variation reorganize?”.

---

## 2. Why classical metrics are insufficient here

In the CCTP cohort (N=10 high-quality records):

| Finding | Implication |
|---------|-------------|
| RR variance often **increases** | “CSD-like” signature present |
| AR(1) frequently **decreases** | Naive CSD fails |
| Intermittent pacing / AF in some records | “Noise” is clinical context, not blind garbage |

Interpreting only var/AR1 yields confusing readings or **conceptual false negatives**.

---

## 3. Differential value of τ_s + RECD

| Ingredient | Role in CCTP | In Lab v1.0 |
|------------|--------------|-------------|
| Proxy \(X = [z(\\mathrm{RR}),\\, z(\\|\\Delta\\mathrm{RR}\\|)]\) | Minimal physiologically motivated multivariate | Auto if 1 column; cardio-like simulates it |
| τ_s (W=101, stride=5) | Ordinal level–variability coupling | Preset `cardiology` |
| Φ₁–Φ₃ + **excess3** | Symbolic structure; excess3 primary under noise | RECD tab + metrics |
| Phase-shuffle | Cross-dependence null | n surrogates slider |
| Context-dependent sign | Reorganization, not a sign dogma | Interpret Δ + p + context |

**Key pilot finding (documented):**  
Δτ_s and Δexcess3 are significant in most records under surrogates, with **sign concordance in 8/10** cases, even when the classical panel is ambiguous.

---

## 4. Platform example datasets

| Resource | Role in the Lab |
|----------|-----------------|
| Sample `sddb_rr_38_demo.csv` | Strong signal / reference case |
| Sample `sddb_rr_51_demo.csv` | Intermittent pacing — quality flags and preset limits |
| **Cardio-like demo** generator | CCTP flow without PhysioNet dependency |

Typical columns: `rr_ms`, `abs_drr`, `z_rr`, `z_abs_drr`. Event: VF onset index (`vfon`) when available.

---

## 5. Design card (uniform schema)

| Field | Value |
|-------|--------|
| **Proxy** | \(X=[z(\\mathrm{RR}), z(\\|\\Delta\\mathrm{RR}\\|)]\) |
| **Event** | VF onset (`vfon`) or approach window |
| **Lab preset** | `cardiology` · W≈101 · stride≈5 · θ₃≈0.08 · m=3 |
| **Primary demos** | `sddb_rr_38_demo`, `sddb_rr_51_demo`, cardio-like |
| **Maturity** | Very high (CCTP anchor) |

### Allowed phrases (examples)
- “Relational reorganization significant vs phase-shuffle under this design…”
- “Classical panel ambiguous (var↑, AR1↓); relational panel moves in the approach…”
- “Not a clinical alarm device; N and sample limits apply.”

### Forbidden phrases (v1.0)
- “Predicts VF / validated real-time alarm”
- “Certified medical device / ICU decision support”
- “Causally proves sudden death risk for a patient”

---

## 6. Guided interpretation checklist

1. **Quality:** excess interpolation, pacing, artefacts?  
2. **Relational panel:** baseline vs approach τ_s; mean excess3 and Δ.  
3. **Nulls:** phase-shuffle p for Δτ_s (and excess3 if computed).  
4. **Classical panel:** var and AR1 — confirm, stay quiet, or contradict?  
5. **Concordance:** do τ_s and excess3 move together?  
6. **Bounded closing sentence** with non-clinical scope.

---

## 7. 20-minute exercise

1. Lab → **Cardio-like demo** → cardiology preset → Fast, n_surr=8.  
2. Table: Δτ_s, mean excess3, Δexcess3, p_surr, qualitative var/AR1.  
3. Write 4 dual-reading lines.  
4. (Optional) Compare samples 38 vs 51.

---

## 8. References

- Padilla-Villanueva — CCTP/SDDB (Zenodo 10.5281/zenodo.21270699).  
- Goldberger et al., PhysioNet / SDDB.  
- Greenwald (1986) — SDDB basis.  
- In platform: **Evidence** + **Core scope** (Learning path).
""",
        "fr": """# Domaine : Cardiologie computationnelle — pré-FV et SDDB

### Objectifs d’apprentissage
1. Expliquer pourquoi var/AR1 peuvent être ambigus avant une fibrillation ventriculaire (FV).
2. Décrire le proxy \(X=[z(\\mathrm{RR}), z(|\\Delta\\mathrm{RR}|)]\) et les presets CCTP.
3. Appliquer le protocole de **lecture duale** à un cas cardio-like ou un sample SDDB.

**Maturité empirique v1.0 :** ★★★★★ (maximum de la plateforme) — pilote CCTP N=10.

---

## 1. Contexte scientifique

La **mort subite cardiaque** par **fibrillation ventriculaire (FV)** reste difficile à anticiper depuis l’ECG de surface. Les Holter de la *Sudden Cardiac Death Holter Database* (SDDB, PhysioNet) sont parmi les rares ressources publiques avec des heures de dynamique pré-événement et un onset de FV documenté.

Le **Cardiac Critical Transitions Protocol (CCTP)** applique le Tau systémique et le RECD ordinal à des séries d’**intervalles RR** pour caractériser la réorganisation relationnelle de la dynamique de fréquence cardiaque **avant** une FV spontanée.

**Question guide :** non pas « la variance monte-t-elle ? », mais « la relation entre le niveau de RR et sa variation battement à battement se réorganise-t-elle ? ».

---

## 2. Pourquoi les métriques classiques sont insuffisantes ici

Dans la cohorte CCTP (N=10 enregistrements de haute qualité) :

| Constat | Implication |
|---------|-------------|
| La variance de RR **augmente** souvent | Signature « type CSD » présente |
| L’AR(1) **diminue** fréquemment | Le CSD naïf échoue |
| Pacing intermittent / FA dans certains enregistrements | Le « bruit » est du contexte clinique |

Interpréter seulement var/AR1 produit des lectures confuses ou des **faux négatifs conceptuels**.

---

## 3. Valeur différentielle de τ_s + RECD

| Ingrédient | Rôle dans CCTP | Dans le Lab v1.0 |
|------------|----------------|------------------|
| Proxy \(X = [z(\\mathrm{RR}),\\, z(\\|\\Delta\\mathrm{RR}\\|)]\) | Multivarié minimal physiologiquement motivé | Auto si 1 colonne ; cardio-like le simule |
| τ_s (W=101, stride=5) | Couplage ordinal niveau–variabilité | Preset `cardiology` |
| Φ₁–Φ₃ + **excess3** | Structure symbolique ; excess3 primaire | Onglet RECD + métriques |
| Phase-shuffle | Null de dépendance croisée | Curseur n surrogates |
| Signe dépendant du contexte | Réorganisation, pas dogme de signe | Interpréter Δ + p + contexte |

**Résultat clé du pilote (documenté) :**  
Δτ_s et Δexcess3 sont significatifs dans la plupart des enregistrements sous surrogates, avec **concordance de signe 8/10**, même quand le panneau classique est ambigu.

---

## 4. Jeux de données d’exemple

| Ressource | Fonction dans le Lab |
|-----------|----------------------|
| Sample `sddb_rr_38_demo.csv` | Signal fort / cas de référence |
| Sample `sddb_rr_51_demo.csv` | Pacing intermittent — flags de qualité |
| Générateur **Cardio-like demo** | Flux CCTP sans dépendre de PhysioNet |

Colonnes typiques : `rr_ms`, `abs_drr`, `z_rr`, `z_abs_drr`. Événement : index d’onset de FV (`vfon`) si disponible.

---

## 5. Fiche de conception (schéma uniforme)

| Champ | Valeur |
|-------|--------|
| **Proxy** | \(X=[z(\\mathrm{RR}), z(\\|\\Delta\\mathrm{RR}\\|)]\) |
| **Événement** | Onset de FV (`vfon`) ou fenêtre d’approche |
| **Preset Lab** | `cardiology` · W≈101 · stride≈5 · θ₃≈0.08 · m=3 |
| **Démos principales** | `sddb_rr_38_demo`, `sddb_rr_51_demo`, cardio-like |
| **Maturité** | Très élevée (ancre CCTP) |

### Phrases autorisées (exemples)
- « Réorganisation relationnelle significative vs phase-shuffle sous ce design… »
- « Panneau classique ambigu (var↑, AR1↓) ; le relationnel bouge dans l’approche… »
- « Pas un dispositif d’alarme clinique ; limites de N et d’échantillon s’appliquent. »

### Phrases interdites (v1.0)
- « Prédit la FV / alarme temps réel validée »
- « Dispositif médical certifié / aide à la décision en réanimation »
- « Prouve causalement le risque de mort subite pour un patient »

---

## 6. Checklist d’interprétation

1. **Qualité :** interpolation excessive, pacing, artéfacts ?  
2. **Panneau relationnel :** τ_s basal vs approche ; mean excess3 et Δ.  
3. **Nulls :** p phase-shuffle pour Δτ_s (et excess3 si calculé).  
4. **Panneau classique :** var et AR1 — confirment, se taisent ou contredisent ?  
5. **Concordance :** τ_s et excess3 bougent-ils ensemble ?  
6. **Phrase de clôture bornée** sans claim clinique.

---

## 7. Exercice de 20 minutes

1. Lab → **Cardio-like demo** → preset cardiology → Fast, n_surr=8.  
2. Tableau : Δτ_s, mean excess3, Δexcess3, p_surr, var/AR1 qualitatif.  
3. Rédiger 4 lignes de lecture duale.  
4. (Optionnel) Comparer samples 38 vs 51.

---

## 8. Références

- Padilla-Villanueva — CCTP/SDDB (Zenodo 10.5281/zenodo.21270699).  
- Goldberger et al., PhysioNet / SDDB.  
- Greenwald (1986).  
- Dans la plateforme : **Evidence** + **Périmètre du noyau**.
""",
    },
}


def _pack(
    title_en: str,
    title_fr: str,
    outcomes_en: list[str],
    outcomes_fr: list[str],
    maturity_en: str,
    maturity_fr: str,
    context_en: str,
    context_fr: str,
    why_en: str,
    why_fr: str,
    value_en: str,
    value_fr: str,
    data_en: str,
    data_fr: str,
    proxy: str,
    event_en: str,
    event_fr: str,
    preset: str,
    demos: str,
    maturity_tag: str,
    allowed_en: list[str],
    allowed_fr: list[str],
    forbidden_en: list[str],
    forbidden_fr: list[str],
    exercise_en: str,
    exercise_fr: str,
    refs_en: str,
    refs_fr: str,
) -> dict[str, str]:
    def body(lang: str) -> str:
        if lang == "en":
            title, outcomes, mat, ctx, why, val, data = (
                title_en,
                outcomes_en,
                maturity_en,
                context_en,
                why_en,
                value_en,
                data_en,
            )
            event, allowed, forbidden, exercise, refs = (
                event_en,
                allowed_en,
                forbidden_en,
                exercise_en,
                refs_en,
            )
            lo = "Learning outcomes"
            sch = "Design card (uniform schema)"
            ap = "Allowed phrases (examples)"
            fp = "Forbidden phrases (v1.0)"
            pe = "Event"
            mp = "Lab preset"
            pd = "Primary demos"
            mm = "Maturity"
            ex = "Guided exercise"
            rf = "References"
            sc = "Scientific context"
            wc = "Why the classical panel is not enough"
            vd = "Value of τ_s + RECD"
            de = "Example data on the platform"
        else:
            title, outcomes, mat, ctx, why, val, data = (
                title_fr,
                outcomes_fr,
                maturity_fr,
                context_fr,
                why_fr,
                value_fr,
                data_fr,
            )
            event, allowed, forbidden, exercise, refs = (
                event_fr,
                allowed_fr,
                forbidden_fr,
                exercise_fr,
                refs_fr,
            )
            lo = "Objectifs d’apprentissage"
            sch = "Fiche de conception (schéma uniforme)"
            ap = "Phrases autorisées (exemples)"
            fp = "Phrases interdites (v1.0)"
            pe = "Événement"
            mp = "Preset Lab"
            pd = "Démos principales"
            mm = "Maturité"
            ex = "Exercice guidé"
            rf = "Références"
            sc = "Contexte scientifique"
            wc = "Pourquoi le panneau classique ne suffit pas"
            vd = "Valeur de τ_s + RECD"
            de = "Données d’exemple sur la plateforme"

        out_lines = "\n".join(f"{i}. {o}" for i, o in enumerate(outcomes, 1))
        all_lines = "\n".join(f"- {a}" for a in allowed)
        forb_lines = "\n".join(f"- {a}" for a in forbidden)
        return f"""# {title}

### {lo}
{out_lines}

**{mm}:** {mat}

---

## 1. {sc}

{ctx}

---

## 2. {wc}

{why}

---

## 3. {vd}

{val}

---

## 4. {de}

{data}

---

## 5. {sch}

| Field | Value |
|-------|--------|
| **Proxy** | {proxy} |
| **{pe}** | {event} |
| **{mp}** | {preset} |
| **{pd}** | {demos} |
| **{mm}** | {maturity_tag} |

### {ap}
{all_lines}

### {fp}
{forb_lines}

---

## 6. {ex}

{exercise}

---

## 7. {rf}

{refs}
"""

    return {"en": body("en"), "fr": body("fr")}


# Non-cardio domains via template
DOMAINS["epidemiologia.md"] = _pack(
    title_en="Domain: Epidemiology — dengue and hyper-persistence",
    title_fr="Domaine : Épidémiologie — dengue et hyper-persistance",
    outcomes_en=[
        "Transfer the τ_s + RECD grammar from cardio to a socio-ecological system.",
        "Explain why var/AR1 confuse seasonality with outbreak proximity.",
        "State a falsifiable hypothesis about ordinal cases–climate coherence.",
    ],
    outcomes_fr=[
        "Transférer la grammaire τ_s + RECD du cardio à un système socio-écologique.",
        "Expliquer pourquoi var/AR1 confondent saisonnalité et proximité d’épidémie.",
        "Formuler une hypothèse falsifiable sur la cohérence ordinale cases–climat.",
    ],
    maturity_en="★★★★☆ — mature narrative and preprints; CCTP remains the platform star cohort.",
    maturity_fr="★★★★☆ — récit et preprints matures ; CCTP reste la cohorte phare de la plateforme.",
    context_en=(
        "**Dengue** is a socio-ecological system forced by climate, *Aedes* vector, immunity and mobility. "
        "Weekly incidence shows **outbreaks**, plateaus and sometimes **hyper-persistence**: the system "
        "stays stuck in high-transmission regimes longer than simple noise models predict. "
        "Puerto Rico and DengAI-style series (San Juan / Iquitos) are natural labs for epidemiological early warning."
    ),
    context_fr=(
        "La **dengue** est un système socio-écologique forcé par le climat, le vecteur *Aedes*, l’immunité et la mobilité. "
        "L’incidence hebdomadaire montre des **épidémies**, des plateaux et parfois une **hyper-persistance**. "
        "Porto Rico et les séries type DengAI (San Juan / Iquitos) sont des laboratoires naturels d’alerte précoce."
    ),
    why_en=(
        "- Incidence is **discrete, noisy and seasonal**; var/AR1 confuse seasonality with outbreak proximity.\n"
        "- The “system” is not only `cases(t)`: it is **cases–climate–vector coupling**.\n"
        "- Univariate thresholds alert **late** or with many false positives.\n"
        "- Predictive ML can hit the number while **hiding** the reorganization mechanism."
    ),
    why_fr=(
        "- L’incidence est **discrète, bruyante et saisonnière** ; var/AR1 confondent saisonnalité et brote.\n"
        "- Le « système » n’est pas seulement `cases(t)` : c’est le **couplage** cases–climat–vecteur.\n"
        "- Les seuils univariés alertent **tard** ou avec beaucoup de faux positifs.\n"
        "- Le ML prédictif peut viser le nombre tout en **occultant** le mécanisme de réorganisation."
    ),
    value_en=(
        "| Contribution | Content |\n"
        "|--------------|----------|\n"
        "| Multivariate ordinal | \(X = [z(\\mathrm{cases}), z(\\mathrm{temp}), z(\\mathrm{precip}), \\ldots]\) |\n"
        "| Ordinal hyper-persistence | Φ₂ (sustained relations) and Tau persistence layers |\n"
        "| RECD | Outbreak “clock”: ticks when joint configuration becomes synergistic |\n"
        "| Comparability | Same language as cardiology/ecology → systems science, not epi silo |"
    ),
    value_fr=(
        "| Apport | Contenu |\n"
        "|--------|----------|\n"
        "| Multivarié ordinal | \(X = [z(\\mathrm{cases}), z(\\mathrm{temp}), z(\\mathrm{precip}), \\ldots]\) |\n"
        "| Hyper-persistance ordinale | Φ₂ (relations soutenues) et couches de persistance Tau |\n"
        "| RECD | « Horloge » de l’épidémie : ticks quand la configuration conjointe devient synergique |\n"
        "| Comparabilité | Même langage que cardio/écologie → science des systèmes |"
    ),
    data_en=(
        "- `dengue_like_demo` — synthetic outbreak with designed ordinal switch.\n"
        "- Variables: cases, temperature, precipitation (z-scored).\n"
        "- Pedagogical outbreak windows (high percentile or historical labels)."
    ),
    data_fr=(
        "- `dengue_like_demo` — épidémie synthétique avec bascule ordinale conçue.\n"
        "- Variables : cases, température, précipitation (z-score).\n"
        "- Fenêtres d’épidémie pédagogiques (percentile élevé ou labels historiques)."
    ),
    proxy=r"\(X=[z(\mathrm{cases}), z(\mathrm{temp}), z(\mathrm{precip})]\)",
    event_en="Outbreak onset / high-transmission regime start",
    event_fr="Début d’épidémie / régime de transmission élevée",
    preset="`epidemiology` · domain-default W/stride · m=3 · dual reading required",
    demos="`dengue_like_demo`",
    maturity_tag="High (transfer; not operational surveillance)",
    allowed_en=[
        "Ordinal cases–climate coherence rises before incidence peak under this design…",
        "Methodological transfer from CCTP grammar; not an operational nowcast.",
        "Seasonality-aware nulls / surrogates must be reported.",
    ],
    allowed_fr=[
        "La cohérence ordinale cases–climat monte avant le pic d’incidence sous ce design…",
        "Transfert méthodologique depuis la grammaire CCTP ; pas un nowcast opérationnel.",
        "Les nulls / surrogates tenant compte de la saisonnalité doivent être rapportés.",
    ],
    forbidden_en=[
        "Operational outbreak alarm for public health agencies",
        "Replaces epidemiological surveillance systems",
        "Causal proof of a real city’s outbreak from the demo alone",
    ],
    forbidden_fr=[
        "Alarme opérationnelle d’épidémie pour les agences de santé publique",
        "Remplace les systèmes de surveillance épidémiologique",
        "Preuve causale d’une épidémie urbaine réelle à partir du seul demo",
    ],
    exercise_en=(
        "1. Lab → `dengue_like_demo` → epidemiology preset → Fast.\n"
        "2. Dual table: Δτ_s, excess3, var/AR1, p_surr.\n"
        "3. One paragraph: what is analogous to the cardio “event”, what is **not** claimed."
    ),
    exercise_fr=(
        "1. Lab → `dengue_like_demo` → preset epidemiology → Fast.\n"
        "2. Tableau dual : Δτ_s, excess3, var/AR1, p_surr.\n"
        "3. Un paragraphe : ce qui est analogue à l’« événement » cardio, ce qui **n’est pas** affirmé."
    ),
    refs_en="- Author dengue Tau/RECD preprints (2025–2026).\n- DengAI DrivenData; vector-borne EWS literature.",
    refs_fr="- Preprints dengue Tau/RECD de l’auteur (2025–2026).\n- DengAI DrivenData ; littérature EWS vectorielles.",
)

DOMAINS["neurociencia.md"] = _pack(
    title_en="Domain: Neuroscience — epileptic seizures (CHB-MIT style)",
    title_fr="Domaine : Neurosciences — crises épileptiques (style CHB-MIT)",
    outcomes_en=[
        "Treat multichannel EEG as a relational system with an annotated event.",
        "Contrast channel-wise CSD with ordinal co-ordination (τ_s / RECD).",
        "State non-clinical scope for any pre-ictal interpretation.",
    ],
    outcomes_fr=[
        "Traiter l’EEG multicanal comme un système relationnel avec événement annoté.",
        "Contraster le CSD par canal avec la co-ordination ordinale (τ_s / RECD).",
        "Énoncer le périmètre non clinique de toute interprétation pré-ictale.",
    ],
    maturity_en="★★★☆☆ — Medium–high pipeline readiness; empirical depth consolidating (below CCTP).",
    maturity_fr="★★★☆☆ — Pipeline prêt ; profondeur empirique en consolidation (sous CCTP).",
    context_en=(
        "**Epileptic seizures** are regime transitions in cortical dynamics. Multichannel EEG is the prototype where "
        "many variables (channels/bands) exist, events are annotated, and clinical interest is **pre-ictal**. "
        "CHB-MIT (PhysioNet) provides pediatric records with seizure annotations; the platform uses processed or "
        "synthetic pre-ictal-like extracts (raw CHB-MIT is not fully redistributed)."
    ),
    context_fr=(
        "Les **crises épileptiques** sont des transitions de régime de la dynamique corticale. L’EEG multicanal est le "
        "prototype à nombreuses variables, événements annotés et intérêt **pré-ictal**. CHB-MIT (PhysioNet) fournit "
        "des enregistrements pédiatriques ; la plateforme utilise des extraits traités ou synthétiques pre-ictal-like."
    ),
    why_en=(
        "- A single channel may not show clear CSD.\n"
        "- Artefacts and sleep confuse var/AR1.\n"
        "- The transition is **spatially distributed**: the signature is in **pattern synchronization**, not one channel’s power alone."
    ),
    why_fr=(
        "- Un seul canal peut ne pas montrer de CSD clair.\n"
        "- Artéfacts et sommeil confondent var/AR1.\n"
        "- La transition est **spatialement distribuée** : la signature est dans la **synchronisation de motifs**."
    ),
    value_en=(
        "- Multivariate: bandpowers or envelopes of 4–8 channels/bands.\n"
        "- Φ₁–Φ₃ capture **symbolic co-ordination** pre-ictal.\n"
        "- excess3 as proxy of irreducible network configuration.\n"
        "- Compare with classical sync indices (PLV, etc.) in Full mode when available."
    ),
    value_fr=(
        "- Multivarié : bandpowers ou enveloppes de 4–8 canaux/bandes.\n"
        "- Φ₁–Φ₃ capturent la **co-ordination symbolique** pré-ictale.\n"
        "- excess3 comme proxy de configuration de réseau irréductible.\n"
        "- Comparer avec des indices de sync classiques (PLV, etc.) en mode Full si disponible."
    ),
    data_en="- `eeg_like_demo` — designed coupling transition between channels.\n- Download scripts under PhysioNet ToS when using real extracts.",
    data_fr="- `eeg_like_demo` — transition de couplage conçue entre canaux.\n- Scripts de téléchargement sous ToS PhysioNet pour extraits réels.",
    proxy=r"\(X=[\mathrm{bandpower}_1,\ldots,\mathrm{bandpower}_k]\) or channel envelopes",
    event_en="Seizure onset / pre-ictal marker (annotated or designed)",
    event_fr="Onset de crise / marqueur pré-ictal (annoté ou conçu)",
    preset="`neuroscience` · m=3 · dual reading; extensions optional",
    demos="`eeg_like_demo`",
    maturity_tag="Medium–high (pedagogical + emerging empirical)",
    allowed_en=[
        "Ordinal co-ordination changes toward the designed/annotated event…",
        "Toy ictal grammar for method training; not a seizure predictor.",
    ],
    allowed_fr=[
        "La co-ordination ordinale change vers l’événement conçu/annoté…",
        "Grammaire ictale de jouet pour l’entraînement méthodologique ; pas un prédicteur de crise.",
    ],
    forbidden_en=[
        "Validated seizure prediction device",
        "Clinical decision support for epilepsy monitoring units",
    ],
    forbidden_fr=[
        "Dispositif validé de prédiction de crises",
        "Aide à la décision clinique pour unités d’épilepsie",
    ],
    exercise_en="Lab → `eeg_like_demo` → neuroscience → dual reading paragraph + non-clinical disclaimer.",
    exercise_fr="Lab → `eeg_like_demo` → neuroscience → paragraphe de lecture duale + disclaimer non clinique.",
    refs_en="- CHB-MIT PhysioNet; seizure prediction literature; ordinal Systemic Tau framework.",
    refs_fr="- CHB-MIT PhysioNet ; littérature de prédiction de crises ; cadre Tau ordinal.",
)

DOMAINS["ecologia.md"] = _pack(
    title_en="Domain: Ecosystem ecology — lake eutrophication",
    title_fr="Domaine : Écologie des écosystèmes — eutrophisation des lacs",
    outcomes_en=[
        "Link classical CSD lake literature to multivariate ordinal observables.",
        "Treat nutrients–Chl-a–DO as a relational triad.",
        "Transfer method language between physiology and ecology without overclaim.",
    ],
    outcomes_fr=[
        "Relier la littérature CSD des lacs aux observables ordinaux multivariés.",
        "Traiter nutriments–Chl-a–DO comme une triade relationnelle.",
        "Transférer le langage méthodologique physiologie ↔ écologie sans overclaim.",
    ],
    maturity_en="★★★☆☆ — Strong pedagogy; empirical depth to expand in v1.x.",
    maturity_fr="★★★☆☆ — Pédagogie forte ; profondeur empirique à étendre en v1.x.",
    context_en=(
        "Shallow lakes can jump from a **clear oligotrophic** to a **turbid eutrophic** state (Scheffer et al.). "
        "Series of chlorophyll-a, nutrients and dissolved oxygen capture that transition at monthly/annual scales "
        "(e.g. NTL LTER, Lake Mendota-like demos)."
    ),
    context_fr=(
        "Les lacs peu profonds peuvent basculer d’un état **clair oligotrophe** à un état **turbide eutrophe** "
        "(Scheffer et al.). Les séries de chlorophylle-a, nutriments et oxygène dissous capturent cette transition."
    ),
    why_en=(
        "This domain is the **historical home** of CSD EWS. They work in many models and some lakes. They fail or "
        "are debated when seasonality is strong, human management alters nutrients, or the transition is a "
        "**food-web** change rather than a single indicator."
    ),
    why_fr=(
        "Ce domaine est le **foyer historique** des EWS de CSD. Elles fonctionnent dans beaucoup de modèles et "
        "certains lacs. Elles échouent ou se débattent quand la saisonnalité est forte, la gestion humaine change "
        "les nutriments, ou la transition est un changement de **réseau trophique**."
    ),
    value_en=(
        "- Same relational language as physiology: the lake “coordinates” nutrients–Chl-a–DO.\n"
        "- RECD offers a clock of **ecological reorganization events**.\n"
        "- Enables **methodological transfer** heart ↔ lake (unifying thesis of the platform)."
    ),
    value_fr=(
        "- Même langage relationnel que la physiologie : le lac « coordonne » nutriments–Chl-a–DO.\n"
        "- RECD offre une horloge d’**événements de réorganisation écologique**.\n"
        "- Permet le **transfert méthodologique** cœur ↔ lac."
    ),
    data_en="- `ecology_like_demo` — Mendota-like monthly series (chla, tp, do, temp z-scored).\n- Regime annotation when a historical Chl-a threshold exists.",
    data_fr="- `ecology_like_demo` — séries mensuelles type Mendota (chla, tp, do, temp en z-score).\n- Annotation de régime si seuil historique de Chl-a.",
    proxy=r"\(X=[\mathrm{chla}, \mathrm{tp}, \mathrm{do}, \mathrm{temp}]\) (z-scored)",
    event_en="Clear → turbid regime flip / bloom onset",
    event_fr="Bascule clair → turbide / onset de bloom",
    preset="`ecology` · dual reading vs classical CSD panel",
    demos="`ecology_like_demo`",
    maturity_tag="Medium (strong teaching bridge to CSD literature)",
    allowed_en=[
        "Relational reorganization around a designed or historical regime flip…",
        "Method transfer from CCTP; not an operational lake management alarm.",
    ],
    allowed_fr=[
        "Réorganisation relationnelle autour d’une bascule de régime conçue ou historique…",
        "Transfert de méthode depuis CCTP ; pas une alarme opérationnelle de gestion de lac.",
    ],
    forbidden_en=["Operational eutrophication early-warning product", "Causal proof for a specific real lake from demo alone"],
    forbidden_fr=["Produit opérationnel d’alerte d’eutrophisation", "Preuve causale pour un lac réel à partir du seul demo"],
    exercise_en="Lab → ecology_like_demo → compare dual reading to a univariate Chl-a variance story.",
    exercise_fr="Lab → ecology_like_demo → comparer la lecture duale à une histoire univariée de variance de Chl-a.",
    refs_en="- Scheffer, *Critical Transitions in Nature and Society*.\n- NTL LTER data publications.",
    refs_fr="- Scheffer, *Critical Transitions in Nature and Society*.\n- Publications de données NTL LTER.",
)

DOMAINS["clima.md"] = _pack(
    title_en="Domain: Climate and hydrology — drought and hydro-climatic regimes",
    title_fr="Domaine : Climat et hydrologie — sécheresse et régimes hydro-climatiques",
    outcomes_en=[
        "Connect classical critical-threshold (CSD) literature to multivariate ordinals.",
        "Distinguish a level shift (more heat) from temp–precip–soil relational reorganization.",
        "State a falsifiable drought-latent hypothesis without operational forecast claims.",
    ],
    outcomes_fr=[
        "Relier la littérature des seuils critiques (CSD) aux ordinaux multivariés.",
        "Distinguer un changement de niveau (plus de chaleur) d’une réorganisation temp–précip–sol.",
        "Formuler une hypothèse falsifiable de latent de sécheresse sans claim de forecast opérationnel.",
    ],
    maturity_en="★★★☆☆ — Strong pedagogy and CSD bridge; not a climate forecast product.",
    maturity_fr="★★★☆☆ — Pédagogie forte et pont CSD ; pas un produit de forecast climatique.",
    context_en=(
        "Droughts and hydro-climatic flips are studied with temperature, precipitation and soil moisture. "
        "Classical early warning asks: is the system approaching an irreversible dry regime? "
        "The τ_s question is complementary: **how do relations reorder** among those variables under a shared drought latent?"
    ),
    context_fr=(
        "Sécheresses et bascules hydro-climatiques s’étudient avec température, précipitation et humidité du sol. "
        "L’alerte classique demande : le système approche-t-il un régime sec irréversible ? "
        "La question τ_s est complémentaire : **comment se réordonnent les relations** sous un latent de sécheresse partagé ?"
    ),
    why_en=(
        "- Seasonality confounds var/AR1.\n"
        "- A single drought index collapses multivariate structure.\n"
        "- The “event” is often a **regime**, not a point instant."
    ),
    why_fr=(
        "- La saisonnalité confond var/AR1.\n"
        "- Un seul indice de sécheresse effondre la structure multivariée.\n"
        "- L’« événement » est souvent un **régime**, pas un instant ponctuel."
    ),
    value_en=(
        "| Contribution | Content |\n|--------------|----------|\n"
        "| Climate triad | \(X = [\\mathrm{temp}, \\mathrm{precip}, \\mathrm{soil}]\) |\n"
        "| Reorganization | Drought latent couples channels that were nearly seasonal/independent |\n"
        "| Comparability | Same language as lakes (ecology) and outbreaks (epidemiology) |"
    ),
    value_fr=(
        "| Apport | Contenu |\n|--------|----------|\n"
        "| Triade climatique | \(X = [\\mathrm{temp}, \\mathrm{precip}, \\mathrm{soil}]\) |\n"
        "| Réorganisation | Le latent de sécheresse couple des canaux auparavant quasi saisonniers |\n"
        "| Comparabilité | Même langage que lacs (écologie) et épidémies |"
    ),
    data_en="- `climate_drought_demo`: synthetic with marked dry-regime start.\n- Designed ground truth shared latent post-event (not real satellite data in v1.0).",
    data_fr="- `climate_drought_demo` : synthétique avec début de régime sec marqué.\n- Vérité terrain conçue (latent partagé post-événement ; pas de données satellitaires réelles en v1.0).",
    proxy=r"\(X=[\mathrm{temp}, \mathrm{precip}, \mathrm{soil}]\)",
    event_en="Onset of dry regime / drought latent activation",
    event_fr="Début du régime sec / activation du latent de sécheresse",
    preset="`climate` · dual reading mandatory",
    demos="`climate_drought_demo`",
    maturity_tag="Medium — teaching emphasis",
    allowed_en=[
        "Relational reorganization under designed drought latent…",
        "Pedagogical transfer; not official drought alerts.",
    ],
    allowed_fr=[
        "Réorganisation relationnelle sous latent de sécheresse conçu…",
        "Transfert pédagogique ; pas d’alertes officielles de sécheresse.",
    ],
    forbidden_en=["Official drought forecast / agency alert system", "Guaranteed prediction of irreversible aridification"],
    forbidden_fr=["Forecast officiel de sécheresse / système d’alerte d’agence", "Prédiction garantie d’aridification irréversible"],
    exercise_en="Lab → climate_drought_demo → dual paragraph + maturity sentence.",
    exercise_fr="Lab → climate_drought_demo → paragraphe dual + phrase de maturité.",
    refs_en="- Scheffer et al., critical transitions / CSD.\n- Drought indices (SPI, SPEI) as univariate contrast.",
    refs_fr="- Scheffer et al., transitions critiques / CSD.\n- Indices de sécheresse (SPI, SPEI) comme contraste univarié.",
)

DOMAINS["educacion.md"] = _pack(
    title_en="Domain: Collective learning — cohort / classroom as a system",
    title_fr="Domaine : Apprentissage collectif — cohorte / classe comme système",
    outcomes_en=[
        "Treat the classroom or cohort as a relational system (engagement · peers · load).",
        "Internalize τ_s with a domain close to teaching practice.",
        "Design a falsifiable question: “was there ordinal reorganization mid-course?”",
    ],
    outcomes_fr=[
        "Traiter la classe ou la cohorte comme un système relationnel (engagement · pairs · charge).",
        "Interioriser τ_s avec un domaine proche de la pratique enseignante.",
        "Concevoir une question falsifiable : « y a-t-il eu réorganisation ordinale à mi-parcours ? »",
    ],
    maturity_en="★★★☆☆ — Meta-pedagogical synthetic demo; not production LMS analytics.",
    maturity_fr="★★★☆☆ — Démo synthétique méta-pédagogique ; pas d’analytics LMS de production.",
    context_en=(
        "STP is **pedagogical** software before it is commercial. A natural example domain is the learning process "
        "itself: engagement, peer synchrony and cognitive load. The method is taught *from inside* educational "
        "practice, not only via finance-like demos."
    ),
    context_fr=(
        "STP est un logiciel **pédagogique** avant d’être commercial. Un domaine d’exemple naturel est le processus "
        "d’apprentissage lui-même : engagement, synchronie entre pairs et charge cognitive."
    ),
    why_en=(
        "- τ_s does **not** “measure learning”: it measures **relational reorganization** of chosen proxies.\n"
        "- Pre-event: relatively loose week-to-week channels.\n"
        "- Post-event: a shared latent couples engagement and peer_sync when load changes regime."
    ),
    why_fr=(
        "- τ_s ne « mesure » **pas** l’apprentissage : il mesure la **réorganisation relationnelle** des proxies choisis.\n"
        "- Pré-événement : canaux relativement lâches.\n"
        "- Post-événement : un latent partagé couple engagement et peer_sync quand la charge change de régime."
    ),
    value_en=(
        "| Contribution | Content |\n|--------------|----------|\n"
        "| Multivariate | \(X = [\\mathrm{engagement}, \\mathrm{peer\\_sync}, \\mathrm{load}]\) |\n"
        "| Course event | Mid-semester, method change, major assessment |\n"
        "| Method teaching | Students analyse a familiar system |"
    ),
    value_fr=(
        "| Apport | Contenu |\n|--------|----------|\n"
        "| Multivarié | \(X = [\\mathrm{engagement}, \\mathrm{peer\\_sync}, \\mathrm{load}]\) |\n"
        "| Événement de cours | Mi-semestre, changement de méthode, évaluation majeure |\n"
        "| Enseignement de la méthode | Les étudiants analysent un système familier |"
    ),
    data_en="- `education_cohort_demo` — synthetic with event near ~55% of the series.",
    data_fr="- `education_cohort_demo` — synthétique avec événement vers ~55 % de la série.",
    proxy=r"\(X=[\mathrm{engagement}, \mathrm{peer\_sync}, \mathrm{load}]\)",
    event_en="Mid-course regime change / assessment shock",
    event_fr="Changement de régime à mi-parcours / choc d’évaluation",
    preset="`education` · Fast mode for classroom demos",
    demos="`education_cohort_demo`",
    maturity_tag="Medium — sandbox for pipeline literacy",
    allowed_en=[
        "Ordinal reorganization of engagement–peer–load under designed mid-course event…",
        "Does not replace formative assessment or LMS privacy controls.",
    ],
    allowed_fr=[
        "Réorganisation ordinale engagement–pairs–charge sous événement de mi-parcours conçu…",
        "Ne remplace pas l’évaluation formative ni les contrôles de confidentialité LMS.",
    ],
    forbidden_en=["Automated student grading from τ_s", "Surveillance of learners without ethics review"],
    forbidden_fr=["Notation automatisée d’étudiants à partir de τ_s", "Surveillance des apprenants sans revue éthique"],
    exercise_en="Lab → education_cohort_demo → dual reading + ethics half-paragraph.",
    exercise_fr="Lab → education_cohort_demo → lecture duale + demi-paragraphe d’éthique.",
    refs_en="- Learning analytics critical literature; STP syllabus meta-domain notes.",
    refs_fr="- Littérature critique des learning analytics ; notes méta-domaine du syllabus STP.",
)

DOMAINS["social.md"] = _pack(
    title_en="Domain: Social dynamics — polarization (toy model)",
    title_fr="Domaine : Dynamique sociale — polarisation (modèle jouet)",
    outcomes_en=[
        "See a polarization cascade as ordinal reorganization of opinions + interaction.",
        "Separate pedagogical method use from any social/political prediction claim.",
        "Contrast with AR control: without shared latent, |Δτ_s| is usually small.",
    ],
    outcomes_fr=[
        "Voir une cascade de polarisation comme réorganisation ordinale opinions + interaction.",
        "Séparer l’usage pédagogique de tout claim de prédiction sociale/politique.",
        "Contraster avec le contrôle AR : sans latent partagé, |Δτ_s| est souvent petit.",
    ],
    maturity_en="★★☆☆☆ — Conceptual demo. No validated social cohort on the platform.",
    maturity_fr="★★☆☆☆ — Démo conceptuelle. Pas de cohorte sociale validée sur la plateforme.",
    context_en=(
        "In simple opinion models, two poles and interaction intensity can pass from a “noisy pluralist” regime "
        "to an **anti-correlated** high-interaction regime. That is a change of **relational structure**, not only "
        "of the mean of a polarization indicator."
    ),
    context_fr=(
        "Dans des modèles simples d’opinion, deux pôles et une intensité d’interaction peuvent passer d’un régime "
        "« pluraliste bruyant » à un régime **anti-corrélé** à forte interaction. C’est un changement de "
        "**structure relationnelle**."
    ),
    why_en=(
        "- No real social-network data in v1.0.\n"
        "- No claim to predict elections, conflict or virality.\n"
        "- Demo exists to **teach the grammar** of τ_s / RECD in collective systems."
    ),
    why_fr=(
        "- Pas de données réelles de réseaux sociaux en v1.0.\n"
        "- Aucune prétention à prédire élections, conflits ou viralité.\n"
        "- La démo existe pour **enseigner la grammaire** τ_s / RECD dans les systèmes collectifs."
    ),
    value_en=(
        "- Variables: `opinion_a`, `opinion_b`, `interaction`.\n"
        "- Post-event: polarization latent forces A ≈ −B and inflates interaction.\n"
        "- Dual reading asks whether Δ is residual vs cross-independence surrogates."
    ),
    value_fr=(
        "- Variables : `opinion_a`, `opinion_b`, `interaction`.\n"
        "- Post-événement : un latent de polarisation force A ≈ −B et gonfle l’interaction.\n"
        "- La lecture duale demande si le Δ est résiduel face aux surrogates d’indépendance croisée."
    ),
    data_en="- `social_polarization_demo` (generated on platform, marked event).",
    data_fr="- `social_polarization_demo` (généré sur la plateforme, événement marqué).",
    proxy=r"\(X=[\mathrm{opinion\_a}, \mathrm{opinion\_b}, \mathrm{interaction}]\)",
    event_en="Polarization cascade onset (designed)",
    event_fr="Début de cascade de polarisation (conçu)",
    preset="`social` · pedagogical only",
    demos="`social_polarization_demo`",
    maturity_tag="Low–medium (conceptual transfer)",
    allowed_en=[
        "Toy polarization cascade shows ordinal reorganization under designed latent…",
        "Critical computational social science teaching with explicit disclaimer.",
    ],
    allowed_fr=[
        "La cascade jouet montre une réorganisation ordinale sous latent conçu…",
        "Enseignement critique de sciences sociales computationnelles avec disclaimer explicite.",
    ],
    forbidden_en=["Predicts elections / conflict / virality", "Causal proof of real-world polarization"],
    forbidden_fr=["Prédit élections / conflits / viralité", "Preuve causale de polarisation réelle"],
    exercise_en="Compare social_polarization_demo vs synthetic_ar_noise dual readings.",
    exercise_fr="Comparer social_polarization_demo vs synthetic_ar_noise en lecture duale.",
    refs_en="- Opinion dynamics toy models; critical CSS literature.",
    refs_fr="- Modèles jouets de dynamique d’opinion ; littérature critique CSS.",
)

DOMAINS["fisiologia.md"] = _pack(
    title_en="Domain: Sleep physiology — circadian fragmentation",
    title_fr="Domaine : Physiologie du sommeil — fragmentation circadienne",
    outcomes_en=[
        "Extend cardio (RR) intuition to a sleep triad: HRV · activity · temperature.",
        "Observe a driver change (clean circadian → high-frequency fragmentation).",
        "Compare maturity: CCTP is the anchor; sleep is a physiological bridge.",
    ],
    outcomes_fr=[
        "Étendre l’intuition cardio (RR) à une triade sommeil : HRV · activité · température.",
        "Observer un changement de driver (circadien propre → fragmentation haute fréquence).",
        "Comparer la maturité : CCTP est l’ancre ; le sommeil est un pont physiologique.",
    ],
    maturity_en="★★★☆☆ — Synthetic demo aligned with sleep-architecture ideas.",
    maturity_fr="★★★☆☆ — Démo synthétique alignée sur des idées d’architecture du sommeil.",
    context_en=(
        "Sleep architecture coordinates autonomic and behavioural variables. When the circadian driver fragments, "
        "it is not only “more noise”: **ordinal relations** among HRV, activity and temperature reorganize."
    ),
    context_fr=(
        "L’architecture du sommeil coordonne variables autonomiques et comportementales. Quand le driver circadien "
        "se fragmente, ce n’est pas seulement « plus de bruit » : les **relations ordinales** se réorganisent."
    ),
    why_en=(
        "- Cardiology (CCTP/SDDB) supplies the platform’s reference cohort.\n"
        "- Sleep offers a second physiological system to practise the same language without mixing clinical claims."
    ),
    why_fr=(
        "- La cardiologie (CCTP/SDDB) fournit la cohorte de référence de la plateforme.\n"
        "- Le sommeil offre un second système physiologique pour pratiquer le même langage sans claims cliniques."
    ),
    value_en="- Proxy triad with designed fragmentation event (~70%).\n- Dual reading vs univariate sleep “fragmentation index” stories.",
    value_fr="- Triade proxy avec événement de fragmentation conçu (~70 %).\n- Lecture duale vs histoires univariées d’« indice de fragmentation ».",
    data_en="- `sleep_fragmentation_demo` — marked fragmentation event.",
    data_fr="- `sleep_fragmentation_demo` — événement de fragmentation marqué.",
    proxy=r"\(X=[\mathrm{HRV}, \mathrm{activity}, \mathrm{temp}]\)",
    event_en="Circadian fragmentation onset (~70% of series)",
    event_fr="Début de fragmentation circadienne (~70 % de la série)",
    preset="`physiology` · Fast for teaching",
    demos="`sleep_fragmentation_demo`",
    maturity_tag="Medium — pedagogical physiological transfer",
    allowed_en=["Relational reorganization under designed sleep fragmentation…", "Not a medical sleep-scoring device."],
    allowed_fr=["Réorganisation relationnelle sous fragmentation de sommeil conçue…", "Pas un dispositif médical de scoring du sommeil."],
    forbidden_en=["Clinical sleep diagnosis", "Medical device claim"],
    forbidden_fr=["Diagnostic clinique du sommeil", "Claim de dispositif médical"],
    exercise_en="Lab → sleep_fragmentation_demo → dual + maturity contrast with cardiology.",
    exercise_fr="Lab → sleep_fragmentation_demo → dual + contraste de maturité avec la cardiologie.",
    refs_en="- Sleep architecture literature; CCTP as maturity anchor.",
    refs_fr="- Littérature d’architecture du sommeil ; CCTP comme ancre de maturité.",
)

DOMAINS["finanzas.md"] = _pack(
    title_en="Domain: Complex systems / finance — volatility regimes",
    title_fr="Domaine : Systèmes complexes / finance — régimes de volatilité",
    outcomes_en=[
        "Map volatility regime shifts to ordinal coupling questions.",
        "Contrast reactive classical vol metrics with dual reading.",
        "Enforce a hard non-trading ethical boundary.",
    ],
    outcomes_fr=[
        "Relier les bascules de régime de volatilité à des questions de couplage ordinal.",
        "Contraster les métriques de vol classiques réactives avec la lecture duale.",
        "Imposer une frontière éthique stricte non-trading.",
    ],
    maturity_en="★★★☆☆ — Optional advanced transfer domain on the learning path.",
    maturity_fr="★★★☆☆ — Domaine de transfert avancé optionnel sur le parcours.",
    context_en=(
        "Markets exhibit **volatility regime changes**, contagion and asset synchronization. They are not “living "
        "systems” biologically, but they share **coupling transitions** in multivariate series."
    ),
    context_fr=(
        "Les marchés exhibent des **changements de régime de volatilité**, contagion et synchronisation d’actifs. "
        "Ce ne sont pas des systèmes biologiques, mais ils partagent des **transitions de couplage** multivariées."
    ),
    why_en=(
        "- Realized vol, VIX, rolling return correlations are often **reactive**.\n"
        "- Regime ML (HMM, etc.) can predict without offering ordinal Φ₁–Φ₃-style decomposition."
    ),
    why_fr=(
        "- Vol réalisée, VIX, corrélations rolling sont souvent **réactifs**.\n"
        "- Le ML de régime (HMM, etc.) peut prédire sans offrir une décomposition ordinale type Φ₁–Φ₃."
    ),
    value_en=(
        "- Proxy: \(X = [z(r_t), z(\\sigma_t^{\\mathrm{RV}})]\) or multi-asset ranges.\n"
        "- Detect **co-ordering of return/vol patterns** before stress regimes.\n"
        "- Advanced exercise of paradigm transferability."
    ),
    value_fr=(
        "- Proxy : \(X = [z(r_t), z(\\sigma_t^{\\mathrm{RV}})]\) ou multi-actifs de rangs.\n"
        "- Détecter la **co-ordination de motifs rendement/vol** avant des régimes de stress.\n"
        "- Exercice avancé de transferabilité du paradigme."
    ),
    data_en="- `finance_like_demo` — designed vol-regime switch.\n- Optional external: daily index + 21d realized vol (user-supplied).",
    data_fr="- `finance_like_demo` — bascule de régime de vol conçue.\n- Optionnel externe : indice journalier + vol réalisée 21j (fourni par l’utilisateur).",
    proxy=r"\(X=[z(r_t), z(\sigma_t^{\mathrm{RV}})]\)",
    event_en="Volatility regime switch / stress onset (designed or user-defined)",
    event_fr="Bascule de régime de volatilité / onset de stress (conçu ou défini par l’utilisateur)",
    preset="`finance` · methodological transfer only",
    demos="`finance_like_demo`",
    maturity_tag="Medium — optional advanced; **no investment advice**",
    allowed_en=[
        "Methodological transfer of ordinal coupling to a vol-regime demo…",
        "Strictly educational / methodological research use.",
    ],
    allowed_fr=[
        "Transfert méthodologique du couplage ordinal vers une démo de régime de vol…",
        "Usage strictement éducatif / recherche méthodologique.",
    ],
    forbidden_en=["Trading signal / alpha / investment advice", "Certified algo-trading system"],
    forbidden_fr=["Signal de trading / alpha / conseil d’investissement", "Système d’algo-trading certifié"],
    exercise_en="Lab → finance_like_demo → dual reading + explicit non-trading closing sentence.",
    exercise_fr="Lab → finance_like_demo → lecture duale + phrase de clôture non-trading explicite.",
    refs_en="- Volatility regime literature; STP ethics handout § finance disclaimer.",
    refs_fr="- Littérature des régimes de volatilité ; handout d’éthique STP § disclaimer finance.",
)


def write_domains() -> None:
    for fname, packs in DOMAINS.items():
        for lang in ("en", "fr"):
            path = LOCALES / lang / "content" / "dominios" / fname
            path.parent.mkdir(parents=True, exist_ok=True)
            text = packs[lang].strip() + "\n"
            path.write_text(text, encoding="utf-8")
            print(f"wrote {path.relative_to(ROOT)} ({len(text)} bytes)")

    # Append uniform design card to thinner Spanish domains if missing
    schema_markers = ("## 5. Ficha de diseño", "Ficha de diseño (esquema uniforme)", "**Proxy**")
    appendices = {
        "ecologia.md": """
---

## Ficha de diseño (esquema uniforme)

| Campo | Valor |
|-------|--------|
| **Proxy** | \(X=[\mathrm{chla}, \mathrm{tp}, \mathrm{do}, \mathrm{temp}]\) (z-score) |
| **Evento** | Bascule claro→turbio / onset de bloom |
| **Preset Lab** | `ecology` · lectura dual vs panel CSD |
| **Demos** | `ecology_like_demo` |
| **Madurez** | Media (puente docente con literatura CSD) |

### Frases permitidas
- Reorganización relacional en torno a bascula de régimen diseñada o histórica…
- Transferencia metodológica desde CCTP; no alarma operativa de gestión de lago.

### Frases prohibidas (v1.0)
- Producto operativo de alerta de eutrofización
- Prueba causal de un lago real solo con el demo
""",
        "finanzas.md": """
---

## Ficha de diseño (esquema uniforme)

| Campo | Valor |
|-------|--------|
| **Proxy** | \(X=[z(r_t), z(\sigma_t^{\mathrm{RV}})]\) |
| **Evento** | Cambio de régimen de volatilidad / onset de estrés |
| **Preset Lab** | `finance` · solo transferencia metodológica |
| **Demos** | `finance_like_demo` |
| **Madurez** | Media — avanzado opcional; **no consejo de inversión** |

### Frases permitidas
- Transferencia metodológica del acoplamiento ordinal a un demo de régimen de vol…
- Uso estrictamente educativo / de investigación metodológica.

### Frases prohibidas (v1.0)
- Señal de trading / alpha / consejo de inversión
- Sistema de trading algorítmico certificado
""",
        "fisiologia.md": """
---

## Ficha de diseño (esquema uniforme)

| Campo | Valor |
|-------|--------|
| **Proxy** | \(X=[\mathrm{HRV}, \mathrm{actividad}, \mathrm{temp}]\) |
| **Evento** | Onset de fragmentación circadiana (~70 % de la serie) |
| **Preset Lab** | `physiology` · Fast para docencia |
| **Demos** | `sleep_fragmentation_demo` |
| **Madurez** | Media — transferencia fisiológica pedagógica |

### Frases permitidas
- Reorganización relacional bajo fragmentación de sueño diseñada…
- No es dispositivo médico de scoring de sueño.

### Frases prohibidas (v1.0)
- Diagnóstico clínico de sueño
- Claim de dispositivo médico
""",
        "neurociencia.md": """
---

## Ficha de diseño (esquema uniforme)

| Campo | Valor |
|-------|--------|
| **Proxy** | Bandpowers / envelopes multicanal |
| **Evento** | Onset de crisis / marcador pre-ictal (anotado o diseñado) |
| **Preset Lab** | `neuroscience` · m=3 · lectura dual |
| **Demos** | `eeg_like_demo` |
| **Madurez** | Medio-Alto (pedagogía + evidencia en consolidación) |

### Frases permitidas
- Cambio de co-ordinación ordinal hacia el evento diseñado/anotado…
- Gramática ictal de juguete para entrenamiento metodológico; no predictor de crisis.

### Frases prohibidas (v1.0)
- Dispositivo validado de predicción de crisis
- Soporte de decisión clínica en unidad de epilepsia
""",
    }
    for fname, app in appendices.items():
        path = CONTENT / "dominios" / fname
        text = path.read_text(encoding="utf-8")
        if "Ficha de diseño (esquema uniforme)" not in text:
            path.write_text(text.rstrip() + "\n" + app, encoding="utf-8")
            print(f"appended schema to ES {fname}")
        else:
            print(f"ES {fname} already has schema")

    # Also append schema to remaining ES domains if missing key sections
    more = {
        "cardiologia.md": """
---

## Ficha de diseño (esquema uniforme)

| Campo | Valor |
|-------|--------|
| **Proxy** | \(X=[z(\mathrm{RR}), z(\|\Delta\mathrm{RR}\|)]\) |
| **Evento** | Onset de FV (`vfon`) o ventana de approach |
| **Preset Lab** | `cardiology` · W≈101 · stride≈5 · θ₃≈0.08 · m=3 |
| **Demos** | `sddb_rr_38_demo`, `sddb_rr_51_demo`, cardio-like |
| **Madurez** | Muy alta (ancla CCTP) |

### Frases permitidas
- Reorganización relacional significativa vs phase-shuffle en este diseño…
- Panel clásico ambiguo (var↑, AR1↓); el relacional se mueve en el approach…
- No es dispositivo de alarma clínica; aplican límites de N y sample.

### Frases prohibidas (v1.0)
- Predice la FV / alarma en tiempo real validada
- Dispositivo médico certificado / soporte de decisión en UCI
""",
        "epidemiologia.md": """
---

## Ficha de diseño (esquema uniforme)

| Campo | Valor |
|-------|--------|
| **Proxy** | \(X=[z(\mathrm{cases}), z(\mathrm{temp}), z(\mathrm{precip})]\) |
| **Evento** | Onset de brote / régimen de transmisión elevada |
| **Preset Lab** | `epidemiology` · lectura dual obligatoria |
| **Demos** | `dengue_like_demo` |
| **Madurez** | Alta (transferencia; no vigilancia operativa) |

### Frases permitidas
- Coherencia ordinal cases–clima sube antes del pico bajo este diseño…
- Transferencia metodológica desde la gramática CCTP; no nowcast operativo.

### Frases prohibidas (v1.0)
- Alarma operativa de brote para agencias de salud pública
- Sustituto de sistemas de vigilancia epidemiológica
""",
        "clima.md": """
---

## Ficha de diseño (esquema uniforme)

| Campo | Valor |
|-------|--------|
| **Proxy** | \(X=[\mathrm{temp}, \mathrm{precip}, \mathrm{soil}]\) |
| **Evento** | Inicio de régimen seco / activación del latente de sequía |
| **Preset Lab** | `climate` · lectura dual obligatoria |
| **Demos** | `climate_drought_demo` |
| **Madurez** | Media — énfasis docente |

### Frases permitidas
- Reorganización relacional bajo latente de sequía diseñado…
- Transferencia pedagógica; no alertas oficiales de sequía.

### Frases prohibidas (v1.0)
- Forecast oficial de sequía / sistema de alerta de agencia
- Predicción garantizada de aridificación irreversible
""",
        "educacion.md": """
---

## Ficha de diseño (esquema uniforme)

| Campo | Valor |
|-------|--------|
| **Proxy** | \(X=[\mathrm{engagement}, \mathrm{peer\_sync}, \mathrm{load}]\) |
| **Evento** | Cambio de régimen a mitad de curso / shock de evaluación |
| **Preset Lab** | `education` · Fast para demos de aula |
| **Demos** | `education_cohort_demo` |
| **Madurez** | Media — sandbox de alfabetización del pipeline |

### Frases permitidas
- Reorganización ordinal engagement–peers–carga bajo evento de mitad de curso…
- No sustituye evaluación formativa ni privacidad de LMS.

### Frases prohibidas (v1.0)
- Calificación automática de estudiantes con τ_s
- Vigilancia de aprendices sin revisión ética
""",
        "social.md": """
---

## Ficha de diseño (esquema uniforme)

| Campo | Valor |
|-------|--------|
| **Proxy** | \(X=[\mathrm{opinion\_a}, \mathrm{opinion\_b}, \mathrm{interaction}]\) |
| **Evento** | Onset de cascada de polarización (diseñado) |
| **Preset Lab** | `social` · solo pedagógico |
| **Demos** | `social_polarization_demo` |
| **Madurez** | Baja-media (transferencia conceptual) |

### Frases permitidas
- Cascada de juguete muestra reorganización ordinal bajo latente diseñado…
- Docencia crítica de ciencias sociales computacionales con disclaimer explícito.

### Frases prohibidas (v1.0)
- Predice elecciones / conflictos / virality
- Prueba causal de polarización del mundo real
""",
    }
    for fname, app in more.items():
        path = CONTENT / "dominios" / fname
        text = path.read_text(encoding="utf-8")
        if "Ficha de diseño (esquema uniforme)" not in text:
            path.write_text(text.rstrip() + "\n" + app, encoding="utf-8")
            print(f"appended schema to ES {fname}")


# ---------------------------------------------------------------------------
# Extra assessment items (append to each module)
# ---------------------------------------------------------------------------

EXTRA_ITEMS: dict[str, list[dict]] = {
    "m1": [
        {
            "id": "m1_q6",
            "type": "mcq",
            "points": 1,
            "prompt": {
                "es": "En una tabla de resultados de Lab aparece: Δvar = +0.8 (sube), ΔAR1 = −0.3 (baja). La lectura más honesta es:",
                "en": "A Lab results table shows: Δvar = +0.8 (up), ΔAR1 = −0.3 (down). The most honest reading is:",
                "fr": "Un tableau de résultats Lab montre : Δvar = +0,8 (↑), ΔAR1 = −0,3 (↓). La lecture la plus honnête est :",
            },
            "choices": [
                {
                    "id": "a",
                    "text": {
                        "es": "Prueba definitiva de critical slowing down clásico en todos los sentidos",
                        "en": "Definitive proof of classical critical slowing down in every sense",
                        "fr": "Preuve définitive de critical slowing down classique dans tous les sens",
                    },
                },
                {
                    "id": "b",
                    "text": {
                        "es": "Panel clásico ambiguo: un indicador sube y otro baja; no cierra solo la pregunta relacional",
                        "en": "Ambiguous classical panel: one indicator rises, another falls; it does not alone close the relational question",
                        "fr": "Panneau classique ambigu : un indicateur monte, l’autre baisse ; il ne clôt pas seul la question relationnelle",
                    },
                },
                {
                    "id": "c",
                    "text": {
                        "es": "Obliga a declarar predicción clínica",
                        "en": "Forces a clinical prediction claim",
                        "fr": "Oblige à déclarer une prédiction clinique",
                    },
                },
                {
                    "id": "d",
                    "text": {
                        "es": "Demuestra que τ_s es innecesario",
                        "en": "Proves that τ_s is unnecessary",
                        "fr": "Prouve que τ_s est inutile",
                    },
                },
            ],
            "correct": "b",
            "explanation": {
                "es": "Ítem de interpretación de tabla: ambigüedad clásica motiva la lectura dual.",
                "en": "Table-interpretation item: classical ambiguity motivates dual reading.",
                "fr": "Item d’interprétation de tableau : l’ambiguïté classique motive la lecture duale.",
            },
        },
        {
            "id": "m1_q7",
            "type": "mcq",
            "points": 1,
            "prompt": {
                "es": "El software STP se usa legítimamente en posgrado para:",
                "en": "STP software is legitimately used in graduate training to:",
                "fr": "Le logiciel STP s’utilise légitimement en formation de 3e cycle pour :",
            },
            "choices": [
                {
                    "id": "a",
                    "text": {
                        "es": "Enseñar gramática ordinal/relacional, nulos y claims acotados",
                        "en": "Teach ordinal/relational grammar, nulls and bounded claims",
                        "fr": "Enseigner la grammaire ordinale/relationnelle, les nulls et les claims bornés",
                    },
                },
                {
                    "id": "b",
                    "text": {
                        "es": "Sustituir comités de ética institucionales",
                        "en": "Replace institutional ethics boards",
                        "fr": "Remplacer les comités d’éthique institutionnels",
                    },
                },
                {
                    "id": "c",
                    "text": {
                        "es": "Certificar dispositivos médicos",
                        "en": "Certify medical devices",
                        "fr": "Certifier des dispositifs médicaux",
                    },
                },
                {
                    "id": "d",
                    "text": {
                        "es": "Publicar señales de trading sin revisión",
                        "en": "Publish trading signals without review",
                        "fr": "Publier des signaux de trading sans revue",
                    },
                },
            ],
            "correct": "a",
            "explanation": {
                "es": "Uso legítimo = investigación y docencia metodológica.",
                "en": "Legitimate use = methodological research and teaching.",
                "fr": "Usage légitime = recherche et enseignement méthodologiques.",
            },
        },
        {
            "id": "m1_q8",
            "type": "mcq",
            "points": 1,
            "prompt": {
                "es": "Una figura muestra solo la traza univariada de casos de dengue con un umbral. ¿Qué falta para una pregunta STP?",
                "en": "A figure shows only the univariate dengue-cases trace with a threshold. What is missing for an STP question?",
                "fr": "Une figure ne montre que la trace univariée des cas de dengue avec un seuil. Que manque-t-il pour une question STP ?",
            },
            "choices": [
                {
                    "id": "a",
                    "text": {
                        "es": "Nada: el umbral basta para reorganización relacional",
                        "en": "Nothing: the threshold suffices for relational reorganization",
                        "fr": "Rien : le seuil suffit pour la réorganisation relationnelle",
                    },
                },
                {
                    "id": "b",
                    "text": {
                        "es": "Canales multivariados (p.ej. clima), diseño de evento y contraste ordinal/nulos",
                        "en": "Multivariate channels (e.g. climate), event design and ordinal/null contrast",
                        "fr": "Canaux multivariés (p.ex. climat), design d’événement et contraste ordinal/nulls",
                    },
                },
                {
                    "id": "c",
                    "text": {
                        "es": "Solo un color más bonito en la figura",
                        "en": "Only a prettier colour on the figure",
                        "fr": "Seulement une plus jolie couleur sur la figure",
                    },
                },
                {
                    "id": "d",
                    "text": {
                        "es": "Obligatoriamente TDA/Betti",
                        "en": "Mandatory TDA/Betti",
                        "fr": "TDA/Betti obligatoire",
                    },
                },
            ],
            "correct": "b",
            "explanation": {
                "es": "Ítem de interpretación de figura: univariado+umbral ≠ pregunta relacional STP.",
                "en": "Figure-interpretation item: univariate+threshold ≠ STP relational question.",
                "fr": "Item d’interprétation de figure : univarié+seuil ≠ question relationnelle STP.",
            },
        },
        {
            "id": "m1_q9",
            "type": "mcq",
            "points": 1,
            "prompt": {
                "es": "¿Cuál es un prerrequisito razonable del curso de 6 semanas?",
                "en": "Which is a reasonable prerequisite for the 6-week course?",
                "fr": "Quel est un prérequis raisonnable du cours de 6 semaines ?",
            },
            "choices": [
                {
                    "id": "a",
                    "text": {
                        "es": "Series temporales o estadística intermedia y lectura de gráficos científicos",
                        "en": "Time series or intermediate statistics and reading scientific graphics",
                        "fr": "Séries temporelles ou statistique intermédiaire et lecture de graphiques scientifiques",
                    },
                },
                {
                    "id": "b",
                    "text": {
                        "es": "Licencia de médico especialista en arritmias",
                        "en": "Specialist cardiology licence in arrhythmias",
                        "fr": "Licence de médecin spécialiste en arythmies",
                    },
                },
                {
                    "id": "c",
                    "text": {
                        "es": "Certificación de trader profesional",
                        "en": "Professional trader certification",
                        "fr": "Certification de trader professionnel",
                    },
                },
                {
                    "id": "d",
                    "text": {
                        "es": "Dominio de ripser en producción",
                        "en": "Production mastery of ripser",
                        "fr": "Maîtrise de ripser en production",
                    },
                },
            ],
            "correct": "a",
            "explanation": {
                "es": "Syllabus §3: base cuantitativa intermedia, no credencial clínica.",
                "en": "Syllabus §3: intermediate quantitative base, not a clinical credential.",
                "fr": "Syllabus §3 : base quantitative intermédiaire, pas une accréditation clinique.",
            },
        },
    ],
    "m2": [
        {
            "id": "m2_q6",
            "type": "mcq",
            "points": 1,
            "prompt": {
                "es": "Una tabla reporta: m=3, W=101, stride=5, repro_hash=abc…, n_surr=0. ¿Qué falta para un claim de nulo?",
                "en": "A table reports: m=3, W=101, stride=5, repro_hash=abc…, n_surr=0. What is missing for a null claim?",
                "fr": "Un tableau rapporte : m=3, W=101, stride=5, repro_hash=abc…, n_surr=0. Que manque-t-il pour un claim de null ?",
            },
            "choices": [
                {
                    "id": "a",
                    "text": {
                        "es": "Surrogates (n_surr>0) o declaración explícita de que no se contrastó nulo",
                        "en": "Surrogates (n_surr>0) or an explicit statement that no null was tested",
                        "fr": "Surrogates (n_surr>0) ou déclaration explicite qu’aucun null n’a été testé",
                    },
                },
                {
                    "id": "b",
                    "text": {
                        "es": "Nada: el hash basta como p-valor",
                        "en": "Nothing: the hash suffices as a p-value",
                        "fr": "Rien : le hash suffit comme p-valeur",
                    },
                },
                {
                    "id": "c",
                    "text": {
                        "es": "Solo cambiar m a 7",
                        "en": "Only change m to 7",
                        "fr": "Seulement passer m à 7",
                    },
                },
                {
                    "id": "d",
                    "text": {
                        "es": "Borrar el hash",
                        "en": "Delete the hash",
                        "fr": "Effacer le hash",
                    },
                },
            ],
            "correct": "a",
            "explanation": {
                "es": "Hash ≠ nulo. n_surr=0 exige transparencia.",
                "en": "Hash ≠ null. n_surr=0 requires transparency.",
                "fr": "Hash ≠ null. n_surr=0 exige la transparence.",
            },
        },
        {
            "id": "m2_q7",
            "type": "mcq",
            "points": 1,
            "prompt": {
                "es": "El control sintético `synthetic_ar_noise` se usa principalmente para:",
                "en": "The synthetic control `synthetic_ar_noise` is mainly used to:",
                "fr": "Le contrôle synthétique `synthetic_ar_noise` sert surtout à :",
            },
            "choices": [
                {
                    "id": "a",
                    "text": {
                        "es": "Simular un switch de acoplamiento fuerte",
                        "en": "Simulate a strong coupling switch",
                        "fr": "Simuler un fort basculement de couplage",
                    },
                },
                {
                    "id": "b",
                    "text": {
                        "es": "Casi-nulo: esperar |Δτ_s| pequeño si no hay transición diseñada",
                        "en": "Near-null: expect small |Δτ_s| when no transition is designed",
                        "fr": "Quasi-null : attendre un |Δτ_s| petit s’il n’y a pas de transition conçue",
                    },
                },
                {
                    "id": "c",
                    "text": {
                        "es": "Validar un dispositivo de FV",
                        "en": "Validate a VF device",
                        "fr": "Valider un dispositif de FV",
                    },
                },
                {
                    "id": "d",
                    "text": {
                        "es": "Entrenar un modelo de trading",
                        "en": "Train a trading model",
                        "fr": "Entraîner un modèle de trading",
                    },
                },
            ],
            "correct": "b",
            "explanation": {
                "es": "Control casi-nulo del syllabus semana 2.",
                "en": "Near-null control from syllabus week 2.",
                "fr": "Contrôle quasi-null du syllabus semaine 2.",
            },
        },
        {
            "id": "m2_q8",
            "type": "mcq",
            "points": 1,
            "prompt": {
                "es": "Si dos transformaciones monótonas distintas se aplican a la misma serie, los símbolos Bandt–Pompe:",
                "en": "If two different monotone transforms are applied to the same series, Bandt–Pompe symbols:",
                "fr": "Si deux transformées monotones distinctes sont appliquées à la même série, les motifs Bandt–Pompe :",
            },
            "choices": [
                {
                    "id": "a",
                    "text": {
                        "es": "Suelen permanecer iguales (invarianza ordinal monótona)",
                        "en": "Typically stay the same (monotone ordinal invariance)",
                        "fr": "Restent en général les mêmes (invariance ordinale monotone)",
                    },
                },
                {
                    "id": "b",
                    "text": {
                        "es": "Siempre se invierten al azar",
                        "en": "Always flip at random",
                        "fr": "S’inversent toujours au hasard",
                    },
                },
                {
                    "id": "c",
                    "text": {
                        "es": "Requieren unidades SI obligatorias",
                        "en": "Require mandatory SI units",
                        "fr": "Exigent des unités SI obligatoires",
                    },
                },
                {
                    "id": "d",
                    "text": {
                        "es": "Eliminan la necesidad de ventanas W",
                        "en": "Remove the need for windows W",
                        "fr": "Suppriment le besoin de fenêtres W",
                    },
                },
            ],
            "correct": "a",
            "explanation": {
                "es": "Propiedad pedagógica central de Bandt–Pompe.",
                "en": "Central pedagogical property of Bandt–Pompe.",
                "fr": "Propriété pédagogique centrale de Bandt–Pompe.",
            },
        },
        {
            "id": "m2_q9",
            "type": "mcq",
            "points": 1,
            "prompt": {
                "es": "Una figura de τ_s(t) sin evento marcado ni panel clásico. ¿Qué debilidad de informe es la principal?",
                "en": "A figure of τ_s(t) with no marked event and no classical panel. What is the main report weakness?",
                "fr": "Une figure de τ_s(t) sans événement marqué ni panneau classique. Quelle est la principale faiblesse du rapport ?",
            },
            "choices": [
                {
                    "id": "a",
                    "text": {
                        "es": "Falta diseño (evento/corte) y lectura dual para situar el Δ",
                        "en": "Missing design (event/cut) and dual reading to situate Δ",
                        "fr": "Manque le design (événement/coupe) et la lecture duale pour situer Δ",
                    },
                },
                {
                    "id": "b",
                    "text": {
                        "es": "Demasiados surrogates",
                        "en": "Too many surrogates",
                        "fr": "Trop de surrogates",
                    },
                },
                {
                    "id": "c",
                    "text": {
                        "es": "Uso correcto de Methods completo",
                        "en": "Correct use of a full Methods section",
                        "fr": "Usage correct d’une section Methods complète",
                    },
                },
                {
                    "id": "d",
                    "text": {
                        "es": "Exceso de citas de PhysioNet",
                        "en": "Too many PhysioNet citations",
                        "fr": "Trop de citations PhysioNet",
                    },
                },
            ],
            "correct": "a",
            "explanation": {
                "es": "Interpretación de figura incompleta sin diseño ni dual.",
                "en": "Incomplete figure interpretation without design or dual panel.",
                "fr": "Interprétation de figure incomplète sans design ni dual.",
            },
        },
    ],
    "m3": [
        {
            "id": "m3_q6",
            "type": "mcq",
            "points": 1,
            "prompt": {
                "es": "Tabla: Φ₃ binario ≈ 0 en casi todas las ventanas, pero mean_excess3 y Δexcess3 son notables. La lectura preferente es:",
                "en": "Table: binary Φ₃ ≈ 0 in almost all windows, but mean_excess3 and Δexcess3 are notable. Preferred reading:",
                "fr": "Tableau : Φ₃ binaire ≈ 0 presque partout, mais mean_excess3 et Δexcess3 sont notables. Lecture préférée :",
            },
            "choices": [
                {
                    "id": "a",
                    "text": {
                        "es": "Usar excess3 como primario; Φ₃ umbralizado puede apagarse por θ₃",
                        "en": "Treat excess3 as primary; thresholded Φ₃ can switch off due to θ₃",
                        "fr": "Traiter excess3 comme primaire ; Φ₃ seuillé peut s’éteindre à cause de θ₃",
                    },
                },
                {
                    "id": "b",
                    "text": {
                        "es": "Ignorar excess3 y declarar ausencia total de estructura",
                        "en": "Ignore excess3 and declare total absence of structure",
                        "fr": "Ignorer excess3 et déclarer l’absence totale de structure",
                    },
                },
                {
                    "id": "c",
                    "text": {
                        "es": "Concluir predicción clínica automática",
                        "en": "Conclude automatic clinical prediction",
                        "fr": "Conclure une prédiction clinique automatique",
                    },
                },
                {
                    "id": "d",
                    "text": {
                        "es": "Sustituir todo por solo varianza",
                        "en": "Replace everything by variance alone",
                        "fr": "Tout remplacer par la seule variance",
                    },
                },
            ],
            "correct": "a",
            "explanation": {
                "es": "Punto pedagógico del syllabus sem. 3 sobre excess3.",
                "en": "Pedagogical point from syllabus week 3 on excess3.",
                "fr": "Point pédagogique du syllabus sem. 3 sur excess3.",
            },
        },
        {
            "id": "m3_q7",
            "type": "mcq",
            "points": 1,
            "prompt": {
                "es": "Patrón de lectura dual: relacional sí, clásico ambiguo. La frase modelo correcta enfatiza:",
                "en": "Dual-reading pattern: relational yes, classical ambiguous. The correct model sentence emphasizes:",
                "fr": "Motif de lecture duale : relationnel oui, classique ambigu. La phrase modèle correcte insiste sur :",
            },
            "choices": [
                {
                    "id": "a",
                    "text": {
                        "es": "Que el hallazgo principal es la reorganización ordinal bajo nulo, con panel univariado ambiguo",
                        "en": "That the main finding is ordinal reorganization under the null, with an ambiguous univariate panel",
                        "fr": "Que le résultat principal est la réorganisation ordinale sous le null, avec un panneau univarié ambigu",
                    },
                },
                {
                    "id": "b",
                    "text": {
                        "es": "Ocultar el panel clásico porque estorba",
                        "en": "Hiding the classical panel because it is inconvenient",
                        "fr": "Cacher le panneau classique parce qu’il gêne",
                    },
                },
                {
                    "id": "c",
                    "text": {
                        "es": "Declarar valor predictivo externo del 99%",
                        "en": "Declaring 99% external predictive value",
                        "fr": "Déclarer une valeur prédictive externe de 99 %",
                    },
                },
                {
                    "id": "d",
                    "text": {
                        "es": "Que TDA es obligatorio",
                        "en": "That TDA is mandatory",
                        "fr": "Que la TDA est obligatoire",
                    },
                },
            ],
            "correct": "a",
            "explanation": {
                "es": "Plantilla B del handout de lectura dual.",
                "en": "Template B from the dual-reading handout.",
                "fr": "Modèle B du handout de lecture duale.",
            },
        },
        {
            "id": "m3_q8",
            "type": "mcq",
            "points": 1,
            "prompt": {
                "es": "¿Qué NO debe basar el claim principal de un informe de semana 3?",
                "en": "What should NOT ground the main claim of a week-3 report?",
                "fr": "Qu’est-ce qui ne doit PAS fonder le claim principal d’un rapport de semaine 3 ?",
            },
            "choices": [
                {
                    "id": "a",
                    "text": {
                        "es": "Δτ_s, excess3 y lectura dual con nulos documentados",
                        "en": "Δτ_s, excess3 and dual reading with documented nulls",
                        "fr": "Δτ_s, excess3 et lecture duale avec nulls documentés",
                    },
                },
                {
                    "id": "b",
                    "text": {
                        "es": "Solo extensiones TDA/breathing sin el núcleo relacional",
                        "en": "Only TDA/breathing extensions without the relational core",
                        "fr": "Seulement les extensions TDA/breathing sans le noyau relationnel",
                    },
                },
                {
                    "id": "c",
                    "text": {
                        "es": "Parámetros W, m, seed",
                        "en": "Parameters W, m, seed",
                        "fr": "Paramètres W, m, seed",
                    },
                },
                {
                    "id": "d",
                    "text": {
                        "es": "Frase de alcance del dominio",
                        "en": "A domain-scope sentence",
                        "fr": "Une phrase de périmètre de domaine",
                    },
                },
            ],
            "correct": "b",
            "explanation": {
                "es": "Extensiones = contraste, no sustituto del núcleo.",
                "en": "Extensions = contrast, not a substitute for the core.",
                "fr": "Extensions = contraste, pas un substitut du noyau.",
            },
        },
        {
            "id": "m3_q9",
            "type": "mcq",
            "points": 1,
            "prompt": {
                "es": "Figura: var y AR1 suben hacia el evento; τ_s estable; p_surr alto. Patrón dual:",
                "en": "Figure: var and AR1 rise toward the event; τ_s stable; high p_surr. Dual pattern:",
                "fr": "Figure : var et AR1 montent vers l’événement ; τ_s stable ; p_surr élevé. Motif dual :",
            },
            "choices": [
                {
                    "id": "a",
                    "text": {
                        "es": "Clásico sí, relacional no — no reclamar detección relacional",
                        "en": "Classical yes, relational no — do not claim relational detection",
                        "fr": "Classique oui, relationnel non — ne pas réclamer de détection relationnelle",
                    },
                },
                {
                    "id": "b",
                    "text": {
                        "es": "Concordancia fuerte relacional+clásica",
                        "en": "Strong relational+classical concordance",
                        "fr": "Forte concordance relationnelle+classique",
                    },
                },
                {
                    "id": "c",
                    "text": {
                        "es": "Obliga a trading",
                        "en": "Forces a trading claim",
                        "fr": "Oblige un claim de trading",
                    },
                },
                {
                    "id": "d",
                    "text": {
                        "es": "Prueba de causalidad clínica",
                        "en": "Proof of clinical causality",
                        "fr": "Preuve de causalité clinique",
                    },
                },
            ],
            "correct": "a",
            "explanation": {
                "es": "Patrón C del handout de lectura dual.",
                "en": "Pattern C of the dual-reading handout.",
                "fr": "Motif C du handout de lecture duale.",
            },
        },
    ],
    "m4": [
        {
            "id": "m4_q7",
            "type": "mcq",
            "points": 1,
            "prompt": {
                "es": "Tabla CCTP-like: Δτ_s significativo, p_surr bajo, var↑, AR1↓, N=1 sample demo. Conclusión correcta:",
                "en": "CCTP-like table: significant Δτ_s, low p_surr, var↑, AR1↓, N=1 demo sample. Correct conclusion:",
                "fr": "Tableau type CCTP : Δτ_s significatif, p_surr bas, var↑, AR1↓, N=1 sample démo. Conclusion correcte :",
            },
            "choices": [
                {
                    "id": "a",
                    "text": {
                        "es": "Reorganización relacional en este diseño con panel clásico ambiguo; no dispositivo de alarma; límites de sample",
                        "en": "Relational reorganization under this design with ambiguous classical panel; not an alarm device; sample limits",
                        "fr": "Réorganisation relationnelle sous ce design avec panneau classique ambigu ; pas un dispositif d’alarme ; limites d’échantillon",
                    },
                },
                {
                    "id": "b",
                    "text": {
                        "es": "Validación clínica de alarma de FV en tiempo real",
                        "en": "Clinical validation of a real-time VF alarm",
                        "fr": "Validation clinique d’une alarme FV temps réel",
                    },
                },
                {
                    "id": "c",
                    "text": {
                        "es": "Se puede omitir el disclaimer porque p es bajo",
                        "en": "The disclaimer can be omitted because p is low",
                        "fr": "On peut omettre le disclaimer car p est bas",
                    },
                },
                {
                    "id": "d",
                    "text": {
                        "es": "El signo de Δ es irrelevante siempre",
                        "en": "The sign of Δ is always irrelevant",
                        "fr": "Le signe de Δ est toujours sans importance",
                    },
                },
            ],
            "correct": "a",
            "explanation": {
                "es": "Interpretación de tabla cardio con ética de claims.",
                "en": "Cardio table interpretation with claim ethics.",
                "fr": "Interprétation de tableau cardio avec éthique des claims.",
            },
        },
        {
            "id": "m4_q8",
            "type": "mcq",
            "points": 1,
            "prompt": {
                "es": "El sample `sddb_rr_51_demo` (pacing) se usa pedagógicamente para:",
                "en": "The `sddb_rr_51_demo` sample (pacing) is used pedagogically to:",
                "fr": "Le sample `sddb_rr_51_demo` (pacing) sert pédagogiquement à :",
            },
            "choices": [
                {
                    "id": "a",
                    "text": {
                        "es": "Ilustrar dificultad, flags de calidad y límites del preset",
                        "en": "Illustrate difficulty, quality flags and preset limits",
                        "fr": "Illustrer la difficulté, les flags de qualité et les limites du preset",
                    },
                },
                {
                    "id": "b",
                    "text": {
                        "es": "Garantizar el caso más fácil de la cohorte",
                        "en": "Guarantee the easiest case in the cohort",
                        "fr": "Garantir le cas le plus facile de la cohorte",
                    },
                },
                {
                    "id": "c",
                    "text": {
                        "es": "Probar un algoritmo de trading",
                        "en": "Test a trading algorithm",
                        "fr": "Tester un algorithme de trading",
                    },
                },
                {
                    "id": "d",
                    "text": {
                        "es": "Sustituir revisión ética",
                        "en": "Replace ethics review",
                        "fr": "Remplacer la revue éthique",
                    },
                },
            ],
            "correct": "a",
            "explanation": {
                "es": "Sample 51 = dificultad / calidad, no 'éxito garantizado'.",
                "en": "Sample 51 = difficulty / quality, not guaranteed success.",
                "fr": "Sample 51 = difficulté / qualité, pas succès garanti.",
            },
        },
        {
            "id": "m4_q9",
            "type": "mcq",
            "points": 1,
            "prompt": {
                "es": "Preset cardiology típico en la app (orden de magnitud):",
                "en": "Typical cardiology preset in the app (order of magnitude):",
                "fr": "Preset cardiology typique dans l’app (ordre de grandeur) :",
            },
            "choices": [
                {
                    "id": "a",
                    "text": {
                        "es": "W≈101, stride≈5, θ₃≈0.08, m=3",
                        "en": "W≈101, stride≈5, θ₃≈0.08, m=3",
                        "fr": "W≈101, stride≈5, θ₃≈0.08, m=3",
                    },
                },
                {
                    "id": "b",
                    "text": {
                        "es": "W=3, stride=1000, m=15 sin justificación",
                        "en": "W=3, stride=1000, m=15 without justification",
                        "fr": "W=3, stride=1000, m=15 sans justification",
                    },
                },
                {
                    "id": "c",
                    "text": {
                        "es": "Solo TDA sin τ_s",
                        "en": "TDA only without τ_s",
                        "fr": "TDA seule sans τ_s",
                    },
                },
                {
                    "id": "d",
                    "text": {
                        "es": "n_surr obligatorio = 0",
                        "en": "Mandatory n_surr = 0",
                        "fr": "n_surr obligatoire = 0",
                    },
                },
            ],
            "correct": "a",
            "explanation": {
                "es": "Preset documentado CCTP/Lab.",
                "en": "Documented CCTP/Lab preset.",
                "fr": "Preset CCTP/Lab documenté.",
            },
        },
        {
            "id": "m4_q10",
            "type": "mcq",
            "points": 1,
            "prompt": {
                "es": "Peso del informe dual cardio en la estructura sugerida del syllabus:",
                "en": "Weight of the cardio dual report in the suggested syllabus structure:",
                "fr": "Poids du rapport dual cardio dans la structure suggérée du syllabus :",
            },
            "choices": [
                {
                    "id": "a",
                    "text": {
                        "es": "≈ 30 % del portfolio/curso",
                        "en": "≈ 30% of the portfolio/course",
                        "fr": "≈ 30 % du portfolio/cours",
                    },
                },
                {
                    "id": "b",
                    "text": {
                        "es": "0 % — solo TDA cuenta",
                        "en": "0% — only TDA counts",
                        "fr": "0 % — seule la TDA compte",
                    },
                },
                {
                    "id": "c",
                    "text": {
                        "es": "100 % sin formativas",
                        "en": "100% with no formatives",
                        "fr": "100 % sans formatifs",
                    },
                },
                {
                    "id": "d",
                    "text": {
                        "es": "Solo 1 % porque es demo",
                        "en": "Only 1% because it is a demo",
                        "fr": "Seulement 1 % car c’est une démo",
                    },
                },
            ],
            "correct": "a",
            "explanation": {
                "es": "Syllabus §6.1 / weights m4=0.30.",
                "en": "Syllabus §6.1 / weights m4=0.30.",
                "fr": "Syllabus §6.1 / weights m4=0.30.",
            },
        },
    ],
    "m5": [
        {
            "id": "m5_q6",
            "type": "mcq",
            "points": 1,
            "prompt": {
                "es": "Al transferir a `finance_like_demo`, la frase de cierre obligatoria debe incluir:",
                "en": "When transferring to `finance_like_demo`, the required closing sentence must include:",
                "fr": "En transférant vers `finance_like_demo`, la phrase de clôture obligatoire doit inclure :",
            },
            "choices": [
                {
                    "id": "a",
                    "text": {
                        "es": "Que no es consejo de inversión ni señal de trading",
                        "en": "That it is not investment advice or a trading signal",
                        "fr": "Que ce n’est ni un conseil d’investissement ni un signal de trading",
                    },
                },
                {
                    "id": "b",
                    "text": {
                        "es": "Una promesa de alpha",
                        "en": "A promise of alpha",
                        "fr": "Une promesse d’alpha",
                    },
                },
                {
                    "id": "c",
                    "text": {
                        "es": "Que la madurez es igual a CCTP automáticamente",
                        "en": "That maturity equals CCTP automatically",
                        "fr": "Que la maturité égale automatiquement CCTP",
                    },
                },
                {
                    "id": "d",
                    "text": {
                        "es": "Que el hash prueba causalidad de mercado",
                        "en": "That the hash proves market causality",
                        "fr": "Que le hash prouve la causalité de marché",
                    },
                },
            ],
            "correct": "a",
            "explanation": {
                "es": "Ética de dominio finanzas / C7.",
                "en": "Finance domain ethics / C7.",
                "fr": "Éthique du domaine finance / C7.",
            },
        },
        {
            "id": "m5_q7",
            "type": "mcq",
            "points": 1,
            "prompt": {
                "es": "Tabla de transferencia: mismo pipeline, proxy distinto, madurez 'media'. ¿Qué cambia y qué no?",
                "en": "Transfer table: same pipeline, different proxy, 'medium' maturity. What changes and what does not?",
                "fr": "Tableau de transfert : même pipeline, proxy différent, maturité « moyenne ». Que change et que ne change pas ?",
            },
            "choices": [
                {
                    "id": "a",
                    "text": {
                        "es": "Cambia jerga/proxy/madurez de claim; no cambia la ontología del método (τ_s/RECD/dual/nulos)",
                        "en": "Jargon/proxy/claim maturity change; method ontology (τ_s/RECD/dual/nulls) does not",
                        "fr": "Jargon/proxy/maturité de claim changent ; l’ontologie de méthode (τ_s/RECD/dual/nulls) non",
                    },
                },
                {
                    "id": "b",
                    "text": {
                        "es": "Cambia toda la matemática del núcleo cada dominio",
                        "en": "The entire core math changes every domain",
                        "fr": "Toute la mathématique du noyau change à chaque domaine",
                    },
                },
                {
                    "id": "c",
                    "text": {
                        "es": "Nada cambia nunca",
                        "en": "Nothing ever changes",
                        "fr": "Rien ne change jamais",
                    },
                },
                {
                    "id": "d",
                    "text": {
                        "es": "Solo cambia el color del UI",
                        "en": "Only the UI colour changes",
                        "fr": "Seul la couleur de l’UI change",
                    },
                },
            ],
            "correct": "a",
            "explanation": {
                "es": "Competencia C7 de transferencia.",
                "en": "Transfer competency C7.",
                "fr": "Compétence de transfert C7.",
            },
        },
        {
            "id": "m5_q8",
            "type": "mcq",
            "points": 1,
            "prompt": {
                "es": "El demo `social_polarization_demo` en v1.0 debe presentarse como:",
                "en": "The `social_polarization_demo` in v1.0 must be presented as:",
                "fr": "Le `social_polarization_demo` en v1.0 doit être présenté comme :",
            },
            "choices": [
                {
                    "id": "a",
                    "text": {
                        "es": "Modelo de juguete pedagógico sin cohorte social validada",
                        "en": "Pedagogical toy model without a validated social cohort",
                        "fr": "Modèle jouet pédagogique sans cohorte sociale validée",
                    },
                },
                {
                    "id": "b",
                    "text": {
                        "es": "Predictor electoral certificado",
                        "en": "Certified election predictor",
                        "fr": "Prédicteur électoral certifié",
                    },
                },
                {
                    "id": "c",
                    "text": {
                        "es": "Evidencia de madurez igual a CCTP",
                        "en": "Evidence of maturity equal to CCTP",
                        "fr": "Preuve d’une maturité égale à CCTP",
                    },
                },
                {
                    "id": "d",
                    "text": {
                        "es": "Sustituto de datos de redes reales sin ética",
                        "en": "A substitute for real network data without ethics",
                        "fr": "Un substitut de données de réseaux réels sans éthique",
                    },
                },
            ],
            "correct": "a",
            "explanation": {
                "es": "Madurez baja-media explícita del dominio social.",
                "en": "Explicit low–medium maturity of the social domain.",
                "fr": "Maturité basse–moyenne explicite du domaine social.",
            },
        },
        {
            "id": "m5_q9",
            "type": "mcq",
            "points": 1,
            "prompt": {
                "es": "Peso sugerido del mini-informe de transferencia (sem. 5):",
                "en": "Suggested weight of the transfer mini-report (week 5):",
                "fr": "Poids suggéré du mini-rapport de transfert (sem. 5) :",
            },
            "choices": [
                {
                    "id": "a",
                    "text": {
                        "es": "≈ 25 %",
                        "en": "≈ 25%",
                        "fr": "≈ 25 %",
                    },
                },
                {
                    "id": "b",
                    "text": {
                        "es": "0 %",
                        "en": "0%",
                        "fr": "0 %",
                    },
                },
                {
                    "id": "c",
                    "text": {
                        "es": "90 % sin cardio",
                        "en": "90% with no cardio",
                        "fr": "90 % sans cardio",
                    },
                },
                {
                    "id": "d",
                    "text": {
                        "es": "Solo peer review sin peso",
                        "en": "Peer review only with zero weight",
                        "fr": "Seulement peer review sans poids",
                    },
                },
            ],
            "correct": "a",
            "explanation": {
                "es": "m5 weight 0.25 en assessments/syllabus.",
                "en": "m5 weight 0.25 in assessments/syllabus.",
                "fr": "Poids m5 0.25 dans assessments/syllabus.",
            },
        },
    ],
    "m6": [
        {
            "id": "m6_q7",
            "type": "mcq",
            "points": 1,
            "prompt": {
                "es": "En la rúbrica 0–2 del informe Lab, el umbral de aprobación de la práctica es:",
                "en": "In the 0–2 Lab report rubric, the practice pass threshold is:",
                "fr": "Dans la grille 0–2 du rapport Lab, le seuil de réussite de la pratique est :",
            },
            "choices": [
                {
                    "id": "a",
                    "text": {
                        "es": "≥ 9 / 12",
                        "en": "≥ 9 / 12",
                        "fr": "≥ 9 / 12",
                    },
                },
                {
                    "id": "b",
                    "text": {
                        "es": "≥ 1 / 12",
                        "en": "≥ 1 / 12",
                        "fr": "≥ 1 / 12",
                    },
                },
                {
                    "id": "c",
                    "text": {
                        "es": "12/12 obligatorio en formativas",
                        "en": "Mandatory 12/12 on formatives",
                        "fr": "12/12 obligatoire en formatifs",
                    },
                },
                {
                    "id": "d",
                    "text": {
                        "es": "No hay umbral",
                        "en": "There is no threshold",
                        "fr": "Il n’y a pas de seuil",
                    },
                },
            ],
            "correct": "a",
            "explanation": {
                "es": "Syllabus §6.2 umbral ≥ 9/12.",
                "en": "Syllabus §6.2 threshold ≥ 9/12.",
                "fr": "Syllabus §6.2 seuil ≥ 9/12.",
            },
        },
        {
            "id": "m6_q8",
            "type": "mcq",
            "points": 1,
            "prompt": {
                "es": "Tabla de portfolio: hay hash y params, pero falta panel EWS y frase de no-alcance. Criterios rúbrica más afectados:",
                "en": "Portfolio table: hash and params present, but missing EWS panel and non-scope sentence. Rubric criteria most affected:",
                "fr": "Tableau de portfolio : hash et params présents, mais panneau EWS et phrase de non-portée manquants. Critères les plus touchés :",
            },
            "choices": [
                {
                    "id": "a",
                    "text": {
                        "es": "EWS en paralelo (criterio 4) y conclusión acotada (criterio 5)",
                        "en": "Parallel EWS (criterion 4) and bounded conclusion (criterion 5)",
                        "fr": "EWS en parallèle (critère 4) et conclusion bornée (critère 5)",
                    },
                },
                {
                    "id": "b",
                    "text": {
                        "es": "Solo tipografía",
                        "en": "Typography only",
                        "fr": "Seulement la typographie",
                    },
                },
                {
                    "id": "c",
                    "text": {
                        "es": "Ninguno: el hash lo compensa todo",
                        "en": "None: the hash compensates everything",
                        "fr": "Aucun : le hash compense tout",
                    },
                },
                {
                    "id": "d",
                    "text": {
                        "es": "Solo el color de las figuras",
                        "en": "Only figure colours",
                        "fr": "Seulement les couleurs des figures",
                    },
                },
            ],
            "correct": "a",
            "explanation": {
                "es": "Ítem de interpretación de rúbrica/tabla de entrega.",
                "en": "Rubric/delivery-table interpretation item.",
                "fr": "Item d’interprétation de grille/tableau de rendu.",
            },
        },
        {
            "id": "m6_q9",
            "type": "mcq",
            "points": 1,
            "prompt": {
                "es": "Phase-shuffle vs IAAFT en la semana 6 se usa para:",
                "en": "Phase-shuffle vs IAAFT in week 6 is used to:",
                "fr": "Phase-shuffle vs IAAFT en semaine 6 sert à :",
            },
            "choices": [
                {
                    "id": "a",
                    "text": {
                        "es": "Refinar nulos y documentar qué hipótesis de independencia/espectro se prueba",
                        "en": "Refine nulls and document which independence/spectrum hypothesis is tested",
                        "fr": "Raffiner les nulls et documenter quelle hypothèse d’indépendance/spectre est testée",
                    },
                },
                {
                    "id": "b",
                    "text": {
                        "es": "Reemplazar por completo τ_s",
                        "en": "Fully replace τ_s",
                        "fr": "Remplacer entièrement τ_s",
                    },
                },
                {
                    "id": "c",
                    "text": {
                        "es": "Obtener certificación FDA automática",
                        "en": "Obtain automatic FDA certification",
                        "fr": "Obtenir une certification FDA automatique",
                    },
                },
                {
                    "id": "d",
                    "text": {
                        "es": "Evitar exportar Methods",
                        "en": "Avoid exporting Methods",
                        "fr": "Éviter d’exporter Methods",
                    },
                },
            ],
            "correct": "a",
            "explanation": {
                "es": "Objetivo de semana 6: nulos refinados.",
                "en": "Week-6 goal: refined nulls.",
                "fr": "Objectif semaine 6 : nulls raffinés.",
            },
        },
        {
            "id": "m6_q10",
            "type": "mcq",
            "points": 1,
            "prompt": {
                "es": "Un portfolio excelente (≥11/12) además debería incluir cuando el docente lo active:",
                "en": "An excellent portfolio (≥11/12) should additionally include when the instructor enables it:",
                "fr": "Un portfolio excellent (≥11/12) devrait en plus inclure lorsque l’enseignant l’active :",
            },
            "choices": [
                {
                    "id": "a",
                    "text": {
                        "es": "Peer review útil según rúbrica",
                        "en": "Useful peer review per the rubric",
                        "fr": "Un peer review utile selon la grille",
                    },
                },
                {
                    "id": "b",
                    "text": {
                        "es": "Overclaim clínico deliberado",
                        "en": "Deliberate clinical overclaim",
                        "fr": "Overclaim clinique délibéré",
                    },
                },
                {
                    "id": "c",
                    "text": {
                        "es": "Omisión del hash",
                        "en": "Omitting the hash",
                        "fr": "Omission du hash",
                    },
                },
                {
                    "id": "d",
                    "text": {
                        "es": "Solo screenshots sin números",
                        "en": "Screenshots only with no numbers",
                        "fr": "Seulement des captures sans nombres",
                    },
                },
            ],
            "correct": "a",
            "explanation": {
                "es": "Syllabus: excelente ≥11/12 y peer review útil si aplica.",
                "en": "Syllabus: excellent ≥11/12 and useful peer review if applicable.",
                "fr": "Syllabus : excellent ≥11/12 et peer review utile si applicable.",
            },
        },
    ],
}


def expand_assessments() -> None:
    path = CONTENT / "learning" / "assessments.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    for mod in data["modules"]:
        mid = mod["id"]
        extras = EXTRA_ITEMS.get(mid, [])
        existing_ids = {q["id"] for q in mod["questions"]}
        for q in extras:
            if q["id"] not in existing_ids:
                mod["questions"].append(q)
                existing_ids.add(q["id"])
        print(f"{mid}: {len(mod['questions'])} questions")
    data["version"] = "1.1"
    text = yaml.dump(
        data,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
        width=100,
    )
    # Prefer block style for readability — dump is fine for tests
    path.write_text(text, encoding="utf-8")
    for lang in ("en", "fr"):
        dest = LOCALES / lang / "content" / "learning" / "assessments.yaml"
        dest.write_text(text, encoding="utf-8")
        print(f"synced {dest.relative_to(ROOT)}")


def main() -> None:
    write_domains()
    expand_assessments()
    print("done")


if __name__ == "__main__":
    main()
