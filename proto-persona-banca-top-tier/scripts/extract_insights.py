"""
extract_insights.py — Extrae insights y patrones de comportamiento del segmento Top Tier
a partir de hallazgos de evaluación estructurados.

Identifica patrones transversales, genera behavioral insights basados en el perfil
del cliente bancario de altos ingresos y prioriza acciones desde su perspectiva.

Uso:
    python extract_insights.py hallazgos.json
    python extract_insights.py hallazgos.json --output insights.md
    python extract_insights.py hallazgos.json --json

Requisitos: Python 3.8+, solo biblioteca estándar.
"""

import argparse
import json
import sys
import os

sys.stdout.reconfigure(encoding="utf-8")

PERFIL_PERSONA = {
    "segmento": "Clase Alta / Top Tier (1-5% superior de ingresos regional)",
    "rango_etario": "40-60 años",
    "ocupacion": "Cargos directivos, empresarios, agroexportadores, profesionales senior",
    "educacion": "Universitario completo o superior",
    "relacion_banca": "El banco es socio estratégico y gestor patrimonial, no solo proveedor",
    "expectativa_hibrida": "Autogestión digital para operaciones cotidianas + acceso directo a gerentes para decisiones complejas",
}

OBJETIVOS_FINANCIEROS = [
    "Preservación y crecimiento patrimonial a largo plazo",
    "Diversificación entre instrumentos financieros y no financieros",
    "Acceso a mercados internacionales y soluciones off-shore",
    "Protección frente a volatilidad económica y política regional",
    "Optimización fiscal y continuidad patrimonial familiar",
    "Eficiencia en gestión del tiempo y procesos financieros",
]

FRICCIONES = [
    "Inseguridad y exposición del patrimonio",
    "Burocracia y procesos lentos",
    "Oferta y asesoría genérica sin diferenciación",
    "Falta de privacidad en manejo de datos",
    "Exposición a errores operativos, fraudes o fallos de seguridad",
]

CONFIANZA = [
    "Reputación sólida y trayectoria institucional",
    "Atención personalizada profesional y consistente",
    "Cumplimiento impecable y discreción",
    "Estándares comparables a banca internacional",
]

DESCONFIANZA = [
    "Beneficios premium meramente cosméticos sin valor real",
    "Cambios frecuentes de ejecutivos sin continuidad",
    "Experiencia digital o humana genérica",
    "Percepción de improvisación o falta de criterio experto",
]

DIMENSIONES = {
    1: "Eficiencia y Respeto al Tiempo",
    2: "Exclusividad y Personalización",
    3: "Seguridad y Confianza",
    4: "Preparación Internacional",
    5: "Consistencia Omnicanal",
    6: "Experiencia Premium",
}

NIVELES_SEVERIDAD = {0: "Ninguno", 1: "Bajo", 2: "Medio", 3: "Alto", 4: "Crítico"}


def cargar_hallazgos(ruta):
    with open(ruta, encoding="utf-8") as f:
        datos = json.load(f)
    hallazgos = datos.get("findings", datos if isinstance(datos, list) else [])
    if isinstance(hallazgos, dict):
        hallazgos = [hallazgos]
    return hallazgos, datos.get("evaluation", {})


def validar_hallazgos(hallazgos):
    errores = []
    for h in hallazgos:
        hid = h.get("id", "?")
        if "severity" not in h or h["severity"] not in range(0, 5):
            errores.append(f"Hallazgo {hid}: severity inválida (debe ser 0-4)")
        if "dimension" not in h or h["dimension"] not in range(1, 7):
            errores.append(f"Hallazgo {hid}: dimension inválida (debe ser 1-6)")
        if "description" not in h:
            errores.append(f"Hallazgo {hid}: falta description")
    return errores


def analizar_distribucion_dimensiones(hallazgos):
    distribucion = {}
    for d in range(1, 7):
        h_d = [h for h in hallazgos if h["dimension"] == d]
        if h_d:
            severidad_prom = sum(h["severity"] for h in h_d) / len(h_d)
            distribucion[d] = {
                "total": len(h_d),
                "severidad_promedio": round(severidad_prom, 2),
                "criticos": len([h for h in h_d if h["severity"] >= 3]),
                "hallazgos": h_d,
            }
    return distribucion


