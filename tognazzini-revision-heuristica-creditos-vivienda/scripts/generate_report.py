"""
generate_report.py — Genera el reporte de revisión heurística de Tognazzini en markdown.

Uso:
    python scripts/generate_report.py <archivo-hallazgos.json> [--output reporte.md] [--template completa|ejecutiva]

Ejemplo:
    python scripts/generate_report.py hallazgos.json --output reporte.md
    python scripts/generate_report.py hallazgos.json --template ejecutiva

Requiere: calculate_score.py en el mismo directorio. Python 3.8+, sin dependencias externas.
"""

import sys
import argparse
from pathlib import Path
from datetime import date
from calculate_score import calculate, interpret_score, priority_group, most_violated_heuristic, load_findings

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass


def build_groups(ranked):
    groups = {"Quick win": [], "Mediana": [], "Estructural": []}
    for f in ranked:
        groups[priority_group(f.get("difficulty", 0))].append(f)
    return groups


def generate_complete(ranked, context, score, groups_count, alerts):
    total = sum(groups_count.values())
    name = context.get("product", "—")
    credit_type = context.get("credit_type", "—")
    channels = ", ".join(context.get("channels", [])) or "—"
    scope = context.get("scope", "—")
    evaluator = context.get("evaluator", "—")
    eval_date = context.get("date", str(date.today()))
    groups = build_groups(ranked)

    lines = []
    lines.append("# Reporte de Revisión Heurística — Tognazzini")
    lines.append("")
    lines.append("## 1. Resumen Ejecutivo")
    lines.append("")
    lines.append("| Ítem | Detalle |")
    lines.append("|---|---|")
    lines.append(f"| **Producto** | {name} |")
    lines.append(f"| **Tipo de crédito** | {credit_type} |")
    lines.append(f"| **Canales evaluados** | {channels} |")
    lines.append(f"| **Alcance** | {scope} |")
    lines.append(f"| **Evaluador** | {evaluator} |")
    lines.append(f"| **Fecha** | {eval_date} |")
    lines.append(f"| **Total hallazgos** | {total} |")
    lines.append("")
    lines.append(f"**Puntuación General: {score}/10 — {interpret_score(score)}**")
    lines.append("")
    lines.append(f"**Heurística más violada:** {most_violated_heuristic(ranked)}")
    lines.append("")
    lines.append("| Grupo | Cantidad | % |")
    lines.append("|---|---|---|")
    for group in ["Quick win", "Mediana", "Estructural"]:
        count = groups_count.get(group, 0)
        pct = round(count / total * 100, 1) if total > 0 else 0
        lines.append(f"| {group} | {count} | {pct}% |")
    lines.append("")

    if alerts["severity_3_pct"] > 20:
        lines.append(f"> 🚨 **Alerta:** {alerts['severity_3_pct']}% de los hallazgos tienen Gravedad 3 (límite: 20%).")
    if alerts["structural_pct"] > 40:
        lines.append(f"> 🟡 **Alerta:** {alerts['structural_pct']}% de los hallazgos son Estructurales (límite: 40%) — requiere patrocinio ejecutivo.")
    lines.append("")

    lines.append("## 2. Tabla de Hallazgos (ordenados por Promedio total)")
    lines.append("")
    lines.append("| ID | Heurística Tognazzini | Descripción del problema | Evidencia / Captura | Gravedad (0-3) | Dificultad (0-3) | Promedio total | Explicación | Recomendación práctica |")
    lines.append("|---|---|---|---|---|---|---|---|---|")
    for f in ranked:
        avg = (f.get("severity", 0) + f.get("difficulty", 0)) / 2
        lines.append(
            f"| {f.get('id')} | {f.get('heuristic')} | {f.get('description')} | {f.get('evidence', '—')} "
            f"| {f.get('severity')} | {f.get('difficulty')} | {avg:.1f} | {f.get('explanation', '—')} | {f.get('recommendation')} |"
        )
    lines.append("")

    lines.append("## 3. Matriz de Priorización")
    lines.append("")
    for group, emoji in [("Quick win", "🟢"), ("Mediana", "🟠"), ("Estructural", "🔴")]:
        lines.append(f"### {emoji} {group}")
        if not groups[group]:
            lines.append("- Sin hallazgos en este grupo.")
        for f in groups[group]:
            lines.append(f"- **#{f.get('id')}** ({f.get('heuristic')}) — {f.get('recommendation')}")
        lines.append("")

    lines.append("## 4. Roadmap por Fases")
    lines.append("")
    lines.append("### Fase 1 — Quick Wins (< 1 semana)")
    for f in groups["Quick win"]:
        lines.append(f"- #{f.get('id')} {f.get('heuristic')} — {f.get('recommendation')}")
    lines.append("")
    lines.append("### Fase 2 — Medianas (1-4 semanas)")
    for f in groups["Mediana"]:
        lines.append(f"- #{f.get('id')} {f.get('heuristic')} — {f.get('recommendation')}")
    lines.append("")
    lines.append("### Fase 3 — Estructurales (1-3+ meses)")
    for f in groups["Estructural"]:
        lines.append(f"- #{f.get('id')} {f.get('heuristic')} — {f.get('recommendation')}")
    lines.append("")
    lines.append("### Fase 4 — Mejora Continua")
    lines.append("- Definir frecuencia de auditorías heurísticas (mínimo semestral).")
    lines.append("- Incluir design reviews accesibles a áreas no técnicas antes de lanzar cambios.")
    lines.append("- Integrar las mejoras en procesos y políticas internas, no solo en pantallas.")
    lines.append("- Medir tasa de finalización, tiempo por etapa, PQR y satisfacción del solicitante.")
    lines.append("")

    return "\n".join(lines)


