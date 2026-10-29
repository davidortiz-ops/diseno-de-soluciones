# Estados de aplicación accesibles (con código)

Patrones para estados de carga, vacío y error en aplicaciones dinámicas
(SPA, contenido asíncrono). Clave para banca (consultas, transacciones) y
retail (búsqueda, carrito, checkout).

SC: 1.4.13, 2.2.1, 3.3.1, 4.1.3.

## Estado de carga (loading)

Anuncia el inicio y fin de la carga con una live region; no dejes al
usuario de AT sin información mientras esperas datos.

```html
<div role="status" aria-live="polite" id="estado-carga"></div>
<div id="resultados" aria-busy="true">…</div>
```

```js
// Inicio
estadoCarga.textContent = 'Cargando movimientos…';
resultados.setAttribute('aria-busy', 'true');
// Fin
estadoCarga.textContent = 'Se cargaron 25 movimientos.';
resultados.setAttribute('aria-busy', 'false');
```

- Usa **skeleton screens** en vez de spinners sin contexto.
- `aria-busy="true"` mientras se actualiza una región.
- Respeta `prefers-reduced-motion` en animaciones de carga (2.3.3).

## Estado vacío (empty state)

No dejes una región vacía sin explicación.

```html
<div role="status">
  <h2>No tienes movimientos este mes</h2>
  <p>Cuando realices una transacción, aparecerá aquí.</p>
</div>
```

Retail: "No encontramos productos para 'xyz'. Prueba con otros términos o
quita filtros."

## Estado de error

SC 3.3.1, 4.1.3. Distingue errores de validación (campo) de errores de
sistema (API).

```html
<div role="alert">
  <h2>No pudimos completar la transferencia</h2>
  <p>Intenta de nuevo en unos minutos. Si persiste, contacta a tu banco.</p>
  <button>Reintentar</button>
</div>
```

- `role="alert"` para errores que requieren atención inmediata.
- Mensaje en lenguaje claro + acción de recuperación.
- No transmitas el error solo con color o ícono rojo (1.4.1).

## Tiempos de espera y sesión

SC 2.2.1, 2.2.6 (crítico en banca):

```html
<div role="alertdialog" aria-labelledby="t-sesion">
  <h2 id="t-sesion">Tu sesión está por expirar</h2>
  <p>Por seguridad, cerraremos la sesión en 2 minutos.</p>
  <button>Continuar conectado</button>
  <button>Cerrar sesión</button>
</div>
```

- Avisa **antes** de expirar y permite extender sin perder datos (2.2.5).
- Reserva de stock en retail: avisa antes de liberar el carrito.

## Notificaciones (toasts)

- No las hagas depender solo de una desaparición automática rápida: deben
  ser perceptibles por AT (4.1.3) y, si son importantes, persistir o ser
  recuperables (2.2.4).
- Anúncialas con `role="status"` (informativas) o `role="alert"` (urgentes).
