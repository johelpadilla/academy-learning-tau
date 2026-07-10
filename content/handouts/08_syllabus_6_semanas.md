# Syllabus — Análisis ordinal de sistemas complejos con Systemic Tau / RECD

| Campo | Valor |
|-------|--------|
| **Plataforma** | Academy Learning Tau · Systemic Tau Platform (STP) v1.0 |
| **Formato** | Curso corto intensivo · **6 semanas** |
| **Nivel** | Posgrado (maestría / doctorado) o especialización profesional con base cuantitativa |
| **Modalidad** | Híbrido o presencial + laboratorio computacional (app Streamlit + CLI opcional) |
| **Carga estimada** | **4–5 h/semana** (≈ 2 h lectura/teoría + 2–3 h Lab/informe) · **24–30 h** totales |
| **Idiomas de la app** | Español (fuente), English, Français |
| **Versión del syllabus** | 1.1 · 2026 |
| **Documento** | Handout `08_syllabus_6_semanas` · uso académico con citación |

---

## 1. Descripción del curso

Este curso enseña a **formular, ejecutar y documentar** un análisis de **reorganización relacional** en series temporales multivariadas mediante:

1. **Systemic Tau (τ_s)** — termómetro de acoplamiento ordinal entre canales;  
2. **RECD ordinal anidado (Φ₁–Φ₃ + excess3)** — gramática de coincidencia, persistencia y sinergia irreducible;  
3. **Lectura dual** — contraste sistemático con **EWS clásicas** (varianza, AR(1));  
4. **Nulos por surrogates** (phase-shuffle / IAAFT) y **reproducibilidad** (hash SHA-256, Methods, export MD/JSON).

El **ancla empírica de referencia** es el protocolo **CCTP** (cardiología computacional / pre-FV, cohorte piloto y demos SDDB). Otras aplicaciones (epidemiología, neuro, ecología, clima, educación, fisiología del sueño, finanzas, dinámica social) se tratan como **transferencia metodológica** con madurez empírica explícita — no como promesas predictivas.

**No es** un curso de dispositivo médico, alerta epidemiológica operativa, trading ni scoring social.

---

## 2. Competencias de salida

Al aprobar el curso, el estudiante será capaz de:

| # | Competencia (observable) |
|---|---------------------------|
| C1 | **Definir** una pregunta relacional (“¿se reorganiza el acoplamiento entre X e Y en torno a un evento?”) distinta de una pregunta solo univariada (“¿sube la varianza?”). |
| C2 | **Seleccionar** variables, evento (si existe), preset de dominio y parámetros (W, stride, m, θ₃, n_surr) de forma justificada. |
| C3 | **Calcular** τ_s en ventana deslizante y el panel RECD (Φ₁–Φ₃, excess3, T_recd) en el Lab o vía CLI. |
| C4 | **Comparar** el panel relacional con var/AR1 (lectura dual) e interpretar concordancia, discordancia o quietud. |
| C5 | **Nular** el contraste Δτ_s con surrogates y reportar p_surr sin reducir el informe a un único p-valor. |
| C6 | **Documentar** Methods reproducibles (parámetros, seed, hash, límites del dominio) y acotar claims a la madurez empírica. |
| C7 | **Transferir** la misma gramática a un segundo dominio, enunciando qué cambia (proxy, W, jerga) y qué no (ontología del método). |

**Competencia integradora (entregable final):** un *portfolio* con informe de lectura dual + export MD/JSON + Methods + checklist firmado, evaluado con la rúbrica de la §7.

---

## 3. Prerrequisitos

**Obligatorios**

- Series temporales o estadística intermedia (media, varianza, correlación, idea de proceso estocástico).  
- Lectura de gráficos científicos y tablas de métricas.  
- Uso básico de un navegador y de un entorno local o servidor de la app.

**Recomendados (no bloqueantes)**

- Python básico o familiaridad con Jupyter (track CLI/notebooks).  
- Nociones de sistemas complejos o EWS / critical slowing down.  
- En el track cardio: vocabulario mínimo de ECG/RR (no se exige formación clínica).

