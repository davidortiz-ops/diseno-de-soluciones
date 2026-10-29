---
name: auditoria-de-flujos
description: Audita la trazabilidad entre la investigación de usuario existente (dolores, necesidades, oportunidades) y un flujo ya diseñado en Figma, Miro, Condens o capturas, para saber qué dolores resuelve, cuáles no, qué partes del flujo no tienen sustento, qué huecos tiene la investigación y qué debe probarse con usuario antes de entregar. Usa esta skill SIEMPRE que el usuario diga "audita este flujo", "confronta el flujo con la investigación", "valida si este flujo resuelve los dolores", "el cliente nos mandó su research y quiero saber si me sirve", "no tenemos tiempo de probar con usuarios", "revisa si el diseño responde a las necesidades", "qué le falta a esta investigación", "quiero rigor antes de entregar", o cuando comparta un flujo, blueprint, journey o service map junto con hallazgos de investigación y quiera saber si uno responde al otro, aunque no diga "auditoría". Úsala también de forma proactiva cuando un diseñador vaya a entregar un flujo apoyado en investigación previa y no en pruebas con usuarios.
---

# Auditoría de flujos contra investigación

Esta skill es la **compuerta de rigor antes de entregar**. La usa un diseñador de producto, UX o service designer que no puede probar con usuarios —porque el negocio no lo permite o porque ya existe investigación previa— y necesita saber si el flujo que diseñó realmente responde a los dolores documentados.

**Idioma:** todo el flujo y los entregables en español.

## Lo que esta skill hace y lo que no

No valida. Validar es un veredicto de verdad y eso solo lo da un usuario real. Lo que hace es **auditar la trazabilidad** entre la evidencia disponible y las decisiones del diseño: qué dolor está cubierto, dónde, cómo, con qué calidad de evidencia, y qué sigue siendo apuesta.

Esta distinción no es retórica. Si el informe dice "validado", el negocio lo usará como certificado para nunca probar con usuarios, que es exactamente el riesgo que la skill debe reducir. Por eso:

- **Nunca emitas un veredicto global** tipo "aprobado", "el flujo es correcto" o un porcentaje de cumplimiento. No existe esa figura en el entregable.
- **Nunca uses la palabra "validado"** para algo sustentado solo en investigación documental.
- El cierre del informe es **qué NO se puede afirmar al entregar**, no un sello.

La auditoría es siempre completa. No hay modo rápido: si alguien pide "solo un chequeo veloz", explica que esta skill es el rigor previo a la entrega y que el valor está en el recorrido completo, y ofrece hacerlo por partes del flujo si el tiempo aprieta.

## Tu sesgo es el enemigo principal

Al recibir un flujo y una investigación, tu tendencia natural es encontrar la narrativa que los concilia. Ese es el modo de falla más probable de toda la skill. Contramedidas obligatorias:

- Por cada dolor que marques como resuelto, escribe **la condición que lo haría falso** ("esto falla si el usuario llega sin haber hecho X") y la señal observable que lo probaría.
- La auditoría no cierra sin declarar **al menos un riesgo no cubierto**, aunque el flujo se vea bien. Si crees que no hay ninguno, no buscaste lo suficiente.
- Ningún veredicto puede ser más fuerte que la evidencia que lo sostiene (ver `references/juicio.md`).

## El recorrido

Siete pasos en orden. Tres tienen **aprobación explícita del usuario**: sin ella no avanzas, porque todo el juicio posterior se apoya en una interpretación tuya que nadie revisó.

### Paso 1 — Qué se va a auditar y con qué

Antes de leer nada, pregunta (si tienes disponible una herramienta de opciones interactivas, úsala; si no, pregunta en texto, agrupado, no de a una):

1. **Tipo de artefacto:** ¿flujo de producto (pantallas, pasos, estados) o blueprint / modelo de proceso (servicio con backstage, handoffs, cambios de canal)? Esto cambia el lente completo — ver `references/blueprint.md` si es lo segundo.
2. **Dónde está la investigación:** Condens, documento de resultados (PDF/Word), tablero de Miro, o varias.
3. **Dónde está el flujo:** Figma, Miro, capturas.
4. **Quién hizo la investigación:** equipo propio o el cliente. Si es del cliente, el brief de vacíos es el entregable más importante de la sesión.

### Paso 2 — Verificar conexiones de verdad

**No asumas que tienes conectores.** Esta skill corre con la sesión de cada diseñador y cada uno tiene los suyos. Para cada fuente que el usuario nombró, verifica en dos capas:

1. **Que el MCP exista** en las herramientas disponibles de esta sesión (búscalo si el entorno usa carga diferida de herramientas).
2. **Que responda.** Haz una llamada real de prueba —listar workspaces, leer metadata del archivo— antes de prometer nada. Un Figma conectado sin permiso sobre ese archivo, o un Condens que devuelve vacío, se ven idénticos a uno sano en la lista de conectores y fallan en el paso siguiente, cuando ya prometiste.

Si falla cualquiera de las dos capas, dilo sin drama y pasa al plan B: capturas organizadas. El detalle de cada fuente y del plan B está en `references/fuentes.md`.

### Paso 3 — Cómo debe entregarte la información

Si la fuente es un tablero (Miro, o un Figma con muchas páginas), **da la recomendación de organización antes de leer nada**. El costo de que leas mal un tablero lo paga el diseñador en credibilidad frente a su equipo.

Pídele que separe en dos zonas nombradas —una con la investigación, otra con el flujo— y que te diga los nombres de frames o secciones. Guion exacto y variantes por herramienta en `references/fuentes.md`.

