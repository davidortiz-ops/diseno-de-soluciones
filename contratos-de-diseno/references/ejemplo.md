# Ejemplo completo: tokens → ficha → contrato → validación

Lee este archivo antes de entregar tu primer contrato en una sesión, o cuando dudes del nivel de detalle esperado. Referencia de calidad. Imitar este nivel de detalle, ni más escueto ni inflado.

## Paso 0: el diseñador subió su tokens.json

```json
{ "control-h-md": "42px", "text-body": "15px", "text-caption": "12px",
  "text-align-left": "left", "feedback-danger": "#C0392B",
  "surface-primary": "#FFFFFF", "action-primary": "#0A5FFF" }
```

Resumen que se le da: "Leí 7 tokens: tamaños de control, tipografía, alineación y colores de feedback/superficie/acción. Ejemplos: `control-h-md`, `feedback-danger`. ¿Es el archivo correcto?" → confirma.

## Ficha que llenó el diseñador

```
1. Nombre: Campo de monto a transferir
2. ¿Qué es?: átomo... ¿o molécula? (tiene etiqueta y mensaje de error)
3. ¿Qué logra?: que el usuario escriba cuánto quiere transferir sin equivocarse
4. Datos:
   - monto (obligatorio: sí)
   - moneda (obligatorio: sí)
   - saldo disponible (obligatorio: no, solo se muestra)
5. Acciones: ninguna directa; valida al perder el foco
6. Mensajes:
   - "No tienes saldo suficiente" — tono cercano, sin culpar
   - "Ingresa un monto para continuar" — tono neutro
7. ¿Qué decide?: rechaza montos mayores al saldo o iguales a cero
8. Medir: cuántas veces aparece el error de saldo insuficiente
9. Guardrails: rechazo con dignidad (el error nunca suena a regaño)
10. Composición: (no la llenó)
```

Nota del compilador al leerla: tiene etiqueta + campo + mensaje de error → es **molécula**, y reutiliza el átomo `campo-texto`. Se le confirma al usuario en una frase y se compila.

## Contrato compilado

```yaml
component_id: campo-monto-transferencia
intencion: Permitir al usuario ingresar el monto a transferir con validación inmediata contra su saldo
tipo: molecula
usa:
  - campo-texto            # átomo base; regla de campo aplica a través de él
  - etiqueta-de-campo      # NOTA: sin contrato aún
datos:
  - nombre: monto
    obligatorio: si
  - nombre: moneda
    obligatorio: si
  - nombre: saldo_disponible
    obligatorio: no        # solo lectura, se muestra como ayuda
estados:
  - reposo
  - foco
  - lleno
  - error                  # agregado por el compilador: la pieza recibe input
  - deshabilitado          # agregado por el compilador: la pieza recibe input
acciones:
  - accion: validar-al-perder-foco
    cuesta_dinero: no
    proteccion: ninguna
mensajes:
  - texto: "No tienes saldo suficiente"
    tono: cercano
    cuando: monto > saldo_disponible
  - texto: "Ingresa un monto para continuar"
    tono: neutro
    cuando: monto vacío al validar
tokens_que_usa:            # regla de campo vía tokens; todos existen en tokens.json
  alto: control-h-md
  texto: text-body
  alineacion: text-align-left
  color-error: feedback-danger
  ayuda-saldo: text-caption
guardrails:
  - rechazo-con-dignidad   # los mensajes de error no culpan al usuario
  - accesibilidad-aa       # agregado por el compilador
medir:
  - frecuencia-error-saldo-insuficiente
# NOTA: la ficha no definió el formato del monto (decimales, separador de miles);
# se asumió formato de la moneda activa. Confirmar con el dueño del sistema.
```

## Validación

1. Identidad → PASA
2. Estados → PASA (error y deshabilitado presentes; no carga datos remotos)
3. Sin valores a mano → PASA (regla de campo expresada vía tokens, no `42px` literal)
4. Tokens existentes → PASA (control-h-md, text-body, text-align-left, feedback-danger, text-caption: todos en tokens.json)
5. Regla de Oro → PASA, con advertencia: `etiqueta-de-campo` sin contrato aún
6. Layout ejecutable → PASA (no aplica layout complejo)
7. Ambigüedades anotadas → PASA (formato del monto anotado)

**Veredicto: LISTO PARA GENERAR**

## Anti-ejemplos (lo que el compilador NUNCA hace)

```yaml
# MAL: valor a mano
alto: 42px

# MAL: prosa como layout
layout: "la etiqueta va arriba y el saldo abajo a la derecha"

# MAL: recrear una pieza existente en vez de referenciarla
campo_interno:
  bordes: redondeados
  color: "#E5E5E5"

# MAL: supuesto silencioso (asumir decimales sin dejar NOTA)
```
