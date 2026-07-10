# Dominio: Fisiología del sueño — fragmentación circadiana

### Objetivos de aprendizaje
1. Extender la intuición cardio (RR) a una triada sueño: HRV · actividad · temperatura.
2. Ver un cambio de **driver** (circadiano limpio → fragmentación de alta frecuencia).
3. Comparar madurez: cardiología CCTP es el ancla; sueño es puente fisiológico.

**Madurez empírica en v1.0:** ★★★☆☆ — demo sintético alineado con ideas de arquitectura del sueño.

---

## 1. Contexto

La arquitectura del sueño coordina variables autonómicas y conductuales. Cuando el driver circadiano se fragmenta, no solo “hay más ruido”: las **relaciones ordinales** entre HRV, actividad y temperatura se reorganizan.

## 2. Relación con cardiología

- Cardiología (CCTP/SDDB) aporta la cohorte de referencia de la plataforma.
- Sueño ofrece un segundo sistema fisiológico para practicar el mismo lenguaje sin mezclar claims clínicos.

## 3. Dataset

- `sleep_fragmentation_demo` — evento de fragmentación marcado (~70 %).

## 4. Madurez

Media — pedagógica y de transferencia; no dispositivo médico ni scoring clínico de sueño.

---

## Ficha de diseño (esquema uniforme)

| Campo | Valor |
|-------|--------|
| **Proxy** | \(X=[\mathrm{HRV}, \mathrm{actividad}, \mathrm{temp}]\) |
| **Evento** | Onset de fragmentación circadiana (~70 % de la serie) |
| **Preset Lab** | `physiology` · Fast para docencia |
| **Demos** | `sleep_fragmentation_demo` |
| **Madurez** | Media — transferencia fisiológica pedagógica |

### Frases permitidas
- Reorganización relacional bajo fragmentación de sueño diseñada…
- No es dispositivo médico de scoring de sueño.

### Frases prohibidas (v1.0)
- Diagnóstico clínico de sueño
- Claim de dispositivo médico
