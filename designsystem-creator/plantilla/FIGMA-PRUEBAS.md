# Guion de pruebas: contratos -> Figma (via MCP)

Requisito: haber corrido `claude plugin install figma@claude-plugins-official`,
reiniciado Claude Code, y autenticado con `/mcp` -> figma -> Authenticate.
Crea en Figma un archivo vacío "DS - pruebas" y copia su link.

Cada fase valida una cosa. NO pases a la siguiente si la anterior falló.

## Fase 1 — Tokens -> Variables (la base)
Prompt:
  "Lee tokens/tokens.json y crea en [link del archivo] las Variables del
  sistema: una colección 'primitivos' y una 'semanticos', con dos modos
  (claro y oscuro) mapeando $value (oscuro) y $extensions.theme-light
  (claro). Al terminar, lee las variables de vuelta y dame el conteo por
  colección para verificar contra el JSON."
Verificar en Figma: cambiar de modo debe alternar los colores.

## Fase 2 — Primer átomo: etiqueta (el más simple)
Prompt:
  "Lee atomos/etiqueta/etiqueta.contract.yaml y crea el componente nativo en
  [link]: component set con los ejes forma y color como variantes, todas las
  propiedades ligadas a las Variables de la Fase 1 (cero valores sueltos).
  Luego léelo de vuelta y compáralo contra el contrato: variantes completas,
  ¿algún valor no ligado a variable?"

## Fase 3 — Composición: tarjeta-producto
Prompt:
  "Crea primero boton e interruptor desde sus contratos (igual que la Fase
  2). Después crea el organismo desde
  organismos/tarjeta-producto/tarjeta-producto.contract.yaml, INSTANCIANDO
  los componentes etiqueta, boton e interruptor ya creados (Regla de Oro: no
  los recrees), con auto layout según el layout del contrato y los datos de
  muestra del LEEME del organismo."
Esta fase prueba lo importante: la Regla de Oro en Figma.

## Fase 4 — Code-to-canvas: los estados vivos
Prompt:
  "Sirve organismos/tarjeta-producto/tarjeta-producto.html en localhost y
  captura a Figma [link] el estado normal y el estado desactivada como
  frames editables."
Compara lado a lado: componente nativo (F3) vs captura del render (F4).

## Fase 5 — Auditoría de drift (el ciclo de gobernanza)
En Figma, a mano, cambia algo de la etiqueta (ej: el radio). Prompt:
  "Lee el componente etiqueta de [link] y compáralo contra
  atomos/etiqueta/etiqueta.contract.yaml. Dame el diff como ficha de cambio
  para aprobación. NO corrijas nada todavía."
Debe detectar el cambio y NO tocar el contrato. Luego: "rechazada: restaura
el componente en Figma según el contrato."

Resultado esperado al final: Figma es una proyección fiel y auditable del
repo. Si una fase falla, anota el error y ajusta el prompt o el contrato —
nunca edites Figma a mano para "cuadrarlo".
