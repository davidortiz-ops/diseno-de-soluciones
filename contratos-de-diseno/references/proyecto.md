# Modo proyecto: el paquete portable

Lee este archivo cuando el usuario pida "el proyecto", "el paquete", "exportar" o pasar los contratos a otra IA. El entregable final. Una carpeta autocontenida que se le pasa a **cualquier IA** para que pinte la interfaz igual, sin importar el modelo. El formato es el estándar del equipo (probado en producción):

## Estructura

```
<nombre-del-paquete>/            # ej: paquete-crear-paquete/
├── LEEME.md                     # orden de lectura + estado + prompt para la IA
├── harness.txt                  # reglas para pintar (copiar de assets/harness.txt, NO reescribir)
├── tokens/
│   └── tokens-extraidos.json    # el JSON que subió el usuario, con este nombre
└── contracts/
    ├── <component_id>.contract.yaml    # átomos, moléculas y organismos
    └── <component_id>.template.yaml    # las plantillas (punto de entrada del render)
```

Reglas:
- Un archivo por contrato: `<component_id>.contract.yaml`; las plantillas van como `.template.yaml`.
- `harness.txt` se copia tal cual desde `assets/harness.txt` de esta skill. Es del dueño del sistema: no se edita por proyecto. Si el usuario quiere cambiar una regla del harness, eso se cambia en la skill, no en un paquete.
- `tokens/tokens-extraidos.json` es el JSON del usuario con el nombre estándar.
- Solo entran contratos con veredicto LISTO PARA GENERAR; los pendientes se declaran en LEEME.md.
- Entregar la carpeta comprimida en `.zip` y presentarla.

## Plantilla de LEEME.md

Generarlo llenando los huecos:

```markdown
# Paquete para pintar la vista "{nombre de la plantilla}" ({COMPLETO | CON PENDIENTES})

## Orden de lectura
1. harness.txt
2. tokens/tokens-extraidos.json
3. contracts/{punto-de-entrada}.template.yaml  (punto de entrada)
4. el resto de contracts/

## Estado: {TODAS las piezas están contratadas | faltan contratos}
Átomos: {lista}.
Moléculas: {lista}.
Organismos: {lista}.
Plantilla: {nombre}.
=> {Este render NO debería tener ninguna pieza PENDIENTE. | Piezas PENDIENTES: {lista} — marcarlas, no inventarlas.}

## Prompt para la IA
---------------------------------------------------------------
Usa el paquete adjunto. Léelo en orden: harness.txt, tokens/, contracts/.

Pinta la INTERFAZ FINAL de contracts/{punto-de-entrada}.template.yaml, tal como
la vería un usuario real en producción. Es una pantalla funcional, NO un diagrama:
sin etiquetas de tokens, sin anotaciones, sin líneas de composición.

Obedece harness.txt en todo. Aplica los tokens a toda superficie. Respeta las
celdas de cada rejilla.
{2-4 recordatorios específicos de este paquete: las reglas que las IAs suelen
romper en ESTAS piezas — ej: "cada sección usa su propia fila", "el bote de
eliminar va gris, rojo solo en hover". Sacarlos de las notas y hallazgos de
los contratos incluidos.}

Al final, aparte del diseño, dame un manifiesto que liste por nombre: los
archivos que leíste, los contratos usados, los tokens aplicados{, y las piezas
pendientes}.
---------------------------------------------------------------
```

Los "recordatorios específicos" son la parte con criterio: revisar los comentarios `# OJO`, `# IMPORTANTE`, `# HALLAZGO` y `nota:` de los contratos del paquete, y subir al prompt los 2-4 que corrigen errores ya vistos en renders.

## Cuándo ofrecerlo

- Automático: cuando la sesión acumula una plantilla + sus piezas LISTAS, ofrecer armar el paquete.
- Obligatorio: cuando el usuario dice "proyecto", "paquete", "exportar", "pasárselo a otra IA", "que todas las IAs lo pinten igual".
- Actualización: si el usuario trae un paquete existente y contratos nuevos o corregidos, reemplazar/agregar solo esos archivos y regenerar LEEME.md (inventario + estado + recordatorios) — no tocar harness ni tokens.
