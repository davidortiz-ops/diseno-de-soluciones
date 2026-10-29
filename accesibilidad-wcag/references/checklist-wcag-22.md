# Checklist WCAG 2.2 — 87 criterios (A, AA, AAA)

Checklist completa de los Criterios de Conformidad (SC) de WCAG 2.2,
agrupados por los cuatro principios POUR (Perceptible, Operable,
Comprensible, Robusto). Cada criterio incluye: requisito, cómo probarlo
(automático/manual), herramienta sugerida y ejemplos contextualizados
para **banca** y **retail** en Colombia.

> **AAA — exigencia máxima:** los criterios marcados como AAA representan
> el nivel más alto de accesibilidad. No se exige conformidad total AAA
> para todo el contenido, pero se recomienda donde sea viable.

## Índice por principio

- [1. Perceptible](#1-perceptible)
- [2. Operable](#2-operable)
- [3. Comprensible](#3-comprensible)
- [4. Robusto](#4-robusto)

Resumen de cantidades: **A = 32**, **AA = 24**, **AAA = 31** → total
**87 criterios** (WCAG 2.2). Criterios nuevos respecto a 2.1 marcados con
🆕: 2.4.11, 2.4.12, 2.4.13, 2.5.7, 2.5.8, 3.2.6, 3.3.7, 3.3.8, 3.3.9.
El criterio 4.1.1 (Procesamiento) fue **obsoleto** en WCAG 2.2.

---

## 1. Perceptible

La información y los componentes de la interfaz deben presentarse de modo
que los usuarios puedan percibirlos.

| SC | Nivel | Requisito WCAG | Cómo probarlo (auto / manual) | Herramienta | Ejemplo banca | Ejemplo retail |
|---|---|---|---|---|---|---|
| 1.1.1 | A | Contenido no textual: todo elemento no textual tiene alternativa textual | Inspeccionar `alt` en imágenes; revisar decorativas (`alt=""`) y funcionales | axe-core / `validate_semantic_html.py` | `alt="Gráfico de rentabilidad CDT Q3 2025: crecimiento del 4,2%"` | `alt="Tenis Nike Air Max 90 — talla 42, color negro/blanco"` |
| 1.2.1 | A | Audio/video pregrabado solo: alternativa | Verificar transcripción o descripción | Manual | Video explicativo de un crédito hipotecario con transcripción | Video de unboxing con transcripción |
| 1.2.2 | A | Subtítulos (pregrabado) | Revisar pista de subtítulos | Manual | Subtítulos en tutorial de app bancaria | Subtítulos en video de campaña |
| 1.2.3 | A | Audiodescripción o alternativa (pregrabado) | Verificar audiodescripción | Manual | Audiodescripción de demo de simulador de crédito | Audiodescripción de video de producto |
| 1.2.4 | AA | Subtítulos (en vivo) | Verificar subtítulos en directo | Manual | Webinar financiero en vivo con subtítulos | Live shopping con subtítulos |
| 1.2.5 | AA | Audiodescripción (pregrabado) | Verificar pista de audiodescripción | Manual | Video de educación financiera con audiodescripción | Video tutorial de armado con audiodescripción |
| 1.2.6 | AAA | Lengua de señas (pregrabado) | Verificar intérprete de LSC | Manual | Comunicado de condiciones de producto con LSC | Política de devoluciones con LSC |
| 1.2.7 | AAA | Audiodescripción extendida (pregrabado) | Verificar pausas con descripción | Manual | Tutorial complejo de banca empresarial | Video de instalación detallado |
| 1.2.8 | AAA | Alternativa para medio (pregrabado) | Verificar transcripción completa | Manual | Transcripción íntegra de webinar | Transcripción íntegra de demo |
| 1.2.9 | AAA | Audio solo (en vivo) | Verificar transcripción en vivo | Manual | Línea de atención con transcripción | Podcast en vivo con transcripción |
| 1.3.1 | A | Información y relaciones: estructura semántica | Inspeccionar `<th scope>`, headings, listas, `<label>` | axe-core / `validate_semantic_html.py` | Tabla de tasas con `<th scope="col">` por plazo | Tabla comparativa de productos con encabezados |
| 1.3.2 | A | Secuencia significativa: orden de lectura lógico | Desactivar CSS y revisar orden DOM | Manual / lector pantalla | Orden lógico en extracto de cuenta | Orden lógico en ficha de producto |
| 1.3.3 | A | Características sensoriales: no depender solo de forma/color/posición | Revisar instrucciones ("haga clic en el botón verde") | Manual | "Confirme con el botón Transferir" (no "el verde") | "Agregue con el botón Comprar" (no "el de la derecha") |
| 1.3.4 | AA | Orientación: no restringir a vertical/horizontal | Rotar dispositivo | Manual | App bancaria usable en horizontal y vertical | Catálogo usable en ambas orientaciones |
| 1.3.5 | AA | Identificar propósito de entrada: `autocomplete` | Inspeccionar `autocomplete` en campos de datos personales | axe-core | `autocomplete="cc-number"` en pago de tarjeta | `autocomplete="shipping postal-code"` en envío |
| 1.3.6 | AAA | Identificar propósito de componentes (ARIA) | Revisar roles y `aria-*` de regiones e íconos | Manual | Iconos de menú con propósito identificable | Iconos de carrito/favoritos identificables |
| 1.4.1 | A | Uso del color: no usar solo color para transmitir info | Revisar errores, enlaces, estados | Manual | Error de campo no solo en rojo (también texto/ícono) | Producto agotado no solo en gris (también etiqueta) |
| 1.4.2 | A | Control de audio: pausar audio que suena >3s | Verificar control de pausa | Manual | Sin audio automático en login | Sin audio automático en home |
| 1.4.3 | AA | Contraste mínimo 4.5:1 (texto normal), 3:1 (grande) | Medir ratio | `check_contrast.py` / CCA | Texto de tasas con ratio ≥ 4.5:1 | Precio con ratio ≥ 4.5:1 |
| 1.4.4 | AA | Redimensionar texto hasta 200% sin pérdida | Zoom navegador 200% | Manual | Extracto legible al 200% | Ficha de producto legible al 200% |
| 1.4.5 | AA | Imágenes de texto: usar texto real salvo logos | Buscar texto rasterizado | Manual | Tasas como texto, no imagen | Promociones como texto, no imagen |
| 1.4.6 | AAA | Contraste mejorado 7:1 (normal), 4.5:1 (grande) | Medir ratio | `check_contrast.py` | Ratio 7:1 en texto de tasas de interés | Ratio 7:1 en precios y descuentos |
| 1.4.7 | AAA | Audio de fondo bajo o nulo | Verificar nivel de fondo | Manual | Voz de IVR sin música de fondo alta | Audio de video sin fondo intrusivo |
| 1.4.8 | AAA | Presentación visual: ancho, interlineado, justificación | Revisar bloques de texto | Manual | Términos y condiciones con interlineado 1.5 | Política de devoluciones legible |
| 1.4.9 | AAA | Imágenes de texto sin excepción (salvo esencial) | Buscar texto en imagen | Manual | Ninguna tasa en imagen | Ningún precio en imagen |
| 1.4.10 | AA | Reflujo: contenido a 320px sin scroll en 2 ejes | Zoom 400% / viewport 320px | Manual | Transferencia usable a 320 CSS px | Checkout usable a 320 CSS px |
| 1.4.11 | AA | Contraste no textual 3:1 (UI y gráficos) | Medir bordes de inputs, íconos | `check_contrast.py` | Borde de campo de monto con 3:1 | Borde de selector de talla con 3:1 |
| 1.4.12 | AA | Espaciado de texto ajustable sin pérdida | Aplicar bookmarklet de espaciado | Manual | Extracto soporta espaciado custom | Descripción soporta espaciado custom |
| 1.4.13 | AA | Contenido en hover/focus: descartable, persistente | Probar tooltips | Manual | Tooltip de TEA descartable con Esc | Tooltip de talla persistente |

---

## 2. Operable

Los componentes de la interfaz y la navegación deben ser operables.

| SC | Nivel | Requisito WCAG | Cómo probarlo (auto / manual) | Herramienta | Ejemplo banca | Ejemplo retail |
|---|---|---|---|---|---|---|
| 2.1.1 | A | Teclado: toda función operable con teclado | Navegar solo con teclado | Manual | Transferencia completable con teclado | Compra completable con teclado |
| 2.1.2 | A | Sin trampa de teclado | Tabular por todo y salir | Manual | Modal de OTP no atrapa el foco | Modal de carrito no atrapa el foco |
| 2.1.3 | AAA | Teclado (sin excepción) | Navegar todo con teclado | Manual | Toda la banca operable por teclado | Todo el e-commerce operable por teclado |
| 2.1.4 | A | Atajos de carácter único: configurables | Revisar shortcuts de una tecla | Manual | Atajo de búsqueda remapeable | Atajo de búsqueda remapeable |
| 2.2.1 | A | Tiempo ajustable: extender/desactivar límites | Esperar timeout de sesión | Manual | Aviso y extensión antes de cerrar sesión | Aviso antes de expirar reserva de stock |
| 2.2.2 | A | Pausar, detener, ocultar (movimiento >5s) | Revisar carruseles/animaciones | Manual | Banner de campañas con pausa | Carrusel de productos con pausa |
| 2.2.3 | AAA | Sin tiempo límite (salvo tiempo real) | Verificar ausencia de límites | Manual | Diligenciar solicitud sin límite | Llenar formulario sin límite |
| 2.2.4 | AAA | Interrupciones posponibles/suprimibles | Revisar pop-ups y alertas | Manual | Avisos de promoción posponibles | Pop-ups de cupón posponibles |
| 2.2.5 | AAA | Reautenticación sin pérdida de datos | Expirar sesión a mitad de flujo | Manual | Reanudar transferencia tras re-login | Recuperar carrito tras re-login |
| 2.2.6 | AAA | Advertencia de timeout (pérdida de datos) | Verificar aviso de inactividad | Manual | Aviso 20h antes de expirar datos | Aviso antes de vaciar carrito |
| 2.3.1 | A | Tres destellos o menos | Revisar contenido parpadeante | Manual | Sin parpadeos en confirmaciones | Sin parpadeos en ofertas flash |
| 2.3.2 | AAA | Tres destellos (sin excepción) | Revisar todo el contenido | Manual | Ningún destello peligroso | Ningún destello peligroso |
| 2.3.3 | AAA | Animación por interacción: poder desactivar | Revisar `prefers-reduced-motion` | Manual | Respeta reducción de movimiento | Respeta reducción de movimiento |
| 2.4.1 | A | Evitar bloques: skip link/landmarks | Tab al primer enlace | `validate_semantic_html.py` | "Saltar al contenido" presente | "Saltar al contenido" presente |
| 2.4.2 | A | Título de página descriptivo | Revisar `<title>` | `validate_semantic_html.py` | `<title>Transferencias \| Banco X</title>` | `<title>Carrito \| Tienda Y</title>` |
| 2.4.3 | A | Orden de foco lógico | Tabular y observar orden | Manual | Foco lógico en formulario de crédito | Foco lógico en checkout |
| 2.4.4 | A | Propósito del enlace (en contexto) | Revisar texto de enlaces | Manual | Enlace "Ver detalle del crédito" | Enlace "Ver ficha del producto" |
| 2.4.5 | AA | Múltiples vías de navegación | Verificar buscador + menú + mapa | Manual | Buscador y menú en portal | Buscador, categorías y filtros |
| 2.4.6 | AA | Encabezados y etiquetas descriptivos | Revisar headings y labels | Manual | "Detalle de movimientos" claro | "Especificaciones del producto" claro |
| 2.4.7 | AA | Foco visible | Tabular y observar indicador | Manual | Anillo de foco visible en botones | Anillo de foco visible en checkout |
| 2.4.8 | AAA | Ubicación: breadcrumb/indicador | Revisar migas de pan | Manual | Breadcrumb en portal corporativo | Breadcrumb Categoría > Producto |
| 2.4.9 | AAA | Propósito del enlace (solo enlace) | Revisar texto aislado del enlace | Manual | Enlaces autoexplicativos | Enlaces autoexplicativos |
| 2.4.10 | AAA | Encabezados de sección | Revisar estructura de headings | `validate_semantic_html.py` | Secciones con headings en extracto | Secciones con headings en ficha |
| 2.4.11 🆕 | AA | Foco no oculto (mínimo) | Verificar que el foco no quede tapado | Manual | Foco no tapado por barra fija de sesión | Foco no tapado por barra de carrito |
| 2.4.12 🆕 | AAA | Foco no oculto (mejorado) | Verificar foco totalmente visible | Manual | Foco 100% visible en formularios | Foco 100% visible en checkout |
| 2.4.13 🆕 | AAA | Apariencia del foco (tamaño/contraste) | Medir grosor y contraste del foco | `check_contrast.py` | Indicador de foco grueso y contrastado | Indicador de foco grueso y contrastado |
| 2.5.1 | A | Gestos de puntero: alternativa simple | Revisar gestos multipunto/trazo | Manual | Firma con alternativa de un punto | Zoom de producto con alternativa |
| 2.5.2 | A | Cancelación de puntero | Probar arrastrar fuera para cancelar | Manual | Botón Pagar cancelable al soltar fuera | Botón Comprar cancelable al soltar fuera |
| 2.5.3 | A | Etiqueta en el nombre accesible | Comparar texto visible vs nombre AT | axe-core | Botón "Transferir" coincide con su `aria-label` | Botón "Comprar" coincide con su `aria-label` |
| 2.5.4 | A | Activación por movimiento: alternativa | Probar funciones por agitar/inclinar | Manual | Confirmación con alternativa a sacudir | Funciones de movimiento con alternativa |
| 2.5.5 | AAA | Tamaño del objetivo (mejorado) 44×44px | Medir botones e íconos | Manual | Botones de teclado numérico ≥ 44px | Botones +/- de cantidad ≥ 44px |
| 2.5.6 | AAA | Mecanismos de entrada concurrentes | Probar teclado + táctil + ratón | Manual | Soporta varios métodos de entrada | Soporta varios métodos de entrada |
| 2.5.7 🆕 | AA | Movimientos de arrastre: alternativa | Revisar sliders y reordenamientos | Manual | Slider de monto con alternativa de input | Reordenar lista con alternativa a drag |
| 2.5.8 🆕 | AA | Tamaño del objetivo (mínimo) 24×24px | Medir objetivos táctiles | Manual | Iconos de acción ≥ 24×24px | Iconos de carrito/favorito ≥ 24×24px |

---

## 3. Comprensible

La información y el manejo de la interfaz deben ser comprensibles.

| SC | Nivel | Requisito WCAG | Cómo probarlo (auto / manual) | Herramienta | Ejemplo banca | Ejemplo retail |
|---|---|---|---|---|---|---|
| 3.1.1 | A | Idioma de la página: `lang` | Inspeccionar `<html lang>` | `validate_semantic_html.py` | `<html lang="es-CO">` | `<html lang="es-CO">` |
| 3.1.2 | AA | Idioma de partes | Revisar `lang` en fragmentos | Manual | Término en inglés con `lang="en"` | Marca extranjera con `lang` apropiado |
| 3.1.3 | AAA | Palabras inusuales: glosario | Revisar jerga financiera definida | Manual | Glosario de TEA, TIR, mora | Glosario de tallas, materiales |
| 3.1.4 | AAA | Abreviaturas: expansión | Revisar `<abbr title>` | Manual | `<abbr title="Tasa Efectiva Anual">TEA</abbr>` | `<abbr title="Stock Keeping Unit">SKU</abbr>` |
| 3.1.5 | AAA | Nivel de lectura: alternativa simple | Evaluar legibilidad del texto | Manual | Versión simple de condiciones | Versión simple de políticas |
| 3.1.6 | AAA | Pronunciación cuando sea ambigua | Revisar guías de pronunciación | Manual | Términos ambiguos con guía | Términos ambiguos con guía |
| 3.2.1 | A | Al recibir foco: sin cambio de contexto | Tabular sin que se dispare navegación | Manual | Foco en campo no envía formulario | Foco en filtro no recarga página |
| 3.2.2 | A | Al recibir entrada: sin cambio inesperado | Escribir/seleccionar sin auto-submit | Manual | Seleccionar plazo no envía solicitud | Elegir talla no recarga sin aviso |
| 3.2.3 | AA | Navegación consistente | Comparar menús entre páginas | Manual | Menú igual en todo el portal | Menú igual en toda la tienda |
| 3.2.4 | AA | Identificación consistente | Comparar íconos/etiquetas repetidas | Manual | "Cerrar sesión" igual en todo el sitio | "Agregar al carrito" consistente |
| 3.2.5 | AAA | Cambio bajo petición | Verificar que cambios sean iniciados | Manual | Sin auto-actualización de saldo intrusiva | Sin recargas automáticas del catálogo |
| 3.2.6 🆕 | A | Ayuda consistente (misma ubicación) | Revisar posición del contacto/ayuda | Manual | Enlace de ayuda en misma posición | Chat/ayuda en misma posición |
| 3.3.1 | A | Identificación de errores | Provocar error de validación | Manual | Error de monto identificado en texto | Error de tarjeta identificado en texto |
| 3.3.2 | A | Etiquetas o instrucciones | Revisar labels e instrucciones | `validate_semantic_html.py` | Campo de cuenta con formato indicado | Campo de tarjeta con formato indicado |
| 3.3.3 | AA | Sugerencia ante error | Provocar error y leer sugerencia | Manual | "El monto excede su saldo disponible" | "El cupón ha expirado, pruebe otro" |
| 3.3.4 | AA | Prevención de errores (legal/financiero) | Verificar revisión/confirmación | Manual | Resumen confirmable antes de transferir | Resumen confirmable antes de pagar |
| 3.3.5 | AAA | Ayuda contextual | Revisar ayuda por campo | Manual | Ayuda contextual en campo de NIT | Ayuda contextual en campo de envío |
| 3.3.6 | AAA | Prevención de errores (todo) | Verificar confirmación en todo envío | Manual | Confirmación en toda transacción | Confirmación en todo pedido |
| 3.3.7 🆕 | A | Entrada redundante: no re-pedir datos | Revisar pasos que repiten datos | Manual | No re-pedir datos ya ingresados | Reusar dirección entre pasos |
| 3.3.8 🆕 | AA | Autenticación accesible (mínimo) | Revisar login sin prueba cognitiva | Manual | Login sin acertijo; permite gestor/pegar | Login sin acertijo; permite pegar |
| 3.3.9 🆕 | AAA | Autenticación accesible (mejorado) | Revisar ausencia de prueba cognitiva | Manual | Sin reconocimiento de objetos en login | Sin reconocimiento de objetos en login |

---

## 4. Robusto

El contenido debe ser suficientemente robusto para ser interpretado por
una amplia variedad de agentes de usuario, incluidas las tecnologías de
asistencia.

| SC | Nivel | Requisito WCAG | Cómo probarlo (auto / manual) | Herramienta | Ejemplo banca | Ejemplo retail |
|---|---|---|---|---|---|---|
| 4.1.1 | A | ~~Procesamiento (parsing)~~ — **obsoleto en WCAG 2.2** | No se evalúa | — | N/A | N/A |
| 4.1.2 | A | Nombre, rol, valor (componentes) | Revisar ARIA y nombres accesibles | axe-core | Botón de OTP con nombre/rol/estado | Filtro de catálogo con nombre accesible |
| 4.1.3 | AA | Mensajes de estado (live regions) | Provocar cambio dinámico y escuchar | Lector pantalla | "Transferencia exitosa" anunciado | "Producto agregado al carrito" anunciado |

> Nota: aunque 4.1.1 quedó obsoleto, mantener HTML válido sigue siendo
> buena práctica para robustez y compatibilidad con tecnologías de
> asistencia.

---

## Cómo usar este checklist

1. Filtra por el **nivel de conformidad** objetivo (A, AA o AAA).
2. Para cada SC, ejecuta la prueba indicada en *Cómo probarlo*.
3. Usa la herramienta sugerida; los scripts `check_contrast.py` y
   `validate_semantic_html.py` están en la carpeta `scripts/`.
4. Documenta cada hallazgo con el formato estandarizado del `SKILL.md`.
5. Adapta el ejemplo de banca o retail según la industria auditada
   (ver `references/verticales/banca.md` y `retail.md`).
