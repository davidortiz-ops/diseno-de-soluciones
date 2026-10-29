---
name: criterio-diseno
description: Criterio de diseño de experiencia (UX) e interfaz (UI) aplicable a cualquier proyecto. Usar SIEMPRE que se construya, modifique o critique una interfaz, componente, página, prototipo, catálogo o render — en cualquier stack. Cubre jerarquía visual, espaciado, color, tipografía, movimiento, estados, flujos, formularios, accesibilidad (WCAG 2.2 AA) y microcopy. También aplica al criticar diseños existentes.
---

# Criterio de diseño UX/UI

Reglas de oficio para que cualquier interfaz salga profesional, usable y
con estética contemporánea sobria. Son independientes del proyecto: se
expresan sobre el sistema visual QUE EL PROYECTO TENGA, nunca sobre
valores inventados.

## Paso 0 — Descubrir el lenguaje del proyecto (siempre primero)

Antes de diseñar o criticar, identifica el sistema visual existente:
tokens de diseño (JSON, variables CSS, theme de Tailwind/MUI/etc.),
tipografías cargadas, componentes ya construidos y sus convenciones.
- Si existe: TODO valor visual sale de ahí. Nada a mano. Las reglas de
  abajo se aplican con SUS escalas (su spacing, sus radios, sus colores).
- Si NO existe: no improvises valores dispersos — propón primero una base
  mínima (escala de espaciado de un solo ritmo, 2 fuentes máximo, escala
  tipográfica de 5-7 tamaños, paleta de neutros + 1 acento + colores de
  estado, escala de radios, 2-3 duraciones de movimiento) y constrúyelo
  todo sobre esa base.
- Si el proyecto tiene reglas propias (guías, contratos, design system),
  esas mandan sobre este criterio; este criterio llena lo que ellas no
  definan.

## Jerarquía visual (lo primero que se juzga)

- Una sola cosa domina por vista. Si todo grita, nada se oye: un titular
  claro, y todo lo demás un escalón abajo deliberadamente.
- Máximo tres niveles de énfasis de texto por bloque (principal, apoyo,
  metadato). Cuatro grises distintos en un bloque = jerarquía rota.
- El tamaño no es la única herramienta: peso, color y espacio jerarquizan
  con más elegancia que agrandar.
- Datos duros (cifras, fechas, código, IDs) en monoespaciada si el
  proyecto la tiene: alinean, escanean mejor y dan carácter técnico.

## Espacio y alineación (el lujo es aire)

- Un solo ritmo de espaciado en todo el proyecto (típicamente base 4 u 8).
  Valores fuera de la escala son ruido.
- El espacio agrupa: más aire ENTRE grupos que DENTRO de ellos (ley de
  proximidad). Si hay que dibujar cajas y líneas para separar, suele
  faltar espacio, no bordes.
- Alineación a retícula estricta: los inicios de un mismo nivel caen en la
  misma vertical. Desalineaciones de 2-4px destruyen la percepción de
  calidad más que cualquier otro defecto.
- Ante la duda entre denso y aireado: aireado. Ancho de lectura de texto
  corrido: 60-80 caracteres, nunca pantalla completa.

## Color (disciplina de acentos)

- Regla 90/9/1: ~90% neutros (superficies y texto), ~9% el acento
  interactivo, ~1% acentos especiales o de marca. El color abundante se
  devalúa.
- UNA acción primaria por vista lleva el acento pleno; el resto de lo
  interactivo usa versiones suaves del acento o estilos secundarios.
- Los colores de estado (error, éxito, alerta) se reservan para estados
  reales; jamás como decoración. El rojo decorativo es el peor ruido.
- Profundidad por contraste de superficies y bordes sutiles antes que por
  sombras duras. Si hay escala de elevación, úsala; si no, propónla.
- Todo par fondo/texto cumple contraste WCAG AA (4.5:1 texto normal,
  3:1 texto grande y componentes de UI) — verificado en todos los temas
  que el proyecto soporte.

## Tipografía

- Máximo dos familias. La jerarquía sale de la escala y el peso, no de
  cambiar fuentes.
- Titulares: tracking apenas negativo y line-height apretado. Texto
  corrido: line-height 1.4-1.6. Etiquetas pequeñas en mayúsculas: tracking
  positivo.
- No usar tamaños fuera de la escala del proyecto; si falta un escalón, se
  propone a la escala, no se inventa localmente.

## Movimiento (lo que separa correcto de premium)

- Todo cambio de estado interactivo transiciona; nada aparece o cambia "de
  golpe". Micro-feedback en hover/press: rápido (~100-150ms, ease-out);
  entradas y cambios de estado: medio (~200-250ms); paneles y overlays:
  lento (~300-400ms, ease-in-out).
