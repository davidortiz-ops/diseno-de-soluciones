# Tokens: cómo leer el JSON que sube el usuario

La skill no trae tokens. Cada sesión se ancla al JSON que sube el usuario en el Paso 0. El archivo puede llamarse como sea; la recomendación oficial al usuario es **`tokens.json`** o **`tokens-extraidos.json`**. Dentro del paquete de proyecto siempre se guarda como `tokens/tokens-extraidos.json`.

## Formatos aceptados

Aceptar cualquier JSON del que se puedan extraer nombres de token. Los tres más comunes:

**1. Plano (nombre → valor):**
```json
{ "control-h-md": "42px", "text-body": "15px", "surface-primary": "#FFFFFF" }
```

**2. Anidado por categoría (Figma Tokens / Style Dictionary):** el nombre del token es la ruta unida por guiones o puntos:
```json
{ "color": { "surface": { "primary": { "value": "#FFFFFF" } } } }
→ token: color-surface-primary (o color.surface.primary)
```
Detectar cuál convención de unión usa el sistema mirando cómo referencian tokens en contratos o código existente; si no hay pista, usar guiones y decirlo.

**3. Lista de objetos:**
```json
[ { "name": "text-body", "value": "15px", "type": "fontSize" } ]
```

## Al recibirlo

1. Extraer la lista completa de nombres válidos. Esa lista es el universo cerrado de la sesión.
2. Resumir al usuario en 2-3 líneas: cuántos tokens, qué categorías (color, tipografía, espaciado, tamaños de control, radios, sombras), y 3-4 nombres de ejemplo — para que confirme que subió el archivo correcto.
3. Si el JSON no parece de tokens (es config de otra cosa, está vacío, es un export de datos), decirlo y pedir el correcto.
4. Si faltan categorías que los contratos van a necesitar (ej: no hay tokens de tamaño de control y la pieza es un campo), avisar desde el Paso 0, no al fallar la validación.

## Durante compilación y validación

- Con formato anidado tipo Design Tokens ($value/$type), el nombre del token es la ruta SIN el grupo raíz cuando así lo usan los contratos reales (ej: `semanticos.surface-inset` → `surface-inset`, `primitivos_escala.control-h.md` → `control-h-md`). Confirmar la convención contra los ejemplos canónicos.
- Compilar usando SOLO nombres presentes en la lista. El token más cercano semánticamente gana; si ninguno encaja, preguntar o anotar `# NOTA: no existe token para X; usar el más cercano Y`.
- Validación punto 4: estricta. Token ausente de la lista → FALLA con el nombre exacto y, si existe, la sugerencia más parecida ("`feedback-danger` no existe; ¿quisiste decir `color-danger`?").
- Nunca aceptar que el usuario "agregue" un token en la conversación: los tokens se cambian en el sistema de diseño y se re-sube el JSON. Anotar la propuesta como advertencia para el dueño del sistema.

## Sin tokens (excepción)

Si el usuario decide avanzar sin subir el JSON: compilar con nombres plausibles marcados `# por verificar`, punto 4 en PENDIENTE, y advertir que el contrato no garantiza consistencia entre IAs hasta validarse contra tokens reales. No armar paquete de proyecto sin tokens.
