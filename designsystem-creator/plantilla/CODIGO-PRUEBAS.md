# Guion: contratos -> componentes React

Mismo método que FIGMA-PRUEBAS.md: una fase a la vez, no avances si la
anterior no quedó verificada, y cada componente se valida contra su contrato.

Convenciones (ya decididas, no re-discutir por componente):
- CO-LOCACIÓN: el código vive junto a su contrato. Ej:
  atomos/etiqueta/etiqueta.contract.yaml + atomos/etiqueta/Etiqueta.tsx + Etiqueta.css
- TypeScript SIEMPRE: el contrato se traduce a tipos (datos obligatorios =
  props required; ejes de variantes = union types).
- Estilos: CSS plano con variables (var(--token)). NADA de Tailwind ni
  estilos inline con valores: si un color/tamaño no viene de una variable
  de tokens.css, es un error (misma regla 1 de REGLAS-GLOBALES.md).
- tokens.css es GENERADO desde tokens/tokens.json, nunca editado a mano.

## Fase R0 — Scaffold (una vez)
Prompt:
  "Monta la base de código React en este repo SIN mover los contratos:
  - Vite + React + TypeScript en la raíz (package.json, vite.config.ts,
    tsconfig.json), con src/ solo para el demo/playground.
  - Un alias de imports para que los componentes se importen desde sus
    carpetas atómicas (ej: import { Etiqueta } from '@atomos/etiqueta/Etiqueta').
  - Agrega a .gitignore lo necesario (node_modules, dist).
  - Actualiza CLAUDE.md con la sección 'Convenciones de código' de este
    guion (co-locación, TS, CSS con variables, tokens.css generado).
  Verifica: npm run dev levanta una página vacía sin errores."

## Fase R1 — Tokens -> CSS (la base, igual que en Figma)
Prompt:
  "Crea scripts/generar_tokens_css.py (o .mjs) que lea tokens/tokens.json
  y genere src/estilos/tokens.css:
  - :root con el tema oscuro ($value) y [data-theme='claro'] con
    $extensions.theme-light cuando exista.
  - Nombres: --grupo-nombre (ej: --control-h-md, --surface-inset).
  - Las referencias var(--x) del JSON se conservan como var() (herencia
    viva, igual que los alias en Figma).
  - El archivo generado lleva encabezado 'GENERADO - no editar a mano'.
  Corre el script, importa tokens.css en el demo, y verifica: pon dos
  rectángulos con surface-card y text-primary y alterna data-theme entre
  claro y oscuro. Ambos deben cambiar."

## Fase R2 — Primer átomo: Etiqueta
Prompt:
  "Lee atomos/etiqueta/etiqueta.contract.yaml y crea atomos/etiqueta/Etiqueta.tsx +
  Etiqueta.css:
  - Props tipadas EXACTAMENTE desde el contrato: texto (required), icono?,
    punto?, mayusculas?; forma: 'pastilla'|'cuadrado'; color:
    'accent'|'accent-2'|'neutral' (con los defaults del contrato).
  - Todo valor visual via var(--token) según tokens_que_usa/colores/estilos.
  - En el demo, renderiza la matriz completa: cada forma x cada color, con
    y sin punto, en ambos temas.
  Después AUDITA: compara el componente contra el contrato y dame el
  reporte (¿props = datos?, ¿variantes completas?, ¿algún valor a mano en
  el CSS?). No inventes props que el contrato no define."

## Fase R3 — Resto de átomos: Interruptor y Boton
Mismo prompt que R2 adaptado, EN ESE ORDEN. Notas:
  - Interruptor: estados foco (anillo focus-ring) y deshabilitado son
    obligatorios; rol switch + aria-checked (guardrail de accesibilidad).
  - Boton: ojo a la regla del contrato sobre texto en primario (gray-0
    sobre accent, text-on-accent SOLO sobre accent-2).

## Fase R4 — Organismo: TarjetaProducto (la fase importante)
Prompt:
  "Lee organismos/tarjeta-producto/tarjeta-producto.contract.yaml y crea
  TarjetaProducto.tsx + CSS:
  - REGLA DE ORO: importa e instancia Etiqueta, Interruptor y Boton;
    prohibido recrear nada de lo que ya existe.
  - Props desde datos: (nombre, version, activo, especificaciones?, precios?,
    caracteristicas?, desde, hasta) + callbacks de acciones (onToggle, onEdit).
  - Implementa la máquina de estados del contrato: normal ->
    confirmando-desactivacion (al apagar) -> desactivada (receta exacta:
    text-disabled, etiquetas neutral, interruptor apagado; SIN opacity global).
  - El diálogo de confirmación NO tiene contrato: márcalo // PENDIENTE y
    hazlo mínimo.
  En el demo, móntala con los datos de muestra del LEEME del organismo y
  compárala visualmente contra tarjeta-producto.html (el render de
  referencia). Audita contra el contrato al final."

## Fase R5 — Cierre
  - Corre python3 scripts/validar_contratos.py (nada debió romperse).
  - Agrega al workflow de CI: npm ci && npx tsc --noEmit (typecheck).
  - Commit por fase, no un mega-commit.

Al terminar R4 tienes las dos proyecciones completas (Figma + React) y el
prerequisito de Code Connect cumplido: hay componentes de código que mapear.

## Fase R6 — Proyección documental: docs-site (única, sin Storybook)
docs-site/ (Astro) es la ÚNICA proyección documental del sistema — no hay
Storybook. Se genera 100% en build leyendo `*.contract.yaml`,
`tokens/tokens.json`, `CLAUDE.md` y `REGLAS-GLOBALES.md`; un contrato nuevo
aparece solo, sin tocar código del sitio.
  - Página por contrato con la intención como titular, seguida de Taller
    (props/variantes en vivo, controles derivados del contrato), Anatomía,
    Especificaciones, Estados y Guías, como secciones ancladas (no tabs)
    con tabla de contenidos flotante.
  - El Taller y la galería de Estados leen `<Nombre>.muestras.ts`
    co-locado (component real + datos de muestra nombrados) — NO es
    fuente de verdad; si contradice el contrato, se corrige el
    `.muestras.ts`.
  - Layout de tres zonas (sidebar con búsqueda + contenido + TOC flotante),
    tema claro/oscuro persistente, accesible (AA).
  - `npm run dev` (con `astro dev --background`) muestra todo sin levantar
    ninguna otra app.
