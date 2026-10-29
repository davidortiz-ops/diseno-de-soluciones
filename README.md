# Diseño de Soluciones

> Chapter de **People Center Design - Pragma**.

Artefactos para la fase de **diseño de soluciones**: evaluación de usabilidad,
accesibilidad, experiencia conductual, madurez de design systems y
especificación de componentes. Incluye skills estructurados (con carpeta,
evals y opcionalmente scripts) y skills planos (archivo único).

---

## Qué tiene

**9 artefactos** organizados en cuatro categorías:

### Skills de usabilidad y accesibilidad

| Artefacto | Tipo | Versión | ¿Qué problema resuelve? |
|-----------|------|---------|-------------------------|
| **Heuristy — Evaluación Heurística Nielsen** | Skill estructurado | 2.0 | Identifica problemas de usabilidad en interfaces digitales usando las 10 heurísticas de Nielsen + 4 extensiones para banca/retail. Genera score global, matriz de priorización y roadmap. |
| **Accesibilidad Digital WCAG 2.2** | Skill estructurado | 2.0 | Audita sitios web contra los 87 criterios WCAG 2.2 (A, AA, AAA). Detecta barreras de acceso, calcula contraste, verifica lectores de pantalla. Adaptado a normativa colombiana. |
| **Tognazzini — Créditos de Vivienda** | Skill estructurado | 2.0 | Evalúa la experiencia de usuario en solicitudes de crédito de vivienda (canales digitales y presenciales) aplicando las 16 heurísticas de Bruce Tognazzini. Genera Puntuación General, ranking de hallazgos por prioridad y roadmap. |
| **Auditoría de Flujos** | Skill estructurado | — | Audita la trazabilidad entre la investigación de usuario existente (dolores, necesidades, oportunidades) y un flujo ya diseñado en Figma, Miro, Condens o capturas: qué dolores resuelve, cuáles no, qué partes del flujo no tienen sustento, qué huecos tiene la investigación y qué debe probarse con usuario antes de entregar. |

### Skills de especificación de sistemas de diseño

| Artefacto | Tipo | Versión | ¿Qué problema resuelve? |
|-----------|------|---------|-------------------------|
| **Contratos de Diseño** | Skill estructurado | 1.0 | Convierte piezas de UI en contratos YAML validados contra los tokens del sistema de diseño del usuario, y los empaqueta como proyecto portable que cualquier IA interpreta y genera igual. |
| **Designsystem-creator** | Skill estructurado | 1.0 | Bootstrapea un sistema de diseño nuevo clonando una plantilla real con toda la arquitectura de contratos (docs-site, scripts, CI, skills ya instaladas), y si hay Figma o código existente siembra tokens reales y fichas parciales por componente. |

### Skills de evaluación conductual y organizacional

| Artefacto | Tipo | Versión | ¿Qué problema resuelve? |
|-----------|------|---------|-------------------------|
| **Proto-Persona Banca Top Tier** | Skill estructurado | 1.0 | Evalúa experiencias digitales bancarias desde la perspectiva del cliente de altos ingresos. Calcula TTES, genera behavioral insights, se integra con otros skills. |
| **Consultor de Madurez de Design Systems** | Skill plano | 1.0 | Diagnostica el nivel de madurez de un Design System (5 niveles: Located → Opened) y su modelo de gestión/operación (4 pilares). Entrega hoja de ruta MoSCoW. |

### Guías

| Artefacto | ¿Qué problema resuelve? |
|-----------|-------------------------|
| **Lineamientos para Skills** | Estandariza la creación y modificación de skills dentro del chapter. Define estructura de directorios, frontmatter, scripts, evals y control de versiones. |

---

## Para qué sirve cada uno

| Artefacto | Úsalo cuando |
|-----------|-------------|
| Heuristy | Necesites una auditoría rápida de usabilidad antes de un lanzamiento. Quieras priorizar problemas de UX con datos (severidad, impacto, esfuerzo). Trabajes en banca digital o e-commerce y necesites cubrir normativa. |
| Accesibilidad WCAG | Te exijan cumplimiento legal de accesibilidad (Circular SFC, Ley 1618, MinTIC). Quieras certificar nivel A/AA/AAA. Necesites reportes técnicos + ejecutivos + declaración de conformidad. |
| Tognazzini | Estés diseñando o auditando el flujo de crédito de vivienda. Necesites una evaluación centrada en la experiencia del usuario, no solo en la interfaz. |
| Auditoría de Flujos | Vayas a entregar un flujo, blueprint o journey apoyado en investigación previa y no en pruebas con usuarios. Quieras saber si el research (propio o del cliente) responde a lo que diseñaste y qué le falta. |
| Contratos de Diseño | Necesites especificar una pieza de UI para que cualquier IA la genere igual. Quieras estandarizar cómo se documentan los componentes de tu design system contra tokens reales. |
| Designsystem-creator | Vayas a arrancar un sistema de diseño nuevo desde cero. Quieras conectar un Figma nuevo o migrar código existente y organizarlo como sistema de contratos. Necesites el andamiaje completo (docs-site, CI, scripts) sin construirlo a mano. |
| Proto-Persona Top Tier | Quieras validar que tu producto bancario cumple las expectativas del segmento premium. Necesites behavioral insights del cliente de altos ingresos. Quieras reinterpretar hallazgos de otros skills desde la perspectiva Top Tier. |
| Consultor Madurez DS | Necesites diagnosticar el estado actual de tu Design System. Quieras una hoja de ruta para evolucionarlo. Estés en una organización que busca estandarizar su DS. |
| Lineamientos Skills | Vayas a crear un skill nuevo en este chapter. Necesites saber la estructura obligatoria, el formato de frontmatter o los estándares de scripts Python. |

