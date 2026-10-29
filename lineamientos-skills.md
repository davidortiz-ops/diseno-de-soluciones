# Lineamientos para Skills de Diseño de Soluciones

Estándares obligatorios para crear, modificar o evaluar skills dentro del chapter **People Center Design — Pragma**.

---

## 1. Estructura de directorio

```
nombre-del-skill/
├── SKILL.md          # Lógica principal (requerido)
├── README.md          # Documentación (requerido)
├── LICENSE            # Licencia Pragma (requerido)
├── evals/
│   └── evals.json     # Pruebas de calidad (requerido)
├── references/        # Documentos de consulta (opcional)
└── scripts/           # Scripts CLI (opcional, solo si aplica)
```

### Reglas

- Todo skill **debe** tener `SKILL.md`, `README.md` y `LICENSE` en la raíz.
- El nombre del directorio usa **kebab-case** y coincide con el `name` del frontmatter.
- No dejar archivos residuales (workspaces de prueba, `.pyc`, etc.).
- `references/` solo si hay documentación complementaria que supere las 500 líneas del SKILL.md.
- `scripts/` solo si el skill tiene modo CLI y los scripts son obligatorios en ese modo.
- `evals/` con `evals.json` siguiendo el schema de skill-creator.

---

## 2. Frontmatter de SKILL.md

```yaml
---
name: nombre-del-skill
description: >
  Descripción clara de qué hace el skill, cuándo usarlo y qué
  palabras del usuario deben activarlo. Incluir sinónimos, contextos
  y variaciones. Ser explícito: "Úsalo SIEMPRE que el usuario mencione...".
  Mínimo 2 párrafos, máximo ~150 palabras.
license: Proprietary — Pragma (uso interno y confidencial)
metadata:
  version: "X.Y"
  author: Pragma
---
```

### Reglas

- `name` en kebab-case, sin espacios, sin mayúsculas.
- `description` en bloque YAML (`>`) de máximo 150 palabras. Debe incluir:
  - Qué hace el skill (1 frase).
  - Cuándo activarlo (lista de términos que el usuario podría decir).
  - Para qué NO usarlo (si aplica).
- `license` siempre: `Proprietary — Pragma (uso interno y confidencial)`.
- `metadata.version` usa semver: `MAJOR.MINOR`. MAJOR cambia con cambios estructurales, MINOR con mejoras incrementales.
- `metadata.author` siempre: `Pragma`.

---

## 3. Estructura de SKILL.md

### Encabezado

```
# Nombre del Skill — Subtítulo
```

Sin emojis en el título. Subtítulo describe industria o especialización.

### Secciones requeridas (en este orden)

| # | Sección | Propósito |
|---|---------|-----------|
| 1 | Cómo usar este skill | Workflow paso a paso que el modelo debe seguir |
| 2 | Preguntas de contexto | Qué preguntar al usuario antes de empezar |
| 3 | Escala/estándar | La escala de medición (severidad, niveles, criterios) |
| 4 | Sistema de puntuación | Fórmula y tabla de interpretación |
| 5 | Criterios de evaluación | Lista detallada de cada criterio/principio con preguntas evaluables |
| 6 | Análisis transversales | Patrones que cruzan múltiples criterios |
| 7 | Matriz de priorización | Cómo clasificar hallazgos (Impacto vs Esfuerzo) |
| 8 | Roadmap | Cómo organizar la implementación en fases |
| 9 | Checklist normativo | Normativa aplicable por industria/país |
| 10 | Restricciones | Lo que SÍ y NO debe hacer el modelo |
| 11 | Scripts CLI | Documentación de scripts (solo si aplica) |
| 12 | Solicitudes sugeridas | Ejemplos de prompts que el usuario puede usar |
| 13 | Referencias externas | URLs, bibliografía |

### Reglas de escritura

- **Modo imperativo**: "Evalúa cada heurística", "Documenta cada hallazgo con".
- **Explicar el porqué**: no solo decir qué hacer, sino por qué es importante.
- **Cada heurística/criterio** debe incluir preguntas evaluables concretas.
- **Lo que SÍ y NO hacer** como tabla o listas separadas.
- **Solicitudes sugeridas**: mínimo 5 ejemplos de prompts realistas.
- **Referencias externas**: solo si son estables y de fuentes autorizadas.
- **Sin emojis en títulos** de secciones. Emojis permitidos en contenido solo si son funcionales (advertencias, señales).
- **Sin JSDoc ni comentarios** en los bloques de código de ejemplos.

---

## 4. README.md

Debe seguir el formato estándar del equipo. Ver `accesibilidad-wcag/README.md` como referencia.

### Secciones requeridas

| Sección | Requerido |
|---------|-----------|
| Título con versión y autor | Sí |
| ¿Qué hace? | Sí |
| ¿Cómo funciona? (workflow) | Sí |
| ¿Para qué usarlo? (tabla por rol) | Sí |
| ¿Cómo se usa? (Desktop vs CLI) | Sí |
| ¿Cuándo usarlo? | Sí |
| Modos de ejecución (tabla comparativa) | Sí |
| Estructura del proyecto | Sí |
| Referencias del skill (tabla archivo→contenido) | Sí |
| Alcances | Sí |
| Limitaciones | Sí |
| Licencia | Sí |