**Software**

- Academy Learning Tau (Streamlit) con catálogo de demos.  
- Opcional: CLI `stp analyze` / `stp serve` (mismo núcleo).  
- Export: Markdown, JSON; PDF vía Pandoc si el LMS lo exige.

---

## 4. Mapa del curso ↔ módulos de la app

| Semana | Módulos STP | Handouts prioritarios |
|--------|-------------|------------------------|
| 1 | Fundamentos (EWS, CSD) · Lab (solo EWS / sintético) | Ética · Guía rápida · Fundamentos 02/05 |
| 2 | Matemática · Lab (τ_s, hash) | Matemática práctica · Teoría τ_s |
| 3 | Fundamentos RECD/excess3 · Lab | Lectura dual · Cheat-sheet Lab |
| 4 | Dominios (cardio) · Evidencia · Lab Full | Dominio cardiología · Checklist |
| 5 | Dominios (transferencia) · Lab | Ficha del dominio elegido · FAQ |
| 6 | Lab export · Materiales · Docencia | Ética (repaso) · Pack estudiante |

---

## 5. Programa semanal detallado

Carga orientativa por semana: **lectura 90–120 min · Lab 90–120 min · escritura 30–60 min**.

### Semana 1 — EWS clásicas, CSD y límites del panel univariado

| Elemento | Contenido |
|----------|-----------|
| **Objetivos** | Explicar var y AR(1) como EWS; enunciar al menos dos fallas conceptuales (ambigüedad de signo, univariado vs relacional); citar el alcance ético del software. |
| **Teoría** | Fundamentos · pestañas EWS y CSD; handout *Ética y alcance*. |
| **Lab** | Dataset `synthetic_coupled_logistic` o `synthetic_ar_noise`. Observar var/AR1; **no** exigir aún lectura dual completa. |
| **Entrega formativa** | Ensayo corto (≈ 1 página): *“¿Cuándo un aumento de varianza no responde la pregunta del sistema?”* |
| **Criterio de éxito** | Distingue EWS clásicas de reorganización relacional; no afirma predicción clínica. |

### Semana 2 — Patrones ordinales Bandt–Pompe y Systemic Tau (τ_s)

| Elemento | Contenido |
|----------|-----------|
| **Objetivos** | Definir símbolos Bandt–Pompe (m=3); interpretar τ_s como acoplamiento ordinal en ventanas; registrar **repro_hash**. |
| **Teoría** | Fundamentos · τ_s; Matemática (sandbox m=3); ilustraciones de reorganización vs amplitud. |
| **Lab** | `synthetic_coupled_logistic` · preset `synthetic` · modo Fast · W/stride coherentes · n_surr ≥ 8. Comparar con `synthetic_ar_noise` (control casi-nulo). |
| **Entrega formativa** | Captura o tabla: Δτ_s, p_surr (si aplica), hash; 5 líneas de interpretación *sin* overclaim. |
| **Criterio de éxito** | Explica por qué el control AR/noise no debe “parecer” un switch de acoplamiento. |

### Semana 3 — RECD anidado, excess3 y lectura dual

| Elemento | Contenido |
|----------|-----------|
| **Objetivos** | Describir Φ₁–Φ₃ y el papel de **excess3** bajo ruido; aplicar el protocolo de lectura dual (concordancia / mixta / quietud). |
| **Teoría** | Fundamentos · RECD y excess3; handouts *Lectura dual* y *Teoría τ_s + RECD*. |
| **Lab** | Mismo sintético o cardio-like en Fast; panel RECD; dual summary; **no** basar el claim solo en extensiones TDA/breathing. |
| **Entrega formativa** | Mini-informe (1–2 págs.) con: pregunta, parámetros, dual reading, una frase de alcance. |
| **Criterio de éxito** | Usa excess3 como primario si Φ₃ binario se apaga; compara con var/AR1. |

### Semana 4 — Ancla empírica: cardiología CCTP / pre-FV

