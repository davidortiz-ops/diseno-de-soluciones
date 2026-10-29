# Heurísticas Extendidas para Banca Digital

Lee este archivo cuando el contexto de evaluación sea **banca digital** (web o app). Estas 4 heurísticas se suman a las 10 de Nielsen. Evalúa cada una siguiendo la misma escala de severidad (0-4).

---

## H11: Seguridad Perceptible y Confianza

El diseño debe transmitir seguridad en cada interacción sin generar fricción innecesaria. Los usuarios de banca digital necesitan sentir que sus datos y transacciones están protegidos.

### Preguntas de evaluación
- ¿La página/login muestra señales de seguridad visibles (candado, https, logo de seguridad)?
- ¿Los mensajes de seguridad usan lenguaje tranquilizador, no alarmista?
- ¿La autenticación biométrica (huella, facial) está disponible como opción por defecto?
- ¿Los elementos de seguridad (2FA, confirmaciones) se presentan como protección, no como obstáculo?
- ¿El diseño evita que el usuario "culpe" a su contraseña cuando hay problemas de acceso?

### Checklist banca
- [ ] Indicador de conexión segura visible en login y durante toda la sesión
- [ ] Mensajes de seguridad con tono tranquilizador ("Protegemos tu información")
- [ ] Autenticación biométrica como opción primaria (no secundaria)
- [ ] Confirmación de acciones sensibles sin ser intrusiva
- [ ] Bloqueo de cuenta con mensaje claro y proceso de recuperación visible

### Ejemplo de hallazgo
| Campo | Valor |
|---|---|
| **Título** | Ausencia de indicador de sesión segura en el dashboard |
| **Ubicación** | Panel principal post-login |
| **Severidad** | 2 (menor) |
| **Recomendación** | Agregar badge "Conexión segura" o candado en el header |
| **Esfuerzo** | Pequeño |

---

## H12: Privacidad y Protección de Datos

El usuario debe tener control visible sobre sus datos personales y financieros, y entender cómo se utilizan.

### Preguntas de evaluación
- ¿El usuario puede ver y gestionar sus datos personales fácilmente?
- ¿Las políticas de privacidad y tratamiento de datos están accesibles desde cualquier pantalla?
- ¿Se solicita consentimiento explícito para compartir datos con terceros?
- ¿El usuario puede cerrar sesión remotamente en todos sus dispositivos?
- ¿Las notificaciones de actividad inusual son claras y accionables?

### Checklist banca
- [ ] Sección "Mis datos" accesible desde el menú principal
- [ ] Política de privacidad disponible sin login y en el footer
- [ ] Opción de "Cerrar sesión en todos los dispositivos"
- [ ] Notificaciones push/email para actividad sospechosa
- [ ] Opción de descarga de datos personales (portabilidad)

### Ejemplo de hallazgo
| Campo | Valor |
|---|---|
| **Título** | Sin opción de cerrar sesión remota en otros dispositivos |
| **Ubicación** | Configuración de seguridad |
| **Severidad** | 3 (mayor) |
| **Recomendación** | Agregar "Cerrar sesión en otros dispositivos" con confirmación |
| **Esfuerzo** | Medio |

---

## H13: Recuperación de Errores Financieros

Cuando ocurre un error en una transacción o proceso financiero, el usuario debe poder recuperarse sin pérdida de datos ni tiempos muertos extensos.

### Preguntas de evaluación
- ¿Las transacciones fallidas muestran mensajes claros sin códigos de error?
- ¿Se ofrece reintento automático o manual para transacciones fallidas?
- ¿El historial muestra el estado real de cada transacción (pendiente/completada/fallida)?
- ¿Hay un proceso claro para reportar errores o discrepancias?
- ¿Los tiempos de espera (timeout) en sesiones no pierden datos del usuario?

### Checklist banca
- [ ] Mensajes de error en lenguaje claro ("No pudimos procesar tu transferencia. Intenta de nuevo.")
- [ ] Botón de "Reintentar" visible sin navegar a otra pantalla
- [ ] Historial de transacciones con estados visibles y fechas
- [ ] Canal de soporte para discrepancias accesible desde la transacción
- [ ] Timeout con guardado automático de datos ingresados

