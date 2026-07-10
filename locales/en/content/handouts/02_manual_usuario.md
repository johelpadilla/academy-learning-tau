# Systemic Tau Platform — User manual

| Field | Value |
|-------|--------|
| **Document** | Handout 02 · User manual |
| **Audience** | Students, instructors, researchers (local use) |
| **Scope** | Streamlit UI + CLI `stp` |
| **Level** | Professional computational laboratory operation |
| **Version** | 1.1 · 2026 |

---

## 1. Installation and launch

### 1.1 Requirements

- Python **3.10+** (3.11–3.12 recommended)  
- Isolated virtual environment  
- Project dependencies (`pip install -e .` or `requirements.txt`)  
- Optional TDA: `pip install systemic-tau-platform[tda]` (ripser)

### 1.2 Launch the UI

From the repository root:

```bash
streamlit run app/Home.py
# or
stp serve
```

Open the local URL (default `http://localhost:8501`).

### 1.3 Environment notes

- If you edit the `stp` package while Streamlit is running, reload or restart.  
- Bootstrap prioritizes repository `src/` to avoid stale editable installs.  
- Set environment variables only when deployment requires them (e.g. `STP_PUBLICATIONS_DIR`).

---

## 2. Application map

| Page | Pedagogical function | Typical deliverable |
|------|----------------------|---------------------|
| **Home** | Core scope, deep-links | Scope reading |
| **Foundations** | τ_s, EWS, RECD, excess3, CSD, philosophy | Micro-labs + theory |
| **Mathematics** | Formal map + Bandt–Pompe sandbox | Ordinal alphabet exercise |
| **Domains** | Empirical maturity + domain sheets | Proxy and W selection |
| **Laboratory** | Full pipeline and exports | Dual report + hash |
| **Learning path** | Sequence, glossary, FAQ | Self-assessment |
| **Evidence** | CCTP anchor / demos | Pilot-cohort reading |
| **Library** | Local publication corpus | Classified download |
| **Teaching** | 6-week syllabus and rubric | Course design |
| **Materials** | Downloadable packs | LMS / print |

Commercial plans UI is **not** part of the v1.0 educational core.

---

## 3. Laboratory — professional protocol

### 3.1 Loading data

| Path | Use | Caution |
|------|-----|---------|
| **Catalog** | Synthetic demos and samples | **Design** ground truth, not a cohort |
| **Own CSV** | Numeric T×N series | Encoding, missingness, ≥2 useful channels |
| **Deep-link** | From Domains / Home | Check domain and preset |

Common catalog metadata: `domain`, preset (W, stride, m, θ₃), `event_index` / `event_fraction`, `variables`, `ground_truth`.

### 3.2 Domain, event, and design

1. Choose the **domain** (cardiology, epidemiology, climate, …).  
2. Mark an **event index** if onset is known (VF, outbreak, drought, cohort cut…).  
3. Without an event: **1st half vs 2nd half** — **exploratory** design: declare it in the report.  
4. Do not move the event *post hoc* to “improve” p without reporting it.

### 3.3 Core parameters

| Parameter | Role | Good practice |
|-----------|------|---------------|
| `window` (W) | τ_s window length | Start from the **domain preset** |
| `stride` | Step between windows | Document implied overlap |
| `m`, `delay` | Bandt–Pompe embedding | v1.0 typical: m=3, delay=1 |
| `theta3` | Φ₃ threshold | 0.08 cardio; ~0.10 others |
| `n_surrogates` | Null replicates | Class 4–8; cite ≥50 |
| `surrogate_method` | `phase_shuffle` / `iaaft` | Default phase-shuffle |
| `mode` | `fast` / `full` | Full before citing p |
| Breathing / TDA / Memory | Extensions | Do not replace the core |

### 3.4 Run and interpret (recommended order)

1. Raw series + event marker.  
2. τ_s(t) trajectory and Δτ_s.  
3. RECD panel: Φ₁–Φ₃, excess3, Δexcess3.  
4. Classical EWS panel (var, AR1).  
5. p_surr and surrogate method.  
6. Extensions (if on): W(t), β₀/β₁, memory.  
7. Written dual reading (Handout 06 template).  
8. Export MD / JSON / Methods + `repro_hash`.

### 3.5 Exports

| File | Content | Use |
|------|---------|-----|
| `.md` report | Narrative + metrics + methods | LMS / review |
| `result.json` | Serializable series and metrics | Re-analysis |
| Methods | Paper-ready paragraph | Report body |
| `repro_hash` | SHA-256 seal | Academic integrity |

---

## 4. Demo catalog (instructor orientation)

| ID | Domain | Pedagogical role |
|----|--------|------------------|
| `synthetic_coupled_logistic` | synthetic | **Positive** control (coupling switch) |
| `synthetic_ar_noise` | synthetic | **Near-null** control |
| `cardiac_like_demo` / `sddb_rr_*` | cardiology | CCTP proxy / sample |
| `dengue_like_demo` | epidemiology | Outbreak + climate (transfer) |
| `eeg_like_demo` | neuroscience | Channel lock-in |
| `ecology_like_demo` | ecology | Bloom / nutrients |
| `climate_drought_demo` | climate | Drought regime (CSD toy) |
| `education_cohort_demo` | education | Cohort / classroom (meta-pedagogy) |
| `social_polarization_demo` | social | Polarization (demo, not social truth) |
| `sleep_fragmentation_demo` | physiology | Circadian fragmentation |
| `finance_like_demo` | finance | Vol regime — **not trading** |

**Claim rule:** synthetic demo ⇒ design ground truth. Do not present it as field evidence for a real domain.

---

## 5. CLI

```bash
stp analyze path/data.csv \
  --domain epidemiology \
  --window 13 --stride 1 \
  --mode full \
  -o out/report.md \
  --json out/result.json

stp analyze data.csv --domain synthetic --breathing --tda -o report.md
stp serve
```

See `stp analyze -h` for current flags.

---

## 6. Reproducibility (graduate standard)

1. Fix `seed` when using surrogates.  
2. Export MD + JSON for every cited run.  
3. Cite the original dataset (PhysioNet, etc.) **and** the software.  
4. Never reuse a synthetic-demo hash as if it were a clinical cohort.  
5. After code updates, re-run and compare hashes.  
6. Record W, stride, m, θ₃, n_surr, null method, and event partition.

---

## 7. Troubleshooting

| Symptom | Check |
|---------|-------|
| STP `ImportError` | `pip install -e .` and restart Streamlit |
| Blank page | Correct repo bootstrap; hard reload |
| Δτ_s ≈ 0 everywhere | AR control? Huge W? Wrong variables? |
| Φ₃ always 0 | Common under noise; report continuous **excess3** |
| Unstable p_surr | Raise n_surr; fix seed; do not cite n=2 |
| CSV fails | Non-numeric, encoding, effective N < 2 |
| Slow TDA | Use demo series or Fast; ripser optional |

---

## 8. Operational ethics (summary)

- Research and **teaching**, not clinical/operational certification.  
- Empirical maturity differs by domain; do not export CCTP pilot strength blindly.  
- Third-party data: licenses and local ethics (IRB if applicable).  
- Detail: *Ethics and scope* handout.

---

*STP User manual v1.1 · downloadable for courses and professional self-study.*
