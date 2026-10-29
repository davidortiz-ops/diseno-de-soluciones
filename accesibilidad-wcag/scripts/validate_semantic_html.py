#!/usr/bin/env python3
"""Validador de estructura semántica HTML para accesibilidad WCAG 2.2.

Revisa marcado HTML en busca de problemas frecuentes de accesibilidad
usando solo la biblioteca estándar (html.parser). No ejecuta JavaScript
ni evalúa significado, por lo que complementa —no reemplaza— la revisión
manual y herramientas como axe-core.

Modos de uso:
    python validate_semantic_html.py --file index.html
    python validate_semantic_html.py --url https://ejemplo.com
    python validate_semantic_html.py --urls urls.txt
    python validate_semantic_html.py --url https://ejemplo.com --report salida.html

Validaciones: idioma, título, encabezados (h1 único y jerarquía), imágenes
con alt, tablas (th/scope, caption), formularios (label asociado), enlaces,
landmarks, iframes con title y skip link.
"""

import argparse
import sys
from html.parser import HTMLParser
from typing import Dict, List, Optional, Tuple

# Asegurar salida UTF-8 (consolas de Windows usan cp1252 por defecto).
try:
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
except (AttributeError, ValueError):
    pass

NIVEL = {"OK": "✅", "WARN": "⚠️", "FAIL": "❌"}


class Hallazgo:
    """Representa un resultado de validación."""

    def __init__(self, nivel: str, regla: str, mensaje: str,
                 linea: Optional[int] = None, sugerencia: str = "") -> None:
        self.nivel = nivel          # OK / WARN / FAIL
        self.regla = regla
        self.mensaje = mensaje
        self.linea = linea
        self.sugerencia = sugerencia


class AnalizadorHTML(HTMLParser):
    """Recolecta información estructural del documento HTML."""

    LANDMARKS = {"main", "header", "footer", "nav", "aside"}
    ROLES_REDUNDANTES = {
        "nav": "navigation", "main": "main", "header": "banner",
        "footer": "contentinfo", "aside": "complementary",
    }

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.html_lang: Optional[str] = None
        self.tiene_title = False
        self.title_texto = ""
        self._en_title = False
        self.encabezados: List[Tuple[int, int]] = []  # (nivel, línea)
        self.imagenes: List[Dict] = []
        self.tablas: List[Dict] = []
        self._pila_tabla: List[Dict] = []
        self.inputs: List[Dict] = []
        self.labels_for: List[str] = []
        self.enlaces: List[Dict] = []
        self._en_enlace = False
        self._enlace_actual: Dict = {}
        self.landmarks_encontrados = set()
        self.iframes: List[Dict] = []
        self.roles_redundantes: List[Tuple[str, int]] = []
        self.skip_link = False
        self._primer_enlace_revisado = False

    def handle_starttag(self, tag: str, attrs_list) -> None:
        attrs = dict(attrs_list)
        linea = self.getpos()[0]

        if tag == "html":
            self.html_lang = attrs.get("lang")
        elif tag == "title":
            self._en_title = True
            self.tiene_title = True
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.encabezados.append((int(tag[1]), linea))
        elif tag == "img":
            self.imagenes.append({
                "linea": linea,
                "alt": attrs.get("alt"),
                "tiene_alt": "alt" in attrs,
                "rol": attrs.get("role"),
                "aria_hidden": attrs.get("aria-hidden"),
            })
            # Una imagen con alt dentro de un enlace aporta su nombre accesible.
            if self._en_enlace and (attrs.get("alt") or "").strip():
                self._enlace_actual["texto"] += " " + attrs["alt"]
        elif tag == "table":
            self._pila_tabla.append({"linea": linea, "th": 0, "scope": 0,
                                     "caption": False})
        elif tag == "caption" and self._pila_tabla:
            self._pila_tabla[-1]["caption"] = True
        elif tag == "th" and self._pila_tabla:
            self._pila_tabla[-1]["th"] += 1
            if "scope" in attrs:
                self._pila_tabla[-1]["scope"] += 1
        elif tag in ("input", "select", "textarea"):
            tipo = attrs.get("type", "text")
            if tipo not in ("hidden", "submit", "button", "reset", "image"):
                self.inputs.append({
                    "linea": linea, "tag": tag, "id": attrs.get("id"),
                    "aria_label": attrs.get("aria-label"),
                    "aria_labelledby": attrs.get("aria-labelledby"),
                    "title": attrs.get("title"),
                })
        elif tag == "label" and "for" in attrs:
            self.labels_for.append(attrs["for"])
        elif tag == "a":
            self._en_enlace = True
            href = attrs.get("href", "")
            self._enlace_actual = {
                "linea": linea, "href": href,
                "aria_label": attrs.get("aria-label"), "texto": "",
            }
            if not self._primer_enlace_revisado:
                self._primer_enlace_revisado = True
                if href.startswith("#") and href not in ("#", ""):
                    self.skip_link = True
        elif tag == "iframe":
            self.iframes.append({"linea": linea, "title": attrs.get("title")})

        # Landmarks por etiqueta o por rol.
        if tag in self.LANDMARKS:
            self.landmarks_encontrados.add(tag)
            rol = attrs.get("role")
            if rol and self.ROLES_REDUNDANTES.get(tag) == rol:
                self.roles_redundantes.append((tag, linea))
        rol_attr = attrs.get("role")
        if rol_attr in ("main", "banner", "contentinfo", "navigation"):
            self.landmarks_encontrados.add(rol_attr)

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._en_title = False
        elif tag == "table" and self._pila_tabla:
            self.tablas.append(self._pila_tabla.pop())
        elif tag == "a" and self._en_enlace:
            self._en_enlace = False
            self.enlaces.append(self._enlace_actual)

    def handle_data(self, data: str) -> None:
        if self._en_title:
            self.title_texto += data
        if self._en_enlace:
            self._enlace_actual["texto"] += data


