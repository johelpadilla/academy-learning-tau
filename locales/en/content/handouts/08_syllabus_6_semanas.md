# Syllabus — Ordinal complex-systems analysis with Systemic Tau / RECD

| Field | Value |
|-------|--------|
| **Platform** | Academy Learning Tau · Systemic Tau Platform (STP) v1.0 |
| **Format** | Intensive short course · **6 weeks** |
| **Level** | Graduate (MSc / PhD) or professional specialization with quantitative background |
| **Modality** | Hybrid or in-person + computational lab (Streamlit app + optional CLI) |
| **Workload** | **4–5 h/week** (≈ 2 h reading/theory + 2–3 h Lab/write-up) · **24–30 h** total |
| **App languages** | Spanish (source), English, French |
| **Syllabus version** | 1.1 · 2026 |
| **Document** | Handout `08_syllabus_6_semanas` · academic use with citation |

---

## 1. Course description

This course trains students to **pose, run, and document** an analysis of **relational reorganization** in multivariate time series using:

1. **Systemic Tau (τ_s)** — ordinal coupling thermometer across channels;  
2. **Nested ordinal RECD (Φ₁–Φ₃ + excess3)** — grammar of coincidence, persistence, and irreducible synergy;  
3. **Dual reading** — systematic contrast with **classical EWS** (variance, AR(1));  
4. **Surrogate nulls** (phase-shuffle / IAAFT) and **reproducibility** (SHA-256 hash, Methods, MD/JSON export).

The **empirical reference anchor** is the **CCTP** protocol (computational cardiology / pre-VF, pilot cohort and SDDB demos). Other applications (epidemiology, neuroscience, ecology, climate, education, sleep physiology, finance, social dynamics) are treated as **methodological transfer** with explicit empirical maturity — not as predictive product claims.

**This is not** a course on a medical device, operational outbreak alerting, trading, or social scoring.

---

## 2. Exit competencies

On successful completion, the student will be able to:

| # | Competency (observable) |
|---|-------------------------|
| C1 | **Define** a relational question (“does coupling between X and Y reorganize around an event?”) as distinct from a purely univariate one (“does variance rise?”). |
| C2 | **Select** variables, event (if any), domain preset, and parameters (W, stride, m, θ₃, n_surr) with justification. |
| C3 | **Compute** sliding-window τ_s and the RECD panel (Φ₁–Φ₃, excess3, T_recd) in the Lab or via CLI. |
| C4 | **Compare** the relational panel with var/AR1 (dual reading) and interpret concordance, mixed results, or quiet regimes. |
| C5 | **Null-test** the Δτ_s contrast with surrogates and report p_surr without reducing the report to a single p-value. |
| C6 | **Document** reproducible Methods (parameters, seed, hash, domain limits) and scope claims to empirical maturity. |
| C7 | **Transfer** the same grammar to a second domain, stating what changes (proxy, W, jargon) and what does not (method ontology). |

**Integrative competency (final deliverable):** a *portfolio* with dual-reading report + MD/JSON export + Methods + signed checklist, graded with the §7 rubric.

---

## 3. Prerequisites

**Required**

- Intermediate time series or statistics (mean, variance, correlation; basic stochastic process ideas).  
- Reading scientific plots and metric tables.  
- Basic browser use and a local or hosted app environment.

**Recommended (not blocking)**

- Basic Python or Jupyter familiarity (CLI/notebooks track).  
- Notions of complex systems or EWS / critical slowing down.  
- Cardio track: minimal ECG/RR vocabulary (clinical training not required).

**Software**

- Academy Learning Tau (Streamlit) with demo catalog.  
- Optional: CLI `stp analyze` / `stp serve` (same core).  
- Export: Markdown, JSON; PDF via Pandoc if the LMS requires it.

---

## 4. Course map ↔ app modules

| Week | STP modules | Priority handouts |
|------|-------------|-------------------|
| 1 | Foundations (EWS, CSD) · Lab (EWS / synthetic only) | Ethics · Quick guide · Foundations 02/05 |
| 2 | Mathematics · Lab (τ_s, hash) | Practical math · τ_s theory |
| 3 | Foundations RECD/excess3 · Lab | Dual reading · Lab cheatsheet |
| 4 | Domains (cardio) · Evidence · Lab Full | Cardiology domain · Checklist |
| 5 | Domains (transfer) · Lab | Chosen domain sheet · FAQ |
| 6 | Lab export · Materials · Teaching | Ethics (review) · Student pack |

