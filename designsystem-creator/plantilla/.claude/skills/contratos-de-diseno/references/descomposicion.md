# Modo descomposición: de una página a un plan de contratos

Se activa cuando el usuario describe una pantalla completa, un flujo, o varias piezas de corrido — señales: "la página de…", "la vista de…", "quiero todo el módulo de…", o una descripción que nombra 3+ bloques distintos. Regla central: **no compilar nada hasta tener el plan confirmado.**

## Fase 1 — Armar el árbol de piezas

1. **Recorrido**: extraer de la descripción cada bloque mencionado. Completar con las preguntas de plantilla de `references/ficha.md` (recorrido de arriba a abajo, modos, "¿algo más, por pequeño que sea?").
2. **Clasificar** cada bloque con el árbol de decisión de tipo (átomo/molécula/organismo/plantilla).
3. **Cruzar contra la biblioteca existente**: contratos ya en la conversación, en el proyecto, o que el usuario pueda subir. Si hay biblioteca y no está en contexto, pedirla ("¿tienes contratos previos? Súbelos para reutilizar en vez de recrear"). Cada bloque que mapea a un `component_id` existente → YA CONTRATADO, cero trabajo.
4. **Detectar moldes**: 3+ bloques con la misma estructura → proponer UN organismo con `params` en vez de contratos casi iguales. Preguntar también si algún bloque nuevo se parece a piezas de otras vistas.
5. **Ordenar de abajo hacia arriba**: átomos → moléculas → organismos → plantilla. Ninguna pieza se contrata antes que sus hijas. La plantilla siempre de última.

## Fase 2 — Presentar y confirmar el plan

Formato del plan:

```
PLAN — Plantilla: <component_id>

YA CONTRATADOS (se reutilizan):
  ✓ <lista de component_id existentes que la página usa>

NUEVOS (orden de contratación):
  1. [átomo]     <id> — <qué es, en una frase>
  2. [molécula]  <id> — ...
  3. [organismo] <id> — ...
  n. [plantilla] <id> — compone ...

DUDAS: <ambigüedades del recorrido: bloques posiblemente olvidados,
       candidatos a molde, piezas que podrían ya existir con otro nombre>
```

Confirmar con el usuario antes de contratar: "¿este árbol refleja tu página? ¿falta algún bloque?". El plan corregido es el contrato de trabajo de la sesión.

## Fase 3 — Contratar pieza por pieza, llevando el marcador

- Ir en orden. Para cada pieza: mini-entrevista SOLO de lo que la descripción original no respondió (mucha ficha ya viene contestada de la Fase 1 — no repreguntar lo dicho).
- Compilar → validar → si LISTO, marcar ✓ en el plan y mostrar el marcador actualizado en una línea ("✓ 1-2 · vamos en 3 de 5") antes de la siguiente.
- El chequeo de dependencias aplica en cadena: si una pieza nueva le pide una variante nueva a una YA CONTRATADA, actualizar primero el contrato existente (decisión del dueño; avisar).
- Si la sesión se corta, el plan es retomable: al volver, mostrar el marcador y seguir en la pieza pendiente.

## Fase 4 — Cierre

Cuando la plantilla queda LISTA con todas sus hijas ✓ → ofrecer de inmediato el Modo proyecto (paquete LEEME + harness + tokens + contracts). Si quedaron piezas en CORREGIR, la plantilla las referencia con nota y el LEEME las declara PENDIENTES.

## Anti-patrones

- Compilar la plantilla primero "para avanzar" → prohibido: quedaría llena de referencias sin contrato.
- Contratar las piezas en el orden en que el usuario las mencionó → no: orden de dependencias.
- Hacer la entrevista completa de la ficha para cada pieza → no: solo lo que falte; la descripción de la página ya es media ficha.
- Recrear una pieza porque el usuario la describió con otro nombre → antes de crear, buscar en la biblioteca por intención ("¿tu 'etiqueta de estado' es el `badge` que ya existe?").
