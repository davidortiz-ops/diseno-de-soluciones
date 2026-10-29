"""
calculate_score.py — Calcula la Puntuación General de experiencia y el ranking
de hallazgos desde un JSON de la revisión heurística de Tognazzini.

Uso:
    python scripts/calculate_score.py <archivo-hallazgos.json>

Ejemplo:
    python scripts/calculate_score.py scripts/sample-findings.json

Requisitos: Python 3.8+, sin dependencias externas.
Salida: Puntuación General, distribución por grupo de priorización, heurística
más violada, ranking de hallazgos por Promedio total y alertas por consola.
"""

import json
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass


def load_findings(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return data["findings"], data.get("context", {})


def priority_group(difficulty):
    if difficulty <= 1:
        return "Quick win"
    if difficulty == 2:
        return "Mediana"
    return "Estructural"


def calculate(findings):
    total = len(findings)
    if total == 0:
        return 10.0, {}, {}, []

    graded = [f for f in findings if f.get("severity", 0) > 0]
    avg_severity = sum(f.get("severity", 0) for f in graded) / len(graded) if graded else 0
    score = round(10 - (avg_severity * 10 / 3), 1)

    groups = {"Quick win": 0, "Mediana": 0, "Estructural": 0}
    for f in findings:
        groups[priority_group(f.get("difficulty", 0))] += 1

    severity_3_pct = round(sum(1 for f in findings if f.get("severity", 0) == 3) / total * 100, 1)
    structural_pct = round(groups["Estructural"] / total * 100, 1)

    alerts = {
        "severity_3_pct": severity_3_pct,
        "structural_pct": structural_pct,
    }

    ranked = sorted(
        findings,
        key=lambda f: (f.get("severity", 0) + f.get("difficulty", 0)) / 2,
        reverse=True,
    )

    return score, groups, alerts, ranked


def interpret_score(score):
    if score >= 9.0:
        return "Excelente"
    elif score >= 7.0:
        return "Buena"
    elif score >= 5.0:
        return "Regular"
    elif score >= 3.0:
        return "Deficiente"
    else:
        return "Crítica"


def most_violated_heuristic(findings):
    counts = {}
    for f in findings:
        h = f.get("heuristic", "—")
        counts[h] = counts.get(h, 0) + 1
    if not counts:
        return "—"
    max_count = max(counts.values())
    top = [h for h, c in counts.items() if c == max_count]
    return f"{', '.join(top)} ({max_count} hallazgos)"


def print_report(score, groups, alerts, ranked, context):
    total = sum(groups.values())
    name = context.get("product", "—")
    credit_type = context.get("credit_type", "—")

    print("=" * 60)
    print("  TOGNAZZINI — Puntuación General de Experiencia")
    print("=" * 60)
    print(f"  Producto:        {name}")
    print(f"  Tipo de crédito: {credit_type}")
    print(f"  Total hallazgos: {total}")
    print()
    print(f"  Puntuación General: {score}/10 — {interpret_score(score)}")
    print(f"  Heurística más violada: {most_violated_heuristic(ranked)}")
    print()
    print("  Distribución por grupo de priorización:")
    for group in ["Quick win", "Mediana", "Estructural"]:
        count = groups.get(group, 0)
        pct = round(count / total * 100, 1) if total > 0 else 0
        bar = "▓" * count + "░" * max(0, 20 - count)
        print(f"    {group:12s} | {bar} {count} ({pct}%)")

    print()
    print("  Ranking de hallazgos (Promedio total descendente):")
    for f in ranked:
        avg = (f.get("severity", 0) + f.get("difficulty", 0)) / 2
        group = priority_group(f.get("difficulty", 0))
        print(f"    #{f.get('id')} [{avg:.1f}] {group:11s} — {f.get('heuristic')}: {f.get('description', '')[:60]}")

    print()
    if alerts["severity_3_pct"] > 20:
        print(f"  🚨 ALERTA: {alerts['severity_3_pct']}% de los hallazgos tienen Gravedad 3 (límite: 20%)")
    if alerts["structural_pct"] > 40:
        print(f"  🟡 ALERTA: {alerts['structural_pct']}% de los hallazgos son Estructurales (límite: 40%) — requiere patrocinio ejecutivo")
    print("=" * 60)


def main():
    if len(sys.argv) < 2:
        print("Uso: python scripts/calculate_score.py <archivo-hallazgos.json>")
        sys.exit(1)

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"Error: no se encuentra el archivo {path}")
        sys.exit(1)

    findings, context = load_findings(path)
    score, groups, alerts, ranked = calculate(findings)
    print_report(score, groups, alerts, ranked, context)


if __name__ == "__main__":
    main()
