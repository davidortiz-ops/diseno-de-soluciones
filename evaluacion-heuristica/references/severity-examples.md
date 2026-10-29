# Escala de Severidad — Ejemplos Expandidos por Industria

Lee este archivo cuando necesites ejemplos concretos para calificar la severidad de un hallazgo. Úsalo como referencia durante la evaluación.

---

## Escala Nielsen 0-4

| Nivel | Nombre | Significado |
|---|---|---|
| 0 | No es problema | No afecta la usabilidad |
| 1 | Cosmético | Problema estético, no funcional. Arreglar si hay tiempo |
| 2 | Menor | Baja prioridad. Causa leve frustración pero no bloquea |
| 3 | Mayor | Alta prioridad. Dificulta significativamente la tarea |
| 4 | Catastrófico | Bloquea completamente al usuario. Debe arreglarse ya |

---

## Ejemplos por Industria

### Banca Digital

| Severidad | Ejemplo |
|---|---|
| **4** | Transferencia falla sin mensaje de error ni opción de reintento — el usuario pierde los datos ingresados |
| **4** | El botón "Pagar" no responde en el paso final de un pago de servicios |
| **3** | La autenticación biométrica falla y no hay opción de respaldo clara |
| **3** | Las tasas de cambio no se muestran antes de confirmar una transferencia internacional |
| **3** | No hay confirmación visual después de agendar un pago recurrente |
| **2** | El historial de transacciones no muestra filtros por fecha o tipo |
| **2** | Los términos y condiciones están en una fuente muy pequeña |
| **2** | El menú tiene términos bancarios internos ("Cruce de cuentas") en lugar de lenguaje de usuario |
| **1** | El color del logo institucional varía ligeramente entre pantallas |
| **1** | Un icono decorativo está pixelado en la pantalla de login |
| **1** | El espaciado entre filas de la tabla de movimientos es inconsistente |
| **0** | La animación del logo en la pantalla de carga no afecta la tarea del usuario |

### Retail / E-commerce

| Severidad | Ejemplo |
|---|---|
| **4** | El botón "Comprar" redirige a un error 500 sin mantener el carrito |
| **4** | No se puede completar el pago porque el formulario de tarjeta rechaza formatos válidos |
| **3** | El costo de envío se revela solo después de ingresar todos los datos de pago |
| **3** | No hay confirmación de compra ni email — el usuario no sabe si su pedido procedió |
| **3** | El buscador no encuentra productos por nombres comunes o sinónimos |
| **2** | Los filtros de búsqueda se resetean al volver de la ficha de producto |
| **2** | Las tallas de ropa usan códigos internos (M1, M2) en vez de S/M/L |
| **2** | El carrito no muestra el stock disponible al agregar cantidades |
| **1** | Las imágenes de producto tienen distinta altura en la grilla de resultados |
| **1** | El footer tiene enlaces rotos a políticas de envío |
| **1** | El placeholder del buscador dice "Buscar..." sin sugerencias |
| **0** | La fuente del copyright en el footer difiere de la del contenido |
| **0** | El badge de "Nuevo" en productos tiene un tono de rojo distinto al del logo |

### Genérico (cualquier sitio web)

| Severidad | Ejemplo |
|---|---|
| **4** | El formulario de login no muestra error al ingresar credenciales incorrectas |
| **4** | No hay manera de recuperar la contraseña |
| **3** | Los mensajes de error muestran códigos técnicos (Error #245AB) |
| **3** | La navegación por teclado se detiene en un campo de formulario |
| **2** | Los enlaces tienen colores que no se distinguen del texto normal |
| **2** | La página de resultados no dice cuántos resultados hay |
| **1** | El logo no está enlazado al homepage |
| **1** | El espaciado entre secciones es inconsistente |
| **0** | La sombra de las tarjetas no es uniforme |
| **0** | El tamaño del favicon no es el estándar |

---

## Matriz de Decisión Rápida

| Situación | Severidad |
|---|---|
| El usuario no puede completar la tarea | 4 |
| El usuario puede completar pero con mucha dificultad | 3 |
| El usuario se frustra pero completa | 2 |
| El usuario nota algo imperfecto pero no le afecta | 1 |
| No afecta la experiencia del usuario | 0 |
