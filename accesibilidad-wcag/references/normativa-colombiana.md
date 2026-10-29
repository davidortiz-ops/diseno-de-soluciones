# Marco normativo colombiano de accesibilidad digital

Mapeo entre la normativa colombiana aplicable, las pautas WCAG 2.2 y las
obligaciones concretas para entidades de **banca** y **retail**.

> ⚠️ **Verificar vigencia:** la normativa puede actualizarse. Confirme la
> versión vigente de cada norma en las fuentes oficiales antes de citarla
> en un informe formal o declaración de conformidad.

## Tabla de mapeo normativo

| Norma | Año | Qué exige | A quién aplica | SC WCAG relacionados | Penalización |
|---|---|---|---|---|---|
| Ley 1346 | 2009 | Ratifica la Convención de la ONU sobre los Derechos de las Personas con Discapacidad; reconoce el acceso a la información y las TIC como derecho | Todas las entidades (públicas y privadas) | Todos | Acción de tutela; responsabilidad del Estado |
| Ley 1680 | 2013 | Garantiza a las personas ciegas y con baja visión el acceso a la información, las comunicaciones y las TIC | Estado y particulares que prestan servicios | 1.1.1, 1.2.x, 1.4.x, 4.1.x | Multas SIC; acciones de protección |
| Ley 1618 | 2013 | Establece disposiciones para garantizar el pleno ejercicio de los derechos de las personas con discapacidad, incluida la accesibilidad | Todas las entidades | Todos | Acción popular; vigilancia de la Procuraduría |
| Res. 1519 (MinTIC) | 2020 | Directiva de accesibilidad web (Anexo 1): adopta WCAG 2.1 nivel AA y la NTC 5854 como estándar para sujetos obligados de la Ley 1712 | Entidades públicas y particulares que ejercen funciones públicas o manejan recursos públicos | Todos los AA | Hallazgos de control; responsabilidad disciplinaria |
| Res. 1239 (MinTIC) | 2022 | Estándar de accesibilidad web para sitios del Estado (basado en WCAG / NTC 5854), nivel AA | Entidades públicas y quienes manejan recursos públicos | Todos los AA | Hallazgos de control interno; responsabilidad disciplinaria |
| Circular Externa SFC | 2022 | Exige que los canales digitales de entidades vigiladas sean accesibles e inclusivos (contraste, formularios, compatibilidad con AT) | Entidades vigiladas por la Superintendencia Financiera | 1.4.3, 1.4.11, 3.3.x, 4.1.2, 4.1.3 | Multas SFC; medidas administrativas |
| Ley 1328 — Consumidor financiero | 2009 | Régimen de protección al consumidor financiero: deber de información clara y debida atención (una barrera de accesibilidad puede vulnerarlo) | Entidades vigiladas SFC | 1.3.x, 1.4.x, 3.3.x | Medidas SFC; reclamaciones |
| Ley 1480 — Estatuto del Consumidor | 2011 | Derecho a información clara, veraz y suficiente en comercio, incluido el electrónico | Productores, proveedores y plataformas de e-commerce | 1.3.x, 1.4.x, 3.3.x | Multas SIC; efectividad de la garantía |
| Circular Única SIC / Res. asociadas | 2023 | Reglas de protección al consumidor en comercio electrónico, incluida la disponibilidad y claridad de la información | Plataformas y retailers de comercio electrónico | 2.4.x, 3.2.x, 3.3.x, 4.1.x | Sanciones SIC |
| NTC 5854 (Icontec) | 2011 | Norma técnica colombiana de accesibilidad web alineada con WCAG | Referente técnico para sector público y privado | Todos | Referente de cumplimiento (no sancionatoria por sí sola) |

> **SMMLV:** las multas suelen expresarse en Salarios Mínimos Mensuales
> Legales Vigentes. Verifique el valor del SMMLV del año en curso para
> estimar montos en el reporte ejecutivo.

