#!/usr/bin/env bash
# Instala o actualiza las skills de Diseño de Soluciones en la carpeta actual, sea cual sea su ruta.
# Pregunta cuáles instalar antes de copiar nada.
#
#   curl -fsSL https://raw.githubusercontent.com/davidortiz-ops/diseno-de-soluciones/main/install.sh | bash
#
# DDS_ORIGEN=<carpeta> instala desde una copia local (lo usan las pruebas).
# DDS_SKILLS='1,3' o 'todas' responde la pregunta sin preguntar.
set -euo pipefail

REPO="davidortiz-ops/diseno-de-soluciones"
RAMA="${DDS_RAMA:-main}"

CARPETAS=(
  accesibilidad-wcag
  auditoria-de-flujos
  consultor-madurez-design-systems
  contratos-de-diseno
  designsystem-creator
  evaluacion-heuristica
  proto-persona-banca-top-tier
  tognazzini-revision-heuristica-creditos-vivienda
)
TEXTOS=(
  "Accesibilidad WCAG 2.2: audita sitios web contra los 87 criterios WCAG."
  "Auditoría de flujos: confronta un flujo diseñado con la investigación de usuario."
  "Consultor de madurez de Design Systems: diagnóstico y hoja de ruta."
  "Contratos de diseño: piezas de UI como contratos YAML contra tus tokens."
  "Designsystem-creator: arranca un sistema de diseño nuevo desde una plantilla."
  "Heuristy: evaluación heurística de Nielsen para banca y retail."
  "Proto-persona banca Top Tier: evalúa como cliente de altos ingresos."
  "Tognazzini: experiencia de solicitud de crédito de vivienda."
)

aviso() { printf '%s\n' "$*"; }
falla() { printf 'No se pudo instalar: %s\n' "$*" >&2; exit 1; }

# Con «curl … | bash» la entrada es el propio script: las preguntas se leen de /dev/tty.
INTERACTIVO=0
if [ -z "${DDS_SKILLS:-}" ] && { : </dev/tty; } 2>/dev/null; then INTERACTIVO=1; fi

no_sirve() {  # la carpeta personal o la raíz del disco no son una carpeta de trabajo
  [ "$1" = "$(cd "$HOME" && pwd -P)" ] || [ "$1" = "/" ]
}

DESTINO_REPO="$(pwd -P)"
if no_sirve "$DESTINO_REPO"; then
  [ "$INTERACTIVO" = 1 ] || falla "estás en tu carpeta personal. Entra primero a la carpeta donde vas a trabajar y vuelve a ejecutar el comando."
  aviso "Estás en tu carpeta personal, no en una carpeta de trabajo."
  printf '%s' "Escribe la ruta de la carpeta donde vas a trabajar (o arrástrala aquí desde el Finder) y presiona Enter: " > /dev/tty
  IFS= read -r ruta < /dev/tty || falla "no se recibió ninguna carpeta."
  # Al arrastrar, Terminal pone una barra antes de cada espacio y un espacio al final.
  ruta="$(printf '%s' "$ruta" | sed -e 's/[[:space:]]*$//' -e 's/^[[:space:]]*//' -e "s/^['\"]//" -e "s/['\"]\$//" -e 's/\\\(.\)/\1/g')"
  case "$ruta" in "~"|"~/"*) ruta="$HOME${ruta#?}" ;; esac
  [ -n "$ruta" ] || falla "no se recibió ninguna carpeta."
  if [ ! -d "$ruta" ]; then
    printf '%s [S/n] ' "La carpeta $ruta no existe. ¿La creo?" > /dev/tty
    read -r r < /dev/tty || r=n
    case "$r" in n|N|no|NO|No) falla "la carpeta $ruta no existe." ;; esac
    mkdir -p "$ruta" || falla "no se pudo crear $ruta."
  fi
  DESTINO_REPO="$(cd "$ruta" && pwd -P)" || falla "no se pudo entrar a $ruta."
  if no_sirve "$DESTINO_REPO"; then falla "esa es tu carpeta personal: elige o crea una carpeta para tu trabajo."; fi
  cd "$DESTINO_REPO"
fi

# ---- Cuáles instalar
aviso ""
aviso "Skills de Diseño de Soluciones disponibles:"
for i in "${!CARPETAS[@]}"; do
  aviso "  $((i + 1)). ${TEXTOS[$i]}"
