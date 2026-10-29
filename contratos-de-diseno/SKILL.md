---
name: contratos-de-diseno
description: >
  Guía a diseñadores de producto para convertir piezas de UI en contratos YAML
  validados contra los tokens de SU sistema de diseño,
  y para estructurar todos los contratos como un proyecto portable que
  cualquier IA interprete y diseñe igual. Úsala siempre que el usuario
  mencione: "contrato", "contrato de componente", "ficha de pieza", "compilar
  contrato", "validar contrato", "YAML de componente", "tokens", suba un JSON
  de tokens de diseño, pida documentar un botón/campo/tarjeta/pantalla como
  contrato, quiera extraer contratos desde código o Figma existente, pida
  armar el proyecto/paquete de contratos de su sistema, describa una página o
  vista completa con varios componentes para descomponerla en contratos, o
  describa querer especificar UI para que cualquier IA la genere de forma
  consistente — aunque no use la palabra "contrato". No la uses para evaluar
  heurísticamente una interfaz ya construida (usa evaluacion-heuristica o
  accesibilidad-wcag) ni para generar el código final del componente.
license: Proprietary — Pragma (uso interno y confidencial)
metadata:
  version: "1.0"
  author: Pragma
---

# Contratos de diseño (tokens → ficha → compilar → validar)

Esta skill convierte descripciones en español de piezas de UI en **contratos YAML** validados contra los tokens del sistema de diseño del usuario, y estructura el conjunto como un **proyecto portable** que cualquier modelo de IA puede usar para generar la interfaz de forma idéntica. El humano nunca escribe YAML: sube sus tokens, llena una ficha (o sube código existente), y tú compilas y validas.

**Idioma:** todo el flujo es en español. Las claves del YAML también (son las del esqueleto).

## Paso 0 — Los tokens (SIEMPRE primero)

La skill funciona para cualquier sistema de diseño porque **no trae tokens propios**: cada sesión se ancla al JSON de tokens que sube el usuario. Antes de compilar cualquier contrato:

1. Revisa si el usuario ya subió un JSON de tokens (puede llamarse como sea: `tokens.json`, `design-tokens.json`, export de Figma/Style Dictionary…). Si hay varios JSON, pregunta cuál es el de tokens.
2. Si no lo ha subido, **pídelo antes de compilar**: "Sube el JSON de tokens de tu sistema de diseño — recomendamos llamarlo `tokens.json` o `tokens-extraidos.json`. Es lo que garantiza que el contrato use tus tokens reales y no inventados." Formatos aceptados en `references/tokens.md`.
3. Al recibirlo, léelo, extrae la lista de nombres de token válidos y **resume en 2-3 líneas** lo que encontraste (cuántos tokens, categorías: color, tipografía, espaciado, tamaños de control) para que el usuario confirme que es el archivo correcto.
4. Ese archivo es la única fuente de verdad de la sesión: compilar y validar SOLO contra él. Con tokens cargados, el punto 4 de la validación es estricto (PASA/FALLA, sin PENDIENTE).

Excepción: si el usuario insiste en avanzar sin tokens, compila marcando cada token `# por verificar` y deja el punto 4 en PENDIENTE — pero adviértele que ese contrato no garantiza consistencia entre IAs hasta validarse contra tokens reales.

Los tokens los mantiene el dueño del sistema; si el usuario quiere inventar tokens nuevos sobre la marcha, anótalo como advertencia (`# NOTA: token inexistente propuesto`) en vez de aceptarlo en silencio.

## Los cuatro modos de entrada

Detecta cuál aplica según lo que traiga el usuario:

1. **Desde cero (una pieza)** — el usuario describe una pieza concreta o pide crear un contrato. → Entrevista con la ficha (Paso 1).
2. **Descomposición (una página o flujo completo)** — el usuario describe una pantalla entera o varias piezas de corrido ("quiero la página de X con esto, esto y esto"). → NO compilar nada todavía: lee `references/descomposicion.md`, produce el árbol de piezas (plan de contratación) con reutilización contra la biblioteca existente, confírmalo con el usuario, y contrata pieza por pieza de abajo hacia arriba llevando el marcador.
3. **Desde código existente** — el usuario sube HTML, export de Figma, código React, o una captura. → Extrae la ficha del código real, **sin inventar valores**, muéstrasela para confirmar, y sigue al Paso 2. Si el código es una página completa, combina con el modo 2: árbol primero, extracción por pieza después.
4. **Validar un YAML existente** — el usuario pega o sube un contrato ya hecho. → Salta directo al Paso 3.

## Paso 1 — La ficha (entrevista)

Lee `references/ficha.md` para el texto exacto de la ficha. Haz la entrevista de forma conversacional, **no como formulario frío**: si el usuario ya dio respuestas en su mensaje, no las vuelvas a preguntar; agrupa las preguntas restantes en un solo turno (máximo dos). Deja en blanco lo que no aplique.

Reglas de la entrevista:
- Pregunta solo lo de la ficha: intención, tipo, datos, acciones, mensajes, decisión, medición, guardrails y composición.
- **Nunca preguntes cosas técnicas** al usuario (estados internos, accesibilidad detallada, tokens, cableado). Eso lo agregas tú al compilar. Si el usuario intenta responderlas, agradece y explica que eso ya está resuelto por el sistema.
- Si el usuario no sabe si su pieza es átomo/molécula/organismo/plantilla, decídelo tú por la descripción y dilo ("esto es una molécula porque combina campo + botón").

