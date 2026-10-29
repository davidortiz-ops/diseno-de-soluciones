---
name: heuristy-evaluacion-heuristica-nielsen
description: >
  Experto en evaluación heurística basada en las 10 heurísticas de Nielsen,
  con extensiones sectoriales para banca y retail. Evalúa interfaces web,
  móviles y desktop identificando problemas de usabilidad, priorizando
  hallazgos con severidad 0-4 y generando reportes estructurados con
  matriz de priorización, puntuación global y roadmap de implementación.
  Incluye checklist regulatorio (Colombia y otros países). Úsalo para
  auditorías de usabilidad en banca digital, e-commerce y sitios web
  transaccionales. Ideal cuando el usuario menciona: evaluación heurística,
  heurísticas de Nielsen, auditoría UX, usabilidad banca, usabilidad retail,
  problemas de usabilidad, test heurístico, evaluar interfaz, revisión de
  experiencia de usuario, análisis de usabilidad bancaria, o compliance
  regulatorio en interfaces financieras.
metadata:
  version: "2.0"
  author: Pragma
  triggers: "evaluación heurística, heurísticas de Nielsen, auditoría de usabilidad, heuristy, problemas de usabilidad, test heurístico, evaluar interfaz, usabilidad banca, usabilidad retail, auditoría UX banca, usabilidad banco digital, usabilidad ecommerce, revisión experiencia de usuario, análisis de usabilidad, compliance regulatorio interfaz, accesibilidad web banca"
---

# Heuristy v2.0 — Evaluación Heurística para Banca y Retail

Evalúa interfaces digitales usando las 10 heurísticas de Nielsen + extensiones sectoriales. Diseñado para profesionales de UX que necesitan un proceso estructurado, repetible y con output accionable.

**Estructura de archivos del skill:**
- `SKILL.md` — instrucciones principales (este archivo)
- `references/banking-heuristics.md` — heurísticas extendidas H11-H14 para banca + normativa Colombia
- `references/retail-heuristics.md` — heurísticas extendidas H11-H14 para retail/e-commerce
- `references/severity-examples.md` — ejemplos expandidos de severidad por industria
- `references/report-templates.md` — plantillas de reporte completo y ejecutivo
- `scripts/calculate_score.py` — script CLI para calcular score global desde hallazgos JSON
- `scripts/generate_report.py` — script CLI para generar reporte markdown desde hallazgos JSON
- `scripts/generate_html_report.py` — script CLI para generar reporte HTML auto-contenido desde hallazgos JSON
- `scripts/validate_findings.py` — script CLI para validar el esquema de hallazgos JSON
- `scripts/findings_template.json` — template JSON para documentar hallazgos
- `scripts/sample-findings.json` — ejemplo completo de hallazgos documentados

---

## 1. Cómo usar este skill

### Paso 1: Definir contexto
Antes de evaluar, determina con el usuario:
- **Tipo de producto**: web, mobile app, desktop, kiosko
- **Industria**: banca, retail, otro (genérico)
- **Alcance**: página específica, flujo completo, sitio completo
- **Flujos críticos**: login, registro, transferencia, checkout, búsqueda, etc.
- **Regulatorio**: normativa local aplicable (Colombia, Perú, México, Chile, UE, etc.)

Usa las preguntas de la sección 2 para capturar el contexto completo.

### Paso 2: Seleccionar plantilla según industria
- **Banca** → lee también `references/banking-heuristics.md` (H11-H14 + normativa)
- **Retail** → lee también `references/retail-heuristics.md` (H11-H14 + conversión)
- **Genérico** → usa solo las 10 heurísticas de Nielsen

### Paso 3: Ejecutar evaluación
Para cada heurística (H1-H10, más H11-H14 si aplica):
1. Recorre la interfaz/flujo como si fueras un usuario real
2. Responde las preguntas de evaluación de cada heurística
3. Documenta cada hallazgo con: título, ubicación, descripción, severidad (0-4), heurística violada, recomendación, esfuerzo estimado
4. Si no hay problemas en una heurística, documéntalo como "Sin problemas"

