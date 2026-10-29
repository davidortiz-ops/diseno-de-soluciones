#!/usr/bin/env python3
"""Validador de contraste de color según WCAG 2.1/2.2.

Calcula el ratio de contraste entre un color de primer plano y uno de
fondo, y lo evalúa contra los umbrales AA y AAA. No requiere dependencias
externas (solo la biblioteca estándar de Python 3.8+).

Modos de uso:
    # Par de colores
    python check_contrast.py --fg "#333333" --bg "#FFFFFF"

    # Texto grande (>=18pt, o >=14pt en negrita)
    python check_contrast.py --fg "#767676" --bg "#FFFFFF" --large

    # Archivo CSS con tokens (variables --nombre: #hex;)
    python check_contrast.py --tokens tokens.css

    # Lote desde JSON: [{"name": "...", "fg": "#...", "bg": "#..."}]
    python check_contrast.py --file colores.json

    # Generar reporte HTML
    python check_contrast.py --tokens tokens.css --report reporte-contraste.html

Formatos de color aceptados: #RGB, #RRGGBB, rgb(r,g,b), hsl(h,s%,l%).
"""

import argparse
import json
import re
import sys
from typing import Dict, List, Optional, Tuple

# Asegurar salida UTF-8 (consolas de Windows usan cp1252 por defecto).
try:
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
except (AttributeError, ValueError):
    pass

# Umbrales WCAG (ratio mínimo de contraste).
UMBRALES = {
    "AA_normal": 4.5,
    "AA_grande": 3.0,
    "AAA_normal": 7.0,
    "AAA_grande": 4.5,
    "ui_componente": 3.0,  # SC 1.4.11: contraste no textual (UI/gráficos)
}

# Límite de tamaño para archivos de entrada (evita consumo excesivo).
LIMITE_BYTES = 1_048_576  # 1 MB


def parse_color(valor: str) -> Tuple[int, int, int]:
    """Convierte una cadena de color a una tupla RGB (0-255).

    Acepta hex (#RGB, #RRGGBB), rgb(r,g,b) y hsl(h,s%,l%).
    Lanza ValueError si el formato no se reconoce.
    """
    valor = valor.strip().lower()

    # Hex.
    if valor.startswith("#"):
        hex_str = valor[1:]
        if len(hex_str) == 3:
            hex_str = "".join(c * 2 for c in hex_str)
        if len(hex_str) != 6 or not re.fullmatch(r"[0-9a-f]{6}", hex_str):
            raise ValueError(f"Color hex inválido: {valor}")
        return (
            int(hex_str[0:2], 16),
            int(hex_str[2:4], 16),
            int(hex_str[4:6], 16),
        )

    # rgb(r, g, b).
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,.*)?\)", valor)
    if m:
        r, g, b = (int(m.group(i)) for i in (1, 2, 3))
        for c in (r, g, b):
            if not 0 <= c <= 255:
                raise ValueError(f"Componente RGB fuera de rango: {valor}")
        return (r, g, b)

    # hsl(h, s%, l%).
    m = re.fullmatch(
        r"hsla?\(\s*(\d+(?:\.\d+)?)\s*,\s*(\d+(?:\.\d+)?)%\s*,\s*"
        r"(\d+(?:\.\d+)?)%\s*(?:,.*)?\)",
        valor,
    )
    if m:
        h = float(m.group(1)) % 360
        s = float(m.group(2)) / 100
        light = float(m.group(3)) / 100
        return _hsl_a_rgb(h, s, light)

    raise ValueError(f"Formato de color no reconocido: {valor}")


def _hsl_a_rgb(h: float, s: float, light: float) -> Tuple[int, int, int]:
    """Convierte HSL a RGB (0-255)."""
    c = (1 - abs(2 * light - 1)) * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = light - c / 2
    if h < 60:
        rp, gp, bp = c, x, 0.0
    elif h < 120:
        rp, gp, bp = x, c, 0.0
    elif h < 180:
        rp, gp, bp = 0.0, c, x
    elif h < 240:
        rp, gp, bp = 0.0, x, c
    elif h < 300:
        rp, gp, bp = x, 0.0, c
    else:
        rp, gp, bp = c, 0.0, x
    return (
        round((rp + m) * 255),
        round((gp + m) * 255),
        round((bp + m) * 255),
    )


