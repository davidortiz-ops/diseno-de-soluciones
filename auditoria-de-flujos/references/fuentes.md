# Fuentes: verificación, lectura y plan B

## Principio

La skill corre con la sesión de cada diseñador. **No heredas los conectores de nadie.** Cada ejecución verifica en vivo.

La verificación tiene dos capas y la segunda es la que importa:

1. **Existe** — el MCP aparece en las herramientas disponibles de esta sesión. Si el entorno carga herramientas de forma diferida, búscalo por nombre antes de concluir que no está.
2. **Responde** — una llamada real de prueba devuelve datos.

Un conector visible pero sin permiso sobre el archivo, con la sesión expirada o apuntando a otro workspace se ve idéntico a uno sano en la lista y falla en el paso siguiente, cuando ya prometiste que ibas a leerlo. Prueba antes de prometer.

Cuando algo falla, dilo en una línea y ofrece el plan B. Sin disculpas largas:

> "No logro leer el archivo de Figma desde aquí (el conector responde pero no tengo acceso a ese archivo). Pásame capturas y te digo exactamente cómo organizarlas para que la lectura sea confiable."

---

## Condens — investigación propia

Es la mejor fuente disponible porque da trazabilidad hasta el clip y la cita, lo que sube el grado de evidencia de los dolores.

**Prueba de conexión:** lista los workspaces accesibles. Si devuelve vacío o error, plan B.

**Flujo obligatorio:**

1. Busca por el tema, producto y segmento del flujo que se va a auditar.
2. Presenta lo encontrado como lista numerada: **título — resumen de dos líneas — link**.
3. Pregunta cuáles entran a la auditoría.
4. **Sin selección explícita no continúas.** Si usas todo lo que devuelve la búsqueda, metes research de otro producto o de otro momento y contaminas la trazabilidad desde el inicio.

Si la búsqueda no devuelve nada relevante, dilo y pregunta con qué otros términos buscar antes de asumir que no hay investigación.

Al normalizar dolores desde Condens, conserva el link del artefacto y, si está disponible, la referencia al clip o cita. Eso es lo que permite grado **alto** de evidencia.

---

## Figma — flujos

**Prueba de conexión:** pide metadata del nodo o archivo. Si el conector exige que el archivo esté abierto en el Figma de escritorio del usuario, dilo explícitamente antes de intentarlo.

**Qué necesitas de Figma:** la secuencia, no la estética. Frames en orden, flechas o conexiones del prototipo, estados de error, pantallas vacías, y cualquier bifurcación.

**Qué pedirle al diseñador si el archivo es grande:** el nombre de la página y de la sección o flow específico. Auditar un archivo completo sin guía produce lecturas mezcladas de exploraciones viejas.

Si solo tienes capturas de Figma, sirve igual — lo que no puedes hacer es inferir transiciones que no estén dibujadas. Pregúntalas.

---

## Miro — investigación, flujos, o ambos en el mismo tablero

Es la fuente más frágil: stickies sueltos, sin jerarquía, con contexto que vive en la posición espacial. Un tablero desordenado leído por MCP produce una lectura plausible y equivocada, que es el peor resultado posible.

**Prueba de conexión:** lista los boards accesibles o lee la metadata del board indicado.

**Antes de leer, siempre da la recomendación de organización:**

> "Para que la lectura sea confiable, organiza el tablero en dos zonas con frames nombrados:
> — un frame llamado **INVESTIGACIÓN** con los hallazgos, dolores u oportunidades, un sticky por hallazgo;
> — un frame llamado **FLUJO** con los pasos en orden de izquierda a derecha, incluyendo errores y salidas.
> Si ya está organizado de otra forma, solo dime los nombres de los frames y qué hay en cada uno. Nunca voy a adivinar qué zona es cuál: si no me lo dices, te lo pregunto."

**Nunca infieras** qué zona es investigación y cuál es flujo. Si el usuario no lo indica, pregunta.

---

## Documento de resultados (PDF, Word, presentación)

Típicamente lo entrega el cliente. Léelo completo antes de resumir, y presta atención a la ficha metodológica: fecha, método, tamaño de muestra, segmento, quién lo hizo.

Si el documento no declara metodología, **eso es un vacío y va al brief**. Un documento sin ficha metodológica no puede sostener grado alto de evidencia por bien escrito que esté.

---

## Capturas (plan B universal)

Siempre funciona y no es un mal resultado. Lo que cambia es que tú no puedes inferir lo que no esté visible.

**Qué pedir:**

- Del flujo: capturas en orden, numeradas, incluyendo estados de error y pantallas vacías. Si hay bifurcaciones, que las señale.
- De la investigación: capturas legibles o el texto pegado. Los stickies fotografiados en diagonal no sirven.

**Qué advertir:** con capturas no ves transiciones, condiciones ni lógica. Todo eso lo vas a preguntar en el paso de reconstrucción, y lo que quede sin responder va al informe como vacío declarado.
