# Fundamentos — Tau Sistémica (τ_s)

| Campo | Valor |
|-------|--------|
| **Módulo** | Fundamentos 01 |
| **Nivel** | Posgrado |
| **Versión** | 1.1 · 2026 |
| **Handouts relacionados** | Teoría · Matemática práctica · Lectura dual |

---

## Resultados de aprendizaje

1. Enunciar la pregunta científica de τ_s en una frase sin “predecir”.  
2. Contrastar la medición ordinal–relacional con amplitud/enlentecimiento univariado.  
3. Listar los elementos de diseño (N, W, evento, nulos) para un Δτ_s defendible.

---

## 1. Objeto científico

**Tau Sistémica (τ_s)** mide cómo se reorganiza en el tiempo la **estructura de orden compartida** entre variables de un sistema multivariado. No pregunta principalmente cuánto fluctúa cada canal, sino cómo cambian las **relaciones de orden** entre canales en torno a un cambio de régimen.

Operativamente (pipeline educativo Lab v1.0):

1. Serie multivariada \(X\in\mathbb{R}^{T\times N}\) (o proxy bivariado documentado).  
2. Ventanas deslizantes de longitud \(W\) con paso `stride`.  
3. Patrones ordinales locales (Bandt–Pompe / rangos).  
4. Resumen de coherencia ordinal cruzada → \(\tau_s(t)\).  
5. Contraste Δ (pre/post evento o mitad/mitad) bajo nulos de surrogates.

---

## 2. ¿Por qué ordinal y relacional?

| Propiedad | Implicación |
|-----------|-------------|
| Ordinal | Robusto a transformaciones estrictamente monótonas |
| Relacional | Apunta a reorganización de acoplamiento, no solo CSD univariado |
| En ventanas | Captura dinámica, no un único coeficiente estático |
| Con nulos | Phase-shuffle evalúa estructura cruzada residual |

---

## 3. Qué no es τ_s

- No es un reetiquetado de marketing del Kendall-τ estático.  
- No es Transfer Entropy (predicción direccional).  
- No es un predictor certificado de eventos clínicos o de mercado.  
- No sustituye la teoría de dominio.

---

## 4. Lectura práctica de τ_s

Siempre con:

1. Tamaño de efecto (magnitud y signo de Δτ_s).  
2. Panel EWS clásico (lectura dual).  
3. p_surr + método + n_surr + seed.  
4. Declaración de madurez del dominio.  
5. `repro_hash`.

**Signo context-dependent:** subir o bajar τ_s puede indicar reorganización según el régimen.

---

## 5. Micro-chequeo

- [ ] Explico τ_s sin reclamar predicción.  
- [ ] Sé por qué se exige N≥2 (o proxy).  
- [ ] No publicaré p sin Δ y diseño.

---

*Fundamentos 01 · STP v1.1*