Lee `references/severity-examples.md` si necesitas ejemplos concretos para asignar severidad.

### Paso 4: Calcular score global
Aplica la fórmula de la sección 4.

### Paso 5: Clasificar en matriz y generar roadmap
Usa la sección 6 y 7 para priorizar y construir el plan de acción.

### Paso 6: Producir el reporte
Usa la plantilla de `references/report-templates.md`. Escoge entre:
- **Completa**: para entregar a stakeholders
- **Ejecutiva**: para auditorías rápidas o iterativas

---

## 2. Preguntas de Contexto (para capturar del usuario)

Antes de empezar, recopila esta información. Si el usuario ya la proporcionó, confírmala.

```
- Producto/Sitio a evaluar: [nombre o URL]
- Industria: [banca | retail | otro]
- Tipo de interfaz: [web | mobile app | desktop | kiosko]
- Alcance: [página específica | flujo completo | sitio completo]
- Flujos a evaluar: [login, registro, transferencia, checkout, búsqueda, etc.]
- Usuarios objetivo: [perfil demográfico, nivel técnico]
- Restricciones técnicas/de negocio: [frameworks, limitaciones conocidas]
- Normativa aplicable: [Colombia | Perú | México | Chile | UE | Otro | Ninguna]
- Nivel de detalle requerido: [ejecutivo | completo]
```

---

## 3. Escala de Severidad Nielsen (0-4)

Usa esta escala para calificar CADA hallazgo. Es la escala estándar de Nielsen, validada por décadas de investigación.

| Nivel | Nombre | Significado | ¿Qué hacer? |
|---|---|---|---|
| 0 | No es problema | No afecta la usabilidad | No documentar |
| 1 | Cosmético | Problema estético. El usuario lo nota pero no le impide完成任务 | Arreglar si hay tiempo |
| 2 | Menor | Causa leve frustración. El usuario completa la tarea pero con molestia | Prioridad baja |
| 3 | Mayor | Dificulta significativamente la tarea. El usuario se atasca o comete errores | Alta prioridad |
| 4 | Catastrófico | Bloquea completamente al usuario. No puede completar la tarea | Debe arreglarse antes del lanzamiento |

Para ejemplos concretos por industria, lee `references/severity-examples.md`.

---

## 4. Sistema de Puntuación Global

Calcula el score global de usabilidad una vez que todos los hallazgos estén documentados.

### Fórmula
```
Score = 10 - (promedio de severidad de todos los hallazgos)
```

Donde el promedio se calcula sumando la severidad de cada hallazgo y dividiendo por el número total de hallazgos (excluyendo severidad 0).

### Interpretación

| Score | Significado |
|---|---|
| 9.0 - 10 | Excelente. Problemas menores o cosméticos solamente |
| 7.0 - 8.9 | Bueno. Problemas menores que no bloquean flujos principales |
| 5.0 - 6.9 | Regular. Problemas mayores que afectan la experiencia |
| 3.0 - 4.9 | Malo. Problemas críticos que requieren intervención urgente |
| 0 - 2.9 | Crítico. Múltiples bloqueos. Rediseño necesario |

También calcula el desglose por tipo:
- **% hallazgos críticos** (severidad 4): alerta roja si > 10%
- **% hallazgos mayores** (severidad 3): alerta amarilla si > 25%
- **Heurística más violada**: identifica el patrón dominante

---

## 5. Las 10 Heurísticas de Nielsen con Preguntas Evaluables

Cada heurística incluye preguntas de evaluación. Responde cada una y documenta los hallazgos que encuentres. Si respondes "Sí" a todas sin observaciones, la heurística está cumplida.

### H1: Visibilidad del Estado del Sistema
*El diseño debe mantener informado al usuario sobre lo que está ocurriendo, con retroalimentación apropiada en tiempo razonable.*

