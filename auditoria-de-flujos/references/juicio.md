# El juicio: evidencia, tope y estados

## 1. Antes de auditar el flujo, audita la regla

La investigación es la vara de medir. Si la vara está torcida, el veredicto no vale nada por impecable que sea el análisis. Califica cada dolor antes de usarlo.

### Grado de evidencia

**Alto** — comportamiento observado, con fuente rastreable hasta la cita o el clip, del mismo segmento del flujo, con menos de 12 meses. Típico de Condens con material propio bien sintetizado.

**Medio** — investigación con ficha metodológica clara (método, muestra, fecha, segmento) pero sin acceso al material crudo, o síntesis interna de tu equipo sin las fuentes adjuntas. Típico de un Miro de síntesis o un informe del cliente bien hecho.

**Bajo** — dolor declarado sin método visible, sin fecha, sin muestra; opinión de stakeholder presentada como hallazgo; investigación de otro segmento o de otro producto; más de 18 meses sin revalidar.

### Ejes que degradan el grado

Aplícalos y deja constancia en el informe:

- **Vigencia** — más de 18 meses sin revalidar baja un nivel. Más de 3 años, o un cambio conocido de mercado, regulación o producto en el intervalo, lo baja a bajo.
- **Segmento** — si el segmento investigado no es el del flujo, baja un nivel y decláralo. Si es abiertamente otro público, no lo uses como vara: decláralo como no aplicable.
- **Método** — declarado > inferido > ausente.
- **Muestra** — n muy pequeño no invalida un hallazgo cualitativo, pero sí impide hablar de frecuencia o prevalencia. Nunca conviertas un hallazgo cualitativo en una afirmación de porcentaje.
- **Observado vs. autorreportado** — lo que la gente dice que hace y lo que hace no coinciden. Un dolor autorreportado no puede sostener una afirmación sobre comportamiento futuro.

## 2. Regla de tope (la más importante)

**El veredicto nunca puede ser más fuerte que la evidencia que lo sostiene.**

| Grado del dolor | Lo más fuerte que puedes afirmar |
|---|---|
| Alto | "el flujo responde a este dolor documentado", con la condición de falla declarada |
| Medio | "el flujo es consistente con lo reportado; requiere confirmación en uso real" |
| Bajo | "el flujo es coherente con lo declarado; no hay evidencia suficiente para afirmar que lo resuelve" |

Esto hace que el rigor sea estructural y no dependa de tu buen juicio ese día. Si un dolor es grado bajo, **no existe** un resultado "resuelto" para él, sin importar qué tan bien diseñado esté el paso.

## 3. Los cinco estados

Sin escala explícita todo sale en verde. Para cada dolor, elige uno:

**Elimina** — después del flujo, la condición que causaba el dolor deja de existir. No es que sea más fácil: es que ya no pasa. Ej.: el dolor era volver a digitar datos que el banco ya tiene, y el flujo los precarga desde el core.

**Reduce** — el dolor sigue existiendo pero baja el costo, el tiempo, los pasos o la carga cognitiva. Es el estado más común y el más honesto. Declara **cuánto** y **con base en qué**; si no puedes, es una hipótesis de reducción, no una reducción.

**Traslada** — el dolor no desaparece, cambia de dueño o de momento. Se lo pasa al usuario más adelante, a otro canal, al call center, al backoffice, o a un tercero. Muy frecuente y casi siempre invisible en las presentaciones. Nómbralo siempre que el trabajo se mueva de lugar en vez de desaparecer.

**Decora** — el flujo nombra el dolor en el copy, en un mensaje tranquilizador, en un texto de ayuda o en una ilustración, pero el comportamiento del sistema no cambia. Reconocer el dolor no es resolverlo. Este estado es el antídoto contra el "sí lo cubre" automático.

**Agrava** — el flujo introduce fricción nueva sobre ese dolor o sobre otro. Búscalo activamente: los rediseños suelen resolver un dolor y crear dos. Pasos añadidos, más decisiones, más espera, más requisitos previos, pérdida de una salida que antes existía.

### Obligación de falsación

Por cada **elimina** o **reduce**, escribe:

- **Condición de falla:** la circunstancia bajo la cual deja de ser cierto ("falla si el usuario llega sin haber hecho X", "falla si el dato no está en el core", "falla si el usuario entra desde el canal Y").
- **Señal que lo probaría:** qué se podría observar o medir para saber si funcionó.

Sin estas dos líneas, el estado no se puede escribir en el informe.

## 4. Dirección flujo → dolor

Recorre cada paso y clasifícalo en una de tres canastas:

- **Responde a un dolor** — indica cuál, por identificador.
- **No negociable declarado** — regulatorio, regla de negocio, restricción técnica o decisión del cliente que el diseñador declaró en la reconstrucción. No se cuestiona, se registra.
- **Sin razón conocida** — ni dolor ni no negociable. Es el hallazgo más valioso del ejercicio.

Sobre la tercera canasta, no acuses: pregunta en el informe. La formulación correcta es *"este paso no quedó asociado a ningún dolor ni a ningún no negociable declarado; vale la pena confirmar por qué está antes de construirlo"*. Muchas veces existe una razón que nadie escribió, y el valor está en hacerla explícita. Cuando no la hay, es scope recortable — y donde la velocidad es el activo, recortar vale tanto como cubrir.

## 5. Qué se sustenta y qué necesita usuario

Al final, cada decisión del flujo cae en uno de dos grupos, y esta separación es el corazón del valor de la skill:

**Se sustenta con la investigación existente** — hay un dolor de grado alto o medio, el flujo lo elimina o lo reduce, la condición de falla está controlada, y no depende de un supuesto de comportamiento no observado. Aquí el diseñador puede avanzar sin probar.

**Necesita prueba con usuario** — cae aquí si se cumple cualquiera de estas: el dolor es grado bajo; el estado es traslada, decora o agrava; la evidencia es autorreportada y la decisión depende de comportamiento; el paso quedó sin razón conocida; o el flujo introduce un patrón de interacción sobre el que la investigación no dice nada.

Prioriza esta segunda lista por **costo de equivocarse**, no por facilidad de prueba: primero lo que ya no se puede deshacer una vez construido.
