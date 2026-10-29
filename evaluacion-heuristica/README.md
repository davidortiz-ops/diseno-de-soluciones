# Heuristy — Evaluación Heurística para Banca y Retail

Skill de auditoría de usabilidad basada en las **10 heurísticas de Nielsen**, con extensiones sectoriales para **banca** y **retail**. Diseñado para investigadores de UX, diseñadores de servicios, analistas de experiencia de cliente y product managers.

Versión 2.0 · People Center Design · Pragma

---

## ¿Qué hace?

Realiza evaluaciones heurísticas de interfaces digitales (web, móvil, desktop) siguiendo el método de Jakob Nielsen. Evalúa una URL o un flujo completo contra las 10 heurísticas de usabilidad (H1-H10) más 4 extensiones por industria (H11-H14), documenta cada hallazgo con severidad 0-4, los prioriza en una matriz Impacto vs Esfuerzo, y genera un reporte estructurado con score global y roadmap de implementación.

**Tres entregables:**

- **Reporte completo** — análisis detallado por heurística, tabla de hallazgos, matriz de priorización, roadmap 4 fases, aspectos positivos y checklist de cumplimiento.
- **Reporte ejecutivo** — resumen de una página para liderazgo con score global, top problemas críticos y quick wins.
- **Reporte HTML** — versión auto-contenida del reporte completo, listo para compartir con stakeholders sin necesidad de herramientas adicionales.

---

## ¿Cómo funciona?

El skill sigue un **workflow de seis pasos**:

1. **Contexto** — Define producto, industria, alcance, flujos críticos, usuarios objetivo y normativa aplicable.
2. **Selección de plantilla** — Escoge la batería de heurísticas según la industria: banca (H1-H14 + normativa Colombia), retail (H1-H14) o genérico (H1-H10).
3. **Evaluación** — Recorre la interfaz heurística por heurística respondiendo preguntas evaluables y documentando cada hallazgo con severidad 0-4 y ubicación precisa.
4. **Cálculo de score** — Aplica la fórmula `Score = 10 - promedio(severidad)` e interpreta el resultado.
5. **Matriz y roadmap** — Clasifica hallazgos en Quick Wins, Major Projects, Fill-ins y Thankless según impacto y esfuerzo.
6. **Reporte** — Genera el entregable en el formato seleccionado.

---

## ¿Para qué usarlo?

| Rol | Aplicación |
|---|---|
| **UX Researcher** | Identificar problemas de usabilidad de forma sistemática antes de pruebas con usuarios. Complementar sesiones de test con una visión estructurada. |
| **Diseñador de servicios** | Validar que los flujos completos (registro, transferencia, checkout) sean intuitivos y sin fricciones. |
| **Analista de experiencia de cliente** | Cuantificar la calidad de usabilidad del producto y medir su evolución entre versiones. |
| **Product Manager** | Priorizar inversión en UX con datos concretos: hallazgos documentados por severidad, impacto en el usuario y esfuerzo estimado. |
| **Consultor en experiencia digital** | Emitir diagnósticos de usabilidad, preparar auditorías y recomendar hojas de ruta de mejora. |

---

## ¿Cómo se usa?

### Claude Desktop / .ai

1. Abre el skill en el asistente AI.
2. Solicita una evaluación. Ejemplos:
   - _"Evalúa heurísticamente el flujo de login de [URL]"_
   - _"Haz una evaluación ejecutiva del checkout de [URL] para retail"_
   - _"Revisa la accesibilidad del flujo de transferencias de [URL], incluye normativa colombiana"_
3. El skill te guiará con preguntas de contexto, ejecutará la evaluación y entregará el reporte.

### Claude Code (CLI)

Además del flujo anterior, puedes usar los scripts incluidos para automatizar partes del proceso:

```bash
# 1. Prepara tu archivo de hallazjos (usa el template como guía)
cp scripts/findings_template.json mis-hallazgos.json

# 2. Edita mis-hallazgos.json con tus hallazgos

# 3. Valida que el JSON cumpla el esquema
python scripts/validate_findings.py mis-hallazgos.json

# 4. Calcula el score global
python scripts/calculate_score.py mis-hallazgos.json

# 5. Genera el reporte markdown completo
python scripts/generate_report.py mis-hallazgos.json --output reporte.md

# O el ejecutivo
python scripts/generate_report.py mis-hallazgos.json --template ejecutiva --output reporte-ejecutivo.md

# 6. Genera el reporte HTML para compartir
python scripts/generate_html_report.py mis-hallazgos.json --output reporte.html
```

No requiere instalación previa más allá de Python 3.

### Modos de ejecución

| Característica | Modo CLI | Modo ID |
|---|---|---|
| Entorno | Terminal disponible (Claude Code) | Sin terminal (Claude Desktop / .ai) |
| Cálculo de score | Automático con scripts Python | El modelo aplica la fórmula manualmente |
| Validación de hallazgos | `validate_findings.py` | Revisión visual del modelo |
| Reportes | Se guardan en archivos (.md, .html) | Se entregan dentro de la conversación |
| HTML compartible | `generate_html_report.py` | Conversión manual del markdown |
| Ideal para | Perfiles técnicos, integración continua | Investigadores, diseñadores, PMs |

