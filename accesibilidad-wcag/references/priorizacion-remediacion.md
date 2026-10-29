# Priorización de remediación

Matriz para ordenar los hallazgos por urgencia de corrección combinando
**severidad**, **esfuerzo** y **riesgo legal**.

## Dimensiones

### Severidad (impacto en el usuario)

| Nivel | Valor | Descripción |
|---|---|---|
| Alta | 3 | Impide el uso (botón sin nombre, navegación rota, trampa de foco) |
| Media | 2 | Afecta parcialmente pero hay alternativa (contraste bajo, orden de lectura) |
| Baja | 1 | Detalle menor (foco poco visible, ARIA innecesario) |

### Riesgo legal (exposición normativa)

| Nivel | Valor | Descripción |
|---|---|---|
| Alto | 3 | Incumple norma con sanción directa (Circular SFC, Estatuto Consumidor) |
| Medio | 2 | Incumple marco general (Ley 1618/1346) sin sanción inmediata |
| Bajo | 1 | Buena práctica sin obligación normativa explícita |

### Esfuerzo (costo de corrección — se invierte en la fórmula)

| Nivel | Valor de esfuerzo | Valor invertido | Descripción |
|---|---|---|---|
| Bajo | <1 día | 3 | Cambio de atributo, texto, color |
| Medio | 1-3 días | 2 | Cambio de componente o patrón |
| Alto | >1 semana | 1 | Cambio de arquitectura, librería o de terceros |

> El esfuerzo se **invierte** (bajo esfuerzo = 3 puntos) para que, a igual
> impacto, las correcciones rápidas suban en prioridad ("quick wins").

## Fórmula de puntuación compuesta

```
Puntaje = (Severidad × 3) + (Riesgo legal × 2) + (Esfuerzo invertido)
```

Rango posible: mínimo 6, máximo 18.

## Rangos de prioridad

| Puntaje | Prioridad | Tiempo sugerido |
|---|---|---|
| 15-18 | **Crítico** | Resolver en < 1 semana |
| 10-14 | **Alta** | Sprint actual |
| 7-9 | **Media** | Siguiente sprint |
| 6 | **Baja** | Backlog / mejora continua |

## Ejemplo de cálculo — Banca

**Hallazgo:** El login bancario usa CAPTCHA visual sin alternativa (SC
1.1.1, 3.3.8).

- Severidad: Alta (3) — bloquea el acceso de usuarios ciegos.
- Riesgo legal: Alto (3) — incumple Circular SFC y Ley 1680.
- Esfuerzo: Bajo (invertido 3) — habilitar reCAPTCHA con audio/alternativa.

```
Puntaje = (3 × 3) + (3 × 2) + 3 = 9 + 6 + 3 = 18 → CRÍTICO
```

## Ejemplo de cálculo — Retail

**Hallazgo:** Carrusel de productos en home sin botón de pausa (SC 2.2.2).

- Severidad: Media (2) — distrae y dificulta, pero el catálogo es accesible
  por otras vías.
- Riesgo legal: Medio (2) — marco general sin sanción inmediata.
- Esfuerzo: Bajo (invertido 3) — agregar control de pausa.

```
Puntaje = (2 × 3) + (2 × 2) + 3 = 6 + 4 + 3 = 13 → ALTA
```

## Guía de estimación de esfuerzo

Para clasificar el esfuerzo, considera:

- **Cambio de atributo/contenido** (alt, label, lang, contraste de token):
  esfuerzo **bajo**.
- **Cambio de componente UI** (refactor de un modal, formulario o tabla):
  esfuerzo **medio**.
- **Cambio de librería o framework** (reemplazar un date-picker
  inaccesible): esfuerzo **medio-alto**.
- **Cambio de arquitectura** (reorganizar el DOM, rehacer un flujo
  completo): esfuerzo **alto**.
- **Dependencia de terceros** (pasarela de pago, core bancario, chat
  embebido): esfuerzo **alto** + gestión externa; documentar como riesgo
  de Conformance Requirement 5.

Factores que suben el esfuerzo: necesidad de re-validar con AT, impacto en
múltiples plantillas, dependencias entre equipos, y pruebas de regresión.