def identificar_patrones_conductuales(hallazgos, distribucion):
    patrones = []

    dimensiones_afectadas = {d for d, info in distribucion.items() if info["severidad_promedio"] >= 2}

    if 3 in dimensiones_afectadas:
        h_confianza = distribucion[3]
        if h_confianza["severidad_promedio"] >= 2.5:
            patrones.append({
                "tipo": "alerta_seguridad",
                "titulo": "Alerta de seguridad patrimonial",
                "descripcion": (
                    "El cliente Top Tier prioriza la protección de su patrimonio sobre cualquier "
                    "otra funcionalidad. Hallazgos recurrentes en seguridad indican riesgo de fuga. "
                    "Para este segmento, la seguridad no es negociable — es la puerta de entrada "
                    "a cualquier relación bancaria."
                ),
                "severidad_promedio": h_confianza["severidad_promedio"],
                "hallazgos_relacionados": h_confianza["hallazgos"],
            })

    if 2 in dimensiones_afectadas and 6 in dimensiones_afectadas:
        patrones.append({
            "tipo": "brecha_premium",
            "titulo": "Brecha de experiencia premium",
            "descripcion": (
                "El cliente Top Tier detecta inmediatamente cuándo la experiencia 'premium' "
                "es cosmética. La combinación de problemas en Exclusividad y Experiencia Premium "
                "sugiere que el banco promete un trato diferenciado pero no lo ejecuta. "
                f"Factor de desconfianza identificado en el perfil: '{DESCONFIANZA[0]}'."
            ),
            "severidad_promedio": max(
                distribucion[2]["severidad_promedio"],
                distribucion[6]["severidad_promedio"],
            ),
            "hallazgos_relacionados": (
                distribucion[2]["hallazgos"] + distribucion[6]["hallazgos"]
            ),
        })

    if 1 in dimensiones_afectadas:
        h_eficiencia = distribucion[1]
        if h_eficiencia["severidad_promedio"] >= 2:
            patrones.append({
                "tipo": "friccion_tiempo",
                "titulo": "Fricción por tiempo perdido",
                "descripcion": (
                    "El tiempo del cliente Top Tier tiene alta valoración económica. "
                    "Procesos lentos o burocráticos son interpretados como falta de respeto "
                    "por su perfil. Frase representativa: 'Necesito resolver esto rápido, "
                    "no tengo tiempo para ir a la oficina'."
                ),
                "severidad_promedio": h_eficiencia["severidad_promedio"],
                "hallazgos_relacionados": h_eficiencia["hallazgos"],
            })

    if 4 in dimensiones_afectadas:
        h_internacional = distribucion[4]
        if h_internacional["severidad_promedio"] >= 2:
            patrones.append({
                "tipo": "brecha_internacional",
                "titulo": "Brecha de preparación internacional",
                "descripcion": (
                    "El cliente Top Tier opera en múltiples países y monedas. "
                    "La falta de soporte internacional limita su capacidad de gestionar "
                    "su patrimonio y contradice uno de sus objetivos principales: "
                    f"'{OBJETIVOS_FINANCIEROS[2]}'."
                ),
                "severidad_promedio": h_internacional["severidad_promedio"],
                "hallazgos_relacionados": h_internacional["hallazgos"],
            })

    return patrones


def generar_insights_conductuales(hallazgos, distribucion, patrones):
    insights = []

    severidad_alta = [h for h in hallazgos if h["severity"] >= 3]
    if severidad_alta:
        pct_alta = len(severidad_alta) / len(hallazgos) * 100
        if pct_alta > 30:
            insights.append({
                "tipo": "Riesgo de fuga",
                "nivel": "Crítico",
                "mensaje": (
                    f"El {pct_alta:.0f}% de los hallazgos son de severidad Alta o Crítica. "
                    "El cliente Top Tier tolera muy poca fricción. Este nivel de problemas "
                    "lo llevaría a buscar activamente otros bancos."
                ),
            })

    dims_criticas = [d for d, info in distribucion.items() if info["severidad_promedio"] >= 2.5]
    if dims_criticas:
        nombres = [DIMENSIONES[d] for d in dims_criticas]
        insights.append({
            "tipo": "Dimensiones críticas",
            "nivel": "Alto",
            "mensaje": (
                f"Las dimensiones más críticas para el segmento son: {'; '.join(nombres)}. "
                "Estas áreas definen la percepción de valor del cliente Top Tier y deben "
                "priorizarse en el roadmap."
            ),
        })

    dimensiones_con_hallazgos = [d for d, info in distribucion.items() if info["total"] > 0]
    if 5 not in dimensiones_con_hallazgos or distribucion[5]["severidad_promedio"] < 1:
        insights.append({
            "tipo": "Fortaleza omnicanal",
            "nivel": "Positivo",
            "mensaje": (
                "La dimensión de Consistencia Omnicanal presenta pocos o ningún hallazgo. "
                "Esto sugiere que el cliente Top Tier percibe continuidad entre canales, "
                "un factor crítico para su perfil híbrido (digital + asesoría humana)."
            ),
        })

    if patrones:
        insights.append({
            "tipo": "Patrones transversales detectados",
            "nivel": "Informativo",
            "mensaje": (
                f"Se detectaron {len(patrones)} patrones de comportamiento transversales. "
                "Estos patrones cruzan múltiples dimensiones y reflejan problemas "
                "estructurales en la experiencia del cliente Top Tier."
            ),
        })

    return insights


