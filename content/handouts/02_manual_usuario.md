# Systemic Tau Platform — Manual de usuario

| Campo | Valor |
|-------|--------|
| **Documento** | Handout 02 · Manual de usuario |
| **Audiencia** | Estudiantes, docentes, investigadores (uso local) |
| **Alcance** | Interfaz Streamlit + CLI `stp` |
| **Nivel** | Operación profesional de laboratorio computacional |
| **Versión** | 1.1 · 2026 |

---

## 1. Instalación y arranque

### 1.1 Requisitos

- Python **3.10+** (recomendado 3.11–3.12)  
- Entorno virtual aislado  
- Dependencias del proyecto (`pip install -e .` o `requirements.txt`)  
- Opcional TDA: `pip install systemic-tau-platform[tda]` (ripser)

### 1.2 Arranque de la interfaz

Desde la raíz del repositorio:

```bash
streamlit run app/Home.py
# o
stp serve
```

Abra la URL local (por defecto `http://localhost:8501`).

### 1.3 Notas de entorno

- Si edita el paquete `stp` con Streamlit en marcha, recargue o reinicie.  
- El bootstrap prioriza el `src/` del repositorio para evitar instalaciones editables obsoletas.  
- Variables de entorno solo si el despliegue lo exige (p.ej. `STP_PUBLICATIONS_DIR`).

---

## 2. Mapa de la aplicación

| Página | Función pedagógica | Entregable típico |
|--------|--------------------|-------------------|
| **Home** | Alcance del núcleo, deep-links | Lectura de límites |
| **Fundamentos** | τ_s, EWS, RECD, excess3, CSD, filosofía | Micro-labs + teoría |
| **Matemática** | Mapa formal + sandbox Bandt–Pompe | Ejercicio de alfabeto ordinal |
| **Dominios** | Madurez empírica + ficha por dominio | Selección de proxy y W |
| **Laboratorio** | Pipeline completo y exportaciones | Informe dual + hash |
| **Ruta de aprendizaje** | Secuencia, glosario, FAQ | Autoevaluación |
| **Evidencia** | Ancla CCTP / demos | Lectura de cohorte piloto |
| **Biblioteca** | Corpus de publicaciones locales | Descarga clasificada |
| **Docencia** | Syllabus 6 semanas y rúbrica | Diseño de curso |
| **Materiales** | Packs descargables | LMS / impresión |

La UI de planes comerciales **no** forma parte del núcleo educativo v1.0.

---

## 3. Laboratorio — protocolo profesional

### 3.1 Carga de datos

| Vía | Uso | Precaución |
|-----|-----|------------|
| **Catálogo** | Demos sintéticos y samples | Ground truth de **diseño**, no cohorte |
| **CSV propio** | Series numéricas T×N | Encoding, missing, ≥2 canales útiles |
| **Deep-link** | Desde Dominios / Home | Verifique dominio y preset |

### 3.2 Dominio, evento y diseño

1. Elija el **dominio**.  
2. Marque un **índice de evento** si conoce el onset.  
3. Sin evento: partición **1ª mitad vs 2ª** — diseño **exploratorio**: declárelo.  
4. No mueva el evento *post hoc* para “mejorar” el p sin reportarlo.

### 3.3 Parámetros del núcleo

| Parámetro | Rol | Buena práctica |
|-----------|-----|----------------|
| `window` (W) | Longitud de ventana de τ_s | Empezar por el **preset de dominio** |
| `stride` | Paso entre ventanas | Documentar solapamiento |
| `m`, `delay` | Embedding Bandt–Pompe | v1.0 típico: m=3, delay=1 |
| `theta3` | Umbral de Φ₃ | 0.08 cardio; ~0.10 otros |
| `n_surrogates` | Réplicas del nulo | Clase 4–8; citar ≥50 |
| `surrogate_method` | `phase_shuffle` / `iaaft` | Default phase-shuffle |
| `mode` | `fast` / `full` | Full antes de citar p |
| Breathing / TDA / Memoria | Extensiones | No sustituyen el núcleo |

