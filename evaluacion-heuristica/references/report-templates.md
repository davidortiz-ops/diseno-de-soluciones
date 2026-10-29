# Plantillas de Reporte

Lee este archivo cuando necesites generar un reporte estructurado. Usa la plantilla completa para evaluaciones formales o la plantilla ejecutiva para auditorías rápidas.

---

## Plantilla Completa

Usa esta plantilla para evaluaciones formales que se compartirán con stakeholders.

```markdown
# Reporte de Evaluación Heurística

## 1. Resumen Ejecutivo

| Ítem | Detalle |
|---|---|
| **Producto evaluado** | [Nombre del sitio/app] |
| **URL / Versión** | [URL o versión] |
| **Industria** | [Banca / Retail / Otro] |
| **Alcance** | [Página específica / Flujo completo / Sitio completo] |
| **Fecha de evaluación** | [DD/MM/AAAA] |
| **Evaluador(es)** | [Nombre(s)] |
| **Total de hallazgos** | [N] |

**Score Global de Usabilidad: [X]/10**
- Críticos (severidad 4): [N]
- Mayores (severidad 3): [N]
- Menores (severidad 2): [N]
- Cosméticos (severidad 1): [N]

**3-5 Problemas Críticos:**
1. [Hallazgo 1]
2. [Hallazgo 2]
3. [Hallazgo 3]
4. [Hallazgo 4]
5. [Hallazgo 5]

**Recomendaciones Prioritarias:**
1. [Recomendación 1]
2. [Recomendación 2]
3. [Recomendación 3]

---

## 2. Análisis Detallado por Heurística

### H1: Visibilidad del Estado del Sistema
- **Severidad:** [0-4] | **Hallazgos:** [N]
- [Detalle de cada hallazgo]

### H2: Coincidencia entre Sistema y Mundo Real
- **Severidad:** [0-4] | **Hallazgos:** [N]
- [Detalle de cada hallazgo]

### H3: Control y Libertad del Usuario
...

### H4: Consistencia y Estándares
...

### H5: Prevención de Errores
...

### H6: Reconocimiento antes que Recuerdo
...

### H7: Flexibilidad y Eficiencia de Uso
...

### H8: Diseño Estético y Minimalista
...

### H9: Ayuda a Reconocer, Diagnosticar y Recuperarse de Errores
...

### H10: Ayuda y Documentación
...

[Si aplica: H11-H14 según industria]

---

## 3. Tabla de Hallazgos Consolidada

| # | Heurística | Severidad | Título | Ubicación | Impacto | Recomendación | Esfuerzo |
|---|---|---|---|---|---|---|---|
| 1 | H1 | 3 | Título del hallazgo | [dónde ocurre] | [descripción del impacto] | [qué hacer] | [Pequeño/Medio/Grande] |
| 2 | H3 | 4 | ... | ... | ... | ... | ... |

---

## 4. Matriz de Priorización (Impacto vs Esfuerzo)

### Quick Wins (Alto Impacto, Bajo Esfuerzo)
- [Hallazgos # que caen aquí]

### Major Projects (Alto Impacto, Alto Esfuerzo)
- [Hallazgos # que caen aquí]

### Fill-ins (Bajo Impacto, Bajo Esfuerzo)
- [Hallazgos # que caen aquí]

### Thankless (Bajo Impacto, Alto Esfuerzo)
- [Hallazgos # que caen aquí]

---

## 5. Roadmap de Implementación

### Fase 1 — Quick Wins (Inmediato, < 1 semana)
- [Hallazgo #]: [Acción]
- [Hallazgo #]: [Acción]

### Fase 2 — Corto Plazo (1-4 semanas)
- [Hallazgo #]: [Acción]
- [Hallazgo #]: [Acción]

### Fase 3 — Mediano Plazo (1-3 meses)
- [Hallazgo #]: [Acción]
- [Hallazgo #]: [Acción]

### Fase 4 — Estratégico (3+ meses)
- [Hallazgo #]: [Acción]
- [Hallazgo #]: [Acción]

---

## 6. Aspectos Positivos
1. [Buen ejemplo de práctica detectado]
2. [Buen ejemplo de práctica detectado]

---

## 7. Checklist de Cumplimiento

### Accesibilidad WCAG
- [ ] Contraste de color >= 4.5:1
- [ ] Navegación por teclado funcional
- [ ] Etiquetas en formularios
- [ ] Texto alternativo en imágenes

### Regulatorio (si aplica)
- [ ] Términos y condiciones visibles
- [ ] Política de privacidad accesible
- [ ] Costos y comisiones transparentes
- [ ] Registros de autorización visibles
```

---

## Plantilla Ejecutiva (Rápida)

Usa esta plantilla para evaluaciones rápidas o iterativas.

```markdown
# Evaluación Heurística — [Nombre]
**Industria:** [Banca/Retail] | **Alcance:** [página/flujo] | **Score:** [X]/10

## Top Hallazgos
| Severidad | Heurística | Problema | Recomendación |
|---|---|---|---|
| 4 | H# | ... | ... |
| 3 | H# | ... | ... |

## Quick Wins (Fase 1)
- [Acción concreta]
- [Acción concreta]

## Próximos Pasos
1. [Acción inmediata]
2. [Acción siguiente]
```