## Paso 2 — Compilar

Lee `references/esqueleto.md` (claves, orden, reglas de compilación) antes de escribir el YAML. Reglas críticas:

- Usa **exactamente** las claves del esqueleto, en ese orden. Ninguna clave extra, ninguna en inglés.
- El humano solo aportó intención, datos, mensajes, medición y composición. **Tú agregas**: la lista completa de estados, la accesibilidad y el cableado a tokens.
- Estados: enuméralos uno por uno. Si la pieza recibe input, incluye **siempre** `error` y `deshabilitado`, aunque la ficha no los mencione.
- Tokens: cada parte visual apunta a un **token por nombre**. Jamás un color, tamaño o tipografía a mano (`#FF0000`, `14px` → prohibido). Usa SOLO tokens que existan en el JSON que subió el usuario (Paso 0). Solo los átomos mapean tokens (moléculas/organismos/plantillas heredan por la Regla de Oro). Para asignar el token correcto a cada parte de un átomo, sigue la prioridad de `references/mapa-semantico.md`: contrato existente → búsqueda inversa en código real → mapa semántico → `# NOTA:` para el dueño. Nunca inventes.
- Regla de campo: si la pieza es un campo de formulario → alto 42px (`control-h-md`), texto 15px (`text-body`), alineado a la izquierda. Solo varían `tipo` y `fuente`. Esta decisión ya está tomada; no la negocies.
- Reutilización (Regla de Oro): si es molécula/organismo/plantilla, referencia las piezas hijas por su `component_id` en `usa:`. **Nunca** recrees una pieza que ya existe. Si referencias una pieza que no tiene contrato, márcala con una nota.
- Layout: si importa, va como estructura ejecutable (`display:flex; justify-content:space-between`), nunca como prosa.
- Ambigüedad: cualquier decisión que la ficha dejó abierta va con una nota `# NOTA: ...` en la línea correspondiente, en vez de inventarla en silencio.

Consulta `references/ejemplo.md` para ver una ficha real convertida en contrato correcto — imita ese nivel de detalle.

Entrega el YAML en un bloque de código, sin explicaciones largas alrededor.

## Paso 3 — Validar (siempre, automático)

Después de compilar (o si el usuario trajo un YAML), corre la validación de `references/validacion.md`: los 7 puntos, cada uno con PASA/FALLA y, si falla, qué y dónde exactamente.

- Si todo PASA → veredicto **LISTO PARA GENERAR**.
- Si algo FALLA y el error es tuyo (compilación) → **corrige el YAML tú mismo y re-valida** antes de mostrar. El usuario solo debe ver contratos que fallan por información faltante en la ficha, nunca por errores de compilación.
- Si falla por información que solo el usuario tiene → veredicto **CORREGIR**, con la lista de preguntas de la ficha que hay que completar. La corrección siempre vuelve a la ficha, nunca al YAML.
- El punto 4 (existencia de tokens) se valida contra el JSON de tokens de la sesión. Solo queda **PENDIENTE** si el usuario decidió avanzar sin tokens.

Muestra la validación como lista compacta al final del contrato.

## Modo proyecto (el entregable final)

El objetivo no son contratos sueltos sino un **paquete portable** que se le entrega a cualquier IA (Claude, ChatGPT, Gemini, Copilot…) para que todas pinten la interfaz igual. Ofrécelo cuando haya una plantilla con sus piezas listas, y hazlo siempre que pidan "el proyecto", "el paquete", "exportar" o "pasarlo a otra IA".

Lee `references/proyecto.md` para la estructura exacta y la plantilla del `LEEME.md`. En resumen:

```
<nombre-del-paquete>/
├── LEEME.md                     # orden de lectura + estado + prompt para la IA (se genera)
├── harness.txt                  # reglas para pintar: copiar TAL CUAL de assets/harness.txt
├── tokens/
│   └── tokens-extraidos.json    # el JSON que subió el usuario, con este nombre
└── contracts/
    ├── <component_id>.contract.yaml
    └── <component_id>.template.yaml   # las plantillas (punto de entrada)
```

El `harness.txt` es del dueño del sistema y viaja idéntico en todos los paquetes (vive en `assets/` de esta skill). El `LEEME.md` se genera por paquete: inventario de piezas, punto de entrada, estado (completo o con pendientes) y el prompt para la IA con 2-4 recordatorios sacados de los `# OJO / # HALLAZGO / nota:` de los contratos incluidos. Solo entran contratos LISTOS PARA GENERAR; los demás se declaran como PENDIENTES en el LEEME. Empaqueta como carpeta + zip y preséntalo.

## Entrega

Para contratos individuales, el bloque YAML en la conversación basta. Si el usuario pide archivos, produjo varios contratos, o pide el paquete → Modo proyecto.

## Qué NO hace esta skill

- No trae tokens ni los inventa: los tokens siempre vienen del JSON que sube el usuario (Paso 0). Si el usuario quiere cambiar tokens, eso se hace en su sistema de diseño y se re-sube el JSON, no contrato por contrato.
- No rediseña el sistema: el esqueleto y las reglas finas (42px, izquierda) son del dueño del sistema y viven en `references/esqueleto.md`.
- No genera el componente final (código de producción) — solo el contrato y el paquete. Si piden generar el componente, puedes hacerlo, pero deja claro que es otra fase y que el paquete validado es la fuente de verdad.
