# Entregables

Dos archivos. El informe es para el diseñador y su equipo. El brief es el único que puede ir directo al cliente.

Markdown por defecto. Si el diseñador va a sustentar frente al cliente o adjuntarlo a una entrega formal, ofrece `.docx` y aplica la identidad de marca si la organización tiene una skill de tema disponible. Presenta siempre los archivos al final.

---

# DOCUMENTO 1 — Informe de auditoría

Usa exactamente estas secciones, en este orden.

```markdown
# Auditoría de flujo contra investigación — [Nombre del flujo]

**Artefacto auditado:** [flujo de producto / blueprint] — [fuente y ubicación]
**Investigación utilizada:** [fuentes, con links, aprobadas por el usuario el DD/MM/AAAA]
**Auditado por:** [nombre del diseñador] · **Fecha:** DD/MM/AAAA

> Este documento audita la trazabilidad entre la investigación disponible y las
> decisiones de este flujo. No reemplaza una prueba con usuarios y no emite un
> veredicto de aprobación.

## 1. Los dolores del cliente

| # | Dolor | A quién le pasa | Fuente | Grado | Observado / Autorreportado |
|---|-------|-----------------|--------|-------|----------------------------|

[Debajo de la tabla, nota sobre la calidad general de la evidencia: vigencia,
segmento, método. Si algún dolor fue degradado de grado, decir por qué.]

## 2. Qué resuelve el flujo y por qué

Por cada dolor cubierto:

**D[#] — [dolor] · Estado: [elimina / reduce]**
- Dónde: paso [n] — [qué hace el flujo]
- Por qué responde: [mecanismo concreto, no intención]
- Condición de falla: [cuándo deja de ser cierto]
- Señal que lo probaría: [qué observar o medir]
- Lo más fuerte que se puede afirmar: [según regla de tope]

## 3. Qué NO resuelve y por qué

Por cada dolor no cubierto, o cubierto de forma insuficiente:

**D[#] — [dolor] · Estado: [traslada / decora / agrava / sin cobertura]**
- Qué hace hoy el flujo con este dolor: [o "nada"]
- Por qué no lo resuelve: [si traslada, decir a quién o a qué momento;
  si decora, decir qué cambia en el discurso y qué no cambia en el comportamiento;
  si agrava, decir qué fricción nueva aparece]
- Consecuencia si se entrega así: [concreta]

## 4. Partes del flujo sin sustento en la investigación

Pasos que no responden a ningún dolor ni a ningún no negociable declarado.

| Paso | Qué hace | Qué se preguntó | Estado |
|------|----------|-----------------|--------|

Formula cada uno como pregunta abierta, no como acusación. Cierra la sección
señalando cuáles son candidatos a recorte si no aparece una razón.

[Añade aquí, en una lista aparte, los no negociables declarados durante la
reconstrucción, para que quede registro de por qué esos pasos no se cuestionan.]

## 5. Huecos en la investigación

Qué preguntas necesarias para decidir este flujo la investigación actual no responde.
Cada hueco enlaza con la decisión de diseño que deja en el aire.

## 6. Qué debe validarse con usuario y por qué

Priorizado por costo de equivocarse, no por facilidad de prueba.

| # | Qué probar | Por qué no basta la investigación | Qué decisión desbloquea | Costo de equivocarse |
|---|------------|-----------------------------------|-------------------------|----------------------|

## 7. Qué ya se sustenta solo con la investigación

Decisiones que pueden avanzar sin prueba adicional, con el dolor que las respalda
y su grado de evidencia. Esta sección es la que da velocidad: dice explícitamente
dónde NO hay que gastar tiempo probando.

## Qué no se puede afirmar al entregar esto

Lista de frases que el diseñador no debe decir en la sustentación porque la
evidencia no las sostiene, cada una con su alternativa defendible.

**En lugar de:** "el flujo resuelve el problema de abandono"
**Decir:** "el flujo reduce tres de los cinco puntos de abandono documentados;
el cuarto queda sin evidencia y el quinto se traslada al canal telefónico"

[Cierra siempre con el riesgo número uno no cubierto, aunque el flujo se vea bien.]
```

## Reglas de redacción del informe

- **Ningún veredicto global.** Ni "aprobado", ni "cumple", ni porcentaje de cobertura. Si el lector quiere un número, el número miente.
- **Nunca la palabra "validado"** para algo sustentado solo en investigación documental.
- Cada afirmación sobre un dolor lleva su identificador `D[#]` para que la trazabilidad sea verificable.
- Mecanismos, no intenciones. "Precarga el dato desde el core" en lugar de "busca facilitar el proceso".
- Los vacíos se escriben como vacíos, no se rellenan con supuestos razonables.

---

# DOCUMENTO 2 — Brief de vacíos de investigación

Se genera **siempre**, incluso si la investigación es buena. Es corto, va dirigido a quien puede financiar o autorizar la investigación —normalmente el cliente— y por eso es el más conservador en sus afirmaciones.

```markdown
# Qué nos falta saber para decidir [nombre del flujo]

**Contexto:** revisamos [fuente de investigación] frente al flujo de [X].
La mayoría de las decisiones quedó sustentada. Estas son las preguntas
abiertas que hoy bloquean decisiones concretas de diseño.

## Vacío 1 — [pregunta de investigación, formulada como pregunta]

- **Por qué importa:** [qué decisión del flujo está bloqueada]
- **Qué pasa si decidimos sin esto:** [riesgo concreto, en términos de negocio]
- **Método mínimo para responderla:** [lo más barato que la responde:
  n de participantes, formato, duración estimada]
- **Qué desbloquea:** [la decisión que se puede tomar después]

[Repetir por vacío. Ordenados por lo que bloquea la decisión más cara de revertir.]

## Lo que sí quedó cubierto

[Dos o tres líneas. Esta sección existe para que el cliente vea que su
investigación sí se usó y que la petición es acotada, no un cuestionamiento
a su trabajo.]
```

## Reglas del brief

- **Una pregunta por vacío**, respondible. "¿Los usuarios entienden el estado de su solicitud sin llamar?" es una pregunta. "Entender mejor al usuario" no lo es.
- **El método mínimo, no el ideal.** Cinco entrevistas que se pueden hacer esta semana desbloquean más que un estudio de tres meses que nadie va a aprobar.
- **Siempre nombrar la decisión bloqueada.** Es lo que hace que el cliente priorice: sin eso el brief se lee como una queja del proveedor.
- **Tono:** no cuestiona el trabajo de nadie. La investigación existente se hizo para responder otras preguntas; estas son nuevas.
