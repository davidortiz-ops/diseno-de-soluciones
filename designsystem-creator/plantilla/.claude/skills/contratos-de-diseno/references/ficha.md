# Ficha de pieza

Texto canónico de la ficha. Úsala como guion de entrevista, no como formulario a pegar (salvo que el usuario pida verla completa).

```
FICHA DE PIEZA

1. Nombre de la pieza:            ___________________________
2. ¿Qué es?  (elige uno)          átomo / molécula / organismo / plantilla
3. ¿Qué logra para el usuario?    ___________________________
4. ¿Qué datos maneja?             (lista; marca cuáles son OBLIGATORIOS)
     - ___________________  obligatorio? sí/no
5. ¿Qué acciones dispara?         (ej: enviar, eliminar; ¿cuesta dinero?, ¿qué protección?)
6. ¿Qué mensajes muestra y con qué tono?
7. ¿Qué decide esta pieza?        (¿hay un punto donde se sigue o se rechaza?)
8. ¿Qué queremos medir aquí?
9. ¿Qué guardrails aplican?       (ej: accesibilidad, rechazo con dignidad)
10. Si es organismo/plantilla: ¿de qué piezas más pequeñas está hecha?
```

## Guía por pregunta (para entrevistar bien)

- **1. Nombre**: en lenguaje humano; tú lo conviertes a `component_id` (minúsculas-con-guiones).
- **2. Tipo**: NO esperes que el diseñador lo sepa (es normal que dude). Decídelo tú con el árbol de decisión de abajo, decláralo en una frase y deja que corrija si describió mal la pieza.
- **3. Intención**: una frase orientada al usuario final ("permite corregir el monto antes de confirmar"), no a la implementación.
- **4. Datos**: lo que la pieza recibe o muestra. Insiste en marcar obligatorios — es lo que más se les olvida.
- **5. Acciones**: verbos. Pregunta explícitamente si alguna cuesta dinero o es irreversible → eso obliga a definir la protección (confirmación, doble paso).
- **6. Mensajes**: textos visibles y su tono (cercano, neutro, formal). Incluye mensajes de error si el usuario los conoce.
- **7. Decisión**: ¿la pieza tiene un punto de sigue/rechaza? (validación, aprobación, límite). Muchas piezas no lo tienen; en blanco está bien.
- **8. Medición**: qué evento o métrica importa aquí (tasa de éxito, abandono, clics).
- **9. Guardrails**: restricciones del negocio o de trato al usuario (accesibilidad, rechazo con dignidad, no ocultar costos).
- **10. Composición**: solo organismos/plantillas. Pide los nombres de las piezas hijas; tú los mapeas a sus `component_id`.

## Árbol de decisión del tipo (lo aplica el compilador, nunca el diseñador)

El criterio es **composición + comportamiento**, no tamaño. Evaluar en orden con la respuesta a "¿de qué piezas está hecha?":

1. **¿Contiene otras piezas con contrato?** No → **átomo**. Es indivisible; su contrato lleva `variantes`, `comun/estilos` y `tokens_que_usa`. Ej: campo, boton, badge, boton-icono.
2. **¿Solo agrupa y adorna, sin lógica propia?** Contiene átomos pero no tiene acciones ni estados propios (más allá de los de sus átomos): etiqueta + campo + insignia → **molécula**. Ej: campo-etiquetado (cero `acciones:`).
3. **¿Compone piezas Y tiene comportamiento propio?** Acciones propias (eliminar, agregar), estados propios (error de fila, vacía), layout con rejilla, datos que fluyen entre sus piezas → **organismo**. Ej: fila-condicion (acción alEliminar + rejilla), seccion-repetible (molde con params), info-general, resumen-en-vivo.
4. **¿Compone organismos y es la vista completa?** Punto de entrada del render, no dibuja campos directamente, puede tener `presentacion` (drawer/página/modal) y `modo` (crear/editar) → **plantilla**. Ej: crear-paquete.

Señales rápidas desde la entrevista:
- El diseñador nombra piezas que ya tienen contrato ("dos listas, una caja, el bote de basura") → mínimo molécula; si además hay una acción o validación → organismo.
- El diseñador describe una pantalla o panel ("el drawer donde se crea el paquete") → plantilla.
- La pieza tiene acción destructiva o de agregar/quitar → nunca es molécula.
- Duda razonable entre molécula y organismo → preguntar solo "¿esta pieza hace algo por sí misma (validar, agregar, quitar), o solo muestra sus partes juntas?" y decidir.

El tipo determina qué claves lleva el contrato: átomo → tokens_que_usa/estilos; molécula → usa + layout simple; organismo → usa con roles + layout ejecutable + acciones; plantilla → usa de organismos + presentacion/modo, sin campos directos.

