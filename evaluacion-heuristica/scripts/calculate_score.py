"""
calculate_score.py — Calcula el score global de usabilidad desde un JSON de hallazgos.

Uso:
    python scripts/calculate_score.py <archivo-hallazgos.json>

Ejemplo:
    python scripts/calculate_score.py hallazgos.json

Salida: score global, distribución de severidad y alertas por consola.
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


def calculate(findings):
    total = len(findings)
    if total == 0:
        return 0.0, {}, {}

    distribution = {4: 0, 3: 0, 2: 0, 1: 0, 0: 0}
    severity_sum = 0

    for f in findings:
        s = f.get("severity", 0)
        distribution[s] = distribution.get(s, 0) + 1
        severity_sum += s

    avg_severity = severity_sum / total
    score = round(10 - avg_severity, 1)

    alerts = {
        "critical_pct": round(distribution[4] / total * 100, 1),
        "major_pct": round(distribution[3] / total * 100, 1),
    }

    return score, distribution, alerts


def interpret_score(score):
    if score >= 9.0:
        return "Excelente"
    elif score >= 7.0:
        return "Bueno"
    elif score >= 5.0:
        return "Regular"
    elif score >= 3.0:
        return "Malo"
    else:
        return "Crítico"


def print_report(score, distribution, alerts, context):
    total = sum(distribution.values())
    name = context.get("product", "—")
    industry = context.get("industry", "—")

    print("=" * 50)
    print("  HEURISTY — Score Global de Usabilidad")
    print("=" * 50)
    print(f"  Producto:     {name}")
    print(f"  Industria:    {industry}")
    print(f"  Total hallazgos: {total}")
    print()
    print(f"  Score Global: {score}/10 — {interpret_score(score)}")
    print()
    print("  Distribución de severidad:")
    for level in [4, 3, 2, 1, 0]:
        count = distribution.get(level, 0)
        label = {4: "Catastrófico", 3: "Mayor", 2: "Menor", 1: "Cosmético", 0: "Sin problema"}
        bar = "▓" * count + "░" * max(0, 20 - count)
        pct = round(count / total * 100, 1) if total > 0 else 0
        print(f"    {label[level]:12s} | {bar} {count} ({pct}%)")

    print()
    if alerts["critical_pct"] > 10:
        print(f"  🚨 ALERTA ROJA:   {alerts['critical_pct']}% son catastróficos (límite: 10%)")
    if alerts["major_pct"] > 25:
        print(f"  🟡 ALERTA AMARILLA: {alerts['major_pct']}% son mayores (límite: 25%)")
    print("=" * 50)


def main():
    if len(sys.argv) < 2:
        print("Uso: python scripts/calculate_score.py <archivo-hallazgos.json>")
        sys.exit(1)

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"Error: no se encuentra el archivo {path}")
        sys.exit(1)

    findings, context = load_findings(path)
    score, distribution, alerts = calculate(findings)
    print_report(score, distribution, alerts, context)


if __name__ == "__main__":
    main()