---

## 5. Detailed weekly program

Orientative load per week: **reading 90–120 min · Lab 90–120 min · writing 30–60 min**.

### Week 1 — Classical EWS, CSD, and limits of the univariate panel

| Element | Content |
|---------|---------|
| **Objectives** | Explain var and AR(1) as EWS; state at least two conceptual failure modes (sign ambiguity, univariate vs relational); cite software ethical scope. |
| **Theory** | Foundations · EWS and CSD tabs; *Ethics and scope* handout. |
| **Lab** | Dataset `synthetic_coupled_logistic` or `synthetic_ar_noise`. Observe var/AR1; full dual reading not yet required. |
| **Formative deliverable** | Short essay (≈ 1 page): *“When does a variance increase fail to answer the system question?”* |
| **Success criterion** | Distinguishes classical EWS from relational reorganization; no clinical prediction claims. |

### Week 2 — Bandt–Pompe ordinal patterns and Systemic Tau (τ_s)

| Element | Content |
|---------|---------|
| **Objectives** | Define Bandt–Pompe symbols (m=3); interpret τ_s as windowed ordinal coupling; record **repro_hash**. |
| **Theory** | Foundations · τ_s; Mathematics (m=3 sandbox); amplitude vs reorganization illustrations. |
| **Lab** | `synthetic_coupled_logistic` · preset `synthetic` · Fast mode · coherent W/stride · n_surr ≥ 8. Compare with `synthetic_ar_noise` (near-null control). |
| **Formative deliverable** | Screenshot or table: Δτ_s, p_surr (if any), hash; 5 lines of interpretation *without* overclaim. |
| **Success criterion** | Explains why the AR/noise control should not “look like” a coupling switch. |

### Week 3 — Nested RECD, excess3, and dual reading

| Element | Content |
|---------|---------|
| **Objectives** | Describe Φ₁–Φ₃ and the role of **excess3** under noise; apply the dual-reading protocol (concordance / mixed / quiet). |
| **Theory** | Foundations · RECD and excess3; *Dual reading* and *τ_s + RECD theory* handouts. |
| **Lab** | Same synthetic or cardio-like in Fast; RECD panel; dual summary; do **not** base the main claim on TDA/breathing extensions alone. |
| **Formative deliverable** | Mini-report (1–2 pp.): question, parameters, dual reading, one scope sentence. |
| **Success criterion** | Treats excess3 as primary if binary Φ₃ collapses; compares with var/AR1. |

### Week 4 — Empirical anchor: CCTP cardiology / pre-VF

| Element | Content |
|---------|---------|
| **Objectives** | Apply proxy \(X=[z(\mathrm{RR}), z(\|\Delta\mathrm{RR}\|)]\) and preset `cardiology` (e.g. W≈101, stride=5, θ₃≈0.08); write dual reading with **domain voice** and clinical disclaimers. |
| **Theory** | Domains · Cardiology; Evidence (CCTP pilot N=10, limits); jargon RR, VF, Holter, SDDB. |
| **Lab** | Preferred: `cardiac_like_demo`. If samples present: `sddb_rr_38_demo` (strong signal) and optional `sddb_rr_51_demo` (pacing / harder). Event = onset marker when available. |
| **Partial summative (30% of portfolio)** | Dual report 2–3 pages: metrics, p_surr, classical panel, allowed vs forbidden phrasing, hash. |
| **Success criterion** | No “VF alarm” or device claim; CCTP maturity stated explicitly. |

### Week 5 — Domain transfer (one non-cardio domain)

| Element | Content |
|---------|---------|
| **Objectives** | Reuse the τ_s/RECD grammar in **one** transfer domain; contrast empirical maturity and jargon; justify the preset. |
| **Choice (one)** | `dengue_like_demo` (epi) · `eeg_like_demo` (neuro) · `ecology_like_demo` · `climate_drought_demo` · `education_cohort_demo` · `sleep_fragmentation_demo` · `social_polarization_demo` · `finance_like_demo` (**method transfer only**; trading claims **forbidden**). |
| **Theory** | Domain sheet in Domains + domain lens in Foundations (situated examples). |
| **Lab** | Domain preset; Fast or Full by workload; document n_surr. |
| **Partial summative (25% of portfolio)** | Transfer mini-report (1–2 pp.): event analog, proxy used, what is **not** claimed. |
| **Success criterion** | Domain maturity and limits are visible in the conclusion. |