def validar(analizador: AnalizadorHTML) -> List[Hallazgo]:
    """Aplica las reglas de validación y devuelve los hallazgos."""
    h: List[Hallazgo] = []

    # Idioma (3.1.1).
    if not analizador.html_lang:
        h.append(Hallazgo("FAIL", "3.1.1 Idioma",
                          "El elemento <html> no tiene atributo lang.",
                          sugerencia='Agregar lang="es-CO" a <html>.'))
    else:
        h.append(Hallazgo("OK", "3.1.1 Idioma",
                          f'Idioma declarado: lang="{analizador.html_lang}".'))

    # Título (2.4.2).
    if not analizador.tiene_title or not analizador.title_texto.strip():
        h.append(Hallazgo("FAIL", "2.4.2 Título",
                          "Falta <title> o está vacío.",
                          sugerencia="Agregar un <title> descriptivo."))
    else:
        h.append(Hallazgo("OK", "2.4.2 Título",
                          f'Título: "{analizador.title_texto.strip()}".'))

    # Encabezados (1.3.1 / 2.4.10).
    niveles = [n for n, _ in analizador.encabezados]
    n_h1 = niveles.count(1)
    if n_h1 == 0:
        h.append(Hallazgo("FAIL", "1.3.1 Encabezados",
                          "No hay <h1> en la página.",
                          sugerencia="Incluir un único <h1> principal."))
    elif n_h1 > 1:
        h.append(Hallazgo("WARN", "1.3.1 Encabezados",
                          f"Hay {n_h1} elementos <h1> (se recomienda uno).",
                          sugerencia="Dejar un solo <h1> por página."))
    else:
        h.append(Hallazgo("OK", "1.3.1 Encabezados", "Existe un único <h1>."))

    anterior = 0
    for nivel, linea in analizador.encabezados:
        if anterior and nivel > anterior + 1:
            h.append(Hallazgo(
                "WARN", "1.3.1 Jerarquía",
                f"Salto de h{anterior} a h{nivel}.", linea,
                "No saltar niveles de encabezado (h2 → h4)."))
        anterior = nivel

    # Imágenes (1.1.1).
    sin_alt = [im for im in analizador.imagenes
               if not im["tiene_alt"] and im.get("aria_hidden") != "true"
               and im.get("rol") != "presentation"]
    if sin_alt:
        for im in sin_alt:
            h.append(Hallazgo("FAIL", "1.1.1 Texto alternativo",
                              "Imagen sin atributo alt.", im["linea"],
                              'Agregar alt descriptivo o alt="" si es decorativa.'))
    elif analizador.imagenes:
        h.append(Hallazgo("OK", "1.1.1 Texto alternativo",
                          f"Las {len(analizador.imagenes)} imágenes tienen alt."))

    # Tablas (1.3.1).
    for t in analizador.tablas:
        if t["th"] == 0:
            h.append(Hallazgo("WARN", "1.3.1 Tablas",
                              "Tabla sin celdas de encabezado <th>.", t["linea"],
                              "Usar <th> para encabezados de fila/columna."))
        elif t["scope"] == 0:
            h.append(Hallazgo("WARN", "1.3.1 Tablas",
                              "<th> sin atributo scope.", t["linea"],
                              'Agregar scope="col" o scope="row".'))
        if not t["caption"]:
            h.append(Hallazgo("WARN", "1.3.1 Tablas",
                              "Tabla sin <caption>.", t["linea"],
                              "Agregar <caption> que describa la tabla."))

    # Formularios (1.3.1 / 3.3.2 / 4.1.2).
    for inp in analizador.inputs:
        tiene_nombre = (
            (inp["id"] and inp["id"] in analizador.labels_for)
            or inp["aria_label"] or inp["aria_labelledby"]
        )
        if not tiene_nombre:
            h.append(Hallazgo(
                "FAIL", "3.3.2 Etiquetas",
                f"<{inp['tag']}> sin etiqueta asociada.", inp["linea"],
                "Asociar <label for> o usar aria-label / aria-labelledby."))
    if analizador.inputs and not any(
        x.regla.startswith("3.3.2") and x.nivel == "FAIL" for x in h
    ):
        h.append(Hallazgo("OK", "3.3.2 Etiquetas",
                          "Todos los campos tienen etiqueta accesible."))

    # Enlaces (2.4.4).
    for a in analizador.enlaces:
        texto = (a["texto"] or "").strip()
        nombre = texto or a["aria_label"]
        if not a["href"]:
            # Un <a> sin href es un ancla, no un enlace en el árbol de
            # accesibilidad; no se le exige nombre accesible.
            h.append(Hallazgo("WARN", "2.4.4 Enlaces",
                              "Enlace <a> sin href.", a["linea"],
                              "Usar <button> para acciones sin navegación."))
        elif not nombre:
            h.append(Hallazgo("FAIL", "2.4.4 Enlaces",
                              "Enlace sin texto ni nombre accesible.", a["linea"],
                              "Agregar texto visible o aria-label."))

    # Landmarks (1.3.1 / 2.4.1).
    faltantes = {"main", "header", "footer"} - analizador.landmarks_encontrados
    # 'banner'/'contentinfo' equivalen a header/footer por rol.
    if "banner" in analizador.landmarks_encontrados:
        faltantes.discard("header")
    if "contentinfo" in analizador.landmarks_encontrados:
        faltantes.discard("footer")
    if "main" in analizador.landmarks_encontrados:
        faltantes.discard("main")
    if faltantes:
        h.append(Hallazgo("WARN", "1.3.1 Landmarks",
                          f"Faltan landmarks: {', '.join(sorted(faltantes))}.",
                          sugerencia="Usar <main>, <header>, <footer> o roles."))
    else:
        h.append(Hallazgo("OK", "1.3.1 Landmarks",
                          "Landmarks principales presentes."))

    # Roles redundantes (4.1.2).
    for tag, linea in analizador.roles_redundantes:
        h.append(Hallazgo("WARN", "4.1.2 ARIA",
                          f"Rol redundante en <{tag}>.", linea,
                          f"Eliminar role en <{tag}> (ya es implícito)."))

    # Iframes (4.1.2).
    for f in analizador.iframes:
        if not f["title"]:
            h.append(Hallazgo("WARN", "4.1.2 Iframe",
                              "<iframe> sin atributo title.", f["linea"],
                              "Agregar title descriptivo al iframe."))

    # Skip link (2.4.1).
    if analizador.skip_link:
        h.append(Hallazgo("OK", "2.4.1 Skip link",
                          "Se detectó un posible enlace de salto al inicio."))
    else:
        h.append(Hallazgo("WARN", "2.4.1 Skip link",
                          "No se detectó skip link al inicio del documento.",
                          sugerencia='Agregar <a href="#main">Saltar al contenido</a>.'))

    return h