**Preguntas:**
- ¿El sistema muestra feedback inmediato después de cada acción del usuario?
- ¿Las barras de progreso o indicadores de carga están presentes en procesos que toman >2 segundos?
- ¿El usuario sabe en qué paso del flujo se encuentra actualmente?
- ¿Los mensajes de confirmación son visibles el tiempo suficiente para ser leídos?
- ¿Las notificaciones de estado (pendiente, aprobado, fallido) son claras y consistentes?

**Específico banca:** ¿La pantalla de transacciones muestra estado en tiempo real (pendiente/completada/fallida)?
**Específico retail:** ¿El carrito muestra el número actualizado de artículos en el ícono?

### H2: Coincidencia entre el Sistema y el Mundo Real
*El diseño debe hablar el lenguaje del usuario, con palabras, frases y conceptos familiares, siguiendo convenciones del mundo real.*

**Preguntas:**
- ¿La terminología usa palabras del usuario, no jerga técnica/interna?
- ¿Los iconos son intuitivos y corresponden a metáforas del mundo real?
- ¿La información aparece en un orden natural y lógico para el usuario?
- ¿Las categorías y etiquetas reflejan la mentalidad del usuario, no la estructura organizacional?

**Específico banca:** ¿Términos como "Cruce de cuentas" o "CDAT" están explicados o reemplazados por lenguaje claro?
**Específico retail:** ¿Las categorías de producto usan nombres que el usuario usaría al buscar?

### H3: Control y Libertad del Usuario
*Los usuarios a menudo realizan acciones por error. Necesitan una "salida de emergencia" claramente marcada.*

**Preguntas:**
- ¿Hay una opción clara de "Cancelar" o "Volver" en cada paso?
- ¿Se soporta Undo/Redo para acciones destructivas?
- ¿El botón "Atrás" del navegador funciona como el usuario espera?
- ¿Los diálogos modales tienen una "X" o botón de cierre visible?
- ¿Las acciones irreversibles tienen confirmación antes de ejecutarse?

**Específico banca:** ¿Se puede cancelar una transferencia antes de confirmar? ¿Hay paso de revisión antes de ejecutar?
**Específico retail:** ¿Se puede modificar/eliminar un producto del carrito sin recargar la página?

### H4: Consistencia y Estándares
*Los usuarios no deberían tener que preguntarse si diferentes palabras, situaciones o acciones significan lo mismo.*

**Preguntas:**
- ¿Los botones con la misma función tienen el mismo color, posición y texto en todo el sitio?
- ¿Los términos y etiquetas son consistentes entre pantallas?
- ¿El diseño sigue convenciones de la industria (carrito arriba a la derecha, logo enlazado al home)?
- ¿Los patrones de interacción (clic, hover, swipe) son predecibles?
- ¿El layout se mantiene consistente entre páginas del mismo tipo?

**Específico banca:** ¿El botón "Pagar" o "Transferir" siempre tiene el mismo color y posición?
**Específico retail:** ¿Las fichas de producto tienen la misma estructura en toda la tienda?

### H5: Prevención de Errores
*Mejor que un buen mensaje de error es evitar que el error ocurra.*

**Preguntas:**
- ¿Los campos de formulario tienen validación en tiempo real (no solo al enviar)?
- ¿Las acciones destructivas piden confirmación antes de ejecutarse?
- ¿Se usan selectores (dropdown, datepicker) en lugar de campos abiertos cuando es posible?
- ¿Los defaults son seguros y evitan errores comunes?
- ¿Las restricciones (límite de caracteres, formato) se comunican antes de que el usuario escriba?

**Específico banca:** ¿El formulario de transferencia valida el número de cuenta antes de enviar? ¿Muestra el nombre del titular para confirmar?
**Específico retail:** ¿El selector de talla/color previene seleccionar combinaciones agotadas?

### H6: Reconocimiento antes que Recuerdo
*Minimizar la carga de memoria del usuario haciendo visibles elementos, acciones y opciones.*

