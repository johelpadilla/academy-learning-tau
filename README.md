# Academy Learning Tau

**Educational and research platform for the Systemic Tau paradigm and the Discrete Extramental Clock (RECD)**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21301571.svg)](https://doi.org/10.5281/zenodo.21301571)
[![ORCID](https://img.shields.io/badge/ORCID-0000--0002--5797--6931-a6ce39.svg)](https://orcid.org/0000-0002-5797-6931)

| | |
|:--|:--|
| **Repository** | [github.com/johelpadilla/academy-learning-tau](https://github.com/johelpadilla/academy-learning-tau) |
| **DOI (Zenodo)** | [10.5281/zenodo.21301571](https://doi.org/10.5281/zenodo.21301571) |
| **Local entry point** | `app/Home.py` |
| **Languages** | Spanish (source) · English · French |
| **Version** | 1.1.0 |
| **Author** | Johel Padilla-Villanueva |
| **Contact** | [joel.padilla2@upr.edu](mailto:joel.padilla2@upr.edu) |

---

## Abstract

**Academy Learning Tau** is an open educational and research software platform that operationalizes the **Systemic Tau** framework and the **Discrete Extramental Clock (RECD)** for the analysis of complex time series. It combines (i) rigorous ordinal metrics (τ<sub>s</sub>, nested RECD levels Φ₁–Φ₃), (ii) classical early-warning signals for methodological comparison, (iii) surrogate-based null models, and (iv) a guided multipage Streamlit laboratory with reproducible exports.

The platform is intended for graduate teaching, methodological training, and exploratory research in domains such as computational cardiology, epidemiology, neuroscience, ecology, and financial regime analysis. It is **not** a medical device, clinical decision-support system, or investment advisory tool.

---

## Scientific scope

### Conceptual framework

| Construct | Role in the platform |
|-----------|----------------------|
| **Systemic Tau (τ<sub>s</sub>)** | Ordinal, structure-sensitive observable for reorganization in complex series |
| **RECD** | Nested discrete-time levels (Φ₁ local, Φ₂ relational, Φ₃ global ascent) |
| **Bandt–Pompe** | Symbolic encoding underlying ordinal pattern statistics |
| **EWS (classical)** | Variance, lag-1 autocorrelation, and related indicators for dual reading |
| **Surrogates** | Phase-shuffle and IAAFT procedures for null comparison |
| **Reproducibility hash** | Fingerprint of data configuration, parameters, and software path |

### Platform modules

| Module | Description |
|--------|-------------|
| **Fundamentos** | Theoretical foundations of Systemic Tau and RECD |
| **Matemática** | Formal definitions and pedagogical walkthroughs |
| **Dominios** | Domain-specific narrative and laboratory presets |
| **Laboratorio** | Interactive analysis: load → configure → run → interpret → export |
| **Ruta de aprendizaje** | Structured learning path for intermediate–advanced users |
| **Evidencia** | Links to publications, preprints, and regenerable figures |
| **Docencia** | Teaching notes and classroom-oriented materials |
| **Materiales** | Downloadable handouts and instructional packs |

### Core library (`src/stp`)

- `core/` — τ<sub>s</sub>, RECD levels, ordinal patterns, EWS, surrogates, pipeline, breathing window, ordinal memory, optional TDA/Betti
- `domains/` — domain adapters and presets
- `education/` — content loading, glossary, handouts
- `i18n/` — ES / EN / FR localization
- `visualization/` — series and dual-reading plots
- `reports/` — Markdown / JSON / methods-style exports
- `data/` — catalog, samples, synthetic generators
- `cli.py` — headless analysis and local serve helpers

---

## Requirements

- Python **3.10** or newer
- Operating system: macOS, Linux, or Windows
- Recommended: 8 GB RAM for interactive laboratory use with moderate series length

Optional scientific extensions (not required for the default educational path):

- `ripser` / `persim` — topological data analysis
- `wfdb` — PhysioNet / SDDB preprocessing
- `systemictau`, `nested-recd` — parity with companion research packages when installed

---

## Installation

```bash
git clone https://github.com/johelpadilla/academy-learning-tau.git
cd academy-learning-tau

python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

pip install -r requirements.txt
pip install -e .
```

---

## Running the platform

### Graphical laboratory (Streamlit)

```bash
streamlit run app/Home.py
```

Open the local URL printed by Streamlit (commonly `http://localhost:8501` or `http://localhost:8502`).

Alternative entry points (if installed in editable mode):

```bash
stp serve
# or
PYTHONPATH=src streamlit run app/Home.py
```

### Streamlit Community Cloud

Main file: `app/Home.py` · repo: `johelpadilla/academy-learning-tau` · branch: `main`.

**Required:** in **Advanced settings** set **Python 3.12** (or 3.11). Do **not** leave the default if it is 3.14 — logs show `ModuleNotFoundError: scipy`, multipage `_DeadlockError`, and segfaults on 3.14 with this stack.

To change Python after deploy: **delete the app and redeploy**, selecting 3.12 in Advanced settings (Cloud does not switch Python in place). Then **Reboot**.

Intended version is also recorded in `runtime.txt` / `.python-version` (Cloud primarily honors the UI selector).

### Command-line analysis

```bash
stp analyze data/samples/sddb_rr_38_demo.csv \
  --domain cardiology \
  --columns z_rr,z_abs_drr \
  --event 6800 \
  -o report.md \
  --json result.json
```

Optional flags (when available in your build): `--breathing`, `--tda`.

---

## Internationalization

| Language | Role |
|----------|------|
| **Spanish (es)** | Source language for UI strings and pedagogical content |
| **English (en)** | Full UI and content locale |
| **French (fr)** | Full UI and content locale |

Select the language in the sidebar (**Idioma / Language / Langue**). Missing keys or documents fall back to Spanish. Programmatic control:

```python
from stp.i18n import set_lang, t
set_lang("en")
```

Or set the environment variable `STP_LANG=en`.

---

## Repository layout

```text
academy-learning-tau/
├── app/                 # Streamlit multipage interface
│   ├── Home.py          # Application entry
│   ├── components/      # UI building blocks
│   └── pages/           # Fundamentos … Materiales
├── src/stp/             # Scientific and educational library
├── content/             # Source pedagogical Markdown (Spanish)
├── locales/             # UI JSON + localized content (es, en, fr)
├── data/                # Dataset catalog and demo samples
├── docs/                # Technical and product documentation
├── tests/               # Pytest suite
├── scripts/             # Preprocessing and export utilities
├── requirements.txt
└── pyproject.toml
```

---

## Documentation

| Document | Contents |
|----------|----------|
| [docs/SPEC.md](docs/SPEC.md) | Product specification: vision, navigation, UI, roadmap |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | Layered architecture overview |
| [docs/ENGINEERING.md](docs/ENGINEERING.md) | Stack, contracts, engineering practices |
| [docs/LAB_FLOW.md](docs/LAB_FLOW.md) | Interactive laboratory interaction design |
| [docs/DATASETS.md](docs/DATASETS.md) | Dataset policy, SDDB and multi-domain sources |

---

## Tests

```bash
PYTHONPATH=src pytest -q
```

---

## Citing this work

If you use Academy Learning Tau in teaching or research, please cite the software and the domain-specific scientific references relevant to your study.

**Software (suggested)**

```bibtex
@software{padilla_academy_learning_tau_2026,
  author    = {Padilla-Villanueva, Johel},
  title     = {Academy Learning Tau: Educational and research platform
               for Systemic Tau and RECD},
  year      = {2026},
  version   = {1.1.0},
  doi       = {10.5281/zenodo.21301571},
  url       = {https://doi.org/10.5281/zenodo.21301571},
  orcid     = {0000-0002-5797-6931}
}
```

**DOI:** [https://doi.org/10.5281/zenodo.21301571](https://doi.org/10.5281/zenodo.21301571)

A machine-readable citation file is provided as [`CITATION.cff`](CITATION.cff).

Domain literature (examples; cite as appropriate to your application):

- Cardiac CCTP / SDDB materials (e.g. Zenodo record `10.5281/zenodo.21270699` when used)
- Systemic Tau and RECD theoretical works by the author (Síntesis Magna, Foundations, and related preprints)

---

## Research and data provenance

Demo samples under `data/samples/` are **illustrative** and may be derived from public sources (e.g. PhysioNet SDDB) under their original licenses. Always:

1. Respect the license of each external dataset.
2. Cite the original data publisher and DOI.
3. Prefer regenerating processed series via documented scripts rather than redistributing large raw archives.

See [docs/DATASETS.md](docs/DATASETS.md) for operational guidance.

---

## Ethical and legal notice

This software is provided for **education and scientific research**. It does **not** constitute:

- a medical device or diagnostic instrument;
- clinical advice or patient-management guidance;
- financial, investment, or risk-management advice.

Use of physiological or epidemiological data must comply with institutional ethics boards, data-use agreements, and applicable law.

---

## License

MIT License © 2026 Johel Padilla-Villanueva  
ORCID: [0000-0002-5797-6931](https://orcid.org/0000-0002-5797-6931)

See [LICENSE](LICENSE) for the full text.

---

## Contributing

Issues and scholarly feedback are welcome via the GitHub repository. For collaboration on pedagogy or domain adapters, contact the author at [joel.padilla2@upr.edu](mailto:joel.padilla2@upr.edu).

---

## Acknowledgments

Development is informed by ongoing research programs in ordinal complex-systems methods, early-warning signals, and multi-domain applications of Systemic Tau / RECD. Companion packages and pilot studies may be cited separately where methods parity is claimed.