- El movimiento comunica causa-efecto (de dónde viene, a dónde va), nunca
  decora. Prohibido: rebotes gratuitos, loops infinitos, parallax
  decorativo, retrasos perceptibles.
- Respetar prefers-reduced-motion: reducir a opacidad o eliminar.

## Estados (una interfaz es TODOS sus estados)

Toda pieza o vista se diseña con su familia completa de estados; entregar
solo el "caso feliz" es entregar la mitad:
- Interactivos: hover, foco VISIBLE (anillo de foco siempre; foco
  invisible es una falla de accesibilidad, no una elección estética),
  activo/presionado, deshabilitado (atenuado, sin hover, cursor acorde).
- Vacío: qué está vacío, por qué importa y UNA acción para empezar. Un
  área en blanco no es un estado vacío.
- Cargando: skeletons con las superficies del sistema (no spinners
  genéricos) si la espera puede superar ~400ms; conservar el layout para
  evitar saltos (CLS).
- Error: qué pasó + qué hacer, en tono calmado y sin culpar al usuario;
  el error se muestra junto a lo que falló, no solo en un toast lejano.
- Éxito/confirmación: feedback visible de que la acción ocurrió.

## Flujos y experiencia (UX)

- Cada vista responde tres preguntas en segundos: ¿dónde estoy?, ¿qué
  puedo hacer?, ¿cuál es el siguiente paso? Si no, falta jerarquía o
  sobra contenido.
- Minimizar pasos y decisiones por pantalla (una decisión principal por
  paso en flujos críticos). Divulgación progresiva: lo avanzado se
  esconde detrás de "más opciones", no compite con lo esencial.
- Acciones destructivas o costosas: protegidas (confirmación explícita o
  deshacer), separadas visualmente de las frecuentes, y nunca donde un
  clic por inercia las alcance.
- Reversibilidad: preferir "deshacer" a "¿estás seguro?" cuando sea
  técnicamente posible; los diálogos de confirmación en cadena entrenan
  a ignorarlos.
- Consistencia interna sobre originalidad: el mismo patrón para el mismo
  problema en todo el producto, aunque exista una alternativa "mejor".

## Formularios (donde la UX se gana o se pierde)

- Etiquetas siempre visibles, encima del campo; el placeholder es ejemplo
  o formato, nunca reemplaza la etiqueta.
- Validar en el momento correcto: al perder foco o al enviar; nunca
  regañar mientras se escribe la primera vez.
- Ser tolerante con la entrada (espacios, mayúsculas, formatos de
  teléfono/fecha): normalizar en código antes que rechazar al usuario.
- Marcar lo OPCIONAL si casi todo es obligatorio (o al revés); pedir solo
  lo necesario para el paso actual.
- El botón de envío dice lo que hace ("Crear cuenta", no "Enviar") y
  muestra estado de progreso al ejecutarse.

## Accesibilidad (no negociable — meta: WCAG 2.2 nivel AA)

La accesibilidad no es una sección al final: es un criterio transversal
que ya aparece en color (contraste), movimiento (reduced-motion), estados
(foco) y formularios (etiquetas y errores). Esta sección fija el estándar
completo. Referencia: WCAG 2.2 AA; los números citados son sus criterios.

### Perceptible
- Contraste mínimo (1.4.3): 4.5:1 texto normal, 3:1 texto grande (18px+
  o 14px+ bold). Contraste de no-texto (1.4.11): 3:1 para bordes de
  inputs, iconos significativos, estados de foco y partes de gráficos.
  Verificado en TODOS los temas del proyecto.
- El color nunca es el único portador de significado (1.4.1): todo estado
  o categoría se acompaña de icono, texto o forma. Probar la vista en
  escala de grises: si algo se vuelve indistinguible, falla.
- Texto real, no imágenes de texto (1.4.5). Todo contenido no textual con
  alternativa (1.1.1): alt descriptivo en imágenes informativas, alt=""
  en decorativas, aria-label en botones de solo icono.
- Reflow (1.4.10): la vista funciona a 320px de ancho y con zoom de texto
  al 200% (1.4.4) sin scroll horizontal ni contenido cortado.
- Espaciado de texto (1.4.12): el layout sobrevive si el usuario aumenta
  line-height/letter-spacing (no contenedores de altura fija con texto).

### Operable
- Todo operable por teclado (2.1.1), sin trampas de foco (2.1.2), en un
  orden que sigue la lógica visual (2.4.3). Los atajos de un solo
  carácter, desactivables o remapeables (2.1.4).
- Foco SIEMPRE visible (2.4.7) y no oscurecido por otros elementos como
  headers pegajosos (2.4.11). El anillo de foco cumple el contraste 3:1.
- Objetivos táctiles: mínimo 24x24px con separación (2.5.8, AA) y
  recomendado 44x44px en móvil; acciones destructivas nunca adyacentes
  sin separación a las frecuentes.
