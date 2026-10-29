"""
validate_persona_findings.py — Valida hallazgos de evaluación contra el perfil del
cliente bancario Top Tier definido en proto-persona-banca-top-tier.

Verifica que los hallazgos sean consistentes con la perspectiva del segmento de altos
ingresos y alto patrimonio. Detecta hallazgos genéricos que no reflejan la perspectiva
del persona, severity inconsistentes y dimensiones mal asignadas.

Uso:
    python validate_persona_findings.py hallazgos.json
    python validate_persona_findings.py hallazgos.json --strict
    python validate_persona_findings.py hallazgos.json --fix output.json

Requisitos: Python 3.8+, solo biblioteca estándar.
"""

import argparse
import json
import sys
import os
import re

sys.stdout.reconfigure(encoding="utf-8")

DIMENSIONES = {
    1: "Eficiencia y Respeto al Tiempo",
    2: "Exclusividad y Personalización",
    3: "Seguridad y Confianza",
    4: "Preparación Internacional",
    5: "Consistencia Omnicanal",
    6: "Experiencia Premium",
}

SEVERIDAD_MAX = 4
SEVERIDAD_MIN = 0

PATRONES_GENERICOS = [
    r"el usuario",
    r"el cliente",
    r"los usuarios",
    r"se debe",
    r"es importante",
    r"es recomendable",
    r"buena práctica",
    r"mejorar la experiencia",
    r"podría ser",
]

FRASES_PERSONA = [
    "necesito",
    "mi patrimonio",
    "mi dinero",
    "no tengo tiempo",
    "esto debería",
    "quiero",
    "busco",
    "espero",
    "como cliente",
    "para mi perfil",
    "no es aceptable",
    "inaceptable",
    "solución, no un trámite",
    "alguien que entienda",
    "alternativas fuera del país",
    "seguro y estable",
    "mi ejecutivo",
    "mi asesor",
]

SEVERIDAD_DESCRIPCION = {
    0: "Ninguno — Cumple mis expectativas como cliente premium",
    1: "Bajo — Incomodidad menor, no afecta mi decisión",
    2: "Medio — Molesto, pero manejable con workaround",
    3: "Alto — Frustración mayor, llamaría a mi ejecutivo de cuenta",
    4: "Crítico — Me haría cambiarme de banco / abandonar el proceso",
}

LIMITES_PERFIL = [
    "No representa clientes ultra-high-net-worth (family offices)",
    "No representa usuarios aspiracionales de ingresos medios-altos",
    "No representa perfiles no bancarizados",
    "No representa comportamientos puramente especulativos",
    "No es solo digital — valora el contacto humano experto",
    "No es un usuario masivo — requiere propuestas personalizadas",
]


def cargar_hallazgos(ruta):
    with open(ruta, encoding="utf-8") as f:
        datos = json.load(f)
    hallazgos = datos.get("findings", datos if isinstance(datos, list) else [])
    if isinstance(hallazgos, dict):
        hallazgos = [hallazgos]
    return hallazgos, datos


def validar_estructura(hallazgos, strict=False):
    errores = []
    advertencias = []

    for idx, h in enumerate(hallazgos):
        hid = h.get("id", idx + 1)
        campos_requeridos = ["title", "description", "dimension", "severity"]
        if strict:
            campos_requeridos.extend(["persona_quote", "recommendation"])

        for campo in campos_requeridos:
            if campo not in h or (isinstance(h.get(campo), str) and not h[campo].strip()):
                errores.append(f"Hallazgo {hid}: falta o está vacío '{campo}'")

        dim = h.get("dimension")
        if dim is not None and dim not in range(1, 7):
            errores.append(f"Hallazgo {hid}: dimension '{dim}' inválida (debe ser 1-6)")

        sev = h.get("severity")
        if sev is not None and sev not in range(SEVERIDAD_MIN, SEVERIDAD_MAX + 1):
            errores.append(
                f"Hallazgo {hid}: severity '{sev}' inválida "
                f"(debe ser {SEVERIDAD_MIN}-{SEVERIDAD_MAX})"
            )

        desc = h.get("description", "")
        if desc and len(desc) < 20:
            advertencias.append(
                f"Hallazgo {hid}: descripción muy corta ({len(desc)} chars). "
                f"La perspectiva del cliente Top Tier requiere contexto."
            )

    return errores, advertencias