def luminancia_relativa(rgb: Tuple[int, int, int]) -> float:
    """Calcula la luminancia relativa según la fórmula del W3C."""
    def canal(c: int) -> float:
        cs = c / 255
        return cs / 12.92 if cs <= 0.03928 else ((cs + 0.055) / 1.055) ** 2.4

    r, g, b = (canal(x) for x in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio_contraste(fg: Tuple[int, int, int], bg: Tuple[int, int, int]) -> float:
    """Calcula el ratio de contraste entre dos colores (1:1 a 21:1)."""
    l1 = luminancia_relativa(fg)
    l2 = luminancia_relativa(bg)
    claro, oscuro = max(l1, l2), min(l1, l2)
    return (claro + 0.05) / (oscuro + 0.05)


def evaluar(ratio: float, grande: bool = False) -> Dict[str, bool]:
    """Evalúa el ratio contra los umbrales AA y AAA."""
    if grande:
        return {
            "AA": ratio >= UMBRALES["AA_grande"],
            "AAA": ratio >= UMBRALES["AAA_grande"],
        }
    return {
        "AA": ratio >= UMBRALES["AA_normal"],
        "AAA": ratio >= UMBRALES["AAA_normal"],
    }


def sugerir_color(
    fg: Tuple[int, int, int],
    bg: Tuple[int, int, int],
    objetivo: float,
) -> Optional[str]:
    """Sugiere un primer plano (oscureciendo/aclarando) que cumpla el ratio.

    Devuelve el color hex sugerido o None si no se encontró.
    """
    bg_lum = luminancia_relativa(bg)
    # Decidir dirección: si el fondo es claro, oscurecer el texto; si no, aclararlo.
    pasos = range(0, 101, 2)
    candidatos: List[Tuple[int, int, int]] = []
    for p in pasos:
        factor = p / 100
        if bg_lum > 0.5:  # fondo claro -> oscurecer
            cand = tuple(round(c * (1 - factor)) for c in fg)
        else:  # fondo oscuro -> aclarar
            cand = tuple(round(c + (255 - c) * factor) for c in fg)
        candidatos.append(cand)  # type: ignore[arg-type]

    for cand in candidatos:
        if ratio_contraste(cand, bg) >= objetivo:
            return "#{:02X}{:02X}{:02X}".format(*cand)
    return None


def _semaforo(ev: Dict[str, bool]) -> str:
    """Devuelve un emoji semáforo según el nivel cumplido."""
    if ev["AAA"]:
        return "✅"
    if ev["AA"]:
        return "⚠️"
    return "❌"


def analizar_par(
    fg_str: str, bg_str: str, grande: bool, nombre: str = ""
) -> Dict:
    """Analiza un par de colores y devuelve un dict con los resultados."""
    fg = parse_color(fg_str)
    bg = parse_color(bg_str)
    ratio = ratio_contraste(fg, bg)
    ev = evaluar(ratio, grande)
    objetivo = UMBRALES["AAA_grande"] if grande else UMBRALES["AAA_normal"]
    sugerencia = None if ev["AAA"] else sugerir_color(fg, bg, objetivo)
    return {
        "nombre": nombre,
        "fg": fg_str,
        "bg": bg_str,
        "grande": grande,
        "ratio": round(ratio, 2),
        "AA": ev["AA"],
        "AAA": ev["AAA"],
        "ui_componente": ratio >= UMBRALES["ui_componente"],
        "semaforo": _semaforo(ev),
        "sugerencia": sugerencia,
    }


def _validar_tamano(ruta: str) -> None:
    """Lanza ValueError si el archivo excede el límite de tamaño."""
    import os
    if os.path.getsize(ruta) > LIMITE_BYTES:
        raise ValueError(
            f"El archivo {ruta} supera el límite de "
            f"{LIMITE_BYTES // 1024} KB."
        )


def extraer_tokens_css(ruta: str) -> Dict[str, str]:
    """Extrae variables CSS (--nombre: valor;) de un archivo."""
    with open(ruta, "r", encoding="utf-8") as f:
        contenido = f.read()
    tokens: Dict[str, str] = {}
    for m in re.finditer(r"(--[\w-]+)\s*:\s*([^;]+);", contenido):
        tokens[m.group(1).strip()] = m.group(2).strip()
    return tokens


def imprimir_consola(resultados: List[Dict]) -> None:
    """Imprime los resultados en consola con semáforo."""
    for r in resultados:
        etiqueta = f"{r['nombre']}: " if r["nombre"] else ""
        tipo = "grande" if r["grande"] else "normal"
        print(
            f"{r['semaforo']} {etiqueta}{r['fg']} sobre {r['bg']} "
            f"({tipo}) → ratio {r['ratio']}:1 | "
            f"AA: {'sí' if r['AA'] else 'no'} | "
            f"AAA: {'sí' if r['AAA'] else 'no'}"
        )
        if r["sugerencia"]:
            print(f"    Sugerencia (AAA): usar primer plano {r['sugerencia']}")


def generar_reporte_html(resultados: List[Dict], ruta: str) -> None:
    """Genera un reporte HTML con la tabla de resultados."""
    filas = []
    for r in resultados:
        sug = r["sugerencia"] or "—"
        filas.append(
            "<tr>"
            f"<td>{r['nombre'] or '—'}</td>"
            f"<td><code>{r['fg']}</code></td>"
            f"<td><code>{r['bg']}</code></td>"
            f"<td>{'grande' if r['grande'] else 'normal'}</td>"
            f"<td>{r['ratio']}:1</td>"
            f"<td>{'✅' if r['AA'] else '❌'}</td>"
            f"<td>{'✅' if r['AAA'] else '❌'}</td>"
            f"<td>{sug}</td>"
            "</tr>"
        )
    html = (
        '<!DOCTYPE html><html lang="es-CO"><head><meta charset="UTF-8">'
        "<title>Reporte de contraste</title>"
        "<style>body{font-family:sans-serif;padding:2rem;}"
        "table{border-collapse:collapse;width:100%;}"
        "th,td{border:1px solid #ccc;padding:.4rem .6rem;text-align:left;}"
        "th{background:#f2f4f7;}code{background:#f2f4f7;padding:.1rem .3rem;}"
        "</style></head><body>"
        "<h1>Reporte de contraste WCAG 2.2</h1>"
        "<table><thead><tr><th>Nombre</th><th>Primer plano</th>"
        "<th>Fondo</th><th>Tipo</th><th>Ratio</th><th>AA</th><th>AAA</th>"
        "<th>Sugerencia AAA</th></tr></thead><tbody>"
        + "".join(filas)
        + "</tbody></table></body></html>"
    )
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Reporte HTML generado: {ruta}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validador de contraste de color WCAG 2.2."
    )
    parser.add_argument("--fg", help="Color de primer plano (texto).")
    parser.add_argument("--bg", help="Color de fondo.")
    parser.add_argument(
        "--large", action="store_true",
        help="Tratar el texto como grande (>=18pt o >=14pt negrita).",
    )
    parser.add_argument("--tokens", help="Archivo CSS con variables de color.")
    parser.add_argument("--file", help="Archivo JSON con pares de colores.")
    parser.add_argument("--report", help="Ruta de salida para reporte HTML.")
    parser.add_argument("--json", action="store_true",
                        help="Salida JSON legible por máquina (para CI).")
    args = parser.parse_args()

    resultados: List[Dict] = []

    try:
        if args.fg and args.bg:
            resultados.append(analizar_par(args.fg, args.bg, args.large))

        elif args.file:
            _validar_tamano(args.file)
            with open(args.file, "r", encoding="utf-8") as f:
                pares = json.load(f)
            for p in pares:
                resultados.append(
                    analizar_par(
                        p["fg"], p["bg"],
                        p.get("large", False), p.get("name", ""),
                    )
                )

        elif args.tokens:
            _validar_tamano(args.tokens)
            tokens = extraer_tokens_css(args.tokens)
            # Buscar convención: tokens con 'fg'/'text' y 'bg'/'background'.
            fondos = {k: v for k, v in tokens.items()
                      if "bg" in k or "background" in k or "fondo" in k}
            textos = {k: v for k, v in tokens.items()
                      if "text" in k or "fg" in k or "texto" in k or "color" in k}
            if not fondos:
                fondos = {"--bg-default": "#ffffff"}
            for tk, tv in textos.items():
                for bk, bv in fondos.items():
                    try:
                        resultados.append(
                            analizar_par(tv, bv, False, f"{tk} / {bk}")
                        )
                    except ValueError:
                        continue
            if not resultados:
                print("No se hallaron pares de color evaluables en los tokens.",
                      file=sys.stderr)
        else:
            parser.print_help()
            return 1
    except (ValueError, KeyError, FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(resultados, ensure_ascii=False, indent=2))
    else:
        imprimir_consola(resultados)
    if args.report:
        generar_reporte_html(resultados, args.report)

    # Código de salida: 1 si algún par no cumple AA (útil en CI).
    incumple = any(not r["AA"] for r in resultados)
    return 1 if incumple else 0


if __name__ == "__main__":
    sys.exit(main())
