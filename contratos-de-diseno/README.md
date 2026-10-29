# Contratos de Diseño — tokens → ficha → compilar → validar

Skill que convierte descripciones en español de piezas de UI en **contratos YAML** validados contra los tokens del sistema de diseño del usuario, y los estructura como un **proyecto portable** que cualquier IA puede interpretar de forma idéntica.

Versión 1.0 · People Center Design · Pragma

---

## ¿Qué hace?

Traduce una pieza de interfaz (botón, campo, tarjeta, sección repetible, pantalla completa) a un contrato YAML que fija sus estados, su composición, su cableado a tokens y su accesibilidad — sin que el diseñador tenga que escribir YAML. El diseñador solo aporta: el JSON de tokens de su sistema, la intención de la pieza (ficha) y, si aplica, el código o la captura de una pieza existente. El skill compila el contrato, lo valida contra un checklist de 7 puntos y, cuando hay varios contratos, los empaqueta en un proyecto portable con instrucciones (`harness.txt`) para que cualquier IA genere la interfaz igual.

**Tres entregables:**

- **Contrato individual** — un YAML validado para una pieza (átomo, molécula, organismo o plantilla).
- **Plan de descomposición** — el árbol de piezas de una página completa, con reutilización contra la biblioteca existente, antes de compilar nada.
- **Paquete de proyecto** — carpeta portable (`LEEME.md`, `harness.txt`, `tokens/`, `contracts/`) lista para entregar a otro equipo o a otra IA.

---

## ¿Cómo funciona?

El skill sigue un flujo de **cuatro pasos**, precedido siempre por los tokens:

1. **Tokens (Paso 0)** — Pide el JSON de tokens del sistema de diseño del usuario si no lo ha subido. Es la única fuente de verdad de la sesión; sin él, cualquier token queda marcado `# por verificar`.
2. **Ficha (Paso 1)** — Entrevista conversacional (intención, tipo, datos, acciones, mensajes, decisión, medición, guardrails y composición). Si la pieza viene de código o Figma existente, extrae la ficha del artefacto real en vez de preguntar.
3. **Compilar (Paso 2)** — Escribe el YAML con las claves del esqueleto en orden, agrega estados (incluyendo siempre `error` y `deshabilitado` en piezas con input), accesibilidad y el cableado a tokens — nunca valores a mano.
4. **Validar (Paso 3)** — Corre el checklist de 7 puntos (PASA/FALLA/PENDIENTE) y entrega veredicto: **LISTO PARA GENERAR** o **CORREGIR**. Si el error es de compilación, el skill se corrige a sí mismo antes de mostrar el resultado.

Cuando el usuario describe una página completa (no una pieza suelta), el skill entra primero en **modo descomposición**: produce el árbol de piezas y lo confirma antes de compilar. Cuando pide "el proyecto" o "el paquete", entra en **modo proyecto** y empaqueta los contratos ya validados.

---

## ¿Para qué usarlo?

| Rol | Aplicación |
|---|---|
| **Diseñador de producto / UX** | Especificar una pieza de UI sin escribir YAML a mano, garantizando que use los tokens reales del sistema. |
| **Design system owner** | Mantener una biblioteca de contratos que se reutiliza (Regla de Oro) en vez de recrear piezas cada vez que aparecen en una nueva pantalla. |
| **Equipo que trabaja con varias IAs** | Producir un paquete portable (`harness.txt` + contratos) para que Claude, ChatGPT, Gemini o Copilot generen la misma interfaz sin depender del modelo. |
| **Ingeniero de frontend** | Partir de un contrato validado como fuente de verdad antes de construir el componente en código. |
| **Consultor de design systems** | Auditar o migrar componentes existentes (código, Figma) a contratos formales para estandarizar cómo se generan con IA. |

---

## ¿Cómo se usa?

### Claude Desktop / .ai

1. Sube el JSON de tokens de tu sistema de diseño al inicio de la conversación.
2. Describe la pieza que necesitas, o sube código/captura de una pieza existente, o pega un YAML para validar. Ejemplos:
   - _"Necesito el contrato de un campo de monto con validación de error"_
   - _"Aquí está el HTML de nuestra tarjeta de producto, extrae el contrato"_
   - _"Quiero la página de detalle de crédito con estas tres secciones"_
3. El skill entrevista lo que falte, compila el YAML, lo valida y entrega el contrato o el plan de piezas.
4. Si pides "el paquete" o "el proyecto", el skill entrega la carpeta portable lista para exportar.

### Claude Code (CLI)

El flujo es el mismo: no hay scripts que ejecutar, porque compilar y validar un contrato es una tarea de interpretación de lenguaje, no de cómputo. La diferencia es solo de manejo de archivos: en vez de subir el JSON de tokens al chat, puedes referenciar su ruta en el repositorio, y el skill puede escribir directamente los archivos del paquete (`LEEME.md`, `contracts/*.yaml`) en el proyecto en lugar de pegarlos en la conversación.

### Modos de ejecución