### Week 6 — Surrogates, extensions, ethics, portfolio, peer review

| Element | Content |
|---------|---------|
| **Objectives** | Refine nulls (phase-shuffle vs IAAFT); decide whether extensions (breathing, TDA, memory) add *contrast* without replacing the core; submit full portfolio; peer review with rubric. |
| **Theory** | Ethics (review); *Extensions* handout; FAQ (context-dependent sign, N=1, “does it predict…?”). |
| **Lab** | Re-analysis of week 4 or 5 case; optional Full mode; export **MD + JSON + Methods**; signed analysis checklist. |
| **Final summative (45% of portfolio)** | Portfolio: (1) main report, (2) transfer report or appendix, (3) exports + hash, (4) checklist, (5) ethics reflection (½ p.). |
| **Success criterion** | §7 rubric meets threshold; scoped claims; verifiable reproducibility. |

---

## 6. Assessment

### 6.0 In-platform assessments (auto-graded)

The app includes the **Assessments** page (`pages/9_Evaluaciones.py`):

- **Local student account** (register / sign-in; progress under `data/student_records/`, not a cloud SaaS).  
- **Per-module MCQ quizzes** (weeks 1–6), automatic grading, default pass threshold **70%**, retakes keep the **best** score.  
- **Weighted course grade** using the same weights as §6.1 (formatives 5%+5%+5%, W4 30%, W5 25%, W6 30%).  
- **Deliverable tracking** (essay/report status) and an **activity log**.  
- The **Learning path** checklist syncs to the account when signed in.  
- Account UI and question bank in **ES / EN / FR**.

Quizzes **complement** (do not replace) the 0–2 Lab report rubric (§6.2): instructors set the relative weight of auto quizzes vs qualitative deliverables.

### 6.1 Suggested structure

| Component | Weight | Timing |
|-----------|--------|--------|
| Formative (weeks 1–3) | 15% | Fast feedback; app quizzes W1–W3 + essays |
| Cardio dual report (week 4) | 30% | Summative · quiz W4 + report |
| Transfer mini-report (week 5) | 25% | Summative · quiz W5 + mini-report |
| Final portfolio + peer review (week 6) | 30% | Summative (includes 15% peer if instructor enables it) · quiz W6 |

*Instructors may collapse weeks 4+5+6 into a single portfolio (100%) in very short offerings.*

### 6.2 Lab / report rubric (6 criteria × 0–2 = **12 points**)

| # | Criterion | 0 | 1 | 2 |
|---|-----------|---|---|---|
| 1 | **Scientific question** | Missing or confuses univariate/relational | Clear question, weak event/design | Relational question + justified cut/event |
| 2 | **Parameters & preset** | Defaults unjustified | Correct preset, weak W/m/θ₃ rationale | Preset + W/stride/m/θ₃/n_surr/seed documented |
| 3 | **Core metrics** | Missing Δτ_s or excess3 | Reports Δ without p_surr/context | Δτ_s, mean/Δ excess3, p_surr (or n_surr=0 declared) |
| 4 | **Parallel EWS** | No classical panel | Mentions var/AR1 without integration | Explicit dual reading (confirms / silent / contradicts) |
| 5 | **Scoped conclusion** | Overclaim (clinical, trading, prediction) | Partial conclusion, weak caveats | Claims match domain maturity + non-scope sentence |
| 6 | **Reproducibility** | No hash or params | Hash **or** incomplete Methods | Hash + Methods + peer-usable export |

**Pass threshold for the practical:** ≥ **9 / 12**.  
**Excellent:** ≥ 11 / 12 and useful peer review (if used).

### 6.3 Delivery phrasing (guidance)

| Allowed (examples) | Forbidden in course v1.0 |
|--------------------|--------------------------|
| “Significant relational reorganization vs phase-shuffle under this design…” | “Predicts VF / outbreak / market crash” |
| “Classical panel ambiguous (var↑, AR1↓); relational panel moves in the approach…” | “Validated clinical alarm device” |
| “Pedagogical transfer to dengue-like; not an operational nowcast” | “Trading signal / alpha” |
| “Demo with designed switch ground truth; calibrates dual reading” | “Causal proof of real-world social polarization” |

