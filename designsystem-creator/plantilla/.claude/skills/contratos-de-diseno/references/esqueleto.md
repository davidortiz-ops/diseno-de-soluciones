# Esqueleto del contrato y reglas de compilación

Los ejemplos canónicos son `canonico-atomo-campo.yaml` (átomo con reglas fijas y variantes) y `canonico-organismo-molde.yaml` (organismo molde con params y composición parametrizada). Ante cualquier duda de formato, imitar esos dos archivos: son contratos reales del sistema en producción.

## Esqueleto base

Claves en este orden. Omitir las que no apliquen (`presentacion`, `modo`, `solo_en`, `variantes`, `comun`, `estilos`, `params`, `usa`, `layout`, `acciones`, `mensajes` pueden faltar; el resto no).

```yaml
# Contrato — {Nombre humano} ({TIPO})
# Compilado desde {ficha o fuente real}
component_id:    # minúsculas-con-guiones, estable, único
intencion:       # "una frase orientada al usuario"
tipo:            # atomo | molecula | organismo | plantilla
presentacion:    # solo plantillas, si aplica: drawer | pagina | modal
modo:            # si la pieza tiene modos: [crear, editar] | solo-lectura
solo_en:         # si solo aparece en un modo del padre: editar

variantes:       # cada eje como objeto, con significado en lenguaje humano
  - eje: tipo
    significa: "¿qué pregunta responde este eje?"
    opciones: [a, b, c]
    por_defecto: a

comun:           # (átomos) lo que comparten TODAS las variantes, vía tokens
estilos:         # (átomos) cómo se ve cada opción de la variante principal,
                 # incluyendo su hover/estados si difieren; todo vía tokens

params:          # (organismos MOLDE) lo único que cambia entre usos,
                 # cada param con su explicación en lenguaje humano

usa:             # molécula/organismo/plantilla: piezas por component_id, con:
  - atomo: campo           # nivel: atomo | molecula | organismo | texto | bloque | grupo | tabla
    rol: valor             # nombre del papel que juega aquí
    variantes: { tipo: texto, fuente: mono }   # qué variante de la pieza usa
    datos: { valor: "t.valor", textoDeAyuda: "0" }  # cableado de datos
    celda: { fila: 1, columna: 2 }              # su lugar en la rejilla, si aplica
    # NUNCA recrear una pieza que ya tiene contrato: referenciarla.

layout:          # SIEMPRE ejecutable, nunca prosa suelta:
  columnas: "1fr 96px 1fr 40px"   # rejillas: anchos exactos
  gap: space
  fondo: surface-inset            # superficies vía tokens
  borde: border-subtle
  radio: radius-md
  # contenedores complejos: strings CSS ("display:flex; align-items:center; ...")
  # y mapa de celdas comentado si hay rejilla (ver canonico-organismo-molde.yaml)

datos:           # cada dato: nombre, tipo, obligatorio
estados:         # UNO POR UNO, con comentario de origen:
  - normal                       # YA EXISTE
  - error                        # FALTA  <- el contrato obliga a que exista
  # Si recibe input: SIEMPRE error y deshabilitado. Si carga datos: cargando, vacia.

acciones:        # nombre, dispara, cuesta_dinero, proteccion
mensajes:        # texto y tono; si el texto lo define el padre, decirlo
tokens_que_usa:  # (átomos) cada parte visual -> token POR NOMBRE
guardrails:
medir:           # [] es válido: el átomo no mide, mide el organismo/plantilla
```

## Reglas de compilación

1. **División del trabajo.** El humano solo llenó: intención, datos, mensajes, medición, guardrails de negocio y composición. El compilador agrega SIEMPRE: la lista completa de estados, la accesibilidad y el cableado a tokens. No devolverle estas preguntas al humano.

2. **Estados exhaustivos y honestos.** Enumerar uno por uno. Input → `error` y `deshabilitado` obligatorios. Datos remotos o listas → `cargando`/`vacia`. Al extraer desde código existente, marcar el origen de cada estado: `# YA EXISTE` o `# FALTA` (el contrato obliga a que exista lo que falta).

3. **Regla de campo.** Todo campo: alto 42px (`control-h-md`), texto 15px (`text-body`), alineado a la IZQUIERDA. Solo varían `tipo` y `fuente`. Decisión del dueño del sistema; no se negocia por contrato.

4. **Tokens por nombre.** Cualquier `#hex`, `px` suelto, `rgb()`, tipografía literal → error de compilación. Verificar existencia contra el JSON de tokens de la sesión (ver `references/tokens.md`). Excepciones permitidas: medidas estructurales de rejilla en `layout.columnas` ("1fr 180px 40px") y tamaños intrínsecos declarados en el contrato del átomo ("40x40") — el layout es estructura, no estilo.

5. **Regla de Oro (reutilización).** Nunca redefinir dentro de un contrato una pieza que ya tiene el suyo: referenciarla en `usa:` con rol, variantes y datos. Pieza hija sin contrato → referenciarla igual con `# NOTA: sin contrato aún`. Si tres o más piezas comparten estructura, proponer un organismo MOLDE con `params` (como `seccion-repetible`) en vez de tres contratos casi iguales.

6. **Layout ejecutable.** Rejillas con anchos exactos y `celda` por pieza; contenedores como strings CSS. Prosa solo como comentario aclaratorio junto a la estructura, nunca en su lugar.

7. **Ambigüedad y hallazgos explícitos.** Decisión abierta → `# NOTA:`. Al compilar desde código real, registrar los hallazgos como comentarios (`# HALLAZGO`, `# OJO`, `# IMPORTANTE`): variantes que faltan en otro contrato, errores que las IAs cometieron en renders anteriores, opciones hardcodeadas que deberían ser datos. Esos comentarios alimentan los recordatorios del LEEME.md del paquete.

8. **Acciones con dinero o irreversibles.** `cuesta_dinero: true` o acción destructiva → `proteccion` obligatoria (ej: `confirmacion-explicita`). Sin definir → nota de ambigüedad.

## Salida

Devolver SOLO el bloque YAML (más la validación del Paso 3 debajo). Sin párrafos explicativos entre medio.
