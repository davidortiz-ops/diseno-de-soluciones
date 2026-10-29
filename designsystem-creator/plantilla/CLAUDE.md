# Design-System — reglas para Claude Code

Este repo es la FUENTE DE VERDAD del sistema de diseño. Figma y el código de
producción son proyecciones derivadas de los contratos; nunca al revés.

## Estructura (Atomic Design)
- `atomos/ moleculas/ organismos/ templates/` — cada componente en su carpeta:
  `<id>.contract.yaml` (+ código, render HTML de referencia, LEEME y
  `<Nombre>.muestras.ts` cuando existan)
- `tokens/tokens.json` — única fuente de tokens (tema oscuro por defecto,
  claro en `$extensions.theme-light`)
- `REGLAS-GLOBALES.md` — reglas obligatorias para pintar cualquier contrato
- `scripts/validar_contratos.py` — validador; correr antes de commitear
  cambios en cualquier `*.contract.yaml` / `*.template.yaml`

## Reglas de trabajo
1. Los contratos mandan. Ningún cambio en código, HTML o Figma puede
   contradecir su contrato; si el cambio es deseado: primero el contrato,
   luego regenerar las proyecciones.
2. Regla de Oro: componer por component_id (`usa:`); jamás recrear una pieza
   contratada. En código = imports; en Figma = instancias.
3. Tokens por nombre, siempre. Nada de valores a mano.
4. Orden de dependencias: átomos → moléculas → organismos → templates.
5. Mapeo contrato→código: datos→props (obligatorio=required),
   estados→estados, acciones→eventos, tokens_que_usa→variables CSS,
   usa→composición.
6. Ambigüedad → `# NOTA:` y preguntar. Hallazgo → `# HALLAZGO:` y conservar.
7. `python3 scripts/validar_contratos.py` debe dar LISTO antes de cada commit
   que toque contratos.

## Convenciones de código (React)
Guion completo de fases en `CODIGO-PRUEBAS.md`. Reglas ya decididas, no
re-discutir por componente:
- CO-LOCACIÓN: el código vive junto a su contrato. Ej:
  `atomos/etiqueta/etiqueta.contract.yaml` + `atomos/etiqueta/Etiqueta.tsx` + `Etiqueta.css`
- TypeScript SIEMPRE: el contrato se traduce a tipos (datos obligatorios =
  props required; ejes de variantes = union types).
- Estilos: CSS plano con variables (`var(--token)`). NADA de Tailwind ni
  estilos inline con valores: si un color/tamaño no viene de una variable de
  `tokens.css`, es un error (misma Regla de Oro de tokens que en Figma/contratos).
- `src/estilos/tokens.css` es GENERADO desde `tokens/tokens.json` (ver
  `scripts/generar_tokens_css.py`, Fase R1), nunca editado a mano.
- Alias de imports hacia las carpetas atómicas: `@atomos/*`, `@moleculas/*`,
  `@organismos/*`, `@templates/*` (configurados en `vite.config.ts` y
  `tsconfig.json`). `src/` es solo el demo/playground, no vive código de
  componentes ahí.

## Al escribir en Figma (MCP figma)
- Primero variables desde tokens/tokens.json: colecciones primitivos y
  semánticos, DOS modos (claro/oscuro) mapeando $value y theme-light.
- Después componentes en orden de dependencias; cada eje de `variantes:` y
  cada estado = variante del component set; TODO ligado a variables.
- Tras crear/actualizar: leer de vuelta y comparar contra el contrato;
  reportar diferencias como diff, no corregirlas en silencio.
- Drift Figma→contrato: generar "ficha de cambio" para aprobación del dueño.
  NUNCA actualizar un contrato automáticamente desde Figma.

### Separación fuente de verdad vs. proyección documental
Fuente de contexto para flujos de Figma, generación o auditoría: SOLO
`*.contract.yaml`, `*.template.yaml`, `tokens/tokens.json` y
`REGLAS-GLOBALES.md`. `docs-site/` (Astro) es la ÚNICA proyección
documental: se genera en build desde los contratos y los tokens — NUNCA
fuente de contexto para Figma o generación. Retiramos Storybook; docs-site
absorbió sus dos funciones (documentar y servir de taller interactivo por
componente).

Los `*.muestras.ts` co-locados (component real + datos de muestra
nombrados, usados por el Taller y la galería de Estados del docs-site)
tampoco son fuente de verdad: si un dato de muestra contradice su contrato,
se corrige el `*.muestras.ts`, nunca al revés.
