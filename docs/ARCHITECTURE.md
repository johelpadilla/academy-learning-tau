# Architecture — Academy Learning Tau

Technical overview of the layered design. For product scope and navigation, see [`SPEC.md`](SPEC.md). For engineering practices and data contracts, see [`ENGINEERING.md`](ENGINEERING.md).

## Design principle

**Separation of concerns:** the user interface never implements scientific formulas; the numerical core never imports Streamlit. Pedagogy and computation remain independently testable.

```text
User (browser)
      │
      ▼
app/  (Streamlit multipage)
      │  session state · widgets · cache · page routing
      ▼
src/stp/
  ├── education/      content loading, glossary, handouts
  ├── i18n/           ES / EN / FR
  ├── domains/        domain adapters and presets
  ├── core/           ordinal, τ_s, RECD, EWS, surrogates, pipeline,
  │                   breathing window, ordinal memory, optional TDA
  ├── visualization/  scientific plots
  ├── reports/        Markdown / JSON / methods exports
  ├── data/           catalog, samples, generators
  └── cli.py          headless analysis and serve helpers
      │
      ▼ (optional parity packages)
systemictau / nested-recd   when installed for research alignment
```

## Repository roles

| Path | Responsibility |
|------|----------------|
| `app/` | Presentation only |
| `src/stp/core/` | Pure scientific functions |
| `content/` | Spanish source pedagogy |
| `locales/` | Localized UI strings and content |
| `data/` | Catalog and small demo samples |
| `tests/` | Automated verification |
| `docs/` | Academic and technical documentation |

## Invariants

1. `import streamlit` is restricted to `app/` (and narrowly scoped display helpers if any).
2. Pipeline outputs include parameters and a reproducibility fingerprint where applicable.
3. Domain interpretation is adapter-driven; core metrics remain domain-agnostic.
4. Missing locale resources fall back to Spanish without failing the session.

## Related documents

- [`SPEC.md`](SPEC.md) — product specification  
- [`LAB_FLOW.md`](LAB_FLOW.md) — laboratory interaction design  
- [`DATASETS.md`](DATASETS.md) — data policy and sources  
- [`ENGINEERING.md`](ENGINEERING.md) — stack and quality practices  