def cargar_html(args) -> List[Tuple[str, str]]:
    """Devuelve una lista de (origen, contenido_html) según los argumentos."""
    fuentes: List[Tuple[str, str]] = []
    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            fuentes.append((args.file, f.read()))
    elif args.url:
        fuentes.append((args.url, _descargar(args.url)))
    elif args.urls:
        with open(args.urls, "r", encoding="utf-8") as f:
            for linea in f:
                u = linea.strip()
                if u:
                    fuentes.append((u, _descargar(u)))
    return fuentes


def _descargar(url: str) -> str:
    """Descarga el HTML de una URL (urllib estándar)."""
    from urllib.request import Request, urlopen
    req = Request(url, headers={"User-Agent": "accesibilidad-wcag/2.0"})
    with urlopen(req, timeout=20) as resp:  # noqa: S310
        datos = resp.read()
    return datos.decode("utf-8", errors="replace")


def analizar_documento(html_str: str) -> List[Hallazgo]:
    """Analiza una cadena HTML y devuelve los hallazgos."""
    parser = AnalizadorHTML()
    parser.feed(html_str)
    return validar(parser)


def imprimir_consola(origen: str, hallazgos: List[Hallazgo]) -> Dict[str, int]:
    """Imprime los hallazgos y devuelve el conteo por nivel."""
    print(f"\n=== {origen} ===")
    conteo = {"OK": 0, "WARN": 0, "FAIL": 0}
    for hh in hallazgos:
        conteo[hh.nivel] += 1
        linea = f" (línea {hh.linea})" if hh.linea else ""
        print(f"{NIVEL[hh.nivel]} [{hh.regla}] {hh.mensaje}{linea}")
        if hh.sugerencia and hh.nivel != "OK":
            print(f"    → {hh.sugerencia}")
    total = sum(conteo.values())
    print(f"\nResumen: {total} validaciones | "
          f"✅ {conteo['OK']} | ⚠️ {conteo['WARN']} | ❌ {conteo['FAIL']}")
    return conteo


