# Extensiones operativas — Breathing Window y TDA / Betti

| Campo | Valor |
|-------|--------|
| **Documento** | Handout 10 · Extensiones |
| **Audiencia** | Estudiantes de Lab (semanas 3–6) y docentes |
| **Estado** | **Operativo** en el Lab STP (no “en desarrollo”) |
| **Rol** | Extensión pedagógica del núcleo τ_s + RECD + EWS + surrogates |
| **Versión** | 1.1 · 2026 |

---

## Resultados de aprendizaje

1. Separar el **claim del núcleo** del **contraste de extensión**.  
2. Interpretar W(t) adaptativa sin inventar acoplamiento.  
3. Reportar β₀/β₁ con el backend correcto (`ripser` vs `vr_skeleton`).  
4. Mantener claims de nivel tesis sobre el núcleo de lectura dual ordinal.

---

## 1. Mensaje clave

| Capa | Componentes | ¿Claim principal? |
|------|-------------|-------------------|
| **Núcleo** | τ_s, RECD/excess3, EWS clásicas, surrogates, hash | Sí |
| **Extensiones** | Breathing window, TDA β₀/β₁, memoria ordinal | Complemento / contraste |

El Lab **no depende** de TDA ni breathing para funcionar. Cuando se activan, aparecen en la pestaña **Extensiones**, en el reporte y en Methods.

---

## 2. Breathing window

### Idea

En regímenes volátiles, una W fija grande **suaviza de más** la transición.  
Breathing mapea la **volatilidad local** a un tamaño de ventana impar:

- alta volatilidad → **W más corta** (más reactivo)  
- régimen estable → **W más larga** (más suave)

### Cómo usarlo en el Lab

1. Active **Breathing window** (por defecto en Full).  
2. Ejecute.  
3. Pestaña **Extensiones** o eje secundario en τ_s: serie **W(t)**.  
4. Documente el rango W observado (p.ej. W∈[21–101]).

### Lectura honesta

Breathing cambia la **resolución temporal** de τ_s. No inventa acoplamiento: si el control AR sigue plano, no force una narrativa.

### Reporte

Declare: activado/desactivado, rango W observado, y si el Δ primario usó W fija o breathing.

---

## 3. TDA / Betti en ventanas

### Idea

En cada ventana se construye un **point cloud** (delay embedding multivariado) y se resumen números de Betti:

- **β₀** — componentes conexas (¿el cloud se fragmenta o se unifica?)  
- **β₁** — ciclos (estructura “con agujeros” / 1-esqueleto)

### Backends

| Backend | Cuándo | Notas |
|---------|--------|-------|
| **ripser** | Si `pip install systemic-tau-platform[tda]` | Persistencia clásica |
| **VR 1-skeleton** | Siempre (fallback) | β₀ = componentes; β₁ = \|E\|−\|V\|+β₀ |

Ambos son **proxies pedagógicos** de topología del estado. No son un pipeline TDA de producción multi-escala.

### Cómo usarlo en el Lab

1. Active **TDA / Betti**.  
2. Ejecute (cuesta más que solo τ_s; use Fast + TDA en demos cortos o Full).  
3. Pestaña **Extensiones**: curvas β₀(t), β₁(t) + marcador de evento.  
4. Métricas: mean/Δ β₀, β₁ y `tda_backend` en el JSON/reporte.

### Lectura dual ampliada

| Pregunta | Herramienta |
|----------|-------------|
| ¿Se reorganiza el orden compartido? | τ_s, excess3 |
| ¿El panel univariado se mueve? | var / AR1 |
| ¿El cloud de estados cambia de topología? | β₀ / β₁ |
| ¿El Δ relacional es residual bajo nulo cruzado? | p_surr |

**No** reemplace la columna relacional por TDA. Use TDA para **contrastar**.

---

## 4. Memoria ordinal (breve)

MI simbólica lag-1 y cross-MI estiman **persistencia de información ordinal**.  
Repórtela como extensión; no la trate como grafo causal.

---

## 5. CLI

```bash
# Extensiones on (también default en --mode full)
stp analyze data.csv --domain synthetic --breathing --tda -o report.md --json out.json

stp analyze data.csv --mode full -o report.md
```

---

## 6. Checklist de entrega con extensiones

- [ ] Claim principal basado en τ_s / excess3 / p_surr (+ EWS)  
- [ ] Breathing/TDA declarados como extensión  
- [ ] Backend TDA reportado (`ripser` o `vr_skeleton`)  
- [ ] Rango W si breathing  
- [ ] Hash de la corrida  
- [ ] Sin promesas clínicas/operativas basadas solo en β₁  

---

## 7. Errores frecuentes

| Error | Corrección |
|-------|------------|
| “TDA aún no está listo” | Está operativo como extensión; actualice la app |
| Publicar solo β₁ | Añada lectura dual del núcleo |
| Confundir fallback VR con ripser multi-escala | Cite el backend |
| Activar TDA en series enormes sin subsample | Use modo Fast o demos del catálogo |
| Tratar cambios de W breathing como “prueba de acoplamiento” | Resolución ≠ estructura |

---

## 8. Consejo de nivel tesis

Un capítulo de tesis defendible:

1. Lidera con lectura dual relacional + nulos.  
2. Usa extensiones en una subsección de **sensibilidad / contraste**.  
3. Declara versiones de software y backends.  
4. Mantiene la madurez del dominio explícita.

---

*Handout extensiones STP v1.1 · Breathing + TDA operativos en el Lab*