def validar_perspectiva_persona(hallazgos):
    advertencias = []

    for idx, h in enumerate(hallazgos):
        hid = h.get("id", idx + 1)
        desc = h.get("description", "").lower()
        title = h.get("title", "").lower()
        texto_completo = desc + " " + title

        tiene_voz_persona = any(frase in texto_completo for frase in FRASES_PERSONA)
        if not tiene_voz_persona:
            advertencias.append(
                f"Hallazgo {hid}: la descripción no usa la voz del cliente Top Tier. "
                f"Incluye frases en primera persona que reflejen su perspectiva "
                f"('necesito', 'mi patrimonio', 'espero', 'como cliente...')."
            )

        es_generico = any(re.search(p, texto_completo) for p in PATRONES_GENERICOS)
        if es_generico:
            advertencias.append(
                f"Hallazgo {hid}: usa lenguaje genérico de UX ('el usuario', 'se debe'). "
                f"Reescribe desde la perspectiva del cliente Top Tier en primera persona."
            )

        severidad = h.get("severity", 0)
        if severidad >= 3 and not h.get("persona_quote"):
            advertencias.append(
                f"Hallazgo {hid}: severidad {severidad} ({SEVERIDAD_DESCRIPCION[severidad]}) "
                f"sin frase textual del persona. Incluye persona_quote representativa."
            )

    return advertencias


def validar_consistencia_perfil(hallazgos):
    advertencias = []

    for idx, h in enumerate(hallazgos):
        hid = h.get("id", idx + 1)
        dim = h.get("dimension")
        desc = h.get("description", "").lower()

        if dim == 2:
            palabras_clave = ["personalizad", "exclusiv", "segmento", "perfil", "premium", "diferenciado"]
            if not any(p in desc for p in palabras_clave):
                advertencias.append(
                    f"Hallazgo {hid}: dimensión 'Exclusividad y Personalización' pero la "
                    f"descripción no menciona personalización, exclusividad o segmentación."
                )

        if dim == 3:
            palabras_clave = ["segur", "confianza", "protege", "privac", "patrimonio", "autentic"]
            if not any(p in desc for p in palabras_clave):
                advertencias.append(
                    f"Hallazgo {hid}: dimensión 'Seguridad y Confianza' pero la "
                    f"descripción no menciona seguridad, confianza o protección."
                )

        if dim == 4:
            palabras_clave = ["internacional", "moneda", "offshore", "extranjero", "multimoneda", "global"]
            if not any(p in desc for p in palabras_clave):
                advertencias.append(
                    f"Hallazgo {hid}: dimensión 'Preparación Internacional' pero la "
                    f"descripción no menciona capacidades internacionales o multimoneda."
                )

        sev = h.get("severity", 0)
        if sev == 4 and dim in (1, 3):
            if not h.get("persona_quote"):
                advertencias.append(
                    f"Hallazgo {hid}: severity Crítico (4) en dimensión clave "
                    f"'{DIMENSIONES[dim]}'. Un hallazgo de este nivel debe incluir "
                    f"cita textual que refleje la reacción del persona."
                )

    return advertencias


def validar_calidad_general(hallazgos):
    advertencias = []

    dimensiones_cubiertas = set(h.get("dimension") for h in hallazgos if h.get("dimension"))
    for d in range(1, 7):
        if d not in dimensiones_cubiertas:
            advertencias.append(
                f"Dimensión '{DIMENSIONES[d]}' no tiene hallazgos. "
                f"Considera evaluar también esta área desde la perspectiva del cliente Top Tier."
            )

    severidades = [h.get("severity", 0) for h in hallazgos]
    if severidades:
        promedio = sum(severidades) / len(severidades)
        if promedio < 0.5:
            advertencias.append(
                f"Severidad promedio muy baja ({promedio:.2f}). "
                f"Revisa si los hallazgos reflejan realmente el nivel de exigencia "
                f"del cliente Top Tier o si la evaluación fue indulgente."
            )
        if promedio > 3.5:
            advertencias.append(
                f"Severidad promedio muy alta ({promedio:.2f}). "
                f"La experiencia evaluada tiene problemas generalizados. "
                f"Probablemente el cliente Top Tier ya estaría evaluando otras opciones."
            )

    return advertencias