**Preguntas:**
- ¿Las opciones disponibles son visibles, no ocultas en menús anidados?
- ¿El usuario puede reconocer información en lugar de tener que recordarla de pantallas anteriores?
- ¿Los campos críticos tienen labels visibles siempre (no placeholders que desaparecen)?
- ¿Las navegaciones principales son persistentes?
- ¿La información de contexto se mantiene visible mientras el usuario trabaja en una tarea?

**Específico banca:** ¿El saldo actual es visible durante todo el flujo de transferencia?
**Específico retail:** ¿El carrito con productos seleccionados es visible durante el checkout?

### H7: Flexibilidad y Eficiencia de Uso
*Los atajos —ocultos para usuarios novatos— pueden acelerar la interacción para el usuario experto.*

**Preguntas:**
- ¿Hay atajos de teclado para acciones frecuentes?
- ¿Los usuarios frecuentes pueden personalizar su dashboard o vista?
- ¿Las acciones repetitivas se pueden automatizar (agendar, guardar como plantilla)?
- ¿Los power users pueden saltar pasos en flujos conocidos?
- ¿La búsqueda permite comandos avanzados (filtros, operadores)?

**Específico banca:** ¿Se pueden guardar transferencias como plantillas para reutilizar? ¿Hay transferencias rápidas entre cuentas propias?
**Específico retail:** ¿Hay compra rápida con 1 clic? ¿Se puede reordenar un pedido anterior?

### H8: Diseño Estético y Minimalista
*Las interfaces no deben contener información irrelevante o raramente necesaria.*

**Preguntas:**
- ¿Cada elemento en pantalla tiene un propósito claro?
- ¿La jerarquía visual guía la atención hacia lo más importante primero?
- ¿El contenido está libre de información redundante o innecesaria?
- ¿Los espacios en blanco se usan para organizar y reducir carga cognitiva?
- ¿Las imágenes y gráficos son funcionales, no meramente decorativos?

**Específico banca:** ¿El dashboard muestra solo la información relevante para la tarea actual, no todo el portafolio de productos?
**Específico retail:** ¿Las fichas de producto muestran solo la información necesaria para decidir, sin bloques de texto extensos?

### H9: Ayuda a los Usuarios a Reconocer, Diagnosticar y Recuperarse de Errores
*Los mensajes de error deben expresarse en lenguaje sencillo, indicar el problema con precisión y sugerir una solución.*

**Preguntas:**
- ¿Los mensajes de error usan lenguaje claro, no códigos técnicos?
- ¿El mensaje dice exactamente qué salió mal y por qué?
- ¿Se ofrece una solución o paso siguiente concreto?
- ¿Los errores de formulario señalan el campo específico con el problema?
- ¿El diseño visual del error es notorio (color, icono, posición)?

**Específico banca:** ¿Un error de transferencia dice "Saldo insuficiente. Tu saldo disponible es $XXX" en vez de "Error 0x80070057"?
**Específico retail:** ¿Un error de pago dice "Tarjeta rechazada. Verifica el número o intenta con otro medio de pago"?

### H10: Ayuda y Documentación
*Es mejor si el sistema no necesita explicación adicional. Pero puede ser necesaria documentación para ayudar a los usuarios a completar tareas.*

**Preguntas:**
- ¿La ayuda es fácil de encontrar y buscar?
- ¿La documentación está enfocada en tareas del usuario, no en funcionalidades del sistema?
- ¿Hay ayuda contextual (tooltips, enlaces "¿Qué es esto?") en el momento justo?
- ¿Las FAQs cubren las preguntas reales de los usuarios?
- ¿Los tutoriales o guías son opcionales y no bloquean al usuario?

**Específico banca:** ¿Hay ayuda contextual en términos financieros complejos? ¿El FAQ cubre "¿Cómo reporto un cargo no reconocido?"?
**Específico retail:** ¿Hay tooltips en campos de pago (CVV, código postal)? ¿La política de devolución es fácil de encontrar?

---

## 6. Detección de Patrones Cruzados

Al finalizar la evaluación, identifica patrones que cruzan múltiples heurísticas. Estos revelan problemas sistémicos que requieren atención estructural.

### Patrones comunes

