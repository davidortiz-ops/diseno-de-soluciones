# Guía vertical: Accesibilidad en Retail / E-commerce

Guía específica para auditar productos digitales de comercio (tiendas
online, catálogos, campañas) en el contexto colombiano (Estatuto del
Consumidor y reglas SIC de comercio electrónico).

## Tipos de sitio

- **E-commerce transaccional:** tienda online con carrito y checkout.
- **Landing promocional:** página de campaña u oferta puntual.
- **Catálogo:** vitrina de productos sin compra directa.
- **Blog corporativo:** contenido editorial, guías, reseñas de marca.

## Flujos críticos de accesibilidad

1. **Búsqueda y filtros de producto** — buscador, facetas, ordenamiento.
2. **Galería de imágenes de producto** — zoom, miniaturas, video.
3. **Selección de variantes** — talla, color, cantidad.
4. **Carrito de compras** — agregar, editar, eliminar, resumen.
5. **Checkout** — datos de envío, pago, confirmación.
6. **Reseñas y valoraciones** — leer y enviar opiniones.

## Issues específicos de retail

| Issue | SC WCAG | Por qué importa |
|---|---|---|
| Carruseles de productos sin control de pausa | 2.2.2 | El movimiento distrae y bloquea a usuarios cognitivos/motrices |
| Imágenes de producto sin alt descriptivo | 1.1.1 | El usuario ciego no conoce el producto que compra |
| Contraste insuficiente en badges de descuento y precios | 1.4.3 | Precios y ofertas ilegibles para baja visión |
| Filtros de catálogo sin nombre accesible | 4.1.2 | El usuario con AT no sabe qué filtro activa |
| Checkout multipaso sin indicador de progreso | 2.4.x, 3.3.x | El usuario se pierde en el proceso de compra |
| Selección de variante solo por color (sin texto) | 1.4.1, 1.3.3 | Daltónicos no distinguen la opción elegida |
| Pasarela de pago redirige a tercero no accesible | Conf. Req. 5 | Rompe la conformidad del flujo de compra completo |
| Errores de pago sin sugerencia clara | 3.3.1, 3.3.3 | El usuario abandona sin entender qué falló |
| Objetivos táctiles pequeños (+/- cantidad, favorito) | 2.5.8 | Difíciles de activar con motricidad reducida |

## Checklist rápida retail (10 puntos prioritarios)

1. ¿Las imágenes de producto tienen alt descriptivo (modelo, color, talla)? — 1.1.1
2. ¿Los carruseles tienen botón de pausa y son operables por teclado? — 2.2.2, 2.1.1
3. ¿Los filtros y facetas tienen nombre accesible y anuncian resultados? — 4.1.2, 4.1.3
4. ¿La selección de variante usa texto además del color? — 1.4.1, 1.3.3
5. ¿El precio, descuento y disponibilidad cumplen contraste ≥ 4.5:1? — 1.4.3
6. ¿El checkout muestra indicador de progreso y pasos claros? — 2.4.x, 3.3.x
7. ¿Los errores de pago se identifican en texto y con sugerencia? — 3.3.1, 3.3.3
8. ¿Antes de pagar hay resumen del pedido confirmable y editable? — 3.3.4
9. ¿Los objetivos táctiles (cantidad, favorito, carrito) miden ≥ 24×24px? — 2.5.8
10. ¿La pasarela de pago de terceros es accesible (o hay alternativa)? — Conf. Req. 5

## Lectores de pantalla recomendados

- **VoiceOver + Safari (iOS)** y **TalkBack + Chrome (Android)** —
  ecosistema móvil predominante en compras retail. Complementar con
  **NVDA + Firefox** en escritorio. Ver
  `references/protocolo-lectores-pantalla.md`.

## Consideración regulatoria

El **Estatuto del Consumidor (Ley 1480)** y las reglas de la **SIC** para
comercio electrónico exigen información clara y suficiente. Prioriza los
issues del flujo de compra (búsqueda → variante → checkout → pago) al
calcular la matriz de `references/priorizacion-remediacion.md`.