done
aviso ""
if [ -n "${DDS_SKILLS:-}" ]; then
  respuesta="$DDS_SKILLS"
else
  [ "$INTERACTIVO" = 1 ] || falla "no hay terminal para preguntar cuáles instalar. Usa DDS_SKILLS='1,3' o DDS_SKILLS=todas."
  printf '%s' "Escribe los números de las que quieres instalar, separados por coma (ej: 1,3,5), o «todas»: " > /dev/tty
  IFS= read -r respuesta < /dev/tty || respuesta=""
fi
respuesta="$(printf '%s' "$respuesta" | tr '[:upper:]' '[:lower:]' | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')"
[ -n "$respuesta" ] || falla "no elegiste ninguna skill."

ELEGIDAS=()
case "$respuesta" in
  todas|todo|t|"*") ELEGIDAS=("${CARPETAS[@]}") ;;
  *)
    for n in $(printf '%s' "$respuesta" | tr ',;' '  '); do
      case "$n" in ''|*[!0-9]*) falla "«$n» no es un número de la lista (del 1 al ${#CARPETAS[@]})." ;; esac
      { [ "$n" -ge 1 ] && [ "$n" -le "${#CARPETAS[@]}" ]; } || falla "«$n» no es un número de la lista (del 1 al ${#CARPETAS[@]})."
      s="${CARPETAS[$((n - 1))]}"
      case " ${ELEGIDAS[*]-} " in *" $s "*) ;; *) ELEGIDAS+=("$s") ;; esac
    done
    ;;
esac

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

if [ -n "${DDS_ORIGEN:-}" ]; then
  ORIGEN="$DDS_ORIGEN"
else
  command -v curl >/dev/null 2>&1 || falla "hace falta curl."
  command -v tar >/dev/null 2>&1 || falla "hace falta tar."
  aviso "Descargando Diseño de Soluciones…"
  mkdir -p "$TMP/repo"
  curl -fsSL "https://codeload.github.com/$REPO/tar.gz/refs/heads/$RAMA" | tar -xz -C "$TMP/repo" \
    || falla "no se pudo descargar de GitHub. Revisa tu conexión."
  ORIGEN="$(find "$TMP/repo" -mindepth 1 -maxdepth 1 -type d | head -1)"
  [ -n "$ORIGEN" ] || falla "la descarga llegó vacía."
fi

SKILLS="$DESTINO_REPO/.claude/skills"
mkdir -p "$SKILLS"
aviso ""
for s in "${ELEGIDAS[@]}"; do
  [ -f "$ORIGEN/$s/SKILL.md" ] || falla "la descarga no trae $s/SKILL.md."
  cp -R "$ORIGEN/$s" "$TMP/$s"
  find "$TMP/$s" -name '__pycache__' -type d -prune -exec rm -rf {} +
  find "$TMP/$s" -name '*.skill' -type f -delete
  if [ -d "$SKILLS/$s" ]; then
    accion="actualizada"
    rm -rf "$SKILLS/$s.anterior"
    mv "$SKILLS/$s" "$SKILLS/$s.anterior"
    mv "$TMP/$s" "$SKILLS/$s"
    rm -rf "$SKILLS/$s.anterior"
  else
    accion="instalada"
    mv "$TMP/$s" "$SKILLS/$s"
  fi
  aviso "  OK  $s $accion"
done

aviso ""
aviso "Listo: ${#ELEGIDAS[@]} skill(s) en $SKILLS"

# ---- Los scripts de apoyo de algunas skills usan Python 3.8 o superior
hay_python=0
for c in python3 python; do
  if command -v "$c" >/dev/null 2>&1 && "$c" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 8) else 1)' 2>/dev/null; then
    hay_python=1; break
  fi
done
if [ "$hay_python" = 0 ]; then
  aviso "Ojo: no encontré Python 3.8 o superior. Las skills funcionan igual, pero sus scripts de cálculo y reportes lo necesitan: https://www.python.org/downloads/"
fi

aviso ""
aviso "Siguiente paso: abre Claude Code en tu carpeta y pide lo que necesites (ej: «audita este flujo»):"
aviso "  cd \"$DESTINO_REPO\"; claude"