| Característica | Modo CLI | Modo ID |
|---|---|---|
| Entorno | Terminal disponible (Claude Code) | Sin terminal (Claude Desktop / .ai) |
| Tokens de entrada | JSON leído desde una ruta del repo | JSON subido como archivo en el chat |
| Compilación y validación | Igual en ambos: no requiere scripts ni dependencias | Igual en ambos: no requiere scripts ni dependencias |
| Paquete de proyecto | Se escribe como carpeta real en el repositorio | Se entrega como bloque de archivos en la conversación |
| Ideal para | Equipos que versionan sus contratos junto al código | Diseñadores que trabajan directamente en el chat |

No necesitas elegir un modo. El skill funciona igual en ambos porque no tiene modo CLI con scripts propios.

---

## ¿Cuándo usarlo?

- Al documentar un componente nuevo (átomo, molécula, organismo o plantilla) antes de construirlo.
- Al migrar piezas existentes (código, Figma, capturas) a un formato que cualquier IA pueda interpretar igual.
- Al descomponer una pantalla o flujo completo en un plan de piezas reutilizables antes de generarlas.
- Al preparar un paquete de contratos para compartir con otro equipo o con otra herramienta de IA.
- Al validar que un YAML de contrato ya escrito cumple el esqueleto y usa tokens reales, no valores inventados.

---

## Estructura

```
contratos-de-diseno/
├── SKILL.md                              # Lógica principal (tokens → ficha → compilar → validar)
├── assets/
│   └── harness.txt                       # Reglas de pintado, viaja idéntico en cada paquete de proyecto
├── references/                           # 8 referencias + 2 contratos canónicos
│   ├── tokens.md                         # Cómo leer el JSON de tokens del usuario
│   ├── ficha.md                          # Texto canónico de la entrevista
│   ├── esqueleto.md                      # Claves, orden y reglas de compilación
│   ├── mapa-semantico.md                 # Qué token corresponde a cada parte
│   ├── ejemplo.md                        # Ficha real convertida en contrato correcto
│   ├── validacion.md                     # Checklist de 7 puntos
│   ├── descomposicion.md                 # Modo página completa → plan de piezas
│   ├── proyecto.md                       # Modo paquete portable
│   ├── canonico-atomo-campo.yaml         # Ejemplo canónico de átomo
│   └── canonico-organismo-molde.yaml     # Ejemplo canónico de organismo molde
├── evals/
│   └── evals.json                        # Pruebas de calidad
├── README.md                             # Este archivo
└── LICENSE                               # Licencia de uso
```

---

## Referencias del skill

| Archivo | Contenido | Cuándo se usa |
|---|---|---|
| `tokens.md` | Formatos de JSON de tokens aceptados y cómo resumirlos | Paso 0, antes de compilar |
| `ficha.md` | Guion de entrevista para piezas nuevas | Paso 1 |
| `esqueleto.md` | Claves del contrato, orden y reglas de compilación | Paso 2 |
| `mapa-semantico.md` | Prioridad para asignar token a cada parte visual | Paso 2, al mapear tokens |
| `ejemplo.md` | Ficha real convertida en contrato, como referencia de nivel de detalle | Antes de entregar el primer contrato |
| `validacion.md` | Checklist de 7 puntos con criterio PASA/FALLA/PENDIENTE | Paso 3, siempre después de compilar |
| `descomposicion.md` | Cómo generar el árbol de piezas de una página completa | Al describir una pantalla o flujo completo |
| `proyecto.md` | Estructura del paquete portable y plantilla del `LEEME.md` | Al pedir "el proyecto" o "el paquete" |
| `canonico-atomo-campo.yaml` / `canonico-organismo-molde.yaml` | Contratos reales de producción, usados como plantilla de formato | Junto con `esqueleto.md` |
| `assets/harness.txt` | Reglas de pintado para quien consuma el paquete | Se copia tal cual en cada paquete de proyecto |

---

## Alcances

- Convierte piezas de UI (átomo, molécula, organismo, plantilla) y páginas completas en contratos YAML validados.
- Ancla cada sesión al JSON de tokens real del usuario: nunca trae ni inventa tokens propios.
- Cubre los cuatro modos de entrada: desde cero, descomposición de página, extracción desde código/Figma existente, y validación de un YAML ya escrito.
- Aplica la Regla de Oro de reutilización: las piezas compuestas referencian sus piezas hijas por `component_id`, nunca las recrean.
- Empaqueta el resultado en un proyecto portable (`LEEME.md`, `harness.txt`, `tokens/`, `contracts/`) interpretable por cualquier IA.
- No requiere instalación ni scripts: todo el flujo es de interpretación de lenguaje.

## Limitaciones

- Depende de que el usuario suba un JSON de tokens real; sin él, los contratos quedan con tokens `# por verificar` y el punto 4 de validación en PENDIENTE.
- No genera el componente final en código de producción — el contrato es la fuente de verdad, no el entregable de desarrollo.
- No rediseña el sistema de diseño: las reglas finas (por ejemplo, la Regla de campo) son del dueño del sistema y se documentan tal cual en `references/esqueleto.md`.
- La calidad de la extracción desde código o Figma depende de la fidelidad del artefacto que suba el usuario.
- El mapa semántico y los contratos canónicos reflejan las convenciones de un sistema de diseño particular; deben revisarse al adoptar el skill en un sistema distinto.

---

## Licencia

Propiedad de **Pragma**. Uso interno y confidencial — ver `LICENSE`.
