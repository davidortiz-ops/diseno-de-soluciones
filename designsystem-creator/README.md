# Designsystem-creator — bootstrap de un sistema de diseño nuevo

Skill que monta el terreno de un sistema de diseño nuevo basado en contratos: clona una plantilla real (`plantilla/`, co-locada en esta skill) con toda la arquitectura reutilizable — docs-site en Astro, scripts de validación y generación de tokens, CI, y las skills `contratos-de-diseno` y `criterio-diseno` ya instaladas — y, si hay una fuente disponible, siembra tokens reales y fichas parciales por componente.

Versión 1.0 · People Center Design · Pragma

---

## ¿Qué hace?

Scaffoldea un proyecto nuevo copiando `plantilla/` tal cual, sin lógica de filtrado ni texto generado — el mismo enfoque que `create-next-app`. Si hay una fuente real disponible (Figma conectado por MCP, o código/ZIP existente), además extrae sus tokens y detecta su inventario de componentes para dejar una FICHA parcial por cada uno, nunca un contrato completo ni inventado. El resultado es siempre un punto de partida verificable: nunca un sistema de diseño terminado.

**Tres entregables:**

- **Proyecto scaffoldeado** — la arquitectura completa (docs-site, scripts, CI, skills) lista para usar, con o sin fuente.
- **Tokens reales** (si hay fuente) — `tokens/tokens.json` extraído tal cual de Figma o del código, nunca inventado.
- **Fichas parciales por componente** (si hay fuente) — una por cada pieza detectada, con `# PENDIENTE` en todo lo que la fuente no revela explícitamente.

---

## ¿Cómo funciona?

El skill sigue un flujo de **cinco fases**:

1. **Fase 0 — Detectar la fuente** — Determina si hay Figma conectado por MCP, código/ZIP existente, o ninguna de las dos, y lo declara antes de seguir.
2. **Fase 1 — Scaffold** — Copia toda `plantilla/` a la raíz del proyecto destino, sin sobrescribir archivos existentes sin avisar, y verifica que `npm install` / `npm run dev` levanten sin error.
3. **Fase 2 — Tokens** — Si hay fuente, extrae los tokens reales tal cual hacia `tokens/tokens.json` (misma forma W3C que trae la plantilla) y genera `tokens.css`. Si no hay fuente, deja el `.ejemplo` y lo advierte.
4. **Fase 3 — Siembra** — Por cada componente que la fuente revele: clasifica su tipo con el árbol de decisión de `contratos-de-diseno`, propone un mapa de clasificación y espera confirmación humana, y crea una FICHA pre-rellenada (nunca un contrato) de abajo hacia arriba (átomos → moléculas → organismos → plantillas). Si la fuente está desordenada o ambigua, primero pasa por el procedimiento de clasificación segura (ver más abajo). Se salta entera si no hay fuente.
5. **Fase 4 — Verificar y entregar** — Corre `validar_contratos.py`, y entrega un reporte de qué se scaffoldeó, qué tokens se cargaron, qué se sembró y qué queda pendiente.

Cuando la fuente (Figma o código) no trae una jerarquía clara, el skill **no clasifica en silencio**: presenta un mapa de `pieza → nivel propuesto + razón + dudas` y espera confirmación antes de crear una sola carpeta. Lo que no se pueda ubicar con confianza va a `_sin-clasificar/`, declarado como pendiente de decisión humana, nunca forzado a un nivel.

---

## ¿Para qué usarlo?

| Rol | Aplicación |
|---|---|
| **Design system owner** | Arrancar un sistema de diseño nuevo con la arquitectura de contratos ya lista, sin construir el andamiaje a mano. |
| **Equipo que migra un Figma o código existente** | Convertir un design system disperso (Figma sin ordenar, o código sin componentizar) en un proyecto con tokens reales y un inventario de componentes clasificado. |
| **Diseñador de producto / UX** | Obtener un punto de partida verificable (docs-site, tokens, fichas) sobre el cual completar contratos con `contratos-de-diseno`. |
| **Ingeniero de frontend** | Recibir el andamiaje de Vite + React + TypeScript con alias de átomos/moléculas/organismos/plantillas ya configurados, sin dependencias de componentes concretos. |
| **Consultor de design systems** | Auditar un Figma o código desordenado y proponer una clasificación átomo/molécula/organismo/plantilla que el humano confirma antes de ejecutar. |

