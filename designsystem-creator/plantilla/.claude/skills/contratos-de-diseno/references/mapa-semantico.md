# Mapa semántico: qué token corresponde a cada parte

Convenciones del sistema, extraídas de los átomos contratados en producción (campo, boton, boton-icono, badge). Este mapa es la fuente para asignar tokens al compilar **átomos nuevos desde ficha** (sin código). En modo extracción desde código, el mapeo es búsqueda inversa valor→token y este mapa solo sirve de verificación.

Prioridad de fuentes al asignar un token:
1. El contrato del átomo si ya existe (Regla de Oro: moléculas/organismos/plantillas NO re-mapean tokens; heredan).
2. Búsqueda inversa contra el código real, si hay código.
3. Este mapa semántico.
4. Nada de lo anterior aplica → `# NOTA:` para el dueño del sistema. Nunca inventar.

## Campos (inputs, selects, fechas)
- fondo: `surface-inset` · borde reposo: `border-default` · borde foco: `border-focus` + anillo `focus-ring`
- texto: `text-primary` · texto de ayuda/placeholder: `text-tertiary` · error: `required`
- radio: `radius-sm` · alto: `control-h-md` (SIEMPRE, regla de campo) · tamaño de texto: `text-body`
- contenido numérico o símbolos: fuente `mono`

## Botones con texto
- forma: `radius-pill` · alto: `control-h-md` (variante suave: `control-h-sm`)
- primario: fondo = el acento (`accent` | `accent-2`); texto = `gray-0` sobre accent (azul), `text-on-accent` sobre accent-2 (lima). OJO: `text-on-accent` es oscuro, SOLO sirve sobre lima.
- secundario: fondo transparente, borde `border-default`, texto `text-primary`, hover `surface-card-hover`
- suave: fondo `{acento}-soft`, texto `{acento}-soft-text`, sin borde

## Botones de solo ícono
- 40x40, fondo transparente en reposo (NUNCA relleno), borde `border-subtle`, ícono `text-tertiary`
- neutral: forma `radius-pill`, hover `surface-card-hover` + ícono `text-primary`
- destructivo: forma `radius-sm`; el rojo (`red-400`) SOLO en hover, nunca en reposo

## Badges / insignias
- fondo `{color}-soft`, texto `{color}-soft-text`, peso `fw-semibold`, tamaño `text-2xs`
- pastilla: `radius-pill`, mayúsculas · cuadrado numerado: `radius-xs`, fuente `mono`, 24x24

## Contenedores de fila y tarjetas
- fondo: `surface-inset` · borde: `border-subtle` · radio: `radius-md` · separación: `space` (10-12px de la escala)
- superficie elevada/barra: `surface-base` + `shadow` si existe en tokens

## Tipografía por rol
- etiqueta de campo: `text-sm` (13px), `fw-semibold`, `text-secondary`
- encabezado de grupo/sección pequeña: `text-2xs`, MAYÚSCULAS, `text-tertiary`, tracking `ls-caps`
- jerarquía de texto: `text-primary` (principal) → `text-secondary` (apoyo) → `text-tertiary` (terciario/hints) → `text-disabled`
- cifras, versiones, operadores, fechas técnicas: fuente `mono`

## Palabras clave estructurales permitidas (no son tokens ni fallan validación)
`transparent`, `none`, `izquierda`, medidas de rejilla en `layout.columnas` ("1fr 96px 40px") y tamaños intrínsecos declarados en el átomo ("40x40", "24x24").

## Mantenimiento
Este mapa lo mantiene el dueño del sistema. Si el sistema del usuario es OTRO (tokens con nombres distintos), derivar el mapa de sus átomos ya contratados o de su código; si no hay ninguno, proponerle el mapeo pieza por pieza y que confirme — nunca aplicar este mapa a un sistema ajeno en silencio.