- Gestos complejos (arrastrar, pellizcar) siempre con alternativa de un
  solo puntero (2.5.7, 2.5.1). Nada se activa solo con hover.
- Sin límites de tiempo no ajustables (2.2.1); todo lo que se mueve o
  actualiza solo, pausable (2.2.2). Nada parpadea más de 3 veces por
  segundo (2.3.1).
- prefers-reduced-motion respetado (2.3.3): transiciones reducidas a
  opacidad o eliminadas; nunca ignorar la preferencia.

### Comprensible
- Etiquetas visibles y programáticamente asociadas a su control (1.3.1,
  3.3.2): label con for/id o aria-labelledby; el placeholder jamás
  sustituye a la etiqueta. El nombre accesible contiene el texto visible
  (2.5.3).
- Errores identificados en texto (3.3.1), junto al campo que falló,
  descritos con sugerencia de corrección (3.3.3), y anunciados a lectores
  de pantalla (aria-describedby + aria-invalid; role=alert si es global).
- Acciones legales/financieras/destructivas: reversibles, verificables o
  confirmadas (3.3.4). No pedir dos veces lo ya dado en el flujo (3.3.7).
- La navegación y los patrones se repiten consistentes en todo el
  producto (3.2.3, 3.2.4). Nada cambia de contexto solo por recibir foco
  o por escribir (3.2.1, 3.2.2).
- Idioma de la página declarado (3.1.1); lenguaje simple, sin jerga.

### Robusto
- Semántica primero, ARIA después: button es <button>, lista es <ul>,
  encabezados en jerarquía real h1->h2->h3 sin saltos (1.3.1). ARIA solo
  para lo que HTML no expresa, y correcto (un aria-* mal puesto es peor
  que ninguno).
- Los mensajes de estado que aparecen sin mover el foco (guardado,
  cargando, resultados de búsqueda) usan live regions (4.1.3).
- Componentes con nombre, rol y valor programáticos (4.1.2): un toggle
  expone role=switch + aria-checked; un acordeón, aria-expanded; un
  modal, foco atrapado dentro y devuelto al origen al cerrar.

### Cómo se verifica (mínimo por entrega)
1. Recorrido completo solo con teclado: ¿llego a todo, veo dónde estoy,
   puedo salir de todo?
2. Contraste de texto, bordes de controles y foco, en todos los temas.
3. Vista en gris: ¿el color era el único diferenciador de algo?
4. Zoom 200% y viewport 320px: ¿reflow sin pérdida?
5. Lectura con lector de pantalla (o auditoría de árbol de accesibilidad):
   ¿los nombres, roles y estados se anuncian con sentido?
6. prefers-reduced-motion activado: ¿la interfaz sigue completa?

## Contenido y microcopy

- Claridad sobre cleverness: verbos concretos, frases cortas, cero jerga
  interna en la UI.
- Los botones nombran la acción y su objeto; los títulos nombran el
  contenido, no el mecanismo ("Tu pedido", no "Vista de detalle").
- Tono consistente en todo el producto, definido una vez (cercano/neutro/
  formal); los errores jamás culpan ni alarman de más.
- Números, fechas y monedas en el formato local del usuario.

## Anti-patrones (rechazar aunque los pidan "para que se vea moderno")

- Gradientes decorativos, glassmorphism, neón, sombras de colores,
  degradados en texto.
- Emojis como iconografía de interfaz; iconos de familias mezcladas.
- Texto corrido centrado; párrafos a todo el ancho de la pantalla.
- Carruseles automáticos, popups de entrada, animaciones en loop.
- Dark patterns: urgencia falsa, opciones preseleccionadas contra el
  usuario, botones de rechazo escondidos o avergonzantes (confirmshaming).
- "Llenar" el espacio vacío con adornos: el vacío bien jerarquizado ES
  diseño.

## Protocolo de crítica (al evaluar una interfaz existente)

Evaluar en este orden y reportar hallazgos estructurados (qué, dónde,
cómo se resuelve, y a qué capa pertenece: sistema visual / componente /
contenido) — sin corregir en silencio si el proyecto tiene proceso de
aprobación:
1. Jerarquía: ¿qué domina? ¿se entiende la vista en 5 segundos?
2. Alineación y ritmo de espaciado.
3. Estados faltantes (foco, vacío, cargando, error).
4. Accesibilidad: recorrido por teclado, contraste (texto y no-texto),
   semántica/nombres accesibles, reflow — en todos los temas.
5. Consistencia con los patrones del propio producto.
6. Movimiento ausente, excesivo o sin causa-efecto.
7. Disciplina de color y una-acción-primaria.
8. Microcopy: botones, errores, títulos.
Priorizar por impacto en el usuario, no por facilidad de arreglo.
