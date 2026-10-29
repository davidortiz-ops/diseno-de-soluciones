# Patrones de formularios accesibles (con código)

Patrones de remediación para formularios, el componente con más hallazgos
de accesibilidad. Aplica a flujos críticos de banca (login, solicitudes,
transferencias) y retail (checkout, registro).

SC principales: 1.3.1, 1.3.5, 3.3.1, 3.3.2, 3.3.3, 3.3.4, 3.3.7, 3.3.8,
4.1.2, 4.1.3.

## Índice

- [Etiquetado](#etiquetado)
- [Campos requeridos](#campos-requeridos)
- [Agrupación de controles](#agrupación-de-controles)
- [Identificación de propósito (autocomplete)](#identificación-de-propósito-autocomplete)
- [Manejo de errores y validación](#manejo-de-errores-y-validación)
- [Ayuda y sugerencias](#ayuda-y-sugerencias)
- [Confirmación de acciones](#confirmación-de-acciones)
- [Autenticación accesible](#autenticación-accesible)

---

## Etiquetado

Todo control debe tener una etiqueta **programáticamente asociada**.

```html
<!-- Correcto: label explícito con for -->
<label for="monto">Monto a transferir (COP)</label>
<input id="monto" name="monto" type="text" inputmode="numeric">

<!-- Aceptable: aria-label cuando no hay texto visible -->
<input type="search" aria-label="Buscar productos">
```

Evita usar solo `placeholder` como etiqueta: desaparece al escribir y
suele fallar contraste.

---

## Campos requeridos

```html
<label for="cedula">Número de cédula <span aria-hidden="true">*</span></label>
<input id="cedula" required aria-required="true"
       aria-describedby="ayuda-cedula">
<p id="ayuda-cedula">Campo obligatorio. Sin puntos ni espacios.</p>
```

Indica los requeridos con texto o `required`/`aria-required`, no solo con
color o un asterisco sin explicación (1.3.3, 1.4.1).

---

## Agrupación de controles

Usa `<fieldset>` y `<legend>` para grupos de radios/checkboxes
relacionados.

```html
<fieldset>
  <legend>Tipo de cuenta destino</legend>
  <label><input type="radio" name="tipo" value="ahorros"> Ahorros</label>
  <label><input type="radio" name="tipo" value="corriente"> Corriente</label>
</fieldset>
```

Retail: agrupar selección de talla/color; banca: tipo de producto, plazo.

---

## Identificación de propósito (autocomplete)

SC 1.3.5: usa `autocomplete` en campos de datos personales para que el
navegador y la AT los identifiquen.

```html
<input autocomplete="name">            <!-- nombre -->
<input autocomplete="email">           <!-- correo -->
<input autocomplete="tel">             <!-- teléfono -->
<input autocomplete="cc-number">       <!-- número de tarjeta (retail/banca) -->
<input autocomplete="postal-code">     <!-- código postal (envío) -->
```

---

## Manejo de errores y validación

SC 3.3.1 (identificar), 3.3.3 (sugerir), 4.1.3 (anunciar).

```html
<!-- Resumen de errores al inicio del formulario -->
<div role="alert" id="resumen-errores">
  <h2>Hay 2 errores en el formulario</h2>
  <ul>
    <li><a href="#monto">El monto excede tu saldo disponible</a></li>
    <li><a href="#fecha">La fecha debe ser futura</a></li>
  </ul>
</div>

<!-- Error en línea, asociado al campo -->
<label for="monto">Monto a transferir</label>
<input id="monto" aria-invalid="true" aria-describedby="err-monto">
<p id="err-monto" class="error">El monto excede tu saldo disponible.</p>
```

**Reglas:**
- Marca el campo con `aria-invalid="true"`.
- Asocia el mensaje con `aria-describedby`.
- El mensaje describe el problema **y** sugiere cómo corregir.
- El resumen usa `role="alert"` y enlaza a cada campo con error.
- No identifiques el error solo con color (1.4.1).

Ejemplos de mensajes con sugerencia (3.3.3):
- Banca: "El monto ($300.000) excede tu saldo disponible ($250.000)."
- Retail: "El cupón VERANO ya expiró. Prueba con un cupón vigente."

---

## Ayuda y sugerencias

```html
<label for="nit">NIT</label>
<input id="nit" aria-describedby="ayuda-nit">
<p id="ayuda-nit">Incluye el dígito de verificación, ej: 900123456-7.</p>
```

Coloca la ayuda **antes** de que el usuario cometa el error y asóciala con
`aria-describedby` (3.3.5).

---

## Confirmación de acciones

SC 3.3.4 (prevención de errores en operaciones legales/financieras).

```html
<div role="dialog" aria-modal="true" aria-labelledby="t-conf">
  <h2 id="t-conf">Confirmar pago</h2>
  <p>Vas a pagar $250.000. Esta acción no se puede deshacer.</p>
  <button>Confirmar pago</button>
  <button>Revisar de nuevo</button>
</div>
```

Antes de transferencias, pagos o compras: muestra un **resumen
confirmable y reversible** (ver patrón de modal en
`patrones-remediacion-aria.md`).

---

## Autenticación accesible

SC 3.3.8 (AA) y 3.3.9 (AAA): no exijas pruebas cognitivas en el login.

- **Permite pegar** en los campos de contraseña/OTP (no bloquees `paste`).
- **Compatibilidad con gestores de contraseñas** (`autocomplete="current-password"`).
- Evita CAPTCHA visual sin alternativa; si es imprescindible, ofrece
  alternativa de audio u otra modalidad (también afecta 1.1.1).
- OTP: anuncia con live region cuando el código expira o falla (4.1.3).

```html
<label for="pass">Contraseña</label>
<input id="pass" type="password" autocomplete="current-password">
<!-- No usar onpaste="return false" -->
```