No necesitas elegir un modo. El skill lo detecta al iniciar la auditoría.

---

## ¿Cuándo usarlo?

- Antes de lanzar un producto o funcionalidad
- En cada sprint o ciclo de desarrollo (evaluaciones iterativas)
- Durante rediseños de flujos existentes
- Al recibir un requerimiento regulatorio (banca: SFC, protección al consumidor)
- En auditorías periódicas (al menos semestral)
- Al evaluar productos de terceros o proveedores
- Como paso previo a pruebas de usabilidad con usuarios

---

## Estructura

```
evaluacion-heuristica/
├── SKILL.md                             # Lógica principal del skill (6 pasos)
├── heuristy-evaluacion-heuristica.skill # Metadatos del skill (futuro)
├── evals/
│   └── evals.json                       # Pruebas de calidad
├── references/                          # Biblioteca de consulta
│   ├── banking-heuristics.md            # H11-H14 para banca + normativa Colombia
│   ├── retail-heuristics.md             # H11-H14 para retail/e-commerce
│   ├── severity-examples.md             # Ejemplos expandidos por industria
│   └── report-templates.md              # Plantillas de reporte (completa y ejecutiva)
├── scripts/                             # Herramientas de validación (solo modo CLI)
│   ├── calculate_score.py               # Cálculo de score global desde JSON
│   ├── generate_report.py               # Generación de reporte markdown
│   ├── generate_html_report.py          # Generación de reporte HTML auto-contenido
│   ├── validate_findings.py             # Validador de esquema JSON
│   ├── findings_template.json           # Template para documentar hallazgos
│   └── sample-findings.json             # Ejemplo completo de hallazgos
├── README.md                            # Este archivo
└── LICENSE                              # Licencia de uso
```

---

## Referencias del skill

| Archivo | Contenido |
|---|---|
| `banking-heuristics.md` | 4 heurísticas extendidas (H11-H14) para banca digital: seguridad perceptible, privacidad, recuperación de errores financieros, cumplimiento regulatorio. Incluye marco normativo colombiano completo (Ley 1328, Ley 1581, Circular 029, etc.). |
| `retail-heuristics.md` | 4 heurísticas extendidas (H11-H14) para retail/e-commerce: claridad del proceso de compra, confianza en pago, findabilidad de productos, post-compra y seguimiento. |
| `severity-examples.md` | Ejemplos concretos de severidad 0-4 por industria (banca, retail, genérico). Incluye matriz de decisión rápida. |
| `report-templates.md` | Plantillas de reporte completo (stakeholders) y ejecutivo (una página). |

### Scripts

| Script | Propósito | Uso |
|---|---|---|
| `calculate_score.py` | Calcula score global y distribución de severidad desde JSON de hallazgos | `python calculate_score.py hallazgos.json` |
| `generate_report.py` | Genera reporte markdown completo o ejecutivo | `python generate_report.py hallazgos.json --output reporte.md` |
| `generate_html_report.py` | Genera reporte HTML auto-contenido con gráficos de barras y matriz visual | `python generate_html_report.py hallazgos.json --output reporte.html` |
| `validate_findings.py` | Valida que el JSON cumpla el esquema esperado por los otros scripts | `python validate_findings.py hallazgos.json --strict` |

---

## Alcances

- Evalúa interfaces web, aplicaciones web progresivas (PWA), aplicaciones móviles y software de escritorio.
- Cubre las 10 heurísticas de Nielsen (H1-H10) validadas por décadas de investigación.
- Extensiones sectoriales: 4 heurísticas adicionales para banca (H11-H14) y 4 para retail (H11-H14).
- Escala de severidad estándar Nielsen 0-4 (catastrófico a cosmético).
- Incluye normativa colombiana para banca: Ley 1328 (consumidor financiero), Ley 1581 (datos personales), Circular 029 (seguridad), entre otras.
- Matriz de priorización Impacto vs Esfuerzo con 4 cuadrantes.
- Roadmap de implementación en 4 fases.
- Reportes en markdown y HTML auto-contenido.
- No requiere instalación.

## Limitaciones

- Las evaluaciones se basan en el conocimiento del evaluador sobre la interfaz. Para resultados precisos, el skill debe poder acceder a la interfaz (imágenes, descripciones, o URL).
- La severidad asignada a cada hallazgo refleja el criterio del evaluador. Para decisiones críticas, se recomienda una segunda opinión o validación con usuarios.
- La normativa citada debe verificarse en su versión vigente. El skill ofrece el mapa normativo basado en la información disponible, pero no reemplaza el consejo legal.
- No evalúa métricas cuantitativas de uso (tasas de conversión, abandono, etc.). Es un método cualitativo de inspección.
- El cálculo de score global es un promedio simple de severidad. No pondera por frecuencia de uso del flujo ni por criticidad del contexto.
- Para evaluaciones formales con impacto legal o regulatorio, se recomienda complementar con pruebas de usabilidad con usuarios reales.

---

## Licencia

Propiedad de **Pragma**. Uso interno y confidencial — ver `LICENSE`.