### Reglas

- El README debe ser **autocontenido**: alguien que lo lea debe entender qué hace el skill sin necesidad de abrir el SKILL.md.
- La tabla "Modos de ejecución" debe comparar **CLI** vs **ID** (Desktop / .ai).
- Incluir ejemplos de uso realistas para cada modo.
- No incluir instrucciones técnicas de instalación. El skill no requiere instalación.

---

## 5. LICENSE

Archivo de texto plano con la licencia propietaria de Pragma. Copiar textualmente de `accesibilidad-wcag/LICENSE` o `evaluacion-heuristica/LICENSE`.

```
Copyright (c) 2026 Pragma. Todos los derechos reservados.
...
```

Sin modificaciones. Solo cambiar el nombre del skill en la línea 3.

---

## 6. Scripts (Python)

Solo aplican en modo CLI. Reglas:

- **Python 3.8+** con solo biblioteca estándar. Sin dependencias externas.
- **Encoding**: incluir `sys.stdout.reconfigure(encoding="utf-8")` al inicio para compatibilidad Windows.
- **Argumentos**: usar `argparse` con `--help` descriptivo.
- **Códigos de salida**: 0 (éxito), 1 (error de validación/datos), 2 (error de sistema/lectura).
- **Nombres**: snake_case. Prefijo `validate_`, `generate_`, `calculate_` según función.
- **Cada script** debe poder ejecutarse de forma independiente.
- **Sin archivos temporales** en el directorio del skill. Usar `--output` para definir rutas de salida.
- **Sin prompts interactivos** (no usar `input()`).
- **Docstring** al inicio con: propósito, modo de uso (ejemplos), requisitos.

---

## 7. Referencias (`references/`)

- Los archivos de referencia se cargan bajo demanda desde el SKILL.md.
- Cada archivo debe comenzar con una línea que indique **cuándo leerlo**:
  > "Lee este archivo cuando el contexto sea banca digital..."
- Usar tablas para checklists, comparaciones y ejemplos estructurados.
- Separar secciones con `---`.
- Incluir ejemplos concretos con valores de ejemplo (no plantillas vacías).

---

## 8. evals.json

Sigue el schema de skill-creator. Ver `references/schemas.md` del skill-creator para el formato exacto.

```json
{
  "skill_name": "nombre-del-skill",
  "evals": [
    {
      "id": 1,
      "prompt": "Prompt realista del usuario",
      "expected_output": "Descripción del resultado esperado",
      "files": [],
      "expectations": [
        "Afirmación verificable sobre el output"
      ]
    }
  ]
}
```

### Reglas

- Mínimo 3 evals cubriendo los casos de uso principales.
- Los prompts deben ser realistas, incluyendo contexto (URL, industria, alcance).
- Cada expectation debe ser verificable objetivamente.
- Los evals deben cubrir: caso principal, caso con extensión/especialización, y caso mínimo/rápido.

---

## 9. Control de versiones

| Cambio | Versión |
|--------|---------|
| Nuevo skill | 1.0 |
| Nuevas heurísticas/criterios | MAJOR+1 |
| Nueva industria/vertical | MAJOR+1 |
| Nuevos scripts | MINOR+1 |
| Nuevas referencias | MINOR+1 |
| Corrección de errores | MINOR+1 |
| Actualización normativa | MINOR+1 |
| Cambios cosméticos (README, typos) | Sin cambio de versión |

---

## 10. Checklist de calidad

Antes de dar por terminado un skill, verificar:

- [ ] `SKILL.md` existe con frontmatter completo
- [ ] `README.md` existe con las 11 secciones requeridas
- [ ] `LICENSE` existe con el texto estándar de Pragma
- [ ] `evals/evals.json` existe con mínimo 3 casos
- [ ] El directorio no contiene archivos residuales (`.pyc`, workspaces, etc.)
- [ ] El skill funciona en Desktop sin scripts (entrega reporte en conversación)
- [ ] El skill funciona en CLI con scripts (comprobar que `python script.py --help` funciona)
- [ ] No hay dependencias externas en los scripts
- [ ] Todos los scripts tienen fix de encoding UTF-8 para Windows
- [ ] El README incluye tabla de modos de ejecución (CLI vs ID)
- [ ] Las referencias indican cuándo leer cada archivo
- [ ] Las solicitudes sugeridas son mínimo 5 y realistas
- [ ] La escala de medición está claramente definida
- [ ] El sistema de puntuación incluye fórmula y tabla de interpretación
- [ ] Cada criterio/heurística tiene preguntas evaluables
- [ ] Se incluyen restricciones (SÍ/NO)

---

## 11. Excepciones

- Skills puramente de referencia (proto-personas, guías) no necesitan `SKILL.md` con frontmatter ni `evals/`. Solo `README.md` con el contenido.
- Skills que no tienen modo CLI no necesitan `scripts/`.
- Skills que caben en un solo archivo no necesitan `references/`.
- Skills experimentales pueden omitir `evals/` temporalmente, pero deben agregarlos antes de la versión 1.0.