---

## Cómo usarlos

Cada skill opera en **dos modos** que se detectan automáticamente:

### Modo ID (Claude Desktop / Claude.ai)
1. Copia el contenido del `SKILL.md` (o del archivo plano) y pégalo en el chat.
2. Sigue las instrucciones del skill — normalmente comienza pidiendo contexto.
3. El skill evalúa, analiza y entrega el reporte completo dentro de la conversación.
4. No requiere terminal, scripts ni instalación.

### Modo CLI (Claude Code)
1. El skill se activa por palabras clave definidas en su frontmatter.
2. El modelo sigue el workflow documentado en el `SKILL.md`.
3. Además, los scripts Python están disponibles para automatizar cálculos y reportes.
4. Los scripts usan solo biblioteca estándar de Python 3.8+, sin dependencias externas.

### Ejemplos de activación

| Skill | Modo ID (en el chat) | Modo CLI (Claude Code) |
|-------|----------------------|------------------------|
| Heuristy | _"Evalúa heurísticamente el flujo de login de [URL]"_, _"Haz una auditoría UX del checkout de [URL] para retail"_ | `python scripts/calculate_score.py hallazgos.json`, `python scripts/generate_report.py hallazgos.json` |
| Accesibilidad WCAG | _"Audita la accesibilidad de [URL] nivel AA"_, _"Revisa el contraste de color de [URL]"_ | `python scripts/check_contrast.py --foreground #fff --background #000` |
| Tognazzini | _"Evalúa el flujo de solicitud de crédito de vivienda de [URL] usando heurísticas de Tognazzini"_ | `python scripts/calculate_score.py hallazgos.json`, `python scripts/generate_report.py hallazgos.json` |
| Contratos de Diseño | _"Aquí están mis tokens, necesito el contrato de este botón"_, _"Valida este YAML de contrato"_ | No tiene scripts (no requiere cómputo, mismo flujo que en modo ID) |
| Designsystem-creator | _"Móntame un sistema de diseño nuevo desde cero"_, _"Tengo un Figma conectado, organízalo como sistema de contratos"_ | Clona `plantilla/` real en el repo, `npm install`, `python scripts/generar_tokens_css.py`, `python scripts/validar_contratos.py` |
| Proto-Persona Top Tier | _"Evalúa el login de [URL] como cliente Top Tier"_, _"Dame behavioral insights sobre wealth management"_ | `python scripts/calculate_tte_score.py hallazgos.json`, `python scripts/extract_insights.py hallazgos.json` |
| Consultor Madurez DS | _"Necesito un test de madurez de mi Design System"_, _"Diagnostica la gestión y operación de mi DS"_ | No tiene scripts (skill plano) |

---

## Cómo instalarlos

Este repositorio es **público**. Cada skill se instala **por separado**: antes de
instalar, elige cuáles necesitas de esta lista.

| Skill | Nombre para instalar | Archivo para subir |
|-------|----------------------|--------------------|
| Accesibilidad WCAG | `accesibilidad-wcag` | [accesibilidad-wcag.skill](instaladores/accesibilidad-wcag.skill) |
| Auditoría de Flujos | `auditoria-de-flujos` | [auditoria-de-flujos.skill](instaladores/auditoria-de-flujos.skill) |
| Consultor Madurez DS | `consultor-madurez-design-systems` | [consultor-madurez-design-systems.skill](instaladores/consultor-madurez-design-systems.skill) |
| Contratos de Diseño | `contratos-de-diseno` | [contratos-de-diseno.skill](instaladores/contratos-de-diseno.skill) |
| Designsystem-creator | `designsystem-creator` | Solo por la Opción A (ver nota) |
| Heuristy | `evaluacion-heuristica` | [evaluacion-heuristica.skill](instaladores/evaluacion-heuristica.skill) |
| Proto-Persona Top Tier | `proto-persona-banca-top-tier` | [proto-persona-banca-top-tier.skill](instaladores/proto-persona-banca-top-tier.skill) |
| Tognazzini | `tognazzini-creditos-vivienda` | [tognazzini-revision-heuristica-creditos-vivienda.skill](instaladores/tognazzini-revision-heuristica-creditos-vivienda.skill) |

