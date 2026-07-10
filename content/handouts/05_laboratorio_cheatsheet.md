# Cheat-sheet del Laboratorio STP

| Campo | Valor |
|-------|--------|
| **Documento** | Handout 05 · Cheat-sheet Lab |
| **Uso** | Imprimir a una cara · tener al lado del monitor en clase |
| **Nivel** | Operación de laboratorio de posgrado |
| **Versión** | 1.1 · 2026 |

---

## Flujo

```
Datos (catálogo | CSV) → Dominio + evento → Parámetros → Analizar
    → Series · τ_s · RECD · EWS · Extensiones (BW/TDA) · lectura dual
    → Export MD/JSON/Methods + hash
```

**Extensiones (operativas):** casillas Breathing / TDA / Memoria — activas por defecto en modo **Full**.

---

## Presets (W / stride / θ₃)

| Dominio | W | stride | θ₃ |
|---------|---|--------|-----|
| Cardiología | 101 | 5 | 0.08 |
| Epidemiología | 13 | 1 | 0.10 |
| Neuro / sueño | 51 | 2 | 0.10 |
| Ecología | 25 | 1 | 0.10 |
| Clima / social / finanzas | 21 | 1 | 0.10 |
| Educación | 17 | 1 | 0.10 |
| Sintético | 31 | 2 | 0.10 |

m=3, delay=1 por defecto en v1.0. Documente cualquier desvío.

---

## Demos que debe conocer el estudiante

| ID | Para qué |
|----|----------|
| `synthetic_coupled_logistic` | Señal fuerte (control positivo) |
| `synthetic_ar_noise` | Casi-nulo (control negativo) |
| `sddb_rr_38_demo` | Ancla cardio (si el sample está) |
| `dengue_like_demo` | Transferencia epi |
| `education_cohort_demo` | Meta-pedagógico |
| `climate_drought_demo` | CSD climático de juguete |

---

## Lectura rápida de salidas

| Salida | Pregunta que responde |
|--------|----------------------|
| τ_s(t) | ¿Cuándo se reorganiza el acoplamiento ordinal? |
| Δτ_s | ¿Cuánto cambió pre/post (o mitad/mitad)? |
| excess3 / Δ | ¿Hay sinergia irreducible en movimiento? |
| Φ₃ | ¿Cruzó el umbral? (puede quedarse en 0) |
| p_surr | ¿El Δ es extremo bajo nulo de independencia cruzada? |
| var / AR1 | ¿El panel clásico cuenta la misma historia? |
| W(t) | Resolución breathing (si activo) |
| β₀ / β₁ | Proxy topológico del cloud de estados (si TDA) |
| hash | ¿Puedo regenerar esta corrida? |

---

## Surrogates (orientativo)

| Uso | n_surr |
|-----|--------|
| Demo en clase | 4–8 |
| Exploración seria | 20–50 |
| A citar | ≥50 + sensibilidad a seed |

Default: **phase_shuffle**. IAAFT si necesita nulo más estricto (más lento).

---

## Export mínimo de una entrega

1. `reporte.md`  
2. `resultado.json`  
3. Párrafo Methods  
4. Hash copiado en el PDF/LMS  
5. Párrafo de lectura dual (Handout 06)

---

## Frases prohibidas (sin evidencia)

- “Predice la muerte súbita / el brote / el crash.”  
- “p<0.05 luego el sistema colapsa.”  
- “Finanzas demo ⇒ estrategia de trading.”  
- “Polarización demo ⇒ verdad social.”  
- “El piloto CCTP valida clima / aula.”

---

## Frases permitidas (con matices)

- “Δτ_s = …; p_surr = … bajo phase-shuffle (n=…, seed=…).”  
- “El panel EWS fue ambiguo/concordante en ….”  
- “Demo sintético con ground truth de diseño; no cohorte clínica.”  
- “Madurez del dominio: …; extrapolar requiere validación externa.”  
- “Métrica continua primaria: mean_excess3 / Δexcess3 (Φ₃ se quedó en 0).”

---

## Atajos mentales de calidad

1. ¿Control positivo y negativo en la misma sesión?  
2. ¿Evento declarado (o mitad/mitad exploratoria)?  
3. ¿Preset o W justificada?  
4. ¿Lectura dual escrita?  
5. ¿Hash + Methods presentes?  
6. ¿Claims acotados por madurez?

Si falla uno, la entrega no está lista.

---

*STP Lab cheat-sheet v1.1*