| Patrón | Señales | Heurísticas típicas |
|---|---|---|
| **Falta de feedback** | Usuarios no saben si su acción funcionó | H1, H5, H9 |
| **Sobrecarga cognitiva** | Demasiada información en pantalla, tareas complejas sin guía | H2, H6, H8 |
| **Inconsistencia** | Mismos elementos se ven/comportan diferente según la pantalla | H4, H2 |
| **Fricción en flujos críticos** | El usuario no puede completar la tarea principal | H3, H5, H6, H7 |
| **Mala recuperación de errores** | Cuando algo sale mal, el usuario queda sin opciones | H9, H5, H3 |
| **Desconfianza** | El usuario duda antes de introducir datos sensibles o pagar | H11, H12, H14 (banca) / H12 (retail) |

Documenta los patrones encontrados en la sección de hallazgos del reporte.

---

## 7. Matriz de Priorización (Impacto vs Esfuerzo)

Clasifica cada hallazgo en uno de estos 4 cuadrantes:

```
                    Impacto
                    Alto
              ┌─────────────┬─────────────┐
              │             │             │
              │  QUICK WINS │   MAJOR     │
              │  Hacer ya   │   PROJECTS  │
              │             │   Planificar│
  Bajo  ──────┤─────────────┼─────────────┤──────  Alto
  Esfuerzo    │             │             │  Esfuerzo
              │  FILL-INS   │  THANKLESS  │
              │  Si sobra   │  Evitar /   │
              │  tiempo     │  Revaluar   │
              │             │             │
              └─────────────┴─────────────┘
                    Bajo
```

### Criterios para clasificar

| Cuadrante | Impacto | Esfuerzo | Acción |
|---|---|---|---|
| **Quick Win** | Alto (severidad 3-4, afecta flujo crítico) | Pequeño-Medio (< 1 semana) | Hacer inmediatamente |
| **Major Project** | Alto (severidad 3-4) | Grande (> 1 semana) | Planificar en roadmap |
| **Fill-in** | Bajo (severidad 1-2) | Pequeño | Hacer si hay tiempo |
| **Thankless** | Bajo (severidad 1-2) | Grande | Evitar o revaluar |

---

## 8. Roadmap de Implementación

Organiza los hallazgos en fases según la matriz de priorización.

### Fase 1: Quick Wins (Inmediato, < 1 semana)
- Todos los hallazgos del cuadrante Quick Win
- Objetivo: eliminar las fricciones más críticas con el mínimo esfuerzo

### Fase 2: Corto Plazo (1-4 semanas)
- Hallazgos Major Projects de menor esfuerzo
- Hallazgos Fill-ins que puedan combinarse con otros trabajos
- Objetivo: estabilizar la experiencia

### Fase 3: Mediano Plazo (1-3 meses)
- Major Projects que requieren desarrollo más profundo
- Objetivo: mejorar la experiencia significativamente

### Fase 4: Estratégico (3+ meses)
- Rediseños de flujos completos o componentes grandes
- Objetivo: transformación de la experiencia

### Métricas para medir éxito
Menciona qué métricas pueden usarse para validar cada mejora:
- **Tasa de finalización de tareas** (antes vs después)
- **Tiempo promedio en tarea**
- **Tasa de errores por flujo**
- **Satisfacción del usuario** (SUS, CSAT)
- **Reducción de tickets de soporte** (para banca/retail)

---

## 9. Checklist de Cumplimiento (Banca)

Cuando la industria sea **banca** y la normativa sea **Colombia**, evalúa estos ítems adicionales además de las heurísticas. Si aplica otra normativa, pregunta al usuario cuál usar.

### Protección al Consumidor Financiero (Ley 1328 de 2009)
- [ ] Información contractual clara y visible al contratar productos
- [ ] Tasa de interés (EA y nominal) visible en todos los productos financieros
- [ ] Proceso de PQR (Peticiones, Quejas, Reclamos) accesible desde el menú principal
- [ ] Número de atención al consumidor financiero visible
- [ ] Costos totales de productos/servicios desglosados antes de contratar

