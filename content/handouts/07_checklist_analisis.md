# Checklist de análisis — entrega Lab / informe corto

| Campo | Valor |
|-------|--------|
| **Documento** | Handout 07 · Checklist de análisis |
| **Uso** | Marque cada ítem antes de enviar; si N/A, justifique en una línea |
| **Puntuación** | Autoevaluación opcional /12 alineada a la rúbrica de lectura dual |
| **Versión** | 1.1 · 2026 |

---

## A. Pregunta y alcance

- [ ] Pregunta científica en una frase (reorganización relacional, no “predecir X”)  
- [ ] Dominio y **madurez empírica** declarados  
- [ ] Se distingue demo sintético vs datos reales  
- [ ] Límites éticos (no clínico / no operativo) mencionados  
- [ ] Métodos complementarios vs competidores enunciados si aplica (p.ej. TE no sustituida en silencio)

## B. Datos

- [ ] Fuente (catálogo ID / CSV / PhysioNet / …)  
- [ ] Dimensiones T × N  
- [ ] Variables usadas y por qué (adapter / teoría)  
- [ ] Preprocess (z-score, proxy RR–|ΔRR|, missing, ties)  
- [ ] Licencia / ToS de terceros respetada  
- [ ] Nota de anonimización / IRB si datos humanos fuera de demos

## C. Diseño

- [ ] Evento marcado **o** partición exploratoria declarada  
- [ ] Preset de dominio o justificación de W, stride, m, θ₃  
- [ ] Seed de surrogates fijada  
- [ ] Modo fast/full y n_surr acordes al claim  
- [ ] Sin caza de evento *post hoc* no declarada

## D. Resultados numéricos

- [ ] Δτ_s (signo + magnitud)  
- [ ] mean_excess3 y Δexcess3  
- [ ] p_surr y método (phase-shuffle / IAAFT)  
- [ ] Al menos un EWS clásico en paralelo  
- [ ] Figuras: series+evento, τ_s, RECD/excess3, EWS  
- [ ] Extensiones (si se usan): rango W y/o β₀/β₁ + backend

## E. Interpretación

- [ ] Lectura dual (concordancia / discordancia / quietud)  
- [ ] No se sobreinterpreta Φ₃ si excess3 es la señal  
- [ ] Signo context-dependent considerado  
- [ ] Comparación con control (AR o basal) si aplica  
- [ ] Claims acotados al diseño y la madurez

## F. Reproducibilidad y entrega

- [ ] `repro_hash` copiado  
- [ ] Export Markdown  
- [ ] Export JSON (si el curso lo pide)  
- [ ] Párrafo Methods  
- [ ] Citas: software + dataset + paper de dominio  

---

## Autoevaluación (opcional)

| Criterio (0–2) | Nota |
|----------------|------|
| Pregunta y alcance | |
| Datos y diseño | |
| Métricas + nulos | |
| Lectura dual | |
| Escritura acotada | |
| Hash / exports | |
| **Total /12** | |

**Guía:** ≥9 para una entrega Lab sólida; 12 solo si está completa y honesta sobre límites.

---

## Controles rápidos del docente (3 preguntas)

1. ¿Puede el estudiante re-correr y recuperar el hash?  
2. ¿Es correcta la categoría de claim (demo / piloto / transferencia)?  
3. ¿Un revisor entendería lo que **no** se reclamó?

---

*Checklist STP v1.1 · imprimible*
