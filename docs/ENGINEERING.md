# Ingeniería — Academy Learning Tau

Prácticas de desarrollo y stack tecnológico de la plataforma. Complementa [`ARCHITECTURE.md`](ARCHITECTURE.md) y [`SPEC.md`](SPEC.md).

## Stack recomendado

| Capa | Librería | Justificación |
|------|----------|---------------|
| Interfaz | **streamlit** (+ streamlit-extras) | Multipágina, adopción en entornos científicos |
| Gráficos | **plotly** | Interactividad y exportación para informes |
| Núcleo numérico | **numpy**, **scipy**, **numba** | Rendimiento en Bandt–Pompe y ventanas deslizantes |
| Datos | **pandas**, **pydantic** | Tablas y validación de parámetros |
| Informes | **reportlab** (base); weasyprint opcional | Artefactos PDF |
| Paridad RECD | **nested-recd** (si instalado) | Alineación con implementaciones de paper |
| Paridad Tau | **systemictau** (si instalado) | Alineación con el ecosistema de investigación |
| TDA opcional | **ripser**, **persim** | Números de Betti / persistencia |
| Fisiología | **wfdb** | SDDB / PhysioNet |
| Calidad | **pytest**, **ruff**, **mypy** | Pruebas y estilo |

### Fuera del alcance de v1.0

- Duplicar la UI en Dash o Gradio sin necesidad pedagógica clara  
- Deep learning en el camino crítico (puede usarse solo como comparación externa)  
- Base de datos obligatoria para la experiencia educativa local

---

## Arquitectura de capas

```text
app/ (Streamlit)     → thin: layout, widgets, cache, session
content/ (Markdown)  → copy pedagógica versionada
src/stp/core         → pure functions, sin streamlit
src/stp/domains      → adapters + interpretación
src/stp/reports      → I/O de artefactos
```

**Regla de oro:** `import streamlit` **solo** bajo `app/` y `stp.education` display helpers. El core debe ser testeable headless.

---

## Contratos de datos

### `AnalysisParams` (pydantic)

```python
class AnalysisParams(BaseModel):
    window: int = 101
    stride: int = 5
    m: int = 3
    delay: int = 1
    d_persist: int = 4
    theta3: float = 0.08
    n_surrogates: int = 8
    mode: Literal["fast", "full"] = "fast"
    seed: int = 42
    zscore: bool = True
    include_ews: bool = True
    include_tda: bool = False
    include_memory: bool = False
```

### `AnalysisResult`

```python
@dataclass
class AnalysisResult:
    tau_s: np.ndarray
    phi1: np.ndarray
    phi2: np.ndarray
    phi3: np.ndarray
    excess3: np.ndarray
    T_recd: np.ndarray
    ews: dict[str, np.ndarray]
    surrogate_stats: dict
    tda: dict | None
    memory: dict | None
    metrics: dict  # deltas, p-values, means
    params: AnalysisParams
    repro_hash: str
    lib_versions: dict[str, str]
```

---

## Caché y rendimiento

1. **Fingerprinting de datos:** hash de `df.values.tobytes()` + nombres de columnas, no del path.
2. **`@st.cache_data`** en:
   - `load_sample(dataset_id)`
   - `run_pipeline(data_hash, params_json)`
3. **`@st.cache_resource`** en loaders de catálogo YAML y glosario.
4. **Numba** en:
   - generación Bandt–Pompe
   - conteos Φ₁/Φ₂ en loops de pares
5. **Stride** generoso en Fast; Full puede usar stride=1.
6. **No** recalcular surrogates al cambiar solo la pestaña de plots.

### Presupuesto de tiempo (guía)

| Operación | Fast | Full |
|-----------|------|------|
| τ_s | O(T·N²/W) | igual |
| RECD levels | O(T·N²·d) | igual |
| Surrogates | ×8 | ×50 |
| TDA | — | O(costoso) → subsample |

---

## Reproducibilidad

```text
repro_hash = SHA256(
  canonical_json(params)
  + data_fingerprint
  + stp_version
  + nested_recd_version?
  + numpy_version
)
```

Incluir en cada reporte:
- hash
- timestamp UTC
- seed
- command-equivalent (params YAML)

---

## Testing

| Nivel | Qué | Dónde |
|-------|-----|-------|
| Unit | ordinal, phi1/2/3 shapes, hash estable | `tests/test_core_*.py` |
| Integration | pipeline Fast en sample sintético | `tests/test_pipeline.py` |
| Smoke UI | `streamlit run` no crashea (manual CI) | opcional |
| Regression | Δτ_s sign en fixture CCTP-like | `tests/fixtures/` |

```bash
pytest -q
ruff check src app
```

---

## Estilo de código

- Type hints en APIs públicas.
- Docstrings estilo NumPy en `core/`.
- Sin side effects en funciones puras.
- Logging con `logging` (no `print`) en core; Streamlit muestra `st.toast` / status.
- Español en UI y content; **inglés** en nombres de API y código.

---

## Seguridad y privacidad

- No loguear filas de CSV del usuario.
- Uploads solo en memoria / temp session; no persistir en Free.
- Disclaimers médicos/financieros en dominios sensibles.
- PhysioNet: no redistribuir `.dat` crudos; solo samples derivados permitidos o scripts.

---

## Empaquetado y deploy

| Target | Cómo |
|--------|------|
| Local dev | `streamlit run app/Home.py` |
| PyPI package | `pip install systemic-tau-platform` + entrypoint |
| Docker | imagen slim + non-root (fase P5) |
| Cloud | Streamlit Community Cloud / Cloud Run (fase SaaS) |

```dockerfile
# sketch
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app/Home.py", "--server.address=0.0.0.0"]
```

---

## Integración gradual con `systemictau` / `nested-recd`

```python
def compute_recd_levels(X, **kw):
    try:
        from nested_recd import compute_recd_from_conjunctions
        return compute_recd_from_conjunctions(X, **kw)
    except ImportError:
        from stp.core.recd_levels import compute_recd_from_conjunctions
        return compute_recd_from_conjunctions(X, **kw)
```

Así la plataforma es **usable sin** instalar el stack completo, pero **bit-compatible** cuando está presente.

---

## Observabilidad (futuro Professional)

- Contador anónimo de análisis por dominio
- Tiempo de pipeline (p50/p95)
- Errores de validación de schema (para mejorar UX)

No en v1.0 free.