### Protección de Datos (Ley 1581 de 2012 + Decreto 1377 de 2013)
- [ ] Aviso de privacidad accesible desde todas las pantallas
- [ ] Consentimiento explícito para tratamiento de datos
- [ ] Opción de ejercer derechos (acceso, corrección, supresión, portabilidad)
- [ ] Política de tratamiento de datos publicada

### Seguridad de la Información (Circular Externa 029 de 2014)
- [ ] Autenticación multifactor para transacciones sensibles
- [ ] Notificaciones de actividad inusual (email/SMS/push)
- [ ] Cierre de sesión por inactividad con tiempo adecuado
- [ ] Bloqueo de cuenta tras intentos fallidos con mensaje claro

### Accesibilidad
- [ ] Contraste mínimo 4.5:1 para texto normal (WCAG AA)
- [ ] Navegación por teclado funcional en formularios y menús
- [ ] Texto alternativo en imágenes funcionales
- [ ] Labels en todos los campos de formulario

Para más detalle sobre cada normativa, consulta la sección "Marco Normativo Colombiano" en `references/banking-heuristics.md`.

---

## 10. Restricciones

**Lo que SÍ debes hacer:**
- Ser específico y concreto en cada hallazgo (título, ubicación, severidad, recomendación)
- Proporcionar contexto para cada problema identificado
- Balancear críticas constructivas con reconocimiento de aspectos positivos (mínimo 3)
- Considerar el contexto de negocio y limitaciones realistas
- Si la industria es banca, verificar normativa local con el usuario
- Preguntar al usuario si aplica normativa de otro país cuando no sea Colombia
- Incluir evidencia (captura de pantalla si está disponible)

**Lo que NO debes hacer:**
- Usar escalas de severidad distintas a 0-4 de Nielsen
- Documentar hallazgos sin recomendación concreta
- Usar criterios subjetivos sin respaldo en principios de usabilidad
- Ignorar el contexto específico del producto o industria
- Asumir normativa sin confirmar con el usuario
- Producir un reporte sin matriz de priorización o roadmap
- Evaluar sin haber confirmado el alcance con el usuario
- Confundir severidad con esfuerzo — son dimensiones distintas

---

## 11. Scripts CLI (obligatorios en modo CLI)

- En **Claude Code (CLI)**: los scripts son obligatorios. El flujo de trabajo completo requiere usar `calculate_score.py`, `generate_report.py` y `validate_findings.py` para producir los entregables. No se genera el reporte manualmente.
- En **Claude Desktop**: no hay terminal disponible. El skill ejecuta la evaluación completa siguiendo los pasos 1-6 y entrega el reporte dentro de la conversación. Los scripts no aplican.

### findings_template.json
Template para estructurar hallazgos en un formato que los scripts pueden procesar.
Cópialo y complétalo con tus hallazgos durante la evaluación.

```json
{
  "context": {
    "product": "Nombre del producto",
    "industry": "banca | retail | otro",
    "scope": "página | flujo | sitio completo",
    "evaluator": "Tu nombre",
    "date": "AAAA-MM-DD"
  },
  "findings": [
    {
      "id": 1,
      "heuristic": "H1",
      "title": "Título breve del hallazgo",
      "location": "Dónde ocurre",
      "description": "Descripción del problema",
      "severity": 3,
      "recommendation": "Qué hacer",
      "effort": "Pequeño | Medio | Grande"
    }
  ]
}
```

### calculate_score.py
Calcula el score global, distribución de severidad y genera alertas.

```bash
python scripts/calculate_score.py scripts/sample-findings.json
```

Salida:
- Score Global (X/10)
- Distribución por severidad (barras ASCII)
- Alertas si %críticos > 10% o %mayores > 25%

Úsalo después de recopilar todos los hallazgos y tener el JSON completo. Te ahorra calcular el score manualmente.

### generate_report.py
Genera un reporte markdown listo para compartir.