### Opción A — Desde Claude Cowork o Claude Code (catálogo)

El repositorio funciona como catálogo de plugins: lo agregas una vez y desde ahí
eliges qué skills instalar.

**En Claude Cowork:** en la sección de plugins, agrega un catálogo (marketplace)
desde GitHub con la dirección `davidortiz-ops/diseno-de-soluciones`. Aparecen las
8 skills como opciones separadas; instala solo las que elegiste.

**En Claude Code:**

```
/plugin marketplace add davidortiz-ops/diseno-de-soluciones
/plugin install accesibilidad-wcag --marketplace davidortiz-ops/diseno-de-soluciones
/plugin install auditoria-de-flujos --marketplace davidortiz-ops/diseno-de-soluciones
/plugin install consultor-madurez-design-systems --marketplace davidortiz-ops/diseno-de-soluciones
/plugin install contratos-de-diseno --marketplace davidortiz-ops/diseno-de-soluciones
/plugin install designsystem-creator --marketplace davidortiz-ops/diseno-de-soluciones
/plugin install evaluacion-heuristica --marketplace davidortiz-ops/diseno-de-soluciones
/plugin install proto-persona-banca-top-tier --marketplace davidortiz-ops/diseno-de-soluciones
/plugin install tognazzini-creditos-vivienda --marketplace davidortiz-ops/diseno-de-soluciones
```

Ejecuta solo las líneas `/plugin install` de las skills que elegiste. También
puedes escribir `/plugin`, entrar al catálogo y marcarlas en la lista.

### Opción B — Subir el archivo en la app de Claude (Claude.ai / Desktop)

1. Descarga de la carpeta [`instaladores/`](instaladores/) el archivo `.skill` de cada skill que elegiste.
2. En Claude, ve a **Configuración → Capacidades → Skills** y usa **Subir skill**.
3. Sube un archivo por skill. Repite con cada una que quieras.

> **Nota:** Designsystem-creator no tiene archivo `.skill` porque trae dentro una
> plantilla con otras dos skills, y la app de Claude rechaza paquetes con más de
> una. Instálala por la Opción A.

---

## Estructura del chapter