### 3.4 Ejecución e interpretación (orden recomendado)

1. Series crudas + marcador de evento.  
2. Trayectoria τ_s(t) y Δτ_s.  
3. Panel RECD: Φ₁–Φ₃, excess3, Δexcess3.  
4. Panel EWS clásicas (var, AR1).  
5. p_surr y método de surrogate.  
6. Extensiones (si activas): W(t), β₀/β₁, memoria.  
7. Lectura dual escrita (plantilla Handout 06).  
8. Export MD / JSON / Methods + `repro_hash`.

### 3.5 Exportaciones

| Archivo | Contenido | Uso |
|---------|-----------|-----|
| Reporte `.md` | Narrativa + métricas + métodos | LMS / revisión |
| `result.json` | Series y métricas serializables | Reanálisis |
| Methods | Párrafo listo para papers | Cuerpo del informe |
| `repro_hash` | Sello SHA-256 | Integridad académica |

---

## 4. Catálogo de demos (orientación docente)

| ID | Dominio | Función pedagógica |
|----|---------|-------------------|
| `synthetic_coupled_logistic` | sintético | Control **positivo** |
| `synthetic_ar_noise` | sintético | Control **casi-nulo** |
| `cardiac_like_demo` / `sddb_rr_*` | cardiología | Proxy CCTP / sample |
| `dengue_like_demo` | epidemiología | Brote + clima (transferencia) |
| `eeg_like_demo` | neurociencia | Lock-in de canales |
| `ecology_like_demo` | ecología | Bloom / nutrientes |
| `climate_drought_demo` | clima | Régimen de sequía (juguete CSD) |
| `education_cohort_demo` | educación | Cohorte / aula (meta-pedagógico) |
| `social_polarization_demo` | social | Polarización (demo, no verdad social) |
| `sleep_fragmentation_demo` | fisiología | Fragmentación circadiana |
| `finance_like_demo` | finanzas | Régimen de vol — **no trading** |

**Regla de claim:** demo sintético ⇒ ground truth de diseño. No lo presente como evidencia empírica de dominio real.

---

## 5. CLI

```bash
stp analyze ruta/datos.csv \
  --domain epidemiology \
  --window 13 --stride 1 \
  --mode full \
  -o salida/reporte.md \
  --json salida/resultado.json

stp analyze data.csv --domain synthetic --breathing --tda -o report.md
stp serve
```

Consulte `stp analyze -h` para flags actualizados.

---

## 6. Reproducibilidad (estándar de posgrado)

1. Fije `seed` cuando use surrogates.  
2. Exporte MD + JSON de toda corrida que cite.  
3. Cite dataset original **y** software.  
4. No reutilice un hash de demo sintético como cohorte clínica.  
5. Tras actualizar código, re-corra y compare hashes.  
6. Registre W, stride, m, θ₃, n_surr, método de nulo y partición del evento.

---

## 7. Solución de problemas

| Síntoma | Qué revisar |
|---------|-------------|
| `ImportError` STP | `pip install -e .` y reiniciar Streamlit |
| Página en blanco | Bootstrap al repo correcto; recarga dura |
| Δτ_s ≈ 0 en todo | ¿Control AR? ¿W enorme? ¿Variables mal elegidas? |
| Φ₃ siempre 0 | Normal con ruido; reporte **excess3** continuo |
| p_surr inestable | Suba n_surr; fije seed; no cite n=2 |
| CSV no carga | No numérico, encoding, N efectivo < 2 |
| TDA lento | Use series demo o Fast; ripser opcional |

---

## 8. Ética operativa (resumen)

- Investigación y **docencia**, no certificación clínica/operativa.  
- Madurez empírica distinta por dominio; no extrapole la fuerza del piloto CCTP.  
- Datos de terceros: licencias y ética local (IRB si aplica).  
- Detalle: handout *Ética y alcance*.

---

*STP Manual de usuario v1.1 · material descargable para cursos y autoestudio profesional.*