| Elemento | Contenido |
|----------|-----------|
| **Objetivos** | Aplicar el proxy \(X=[z(\mathrm{RR}), z(\|\Delta\mathrm{RR}\|)]\) y el preset `cardiology` (p.ej. W≈101, stride=5, θ₃≈0.08); redactar lectura dual **con voz de dominio** y disclaimers clínicos. |
| **Teoría** | Dominios · Cardiología; Evidencia (piloto CCTP N=10, límites); jerga RR, FV, Holter, SDDB. |
| **Lab** | Preferente: `cardiac_like_demo`. Si hay samples: `sddb_rr_38_demo` (señal fuerte) y opcional `sddb_rr_51_demo` (pacing / dificultad). Evento = marcador de onset cuando exista. |
| **Entrega sumativa parcial (30 % del portfolio)** | Informe dual 2–3 páginas: métricas, p_surr, panel clásico, frase *prohibida* vs *permitida*, hash. |
| **Criterio de éxito** | Ningún claim de “alarma de FV” o dispositivo; madurez CCTP explicitada. |

### Semana 5 — Transferencia de dominio (un solo dominio no-cardio)

| Elemento | Contenido |
|----------|-----------|
| **Objetivos** | Reutilizar la gramática τ_s/RECD en **un** dominio de transferencia; contrastar madurez empírica y jerga; justificar el preset. |
| **Elección (uno)** | `dengue_like_demo` (epi) · `eeg_like_demo` (neuro) · `ecology_like_demo` · `climate_drought_demo` · `education_cohort_demo` · `sleep_fragmentation_demo` · `social_polarization_demo` · `finance_like_demo` (**solo** transferencia metodológica; **prohibido** claim de trading). |
| **Teoría** | Ficha del dominio en Dominios + lente de dominio en Fundamentos (ejemplos situados). |
| **Lab** | Preset del dominio; Fast o Full según carga; n_surr documentado. |
| **Entrega sumativa parcial (25 % del portfolio)** | Mini-informe de transferencia (1–2 págs.): qué es análogo al “evento”, qué proxy usó, qué **no** afirma. |
| **Criterio de éxito** | Madurez y límites del dominio elegidos son visibles en la conclusión. |

### Semana 6 — Surrogates, extensiones, ética, portfolio y peer review

| Elemento | Contenido |
|----------|-----------|
| **Objetivos** | Refinar nulos (phase-shuffle vs IAAFT); decidir si extensiones (breathing, TDA, memoria) aportan *contraste* sin sustituir el núcleo; entregar portfolio completo; peer review con rúbrica. |
| **Teoría** | Ética (repaso); handout *Extensiones*; FAQ de malentendidos (signo context-dependent, N=1, “¿predice…?”). |
| **Lab** | Re-análisis del caso de sem. 4 o 5 en modo Full opcional; export **MD + JSON + Methods**; checklist de análisis firmado. |
| **Entrega sumativa final (45 % del portfolio)** | Portfolio: (1) informe principal, (2) informe de transferencia o apéndice, (3) exports + hash, (4) checklist, (5) reflexión ética (½ pág.). |
| **Criterio de éxito** | Rúbrica §7 ≥ umbral; claims acotados; reproducibilidad verificable. |

---

## 6. Evaluación

### 6.0 Evaluaciones en la plataforma (auto-calificadas)

La app incluye la página **Evaluaciones** (`pages/9_Evaluaciones.py`):

- **Cuenta local** del estudiante (registro / login; progreso en `data/student_records/`, no SaaS).  
- **Quiz MCQ por módulo** (semanas 1–6), corrección automática, umbral por defecto **70 %**, reintentos con **mejor nota** conservada.  
- **Nota del curso ponderada** con los mismos pesos de §6.1 (formativas 5 %+5 %+5 %, S4 30 %, S5 25 %, S6 30 %).  
- **Seguimiento de entregables** (estado de ensayos/informes) y **registro de actividad**.  
- Checklist de la **Ruta de aprendizaje** se sincroniza con la cuenta si hay sesión.  
- Textos de cuenta, UI y banco de preguntas en **ES / EN / FR**.

