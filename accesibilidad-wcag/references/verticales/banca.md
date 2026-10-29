# Guía vertical: Accesibilidad en Banca

Guía específica para auditar productos digitales del sector financiero
colombiano (entidades vigiladas por la SFC).

## Tipos de sitio

- **Banca transaccional:** portal/app donde el cliente opera (consultas,
  transferencias, pagos, recargas).
- **Portal corporativo / público:** información de productos, tasas,
  oficinas, sin autenticación.
- **Intranet:** herramientas internas para empleados.
- **Onboarding digital:** apertura de cuenta o vinculación 100% digital
  (con validación de identidad).
- **Dashboard financiero:** tableros de posición, inversiones, indicadores.

## Flujos críticos de accesibilidad

1. **Login / autenticación** — 2FA, OTP, biometría, token.
2. **Solicitud de productos** — créditos, tarjetas, CDTs, cuentas.
3. **Consulta de estados de cuenta** — extractos, movimientos, certificados.
4. **Transferencias y pagos** — entre cuentas, a terceros, PSE, servicios.
5. **Recarga de productos** — celulares, monederos, tarjetas prepago.

## Issues específicos de banca

| Issue | SC WCAG | Por qué importa |
|---|---|---|
| Timeout de sesión sin advertencia ni opción de extender | 2.2.1, 2.2.6 | El usuario con AT pierde una transacción a medio completar |
| CAPTCHA visual sin alternativa | 1.1.1, 3.3.8 | Bloquea a usuarios ciegos; viola autenticación accesible |
| Tablas de movimientos/tasas sin encabezados de celda | 1.3.1 | El lector no relaciona el dato con su columna |
| Contraste insuficiente en tablas de tasas e intereses | 1.4.3, 1.4.6 | Cifras financieras ilegibles para baja visión |
| Widgets de terceros (core bancario embebido, chat) sin accesibilidad | 4.1.2, Conf. Req. 5 | Rompe la cadena de conformidad del flujo completo |
| OTP que expira sin anuncio a lector de pantalla | 4.1.3, 2.2.1 | El usuario no sabe que el código caducó |
| Errores de validación de monto solo en color rojo | 1.4.1, 3.3.1 | No perceptible para daltónicos ni lectores |
| Foco oculto tras barra fija de sesión/saldo | 2.4.11 | El usuario por teclado pierde de vista dónde está |

## Checklist rápida bancaria (10 puntos prioritarios)

1. ¿El login funciona 100% con teclado y permite pegar/gestor de
   contraseñas (sin acertijos cognitivos)? — 2.1.1, 3.3.8
2. ¿Hay aviso de inactividad con opción de extender la sesión? — 2.2.1, 2.2.6
3. ¿El OTP/2FA anuncia su estado y errores a la AT? — 4.1.3, 3.3.1
4. ¿Las tablas de movimientos y tasas tienen `<th scope>` y `<caption>`? — 1.3.1
5. ¿El contraste de cifras y tasas cumple ≥ 4.5:1 (ideal 7:1)? — 1.4.3, 1.4.6
6. ¿Los errores de formulario se identifican en texto y con sugerencia? — 3.3.1, 3.3.3
7. ¿Antes de transferir/pagar hay resumen confirmable y reversible? — 3.3.4
8. ¿Los botones de acción (Transferir, Pagar) tienen nombre accesible coherente? — 2.5.3, 4.1.2
9. ¿Los widgets de terceros (chat, core) son operables con AT? — 4.1.2
10. ¿El foco es visible y no queda oculto por barras fijas? — 2.4.7, 2.4.11

## Lectores de pantalla recomendados

- **NVDA + Firefox** y **JAWS + Chrome** — ecosistema Windows corporativo,
  predominante en banca colombiana. Ver
  `references/protocolo-lectores-pantalla.md`.

## Consideración regulatoria

La **Circular Externa SFC (2022)** obliga a canales digitales accesibles.
Prioriza los issues con riesgo legal alto (login, transacciones, errores)
al calcular la matriz de `references/priorizacion-remediacion.md`.
