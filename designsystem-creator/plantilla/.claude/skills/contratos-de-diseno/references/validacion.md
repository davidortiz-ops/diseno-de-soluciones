# Validación de contratos (checklist canónico)

Correr SIEMPRE después de compilar, y cuando el usuario traiga un YAML externo. Responder cada punto con PASA / FALLA / PENDIENTE. Si FALLA: decir exactamente qué y en qué línea o clave.

1. **Identidad.** ¿Tiene `component_id`, `intencion` y `tipo`? ¿El `component_id` está en minúsculas-con-guiones y el `tipo` es uno de los cuatro válidos?
2. **Estados.** ¿Están enumerados uno por uno? Si la pieza recibe input, ¿incluye `error` y `deshabilitado`? Si carga datos remotos, ¿incluye `cargando` y `vacio`?
3. **Sin valores a mano.** ¿Cada parte visual apunta a un token por nombre? Buscar patrones prohibidos: `#` seguido de hex, números con `px/rem/em` sueltos, `rgb(`, nombres de tipografía literales. Uno solo → FALLA.
4. **Tokens existentes.** ¿Todos los tokens mencionados existen en el JSON de tokens de la sesión? Alguno no existe → FALLA con el nombre exacto y la sugerencia más parecida. Solo si el usuario avanzó sin tokens → PENDIENTE, listando los tokens a verificar.
5. **Regla de Oro.** Si es molécula/organismo/plantilla: ¿reutiliza piezas por `component_id` en `usa:` en vez de recrearlas? ¿Alguna pieza referenciada no tiene contrato? → marcarla (no es FALLA, es advertencia). **Dependencias**: ¿cada variante, estado u opción que la composición le pide a una pieza EXISTE en el contrato de esa pieza? Pide algo que no existe → FALLA con hallazgo: actualizar primero el contrato de la pieza.
6. **Layout ejecutable.** Si hay layout, ¿está como estructura ejecutable (CSS-like) y no como prosa?
7. **Ambigüedades anotadas.** ¿Toda decisión que la ficha dejó abierta tiene su nota `# NOTA:`? ¿Hay algún supuesto silencioso? → FALLA.

Puntos extra (advertencias, no bloquean):
- Acción con `cuesta_dinero: si` sin `proteccion` definida.
- `medir` vacío (contrato sin métrica: legal, pero sospechoso).
- `datos` sin ningún obligatorio en una pieza que claramente valida algo.

## Veredicto final

- Todos PASA (los PENDIENTE de tokens no bloquean, pero se listan) → **LISTO PARA GENERAR**.
- Cualquier FALLA → **CORREGIR**, con la lista.

## A dónde va la corrección

- FALLA por error de compilación (estados faltantes, valor a mano, prosa en layout) → **la corrige el compilador**, nunca el humano. Corregir y re-validar antes de mostrar.
- FALLA por información faltante (no se sabe si la acción cuesta dinero, no hay intención clara) → **vuelve a la ficha**: formular la pregunta exacta de la ficha que falta responder. El humano nunca edita YAML.