Los quizzes **complementan** (no sustituyen) la rúbrica 0–2 del informe Lab (§6.2): el docente decide el peso relativo entre quiz automático y entregables cualitativos.

### 6.1 Estructura sugerida

| Componente | Peso | Momento |
|------------|------|---------|
| Formativas (sem. 1–3) | 15 % | Feedback rápido; quizzes S1–S3 en la app + ensayos |
| Informe dual cardio (sem. 4) | 30 % | Sumativo · quiz S4 + informe |
| Mini-informe transferencia (sem. 5) | 25 % | Sumativo · quiz S5 + mini-informe |
| Portfolio final + peer review (sem. 6) | 30 % | Sumativo (incluye 15 % peer si el docente lo activa) · quiz S6 |

*El docente puede colapsar 4+5+6 en un único portfolio (100 %) en cursos muy cortos.*

### 6.2 Rúbrica de la práctica Lab / informe (6 criterios × 0–2 = **12 puntos**)

| # | Criterio | 0 | 1 | 2 |
|---|----------|---|---|---|
| 1 | **Pregunta científica** | Ausente o confunde univariado/relacional | Pregunta clara pero sin evento/diseño | Pregunta relacional + corte/evento justificado |
| 2 | **Parámetros y preset** | Defaults sin justificación | Preset correcto, poca justificación de W/m/θ₃ | Preset + W/stride/m/θ₃/n_surr/seed documentados |
| 3 | **Métricas núcleo** | Faltan Δτ_s o excess3 | Reporta Δ pero sin p_surr ni contexto | Δτ_s, mean/Δ excess3, p_surr (o n_surr=0 declarado) |
| 4 | **EWS en paralelo** | No hay panel clásico | Menciona var/AR1 sin integrar | Lectura dual explícita (confirma / calla / contradice) |
| 5 | **Conclusión acotada** | Overclaim (clínico, trading, predicción) | Conclusión parcial con salvedades débiles | Claims alineados a madurez del dominio + frase de no-alcance |
| 6 | **Reproducibilidad** | Sin hash ni params | Hash **o** Methods incompletos | Hash + Methods + export usable por un par |

**Umbral de aprobación de la práctica:** ≥ **9 / 12**.  
**Excelente:** ≥ 11 / 12 y peer review útil (si aplica).

### 6.3 Frases de entrega (orientación)

| Permitidas (ejemplos) | Prohibidas en v1.0 del curso |
|----------------------|------------------------------|
| “Reorganización relacional significativa vs phase-shuffle en este diseño…” | “Predice la FV / el brote / el crash” |
| “Panel clásico ambiguo (var↑, AR1↓); el relacional se mueve en el approach…” | “Dispositivo de alarma clínica validado” |
| “Transferencia pedagógica a dengue-like; no nowcast operativo” | “Señal de trading / alpha” |
| “Demo con ground truth de switch; calibra la lectura dual” | “Prueba causal de polarización social real” |

---

## 7. Datasets del catálogo (v1.0)

### Controles (semanas 1–2)

| ID | Rol |
|----|-----|
| `synthetic_coupled_logistic` | Control **positivo** (switch de acoplamiento) |
| `synthetic_ar_noise` | Control **casi-nulo** / ruido |

### Ancla cardio (semana 4)

| ID | Rol |
|----|-----|
| `cardiac_like_demo` | Flujo CCTP sin depender de PhysioNet |
| `sddb_rr_38_demo` | Sample demo señal fuerte (si está en `data/samples/`) |
| `sddb_rr_51_demo` | Sample con pacing / mayor dificultad |

### Transferencia (semana 5) — elegir **uno**

| ID | Dominio |
|----|---------|
| `dengue_like_demo` | Epidemiología |
| `eeg_like_demo` | Neurociencia |
| `ecology_like_demo` | Ecología |
| `climate_drought_demo` | Clima / hidrología |
| `education_cohort_demo` | Aprendizaje colectivo |
| `sleep_fragmentation_demo` | Fisiología del sueño |
| `social_polarization_demo` | Dinámica social (juguete) |
| `finance_like_demo` | Finanzas (**solo** método; no trading) |