---

## ¿Cómo se usa?

### Claude Code (CLI)

1. Ubícate en el proyecto destino (nuevo o existente) y activa la skill describiendo lo que quieres montar. Ejemplos:
   - _"Móntame un sistema de diseño nuevo desde cero, todavía no tengo Figma ni código"_
   - _"Aquí está el ZIP de nuestro código actual, extrae los componentes y tokens reales"_
   - _"Tengo un Figma conectado, pero los frames no están ordenados por átomos/moléculas"_
2. El skill declara la fuente detectada (Fase 0), clona `plantilla/` en el proyecto, ejecuta `npm install` y los scripts Python de tokens y validación, y verifica que todo levante.
3. Si hay fuente, siembra tokens reales y fichas parciales, presentando el mapa de clasificación antes de crear carpetas.
4. Entrega el reporte final de la Fase 4 con lo scaffoldeado, los tokens cargados, lo sembrado y lo pendiente.

### Claude Desktop / .ai

Sin terminal ni sistema de archivos real, el skill **no puede ejecutar el scaffold**: clonar `plantilla/`, correr `npm install` o los scripts de Python requiere un entorno con archivos y comandos. En este modo, el skill declara la fuente (Fase 0), describe la estructura que se generaría y entrega el contenido de los archivos clave (tokens.json extraído, fichas de componentes) para que el humano los copie a mano en su proyecto.

### Modos de ejecución

| Característica | Modo CLI | Modo ID |
|---|---|---|
| Entorno | Terminal disponible (Claude Code) | Sin terminal (Claude Desktop / .ai) |
| Scaffold de `plantilla/` | Se clona real en el proyecto destino | Se describe la estructura; no se puede crear en disco |
| `npm install` / `npm run dev` | Se ejecutan y se verifica que levanten sin error | No aplica: no hay dónde ejecutarlos |
| Scripts de tokens y validación | Corren de verdad (`generar_tokens_css.py`, `validar_contratos.py`) | No aplica: se describe qué harían |
| Siembra de fichas | Se escriben como archivos reales en `atomos/moleculas/organismos/templates` | Se entrega el contenido de cada ficha en la conversación, para copiar a mano |
| Ideal para | Montar el sistema de diseño directamente en el repositorio | Explorar el plan de scaffold/siembra antes de tener un entorno con terminal |

---

## ¿Cuándo usarlo?

- Al arrancar un sistema de diseño nuevo desde cero, sin arquitectura de contratos todavía.
- Al conectar un Figma nuevo y querer organizarlo como sistema de contratos, con o sin jerarquía clara.
- Al migrar un código existente (componentes sin documentar) hacia un proyecto con tokens reales y fichas clasificadas.
- Al necesitar el andamiaje completo (docs-site, CI, scripts, skills de contratos) sin construirlo pieza por pieza a mano.

No usarla para completar un contrato ya sembrado, ni para compilar o validar uno — eso es trabajo de `contratos-de-diseno`, que este skill ya deja instalada dentro del proyecto nuevo. Tampoco para evaluar heurísticamente una interfaz ya construida — para eso está `criterio-diseno`.

---

## Estructura del proyecto

```
designsystem-creator/
├── SKILL.md                              # Lógica principal (detectar fuente → scaffold → tokens → siembra → verificar)
├── plantilla/                            # Proyecto base que se clona tal cual (co-locado, no se filtra)
│   ├── .claude/skills/
│   │   ├── contratos-de-diseno/          # Skill completa, ya instalada en el proyecto nuevo
│   │   └── criterio-diseno/              # Skill completa, ya instalada en el proyecto nuevo
│   ├── .github/workflows/                # CI: validar-contratos, typecheck
│   ├── docs-site/                        # Proyección documental en Astro
│   ├── scripts/                          # validar_contratos.py, generar_tokens_css.py
│   ├── atomos/ moleculas/ organismos/ templates/   # Vacías, solo .gitkeep
│   ├── tokens/tokens.json.ejemplo        # Estructura W3C de muestra, no real
│   ├── esqueleto-contrato.yaml           # Esqueleto en blanco para copiar a mano
│   ├── _ejemplos/                        # Un contrato de ejemplo por tipo, no activo
│   ├── src/                              # Playground vacío (Vite + React + TS)
│   └── CLAUDE.md, REGLAS-GLOBALES.md, FIGMA-PRUEBAS.md, CODIGO-PRUEBAS.md
├── evals/
│   └── evals.json                        # Pruebas de calidad
├── README.md                             # Este archivo
└── LICENSE                               # Licencia de uso
```

