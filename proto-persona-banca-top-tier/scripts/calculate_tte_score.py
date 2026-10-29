"""
calculate_tte_score.py — Calcula el Top Tier Experience Score (TTES) desde hallazgos estructurados.

Evalúa qué tan preparada está una experiencia digital bancaria para el segmento
de clientes de altos ingresos y alto patrimonio (Top Tier) según el perfil definido
en proto-persona-banca-top-tier.

Uso:
    python calculate_tte_score.py hallazgos.json
    python calculate_tte_score.py hallazgos.json --output reporte.md
    python calculate_tte_score.py hallazgos.json --json

Requisitos: Python 3.8+, solo biblioteca estándar.
"""

import argparse
import json
import sys
import os

sys.stdout.reconfigure(encoding="utf-8")

DIMENSIONES = {
    1: "Eficiencia y Respeto al Tiempo",
    2: "Exclusividad y Personalización",
    3: "Seguridad y Confianza",
    4: "Preparación Internacional",
    5: "Consistencia Omnicanal",
    6: "Experiencia Premium",
}

NIVELES_SEVERIDAD = {
    0: "Ninguno",
    1: "Bajo",
    2: "Medio",
    3: "Alto",
    4: "Crítico",
}

ANALISIS_TRANSVERSALES = {
    "friccion_momentos_verdad": "Fricción en momentos de verdad — Operaciones de alto valor donde confluyen eficiencia, seguridad y personalización",
    "brecha_promesa_realidad": "Brecha promesa vs realidad — El banco promete exclusividad pero la ejecución es genérica",
    "sobrecarga_seguridad": "Sobrecarga de seguridad mal diseñada — Controles frecuentes o complejos que dañan la eficiencia",
    "falta_continuidad": "Falta de continuidad contextual — El persona debe repetir información entre canales o sesiones",
    "experiencia_masiva": "Experiencia masiva disfrazada de premium — Funcionalidades premium cosméticas sin valor real",
}


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
        if "severity" not in h:
            errores.append(f"Hallazgo {hid}: falta 'severity'")
        elif h["severity"] not in range(0, 5):
            errores.append(f"Hallazgo {hid}: severity debe ser 0-4, got {h['severity']}")
        if "dimension" not in h:
            errores.append(f"Hallazgo {hid}: falta 'dimension'")
        elif h["dimension"] not in range(1, 7):
            errores.append(f"Hallazgo {hid}: dimension debe ser 1-6, got {h['dimension']}")
        if "title" not in h:
            errores.append(f"Hallazgo {hid}: falta 'title'")
    return errores


def calcular_tte_score(hallazgos):
    if not hallazgos:
        return 0.0, {}

    severidades = [h["severity"] for h in hallazgos]
    ttes_global = round(10 - (sum(severidades) / len(severidades)), 2)

    scores_dimension = {}
    for d in range(1, 7):
        h_dim = [h for h in hallazgos if h["dimension"] == d]
        if h_dim:
            avg_sev = sum(h["severity"] for h in h_dim) / len(h_dim)
            scores_dimension[d] = round(10 - avg_sev, 2)

    return ttes_global, scores_dimension


def distribucion_severidad(hallazgos):
    dist = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
    for h in hallazgos:
        dist[h["severity"]] += 1
    return dist


def detectar_patrones_transversales(hallazgos):
    patrones_detectados = {}

    dims_afectadas = set(h["dimension"] for h in hallazgos if h["severity"] >= 2)

    if 1 in dims_afectadas and 3 in dims_afectadas:
        patrones_detectados["sobrecarga_seguridad"] = {
            "patron": ANALISIS_TRANSVERSALES["sobrecarga_seguridad"],
            "hallazgos": [h["id"] for h in hallazgos if h["dimension"] in (1, 3) and h["severity"] >= 2],
        }

    if 2 in dims_afectadas and 6 in dims_afectadas:
        patrones_detectados["brecha_promesa_realidad"] = {
            "patron": ANALISIS_TRANSVERSALES["brecha_promesa_realidad"],
            "hallazgos": [h["id"] for h in hallazgos if h["dimension"] in (2, 6) and h["severity"] >= 2],
        }
        patrones_detectados["experiencia_masiva"] = {
            "patron": ANALISIS_TRANSVERSALES["experiencia_masiva"],
            "hallazgos": [h["id"] for h in hallazgos if h["dimension"] in (2, 6) and h["severity"] >= 3],
        }

    if 1 in dims_afectadas and 5 in dims_afectadas:
        patrones_detectados["falta_continuidad"] = {
            "patron": ANALISIS_TRANSVERSALES["falta_continuidad"],
            "hallazgos": [h["id"] for h in hallazgos if h["dimension"] in (1, 5) and h["severity"] >= 2],
        }

    hallazgos_criticos = [h for h in hallazgos if h["severity"] >= 3]
    if hallazgos_criticos:
        dims_criticas = set(h["dimension"] for h in hallazgos_criticos)
        if len(dims_criticas) >= 2:
            patrones_detectados["friccion_momentos_verdad"] = {
                "patron": ANALISIS_TRANSVERSALES["friccion_momentos_verdad"],
                "hallazgos": [h["id"] for h in hallazgos_criticos],
            }

    return patrones_detectados


