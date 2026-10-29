#!/usr/bin/env python3
"""
validate_findings.py — Validador de esquema para hallazgos de la revisión
heurística de Tognazzini.

Verifica que un archivo JSON de hallazgos cumpla con el esquema esperado por
calculate_score.py y generate_report.py.

Uso:
    python scripts/validate_findings.py hallazgos.json
    python scripts/validate_findings.py hallazgos.json --strict
    python scripts/validate_findings.py hallazgos.json --fix

Modos:
    --strict   Exige que todos los campos opcionales estén presentes
    --fix      Corrige errores menores automáticamente (Gravedad/Dificultad
               fuera de rango, ids duplicados)

Códigos de salida: 0 (válido), 1 (errores encontrados), 2 (error de lectura).
"""

import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List

CAMPOS_OBLIGATORIOS = {"heuristic", "description", "severity", "difficulty", "recommendation"}
CAMPOS_HALLAZGO = {"id", "heuristic", "description", "evidence", "severity",
                   "difficulty", "explanation", "recommendation"}
HEURISTICAS_VALIDAS = {
    "Visibilidad del sistema", "Consistencia", "Minimizar la carga de memoria",
    "Retroalimentación inmediata", "Prevención de errores", "Deshacer / rehacer",
    "Control del usuario", "Facilidad de aprendizaje", "Eficiencia de uso",
    "Diseño estético y minimalista", "Ayuda contextual",
    "Accesibilidad y adaptabilidad", "Claridad en el flujo temporal",
    "Anticipación", "Compatibilidad entre canales", "Satisfacción emocional",
}
PATRON_FECHA = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def validar_hallazgo(h: Dict[str, Any], idx: int, strict: bool,
                     errors: List[str], warnings: List[str]) -> None:
    id_h = h.get("id", idx)

    faltantes = CAMPOS_OBLIGATORIOS - h.keys()
    if faltantes:
        errors.append(f"Hallazgo #{id_h}: faltan campos obligatorios: {', '.join(sorted(faltantes))}")
        return

    for campo in ("severity", "difficulty"):
        valor = h.get(campo)
        if not isinstance(valor, int):
            errors.append(f"Hallazgo #{id_h}: {campo} debe ser entero, se encontró {type(valor).__name__}")
        elif valor < 0 or valor > 3:
            errors.append(f"Hallazgo #{id_h}: {campo}={valor} fuera de rango 0-3")

    heur = h.get("heuristic", "")
    if heur not in HEURISTICAS_VALIDAS:
        warnings.append(f"Hallazgo #{id_h}: heuristic='{heur}' no coincide con ninguna de las 16 heurísticas de Tognazzini")

    if not str(h.get("description", "")).strip():
        errors.append(f"Hallazgo #{id_h}: description está vacía")

    if not str(h.get("recommendation", "")).strip():
        errors.append(f"Hallazgo #{id_h}: recommendation está vacía")

    if strict:
        opcionales_faltan = CAMPOS_HALLAZGO - h.keys()
        if opcionales_faltan:
            warnings.append(f"Hallazgo #{id_h}: faltan campos opcionales: {', '.join(sorted(opcionales_faltan))}")


def validar_contexto(ctx: Dict[str, Any], warnings: List[str]) -> None:
    credit_type = ctx.get("credit_type", "")
    if credit_type and credit_type not in ("convencional", "especial"):
        warnings.append(f"credit_type='{credit_type}' debería ser 'convencional' o 'especial'")

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

    validar_contexto(data.get("context", {}), warnings)

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
    fixes_aplicados = 0
    for h in data.get("findings", []):
        if not isinstance(h, dict):
            continue
        for campo in ("severity", "difficulty"):
            valor = h.get(campo)
            if isinstance(valor, (int, float)) and (valor < 0 or valor > 3):
                h[campo] = max(0, min(3, int(valor)))
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
        description="Validador de esquema para hallazgos de la revisión heurística de Tognazzini"
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
