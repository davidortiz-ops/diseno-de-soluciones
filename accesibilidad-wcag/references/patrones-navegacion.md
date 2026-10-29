# Patrones de navegación accesible (con código)

Patrones de remediación para la navegación, una de las áreas con más
impacto en usuarios de teclado y lectores de pantalla.

SC: 2.4.1, 2.4.2, 2.4.3, 2.4.4, 2.4.5, 2.4.8, 2.4.11, 3.2.3, 3.2.6.

## Skip link (saltar al contenido)

SC 2.4.1. Primer elemento enfocable de la página.

```html
<a href="#contenido" class="skip-link">Saltar al contenido</a>
...
<main id="contenido" tabindex="-1">…</main>
```

```css
.skip-link { position:absolute; left:-9999px; }
.skip-link:focus { left:1rem; top:1rem; position:fixed; z-index:1000; }
```

## Landmarks

SC 1.3.1, 2.4.1. Estructura la página con regiones nativas.

```html
<header>…</header>
<nav aria-label="Principal">…</nav>
<main id="contenido">…</main>
<aside aria-label="Filtros">…</aside>
<footer>…</footer>
```

Si hay varias `<nav>`, distínguelas con `aria-label` ("Principal",
"Migas de pan", "Pie").

## Menú de navegación

```html
<nav aria-label="Principal">
  <ul>
    <li><a href="/cuentas" aria-current="page">Cuentas</a></li>
    <li><a href="/tarjetas">Tarjetas</a></li>
  </ul>
</nav>
```

- Usa `<a href>` reales (no `<div onclick>`).
- Marca la página actual con `aria-current="page"`.
- No uses `role="menu"` para navegación de sitio (eso es para menús de
  aplicación; ver `patrones-remediacion-aria.md`).

## Migas de pan (breadcrumb)

SC 2.4.8. Banca: portal corporativo. Retail: Categoría > Subcategoría >
Producto.

```html
<nav aria-label="Migas de pan">
  <ol>
    <li><a href="/">Inicio</a></li>
    <li><a href="/zapatos">Zapatos</a></li>
    <li><a href="/zapatos/123" aria-current="page">Nike Air Max</a></li>
  </ol>
</nav>
```

## Foco visible y no oculto

SC 2.4.7, 2.4.11, 2.4.13. Las barras fijas (saldo en banca, carrito en
retail) no deben tapar el elemento enfocado.

```css
:focus-visible {
  outline: 3px solid #003d7a;
  outline-offset: 2px;
}
/* Compensar barras fijas para que el foco no quede oculto */
:target, [tabindex="-1"]:focus { scroll-margin-top: 5rem; }
```

## Paginación y "ver más"

- Botones/enlaces con nombre claro ("Página siguiente", no solo ">").
- Al cargar más resultados, anuncia con live region cuántos se agregaron
  (4.1.3).

## Consistencia

SC 3.2.3 (navegación consistente), 3.2.4 (identificación consistente),
3.2.6 (ayuda en ubicación consistente): el menú, los íconos repetidos y el
acceso a ayuda/contacto deben mantenerse en el mismo lugar en todo el sitio.
