# Protocolo de prueba con lectores de pantalla

Guía para verificar accesibilidad con tecnologías de asistencia (AT).
Incluye atajos, checklist de verificación y un script de prueba estándar
por lector.

## Tabla resumen de lectores

| AT | SO | Navegador recomendado | Instalación | Atajos clave |
|---|---|---|---|---|
| NVDA | Windows | Firefox | nvda.es (gratuito) | Insert+F7 (lista de elementos), Insert+F6, H (encabezados), Tab, flechas |
| JAWS | Windows | Chrome | freedomscientific.com (comercial) | Insert+F6 (encabezados), Insert+F3 (lista), Ctrl+Insert+Home, flechas |
| VoiceOver | macOS | Safari | Integrado (Cmd+F5) | VO=Ctrl+Opt; VO+U (rotor), VO+flechas, Tab |
| TalkBack | Android | Chrome | Integrado | Swipe izq/der (siguiente/anterior), doble tap (activar), exploración táctil |

## Atajos esenciales (mínimo 10) por lector

### NVDA (Windows + Firefox)

1. `Insert+F7` — lista de elementos (enlaces, encabezados, landmarks)
2. `H` / `Shift+H` — siguiente/anterior encabezado
3. `1`–`6` — encabezado de nivel N
4. `K` / `Shift+K` — siguiente/anterior enlace
5. `F` — siguiente campo de formulario
6. `T` — siguiente tabla
7. `D` — siguiente landmark/región
8. `B` — siguiente botón
9. `Insert+Espacio` — alternar modo navegación/formulario
10. `Insert+flecha abajo` — leer todo desde el foco

### JAWS (Windows + Chrome)

1. `Insert+F6` — lista de encabezados
2. `Insert+F7` — lista de enlaces
3. `Insert+F5` — lista de campos de formulario
4. `Insert+Ctrl+R` — lista de regiones/landmarks
5. `H` — siguiente encabezado
6. `T` — siguiente tabla
7. `F` — siguiente campo de formulario
8. `B` — siguiente botón
9. `Insert+flecha abajo` — leer todo
10. `Insert+Z` — alternar modo virtual

### VoiceOver (macOS + Safari)

1. `VO+U` — rotor (navegación por tipo de elemento)
2. `VO+flecha der/izq` — siguiente/anterior elemento
3. `VO+Cmd+H` — siguiente encabezado
4. `VO+Cmd+L` — siguiente enlace
5. `VO+Cmd+J` — siguiente control de formulario
6. `VO+Cmd+T` — siguiente tabla
7. `VO+A` — leer todo desde el foco
8. `VO+Espacio` — activar elemento
9. `VO+Shift+flecha abajo` — entrar en grupo/área
10. `Ctrl` — pausar/reanudar lectura

### TalkBack (Android + Chrome)

1. Swipe derecha/izquierda — siguiente/anterior elemento
2. Doble tap — activar elemento enfocado
3. Swipe arriba/abajo — cambiar granularidad (menú de control)
4. Swipe abajo-luego-derecha — menú global
5. Exploración táctil — arrastrar el dedo para leer bajo el dedo
6. Tres dedos swipe — desplazar página
7. Menú de lectura por encabezados/enlaces/controles
8. Doble tap y mantener — acción larga
9. L invertida (gesto) — menú local
10. Volumen arriba+abajo — pausar/reanudar (según versión)

## Checklist de verificación con AT

Para cada flujo, verificar que el lector anuncie correctamente:

- [ ] **Landmarks/roles:** se puede navegar por regiones (header, nav,
  main, footer, search).
- [ ] **Encabezados:** jerarquía h1→h6 sin saltos; navegación por
  encabezados funcional.
- [ ] **Formularios:** cada campo anuncia su etiqueta, tipo, estado
  (requerido/inválido) y mensaje de error/sugerencia.
- [ ] **Tablas:** se anuncian encabezados de fila/columna al recorrer
  celdas; existe `<caption>` o resumen.
- [ ] **Diálogos y modales:** al abrir, el foco entra al modal; al cerrar,
  vuelve al disparador; `Esc` cierra; el fondo queda inerte.
- [ ] **Live regions:** los cambios dinámicos (confirmaciones, resultados,
  carrito) se anuncian sin mover el foco.
- [ ] **Imágenes:** las informativas anuncian alt útil; las decorativas se
  ignoran.
- [ ] **Enlaces:** se anuncia el propósito y, si abre nueva pestaña, se
  informa.

## Script de prueba estándar

Secuencia que el auditor ejecuta y verifica con cada lector:

1. Abrir la página y escuchar el anuncio del **título** y del **idioma**.
2. Activar el **skip link** ("saltar al contenido") y confirmar el salto.
3. Listar **encabezados** y verificar jerarquía lógica (un solo h1).
4. Listar **landmarks** y navegar a `main`, `nav`, `search`.
5. Recorrer el **formulario** principal con Tab: cada campo anuncia
   etiqueta y estado; provocar un error y confirmar que se anuncia con
   sugerencia.
6. Abrir un **modal** (p. ej. OTP en banca, carrito en retail): verificar
   foco al abrir, `Esc` para cerrar y retorno del foco.
7. Recorrer una **tabla** (movimientos en banca, comparativa en retail) y
   confirmar que se anuncian los encabezados de celda.
8. Disparar un **cambio dinámico** (transferencia exitosa / producto
   agregado) y confirmar el anuncio en la live region.
9. Verificar que las **imágenes** clave anuncian alt descriptivo.
10. Recorrer los **enlaces** y confirmar que el propósito es claro fuera de
    contexto.

> Documenta cada paso fallido como hallazgo con su SC asociado (típicamente
> 1.3.1, 2.4.x, 3.3.x, 4.1.2, 4.1.3) y adjunta la grabación de la sesión
> de lectura como evidencia.
