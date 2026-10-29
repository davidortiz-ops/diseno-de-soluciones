#!/usr/bin/env python3
"""Validador de contratos v0 — corre desde la raíz del repo: python3 scripts/validar_contratos.py"""
import glob, json, re, sys, difflib
from pathlib import Path
try:
    import yaml
except ImportError:
    sys.exit("Falta PyYAML: pip install pyyaml")

TIPOS = {"atomo", "molecula", "organismo", "plantilla", "template"}
ALLOW_PX = ("columnas", "tamano", "padding", "celda", "gap", "estructura", "margin")

def aplanar_tokens(path):
    data = json.load(open(path))
    flat = set()
    def walk(d, p):
        if isinstance(d, dict):
            if "$value" in d: flat.add("-".join(p))
            else:
                for k, v in d.items():
                    if not k.startswith(("_", "$")): walk(v, p + [k])
    for g, c in data.items():
        if not g.startswith("_"): walk(c, [])
    return flat

def extraer_tokens_usados(doc):
    usados = set()
    def rec(d, en_tokens=False):
        if isinstance(d, dict):
            for k, v in d.items():
                dentro = en_tokens or k in ("tokens_que_usa", "colores", "comun")
                if dentro and isinstance(v, str):
                    for t in v.split():
                        if re.fullmatch(r"[a-z][a-z0-9-]+", t) and t not in ("transparent","none","ninguna","ninguno","izquierda","true","false","si","no","mono","body"):
                            usados.add(t)
                rec(v, dentro)
        elif isinstance(d, list):
            for x in d: rec(x, en_tokens)
    rec(doc)
    return usados

def main():
    tokens = aplanar_tokens("tokens/tokens.json")
    crudos = glob.glob("**/*.contract.yaml", recursive=True) + glob.glob("**/*.template.yaml", recursive=True)
    archivos = sorted(f for f in crudos if "_ejemplos" not in Path(f).parts)
    fallas = 0
    for f in archivos:
        errores, avisos = [], []
        texto = open(f).read()
        try:
            doc = yaml.safe_load(texto)
        except yaml.YAMLError as e:
            print(f"FALLA {f}: YAML inválido -> {e}"); fallas += 1; continue
        for clave in ("component_id", "intencion", "tipo"):
            if not doc.get(clave): errores.append(f"falta '{clave}'")
        if doc.get("tipo") and doc["tipo"] not in TIPOS: errores.append(f"tipo inválido: {doc['tipo']}")
        if not doc.get("estados"): avisos.append("sin 'estados'")
        if doc.get("tipo") in ("molecula", "organismo", "plantilla", "template") and not doc.get("usa"):
            avisos.append("sin 'usa' (Regla de Oro: ¿compone por component_id?)")
        # valores a mano
        for i, linea in enumerate(texto.splitlines(), 1):
            limpia = linea.split("#")[0]
            if re.search(r"#[0-9A-Fa-f]{3,8}\b", linea.split("#",1)[0] + ("#"+linea.split("#",2)[1] if linea.count("#")>1 else "")):
                pass  # hex dentro de comentario se ignora arriba
            if re.search(r"['\"]?#[0-9A-Fa-f]{3,8}", limpia):
                errores.append(f"línea {i}: color a mano")
            if re.search(r"\b\d+px\b", limpia) and not any(a in limpia for a in ALLOW_PX):
                avisos.append(f"línea {i}: px a mano ({limpia.strip()[:50]})")
        # tokens existentes
        for t in sorted(extraer_tokens_usados(doc)):
            if t not in tokens:
                sug = difflib.get_close_matches(t, tokens, n=1)
                errores.append(f"token inexistente '{t}'" + (f" (¿quisiste decir '{sug[0]}'?)" if sug else ""))
        if errores:
            fallas += 1
            print(f"FALLA {f}:")
            for e in errores: print(f"   - {e}")
        else:
            print(f"PASA  {f}" + (f"  ({len(avisos)} avisos)" if avisos else ""))
        for a in avisos: print(f"   ! {a}")
    print(f"\n{'CORREGIR: ' + str(fallas) + ' contrato(s) con fallas' if fallas else 'LISTO PARA GENERAR: todos los contratos pasan'}")
    sys.exit(1 if fallas else 0)

if __name__ == "__main__":
    main()
