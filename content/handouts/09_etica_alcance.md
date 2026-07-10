# Ética, alcance del núcleo y uso responsable

| Campo | Valor |
|-------|--------|
| **Documento** | Handout 09 · Ética y alcance |
| **Audiencia** | Todo usuario · obligatorio antes de claims públicos |
| **Versión** | 1.1 · 2026 |
| **Colocación en el curso** | Semana 1 y relectura en semana 6 |

---

## Resultados de aprendizaje

1. Enunciar para qué existe STP y qué no es.  
2. Separar claims del núcleo de extensiones del Lab.  
3. Mapear la fuerza de claims a la madurez empírica.  
4. Citar correctamente software, datos, paper de dominio y hash.

---

## 1. Para qué existe STP

Systemic Tau Platform es software de **investigación y docencia** para:

- enseñar la gramática τ_s + RECD frente a EWS clásicas;  
- reproducir demos y análisis con hash;  
- transferir el método entre dominios con madurez explícita.

No es, en v1.0:

- un dispositivo médico certificado;  
- un sistema de alerta epidemiológica operativa;  
- un motor de trading o scoring social;  
- un sustituto de validación externa ni de revisión ética institucional.

---

## 2. Alcance del núcleo técnico (v1.0)

### Listo para enseñar y explorar

- Pipeline completo τ_s + RECD/excess3 + EWS + surrogates + repro_hash  
- Lab, presets, catálogo de demos, export MD/JSON/Methods  
- Fundamentos, matemática, dominios, evidencia CCTP demo  
- CLI `stp analyze` / `stp serve`  
- Catálogo de biblioteca de investigación (ruta local de publicaciones)

### Extensiones operativas del Lab vs horizonte de producto

**Ya operativas en el Lab** (casillas / modo Full; no son el claim principal):

- Breathing window (W adaptativa para τ_s)  
- TDA / Betti en ventanas (ripser opcional o VR skeleton)  
- Memoria ordinal (MI simbólica)

**Horizonte / no bloquee una tesis en ellos como núcleo:**

- TDA multi-escala de producción con pipelines de persistencia exhaustivos  
- TE simbólica / causalidad como producto  
- Backends de facturación o “planes” comerciales  

Si el núcleo ya responde la pregunta del estudiante, use extensiones como **contraste**, no como sustituto.

---

## 3. Madurez empírica y honestidad de claims

| Claim | ¿Cuándo es aceptable? |
|-------|------------------------|
| “En este demo sintético, Δτ_s es extremo vs phase-shuffle” | Siempre, con hash y diseño |
| “En sample SDDB demo, el panel relacional se mueve así…” | Con salvedades de sample y N |
| “El piloto CCTP sugiere ventaja relacional vs EWS ambiguas” | Citando el trabajo de dominio y límites de N |
| “Predice FV / brote / crisis de mercado / polarización real” | **No** en v1.0 sin validación externa y gobernanza |

**Regla:** la fuerza del ancla cardiológica **no** se exporta automáticamente a clima, aula o finanzas.

---

## 4. Datos de terceros

- PhysioNet / SDDB: cumplan ToS y citación PhysioNet.  
- Cualquier CSV clínico o educativo real: consentimiento, anonimización, IRB/ética local.  
- Demos generados en plataforma: licencia “generated in-platform”; no son mediciones de campo.  
- Archivos de biblioteca de investigación: respete licencias de origen; rutas locales pueden contener material no publicado — trátelo en consecuencia.

---

## 5. Docencia y evaluación

- Evalúe **proceso** (diseño, nulos, lectura dual, límites), no solo un p-valor bajo.  
- Premie el uso de **controles** (logísticos vs AR).  
- Penalice promesas comerciales o clínicas sin base.  
- Conserve hashes de entregas para integridad académica.  
- Enseñe a escribir **no-claims** con la misma claridad que los claims.

---

## 6. Citación mínima recomendada

1. Software: Systemic Tau Platform v1.0 (y dependencias alineadas del paradigma).  
2. Paper/preprint del **dominio** analizado.  
3. Dataset original.  
4. `repro_hash` de la corrida si reporta números concretos.

---

## 7. Contacto institucional / comercial

Usos comerciales o institucionales más allá del uso académico local pueden requerir licencia aparte. Eso **no** limita el aprendizaje con el código y demos locales del curso.

---

## 8. Árbol de decisión antes de una frase pública

1. ¿El objeto es un demo, un sample piloto o datos externos?  
2. ¿El claim es sobre reorganización bajo un diseño declarado — o sobre predicción?  
3. ¿Están presentes panel dual + nulo + hash?  
4. ¿Un experto de dominio aceptaría el enunciado de madurez?

Si alguna respuesta es débil, reescriba la frase.

---

*Handout de ética y alcance STP v1.1 · leer en semana 1 y releer en semana 6.*
