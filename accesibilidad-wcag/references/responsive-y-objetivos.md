# Responsive, reflujo y tamaño de objetivos

Patrones para que el contenido funcione en distintos tamaños y modalidades
de entrada. Banca: app y portal multidispositivo. Retail: compra desde
móvil.

SC: 1.3.4, 1.4.4, 1.4.10, 1.4.12, 2.5.5, 2.5.7, 2.5.8.

## Breakpoints mínimos

Soporta al menos tres tamaños: móvil, tableta y escritorio.

```css
/* Mobile-first */
.contenedor { padding: 1rem; }
@media (min-width: 768px)  { /* tableta */ }
@media (min-width: 1024px) { /* escritorio */ }
```

## Reflujo (1.4.10)

A 320 px CSS de ancho (equivalente a zoom 400% en 1280px) el contenido no
debe requerir scroll en **dos** ejes. Excepción: contenido que requiere
disposición bidimensional (tablas grandes, mapas), que puede tener scroll
en un eje.

- Usa layouts fluidos (`flex`, `grid`, `%`, `clamp()`), no anchos fijos en px.
- Evita `overflow:hidden` que corte contenido al hacer zoom.

## Redimensionar texto (1.4.4) y espaciado (1.4.12)

- El texto debe escalar hasta 200% sin pérdida de contenido o función.
- Usa unidades relativas (`rem`, `em`), no `px` fijos para tamaños de fuente.
- El contenido debe soportar overrides de espaciado del usuario:

```css
/* No romper con estos valores impuestos por el usuario */
line-height: 1.5; letter-spacing: 0.12em; word-spacing: 0.16em;
```

## Orientación (1.3.4)

No bloquees el contenido a vertical u horizontal salvo que sea esencial.
La app bancaria y el checkout deben funcionar en ambas orientaciones.

## Tamaño de objetivos táctiles

- **2.5.8 (AA, mínimo):** objetivos de al menos **24×24 px** CSS, o con
  separación suficiente.
- **2.5.5 (AAA, mejorado):** al menos **44×44 px** CSS.

```css
.boton-cantidad, .icono-accion {
  min-width: 44px; min-height: 44px;  /* AAA */
}
```

Banca: botones del teclado numérico, +/- de monto. Retail: +/- de
cantidad, favorito, agregar al carrito.

## Arrastre (2.5.7)

Toda función que use arrastre (sliders de monto, reordenar listas) debe
tener una **alternativa de un solo puntero** (botones, campo de entrada).

```html
<label for="monto-slider">Monto</label>
<input id="monto-slider" type="range" min="0" max="1000000" step="50000">
<input type="number" aria-label="Monto exacto" min="0" max="1000000">
```