```
diseno-de-soluciones/
├── accesibilidad-wcag/                          # Skill estructurado
│   ├── SKILL.md                                 # Lógica principal
│   ├── README.md                                # Documentación
│   ├── LICENSE                                  # Licencia Pragma
│   ├── evals/evals.json                         # Pruebas de calidad
│   ├── references/                              # 14 referencias
│   │   ├── checklist-wcag-22.md                 # 87 criterios WCAG 2.2
│   │   ├── calculo-contraste-manual.md          # Fórmula de contraste
│   │   ├── normativa-colombiana.md              # Leyes Colombia
│   │   ├── protocolo-lectores-pantalla.md       # NVDA, JAWS, VoiceOver
│   │   ├── patrones-*.md                        # 7 guías de remediación
│   │   ├── seguridad-accesible.md               # Auth, timeouts
│   │   ├── metodologia-evaluacion.md            # Paso a paso auditoría
│   │   ├── priorizacion-remediacion.md          # Matriz severidad × esfuerzo
│   │   ├── presentacion-datos.md               # Tablas, gráficos
│   │   ├── responsive-y-objetivos.md           # Zoom, reflujo
│   │   └── verticales/                          # banca.md, retail.md
│   ├── scripts/                                 # 3 scripts CLI
│   └── templates/                               # 3 plantillas de reporte
│
├── evaluacion-heuristica/                       # Skill estructurado
│   ├── SKILL.md                                 # Lógica principal
│   ├── README.md                                # Documentación
│   ├── LICENSE                                  # Licencia Pragma
│   ├── evals/evals.json                         # Pruebas de calidad
│   ├── references/                              # 4 referencias
│   │   ├── banking-heuristics.md                # H11-H14 banca
│   │   ├── retail-heuristics.md                 # H11-H14 retail
│   │   ├── severity-examples.md                 # Ejemplos por industria
│   │   └── report-templates.md                  # Plantillas
│   └── scripts/                                 # 4 scripts + 2 plantillas JSON
│
├── proto-persona-banca-top-tier/                # Skill estructurado
│   ├── SKILL.md                                 # Lógica principal
│   ├── README.md                                # Perfil fundacional
│   ├── LICENSE                                  # Licencia Pragma
│   ├── evals/evals.json                         # Pruebas de calidad
│   └── scripts/                                 # 3 scripts + 2 plantillas JSON
│
├── tognazzini-revision-heuristica-creditos-vivienda/  # Skill estructurado
│   ├── SKILL.md                                 # Lógica principal
│   ├── README.md                                # Documentación
│   ├── LICENSE                                  # Licencia Pragma
│   ├── evals/evals.json                         # Pruebas de calidad
│   └── scripts/                                 # 3 scripts + 2 plantillas JSON
│
├── auditoria-de-flujos/                         # Skill estructurado
│   ├── SKILL.md                                 # Lógica principal (7 pasos, 3 aprobaciones)
│   └── references/                              # 4 referencias
│       ├── fuentes.md                           # Verificar Condens, Figma, Miro, capturas
│       ├── juicio.md                            # Grados de evidencia y cinco estados
│       ├── documento.md                         # Plantilla del informe y del brief
│       └── blueprint.md                         # Auditoría de blueprints
│
├── contratos-de-diseno/                         # Skill estructurado (sin scripts)
│   ├── SKILL.md                                 # Lógica principal (tokens → ficha → compilar → validar)
│   ├── README.md                                # Documentación
│   ├── LICENSE                                  # Licencia Pragma
│   ├── evals/evals.json                         # Pruebas de calidad
│   ├── assets/harness.txt                       # Reglas de pintado del paquete de proyecto
│   ├── references/                              # 8 referencias + 2 contratos canónicos
│   │   ├── tokens.md, ficha.md, esqueleto.md    # Paso 0, 1 y 2
│   │   ├── mapa-semantico.md, ejemplo.md        # Apoyo a compilación
│   │   ├── validacion.md                        # Checklist de 7 puntos
│   │   ├── descomposicion.md, proyecto.md       # Modo página completa y modo paquete
│   │   └── canonico-*.yaml                      # 2 contratos reales de referencia
│   └── contratos-de-diseno.skill                # Paquete .skill del artefacto
│
├── designsystem-creator/                        # Skill estructurado (bootstrap de sistema de diseño nuevo)
│   ├── SKILL.md                                 # Lógica principal (detectar fuente → scaffold → tokens → siembra → verificar)
│   ├── README.md                                # Documentación
│   ├── LICENSE                                  # Licencia Pragma
│   ├── evals/evals.json                         # Pruebas de calidad
│   └── plantilla/                               # Proyecto base que se clona tal cual (docs-site, scripts, CI, skills co-locadas)
│
├── consultor-madurez-design-systems/            # Skill (archivo único en carpeta)
│   └── SKILL.md
├── lineamientos-skills.md                       # Guía de estándares
└── README.md                                    # Este archivo
```

---

## Skills que se complementan

| Combinación | Para qué sirve |
|-------------|---------------|
| Heuristy + Accesibilidad WCAG | Auditoría completa: usabilidad + accesibilidad. Detecta problemas de diseño y barreras de acceso en una misma evaluación. |
| Heuristy / Tognazzini + Proto-Persona Top Tier | El skill base evalúa técnicamente; la proto-persona reinterpreta cada hallazgo desde la perspectiva del cliente premium. Ajusta severidad y prioridad según cómo los experimenta este segmento. |
| Proto-Persona Top Tier + Accesibilidad WCAG | Evalúa la accesibilidad desde la perspectiva de un usuario de altos ingresos con posibles discapacidades o preferencias de accesibilidad. |
| Consultor Madurez DS + Proto-Persona Top Tier | Evalúa si la madurez del Design System soporta adecuadamente las necesidades del segmento premium. |
| Consultor Madurez DS + Contratos de Diseño | Diagnostica la madurez del Design System y, una vez tiene tokens documentados, especifica sus componentes como contratos reutilizables. |
| Designsystem-creator + Contratos de Diseño | El creator monta el terreno (scaffold, tokens, fichas parciales); Contratos de Diseño completa, compila y valida cada ficha sembrada. |
| Consultor Madurez DS + Designsystem-creator | Diagnostica que el Design System no tiene arquitectura de contratos todavía, y el creator la monta desde cero o desde el Figma/código existente. |

---

## Archivos totales en el chapter

| Tipo | Cantidad |
|------|:--------:|
| Skills estructurados (carpeta) | 7 |
| Skills de archivo único (en carpeta) | 1 |
| Guías | 1 |
| **Total artefactos** | **9** |
| Referencias técnicas | 32 |
| Scripts Python / Shell | 15 |
| Plantillas de reporte | 3 |
| Archivos de evaluación (evals) | 6 |
