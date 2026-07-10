# Dominio: Sistemas complejos / Finanzas — regímenes de volatilidad

## 1. Contexto

Los mercados exhiben **cambios de régimen de volatilidad**, contagio y sincronización de activos. Aunque no son “sistemas vivos” en sentido biológico, comparten la estructura de **transiciones de acoplamiento** en series multivariadas.

## 2. EWS y métricas clásicas

- Volatilidad realizada, VIX, correlaciones rolling de retornos.
- Buenas para descripción; a menudo **reactivas**.
- ML de régimen (HMM, etc.) predice sin ofrecer descomposición ordinal interpretable tipo Φ₁–Φ₃.

## 3. Aporte Tau + RECD

- Proxy: \(X = [z(r_t), z(\sigma_t^{\mathrm{RV}})]\) o multi-activo de rangos.
- Detectar **co-ordenación de patrones de retorno/vol** antes de regímenes de estrés.
- Ejercicio avanzado de transferibilidad del paradigma.

## 4. Disclaimer

**No es consejo de inversión.** Uso estrictamente educativo y de investigación metodológica.

## 5. Madurez

**Media** — dominio opcional avanzado en la ruta de aprendizaje.

## 6. Sample

- S&P 500 diario + realized vol 21d (últimos años).

---

## Ficha de diseño (esquema uniforme)

| Campo | Valor |
|-------|--------|
| **Proxy** | \(X=[z(r_t), z(\sigma_t^{\mathrm{RV}})]\) |
| **Evento** | Cambio de régimen de volatilidad / onset de estrés |
| **Preset Lab** | `finance` · solo transferencia metodológica |
| **Demos** | `finance_like_demo` |
| **Madurez** | Media — avanzado opcional; **no consejo de inversión** |

### Frases permitidas
- Transferencia metodológica del acoplamiento ordinal a un demo de régimen de vol…
- Uso estrictamente educativo / de investigación metodológica.

### Frases prohibidas (v1.0)
- Señal de trading / alpha / consejo de inversión
- Sistema de trading algorítmico certificado
