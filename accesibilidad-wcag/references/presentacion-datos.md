# Presentación de datos accesible (con código)

Patrones para tablas, datos tabulares y gráficos. Banca: movimientos,
tasas, extractos. Retail: comparativas de productos, especificaciones.

SC: 1.3.1, 1.4.1, 1.4.3, 1.4.10, 1.4.11, 2.4.6, 4.1.2.

## Tabla de datos accesible

```html
<table>
  <caption>Movimientos de octubre 2025</caption>
  <thead>
    <tr>
      <th scope="col">Fecha</th>
      <th scope="col">Descripción</th>
      <th scope="col">Valor</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">01/10/2025</th>
      <td>Pago nómina</td>
      <td>$3.200.000</td>
    </tr>
  </tbody>
</table>
```

**Reglas:**
- `<caption>` describe la tabla.
- `<th scope="col">` para encabezados de columna; `scope="row"` para el
  encabezado de cada fila.
- No uses tablas para maquetar; solo para datos tabulares.
- Para tablas complejas (multinivel), usa `id` + `headers`.

## Tabla ordenable (sortable)

SC 4.1.2: comunica el estado de orden.

```html
<th scope="col" aria-sort="ascending">
  <button>Valor</button>
</th>
```

`aria-sort` toma `ascending`, `descending` o `none`. El botón dentro del
`<th>` dispara el reordenamiento y es operable por teclado.

## Tablas responsive (reflujo)

SC 1.4.10: a 320px no debe haber scroll en dos ejes. Opciones:
- Permitir scroll horizontal **solo** de la tabla dentro de un contenedor
  con `overflow-x:auto` y `tabindex="0"` (para que sea enfocable) y un
  `aria-label`.
- O transformar filas en tarjetas apiladas en móvil (manteniendo la
  asociación dato↔encabezado con `data-label` o markup ARIA).

```html
<div role="region" aria-label="Tabla de movimientos" tabindex="0"
     style="overflow-x:auto">
  <table>…</table>
</div>
```

## Gráficos y visualizaciones

SC 1.1.1, 1.4.1, 1.4.11. Banca: gráfico de rentabilidad. Retail: gráfico
de precios.

- Proporciona una **alternativa textual** (resumen o tabla de datos
  equivalente).
- No transmitas información **solo por color** (1.4.1): usa también
  etiquetas, patrones o texto directo.
- Líneas/segmentos con contraste ≥ 3:1 entre sí y con el fondo (1.4.11).

```html
<figure>
  <img src="grafico.png" alt="Rentabilidad del CDT: subió de 3,8% en
       julio a 4,2% en septiembre de 2025.">
  <figcaption>Rentabilidad trimestral del CDT (2025).</figcaption>
</figure>
<details>
  <summary>Ver datos del gráfico</summary>
  <table>…</table>
</details>
```

## Cifras y montos

- Contraste de precios, tasas y saldos ≥ 4.5:1 (ideal 7:1 — 1.4.6).
- No uses imágenes de texto para tasas/precios (1.4.5/1.4.9): usa texto
  real para que escale (1.4.4) y sea seleccionable.
