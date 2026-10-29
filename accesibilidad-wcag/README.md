# Skill de Accesibilidad Digital WCAG 2.2 — Banca y Retail

Skill de auditoría de accesibilidad web para **banca** y **retail** en el contexto normativo colombiano. Diseñado para investigadores de UX, diseñadores de servicios, analistas de experiencia de cliente, product managers y consultores de inclusión digital.

Versión 2.1 · People Center Design · Pragma

---

## ¿Qué hace?

Realiza auditorías de accesibilidad web siguiendo el estándar internacional **WCAG 2.2** (niveles A, AA y AAA). Evalúa una URL o un flujo completo contra 87 criterios de accesibilidad, documenta cada hallazgo, lo prioriza por severidad y riesgo legal, y genera tres entregables:

- **Reporte técnico** — detalle completo de hallazgos para equipos de desarrollo y QA.
- **Reporte ejecutivo** — resumen para liderazgo y stakeholders con hallazgos críticos y riesgo legal.
- **Declaración de conformidad** — documento formal que certifica el nivel de cumplimiento WCAG.

---

## ¿Cómo funciona?

El skill sigue un **workflow de seis fases**:

1. **Alcance** — Define qué auditar (URL, flujo, industria). Detecta automáticamente si es banca o retail y ajusta los criterios.
2. **Auditoría automatizada** — Ejecuta verificaciones medibles (contraste de color, estructura de encabezados, etiquetas de formularios, atributos de accesibilidad).
3. **Auditoría manual** — Revisa lo que las herramientas no detectan: navegación con teclado, compatibilidad con lectores de pantalla, claridad de instrucciones, mensajes de error.
4. **Análisis y priorización** — Clasifica cada hallazgo combinando severidad (impacto en el usuario), esfuerzo de corrección y riesgo legal.
5. **Generación de reportes** — Produce los tres entregables estándar.
6. **Remediación y verificación** — Entrega recomendaciones priorizadas y define una re-auditoría.

---

## ¿Para qué usarlo?

| Rol | Aplicación |
|---|---|
| **UX Researcher** | Identificar barreras en estudios de usabilidad antes de que un usuario con discapacidad las encuentre. Complementar sesiones de prueba con una visión sistemática. |
| **Diseñador de servicios** | Validar que los flujos completos (registro, consulta, compra) sean navegables por cualquier persona. |
| **Analista de experiencia de cliente** | Cuantificar el riesgo de exclusión digital del producto y medir su evolución. |
| **Product Manager** | Priorizar inversión en accesibilidad con datos concretos: hallazgos documentados, severidad y riesgo legal. |
| **Consultor de inclusión digital** | Emitir declaraciones de conformidad, preparar auditorías formales y educar a equipos sobre accesibilidad. |

---

## ¿Cómo se usa?

1. Abre el skill en el asistente AI (Claude Code, Claude Desktop o Claude.ai).
2. Solicita una auditoría indicando la URL o el flujo a evaluar. Ejemplos:
   - _"Audita la página de inicio de sesión de [URL]"_
   - _"Revisa la accesibilidad del flujo de checkout de [URL] para retail, nivel AA"_
   - _"Necesito el reporte ejecutivo de [URL]"_
3. El skill recupera la página, la evalúa y entrega los resultados en el formato solicitado.

No requiere instalación ni configuración previa.

---

## ¿Cuándo usarlo?

- Antes de lanzar un producto o funcionalidad
- En cada sprint o ciclo de desarrollo
- Durante rediseños
- Al recibir un requerimiento legal o de compliance (SIC, SFC, MinTIC)
- En auditorías periódicas (al menos anual)
- Al evaluar productos de terceros o proveedores
- En preparación de licitaciones públicas

---

## Modos de ejecución

El skill se adapta automáticamente al entorno donde se ejecute:

| Característica | Modo CLI | Modo ID |
|---|---|---|
| Entorno | Terminal disponible (Claude Code) | Sin terminal (Claude Desktop / .ai) |
| Verificaciones automáticas | Ejecuta herramientas de validación | Las hace el modelo inspeccionando directamente |
| Cálculo de contraste | Automático | Fórmula WCAG incluida en el skill |
| Reportes | Se guardan en archivos | Se entregan dentro de la conversación |
| Ideal para | Perfiles técnicos | Investigadores, diseñadores, PMs |

