# Seguimiento interno de información legal faltante

Este archivo reúne las verificaciones y los datos que todavía faltan. No se copia al directorio `site/` ni se publica en el sitio legal. Quitar los avisos de los documentos públicos no significa que estos puntos estén resueltos.

Última revisión: 13 de noviembre de 2026.

## Prioridad alta — privacidad y operación

### 1. Inventario real de proveedores y encargados

- **Documento relacionado:** Política de privacidad, §5.
- **Falta:** confirmar los servicios activos y la configuración efectiva de Supabase, Render, Cloudflare/R2, Sentry, AdMob, RevenueCat, Apple y Google; identificar partners publicitarios, entidades contratadas y cualquier proveedor usado para soporte.
- **Datos a reunir:** entidad legal, función, categorías de datos, región de procesamiento, plazo de retención, subencargados y enlace de privacidad.
- **Criterio de cierre:** inventario contrastado contra producción y consolas, con enlaces y texto público corregidos si existen diferencias.

### 2. Transferencias internacionales

- **Documento relacionado:** Política de privacidad, §6.
- **Falta:** identificar los países o regiones reales de almacenamiento y acceso para cada proveedor, el mecanismo jurídico aplicable a cada transferencia y las salvaguardas disponibles.
- **Criterio de cierre:** mapa de transferencias validado, mecanismo documentado y canal definido para solicitar información sobre las salvaguardas.

### 3. Retención de registros técnicos y datos de proveedores

- **Documento relacionado:** Política de privacidad, §9.
- **Falta:** obtener y documentar la retención efectiva de registros técnicos de Sentry, Render y Cloudflare, además de cualquier otro proveedor confirmado.
- **También verificar:** que la configuración real y los planes contratados coincidan con esos plazos y que los procesos de eliminación alcancen los datos que corresponda borrar en terceros.
- **Criterio de cierre:** tabla de retención por proveedor y categoría, configuración comprobada y texto público actualizado con cualquier plazo relevante.

## Cierre transversal

### 4. Revisión legal y aprobación de versión

- **Alcance:** Política de privacidad, Términos, Reglas de comunidad, Compras, Soporte, Eliminación de cuenta, Créditos y Licencias de código abierto.
- **Falta:** revisión integral por una persona profesional competente para los mercados donde se distribuirá la app y aprobación de una versión identificable.
- **Criterio de cierre:** versión, fecha, responsable de aprobación y registro de cambios conservados.

### 5. Mercados e idiomas futuros

- **Falta:** antes de distribuir fuera de Argentina, revisar jurisdicción, consumidor, privacidad, menores, publicidad, tiendas, domicilio o canales obligatorios y traducciones para cada país.
- **Criterio de cierre:** checklist por mercado e idioma, traducción revisada y contenido publicado en su ruta estable antes de habilitar la distribución.

### 6. Lanzamiento del modo Versus

- **Propuesta:** [Reglas](propuestas/versus/01-reglas-versus.es.md), [integración y recompensas futuras](propuestas/versus/02-integracion-y-futuras-recompensas.es.md) y [comunicación y lanzamiento](propuestas/versus/03-comunicacion-y-lanzamiento.es.md). Son borradores fuera del sitio legal, visibles en este repositorio público.
- **Verificado en el código local el 10 de noviembre de 2026:** crear cuesta **30 tokens**, solo para el creador; los invitados juegan gratis y no hay premios. La API informa el precio y cobra en la transacción de creación, con protección de reintentos y rechazo sin cobro si falta saldo. La app muestra el precio, pide confirmación y actualiza el saldo. Se retiró de los borradores la alternativa gratuita.
- **También falta:** habilitar la consulta de reglas desde la app y su aceptación verificable antes de usar Versus; hoy la detección de nueva versión borra la aceptación local y vuelve a pedirla en el siguiente inicio. Contrastar con clientes anteriores y sesiones abiertas.
- **Plan de mobile:** [Modales de primer inicio y actualización](propuestas/versus/04-plan-modales-legales-mobile.es.md). Cambia solo la presentación del primer inicio y propone un flujo separado para avisos de actualización, con carga de datos en segundo plano y versiones de privacidad.
- **Documentos relacionados:** términos, compras por el costo de creación, privacidad por visibilidad/estadísticas y retención, y nuevo anexo Versus. Fijar fecha y versiones, archivar textos anteriores, contrastar con el despliegue y revisar el encuadre legal antes de publicar.
- **Criterio de cierre:** mecánica, costo, soporte para correcciones/restituciones, reglas publicadas, enlaces, aceptación registrada y comunicación de tiendas coincidentes con el lanzamiento. Los premios o un pozo futuro requieren una revisión nueva.

## Puntos cerrados por los cambios incorporados en `main`

Los PR #4 y #5 completaron o documentaron bases jurídicas, consentimiento publicitario y ATT, control de edad, aceptación de términos, eliminación de cuentas invitadas, verificación de titularidad, exportación de datos, colisión de cuentas, ofertas y cancelaciones, reportes de jugadores/grupos/anuncios, catálogo de Picture Cross, listas de palabras y avisos de software de código abierto. Esos puntos se retiraron del seguimiento activo al resolver el conflicto con `main`.