---

## Referencias del skill

| Archivo / carpeta | Contenido | Cuándo se usa |
|---|---|---|
| `plantilla/.claude/skills/contratos-de-diseno/` | Skill completa para compilar y validar contratos | Se copia tal cual en la Fase 1; el humano la usa después del scaffold |
| `plantilla/.claude/skills/criterio-diseno/` | Skill completa de criterio UX/UI | Se copia tal cual en la Fase 1 |
| `plantilla/scripts/generar_tokens_css.py` | Genera `src/estilos/tokens.css` desde `tokens/tokens.json` | Fase 2, tras cargar tokens |
| `plantilla/scripts/validar_contratos.py` | Valida las fichas/contratos sembrados | Fase 4, verificación final |
| `plantilla/tokens/tokens.json.ejemplo` | Estructura W3C de muestra (primitivos + semánticos) | Fase 1, si el destino no trae tokens reales |
| `plantilla/esqueleto-contrato.yaml` | Esqueleto en blanco para llenar a mano | Solo si no se usa el flujo de ficha de `contratos-de-diseno` |
| `plantilla/_ejemplos/` | Un contrato de ejemplo por tipo (átomo, organismo, plantilla) | Referencia de formato, no se instala en `atomos/organismos/templates` |
| `plantilla/docs-site/` | Proyección documental en Astro | Fase 1; descubre contratos automáticamente vía `import.meta.glob` |

---

## Alcances

- Scaffoldea un proyecto nuevo con toda la arquitectura de contratos (docs-site, CI, scripts, skills) clonando `plantilla/` tal cual, sin lógica de filtrado.
- Si hay Figma conectado por MCP o código/ZIP existente, extrae tokens reales y siembra una FICHA parcial por componente detectado — nunca un contrato completo ni inventado.
- Clasifica cada componente (átomo/molécula/organismo/plantilla) con el árbol de decisión de `contratos-de-diseno`, y ante una fuente desordenada presenta un mapa de clasificación propuesto que el humano confirma antes de crear carpetas.
- Siembra de abajo hacia arriba (átomos antes que sus contenedores), y marca explícitamente con `# PENDIENTE` todo lo que la fuente no revela.
- Deja `contratos-de-diseno` y `criterio-diseno` ya instaladas dentro del proyecto nuevo, listas para completar y validar los contratos sembrados.

## Limitaciones

- Solo el modo CLI (Claude Code) puede ejecutar el scaffold real: clonar `plantilla/`, correr `npm install` y los scripts de Python requiere sistema de archivos y terminal. En modo ID, la skill describe el plan pero no crea el proyecto.
- No genera contratos completos ni listos para producción: el resultado de la Fase 3 son fichas parciales, que se completan con el flujo ficha → compilar → validar de `contratos-de-diseno`.
- La calidad de la siembra depende de la fidelidad de la fuente (Figma o código); una fuente pobre o inconsistente produce más piezas en `_sin-clasificar/` y más `# PENDIENTE` en las fichas.
- No decide la clasificación de tipo por cuenta propia cuando depende de comportamiento no visible en Figma: siempre pregunta antes de asumir.
- No sobrescribe archivos existentes en el destino sin avisar; si el proyecto destino ya tiene `package.json`, `CLAUDE.md`, etc., el humano decide cómo resolver cada choque.

---

## Licencia

Propiedad de **Pragma**. Uso interno y confidencial — ver `LICENSE`.