No necesitas elegir un modo. El skill lo detecta al iniciar la auditoría.

---

## Estructura

```
accesibilidad-wcag/
├── SKILL.md                        # Lógica principal de la auditoría (6 fases)
├── accesibilidad-wcag.skill        # Metadatos del skill
├── evals/
│   └── evals.json                  # Pruebas de calidad
├── references/                     # Biblioteca de consulta
│   ├── checklist-wcag-22.md        # Los 87 criterios WCAG con ejemplos banca/retail
│   ├── calculo-contraste-manual.md # Fórmula de contraste (alternativa manual)
│   ├── normativa-colombiana.md     # Mapeo WCAG ↔ leyes colombianas
│   ├── metodologia-evaluacion.md   # Paso a paso de la auditoría
│   ├── protocolo-lectores-pantalla.md  # NVDA, JAWS, VoiceOver, TalkBack
│   ├── priorizacion-remediacion.md # Matriz severidad × esfuerzo × riesgo legal
│   ├── patrones-remediacion-aria.md    # Corrección de componentes interactivos
│   ├── patrones-formularios.md     # Corrección de formularios y validación
│   ├── patrones-navegacion.md      # Corrección de navegación y estructura
│   ├── presentacion-datos.md       # Corrección de tablas, gráficos, cifras
│   ├── estados-aplicacion.md       # Corrección de estados de carga, error, sesión
│   ├── responsive-y-objetivos.md   # Corrección de zoom, reflujo, objetivos táctiles
│   ├── seguridad-accesible.md      # Corrección de autenticación y timeouts
│   └── verticales/
│       ├── banca.md                # Flujos y problemas típicos de banca
│       └── retail.md               # Flujos y problemas típicos de retail
├── templates/                      # Plantillas de reportes
│   ├── reporte-auditoria.html      # Reporte técnico detallado
│   ├── reporte-ejecutivo.md        # Resumen para stakeholders
│   └── declaracion-conformidad.md  # Declaración formal de conformidad
└── scripts/                        # Herramientas de validación (solo modo CLI)
    ├── run_pa11y_audit.sh
    ├── check_contrast.py
    └── validate_semantic_html.py
```

---

## Referencias del skill

| Archivo | Contenido |
|---|---|
| `checklist-wcag-22.md` | Lista completa de los 87 criterios de accesibilidad WCAG 2.2, con ejemplos contextualizados para banca y retail. |
| `calculo-contraste-manual.md` | Procedimiento para calcular contraste entre colores usando la fórmula WCAG, sin depender de herramientas externas. |
| `normativa-colombiana.md` | Mapeo de las normas colombianas que exigen accesibilidad digital: Ley 1618, Circular SFC, Estatuto del Consumidor, resoluciones MinTIC, NTC 5854. |
| `metodologia-evaluacion.md` | Metodología detallada de la auditoría: qué revisar, en qué orden, cómo documentar. |
| `protocolo-lectores-pantalla.md` | Guía para realizar pruebas con lectores de pantalla recomendados en cada plataforma. |
| `priorizacion-remediacion.md` | Matriz para calcular la prioridad de cada hallazgo combinando severidad, esfuerzo y riesgo legal. |
| `patrones-remediacion-aria.md` | Guías para corregir componentes interactivos: modales, pestañas, menús, acordeones, alertas, combobox. |
| `patrones-formularios.md` | Guías para corregir formularios: etiquetas, mensajes de error, validación, autenticación. |
| `patrones-navegacion.md` | Guías para corregir la navegación: enlaces para saltar contenido, landmarks, migas de pan, foco. |
| `presentacion-datos.md` | Guías para corregir la presentación de tablas, gráficos y datos numéricos. |
| `estados-aplicacion.md` | Guías para corregir estados de carga, vacío, error, sesión y live regions. |
| `responsive-y-objetivos.md` | Guías para corregir zoom, reflujo, orientación y tamaño mínimo de objetivos táctiles. |
| `seguridad-accesible.md` | Guías para corregir autenticación, CAPTCHA, timeouts de sesión y manejo de errores de seguridad. |
| `verticales/banca.md` | Problemas de accesibilidad más frecuentes en banca digital: login, transferencias, OTP, tablas de tasas, consultas de saldo. |
| `verticales/retail.md` | Problemas de accesibilidad más frecuentes en comercio electrónico: carruseles, filtros, selección de variantes, checkout, pasarelas de pago. |

