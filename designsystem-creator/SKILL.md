---
name: designsystem-creator
description: >
  Bootstrapea un sistema de diseño nuevo basado en contratos, clonando una
  plantilla real (enfoque create-next-app: una carpeta plantilla/ que se
  copia tal cual, sin lógica de filtrado) con docs-site en Astro, scripts de
  validación y generación de tokens, CI, y las skills contratos-de-diseno y
  criterio-diseno ya instaladas dentro del proyecto nuevo. Si hay una fuente
  disponible (Figma conectado por MCP o código/ZIP existente), siembra
  tokens reales y una FICHA parcial por cada componente que detecta — nunca
  un contrato completo ni inventado. Úsala cuando el usuario quiera crear,
  iniciar, bootstrapear o montar un sistema de diseño nuevo desde cero,
  quiera la arquitectura de contratos en un proyecto que no la tiene
  todavía, o quiera conectar un Figma nuevo para organizarlo como sistema de
  contratos. No la uses para completar un contrato ya sembrado, para
  compilar/validar uno (usa contratos-de-diseno) ni para evaluar una
  interfaz ya construida (usa criterio-diseno).
license: Proprietary — Pragma (uso interno y confidencial)
metadata:
  version: "1.0"
  author: Pragma
---

# Designsystem-creator (bootstrap de un sistema de diseño nuevo)

Esta skill no compila contratos: **monta el terreno** donde `contratos-de-diseno`
después los compila. Funciona clonando `plantilla/` (co-locada en esta misma
skill) tal cual, sin plantillas de texto ni lógica de filtrado — el mismo
enfoque que `create-next-app`: una carpeta en blanco lista para usar, más un
paso opcional de siembra si hay una fuente real de donde extraer tokens e
inventario de componentes.

**Idioma:** todo el flujo es en español, igual que el resto de las skills que
esta instala.

## Qué hay en `plantilla/`

Cópiala completa, tal cual, sin editar nada de su contenido en este paso:

- `.claude/skills/contratos-de-diseno/` y `.claude/skills/criterio-diseno/`
  — completas, con `references/` y `assets/`. El proyecto nuevo nace con
  ambas skills ya instaladas a nivel de proyecto.
- `CLAUDE.md`, `REGLAS-GLOBALES.md`, `FIGMA-PRUEBAS.md`, `CODIGO-PRUEBAS.md`
  — las guías de método. Los ejemplos con nombres concretos que traen
  (`badge`, `tarjeta-paquete`…) son ilustrativos de CÓMO se corrió el método
  la primera vez, no componentes reales de este proyecto nuevo.
- `scripts/validar_contratos.py`, `scripts/generar_tokens_css.py`.
- `.github/workflows/` (validar-contratos, typecheck).
- `.gitignore`, `package.json`, `tsconfig.json`, `vite.config.ts`,
  `.env.example`, `index.html` — el andamiaje base de Vite + React +
  TypeScript, con los alias `@atomos/@moleculas/@organismos/@templates` ya
  configurados. Sin dependencias de ningún componente concreto.
- `src/` — un playground vacío (`App.tsx` sin imports de componentes,
  `main.tsx`, `App.css` con las clases genéricas de layout).
- `docs-site/` completo — la proyección documental en Astro (sidebar con
  búsqueda, Taller interactivo, TOC flotante, tema claro/oscuro). Descubre
  los contratos con `import.meta.glob` sobre `atomos/moleculas/organismos/
  templates`: no tiene ningún componente hardcodeado, así que en el proyecto
  nuevo muestra "sin componentes todavía" hasta que se siembre el primero.
- `atomos/`, `moleculas/`, `organismos/`, `templates/` — vacías, solo con
  `.gitkeep`.
- `tokens/tokens.json.ejemplo` — estructura W3C correcta (primitivos de
  color/escala + semánticos con tema oscuro en `$value` y claro en
  `$extensions.theme-light`), con un puñado de tokens de muestra. NO son
  tokens reales de ningún sistema: existen solo para que los scripts tengan
  algo con qué correr antes de cargar los de verdad.
- `esqueleto-contrato.yaml` — el esqueleto en blanco (mismas claves y orden
  que `references/esqueleto.md` de la skill contratos-de-diseno), para
  copiar a mano si alguna vez no se usa el flujo de ficha.
- `_ejemplos/` — un contrato de ejemplo por tipo (`ejemplo-atomo`,
  `ejemplo-organismo`, `ejemplo-template`), con dominio genérico y
  encabezado "EJEMPLO — no es un componente activo". Sirven de referencia de
  formato; no se instalan en `atomos/organismos/templates`.

## Fase 0 — Detectar la fuente

Antes de scaffoldear, determina con qué se va a sembrar (pregúntalo si no es
obvio del mensaje del usuario):