def generar_reporte_validacion(hallazgos, errores_estructurales, advertencias_estructurales,
                                advertencias_persona, advertencias_perfil, advertencias_calidad):
    lineas = []
    lineas.append("# Validación de Hallazgos — Proto-Persona Banca Top Tier")
    lineas.append("")

    total = len(hallazgos)
    total_errores = len(errores_estructurales)
    total_advertencias = (
        len(advertencias_estructurales)
        + len(advertencias_persona)
        + len(advertencias_perfil)
        + len(advertencias_calidad)
    )

    estado = "✅ VÁLIDO" if total_errores == 0 else "❌ INVÁLIDO"
    lineas.append(f"**Estado:** {estado}")
    lineas.append(f"**Hallazgos evaluados:** {total}")
    lineas.append(f"**Errores:** {total_errores}")
    lineas.append(f"**Advertencias:** {total_advertencias}")
    lineas.append("")
    lineas.append("---")
    lineas.append("")

    if errores_estructurales:
        lineas.append("## Errores Estructurales")
        lineas.append("")
        for e in errores_estructurales:
            lineas.append(f"- ❌ {e}")
        lineas.append("")
        lineas.append("---")
        lineas.append("")

    if advertencias_estructurales:
        lineas.append("## Advertencias de Estructura")
        lineas.append("")
        for a in advertencias_estructurales:
            lineas.append(f"- ⚠️ {a}")
        lineas.append("")
        lineas.append("---")
        lineas.append("")

    if advertencias_persona:
        lineas.append("## Voz y Perspectiva del Persona")
        lineas.append("")
        lineas.append("Los hallazgos deben reflejar la perspectiva en primera persona del cliente Top Tier.")
        lineas.append("")
        for a in advertencias_persona:
            lineas.append(f"- 👤 {a}")
        lineas.append("")
        lineas.append("---")
        lineas.append("")

    if advertencias_perfil:
        lineas.append("## Consistencia con el Perfil del Segmento")
        lineas.append("")
        for a in advertencias_perfil:
            lineas.append(f"- 🎯 {a}")
        lineas.append("")
        lineas.append("---")
        lineas.append("")

    if advertencias_calidad:
        lineas.append("## Calidad General de la Evaluación")
        lineas.append("")
        for a in advertencias_calidad:
            lineas.append(f"- 📊 {a}")
        lineas.append("")
        lineas.append("---")
        lineas.append("")

    lineas.append("## Límites del Perfil a Considerar")
    lineas.append("")
    for limite in LIMITES_PERFIL:
        lineas.append(f"- {limite}")
    lineas.append("")
    lineas.append("---")
    lineas.append("")

    lineas.append("## Resumen de Severidad")
    lineas.append("")
    lineas.append("| Nivel | Descripción |")
    lineas.append("|-------|-------------|")
    for sev in range(SEVERIDAD_MIN, SEVERIDAD_MAX + 1):
        count = sum(1 for h in hallazgos if h.get("severity") == sev)
        lineas.append(f"| {sev} | {SEVERIDAD_DESCRIPCION[sev]} | {count} hallazgo(s) |")
    lineas.append("")

    return "\n".join(lineas)


def auto_corregir(hallazgos):
    corregidos = 0

    for h in hallazgos:
        dim = h.get("dimension")
        if dim is not None and dim not in range(1, 7):
            h["dimension"] = 1
            corregidos += 1

        sev = h.get("severity")
        if sev is not None and sev not in range(SEVERIDAD_MIN, SEVERIDAD_MAX + 1):
            h["severity"] = max(SEVERIDAD_MIN, min(SEVERIDAD_MAX, sev))
            corregidos += 1

        if not h.get("title") and h.get("description"):
            h["title"] = h["description"][:60] + ("..." if len(h["description"]) > 60 else "")
            corregidos += 1

    return hallazgos, corregidos


def main():
    parser = argparse.ArgumentParser(
        description="Valida hallazgos de evaluación contra el perfil del cliente bancario Top Tier",
        epilog="Ejemplo: python validate_persona_findings.py hallazgos.json --strict",
    )
    parser.add_argument("input", help="Archivo JSON con los hallazgos a validar")
    parser.add_argument(
        "--strict", action="store_true",
        help="Validación estricta (requiere persona_quote y recommendation en todos los hallazgos)"
    )
    parser.add_argument(
        "--fix", metavar="OUTPUT",
        help="Corrige errores automáticamente y guarda el resultado en OUTPUT"
    )

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: No se encuentra el archivo '{args.input}'", file=sys.stderr)
        sys.exit(2)

    hallazgos, datos_originales = cargar_hallazgos(args.input)

    if args.fix:
        hallazgos, corregidos = auto_corregir(hallazgos)
        if isinstance(datos_originales, dict) and "findings" in datos_originales:
            datos_originales["findings"] = hallazgos
        else:
            datos_originales = hallazgos

        with open(args.fix, "w", encoding="utf-8") as f:
            json.dump(datos_originales, f, indent=2, ensure_ascii=False)
        print(f"Hallazgos corregidos guardados en: {args.fix} ({corregidos} correcciones)")
        sys.exit(0)

    errores_estructurales, advertencias_estructurales = validar_estructura(hallazgos, strict=args.strict)
    advertencias_persona = validar_perspectiva_persona(hallazgos)
    advertencias_perfil = validar_consistencia_perfil(hallazgos)
    advertencias_calidad = validar_calidad_general(hallazgos)

    reporte = generar_reporte_validacion(
        hallazgos,
        errores_estructurales,
        advertencias_estructurales,
        advertencias_persona,
        advertencias_perfil,
        advertencias_calidad,
    )

    print(reporte)

    if errores_estructurales:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
