# Flujo del Laboratorio — Academy Learning Tau

## Objetivo pedagógico y de investigación

Permitir que un investigador o estudiante de posgrado complete, en un tiempo acotado (del orden de minutos), un ciclo completo:

> cargar datos → configurar → analizar → interpretar → exportar con huella de reproducibilidad

sin programar, con valores por defecto coherentes por dominio.

---

## Mapa de estados (`st.session_state`)

| Clave | Tipo | Descripción |
|-------|------|-------------|
| `lab_data` | `pd.DataFrame` | Serie cargada |
| `lab_meta` | `dict` | dominio, fuente, event_index |
| `lab_params` | `AnalysisParams` | ventana, m, modo, etc. |
| `lab_result` | `AnalysisResult` | salidas del pipeline |
| `lab_hash` | `str` | repro hash |
| `lab_step` | `int` | 1–5 wizard |

---

## Wizard de 5 pasos

### Paso 1 — Origen de datos

```
┌──────────────────────────────────────────────────────────┐
│  ○ Dataset de ejemplo (dominio)                          │
│  ○ Subir CSV / Excel                                     │
│  ○ Sintético (demo pedagógica)                           │
└──────────────────────────────────────────────────────────┘
```

**Widgets**
- `st.radio` origen
- Si sample: `st.selectbox` dominio → dataset del catálogo
- Si upload: `st.file_uploader` (csv, xlsx) + preview `st.dataframe`
- Si sintético: tipo (logistic coupled, AR noise, Feigenbaum sweep)

**Validaciones**
- ≥ 2 columnas numéricas
- T ≥ max(3·W, 100)
- Mensaje claro si falla

**Acción:** “Continuar →” guarda `lab_data`, avanza a paso 2.

---

### Paso 2 — Esquema y roles

```
Columna tiempo (opcional): [auto index ▼]
Variables de análisis:     [x] col_a  [x] col_b  [ ] col_c
Evento / transición:       [ninguno ▼]  o índice manual
```

**Widgets**
- Multiselect de columnas
- Opcional: columna de timestamp
- Opcional: índice de evento (vfon, brote, crisis)
- Switch “Estandarizar (z-score)” (default ON)

**Dominio-aware hints**
- Cardio: sugiere `z_rr`, `z_abs_drr`
- Dengue: `cases_z`, clima
- etc.

---

### Paso 3 — Parámetros de análisis

Layout: **2 columnas** (Core | Advanced expander)

| Parámetro | Default | Rango |
|-----------|---------|-------|
| Modo | Fast | Fast / Full |
| W (ventana τ_s) | dominio | 11–301 (impar) |
| stride | dominio | 1–20 |
| m (ordinal) | 3 | 3–5 |
| delay | 1 | 1–5 |
| d_persist (Φ₂) | 4 | 2–10 |
| θ₃ (Φ₃) | 0.08–0.10 | 0.01–0.5 |
| n_surrogates | 8 / 50 | 0–200 |
| EWS clásicos | ON | toggle |
| TDA | OFF en Fast | toggle |
| Memoria ordinal | OFF en Fast | toggle |

**Presets**
- Botones: “Preset CCTP Cardio”, “Preset Dengue W=13”, “Preset Research Full”

**Seed** para surrogates: input int (reproducibilidad).

---

### Paso 4 — Ejecución

```
[▶ Ejecutar análisis completo]
```

Durante la corrida:
1. `st.status` o `st.progress` con etapas:
   - Preprocess
   - Systemic Tau
   - RECD levels
   - Classical EWS
   - Surrogates (si n>0)
   - TDA / Memory (si Full)
   - Hash
2. Errores capturados con mensaje accionable (no traceback crudo al usuario).

Al terminar: `lab_result` + `lab_hash` → paso 5 automático.

**Cache**
```python
@st.cache_data(show_spinner=False)
def run_pipeline(data_bytes_hash, params_json) -> AnalysisResult:
    ...
```

---

### Paso 5 — Resultados e interpretación

**Tabs**

| Tab | Contenido |
|-----|-----------|
| **Overview** | Métricas clave (Δτ_s, mean excess3, p_surr), hash, params |
| **Series** | Series originales + event marker |
| **τ_s** | Serie temporal τ_s, hist, basal vs approach boxplot |
| **RECD** | Φ₁, Φ₂, Φ₃, excess3; stacked contribuciones; T_recd |
| **EWS clásicos** | var, AR1 overlay vs τ_s (normalizados) |
| **Surrogates** | null distribution de Δτ_s / Δexcess3 |
| **TDA** | Betti curves / persistence (Full) |
| **Interpretación** | Texto guiado por dominio + semáforo |

**Semáforo de interpretación (heurística pedagógica)**

| Condición | Color | Mensaje |
|-----------|-------|---------|
| \|Δτ_s\| significativo + concordante excess3 | 🟢 | Reorganización relacional detectada |
| Solo EWS clásicos se mueven | 🟡 | Señal univariada sin soporte ordinal |
| Nada significativo | ⚪ | Sin evidencia de transición en ventana |
| Discordancia fuerte | 🟠 | Revisar calidad de datos / pacing / AF |

**Export row**
- Descargar Markdown
- Descargar PDF (reportlab)
- Descargar JSON resultados
- Descargar figuras PNG (zip opcional)
- Copiar `repro_hash`

---

## Diagrama de secuencia (usuario × sistema)

```text
Usuario                Streamlit UI              stp.core
  │                         │                        │
  │  elige sample cardio    │                        │
  │────────────────────────▶│  load_catalog()        │
  │                         │───────────────────────▶│
  │                         │◀───────────────────────│
  │  ajusta W=101, Fast     │                        │
  │────────────────────────▶│                        │
  │  Ejecutar               │                        │
  │────────────────────────▶│  compute_tau_s()       │
  │                         │───────────────────────▶│
  │                         │  compute_recd()        │
  │                         │───────────────────────▶│
  │                         │  surrogates()          │
  │                         │───────────────────────▶│
  │                         │  repro_hash()          │
  │                         │───────────────────────▶│
  │  ve tabs + exporta PDF  │◀───────────────────────│
  │◀────────────────────────│                        │
```

---

## Edge cases a manejar en UI

1. **N=1** → ofrecer generar proxy `|Δx|` como segunda variable (patrón CCTP).
2. **T corto** → advertir y sugerir reducir W.
3. **NaNs** → opción drop / interpolate; nunca silenciar.
4. **Columnas no numéricas** → filtrar y avisar.
5. **Upload > 200 MB** — bloqueado por config Streamlit; sugerir downsample.
6. **Sin event_index** — reportar medias globales + percentiles, no Δ basal/approach.
7. **Timeout Full** — permitir cancelar y degradar a Fast.

---

## Criterios de aceptación del Lab

- [ ] Demo cardio record 38 completa en Fast < 10 s en laptop M-series
- [ ] Hash idéntico al re-ejecutar mismos datos+params+seed
- [ ] PDF genera sin error con 2 figuras embebidas
- [ ] Comparación EWS visible y legible
- [ ] Mensajes de error en español (UI) con detalle técnico en expander