1. **Figma conectado (MCP figma disponible)** → se usará en Fase 2/3 para
   extraer variables (tokens) e inventario de componentes/frames reales.
2. **Código o ZIP existente** que el usuario sube o referencia → se leerá su
   estructura y sus valores reales (CSS/tokens, árbol de componentes).
3. **Nada de lo anterior** → se scaffoldea con la base mínima de
   `tokens.json.ejemplo` y sin componentes sembrados; queda explícitamente
   marcado para que el dueño del sistema cargue tokens reales después.

Declara cuál de los tres aplica antes de seguir, para que el usuario lo
confirme o corrija.

## Fase 1 — Scaffold

Copia **toda** la carpeta `plantilla/` (co-locada en esta skill) a la raíz
del proyecto destino, preservando la estructura exacta.

- **No sobrescribas archivos existentes sin avisar.** Si el destino ya tiene
  `package.json`, `CLAUDE.md`, etc., detente y muestra la lista de choques
  antes de decidir con el usuario si se fusionan, se saltan o se
  sobrescriben uno por uno.
- Si el destino no tiene `tokens/tokens.json` real, renombra
  `tokens/tokens.json.ejemplo` → `tokens/tokens.json` (así los scripts y el
  docs-site tienen algo con qué correr desde el primer momento). Si el
  destino YA tiene un `tokens/tokens.json` propio, no lo toques y deja
  `tokens.json.ejemplo` al lado como referencia.
- Verifica al terminar: `npm install` en la raíz y en `docs-site/`, y que
  `npm run dev` (raíz) y `astro dev --background` (`docs-site/`) levanten sin
  error — con el playground vacío y el docs-site mostrando "sin componentes
  todavía".

## Fase 2 — Tokens

- Si la Fase 0 detectó Figma o código con tokens reales: extráelos **TAL
  CUAL** (nombres y valores reales) hacia `tokens/tokens.json`, con la misma
  forma W3C que ya trae `tokens.json.ejemplo` (primitivos + semánticos,
  `$value` = oscuro, `$extensions.theme-light` = claro si existe un tema
  claro real). No inventes categorías ni "mejores" valores que los de la
  fuente — si la fuente no separa primitivo/semántico, pregunta antes de
  decidirlo por tu cuenta.
- Si no hay fuente: deja `tokens.json.ejemplo` como está y dilo explícito en
  el reporte final (Fase 4) — no es apto para producción, solo para que el
  scaffold funcione.
- Corre `python3 scripts/generar_tokens_css.py` para generar
  `src/estilos/tokens.css` desde lo que haya quedado en `tokens/tokens.json`.

## Fase 3 — Siembra (nunca generación final)

Por cada componente que la fuente (Figma o código) revele:

1. **Clasifica el tipo** (átomo/molécula/organismo/plantilla) con el árbol
   de decisión de `.claude/skills/contratos-de-diseno/references/ficha.md`
   ("Árbol de decisión del tipo") — nunca a ojo. Si la fuente está
   desordenada o ambigua, sigue el procedimiento de la subsección de abajo
   ANTES de clasificar nada en firme.
2. **Presenta el mapa de clasificación propuesto** (pieza → nivel + razón +
   dudas) y espera confirmación del humano antes de crear ninguna carpeta o
   ficha — ver subsección de abajo.
3. **Crea la carpeta** del componente en `atomos/`, `moleculas/`,
   `organismos/` o `templates/` según corresponda (solo tras confirmación),
   y dentro una FICHA pre-rellenada — no un contrato — **solo** con lo que
   la fuente revela de verdad: composición (`usa:` si compone otras piezas
   ya sembradas), jerarquía visual, y las variantes que se ven distintas en
   la fuente.
4. **Marca todo lo ausente** con `# PENDIENTE: estados, acciones, datos —
   completar con flujo ficha` en vez de inventarlo. Nunca rellenes estados,
   comportamiento, acciones ni datos que la fuente no muestra explícitamente
   — eso es trabajo de la entrevista de `contratos-de-diseno`, no de esta
   siembra.
5. **Ordena de abajo hacia arriba**: siembra átomos primero, luego
   moléculas, luego organismos, luego plantillas — nunca una pieza antes que
   sus hijas, igual que exige la Regla de Oro del sistema.

Si no hay fuente (Fase 0 = "nada"), esta fase se salta entera: el proyecto
queda con `atomos/organismos/templates` vacíos, listos para que el humano
arranque con `contratos-de-diseno` desde cero.

### Clasificación desde una fuente desordenada (Figma o código sin estructura clara)

Esta skill **no clasifica en silencio**. Cuando la fuente no trae una
jerarquía clara (frames sueltos, nombres inconsistentes, código sin
componentizar), procede así antes de tocar `atomos/moleculas/organismos/
templates`:

