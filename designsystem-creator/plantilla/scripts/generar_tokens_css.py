#!/usr/bin/env python3
"""Genera src/estilos/tokens.css desde tokens/tokens.json — correr desde la
raíz del repo: python3 scripts/generar_tokens_css.py

Mismo recorrido que aplanar_tokens() de validar_contratos.py: cada hoja con
"$value" se convierte en --<ruta-unida-con-guiones>, sin el nivel superior
(primitivos_color / primitivos_escala / semanticos). Esto garantiza que el
nombre de variable CSS sea IDÉNTICO al nombre de token usado en los
contratos (ej: primitivos_color.gray.0 -> --gray-0, semanticos.surface-app
-> --surface-app).
"""
import json

ENTRADA = "tokens/tokens.json"
SALIDA = "src/estilos/tokens.css"


def recorrer(d, ruta, out):
    if not isinstance(d, dict):
        return
    if "$value" in d:
        out.append({
            "nombre": "-".join(ruta),
            "valor": d["$value"],
            "claro": d.get("$extensions", {}).get("theme-light"),
        })
        return
    for k, v in d.items():
        if not k.startswith(("_", "$")):
            recorrer(v, ruta + [k], out)


def main():
    tokens = json.load(open(ENTRADA))

    semanticos = []
    recorrer(tokens.get("semanticos", {}), [], semanticos)
    nombres_semanticos = {t["nombre"] for t in semanticos}

    primitivos_color = []
    recorrer(tokens.get("primitivos_color", {}), [], primitivos_color)
    primitivos_escala = []
    recorrer(tokens.get("primitivos_escala", {}), [], primitivos_escala)

    # Algunas entradas de primitivos_escala.text (primary/secondary/tertiary/
    # disabled/on-accent/link) duplican, sin variante clara, un color que
    # también existe en semanticos con el mismo valor oscuro. El semántico
    # manda (trae la variante clara); el primitivo se omite para no declarar
    # la misma variable CSS dos veces con valores distintos.
    omitidos = [t for t in primitivos_color + primitivos_escala if t["nombre"] in nombres_semanticos]
    primitivos_color = [t for t in primitivos_color if t["nombre"] not in nombres_semanticos]
    primitivos_escala = [t for t in primitivos_escala if t["nombre"] not in nombres_semanticos]

    lineas = []
    lineas.append("/* GENERADO - no editar a mano.")
    lineas.append(f"   Fuente: {ENTRADA}")
    lineas.append("   Regenerar con: python3 scripts/generar_tokens_css.py */")
    lineas.append("")
    lineas.append(":root {")
    lineas.append("  /* primitivos_color */")
    for t in primitivos_color:
        lineas.append(f"  --{t['nombre']}: {t['valor']};")
    lineas.append("")
    lineas.append("  /* primitivos_escala */")
    for t in primitivos_escala:
        lineas.append(f"  --{t['nombre']}: {t['valor']};")
    if omitidos:
        lineas.append("")
        nombres = ", ".join(f"--{t['nombre']}" for t in omitidos)
        lineas.append(f"  /* {nombres}: definidos abajo en semanticos (mismo valor oscuro, con variante clara) */")
    lineas.append("")
    lineas.append("  /* semanticos (tema oscuro = valor por defecto) */")
    for t in semanticos:
        lineas.append(f"  --{t['nombre']}: {t['valor']};")
    lineas.append("}")

    con_variante_clara = [t for t in semanticos + primitivos_color + primitivos_escala if t["claro"]]
    if con_variante_clara:
        lineas.append("")
        lineas.append("[data-theme='claro'] {")
        for t in con_variante_clara:
            lineas.append(f"  --{t['nombre']}: {t['claro']};")
        lineas.append("}")

    contenido = "\n".join(lineas) + "\n"
    with open(SALIDA, "w") as f:
        f.write(contenido)

    total = len(primitivos_color) + len(primitivos_escala) + len(semanticos)
    print(f"{SALIDA}: {total} variables ({len(con_variante_clara)} con variante clara), {len(omitidos)} omitidas por duplicado")


if __name__ == "__main__":
    main()
