#!/usr/bin/env python3
"""
validate_findings.py — Validador de esquema para hallazgos de evaluación heurística.

Verifica que un archivo JSON de hallazgos cumpla con el esquema esperado por
calculate_score.py y generate_report.py. Útil en CI o antes de generar reportes.

Uso:
    python scripts/validate_findings.py hallazgos.json
    python scripts/validate_findings.py hallazgos.json --strict
    python scripts/validate_findings.py hallazgos.json --fix

Modos:
    --strict   Exige que todos los campos opcionales estén presentes
    --fix      Corrige errores menores automáticamente (severidad fuera de rango,
               effort mal escrito, ids duplicados)

Códigos de salida: 0 (válido), 1 (errores encontrados), 2 (error de lectura).
"""

import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

CAMPO_OBLIGATORIO = {"heuristic", "title", "description", "severity", "recommendation"}
CAMPOS_HALLAZGO = {"id", "heuristic", "title", "location", "description",
                   "severity", "recommendation", "effort"}
CAMPOS_CONTEXTO = {"product", "industry", "scope", "evaluator", "date"}
HEURISTICAS_VALIDAS = {f"H{i}" for i in range(1, 15)} | {"H?"}
EFFORT_VALIDO = {"Pequeño", "Medio", "Grande"}
PATRON_FECHA = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def validar_hallazgo(h: Dict[str, Any], idx: int, strict: bool,
                     errors: List[str], warnings: List[str]) -> None:
    id_h = h.get("id", idx)

    faltantes = CAMPO_OBLIGATORIO - h.keys()
    if faltantes:
        errors.append(f"Hallazgo #{id_h}: faltan campos obligatorios: {', '.join(sorted(faltantes))}")
        return

    if not isinstance(h.get("severity"), int):
        errors.append(f"Hallazgo #{id_h}: severity debe ser entero, se encontró {type(h.get('severity')).__name__}")
    else:
        s = h["severity"]
        if s < 0 or s > 4:
            errors.append(f"Hallazgo #{id_h}: severity={s} fuera de rango 0-4")

    heur = h.get("heuristic", "")
    if heur not in HEURISTICAS_VALIDAS:
        warnings.append(f"Hallazgo #{id_h}: heuristic='{heur}' no está en el rango H1-H14")

    effort = h.get("effort")
    if effort and effort not in EFFORT_VALIDO:
        warnings.append(f"Hallazgo #{id_h}: effort='{effort}' debe ser Pequeño, Medio o Grande")

    if not h.get("title", "").strip():
        errors.append(f"Hallazgo #{id_h}: title está vacío")

    if not h.get("recommendation", "").strip():
        errors.append(f"Hallazgo #{id_h}: recommendation está vacía")

    if strict:
        opcionales_faltan = CAMPOS_HALLAZGO - h.keys()
        if opcionales_faltan:
            warnings.append(f"Hallazgo #{id_h}: faltan campos opcionales: {', '.join(sorted(opcionales_faltan))}")


def validar_contexto(ctx: Dict[str, Any], errors: List[str], warnings: List[str]) -> None:
    industry = ctx.get("industry", "")
    if industry and industry not in ("banca", "retail", "otro"):
        warnings.append(f"industry='{industry}' debería ser 'banca', 'retail' o 'otro'")

    fecha = ctx.get("date", "")
    if fecha and not PATRON_FECHA.match(str(fecha)):
        warnings.append(f"date='{fecha}' no sigue el formato AAAA-MM-DD")


def validar(archivo: str, strict: bool = False, fix: bool = False) -> int:
    path = Path(archivo)
    if not path.exists():
        print(f"Error: no se encuentra el archivo {archivo}", file=sys.stderr)
        return 2

    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        print(f"Error: JSON inválido — {e}", file=sys.stderr)
        return 2

    if not isinstance(data, dict):
        print("Error: la raíz del JSON debe ser un objeto con 'context' y 'findings'", file=sys.stderr)
        return 1

    if "context" not in data:
        print("Advertencia: falta el objeto 'context'")
        data["context"] = {}

    if "findings" not in data:
        print("Error: falta el array 'findings'", file=sys.stderr)
        return 1

    findings = data["findings"]
    if not isinstance(findings, list):
        print("Error: 'findings' debe ser un array", file=sys.stderr)
        return 1

    errors: List[str] = []
    warnings: List[str] = []
    ids_vistos: set = set()

    for i, h in enumerate(findings):
        if not isinstance(h, dict):
            errors.append(f"Hallazgo índice {i}: no es un objeto")
            continue

        validar_hallazgo(h, i, strict, errors, warnings)

        hid = h.get("id")
        if hid is not None:
            if hid in ids_vistos:
                errors.append(f"Hallazgo #{hid}: id duplicado")
            ids_vistos.add(hid)

    validar_contexto(data.get("context", {}), errors, warnings)

    if fix and errors:
        return _aplicar_fixes(path, data, errors)

    print(f"Archivo: {archivo}")
    print(f"Hallazgos: {len(findings)}")
    print(f"Estado: {'VÁLIDO' if not errors else 'INVÁLIDO'}")
    if errors:
        print(f"\nErrores ({len(errors)}):")
        for e in errors:
            print(f"  ❌ {e}")
    if warnings:
        print(f"\nAdvertencias ({len(warnings)}):")
        for w in warnings:
            print(f"  ⚠️  {w}")

    return 1 if errors else 0


def _aplicar_fixes(path: Path, data: Dict, errors: List[str]) -> int:
    """Intenta corregir errores automáticamente y guarda el archivo."""
    fixes_aplicados = 0
    for h in data.get("findings", []):
        if not isinstance(h, dict):
            continue
        s = h.get("severity")
        if isinstance(s, (int, float)) and (s < 0 or s > 4):
            h["severity"] = max(0, min(4, int(s)))
            fixes_aplicados += 1
        effort = h.get("effort")
        if effort and effort not in EFFORT_VALIDO:
            mapping = {"bajo": "Pequeño", "alta": "Grande", "pequeño": "Pequeño",
                       "medio": "Medio", "grande": "Grande", "baja": "Pequeño",
                       "alta": "Grande", "1": "Pequeño", "2": "Medio", "3": "Grande"}
            corregido = mapping.get(str(effort).strip().lower())
            if corregido:
                h["effort"] = corregido
                fixes_aplicados += 1

    if fixes_aplicados:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Se aplicaron {fixes_aplicados} correcciones automáticas en {path}")

    return _revalidar(path)


def _revalidar(path: Path) -> int:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return 0 if "findings" in data else 1


def main() -> int:
    import argparse
    parser = argparse.ArgumentParser(
        description="Validador de esquema para hallazgos de evaluación heurística"
    )
    parser.add_argument("input", help="Archivo JSON con hallazgos")
    parser.add_argument("--strict", action="store_true",
                        help="Exigir todos los campos opcionales")
    parser.add_argument("--fix", action="store_true",
                        help="Corregir errores menores automáticamente")
    args = parser.parse_args()

    return validar(args.input, strict=args.strict, fix=args.fix)


if __name__ == "__main__":
    sys.exit(main())
