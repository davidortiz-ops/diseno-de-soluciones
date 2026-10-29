# Cálculo manual de contraste de color (sin herramientas)

Guía para calcular el ratio de contraste WCAG 2.2 usando solo la
fórmula matemática — no requiere Python ni ninguna herramienta externa.
Úsala en **Modo ID** cuando `check_contrast.py` no esté disponible.

---

## Fórmula completa (WCAG 2.2 — Understanding SC 1.4.3)

### Paso 1: Convertir hex a RGB lineal

Dado un color en hex `#RRGGBB`:

```
R_8bit = 0xRR  (0-255)
G_8bit = 0xGG  (0-255)
B_8bit = 0xBB  (0-255)

r = R_8bit / 255.0
g = G_8bit / 255.0
b = B_8bit / 255.0
```

Ejemplo: `#333333` → R=51, G=51, B=51 → r=0.2, g=0.2, b=0.2

### Paso 2: Corrección gamma (sRGB)

Para cada componente:

```
Si valor <= 0.04045:
  lineal = valor / 12.92
Si valor > 0.04045:
  lineal = ((valor + 0.055) / 1.055) ^ 2.4
```

### Paso 3: Luminancia relativa (L)

```
L = 0.2126 × R_lineal + 0.7152 × G_lineal + 0.0722 × B_lineal
```

Redondea a 4 decimales. La L siempre está entre 0 (negro puro) y 1 (blanco puro).

### Paso 4: Ratio de contraste

```
ratio = (L_más_claro + 0.05) / (L_más_oscuro + 0.05)
```

Redondea a 1 decimal (p. ej. 4.5:1).

---

## Umbrales de cumplimiento

| Tipo | AA | AAA |
|---|---|---|
| Texto normal (<18pt, o <14pt bold) | ≥ 4.5:1 | ≥ 7:1 |
| Texto grande (≥18pt, o ≥14pt bold) | ≥ 3:1 | ≥ 4.5:1 |
| Componentes UI, gráficos (1.4.11) | ≥ 3:1 | — |
| Contraste de borde de input, íconos | ≥ 3:1 | — |

---

## Ejemplo resuelto paso a paso

**Texto:** `#333333` sobre fondo `#FFFFFF`

**Paso 1 — RGB:**
- `#333333` → R=51, G=51, B=51 → r=0.2, g=0.2, b=0.2
- `#FFFFFF` → R=255, G=255, B=255 → r=1.0, g=1.0, b=1.0

**Paso 2 — Corrección gamma:**
- Texto: 0.2 > 0.04045 → ((0.2 + 0.055) / 1.055) ^ 2.4 ≈ 0.0214
- Fondo: 1.0 > 0.04045 → ((1.0 + 0.055) / 1.055) ^ 2.4 = 1.0

**Paso 3 — Luminancia:**
- L_texto = 0.2126×0.0214 + 0.7152×0.0214 + 0.0722×0.0214 = 0.0214
- L_fondo = 0.2126×1.0 + 0.7152×1.0 + 0.0722×1.0 = 1.0

**Paso 4 — Ratio:**
- ratio = (1.0 + 0.05) / (0.0214 + 0.05) = 1.05 / 0.0714 ≈ 14.7:1

**Resultado:** ✅ Cumple AA (4.5:1) y AAA (7:1) para texto normal.

---

## Casos comunes

| Texto | Fondo | Ratio | AA normal | AA grande | AAA normal |
|---|---|---|---|---|---|
| `#000000` | `#FFFFFF` | 21:1 | ✅ | ✅ | ✅ |
| `#333333` | `#FFFFFF` | 14.7:1 | ✅ | ✅ | ✅ |
| `#666666` | `#FFFFFF` | 5.7:1 | ✅ | ✅ | ❌ |
| `#999999` | `#FFFFFF` | 3.0:1 | ❌ | ✅ (justo) | ❌ |
| `#CCCCCC` | `#FFFFFF` | 1.6:1 | ❌ | ❌ | ❌ |
| `#FFFFFF` | `#003D7A` | 9.5:1 | ✅ | ✅ | ✅ |
| `#767676` | `#FFFFFF` | 4.0:1 | ❌ | ✅ | ❌ |

---

## Cómo documentar el hallazgo de contraste

En el reporte, cada hallazgo debe incluir:

```markdown
- Elemento: texto de tasas en tabla
- Color texto: #666666 | Color fondo: #FFFFFF
- Ratio calculado: 5.7:1
- Umbral requerido: 4.5:1 (AA texto normal)
- Cumple AA texto normal: ✅
- Cumple AAA texto normal: ❌ (necesita ≥ 7:1)
- Recomendación: cambiar texto a #4D4D4D (ratio 8.1:1 contra blanco)
```

---

## Referencia rápida: colores comunes y su luminancia

| Color | Hex | R 8-bit | L (aprox) |
|---|---|---|---|
| Blanco | `#FFFFFF` | 255 | 1.0000 |
| Gris claro | `#F5F5F5` | 245 | 0.8963 |
| Gris medio | `#CCCCCC` | 204 | 0.5734 |
| Gris | `#999999` | 153 | 0.3323 |
| Gris oscuro | `#666666` | 102 | 0.1517 |
| Casi negro | `#333333` | 51 | 0.0214 |
| Negro | `#000000` | 0 | 0.0000 |
| Azul Pragma | `#003D7A` | 0,61,122 | 0.0725 |
| Rojo error | `#B42318` | 180,35,24 | 0.0559 |
| Verde éxito | `#027A48` | 2,122,72 | 0.1445 |

---

> Esta guía reemplaza a `check_contrast.py` cuando no hay terminal
> disponible. Los valores calculados manualmente tienen precisión
> suficiente para fines de auditoría (±0.1 respecto al script).
