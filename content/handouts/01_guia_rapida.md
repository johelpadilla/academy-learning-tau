# Systemic Tau Platform — Guía rápida de arranque

| Campo | Valor |
|-------|--------|
| **Documento** | Handout 01 · Guía rápida |
| **Nivel** | Posgrado / especialización · primera sesión |
| **Tiempo estimado** | 15–25 minutos hasta el primer experimento documentado |
| **Plataforma** | Academy Learning Tau · STP v1.0 |
| **Versión del material** | 1.1 · 2026 |

---

## 1. Propósito científico (una frase)

Enseñar a **formular, calcular y documentar** un análisis de **reorganización relacional ordinal** — Systemic Tau (τ_s) + RECD/excess3 — en **lectura dual** con *early warning signals* (EWS) clásicas (varianza, AR(1)), bajo nulos de dependencia cruzada (surrogates) y con **reproducibilidad** (hash SHA-256).

**No es** un dispositivo clínico certificado, un sistema de alerta epidemiológica operativa, ni un motor de trading o scoring social.

---

## 2. Resultados de aprendizaje de esta guía

Al terminar la sesión de arranque, usted podrá:

1. Distinguir una pregunta **relacional** de una pregunta **solo univariada**.  
2. Ejecutar un control positivo y un control casi-nulo en el Laboratorio.  
3. Reportar Δτ_s, p_surr y al menos un EWS clásico en paralelo.  
4. Exportar Markdown + Methods + `repro_hash`.

---

## 3. Ruta en 5 pasos (UI)

| Paso | Dónde | Acción de posgrado |
|------|--------|--------------------|
| 1 | **Home** | Leer el alcance del núcleo: qué está listo, qué es extensión, qué no se reclama. |
| 2 | **Fundamentos** | τ_s vs EWS; RECD Φ₁–Φ₃; excess3; CSD como marco clásico. |
| 3 | **Matemática** | Sandbox Bandt–Pompe (m=3 → 6 símbolos); no salte el alfabeto ordinal. |
| 4 | **Laboratorio** | Catálogo → Analizar → lectura dual → Exportar. |
| 5 | **Evidencia / Biblioteca** | Ancla empírica CCTP/SDDB y corpus de publicaciones; no generalizar a ciegas. |

---

## 4. Primer experimento (protocolo mínimo)

1. Abra **Laboratorio**.  
2. Catálogo → `synthetic_coupled_logistic` (switch de acoplamiento con *ground truth* de diseño).  
3. Dominio **Sintético** · modo **Fast** · `n_surr` 4–8 · seed fija.  
4. Observe |Δτ_s| y p_surr; compare con el control `synthetic_ar_noise` (casi-nulo).  
5. Descargue el reporte **Markdown**, el párrafo **Methods** y copie el **repro_hash**.

**Preguntas de cierre (escriba 3–5 líneas):**

- ¿El Δ del logístico acoplado se mantiene extremo frente a *phase-shuffle*?  
- ¿El panel EWS (var/AR1) concuerda, calla o contradice?  
- ¿Qué claim **no** puede hacer con un demo sintético?

---

## 5. Controles mentales antes de interpretar

| Control | Por qué importa |
|---------|-----------------|
| N ≥ 2 (o proxy RR + \|ΔRR\| documentado) | El núcleo es relacional |
| Preset de dominio antes de retocar W | Evita *p-hacking* de ventana |
| Lectura dual obligatoria | Un solo panel no basta |
| p_surr + tamaño de efecto | Nunca publique solo el p |
| Signo *context-dependent* | Subir o bajar puede ser reorganización real |
| Madurez del dominio | Demo ≠ cohorte; cardio ≠ clima |

---

## 6. Mapa de materiales descargables

| Documento | Uso en el curso |
|-----------|-----------------|
| Manual de usuario | Operación Lab + CLI |
| Teoría τ_s + RECD | Marco conceptual de posgrado |
| Matemática práctica | Notación, Bandt–Pompe, nulos |
| Cheat-sheet del Lab | Presets y frases permitidas |
| Lectura dual | Plantillas de informe |
| Checklist | Entrega / autoevaluación /12 |
| Syllabus 6 semanas | Diseño del curso y rúbrica |
| Ética y alcance | Claims honestos |
| Extensiones (Breathing / TDA) | Complemento, no sustituto del núcleo |
| FAQ + Glosario | Malentendidos de revisión por pares |

---

## 7. CLI (opcional)

```bash
stp serve
stp analyze datos.csv --domain cardiology -o reporte.md --json resultado.json
```

---

## 8. Citación mínima de una corrida

1. Software: Systemic Tau Platform v1.0.  
2. Dataset (catálogo ID o fuente original).  
3. Paper/preprint de dominio si aplica.  
4. `repro_hash` de la corrida citada.

---

*Material docente STP v1.1 · uso académico con citación · no sustituye validación externa ni revisión ética institucional.*
