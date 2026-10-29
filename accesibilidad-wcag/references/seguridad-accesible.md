# Seguridad accesible (con código)

La seguridad y la accesibilidad deben convivir: medidas de seguridad mal
implementadas (CAPTCHA, timeouts, bloqueo de pegar) rompen la
accesibilidad. Especialmente relevante para **banca** (datos sensibles,
SFC) y checkout de **retail**.

SC relacionados: 2.2.1, 2.2.5, 2.2.6, 3.3.4, 3.3.7, 3.3.8, 3.3.9, 1.1.1.

## Autenticación accesible (no romper seguridad ni acceso)

- **Permitir pegar** y gestores de contraseñas (`autocomplete="current-password"`,
  `one-time-code` para OTP). No uses `onpaste="return false"`.
- **Evitar CAPTCHA cognitivo** sin alternativa (3.3.8/3.3.9, 1.1.1). Si es
  imprescindible, ofrece alternativa de audio u otro factor.
- **2FA/OTP:** anuncia expiración y errores con live region (4.1.3); da
  tiempo suficiente o permite reenviar sin penalizar (2.2.1).

```html
<input type="text" inputmode="numeric" autocomplete="one-time-code"
       aria-describedby="ayuda-otp">
<p id="ayuda-otp">Ingresa el código de 6 dígitos enviado a tu celular.</p>
```

## Tiempos de sesión (2.2.1, 2.2.5, 2.2.6)

- Avisa **antes** de cerrar por inactividad y permite extender.
- Al reautenticar, **no pierdas los datos** del flujo en curso (2.2.5).
- Banca: clave en transferencias a medio diligenciar. (Ver patrón en
  `estados-aplicacion.md`.)

## CSRF (protección sin romper accesibilidad)

Incluye tokens CSRF en operaciones que cambian estado (transferir, pagar,
comprar). El token va en campo oculto o cabecera; no afecta la AT.

```html
<form method="post" action="/transferir">
  <input type="hidden" name="csrf_token" value="{{CSRF_TOKEN}}">
  …
</form>
```

## XSS (codificación en salida)

Nunca inyectes entrada del usuario sin codificar; esto también protege la
integridad de los nombres accesibles y live regions.

```js
// Correcto: textContent escapa el contenido
nodo.textContent = nombreUsuario;
// Evitar: innerHTML con datos del usuario
// nodo.innerHTML = nombreUsuario;  // riesgo XSS
```

## Cabeceras de seguridad (CSP)

Una CSP estricta no debe romper el JS que da accesibilidad (focus trap,
live regions). Evita `unsafe-inline` y mueve scripts a archivos con nonce.

```
Content-Security-Policy: default-src 'self';
  script-src 'self' 'nonce-{{NONCE}}'; object-src 'none';
```

## Prevención de errores en operaciones sensibles (3.3.4)

Transacciones financieras y compras deben ser **reversibles, verificables
o confirmadas**: muestra resumen, pide confirmación y permite cancelar
antes de ejecutar. (Ver patrón de confirmación en
`patrones-formularios.md`.)

## Entrada redundante (3.3.7)

No vuelvas a pedir datos ya ingresados en el mismo proceso (p. ej.,
reutiliza la dirección de envío como dirección de facturación con un
checkbox). Reduce errores y carga cognitiva.