def priorizar_acciones(distribucion):
    prioridades = []
    for d in range(1, 7):
        info = distribucion.get(d)
        if not info:
            continue
        score_severidad = info["severidad_promedio"]
        cantidad = info["total"]
        criticos = info["criticos"]

        if score_severidad >= 3:
            prioridad = "Crítica"
        elif score_severidad >= 2:
            prioridad = "Alta"
        elif score_severidad >= 1:
            prioridad = "Media"
        else:
            prioridad = "Baja"

        prioridades.append({
            "dimension": d,
            "nombre": DIMENSIONES[d],
            "prioridad": prioridad,
            "severidad_promedio": score_severidad,
            "total_hallazgos": cantidad,
            "criticos": criticos,
        })

    prioridades.sort(key=lambda x: x["severidad_promedio"], reverse=True)
    return prioridades


def generar_reporte_insights(hallazgos, distribucion, patrones, insights, prioridades, evaluacion):
    lineas = []
    lineas.append("# Insights del Segmento Top Tier — Análisis Conductual")
    lineas.append("")

    titulo = evaluacion.get("title", "Evaluación de experiencia digital bancaria")
    lineas.append(f"**Evaluación:** {titulo}")
    if evaluacion.get("url"):
        lineas.append(f"**URL:** {evaluacion['url']}")
    if evaluacion.get("product"):
        lineas.append(f"**Producto:** {evaluacion['product']}")
    lineas.append("")
    lineas.append("---")
    lineas.append("")

    lineas.append("## Perfil del Segmento Evaluado")
    lineas.append("")
    lineas.append(f"- **Segmento:** {PERFIL_PERSONA['segmento']}")
    lineas.append(f"- **Rango etario:** {PERFIL_PERSONA['rango_etario']}")
    lineas.append(f"- **Ocupación:** {PERFIL_PERSONA['ocupacion']}")
    lineas.append(f"- **Relación con la banca:** {PERFIL_PERSONA['relacion_banca']}")
    lineas.append(f"- **Expectativa híbrida:** {PERFIL_PERSONA['expectativa_hibrida']}")
    lineas.append("")
    lineas.append("---")
    lineas.append("")
    lineas.append(f"**Total de hallazgos analizados:** {len(hallazgos)}")
    lineas.append("")
    lineas.append("---")
    lineas.append("")

    if patrones:
        lineas.append("## Patrones de Comportamiento Detectados")
        lineas.append("")
        for p in patrones:
            lineas.append(f"### {p['titulo']}")
            lineas.append("")
            lineas.append(f"Severidad promedio: {p['severidad_promedio']:.1f}/4")
            lineas.append("")
            lineas.append(p["descripcion"])
            lineas.append("")
        lineas.append("---")
        lineas.append("")

    if insights:
        lineas.append("## Insights Conductuales")
        lineas.append("")
        for ins in insights:
            nivel_icono = {"Crítico": "🚨", "Alto": "⚠️", "Positivo": "✅", "Informativo": "ℹ️"}
            icono = nivel_icono.get(ins["nivel"], "•")
            lineas.append(f"{icono} **{ins['tipo']}** ({ins['nivel']})")
            lineas.append("")
            lineas.append(f"  {ins['mensaje']}")
            lineas.append("")
        lineas.append("---")
        lineas.append("")

    lineas.append("## Priorización de Acciones desde la Perspectiva del Segmento")
    lineas.append("")
    lineas.append("| Prioridad | Dimensión | Severidad Prom. | Hallazgos | Críticos |")
    lineas.append("|-----------|-----------|:-:|:-:|:-:|")
    for p in prioridades:
        icono_p = {"Crítica": "🔴", "Alta": "🟠", "Media": "🟡", "Baja": "🟢"}
        lineas.append(
            f"| {icono_p.get(p['prioridad'], '•')} {p['prioridad']} "
            f"| {p['nombre']} "
            f"| {p['severidad_promedio']:.1f} "
            f"| {p['total_hallazgos']} "
            f"| {p['criticos']} |"
        )
    lineas.append("")
    lineas.append("---")
    lineas.append("")

    lineas.append("## Recomendaciones desde la Perspectiva del Cliente Top Tier")
    lineas.append("")
    for p in prioridades[:3]:
        if p["prioridad"] in ("Crítica", "Alta"):
            lineas.append(f"**{p['nombre']}** — Prioridad {p['prioridad']}")
            dim = p["dimension"]

            if dim == 1:
                lineas.append("  > 'Necesito resolver esto rápido, no tengo tiempo para ir a la oficina'")
                lineas.append("  > Optimizar flujos, reducir pasos, eliminar burocracia.")
            elif dim == 2:
                lineas.append("  > 'Necesito una solución, no un trámite'")
                lineas.append("  > Personalizar la experiencia, segmentar por perfil y patrimonio.")
            elif dim == 3:
                lineas.append("  > 'Busco algo seguro y estable para mi familia'")
                lineas.append("  > Reforzar señales de seguridad sin afectar eficiencia.")
            elif dim == 4:
                lineas.append("  > '¿Qué alternativas tengo fuera del país?'")
                lineas.append("  > Habilitar operaciones multimoneda e internacionales.")
            elif dim == 5:
                lineas.append("  > 'Esto debería poder hacerlo online'")
                lineas.append("  > Asegurar continuidad contextual entre canales digitales y humanos.")
            elif dim == 6:
                lineas.append("  > 'Busco un banco que entienda mi nivel'")
                lineas.append("  > Elevar la calidad estética y funcional al estándar internacional.")

            lineas.append("")

    return "\n".join(lineas)


