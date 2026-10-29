"""
generate_report.py — Genera un reporte de evaluación heurística en markdown.

Uso:
    python scripts/generate_report.py <archivo-hallazgos.json> [--output reporte.md] [--template ejecutiva|completa]

Ejemplo:
    python scripts/generate_report.py hallazgos.json --output reporte.md
    python scripts/generate_report.py hallazgos.json --template ejecutiva

Requiere: calculate_score.py en el mismo directorio
"""

import json
import sys
import argparse
from pathlib import Path
from datetime import date
from calculate_score import calculate, interpret_score

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass


SEVERITY_LABELS = {4: "Catastrófico", 3: "Mayor", 2: "Menor", 1: "Cosmético", 0: "Sin problema"}
EFFORT_ORDER = {"Pequeño": 1, "Medio": 2, "Grande": 3}


def load_findings(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return data["findings"], data.get("context", {})


def build_matrix(findings):
    quick_wins = []
    major_projects = []
    fill_ins = []
    thankless = []

    for f in findings:
        effort = f.get("effort", "Medio")
        severity = f.get("severity", 2)
        effort_val = EFFORT_ORDER.get(effort, 2)

        if severity >= 3 and effort_val <= 2:
            quick_wins.append(f)
        elif severity >= 3 and effort_val > 2:
            major_projects.append(f)
        elif severity < 3 and effort_val <= 2:
            fill_ins.append(f)
        else:
            thankless.append(f)

    return quick_wins, major_projects, fill_ins, thankless


def generate_complete(findings, context, score, distribution):
    total = sum(distribution.values())
    name = context.get("product", "—")
    industry = context.get("industry", "—")
    scope = context.get("scope", "—")
    evaluator = context.get("evaluator", "—")
    eval_date = context.get("date", str(date.today()))
    qw, mp, fi, tl = build_matrix(findings)

    lines = []
    lines.append(f"# Reporte de Evaluación Heurística")
    lines.append(f"")
    lines.append(f"## 1. Resumen Ejecutivo")
    lines.append(f"")
    lines.append(f"| Ítem | Detalle |")
    lines.append(f"|---|---|")
    lines.append(f"| **Producto** | {name} |")
    lines.append(f"| **Industria** | {industry} |")
    lines.append(f"| **Alcance** | {scope} |")
    lines.append(f"| **Evaluador** | {evaluator} |")
    lines.append(f"| **Fecha** | {eval_date} |")
    lines.append(f"| **Total hallazgos** | {total} |")
    lines.append(f"")
    lines.append(f"**Score Global: {score}/10 — {interpret_score(score)}**")
    lines.append(f"")
    lines.append(f"| Severidad | Cantidad | % |")
    lines.append(f"|---|---|---|")
    for level in [4, 3, 2, 1]:
        count = distribution.get(level, 0)
        label = SEVERITY_LABELS[level]
        pct = round(count / total * 100, 1) if total > 0 else 0
        lines.append(f"| **{label}** | {count} | {pct}% |")

    lines.append(f"")
    lines.append(f"**Heurística más violada:** {most_violated_heuristic(findings)}")
    lines.append(f"")

    lines.append(f"### Problemas Críticos")
    criticals = [f for f in findings if f.get("severity", 0) >= 3]
    for i, c in enumerate(criticals[:5], 1):
        lines.append(f"{i}. **H{c.get('heuristic')} — {c.get('title')}** ({SEVERITY_LABELS[c.get('severity', 0)]}) — {c.get('recommendation')}")
    lines.append(f"")

    lines.append(f"## 2. Hallazgos Detallados")
    lines.append(f"")
    lines.append(f"| # | Heur. | Severidad | Título | Ubicación | Recomendación | Esfuerzo |")
    lines.append(f"|---|---|---|---|---|---|---|")
    for f in findings:
        lines.append(f"| {f.get('id')} | {f.get('heuristic')} | {f.get('severity')} | {f.get('title')} | {f.get('location')} | {f.get('recommendation')} | {f.get('effort', '—')} |")
    lines.append(f"")

    lines.append(f"## 3. Matriz de Priorización (Impacto vs Esfuerzo)")
    lines.append(f"")
    lines.append(f"### Quick Wins (Alto Impacto, Bajo Esfuerzo)")
    for f in qw:
        lines.append(f"- **#{f.get('id')}** — {f.get('title')}")
    lines.append(f"")
    lines.append(f"### Major Projects (Alto Impacto, Alto Esfuerzo)")
    for f in mp:
        lines.append(f"- **#{f.get('id')}** — {f.get('title')}")
    lines.append(f"")
    lines.append(f"### Fill-ins (Bajo Impacto, Bajo Esfuerzo)")
    for f in fi:
        lines.append(f"- **#{f.get('id')}** — {f.get('title')}")
    lines.append(f"")
    lines.append(f"### Thankless (Bajo Impacto, Alto Esfuerzo)")
    for f in tl:
        lines.append(f"- **#{f.get('id')}** — {f.get('title')}")
    lines.append(f"")

    lines.append(f"## 4. Roadmap Sugerido")
    lines.append(f"")
    lines.append(f"### Fase 1 — Quick Wins (< 1 semana)")
    for f in qw:
        lines.append(f"- #{f.get('id')} {f.get('title')} — {f.get('recommendation')}")
    lines.append(f"")
    lines.append(f"### Fase 2 — Corto Plazo (1-4 semanas)")
    for f in mp[:3]:
        lines.append(f"- #{f.get('id')} {f.get('title')}")
    lines.append(f"")
    lines.append(f"### Fase 3 — Mediano Plazo (1-3 meses)")
    for f in mp[3:]:
        lines.append(f"- #{f.get('id')} {f.get('title')}")
    lines.append(f"")
    lines.append(f"### Fase 4 — Estratégico (3+ meses)")
    for f in tl + fi:
        lines.append(f"- #{f.get('id')} {f.get('title')}")
    lines.append(f"")

    return "\n".join(lines)


def generate_executive(findings, context, score, distribution):
    total = sum(distribution.values())
    name = context.get("product", "—")
    qw, mp, fi, tl = build_matrix(findings)

    lines = []
    lines.append(f"# Evaluación Heurística — {name}")
    lines.append(f"**Score Global: {score}/10 — {interpret_score(score)}**")
    lines.append(f"**Total hallazgos:** {total}")
    lines.append(f"")

    lines.append(f"## Top Problemas Críticos")
    criticals = [f for f in findings if f.get("severity", 0) >= 3]
    for i, c in enumerate(criticals[:5], 1):
        lines.append(f"{i}. **H{c.get('heuristic')}** (S{c.get('severity')}) — {c.get('title')}")
    lines.append(f"")

    if qw:
        lines.append(f"## Quick Wins")
        for f in qw:
            lines.append(f"- {f.get('title')} → {f.get('recommendation')}")
        lines.append(f"")

    lines.append(f"## Próximos Pasos")
    if qw:
        lines.append(f"1. Abordar {len(qw)} Quick Wins identificados")
    if mp:
        lines.append(f"2. Planificar {len(mp)} Major Projects")
    lines.append(f"3. Programar validación con usuarios")

    return "\n".join(lines)


def most_violated_heuristic(findings):
    counts = {}
    for f in findings:
        h = f.get("heuristic", "H?")
        counts[h] = counts.get(h, 0) + 1
    if not counts:
        return "—"
    max_count = max(counts.values())
    top = [h for h, c in counts.items() if c == max_count]
    return f"{', '.join(top)} ({max_count} hallazgos)"


def main():
    parser = argparse.ArgumentParser(description="Genera reporte de evaluación heurística en markdown")
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
    score, distribution, _ = calculate(findings)

    if args.template == "ejecutiva":
        report = generate_executive(findings, context, score, distribution)
    else:
        report = generate_complete(findings, context, score, distribution)

    if args.output:
        out_path = Path(args.output)
        out_path.write_text(report, encoding="utf-8")
        print(f"Reporte guardado en: {out_path}")
    else:
        print(report)


if __name__ == "__main__":
    main()