### Plantillas de reportes

| Archivo | Destinatario | Propósito |
|---|---|---|
| `reporte-auditoria.html` | Equipos técnicos | Todos los hallazgos con detalle completo: criterio, evidencia, justificación, prioridad. |
| `reporte-ejecutivo.md` | Liderazgo, PMs, stakeholders | Resumen ejecutivo con hallazgos críticos, impacto en usuarios, riesgo legal y recomendaciones. |
| `declaracion-conformidad.md` | Clientes, entes regulatorios, licitaciones | Declaración formal del nivel de conformidad con WCAG. |

---

## Alcances

- Evalúa sitios web y aplicaciones web (todo lo que corre en un navegador).
- Cubre los tres niveles WCAG 2.2: A, AA y AAA (87 criterios).
- Adaptado al contexto colombiano: normativa local, ejemplos de banca y retail, español.
- Considera cinco tipos de usuario: discapacidad visual, cognitiva, auditiva, motriz y múltiple.
- Genera los tres entregables estándar de una auditoría profesional.
- Evalúa URLs individuales o flujos completos (múltiples páginas).
- No requiere instalación.

## Limitaciones

- Solo aplicaciones web. No audita aplicaciones móviles nativas (iOS/Android), aunque las PWAs sí entran en alcance.
- Las verificaciones automáticas cubren ~30-40% de los criterios. La auditoría manual del skill compensa esta brecha, pero la verificación con usuarios reales y tecnologías de asistencia sigue siendo necesaria para declarar conformidad total.
- El cálculo de contraste puede tener diferencias mínimas frente a herramientas especializadas. Para certificación formal, se recomienda usar Colour Contrast Analyzer u otra herramienta estándar.
- Las pruebas con lectores de pantalla deben ejecutarlas un humano con el lector instalado. El skill describe qué probar y cómo, pero no las ejecuta.
- La normativa citada debe verificarse en su versión vigente. El skill ofrece el mapa normativo basado en la información disponible, pero no reemplaza el consejo legal.
- No evalúa accesibilidad de contenido descargable (PDFs, documentos Office) ni de multimedia (audio, video) más allá de verificar alternativas textuales.

---

## Normatividad colombiana aplicable

| Norma | Año | Exigencia principal |
|---|---|---|
| **Ley 1346** | 2009 | Ratifica la Convención de la ONU: el acceso a la información y las TIC es un derecho de las personas con discapacidad. |
| **Ley 1618** | 2013 | Disposiciones para garantizar el pleno ejercicio de los derechos de personas con discapacidad, incluida la accesibilidad digital. |
| **Ley 1680** | 2013 | Garantiza a personas ciegas y con baja visión el acceso a la información, comunicaciones y TIC. |
| **Circular Externa SFC** | 2022 | Exige que los canales digitales de entidades vigiladas por la Superintendencia Financiera sean accesibles e inclusivos. |
| **Ley 1480 — Estatuto del Consumidor** | 2011 | Exige información clara, veraz y suficiente en comercio electrónico. Una barrera de accesibilidad puede vulnerar este derecho. |
| **Res. MinTIC 1519/2020 y 1239/2022** | 2020-2022 | Adoptan WCAG 2.1 nivel AA como estándar obligatorio para sitios del Estado colombiano. |
| **NTC 5854 (Icontec)** | 2011 | Norma técnica colombiana de accesibilidad web alineada con WCAG. |

El detalle completo, incluyendo sanciones y alcance de cada norma, está en `references/normativa-colombiana.md`.

---

## Licencia

Propiedad de **Pragma**. Uso interno y confidencial — ver `LICENSE`.