```bash
# Reporte completo (incluye matriz y roadmap):
python scripts/generate_report.py hallazgos.json --output reporte.md

# Reporte ejecutivo (una página):
python scripts/generate_report.py hallazgos.json --template ejecutiva --output reporte-ejecutivo.md
```

El reporte completo incluye: resumen ejecutivo, tabla de hallazgos, matriz de priorización (Quick Wins, Major Projects, Fill-ins, Thankless) y roadmap por fases. El ejecutivo incluye solo score, top problemas y quick wins.

### generate_html_report.py
Genera un reporte HTML auto-contenido (sin dependencias externas) listo para compartir con stakeholders. Incluye gráfico de barras de severidad, tabla de hallazgos, matriz de priorización visual y roadmap.

```bash
# Reporte completo (por defecto):
python scripts/generate_html_report.py hallazgos.json --output reporte.html

# Reporte ejecutivo (una página):
python scripts/generate_html_report.py hallazgos.json --template ejecutiva --output reporte-ejecutivo.html

# En inglés:
python scripts/generate_html_report.py hallazgos.json --lang en --output report.html
```

### validate_findings.py
Valida que el archivo JSON de hallazgos cumpla el esquema esperado por los demás scripts. Útil para prevenir errores antes de generar reportes.

```bash
# Validación básica:
python scripts/validate_findings.py hallazgos.json

# Validación estricta (todos los campos opcionales):
python scripts/validate_findings.py hallazgos.json --strict

# Corregir errores menores automáticamente:
python scripts/validate_findings.py hallazgos.json --fix
```

### Flujo de trabajo recomendado con scripts

1. Durante la evaluación, completa el `findings_template.json` con cada hallazgo
2. Al terminar, valida el JSON: `validate_findings.py hallazgos.json`
3. Calcula el score: `calculate_score.py hallazgos.json`
4. Genera el reporte markdown: `generate_report.py hallazgos.json --output reporte.md`
5. Genera el reporte HTML: `generate_html_report.py hallazgos.json --output reporte.html`
6. Comparte el reporte HTML con el equipo (no requiere herramientas adicionales para abrirlo)

Los scripts requieren **Python 3.8+**. Verifica con `python --version`. Si no está disponible, el skill puede calcular el score manualmente (ver sección 4).

- [NNGroup - 10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/)
- [NNGroup - How to Conduct a Heuristic Evaluation](https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/)
- [Interaction Design Foundation](https://www.interaction-design.org/literature/topics/)
- [Maze - Usability Testing Guide](https://maze.co/guides/usability-testing/)
- [UOC - Evaluación Heurística](https://design-toolkit.recursos.uoc.edu/es/evaluacion-heuristica/)
- Superintendencia Financiera de Colombia — [Circular Básica Jurídica](https://www.superfinanciera.gov.co/)
- Ley 1328 de 2009 — [Protección al Consumidor Financiero](https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=38142)
- Ley 1581 de 2012 — [Protección de Datos](https://www.sic.gov.co/ley-1581-de-2012)

---

## 13. Solicitudes Sugeridas

**Configurar Contexto**
Necesito evaluar un sitio de [banca/retail]. Te comparto: URL, alcance, flujos críticos. Prepara las preguntas de contexto y empecemos.

**Evaluación Banca**
Evalúa heurísticamente el flujo de [login / transferencia / pago de servicios] de [nombre del banco / URL]. Enfócate en visibilidad del estado, prevención de errores y seguridad perceptible. Incluye normativa colombiana.

**Evaluación Retail**
Analiza el proceso de checkout de [URL tienda]. Evalúa las 10 heurísticas + extensión retail. Dame la matriz de priorización y roadmap.

**Priorizar Problemas**
Toma esta lista de hallazgos y genera matriz Impacto vs Esfuerzo con roadmap de implementación por fases.

**Reporte Rápido**
Haz una evaluación ejecutiva de [URL]. Dame score global, top 5 problemas críticos y quick wins.

**Aspectos Positivos + Mejora**
Además de los problemas, señala al menos 5 aspectos positivos de la interfaz con ejemplos concretos de buenas prácticas.
