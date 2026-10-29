#!/usr/bin/env bash
#
# run_pa11y_audit.sh — Auditoría automática de accesibilidad con pa11y.
#
# Ejecuta pa11y (motor HTML_CodeSniffer) contra una URL, un archivo HTML
# local o una lista de URLs, evaluando contra WCAG2A, WCAG2AA o WCAG2AAA.
#
# Requisitos: Node.js (se usa npx para invocar pa11y sin instalación global)
# y Python 3 para serializar el reporte JSON de forma segura.
#
# En Windows: ejecutar desde Git Bash. pa11y descarga Chromium headless.
#
# Uso:
#   ./run_pa11y_audit.sh https://ejemplo.com
#   ./run_pa11y_audit.sh --standard WCAG2AAA https://ejemplo.com
#   ./run_pa11y_audit.sh --urls urls.txt --report reporte.json
#   ./run_pa11y_audit.sh index.html
#
# Códigos de salida: 0 (sin issues), 1 (issues encontrados), 2 (error de setup).

set -uo pipefail

STANDARD="WCAG2AA"
REPORT=""
URLS_FILE=""
TARGET=""

# Esquemas de URL permitidos (evita file:// arbitrario no intencionado).
ALLOWED_SCHEMES="http https file"

uso() {
  grep '^#' "$0" | sed 's/^#//' | sed '1d'
  exit "${1:-0}"
}

# --- Parseo de argumentos ---
while [[ $# -gt 0 ]]; do
  case "$1" in
    --standard) STANDARD="$2"; shift 2 ;;
    --report)   REPORT="$2";   shift 2 ;;
    --urls)     URLS_FILE="$2"; shift 2 ;;
    -h|--help)  uso 0 ;;
    -*)         echo "Opción desconocida: $1" >&2; uso 2 ;;
    *)          TARGET="$1"; shift ;;
  esac
done

# --- Validaciones de setup ---
if ! command -v npx >/dev/null 2>&1; then
  echo "Error: se requiere Node.js/npx. Instala Node 18+." >&2
  exit 2
fi

case "$STANDARD" in
  WCAG2A|WCAG2AA|WCAG2AAA) ;;
  *) echo "Error: --standard debe ser WCAG2A, WCAG2AA o WCAG2AAA." >&2; exit 2 ;;
esac

# Construye la lista de objetivos.
declare -a OBJETIVOS=()
if [[ -n "$URLS_FILE" ]]; then
  if [[ ! -f "$URLS_FILE" ]]; then
    echo "Error: no existe el archivo de URLs: $URLS_FILE" >&2; exit 2
  fi
  while IFS= read -r linea; do
    linea="$(echo "$linea" | tr -d '\r' | xargs)"
    [[ -n "$linea" ]] && OBJETIVOS+=("$linea")
  done < "$URLS_FILE"
elif [[ -n "$TARGET" ]]; then
  OBJETIVOS+=("$TARGET")
else
  echo "Error: indica una URL, un archivo o --urls." >&2; uso 2
fi

# Normaliza archivos locales a file://.
normalizar() {
  local t="$1"
  if [[ "$t" =~ ^https?:// || "$t" =~ ^file:// ]]; then
    echo "$t"
  elif [[ -f "$t" ]]; then
    # Ruta absoluta a file://
    echo "file://$(cd "$(dirname "$t")" && pwd)/$(basename "$t")"
  else
    echo "$t"
  fi
}

# --- Ejecución ---
EXIT_GLOBAL=0
RESULTADOS_JSON="["
PRIMERO=1

echo "Auditoría pa11y — estándar: $STANDARD"
echo "Nota: las herramientas automáticas detectan ~30-40% de los issues."
echo "Complementa siempre con revisión manual (teclado + lector de pantalla)."
echo "------------------------------------------------------------"

for obj in "${OBJETIVOS[@]}"; do
  url="$(normalizar "$obj")"
  esquema="${url%%:*}"
  if ! echo "$ALLOWED_SCHEMES" | grep -qw "$esquema"; then
    echo "⚠️  Esquema no permitido, se omite: $url" >&2
    continue
  fi

  echo ""
  echo "== $url =="
  salida_json="$(npx --yes pa11y --standard "$STANDARD" --reporter json "$url" 2>/dev/null)"
  codigo=$?

  if [[ $codigo -eq 2 || -z "$salida_json" ]]; then
    echo "❌ Error al auditar (¿URL inalcanzable o setup de pa11y?)."
    EXIT_GLOBAL=2
    continue
  fi

  # Conteo legible con Python.
  conteo="$(python3 - "$salida_json" <<'PY'
import json, sys
try:
    data = json.loads(sys.argv[1])
except Exception:
    print("0 0 0"); sys.exit()
err = sum(1 for i in data if i.get("type") == "error")
warn = sum(1 for i in data if i.get("type") == "warning")
notice = sum(1 for i in data if i.get("type") == "notice")
print(f"{err} {warn} {notice}")
PY
)"
  read -r n_err n_warn n_notice <<< "$conteo"
  echo "Errores: $n_err | Advertencias: $n_warn | Avisos: $n_notice"
  [[ "$n_err" -gt 0 ]] && EXIT_GLOBAL=$(( EXIT_GLOBAL == 2 ? 2 : 1 ))

  if [[ -n "$REPORT" ]]; then
    [[ $PRIMERO -eq 0 ]] && RESULTADOS_JSON+=","
    RESULTADOS_JSON+="$(python3 - "$url" "$salida_json" <<'PY'
import json, sys
url, raw = sys.argv[1], sys.argv[2]
try:
    issues = json.loads(raw)
except Exception:
    issues = []
print(json.dumps({"url": url, "issues": issues}, ensure_ascii=False))
PY
)"
    PRIMERO=0
  fi
done

RESULTADOS_JSON+="]"

if [[ -n "$REPORT" ]]; then
  echo "$RESULTADOS_JSON" > "$REPORT"
  echo ""
  echo "Reporte JSON generado: $REPORT"
fi

echo ""
echo "------------------------------------------------------------"
case $EXIT_GLOBAL in
  0) echo "Resultado: sin errores automáticos. Falta revisión manual." ;;
  1) echo "Resultado: se encontraron errores. Revisa el detalle." ;;
  2) echo "Resultado: hubo errores de ejecución en alguna auditoría." ;;
esac
exit $EXIT_GLOBAL
