# Matemática práctica — Bandt–Pompe, τ_s y RECD

| Campo | Valor |
|-------|--------|
| **Documento** | Handout 04 · Matemática práctica |
| **Audiencia** | Quien ya leyó la guía rápida; sandbox de Matemática / Lab |
| **Objetivo** | Calcular e interpretar sin saltarse el alfabeto ordinal |
| **Nivel** | Métodos cuantitativos de posgrado |
| **Versión** | 1.1 · 2026 |

---

## Resultados de aprendizaje

1. Construir símbolos Bandt–Pompe para m=3 y explicar la invariancia monótona.  
2. Enunciar el pipeline operativo de \(X\) a τ_s y RECD/excess3.  
3. Describir phase-shuffle como nulo de dependencia cruzada.  
4. Completar el checklist numérico antes de cualquier claim público.

---

## 1. Orden de aprendizaje (no salte pasos)

| # | Bloque | Una frase | Dónde |
|---|--------|-----------|--------|
| 1 | Bandt–Pompe | m! patrones de orden local | Matemática (sandbox) |
| 2 | τ_s | Termómetro relacional en ventanas | Lab |
| 3 | Φ₁–Φ₃ + excess3 | Reloj anidado y sinergia | Fundamentos + Lab |
| 4 | EWS clásicas | Panel univariado de control | Lab |
| 5 | Surrogates | Nulos de dependencia cruzada | Lab (`n_surr`) |
| 6 | Breathing / memoria / TDA | Extensiones operativas del Lab | Lab · modo Full |

**Regla:** si no puede dibujar Bandt–Pompe en una pizarra, no interprete excess3.

---

## 2. Notación

| Símbolo | Significado | Típico v1.0 |
|---------|-------------|-------------|
| \(X\in\mathbb{R}^{T\times N}\) | Serie multivariada | N≥2 |
| \(m,\tau\) | Dimensión y delay ordinal | m=3, delay=1 |
| \(W\), stride | Ventana y paso | ver presets |
| \(\Phi_1,\Phi_2,\Phi_3\) | Niveles de conjunción | [0,1] / binario |
| excess3 | Sinergia continua | primario en ruido |
| \(\theta_3\) | Umbral de Φ₃ | 0.08 cardio; ~0.10 otros |
| \(\lambda\) | Intensidad de reorganización | ligada a \|τ_s\| |
| p_surr | p de surrogate para Δ | reporte método + n |

---

## 3. Bandt–Pompe en 90 segundos

Para una ventana de \(m\) puntos con delay \(\tau\):

1. Tome \(x_t, x_{t+\tau},\ldots,x_{t+(m-1)\tau}\).  
2. Ordene los valores: el **patrón de rangos** es un símbolo en \(\{0,\ldots,m!-1\}\).  
3. Con \(m=3\) hay **6** símbolos.

### Propiedad clave

Invariancia a transformaciones **estrictamente monótonas**. Tras un preprocess honesto, el paradigma es robusto a escalas distintas entre canales.

### Ejercicio de pizarra

Serie: `3, 1, 4, 2` con m=3, delay=1.

- Tripleta (3,1,4) → patrón de permutación.  
- Tripleta (1,4,2) → otro símbolo.  
Cuente frecuencias en una ventana más larga en el sandbox de la app.

### Empates (ties)

Defina y reporte una política de desempate. Ties no documentados son un defecto de métodos.

---

## 4. De símbolos a τ_s (intuición operativa)

1. Cada canal se simboliza (Bandt–Pompe).  
2. En la ventana se mide **coherencia / reorganización** entre canales.  
3. Se obtiene \(\tau_s(t)\) a lo largo del tiempo.  
4. Con un **evento** marcado se calcula Δ pre/post; si no, 1ª vs 2ª mitad (declare diseño exploratorio).

### Controles mentales

- **Control positivo:** logísticos acoplados con switch → |Δτ_s| grande.  
- **Control casi-nulo:** AR independientes → |Δτ_s| pequeño.  
- Si su demo “aplicado” se parece al AR, no force una narrativa de reorganización.

---

## 5. RECD y excess3 (fórmulas en palabras)

### Φ₁
Fracción normalizada de pares con el **mismo símbolo** en t. Base estadística; insuficiente sola.

### Φ₂
Relaciones de a pares que **persisten** al menos \(d\) pasos (típico d=4). Hábitos, no destellos.

### excess3
Proxy continuo de **sinergia irreducible**. Alimenta la decisión de Φ₃.

### Φ₃
1 si excess3 > θ₃; 0 si no. En series ruidosas puede quedarse apagado mientras excess3 se mueve: **reporte el continuo**.

### ΔRECD
Acumulación de ticks de reorganización modulados por el régimen. Opera Chronos vs Kairos.

---

## 6. Surrogates — matemática del nulo

**Phase-shuffle independiente por canal**

1. FFT del canal.  
2. Aleatorizar fases.  
3. IFFT → misma densidad espectral aproximada, dependencia cruzada destruida.

Si el Δ de los datos es extremo respecto a la distribución de Δ en surrogates, p_surr es bajo: evidencia de que la estructura **cruzada** importa.

**IAAFT** itera para ajustar también el histograma de amplitudes; más costoso; útil en modo full.

### Estándar de reporte

Método, n_surr, seed, qué Δ se contrastó (τ_s y/o excess3), política uni/bilateral si aplica.

---

## 7. Checklist numérico antes de un claim

- [ ] N ≥ 2 (o proxy documentado)  
- [ ] W y stride justificados  
- [ ] m, delay fijados y reportados  
- [ ] Evento o partición exploratoria **declarada**  
- [ ] Δτ_s y Δexcess3 con signo y magnitud  
- [ ] p_surr con n_surr y método  
- [ ] Panel EWS en paralelo  
- [ ] Hash y Methods exportados  

---

## 8. Errores matemáticos frecuentes

| Error | Corrección |
|-------|------------|
| Interpretar τ_s como correlación de Pearson | Es ordinal–relacional en ventanas |
| Publicar solo Φ₃ | Preferir excess3 + Φ₃ |
| n_surr = 2 para un paper | Usar decenas y sensibilidad a seed |
| Comparar dominios con W distintos sin decirlo | La escala temporal del reloj cambia |
| Tratar demos sintéticos como cohorte | Ground truth de diseño ≠ evidencia de campo |
| Ocultar política de ties / missing | Métodos incompletos |

---

## 9. Complejidad (orden de magnitud)

| Bloque | Orden de coste |
|--------|----------------|
| Bandt–Pompe univariado | \(O(T \cdot m \log m)\) (m=3 barato) |
| Φ₁ | \(O(T \cdot N^2)\) |
| Φ₂ | \(O(T \cdot N^2 \cdot d)\) |
| excess3 | crece con ventanas de conteo; N pequeño y m=3 factible |
| Surrogates | × n_surr el coste de la métrica |

---

## 10. Fast vs Full (política numérica)

| Bloque | Fast (docencia / exploración) | Full (paper-like) |
|--------|-------------------------------|-------------------|
| τ_s + RECD | Sí | Sí |
| EWS clásicas | Sí | Sí |
| Surrogates | n≈8 | n≥50 (recomendado) |
| TDA Betti | Opcional | Sí (default Full) |
| Breathing | Opcional | Sí (default Full) |

**Regla:** explore en Fast; confirme en Full antes de citar un p-valor.

---

*Handout de matemática práctica STP v1.1 · usar junto al sandbox de Matemática.*
