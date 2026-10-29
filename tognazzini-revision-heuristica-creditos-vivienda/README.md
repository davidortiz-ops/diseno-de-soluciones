# Tognazzini — Revisión Heurística para Créditos de Vivienda

Skill de auditoría de experiencia de usuario basado en las **16 heurísticas de Bruce Tognazzini**, aplicado al proceso de **crédito de vivienda convencional y especial**. Diseñado para investigadores de UX, diseñadores de servicios, analistas de experiencia de cliente y product managers de banca hipotecaria.

Versión 2.0 · People Center Design · Pragma

---

## ¿Qué hace?

Evalúa la experiencia completa de una persona que solicita, gestiona o hace seguimiento a un crédito de vivienda — no solo la interfaz digital, sino también los puntos de contacto no digitales (asesor comercial, abogado, notaría, TINSA, aseguradora). Aplica las 16 heurísticas de Tognazzini, documenta cada hallazgo con **Gravedad** y **Dificultad de solución** (0-3 cada una), calcula un promedio de prioridad por hallazgo y una Puntuación General de experiencia, y agrupa las recomendaciones en quick wins, medianas y estructurales.

**Tres entregables:**

- **Reporte completo** — tabla de hallazgos ordenada por prioridad, matriz de priorización, roadmap en 4 fases, checklist normativo y resumen ejecutivo.
- **Reporte ejecutivo** — una página con Puntuación General, top hallazgos críticos y quick wins.
- **Puntuación y ranking vía script** — cálculo reproducible desde un JSON de hallazgos (modo CLI).

---

## ¿Cómo funciona?

El skill sigue un **workflow de seis pasos**:

1. **Contexto** — Define tipo de crédito (convencional/especial), canales involucrados, alcance y evidencia disponible.
2. **Recolección de evidencia** — Reúne capturas, grabaciones, el paso a paso narrado del proceso y quejas o PQR previas.
3. **Evaluación** — Recorre las 16 heurísticas dando mayor peso a las 5 prioritarias (retroalimentación inmediata, prevención de errores, claridad del flujo temporal, compatibilidad entre canales y satisfacción emocional), documentando cada hallazgo con Gravedad y Dificultad.
4. **Cálculo de prioridad** — Aplica `Promedio total = (Gravedad + Dificultad) / 2` y ordena los hallazgos de mayor a menor.
5. **Matriz y roadmap** — Clasifica los hallazgos en Quick Wins, Medianas o Estructurales según su Dificultad, y organiza la implementación en 4 fases.
6. **Reporte** — Genera el entregable en el formato seleccionado, con resumen ejecutivo y recomendaciones agrupadas.

---

## ¿Para qué usarlo?

| Rol | Aplicación |
|---|---|
| **UX Researcher** | Identificar fricciones en el proceso de crédito hipotecario de forma sistemática, incluyendo canales presenciales que suelen quedar fuera de las auditorías digitales. |
| **Diseñador de servicios** | Validar que el proceso completo (solicitud → aprobación → desembolso → postventa) sea coherente entre lo digital y lo presencial. |
| **Analista de experiencia de cliente** | Cuantificar la calidad de la experiencia del solicitante y detectar patrones transversales de fricción o desconfianza. |
| **Product Manager de banca hipotecaria** | Priorizar inversión en UX con datos: hallazgos documentados por Gravedad, Dificultad y heurística violada. |
| **Consultor en experiencia digital** | Emitir diagnósticos y hojas de ruta para procesos financieros de alto monto y múltiples actores. |

---

## ¿Cómo se usa?

### Claude Desktop / .ai

1. Abre el skill en el asistente AI.
2. Solicita una evaluación. Ejemplos:
   - _"Evalúa heurísticamente el flujo de solicitud de crédito de vivienda en Conectados"_
   - _"Analiza la experiencia completa del crédito hipotecario especial, desde la solicitud hasta la notaría"_
3. El skill te guiará con preguntas de contexto, ejecutará la evaluación y entregará el reporte.

### Claude Code (CLI)

Además del flujo anterior, puedes usar los scripts incluidos para automatizar el cálculo:

```bash
# 1. Prepara tu archivo de hallazgos (usa el template como guía)
cp scripts/findings_template.json mis-hallazgos.json

# 2. Edita mis-hallazgos.json con tus hallazgos

# 3. Valida que el JSON cumpla el esquema
python scripts/validate_findings.py mis-hallazgos.json

# 4. Calcula la Puntuación General y el ranking
python scripts/calculate_score.py mis-hallazgos.json

# 5. Genera el reporte markdown completo
python scripts/generate_report.py mis-hallazgos.json --output reporte.md

# O el ejecutivo
python scripts/generate_report.py mis-hallazgos.json --template ejecutiva --output reporte-ejecutivo.md
```