def generate_executive(ranked, context, score, groups_count, alerts):
    total = sum(groups_count.values())
    name = context.get("product", "—")
    groups = build_groups(ranked)

    lines = []
    lines.append(f"# Revisión Heurística Tognazzini — {name}")
    lines.append(f"**Puntuación General: {score}/10 — {interpret_score(score)}**")
    lines.append(f"**Total hallazgos:** {total}")
    lines.append("")

    lines.append("## Top Hallazgos Críticos")
    criticals = [f for f in ranked if f.get("severity", 0) == 3]
    for i, c in enumerate(criticals[:5], 1):
        lines.append(f"{i}. **{c.get('heuristic')}** (Gravedad {c.get('severity')}, Dificultad {c.get('difficulty')}) — {c.get('description')}")
    lines.append("")

    if groups["Quick win"]:
        lines.append("## Quick Wins")
        for f in groups["Quick win"]:
            lines.append(f"- {f.get('heuristic')} → {f.get('recommendation')}")
        lines.append("")

    lines.append("## Próximos Pasos")
    if groups["Quick win"]:
        lines.append(f"1. Abordar {len(groups['Quick win'])} quick wins identificados.")
    if groups["Mediana"]:
        lines.append(f"2. Coordinar {len(groups['Mediana'])} hallazgos medianos entre áreas.")
    if groups["Estructural"]:
        lines.append(f"3. Escalar {len(groups['Estructural'])} hallazgos estructurales a patrocinador ejecutivo.")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Genera el reporte de revisión heurística de Tognazzini en markdown")
    parser.add_argument("input", help="Archivo JSON con hallazgos")
    parser.add_argument("--output", "-o", default=None, help="Archivo de salida (opcional, por defecto stdout)")
    parser.add_argument("--template", "-t", choices=["completa", "ejecutiva"], default="completa",
                        help="Tipo de reporte (completa o ejecutiva)")
    args = parser.parse_args()

    path = Path(args.input)
    if not path.exists():
        print(f"Error: no se encuentra el archivo {path}")
        sys.exit(1)

    findings, context = load_findings(path)
    score, groups_count, alerts, ranked = calculate(findings)

    if args.template == "ejecutiva":
        report = generate_executive(ranked, context, score, groups_count, alerts)
    else:
        report = generate_complete(ranked, context, score, groups_count, alerts)

    if args.output:
        out_path = Path(args.output)
        out_path.write_text(report, encoding="utf-8")
        print(f"Reporte guardado en: {out_path}")
    else:
        print(report)


if __name__ == "__main__":
    main()