---

## 7. Catalog datasets (v1.0)

### Controls (weeks 1–2)

| ID | Role |
|----|------|
| `synthetic_coupled_logistic` | **Positive** control (coupling switch) |
| `synthetic_ar_noise` | **Near-null** / noise control |

### Cardio anchor (week 4)

| ID | Role |
|----|------|
| `cardiac_like_demo` | CCTP flow without PhysioNet dependence |
| `sddb_rr_38_demo` | Strong-signal demo sample (if in `data/samples/`) |
| `sddb_rr_51_demo` | Pacing / harder sample |

### Transfer (week 5) — choose **one**

| ID | Domain |
|----|--------|
| `dengue_like_demo` | Epidemiology |
| `eeg_like_demo` | Neuroscience |
| `ecology_like_demo` | Ecology |
| `climate_drought_demo` | Climate / hydrology |
| `education_cohort_demo` | Collective learning |
| `sleep_fragmentation_demo` | Sleep physiology |
| `social_polarization_demo` | Social dynamics (toy) |
| `finance_like_demo` | Finance (**method only**; no trading) |

Third-party data (e.g. PhysioNet/SDDB) remain under their terms of use.

---

## 8. Materials and readings

### Downloadable packs (Materials page)

- **Student pack:** quick guide, theory, math, cheatsheet, dual reading, checklist, FAQ, ethics.  
- **Instructor pack:** syllabus (this document), ethics, manual, theory/lab packs, FAQ, glossary.  
- Individual domain sheets and compiled Foundations in the app.

### Scientific readings (instructor selects 1–2)

- CCTP-domain and classical EWS works cited under **Evidence**.  
- These do not replace Lab practice.

### CLI (optional advanced track)

```bash
stp analyze data.csv --domain cardiology -o report.md --json result.json
stp serve
```

---

## 9. Course policies

### 9.1 Ethics and scope

- *Ethics and core scope* handout is mandatory before public claims or week 4–6 submissions.  
- Software is for **research and teaching**, not a regulated clinical or financial product.  
- **Empirical maturity** is asymmetric: cardio (CCTP) > synthetic transfer demos.

### 9.2 Academic integrity

- Exports and hashes must match the student’s (or declared team’s) runs.  
- Cite STP software and domain references used.  
- Do not present synthetic demos as unlabeled real clinical or surveillance data.

### 9.3 Teamwork

- Optional pairs (weeks 4–6); each member must be able to explain Methods and the hash.  
- Week 6 peer review: blind or semi-blind per LMS.

### 9.4 Calendar variants

| Variant | Adjustment |
|---------|------------|
| **4-week intensive** | Merge 1–2 and 5–6; one report + short transfer. |
| **8-week seminar** | Add paper-discussion week and extension week (TDA/breathing as contrast). |
| **2-day Lab workshop** | Compress weeks 2–4; reduced rubric (criteria 3–6). |

---

## 10. Instructor notes

1. Prefer **pedagogy and falsification** over product promises: celebrate a well-interpreted near-null control.  
2. Explicit time for **synthetic controls** (week 2) before the cardio anchor.  
3. In week 4, if SDDB samples are missing, `cardiac_like_demo` suffices for the competency.  
4. Finance and social: frame as **grammar sandboxes**, never prediction.  
5. Extensions (TDA, breathing, memory): opt-in Full; main claim remains τ_s + excess3 + dual + null.  
6. Use **domain voice** (jargon in interpretation and Foundations) to transfer concepts without changing the math.  
7. Grade **claim scoping** quality above |Δ| magnitude.  
8. Language: app and handouts exist in ES/EN/FR; pick one delivery language per cohort.

---

## 11. Suggested citation

If you use this syllabus and platform in teaching or research, cite Academy Learning Tau / Systemic Tau Platform and the domain scientific references (e.g. CCTP for cardio) listed under Evidence in the app and in `CITATION.cff`.

---

## 12. Contact and continuous improvement

- Academic issues and feedback via the project repository.  
- Pedagogy / domain-adapter collaboration: see repository README.  
- This syllabus is a **living document**: always align dataset IDs and presets with the installed STP version.

---

*Syllabus STP v1.1 · Academy Learning Tau · academic use with citation · does not constitute clinical, operational epidemiological, or financial advice.*