1. **La jerarquía de anidamiento de la fuente es solo una PISTA** del orden
   relativo — no una clasificación. Lo más anidado y sin hijos es candidato
   a átomo; lo que envuelve a otras piezas sube de nivel. El **nombre** que
   le puso el diseñador al frame o a la capa **no es fuente confiable** (un
   frame llamado "Botón" puede ser en realidad una molécula con un ícono
   adentro, y viceversa).
2. **El comportamiento no es visible en Figma.** Lo que distingue molécula
   de organismo es si la pieza "hace algo por sí misma" (acciones, estados
   propios más allá de los de sus átomos) — eso Figma no lo muestra. Por
   cada pieza donde el nivel dependa de comportamiento que no puedes ver,
   **pregunta al humano en vez de asumirlo**.
3. **Propón antes de crear.** Presenta un mapa de clasificación propuesto —
   tabla o lista de `pieza → nivel propuesto + razón + dudas abiertas` — y
   espera confirmación explícita del humano ANTES de crear una sola carpeta
   o ficha. El mapa corregido por el humano es el que se ejecuta, igual que
   el árbol de piezas de una descomposición en `contratos-de-diseno`.
4. **Lo que no se pueda ubicar con confianza no se fuerza.** Las piezas
   dudosas van a una carpeta `_sin-clasificar/` en la raíz del proyecto
   (fuera de `atomos/moleculas/organismos/templates`), con una nota de por
   qué quedó ahí — nunca metidas en una carpeta solo para "dejarlo
   completo". `_sin-clasificar/` se declara en el reporte de la Fase 4 como
   pendiente de decisión humana, no como error de la skill.

Regla general: **Figma (o el código) siembra y propone; el humano confirma
la arquitectura.** Una clasificación inventada y ejecutada en silencio es
peor que una pieza pendiente y declarada.

## Fase 4 — Verificar y entregar

1. Corre `python3 scripts/validar_contratos.py` sobre lo que se sembró (si
   algo se sembró) y muestra el resultado tal cual.
2. Entrega un reporte con:
   - Qué se scaffoldeó (lista breve de lo copiado desde `plantilla/`).
   - Qué tokens se cargaron: reales desde Figma/código, o el `.ejemplo` sin
     tocar (y la advertencia de que no sirve para producción).
   - Qué componentes se sembraron, su tipo y clasificación, y qué le falta a
     cada uno (la lista de `# PENDIENTE` de su ficha).
   - Qué piezas quedaron en `_sin-clasificar/` (si alguna) y por qué —
     declaradas como pendiente de decisión humana, no como error.
   - El siguiente paso: completar cada ficha pendiente con el flujo
     ficha → compilar → validar de la skill `contratos-de-diseno`, que ya
     quedó instalada dentro del proyecto nuevo (no hay que instalarla de
     nuevo ni pedirle tokens: ya están en `tokens/tokens.json`).

## Límites (declarar si el usuario pregunta o si el resultado podría malentenderse)

- **Figma y código SIEMBRAN, no generan.** El resultado de esta skill es
  scaffold + tokens + fichas parciales — nunca contratos completos listos
  para generar. Los contratos se completan y validan con el flujo
  ficha → compilar → validar de `contratos-de-diseno`.
- **No inventa tokens ni "mejora" los de un sistema existente.** Los extrae
  tal cual de la fuente. Si el usuario quiere cambiar un token, eso se hace
  en su sistema de diseño y se vuelve a extraer — no se edita a mano en
  `tokens.json` por esta skill.
- **No decide la clasificación de tipo a la ligera, y menos desde una
  fuente desordenada.** Usa el árbol de decisión de `contratos-de-diseno`,
  y ante un Figma o código sin estructura clara presenta primero un mapa de
  clasificación propuesto y espera confirmación antes de crear carpetas o
  fichas. Lo que no se pueda ubicar con confianza va a `_sin-clasificar/`
  con nota — nunca forzado a un nivel para completar. Una clasificación
  inventada y ejecutada en silencio es peor que una pieza pendiente y
  declarada.
- **Solo el modo CLI puede ejecutar el scaffold real.** Clonar `plantilla/`,
  correr `npm install` y los scripts de Python requiere sistema de archivos
  y terminal. En modo ID (sin terminal), la skill no puede crear el proyecto
  real: como máximo describe la estructura y entrega el contenido de los
  archivos clave para que el humano los copie a mano.
- **Todo proyecto nuevo nace con `contratos-de-diseno` y `criterio-diseno`
  ya dentro** (vienen co-locadas en `plantilla/.claude/skills/`): no hace
  falta instalarlas por separado después del scaffold.