### Paso 4 — Ingesta de la investigación

**Si es Condens:** busca por el tema del flujo, y presenta lo que encontraste como lista con **título, resumen de dos líneas y link**. El usuario elige cuáles entran. **Sin selección explícita no continúas** — si buscas y usas todo lo que aparece, contaminas la trazabilidad con research de otro producto desde el minuto uno.

**Si es documento o tablero:** léelo completo antes de resumir.

### Paso 5 — Aprobación 1: la lista de dolores normalizada

Convierte la investigación en **afirmaciones discretas y auditables**. Esa conversión ya es interpretación tuya: si la haces en silencio, todo el veredicto se apoya en una lectura que nadie revisó. Además obliga al diseñador a mirar la investigación de verdad en vez de pegarla.

Devuelve una tabla con: identificador, el dolor en una frase, a quién le pasa, de dónde sale (fuente + cita o clip si Condens lo permite), grado de evidencia y si es **observado** o **autorreportado**. Criterios de grado en `references/juicio.md`.

Pregunta explícitamente: ¿esta lista representa lo que dice la investigación? ¿falta alguno? ¿alguno sobra o está mal leído? **Espera respuesta.**

Si la investigación resulta ser de otro segmento, de más de 18 meses, o no toca el tema del flujo, dilo aquí: *"esta investigación no responde esta pregunta; auditar contra ella sería auditar contra el vacío"*. Tienes permiso explícito de negarte a emitir juicio sobre un tramo por falta de evidencia — eso también es un resultado útil y va al informe.

### Paso 6 — Aprobación 2: el flujo reconstruido como secuencia

Reconstruye el flujo como **secuencia, no como pantallas**: pasos, decisiones, estados de error, puntos de abandono, salidas. Si no logras reconstruir la secuencia, no puedes auditar nada, solo comentar estética.

**Mientras reconstruyes, pregunta las reglas en el paso donde aparecen.** No al inicio como cuestionario, sino inline: "en este paso pides el documento de identidad, ¿eso es un requisito regulatorio, una regla de negocio, o una decisión de diseño?". Tres canastas posibles para cada paso:

- responde a un dolor de la lista,
- es un **no negociable declarado** (regulatorio, regla de negocio, restricción técnica, decisión no negociable del cliente),
- **no tiene razón conocida**.

La tercera canasta es lo más valioso del ejercicio y solo aparece si existen las otras dos. Ahí vive el scope heredado, el requerimiento interno que nadie cuestionó y el gusto personal.

Lo que el diseñador no sepa responder **no bloquea**: entra al informe como vacío declarado. La skill nunca cierra la puerta, solo dice con qué nivel de certeza puede hablar de cada tramo.

Devuelve la secuencia numerada con su canasta y pide confirmación. **Espera respuesta.**

### Paso 7 — Juicio y documento

Recorre la auditoría en **las dos direcciones**:

- **Dolor → flujo:** ¿hay cobertura? ¿en qué paso? ¿con qué efecto? Usa la escala de cinco estados de `references/juicio.md`: **elimina, reduce, traslada, decora, agrava**.
- **Flujo → dolor:** ¿este paso, esta pantalla, este campo, a qué responde? Es la dirección que casi nadie hace y la que más tiempo ahorra, porque saca a la luz lo que se puede recortar. Donde la velocidad es el activo, recortar vale tanto como cubrir.

Luego genera los entregables siguiendo la plantilla exacta de `references/documento.md`:

1. **El informe de auditoría** (archivo), con las secciones en ese orden y sin veredicto global.
2. **El brief de vacíos de investigación** (archivo aparte), que es el único entregable que puede ir directo al cliente. Cada vacío formulado como pregunta de investigación, con el método mínimo para responderla y **qué decisión del flujo está bloqueada por ella** — eso último es lo que hace que el cliente lo priorice.

Formato por defecto: Markdown. Si el diseñador dice que va a sustentar frente al cliente o adjuntarlo a una entrega formal, ofrécelo en `.docx` (y aplica la identidad de marca si la organización tiene una skill de tema disponible). Presenta siempre los archivos al final para que pueda descargarlos.

## Errores que arruinan la auditoría

- **Saltarte una aprobación** porque el usuario parece tener prisa. Las tres aprobaciones son el mecanismo que hace que el resto valga; sin ellas produces un documento fluido y sin fundamento.
- **Conciliar.** Si un dolor no está cubierto, decirlo. El diseñador te va a agradecer más el hallazgo incómodo antes de entregar que el elogio antes del fracaso.
- **Marcar todo "resuelto"** porque el flujo menciona el tema. Mencionar no es resolver: para eso existe el estado **decora**.
- **Olvidar el estado "agrava".** Los rediseños suelen resolver un dolor y crear dos. Búscalo activamente.
- **Auditar un blueprint con lentes de flujo de app.** Se ve competente sin serlo. Lee `references/blueprint.md`.
- **Prometer una conexión que no probaste.**

## Archivos de referencia

- `references/fuentes.md` — cómo verificar y usar Condens, Figma, Miro, documentos y capturas; guiones de organización de tableros y plan B.
- `references/juicio.md` — grados de evidencia, regla de tope, los cinco estados con ejemplos, y cómo clasificar pasos sin sustento.
- `references/documento.md` — plantilla exacta del informe y del brief de vacíos.
- `references/blueprint.md` — qué cambia cuando el artefacto es un blueprint o modelo de proceso.