No requiere instalación previa más allá de Python 3.

### Modos de ejecución

| Característica | Modo CLI | Modo ID |
|---|---|---|
| Entorno | Terminal disponible (Claude Code) | Sin terminal (Claude Desktop / .ai) |
| Cálculo de Puntuación General | Automático con `calculate_score.py` | El modelo aplica la fórmula manualmente |
| Validación de hallazgos | `validate_findings.py` | Revisión visual del modelo |
| Reportes | Se guardan en archivos `.md` | Se entregan dentro de la conversación |
| Ideal para | Perfiles técnicos, integración con otros procesos | Investigadores, diseñadores, PMs |

No necesitas elegir un modo. El skill lo detecta al iniciar la evaluación.

---

## ¿Cuándo usarlo?

- Al diseñar o rediseñar el flujo de solicitud, aprobación o desembolso de crédito de vivienda.
- Antes de lanzar cambios en Conectados, Bizagi o SAP relacionados con crédito hipotecario.
- Al recibir quejas o PQR recurrentes sobre incertidumbre en el estado del crédito.
- En auditorías periódicas del proceso completo (al menos semestral).
- Al evaluar la coherencia entre el trabajo del asesor comercial y los canales digitales.
- Como insumo para priorizar el roadmap de mejora de la experiencia hipotecaria.

---

## Estructura

```
tognazzini-revision-heuristica-creditos-vivienda/
├── SKILL.md                    # Lógica principal del skill (16 heurísticas, 6 pasos)
├── evals/
│   └── evals.json              # Pruebas de calidad
├── scripts/                    # Herramientas de cálculo (solo modo CLI)
│   ├── calculate_score.py      # Puntuación General y ranking desde JSON
│   ├── generate_report.py      # Generación de reporte markdown (completo/ejecutivo)
│   ├── validate_findings.py    # Validador de esquema JSON
│   ├── findings_template.json  # Template para documentar hallazgos
│   └── sample-findings.json    # Ejemplo completo de hallazgos
├── README.md                   # Este archivo
└── LICENSE                     # Licencia de uso
```

---

## Referencias del skill

Este skill es autocontenido: las 16 heurísticas con sus preguntas evaluables, la escala de Gravedad/Dificultad, la matriz de priorización y el checklist normativo viven directamente en `SKILL.md`. No requiere `references/` adicionales.

### Scripts

| Script | Propósito | Uso |
|---|---|---|
| `calculate_score.py` | Calcula la Puntuación General, la distribución por grupo de priorización y el ranking de hallazgos | `python calculate_score.py hallazgos.json` |
| `generate_report.py` | Genera el reporte markdown completo o ejecutivo | `python generate_report.py hallazgos.json --output reporte.md` |
| `validate_findings.py` | Valida que el JSON cumpla el esquema esperado por los otros scripts | `python validate_findings.py hallazgos.json --strict` |

---

## Alcances

- Evalúa el proceso de crédito de vivienda convencional y especial de extremo a extremo: solicitud, aprobación, desembolso y postventa.
- Cubre canales digitales (Conectados, Bizagi, SAP, correo) y no digitales (asesor comercial, abogado, notaría, TINSA, aseguradora).
- Aplica las 16 heurísticas de Bruce Tognazzini, con peso adicional a las 5 más relevantes para crédito de vivienda.
- Escala dual Gravedad (0-3) y Dificultad (0-3), con fórmula de prioridad y Puntuación General 0-10.
- Incluye checklist normativo colombiano orientativo: Ley 546 (vivienda), Ley 1328 (consumidor financiero), Ley 1581 (datos personales), Circular 029 (seguridad).
- Matriz de priorización en 3 grupos (Quick wins, Medianas, Estructurales) y roadmap en 4 fases.
- No requiere instalación; los scripts son opcionales y solo aplican en modo CLI.

## Limitaciones

- La evaluación se basa en la evidencia y descripción que el usuario proporcione. Sin acceso a capturas, grabaciones o un paso a paso detallado, el análisis de los puntos de contacto presenciales (notaría, TINSA, aseguradora) queda limitado a lo narrado.
- La Gravedad y la Dificultad asignadas a cada hallazgo reflejan el criterio del evaluador. Para decisiones críticas o de alto costo, se recomienda validar con datos operativos (tiempos reales por etapa, volumen de PQR).
- El checklist normativo es un mapa de referencia, no asesoría legal ni notarial; la normativa citada debe verificarse en su versión vigente.
- No evalúa métricas cuantitativas de negocio (tasa de conversión, tiempo de aprobación real). Es un método cualitativo de inspección heurística.
- Para normativa de países distintos a Colombia, el skill pregunta al usuario en vez de asumir equivalencias.

---

## Licencia

Propiedad de **Pragma**. Uso interno y confidencial — ver `LICENSE`.