def generar_insights(hallazgos, scores_dimension):
    insights = []

    peor_dim = min(scores_dimension, key=scores_dimension.get) if scores_dimension else None
    if peor_dim:
        nombre = DIMENSIONES[peor_dim]
        score = scores_dimension[peor_dim]
        if score < 5:
            insights.append(
                f"Dimensión crítica: {nombre} (Score: {score}). "
                f"El cliente Top Tier percibiría esta área como deficiente. "
                f"Requiere atención inmediata para retener el segmento."
            )
        elif score < 7:
            insights.append(
                f"Dimensión con oportunidad de mejora: {nombre} (Score: {score}). "
                f"El cliente Top Tier lo nota como funcional pero con fricciones."
            )

    severidad_alta = [h for h in hallazgos if h["severity"] >= 3]
    if len(severidad_alta) >= 3:
        insights.append(
            f"Riesgo de fuga detectado: {len(severidad_alta)} hallazgos de severidad "
            f"Alta o Crítica. El cliente Top Tier consideraría activamente otras opciones."
        )

    hallazgos_confianza = [h for h in hallazgos if h["dimension"] == 3 and h["severity"] >= 2]
    if hallazgos_confianza:
        insights.append(
            f"La seguridad y confianza ({len(hallazgos_confianza)} hallazgos) "
            f"es una preocupación central. El cliente Top Tier prioriza la protección "
            f"de su patrimonio sobre cualquier otra funcionalidad."
        )

    return insights


def grafico_barras_ascii(scores_dimension):
    lineas = ["\nScore por dimensión:"]
    for d in range(1, 7):
        score = scores_dimension.get(d, 0)
        barras = int(score / 10 * 20)
        barra = "█" * barras + "░" * (20 - barras)
        nombre_corto = DIMENSIONES[d].split("—")[0].strip()[:25]
        lineas.append(f"  {d}. {nombre_corto:25s} {barra} {score:.1f}")
    return "\n".join(lineas)


def interpretar_tte_score(score):
    if score >= 9:
        return "Excelente. Experiencia premium que cumple estándares internacionales."
    elif score >= 7:
        return "Sólida. Algunos detalles por pulir para el segmento Top Tier."
    elif score >= 5:
        return "Funcional pero con fricciones que molestan a un cliente Top Tier."
    elif score >= 3:
        return "Deficiente. El persona consideraría otras opciones."
    else:
        return "Crítica. El persona buscaría activamente otro banco."


