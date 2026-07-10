# Teoría — Tau Sistémica, RECD y lectura dual

| Campo | Valor |
|-------|--------|
| **Documento** | Handout 03 · Teoría |
| **Audiencia** | Posgrado · docentes · lectores de papers del paradigma |
| **Uso** | Complementa Fundamentos en la app; imprimible / LMS |
| **Versión** | 1.1 · 2026 |
| **Prerrequisitos** | Series temporales intermedias; correlación y procesos |

---

## Resultados de aprendizaje

1. Enunciar la **pregunta relacional** de τ_s frente a la pregunta univariada de las EWS.  
2. Describir el pipeline ventana → patrones ordinales → τ_s(t) → RECD/excess3.  
3. Interpretar p_surr bajo *phase-shuffle* sin reducir la evidencia a un único p-valor.  
4. Aplicar **lectura dual** (concordancia / discordancia / quietud).  
5. Acotar claims según **madurez empírica** del dominio.

---

## 1. La pregunta científica

Las *early warning signals* (EWS) clásicas, motivadas por *critical slowing down* (CSD; Scheffer et al.), preguntan en lo esencial:

> ¿Cuánto se mueve cada variable? ¿Se vuelve más lenta la recuperación ante perturbaciones?

**Tau Sistémica (τ_s)** pregunta otra cosa:

> **¿Cómo se reorganiza la estructura de orden compartida entre las variables del sistema en torno a un cambio de régimen?**

En sistemas vivos y socio-ecológicos, la transición suele ser un **cambio de ley relacional** (acoplamiento, sinergia, hábitos de co-orden), no solo un enlentecimiento univariado. Por eso τ_s es **ordinal** y **relacional**.

### 1.1 Qué no es τ_s

| Confusión frecuente | Aclaración de posgrado |
|---------------------|------------------------|
| “Es Kendall-τ con marketing” | Comparte sustrato de rangos, pero opera en **ventanas**, es multivariado, se acopla al reloj RECD y se interpreta con nulos de dependencia cruzada. |
| “Es causalidad / Transfer Entropy” | TE pregunta predicción direccional A→B. τ_s pregunta reorganización de estructura conjunta. Son **complementarios**. |
| “Predice muerte / brote / crisis” | Marco de **investigación y docencia**. No es dispositivo certificado ni alerta operativa. |
| “Sustituye la fisiología / la epidemiología” | Aporta un **observable de acoplamiento**; no reemplaza el conocimiento de dominio. |

---

## 2. Observables, ventana y definición operativa

Sea \(X \in \mathbb{R}^{T \times N}\) con \(N \ge 2\) (o un proxy bivariado legítimo, p.ej. \(z(\mathrm{RR}),\, z(|\Delta\mathrm{RR}|)\) en el patrón CCTP).

En una ventana de longitud \(W\) con paso `stride`:

1. Se construyen **patrones de orden** locales (Bandt–Pompe / rangos) con \(m\) y \(\tau\).  
2. Se resume la **coherencia ordinal cruzada** en un escalar \(\tau_s(t)\).  
3. La trayectoria \(\tau_s(t)\) puede acelerar, invertirse o estabilizarse cuando el sistema se reorganiza — **no necesariamente** cuando sube la varianza univariada.

**Definición pedagógica (v1.0 Lab):** \(\tau_s\) se relaciona con un resumen (p.ej. media de coeficientes de rango por pares en ventana) de la estructura ordinal compartida. El claim científico se juega en la **dinámica de reorganización** (Δ, nulos, dual reading), no en un único coeficiente estático.

### 2.1 Parámetros típicos (presets v1.0)

| Dominio | W | stride | θ₃ (orientativo) | Nota |
|---------|---|--------|------------------|------|
| Cardiología | 101 | 5 | 0.08 | Ancla empírica CCTP |
| Epidemiología | 13 | 1 | 0.10 | Series a menudo cortas |
| Neurociencia / sueño | 51 | 2 | 0.10 | Multi-canal |
| Ecología | 25 | 1 | 0.10 | Transferencia metodológica |
| Clima / social / finanzas | 21 | 1 | 0.10 | Sandbox / madurez baja–media |
| Educación (cohorte) | 17 | 1 | 0.10 | Meta-pedagógico |
| Sintético | 31 | 2 | 0.10 | Controles de diseño |

Documente siempre W, stride, m, delay y θ₃; el **repro_hash** los sella.

---

## 3. RECD — reloj extramental discreto

**RECD** formaliza un tiempo emergente del sistema (**Kairos**) distinto del índice del CSV (**Chronos**).

### 3.1 Niveles de conjunción ordinal

| Nivel | Idea formal-intuitiva | Trampa de interpretación |
|-------|----------------------|--------------------------|
| **Φ₁** | Coincidencia de símbolos entre pares en \(t\) | Alto Φ₁ ≠ “emergencia” |
| **Φ₂** | Persistencia de relaciones de a pares (≥ \(d\) pasos; típ. d=4) | Hábito relacional, no destello |
| **Φ₃** | Indicador binario de sinergia sobre umbral θ₃ | En ruido puede quedarse en 0 |
| **excess3** | Proxy **continuo** de sinergia irreducible | Métrica primaria en regímenes ruidosos (CCTP) |

