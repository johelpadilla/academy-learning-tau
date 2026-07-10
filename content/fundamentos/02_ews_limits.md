# Fundamentos — EWS clásicas y sus límites

| Campo | Valor |
|-------|--------|
| **Módulo** | Fundamentos 02 |
| **Nivel** | Posgrado |
| **Versión** | 1.1 · 2026 |

---

## Resultados de aprendizaje

1. Definir varianza y AR(1) como señales tempranas clásicas.  
2. Enunciar al menos tres modos de falla de EWS solo univariadas.  
3. Explicar por qué la lectura dual es obligatoria, no opcional.

---

## 1. Marco clásico (CSD)

El *critical slowing down* (CSD) sugiere que cerca de ciertas bifurcaciones el sistema se recupera más lento de perturbaciones. Empíricamente suele aparecer como:

- **varianza** creciente en ventana;  
- **autocorrelación lag-1** (coeficiente AR(1)) creciente;  
- a veces otros indicadores univariados.

Siguen siendo **controles valiosos**. STP no los descarta.

---

## 2. Límites que motivan τ_s

| Límite | Consecuencia |
|--------|--------------|
| Enfoque univariado | Pierde reorganización pura de acoplamiento |
| Ambigüedad de signo | La varianza sube por muchas razones no críticas |
| Transiciones multivariadas | Los canales locales pueden no “enlentecerse” |
| Proceso de observación | Ruido, muestreo, no estacionariedad |
| Tentación de umbral | Lenguaje de “alerta” sin validación externa |

---

## 3. Regla pedagógica

En el Lab STP:

- Siempre calcule **EWS clásicas en paralelo**.  
- Nunca oculte un panel clásico incómodo.  
- Declare concordancia, discordancia o quietud.

---

## 4. Micro-lab

En `synthetic_coupled_logistic` y `synthetic_ar_noise`, compare var/AR1 vs Δτ_s. Escriba cuatro líneas de lectura dual.

---

*Fundamentos 02 · STP v1.1*