def generar_reporte_texto(hallazgos, ttes_global, scores_dimension, distribucion, patrones, insights, evaluacion):
    lineas = []
    lineas.append("# Reporte Top Tier Experience Score (TTES)")
    lineas.append("")

    titulo = evaluacion.get("title", "Evaluación de experiencia digital bancaria")
    lineas.append(f"**Evaluación:** {titulo}")
    if evaluacion.get("url"):
        lineas.append(f"**URL:** {evaluacion['url']}")
    if evaluacion.get("product"):
        lineas.append(f"**Producto:** {evaluacion['product']}")
    if evaluacion.get("channel"):
        lineas.append(f"**Canal:** {evaluacion['channel']}")
    if evaluacion.get("date"):
        lineas.append(f"**Fecha:** {evaluacion['date']}")
    lineas.append("")
    lineas.append("---")
    lineas.append("")

    lineas.append("## TTES Global")
    lineas.append("")
    lineas.append(f"**{ttes_global:.1f}/10** — {interpretar_tte_score(ttes_global)}")
    lineas.append("")
    lineas.append("### Distribución de severidad")
    lineas.append("")
    for sev in range(4, -1, -1):
        count = distribucion[sev]
        barra = "█" * count + "░" * max(0, 10 - count)
        lineas.append(f"  {NIVELES_SEVERIDAD[sev]:10s} ({sev}): {barra} {count}")
    lineas.append("")
    lineas.append("---")
    lineas.append("")

    lineas.append("## Scores por Dimensión")
    lineas.append("")
    for d in range(1, 7):
        score = scores_dimension.get(d, 0)
        sev_prom = round(10 - score, 2) if score else 0
        lineas.append(f"**D{d}. {DIMENSIONES[d]}** — Score: **{score:.1f}/10** (Severidad promedio: {sev_prom})")
        h_dim = [h for h in hallazgos if h["dimension"] == d]
        for h in h_dim:
            sev_label = NIVELES_SEVERIDAD[h["severity"]]
            quote = f" — *{h.get('persona_quote', '')}*" if h.get("persona_quote") else ""
            lineas.append(f"  - [{sev_label}] {h['title']}{quote}")
        lineas.append("")
    lineas.append("---")
    lineas.append("")

    if patrones:
        lineas.append("## Patrones Transversales Detectados")
        lineas.append("")
        for key, info in patrones.items():
            lineas.append(f"- {info['patron']}")
            lineas.append(f"  Hallazgos relacionados: {', '.join(str(h) for h in info['hallazgos'])}")
        lineas.append("")
        lineas.append("---")
        lineas.append("")

    if insights:
        lineas.append("## Insights para el Segmento Top Tier")
        lineas.append("")
        for ins in insights:
            lineas.append(f"- {ins}")
        lineas.append("")
        lineas.append("---")
        lineas.append("")

    lineas.append(grafico_barras_ascii(scores_dimension))
    lineas.append("")

    return "\n".join(lineas)


def generar_json_output(hallazgos, ttes_global, scores_dimension, distribucion, patrones, insights):
    output = {
        "ttes_global": ttes_global,
        "interpretacion": interpretar_tte_score(ttes_global),
        "scores_dimension": {str(d): scores_dimension.get(d, 0) for d in range(1, 7)},
        "distribucion_severidad": {str(k): v for k, v in distribucion.items()},
        "total_hallazgos": len(hallazgos),
        "patrones_transversales": {
            k: {
                "descripcion": v["patron"],
                "hallazgos": v["hallazgos"],
            }
            for k, v in patrones.items()
        },
        "insights": insights,
    }
    return json.dumps(output, indent=2, ensure_ascii=False)


def main():
    parser = argparse.ArgumentParser(
        description="Calcula el Top Tier Experience Score (TTES) desde hallazgos estructurados",
        epilog="Ejemplo: python calculate_tte_score.py hallazgos.json --output reporte.md",
    )
    parser.add_argument("input", help="Archivo JSON con los hallazgos de evaluación")
    parser.add_argument("--output", "-o", help="Ruta para guardar el reporte generado (opcional)")
    parser.add_argument(
        "--json", action="store_true", help="Salida en formato JSON máquina-legible"
    )

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: No se encuentra el archivo '{args.input}'", file=sys.stderr)
        sys.exit(2)

    hallazgos, evaluacion = cargar_hallazgos(args.input)

    errores = validar_hallazgos(hallazgos)
    if errores:
        print("Error: Datos inválidos en el archivo de hallazgos:", file=sys.stderr)
        for e in errores:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(1)

    if not hallazgos:
        print("Error: No se encontraron hallazgos en el archivo.", file=sys.stderr)
        sys.exit(1)

    ttes_global, scores_dimension = calcular_tte_score(hallazgos)
    distribucion = distribucion_severidad(hallazgos)
    patrones = detectar_patrones_transversales(hallazgos)
    insights = generar_insights(hallazgos, scores_dimension)

    if args.json:
        salida = generar_json_output(hallazgos, ttes_global, scores_dimension, distribucion, patrones, insights)
    else:
        salida = generar_reporte_texto(hallazgos, ttes_global, scores_dimension, distribucion, patrones, insights, evaluacion)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(salida)
        print(f"Reporte guardado en: {args.output}")
    else:
        print(salida)

    sys.exit(0)


if __name__ == "__main__":
    main()