En datos reales, **mean_excess3** y **Δexcess3** suelen ser más informativos que el bit Φ₃.

El avance del reloj (ΔRECD) se modula por la intensidad de reorganización \(\lambda\) (en la práctica ligada a \(|\tau_s|\) y al régimen).

### 3.2 Chronos vs Kairos

| Concepto | Definición operativa en STP |
|----------|----------------------------|
| Chronos | Índice temporal del muestreo (fila del CSV) |
| Kairos | Tiempo ponderado por ticks de reorganización (RECD) |

No confunda “el evento está en t=500” (Chronos) con “el reloj del sistema aceleró” (Kairos).

---

## 4. Surrogates — el nulo relacional

Pregunta: *¿el Δ observado es compatible con independencia cruzada preservando espectros univariados?*

| Método | Qué preserva | Qué rompe | Uso v1.0 |
|--------|--------------|-----------|----------|
| **Phase-shuffle** (default) | Espectro por canal (aprox.) | Dependencia cruzada | Nulo natural relacional |
| **IAAFT** (opcional) | Espectro + histograma (iterativo) | Dependencia cruzada (más estricto) | Modo full / sensibilidad |

### 4.1 Lectura conjunta efecto × nulo

| Δ (efecto) | p_surr | Lectura de posgrado |
|------------|--------|---------------------|
| Grande | Bajo (p.ej. ≤0.05) | Candidato a estructura relacional residual |
| Grande | Alto | No reclame detección; revise W, preprocess, N |
| Pequeño | Bajo | Efecto pequeño pero estable — cautela de dominio |
| Pequeño | Alto | Compatible con nulo; útil como **control** |

**Nunca** publique solo el p-valor sin tamaño de efecto, diseño, n_surr, seed y madurez del dominio.

---

## 5. Lectura dual (obligatoria)

Todo resultado serio se presenta en **dos columnas**:

1. **Panel relacional:** τ_s, RECD, excess3, p_surr.  
2. **Panel clásico:** var, AR(1) u otras EWS univariadas en el mismo diseño.

### 5.1 Por qué es metodológicamente necesario

- Las EWS clásicas pueden ser ambiguas cuando la transición es multivariada.  
- τ_s puede moverse cuando var/AR1 no “alertan” — y al revés.  
- La ciencia útil declara **concordancia, discordancia o quietud**.

### 5.2 Signo *context-dependent*

Δτ_s o Δexcess3 pueden **subir o bajar** hacia un evento según el régimen. La evidencia se juega en magnitud, concordancia, nulos y narrativa de dominio — no en un letrero universal “positivo = malo”.

---

## 6. Madurez empírica (v1.0)

| Nivel | Dominios / materiales | Implicación para claims |
|-------|----------------------|-------------------------|
| **Ancla** | Cardiología CCTP / SDDB (piloto documentado) | Claims más fuertes, aún de investigación; N limitado |
| **Transferencia** | Epidemiología (narrativa + demos) | Hipótesis transferibles; validar fuera |
| **Sandbox pedagógico** | Clima, educación, social, sueño, finanzas, sintéticos | Ground truth de **diseño**; enseñan el método |

**Regla de oro:** no venda la fuerza del piloto cardio como validación de polarización social o de trading.

---

## 7. Reproducibilidad y citación

Cada corrida del Lab genera un **repro_hash** (SHA-256). Para citar un número:

1. Paper/preprint del dominio.  
2. Software (STP v1.0 / librerías alineadas).  
3. Dataset original y licencia.  
4. Hash de la corrida + Methods exportados.

---

## 8. Glosario mínimo

| Término | Definición operativa |
|---------|---------------------|
| **τ_s** | Termómetro de reorganización relacional ordinal en ventanas |
| **RECD** | Reloj de ticks de reorganización (Kairos) |
| **excess3** | Sinergia ordinal continua (primario en ruido) |
| **Bandt–Pompe** | Alfabeto de m! patrones de orden (m=3 → 6) |
| **EWS** | Señales tempranas univariadas (panel de control) |
| **CSD** | *Critical slowing down* (marco clásico) |
| **p_surr** | Extremo del Δ bajo nulo de surrogates |

---

## 9. Lecturas de contexto (no exhaustivo)

- Bandt, C. & Pompe, B. — *Permutation entropy* / ordinal patterns.  
- Scheffer, M. et al. — critical transitions / CSD / EWS.  
- Literatura de nulos espectrales (phase randomization) y IAAFT.  
- Papers/preprints del dominio (p.ej. CCTP).  
- Documentación de datasets (PhysioNet SDDB, etc.).

---

## 10. Auto-chequeo teórico (5 ítems)

1. ¿Puedo enunciar la pregunta de τ_s sin la palabra “predice”?  
2. ¿Sé por qué excess3 puede importar más que Φ₃?  
3. ¿Qué rompe el phase-shuffle y qué preserva?  
4. ¿Qué es una discordancia relacional–clásica legítima?  
5. ¿Qué claim **no** puedo hacer con un demo sintético?

---

*Handout teórico STP v1.1 · complementa la app · uso académico con citación.*
