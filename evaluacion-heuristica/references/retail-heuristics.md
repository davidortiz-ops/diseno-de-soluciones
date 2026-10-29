# Heurísticas Extendidas para Retail / E-commerce

Lee este archivo cuando el contexto de evaluación sea **retail o e-commerce** (tienda online, marketplace). Estas 4 heurísticas se suman a las 10 de Nielsen. Evalúa cada una siguiendo la misma escala de severidad (0-4).

---

## H11: Claridad del Proceso de Compra

El flujo de compra debe ser predecible, transparente y sin fricciones. Cada paso debe comunicar claramente qué está ocurriendo y qué sigue.

### Preguntas de evaluación
- ¿El proceso de checkout muestra los pasos totales y el progreso actual?
- ¿Los costos totales (producto + envío + impuestos) se muestran antes de ingresar datos de pago?
- ¿El botón de pago/compra es claramente visible y distinguible?
- ¿Se pueden modificar cantidades o eliminar productos desde el carrito sin perder el contexto?
- ¿El formulario de pago permite guardar información para futuras compras?

### Checklist retail
- [ ] Barra de progreso visible con pasos numerados (ej. "Paso 2 de 4")
- [ ] Desglose de costos visible antes del pago
- [ ] Botón "Comprar ahora" / "Pagar" con color contrastante y tamaño adecuado
- [ ] Edición de cantidades en carrito sin recargar la página
- [ ] Opción "Recordar tarjeta" con checkbox y mensaje de seguridad

### Ejemplo de hallazgo
| Campo | Valor |
|---|---|
| **Título** | Costo de envío no visible hasta el último paso del checkout |
| **Ubicación** | Carrito de compras / paso 1 de checkout |
| **Severidad** | 3 (mayor) |
| **Recomendación** | Mostrar estimado de envío en la página del carrito con calculadora de código postal |
| **Esfuerzo** | Medio |

---

## H12: Confianza en Pago y Datos

El usuario debe sentir que sus datos de pago están seguros y que puede confiar en el vendedor.

### Preguntas de evaluación
- ¿Se muestran sellos de seguridad y medios de pago aceptados antes del pago?
- ¿El formulario de pago está en una página segura (https, candado)?
- ¿Se ofrecen métodos de pago familiares (tarjeta, PayPal, transferencia)?
- ¿Las políticas de envío, devolución y garantía están accesibles desde el checkout?
- ¿Los datos de contacto y atención al cliente son visibles?

### Checklist retail
- [ ] Sellos de seguridad (SSL, McAfee, etc.) visibles en el checkout
- [ ] Logos de medios de pago aceptados mostrados antes de seleccionar
- [ ] Indicador de página segura en la barra de direcciones
- [ ] Enlaces a políticas de devolución en el footer del checkout
- [ ] Número de atención al cliente visible en todas las páginas

### Ejemplo de hallazgo
| Campo | Valor |
|---|---|
| **Título** | Sin sellos de seguridad ni medios de pago visibles en la página de checkout |
| **Ubicación** | Página de pago completa |
| **Severidad** | 3 (mayor) |
| **Recomendación** | Agregar badges de seguridad y logos de tarjetas aceptadas cerca del botón de pago |
| **Esfuerzo** | Pequeño |

---

## H13: Findabilidad de Productos

El usuario debe encontrar productos rápidamente mediante búsqueda, filtros y navegación intuitiva.

### Preguntas de evaluación
- ¿El buscador está visible y accesible desde cualquier página?
- ¿Los resultados de búsqueda incluyen filtros relevantes (precio, marca, categoría)?
- ¿Los filtros aplicados son visibles y editables?
- ¿La navegación por categorías refleja la mentalidad del usuario, no la estructura interna?
- ¿Las fichas de producto muestran información clave (precio, stock, variantes) sin scroll?

### Checklist retail
- [ ] Barra de búsqueda en el header con placeholder descriptivo
- [ ] Filtros por precio, marca, rating y categoría visibles sin scroll
- [ ] Etiquetas de filtros activos con opción "Limpiar todos"
- [ ] Categorías con nombres de usuario, no técnicos
- [ ] Ficha de producto con precio, stock, colores/tallas y rating visibles

### Ejemplo de hallazgo
| Campo | Valor |
|---|---|
| **Título** | Búsqueda no muestra resultados mientras se escribe (no hay autocomplete) |
| **Ubicación** | Barra de búsqueda del header |
| **Severidad** | 2 (menor) |
| **Recomendación** | Implementar búsqueda predictiva con sugerencias de productos y categorías |
| **Esfuerzo** | Grande |

---

## H14: Post-Compra y Seguimiento

La experiencia no termina en el pago. El usuario debe tener visibilidad del estado de su pedido y opciones post-compra claras.

### Preguntas de evaluación
- ¿La confirmación de compra es inmediata e incluye resumen del pedido?
- ¿El usuario recibe seguimiento del envío (tracking) sin tener que buscarlo?
- ¿La página de "Mis pedidos" muestra estado actual y acciones disponibles?
- ¿El proceso de devolución/cambio es visible y accesible?
- ¿Hay opciones de post-compra (factura, modificar dirección, cancelar)?

### Checklist retail
- [ ] Pantalla de confirmación con número de pedido, resumen y fecha estimada
- [ ] Email/SMS con link de tracking activo
- [ ] Sección "Mis pedidos" con cada pedido, estado y acciones (ver detalle, tracking, devolver)
- [ ] Política de devolución visible desde el panel de pedido
- [ ] Opción de descargar factura sin contactar a soporte

### Ejemplo de hallazgo
| Campo | Valor |
|---|---|
| **Título** | Sin pantalla de confirmación post-pago — solo redirección al homepage |
| **Ubicación** | Post-checkout |
| **Severidad** | 3 (mayor) |
| **Recomendación** | Implementar pantalla de confirmación con resumen, número de pedido y opción de tracking |
| **Esfuerzo** | Medio |