## Entrevista para PLANTILLAS (pantallas completas)

Cuando el árbol de decisión da plantilla, la entrevista cambia de énfasis: no se pregunta por datos campo a campo (eso vive en los contratos hijos), se pregunta por composición, modos y recorrido. Las seis preguntas:

1. **Recorrido**: "Recorre la pantalla de arriba a abajo y nómbrame cada bloque que ves, aunque parezca menor." — Esta pregunta existe para atrapar piezas que se olvidan al descomponer (auditorías, footers, estados especiales). Repreguntar una vez: "¿algo más, por pequeño que sea?"
2. **Presentación**: ¿página completa, panel lateral (drawer), ventana emergente (modal)?
3. **Modos**: ¿crear/editar/ver? ¿Qué cambia entre ellos? ¿Algún bloque aparece SOLO en uno? → `solo_en:`.
4. **Organización gruesa**: ¿una columna, dos, formulario + resumen? Sin medidas finas; las medidas van como NOTA si no salen de código real.
5. **Acciones globales**: guardar, cancelar, publicar. ¿Alguna cuesta dinero o es irreversible? → protección.
6. **Medición**: qué eventos importan a nivel de pantalla (la medición vive aquí, no en las piezas).

Al compilar la plantilla:
- Mapear CADA bloque del recorrido a un contrato existente por `component_id`. Bloque sin contrato → no inventarlo: marcarlo PENDIENTE y proponer contratarlo primero (orden de dependencias: átomos → moléculas → organismos → plantilla).
- Si el diseñador describe 3+ bloques "muy parecidos" → regla del molde: reutilizar (o proponer) UN organismo con `params` en vez de contratos casi iguales.
- La plantilla nunca dibuja campos directamente: solo compone organismos.
- Numeración/orden de secciones: inferir del recorrido, con NOTA si no es explícito.
- Si todas las hijas están contratadas y LISTAS → ofrecer armar el paquete completo de inmediato (Modo proyecto).

## Entrevista para ORGANISMOS de formulario (estructura fija con campos)

Cuando el organismo es un formulario con acomodo fijo (no una lista repetible), agregar dos preguntas a la ficha:

- **Acomodo, fila por fila**: "¿Cómo se acomodan los campos? Recórrelos: ¿cuáles van lado a lado y cuáles ocupan todo el ancho?" — La respuesta en lenguaje humano ("nombre y versión lado a lado; estado solito a lo ancho") se traduce a rejilla con `celda: { fila, columna }` por pieza y mapa de celdas comentado en `layout`. El diseñador nunca dice "grid" ni "1fr"; eso es del compilador.
- **Campos especiales**: "¿Algún campo bloqueado, que se calcule solo, o con insignia/ícono?" — Bloqueado → `estado: deshabilitado` + nota; el estilo del indicador (candado gris `text-tertiary`, sin acento) lo fija el harness, no el diseñador; insignia → `badge` de la molécula.

## Chequeo de dependencias entre contratos (al compilar composición)

Cada vez que un contrato pide una pieza con `variantes`, `estado` u opción específica, verificar que el contrato de esa pieza LA TENGA:
- La pide y existe → seguir.
- La pide y NO existe (ej: la composición necesita `tipo: fecha` y el átomo solo tiene `[texto, lista]`) → `# HALLAZGO:` en el contrato nuevo + proponer actualizar el contrato del átomo PRIMERO (es un cambio del dueño del sistema: agregar la opción al eje, no parchar por fuera).
- La pieza no tiene contrato → PENDIENTE, contratar de abajo hacia arriba.
Este chequeo convierte en error de compilación lo que antes se descubría en un render roto.

## Regla de oro de la entrevista

Si una pregunta es técnica (estados internos, cableado a tokens, accesibilidad detallada), **no se le hace al humano**. Eso lo agrega el compilador. La ficha es deliberadamente no-técnica: es la única interfaz del diseñador con el sistema.

## Contradicciones y estructuras "para cada línea" (lección de render real)

- Si una respuesta de la entrevista **contradice** la descripción original (ej: primero "el texto va en negro", después "texto en gris"), el compilador NO reconcilia ni promedia en silencio: muestra las dos versiones lado a lado y pregunta cuál manda. Una contradicción sin resolver produce un contrato que ninguna imagen de referencia va a cumplir.
- Si el usuario describe una estructura de línea ("icono + texto gris + valor a la derecha") en una pieza con **varios grupos** (condiciones, tarifas, beneficios), confirmar A QUÉ grupo(s) aplica antes de compilarla. Aplicarla al grupo equivocado fue la causa del primer contrato defectuoso en producción.
- "Al lado derecho" es ambiguo: ¿inmediatamente después del texto, o alineado al borde derecho del contenedor? Si importa, preguntar con esas dos opciones.