Los datos de terceros (p.ej. PhysioNet/SDDB) están sujetos a sus términos de uso.

---

## 8. Materiales y lecturas

### Packs descargables (página Materiales)

- **Pack estudiante:** guía rápida, teoría, matemática, cheatsheet, lectura dual, checklist, FAQ, ética.  
- **Pack docente:** syllabus (este documento), ética, manual, packs de teoría/lab, FAQ, glosario.  
- Individuales: Fundamentos compilados, extensiones TDA/breathing, dominio-specific sheets en la app.

### Lecturas científicas (docente selecciona 1–2)

- Trabajos / preprints del dominio CCTP y de EWS clásicas citados en **Evidencia**.  
- No sustituyen la práctica en el Lab.

### CLI (opcional, track avanzado)

```bash
stp analyze data.csv --domain cardiology -o report.md --json result.json
stp serve
```

---

## 9. Políticas del curso

### 9.1 Ética y alcance

- Obligatorio el handout *Ética y alcance del núcleo* antes de claims públicos o entregas sem. 4–6.  
- El software es de **investigación y docencia**, no producto clínico ni financiero regulado.  
- La **madurez empírica** es asimétrica: cardio (CCTP) > demos sintéticas de transferencia.

### 9.2 Integridad académica

- Los exports y hashes deben corresponder a corridas del estudiante (o equipo declarado).  
- Citar software STP y referencias de dominio usadas.  
- Prohibido presentar demos sintéticas como datos clínicos o de vigilancia reales sin etiquetarlas.

### 9.3 Trabajo en equipo

- Opcional en parejas (sem. 4–6); cada miembro debe poder explicar el Methods y el hash.  
- Peer review en sem. 6: rúbrica ciega o semi-ciega según el LMS.

### 9.4 Variantes de calendario

| Variante | Ajuste |
|----------|--------|
| **Intensivo 4 semanas** | Fusionar 1–2 y 5–6; un solo informe + transferencia breve. |
| **Seminario 8 semanas** | Añadir semana de paper discussion y semana de extensión TDA/breathing como contraste. |
| **Solo Lab workshop (2 días)** | Semanas 2–4 comprimidas; rúbrica reducida (criterios 3–6). |

---

## 10. Notas para el docente

1. **Pedagogía y falsación** antes que promesas de producto: celebre un control casi-nulo bien interpretado.  
2. Dedique tiempo explícito a **controles sintéticos** (sem. 2) antes del ancla cardio.  
3. En sem. 4, si no hay samples SDDB, `cardiac_like_demo` es suficiente para la competencia.  
4. Finanzas y social: enmarcar como **sandbox de gramática**, nunca como predicción.  
5. Extensiones (TDA, breathing, memoria): opt-in en Full; el claim principal sigue siendo τ_s + excess3 + dual + nulo.  
6. Use la **voz de dominio** (jerga en interpretación y Fundamentos) para transferir concepto sin cambiar la matemática.  
7. Evaluación: priorice la calidad del **acotamiento** del claim sobre la magnitud de Δ.  
8. Idioma: la app y los handouts existen en ES/EN/FR; elija un idioma de entrega por cohorte.

---

## 11. Citación sugerida

Si usa este syllabus y la plataforma en docencia o investigación, cite el software Academy Learning Tau / Systemic Tau Platform y las referencias científicas del dominio (p.ej. CCTP para cardio) listadas en la sección Evidencia de la app y en `CITATION.cff`.

---

## 12. Contacto y mejora continua

- Issues y feedback académico vía repositorio del proyecto.  
- Colaboración pedagógica / adapters de dominio: según README del repositorio.  
- Este syllabus es un **documento vivo**: alinee siempre IDs de datasets y presets con la versión instalada de STP.

---

*Syllabus STP v1.1 · Academy Learning Tau · uso académico con citación · no constituye consejo clínico, epidemiológico operativo ni financiero.*