> **Matiz "sujeto obligado" (no exagerar el riesgo):** las Resoluciones
> MinTIC 1519/2020 y 1239/2022 obligan **directamente** a entidades
> públicas y a particulares que ejercen funciones públicas o manejan
> recursos públicos (Ley 1712). Un **retail privado** normalmente **no es
> sujeto obligado directo** de esas resoluciones; su exposición real viene
> por la vía del **consumidor (SIC / Ley 1480)** y por **acción de tutela**
> (derechos a la igualdad y al acceso, Leyes 1346/1618/1680). Aun así,
> WCAG/NTC 5854 son el estándar probatorio de referencia, y la
> obligatoriedad directa aparece si la empresa **contrata con el Estado**.
> Refleja este matiz al estimar el riesgo legal en el reporte para no
> sobredimensionarlo.

## Cómo cada norma impacta el desarrollo de software

- **Ley 1346 / 1618 (marco de derechos):** convierten la accesibilidad en
  una obligación de derechos humanos, no solo una buena práctica. Un
  incumplimiento puede derivar en acción de tutela, que es de trámite
  rápido y prioritario. Impacto: la accesibilidad debe tratarse como
  requisito funcional, no como "nice to have".

- **Ley 1680 (acceso para personas ciegas):** obliga a que el contenido
  sea consumible por lectores de pantalla. Impacto directo en: texto
  alternativo (1.1.1), estructura semántica (1.3.1), nombre/rol/valor
  (4.1.2). Todo formulario y tabla deben ser navegables con AT.

- **Resolución 1239 de MinTIC (sector público):** fija nivel **AA** como
  obligatorio para sitios del Estado. Si la entidad financiera o retail
  presta servicios al Estado o maneja recursos públicos, aplica. Impacto:
  define el listón mínimo de conformidad (AA) para el alcance.

- **Circular Externa SFC (banca):** las entidades vigiladas deben
  asegurar canales digitales accesibles. Impacto en banca digital:
  contraste (1.4.3/1.4.11), formularios con errores claros (3.3.x),
  componentes con nombre accesible (4.1.2) y anuncios de estado (4.1.3)
  en operaciones como transferencias y consultas.

- **Ley 1480 — Estatuto del Consumidor (retail):** exige información
  clara y suficiente. Impacto en e-commerce: relaciones e instrucciones
  (1.3.x), contraste de precios y condiciones (1.4.x), identificación y
  prevención de errores en el checkout (3.3.x).

- **Circular Única SIC (comercio electrónico):** refuerza la claridad de
  la información y la navegación. Impacto: navegación consistente
  (3.2.x), nombre/rol/valor de filtros y controles (4.1.x), títulos y
  enlaces descriptivos en el flujo de compra (2.4.x).

## Recomendación de nivel objetivo

| Industria | Nivel mínimo recomendado | Justificación |
|---|---|---|
| Banca (entidad vigilada SFC) | **AA**, con AAA en flujos críticos | Circular SFC + marco de derechos; flujos transaccionales sensibles |
| Retail / e-commerce | **AA** | Estatuto del Consumidor + reglas SIC de comercio electrónico |
| Servicios al Estado | **AA** (obligatorio) | Resolución 1239 de MinTIC |

## Enlaces a textos oficiales

- Ley 1346 de 2009 — `https://www.suin-juriscol.gov.co/`
- Ley 1680 de 2013 — `https://www.suin-juriscol.gov.co/`
- Ley 1618 de 2013 — `https://www.suin-juriscol.gov.co/`
- Resolución MinTIC sobre accesibilidad web — `https://www.mintic.gov.co/`
- Circulares de la Superintendencia Financiera — `https://www.superfinanciera.gov.co/`
- Ley 1480 de 2011 (Estatuto del Consumidor) — `https://www.sic.gov.co/`
- Circular Única SIC — `https://www.sic.gov.co/`
- NTC 5854 — `https://www.icontec.org/`

> Los buscadores oficiales (SUIN-Juriscol, MinTIC, SFC, SIC) permiten
> confirmar el número, año y vigencia exacta de cada norma citada.