### Ejemplo de hallazgo
| Campo | Valor |
|---|---|
| **Título** | Error genérico "Transacción fallida" sin motivo ni acción sugerida |
| **Ubicación** | Flujo de transferencia, paso de confirmación |
| **Severidad** | 4 (catastrófico) |
| **Recomendación** | Reemplazar por mensaje descriptivo + botón de reintento + opción de contactar soporte |
| **Esfuerzo** | Medio |

---

## H14: Cumplimiento Regulatorio Visible

La interfaz debe evidenciar cumplimiento con normativas financieras y de accesibilidad sin abrumar al usuario. En Colombia, aplica un marco normativo específico que debe reflejarse en el diseño.

### Preguntas de evaluación
- ¿Se muestran los registros/números de autorización de la Superintendencia Financiera?
- ¿Las tasas, comisiones y cargos (incluyendo 4x1000, IVA) se muestran antes de confirmar operaciones?
- ¿El diseño cumple con contraste WCAG 2.1 AA (4.5:1 texto normal)?
- ¿La navegación por teclado es funcional en todas las pantallas críticas?
- ¿Los términos legales están disponibles sin interrumpir el flujo?

### Checklist banca Colombia
- [ ] Número de registro ante la Superintendencia Financiera visible en footer
- [ ] Costos totales (incluyendo impuestos: 4x1000, IVA) visibles antes de cada transacción
- [ ] Información clara sobretasas de interés (EA, nominal) y plazo según Circular Externa 007
- [ ] Enlace visible al Seguro de Depósitos (Fogafín) en el homepage
- [ ] Política de Protección de Datos (Ley 1581 de 2012) accesible desde cualquier pantalla
- [ ] Relación de contraste >= 4.5:1 en textos
- [ ] Todos los formularios accesibles por teclado
- [ ] Tooltips o enlaces a términos sin salir del flujo actual
- [ ] Número de atención al consumidor financiero visible (Superintendencia Financiaria)
- [ ] Proceso de PQR (Peticiones, Quejas, Reclamos) accesible desde el menú principal

### Ejemplo de hallazgo
| Campo | Valor |
|---|---|
| **Título** | Tasas y comisiones no visibles antes de confirmar transferencia internacional |
| **Ubicación** | Flujo de transferencia internacional |
| **Severidad** | 3 (mayor) |
| **Recomendación** | Agregar desglose de costos totales en la pantalla de confirmación antes del submit |
| **Esfuerzo** | Pequeño |

---

## Marco Normativo Colombiano (Referencia)

Evalúa también que la interfaz refleje el cumplimiento de estas normas aplicables al sector financiero en Colombia:

| Norma | Ámbito | Requisito clave para UI |
|---|---|---|
| **Ley 1328 de 2009** | Protección al consumidor financiero | Información clara, contractual, tasa de interés visible, PQR accesible |
| **Ley 1581 de 2012** + Decreto 1377 de 2013 | Protección de datos personales | Aviso de privacidad, consentimiento explícito, portabilidad, supresión |
| **Circular Externa 007 de 1996** (actualizaciones SFC) | Transparencia en productos financieros | Tasas, plazos, costos totales antes de contratar |
| **Circular Externa 029 de 2014** | Seguridad de la información | Autenticación multifactor, notificaciones de actividad, sesiones seguras |
| **Ley 527 de 1999** | Comercio electrónico y firmas digitales | Confirmación de transacciones, validez jurídica de operaciones digitales |
| **Decreto 2555 de 2010** | Normas sector financiero | Requisitos de información para captación y pagos |
| **Ley 1735 de 2014** | SEDPEs (banca digital) | Regulación específica para entidades de pagos electrónicos |
| **Ley 1480 de 2011** | Estatuto del Consumidor | Información veraz, garantías, reverso de pagos (aplica también a retail) |
| **Resolución MINTIC 41462 de 2012** | Accesibilidad web sitios del Estado | Referencia para estándares WCAG 2.0 (extrapolable a banca) |
| **NTC 5854** | Accesibilidad web Colombia | Pautas de accesibilidad para contenido web |
| **Ley 2052 de 2020** | Simplificación de trámites | Eliminación de requisitos innecesarios en flujos digitales |

### Nota para evaluaciones con otra normativa
Si el contexto del cliente es otro país (Perú, México, Chile, etc.), pregunta al usuario qué normativa local aplica antes de evaluar. Sustituye o complementa esta tabla con la regulación correspondiente.