def generar_reporte_html(resultados: List[Tuple[str, List[Hallazgo]]],
                         ruta: str) -> None:
    """Genera un reporte HTML con los hallazgos de validación semántica."""
    bloques = []
    for origen, hallazgos in resultados:
        filas = []
        for hh in hallazgos:
            linea = hh.linea if hh.linea else "—"
            filas.append(
                f"<tr><td>{NIVEL[hh.nivel]}</td><td>{hh.regla}</td>"
                f"<td>{hh.mensaje}</td><td>{linea}</td>"
                f"<td>{hh.sugerencia or '—'}</td></tr>"
            )
        bloques.append(
            f"<h2>{origen}</h2><table><thead><tr><th>Nivel</th>"
            "<th>Regla</th><th>Mensaje</th><th>Línea</th>"
            "<th>Sugerencia</th></tr></thead><tbody>"
            + "".join(filas) + "</tbody></table>"
        )
    html = (
        '<!DOCTYPE html><html lang="es-CO"><head><meta charset="UTF-8">'
        "<title>Reporte de validación semántica</title>"
        "<style>body{font-family:sans-serif;padding:2rem;}"
        "table{border-collapse:collapse;width:100%;margin-bottom:2rem;}"
        "th,td{border:1px solid #ccc;padding:.4rem .6rem;text-align:left;}"
        "th{background:#f2f4f7;}</style></head><body>"
        "<h1>Reporte de validación semántica HTML</h1>"
        + "".join(bloques) + "</body></html>"
    )
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"\nReporte HTML generado: {ruta}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validador de estructura semántica HTML (WCAG 2.2)."
    )
    parser.add_argument("--file", help="Ruta a un archivo HTML local.")
    parser.add_argument("--url", help="URL a validar.")
    parser.add_argument("--urls", help="Archivo de texto con una URL por línea.")
    parser.add_argument("--report", help="Ruta de salida para reporte HTML.")
    args = parser.parse_args()

    if not (args.file or args.url or args.urls):
        parser.print_help()
        return 1

    try:
        fuentes = cargar_html(args)
    except (FileNotFoundError, OSError) as e:
        print(f"Error al cargar la fuente: {e}", file=sys.stderr)
        return 1

    resultados: List[Tuple[str, List[Hallazgo]]] = []
    total_fail = 0
    for origen, contenido in fuentes:
        hallazgos = analizar_documento(contenido)
        conteo = imprimir_consola(origen, hallazgos)
        total_fail += conteo["FAIL"]
        resultados.append((origen, hallazgos))

    if args.report:
        generar_reporte_html(resultados, args.report)

    # Código de salida: 2 si hay fallos críticos, 0 si no.
    return 2 if total_fail else 0


if __name__ == "__main__":
    sys.exit(main())