def generar_json_output(hallazgos, distribucion, patrones, insights, prioridades):
    output = {
        "total_hallazgos": len(hallazgos),
        "distribucion_dimensiones": {
            str(d): {
                "nombre": DIMENSIONES[d],
                "total": info["total"],
                "severidad_promedio": info["severidad_promedio"],
                "criticos": info["criticos"],
            }
            for d, info in distribucion.items()
        },
        "patrones_conductuales": [
            {
                "tipo": p["tipo"],
                "titulo": p["titulo"],
                "descripcion": p["descripcion"],
                "severidad_promedio": p["severidad_promedio"],
            }
            for p in patrones
        ],
        "insights": [
            {"tipo": i["tipo"], "nivel": i["nivel"], "mensaje": i["mensaje"]}
            for i in insights
        ],
        "priorizacion": [
            {
                "dimension": p["dimension"],
                "nombre": p["nombre"],
                "prioridad": p["prioridad"],
                "severidad_promedio": p["severidad_promedio"],
                "criticos": p["criticos"],
            }
            for p in prioridades
        ],
    }
    return json.dumps(output, indent=2, ensure_ascii=False)


def main():
    parser = argparse.ArgumentParser(
        description="Extrae insights y patrones de comportamiento del segmento Top Tier desde hallazgos de evaluación",
        epilog="Ejemplo: python extract_insights.py hallazgos.json --output insights.md",
    )
    parser.add_argument("input", help="Archivo JSON con los hallazgos de evaluación")
    parser.add_argument("--output", "-o", help="Ruta para guardar el reporte de insights (opcional)")
    parser.add_argument("--json", action="store_true", help="Salida en formato JSON")

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: No se encuentra el archivo '{args.input}'", file=sys.stderr)
        sys.exit(2)

    hallazgos, evaluacion = cargar_hallazgos(args.input)
    errores = validar_hallazgos(hallazgos)
    if errores:
        print("Error: Datos inválidos:", file=sys.stderr)
        for e in errores:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(1)

    if not hallazgos:
        print("Error: No se encontraron hallazgos.", file=sys.stderr)
        sys.exit(1)

    distribucion = analizar_distribucion_dimensiones(hallazgos)
    patrones = identificar_patrones_conductuales(hallazgos, distribucion)
    insights = generar_insights_conductuales(hallazgos, distribucion, patrones)
    prioridades = priorizar_acciones(distribucion)

    if args.json:
        salida = generar_json_output(hallazgos, distribucion, patrones, insights, prioridades)
    else:
        salida = generar_reporte_insights(hallazgos, distribucion, patrones, insights, prioridades, evaluacion)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(salida)
        print(f"Reporte de insights guardado en: {args.output}")
    else:
        print(salida)

    sys.exit(0)


if __name__ == "__main__":
    main()
