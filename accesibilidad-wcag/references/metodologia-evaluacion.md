# Metodología de evaluación de accesibilidad

Guía paso a paso para ejecutar una auditoría WCAG 2.2 completa y
replicable. Combina pruebas automáticas y manuales por principio POUR.

## Flujo general de la auditoría

### Paso 1 — Alcance

Antes de evaluar, define y documenta:

- **Páginas/pantallas:** home, login, formularios, listados, checkout,
  contenido dinámico. Selecciona muestras representativas de cada plantilla.
- **Dispositivos y navegadores:** desktop y móvil; al menos Chrome,
  Firefox, Safari.
- **Tecnologías de asistencia (AT):** NVDA, JAWS, VoiceOver, TalkBack
  según industria (ver verticales).
- **Nivel objetivo:** A, AA o AAA (ver `normativa-colombiana.md`).
- **Industria:** banca o retail (define los ejemplos y flujos críticos).

### Paso 2 — Auditoría automática

Ejecuta herramientas automáticas sobre cada página del alcance:

- **axe-core** (extensión o CLI): detecta ~30-57% de los SC.
- **WAVE:** apoyo visual de estructura y errores.
- **Lighthouse:** score general y consejos.
- **Scripts propios:** `check_contrast.py` (contraste) y
  `validate_semantic_html.py` (estructura semántica).

Documenta cada hallazgo automático con su SC asociado. **Importante:** las
herramientas automáticas no sustituyen la revisión manual; cubren solo una
fracción de los criterios.

### Paso 3 — Auditoría manual

Revisión experta de lo que la automatización no detecta:

- **Inspección visual:** color, contraste contextual, jerarquía, foco.
- **Navegación por teclado:** Tab, Shift+Tab, Enter, Espacio, flechas, Esc.
- **Lectores de pantalla:** seguir `protocolo-lectores-pantalla.md`.
- **Zoom y reflujo:** 200% y 400% / viewport 320px.

### Paso 4 — Documentación

Para cada hallazgo registra: descripción, SC asociado, principio, nivel,
industria, componente, justificación, evidencia (captura/código/grabación),
recomendación con código, y severidad/esfuerzo/riesgo legal (ver
`priorizacion-remediacion.md` y el formato del `SKILL.md`).

---

## Técnicas de prueba por principio POUR

### Perceptible

- **Contraste (1.4.3 / 1.4.6 / 1.4.11):** medir con `check_contrast.py` o
  Colour Contrast Analyser. Verificar texto, UI y gráficos.
- **Texto alternativo (1.1.1):** inspeccionar `alt`; distinguir imágenes
  decorativas (`alt=""`) de funcionales/informativas.
- **Subtítulos y audiodescripción (1.2.x):** verificar pistas y
  transcripciones en multimedia.
- **Reflujo (1.4.10):** zoom 400% o viewport 320px; no debe haber scroll
  en dos ejes.
- **Uso del color (1.4.1):** confirmar que la información no dependa solo
  del color (errores, estados, enlaces).

### Operable

- **Navegación por teclado (2.1.1, 2.1.2):** recorrer todo con teclado;
  verificar que no haya trampas de foco.
- **Tiempo (2.2.1, 2.2.6):** provocar timeouts; verificar aviso y extensión.
- **Foco (2.4.3, 2.4.7, 2.4.11):** orden lógico, indicador visible, foco no
  oculto por elementos fijos.
- **Movimiento (2.2.2, 2.3.x):** pausar carruseles; respetar
  `prefers-reduced-motion`; sin destellos peligrosos.
- **Objetivos y gestos (2.5.x):** medir tamaño de objetivos; verificar
  alternativas a gestos complejos y arrastre.

### Comprensible

- **Idioma (3.1.1, 3.1.2):** `lang` en `<html>` y en fragmentos.
- **Predictibilidad (3.2.x):** sin cambios de contexto inesperados al
  enfocar o ingresar datos; navegación e identificación consistentes;
  ayuda en ubicación consistente (3.2.6).
- **Errores (3.3.1–3.3.4):** identificación, etiquetas/instrucciones,
  sugerencias y prevención en operaciones sensibles.
- **Autenticación (3.3.8, 3.3.9):** login sin pruebas cognitivas;
  permitir pegar y gestores de contraseñas.

### Robusto

- **Nombre, rol, valor (4.1.2):** inspeccionar ARIA y nombre accesible de
  componentes (botones, inputs, custom widgets).
- **Mensajes de estado (4.1.3):** verificar `aria-live` / roles `status`,
  `alert` para cambios dinámicos (confirmaciones, resultados, carrito).
- **HTML válido:** aunque 4.1.1 quedó obsoleto en 2.2, mantener marcado
  válido mejora la compatibilidad con AT.

---

## Tabla de herramientas

| Herramienta | Tipo | Cobertura | Cómo usarla | Limitaciones |
|---|---|---|---|---|
| axe-core | Automática | ~30-57% de SC | Extensión Chrome / CLI / CI | No detecta contraste contextual ni significado |
| WAVE | Automática | ~30% de SC | Extensión de navegador | Sin API pública; revisión manual |
| Lighthouse | Automática | ~20% de SC | Chrome DevTools | Consejos generales; score limitado |
| Accessibility Insights | Auto + Manual | ~65% de SC | Extensión (FastPass + Assessment) | Algunas funciones solo en Windows |
| NVDA | Lector de pantalla | 100% manual | Software libre (Windows) | Curva de aprendizaje |
| JAWS | Lector de pantalla | 100% manual | Comercial (Windows) | Licencia de pago |
| VoiceOver | Lector de pantalla | 100% manual | Integrado (macOS/iOS) | Solo ecosistema Apple |
| TalkBack | Lector de pantalla | 100% manual | Integrado (Android) | Solo Android |
| Colour Contrast Analyser | Manual | Contraste | App de escritorio | Solo color |
| `check_contrast.py` | Automática | Contraste | `scripts/` (Python stdlib) | Solo contraste |
| `validate_semantic_html.py` | Automática | Estructura semántica | `scripts/` (Python stdlib) | No ejecuta JS ni evalúa significado |

> **Regla de oro:** la conformidad WCAG no se declara solo con
> herramientas automáticas. La revisión manual con teclado y lector de
> pantalla es obligatoria para cubrir la mayoría de los criterios.
