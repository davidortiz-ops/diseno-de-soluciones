# Patrones de remediación ARIA (con código)

Biblioteca de patrones accesibles para los componentes interactivos más
auditados. Cada patrón incluye **markup**, **interacción por teclado** y
**manejo de foco**, listo para copiar en el campo *Recomendación* de un
hallazgo. Basado en la WAI-ARIA Authoring Practices Guide (APG).

> **Regla previa:** prefiere HTML nativo antes que ARIA. Un `<button>`,
> `<a href>`, `<select>` o `<dialog>` nativo ya trae semántica, foco y
> teclado. ARIA solo se usa cuando no hay equivalente nativo.

## Índice

- [Modal / diálogo](#modal--diálogo)
- [Pestañas (tabs)](#pestañas-tabs)
- [Acordeón](#acordeón)
- [Alertas y toasts (live regions)](#alertas-y-toasts-live-regions)
- [Menú / botón de menú](#menú--botón-de-menú)
- [Combobox / autocompletado](#combobox--autocompletado)
- [Conceptos transversales](#conceptos-transversales)

---

## Modal / diálogo

SC relacionados: 2.1.2 (sin trampa de teclado), 2.4.3 (orden de foco),
4.1.2 (nombre/rol/valor). Banca: modal de OTP. Retail: modal de carrito.

```html
<button id="abrir-dialogo">Confirmar transferencia</button>

<div role="dialog" aria-modal="true" aria-labelledby="titulo-dlg"
     aria-describedby="desc-dlg" hidden>
  <h2 id="titulo-dlg">Confirmar transferencia</h2>
  <p id="desc-dlg">Vas a transferir $250.000 a Juan Pérez.</p>
  <button id="confirmar">Confirmar</button>
  <button id="cancelar">Cancelar</button>
</div>
```

**Teclado y foco:**
- Al abrir: mover el foco al primer elemento interactivo (o al `<h2>` con
  `tabindex="-1"`).
- `Tab` / `Shift+Tab`: el foco queda **atrapado** dentro del diálogo
  (focus trap) mientras está abierto.
- `Esc`: cierra el diálogo.
- Al cerrar: devolver el foco al botón que lo abrió.
- El fondo debe quedar **inerte** (`inert` o `aria-hidden="true"` en el
  resto del documento).

```js
// Focus trap mínimo
function atraparFoco(dialogo) {
  const focuseables = dialogo.querySelectorAll(
    'a[href],button:not([disabled]),input,select,textarea,[tabindex]:not([tabindex="-1"])'
  );
  const primero = focuseables[0];
  const ultimo = focuseables[focuseables.length - 1];
  dialogo.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') cerrar();
    if (e.key !== 'Tab') return;
    if (e.shiftKey && document.activeElement === primero) {
      e.preventDefault(); ultimo.focus();
    } else if (!e.shiftKey && document.activeElement === ultimo) {
      e.preventDefault(); primero.focus();
    }
  });
}
```

> Alternativa nativa: el elemento `<dialog>` con `showModal()` ya aporta
> focus trap, `Esc` e inertización del fondo.

---

## Pestañas (tabs)

SC: 2.1.1, 4.1.2. Banca: secciones de un producto. Retail: descripción /
especificaciones / reseñas.

```html
<div class="tabs">
  <div role="tablist" aria-label="Detalle del producto">
    <button role="tab" id="tab-1" aria-selected="true"
            aria-controls="panel-1">Descripción</button>
    <button role="tab" id="tab-2" aria-selected="false"
            aria-controls="panel-2" tabindex="-1">Reseñas</button>
  </div>
  <div role="tabpanel" id="panel-1" aria-labelledby="tab-1">…</div>
  <div role="tabpanel" id="panel-2" aria-labelledby="tab-2" hidden>…</div>
</div>
```

**Teclado:**
- `Tab`: entra/sale del conjunto de pestañas (solo la activa es tabbable;
  las demás llevan `tabindex="-1"`).
- `Flecha izq/der`: mueve entre pestañas y activa (patrón de selección
  automática) o solo enfoca (selección manual).
- `Home`/`End`: primera/última pestaña.

---

## Acordeón

SC: 2.1.1, 4.1.2. Banca: preguntas frecuentes de un crédito. Retail: FAQ
de envíos.

```html
<h3>
  <button aria-expanded="false" aria-controls="sec-1" id="acc-1">
    ¿Cuál es la tasa de interés?
  </button>
</h3>
<div role="region" id="sec-1" aria-labelledby="acc-1" hidden>
  La tasa efectiva anual es del 18,5%.
</div>
```

**Teclado:** `Enter`/`Espacio` alterna; `aria-expanded` refleja el estado.
El contenido oculto usa `hidden` (no solo `display:none` por CSS sin
estado ARIA).

---

## Alertas y toasts (live regions)

SC: **4.1.3 Mensajes de estado**. Banca: "Transferencia exitosa". Retail:
"Producto agregado al carrito".

```html
<!-- Mensaje no urgente: no interrumpe -->
<div role="status" aria-live="polite" id="estado"></div>

<!-- Mensaje urgente: interrumpe la lectura actual -->
<div role="alert" aria-live="assertive" id="error"></div>
```

```js
// El nodo de la live region debe existir ANTES de inyectar el texto.
document.getElementById('estado').textContent =
  'Transferencia realizada con éxito.';
```

**Reglas:**
- `role="status"` / `aria-live="polite"`: confirmaciones, resultados.
- `role="alert"` / `aria-live="assertive"`: errores que requieren acción
  inmediata.
- No mover el foco al mensaje; la live region lo anuncia sin robar foco.
- El contenedor debe estar presente en el DOM desde el inicio.

---

## Menú / botón de menú

SC: 2.1.1, 4.1.2. Banca: menú de acciones de una cuenta. Retail: menú de
opciones de un producto.

```html
<button aria-haspopup="true" aria-expanded="false" aria-controls="menu-1"
        id="btn-menu">Acciones</button>
<ul role="menu" id="menu-1" aria-labelledby="btn-menu" hidden>
  <li role="menuitem" tabindex="-1">Ver detalle</li>
  <li role="menuitem" tabindex="-1">Descargar certificado</li>
</ul>
```

**Teclado:** `Enter`/`Espacio`/`Flecha abajo` abre; `Flecha arriba/abajo`
navega; `Esc` cierra y devuelve foco al botón; `Home`/`End` extremos.

> No confundir `role="menu"` (menú de aplicación) con un menú de
> navegación de sitio: para navegación usa `<nav>` con `<ul>`/`<a>`.

---

## Combobox / autocompletado

SC: 1.3.5, 4.1.2. Banca: buscador de bancos para PSE. Retail: buscador de
productos con sugerencias.

```html
<label for="busca">Buscar producto</label>
<input id="busca" role="combobox" aria-expanded="false"
       aria-controls="lista" aria-autocomplete="list"
       autocomplete="off">
<ul role="listbox" id="lista" hidden>
  <li role="option" id="op-1">Tenis Nike Air Max</li>
</ul>
```

**Teclado:** `Flecha abajo` abre/recorre opciones; `Enter` selecciona;
`Esc` cierra; el `input` mantiene el foco y `aria-activedescendant`
apunta a la opción resaltada.

---

## Conceptos transversales

- **Nombre accesible (4.1.2):** todo control debe tener nombre por texto
  visible, `aria-label` o `aria-labelledby`. Verifica con 2.5.3 que el
  nombre accesible **contenga** el texto visible.
- **Estados (4.1.2):** refleja estado con `aria-expanded`, `aria-selected`,
  `aria-checked`, `aria-disabled`, `aria-invalid`, `aria-current`.
- **Foco visible (2.4.7, 2.4.11, 2.4.13):** nunca elimines el outline sin
  reemplazarlo por un indicador con contraste ≥ 3:1 y grosor adecuado.
- **`aria-hidden`:** úsalo solo en contenido decorativo; nunca sobre un
  elemento que contenga foco.
- **No anular roles nativos:** evita `role` redundante (`<nav role="navigation">`).
