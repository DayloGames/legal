# Seguimiento interno de información legal faltante

Este archivo reúne las verificaciones y los datos que todavía faltan. No se copia al directorio `site/` ni se publica en el sitio legal. Quitar los avisos de los documentos públicos no significa que estos puntos estén resueltos.

Última revisión: 26 de octubre de 2026.

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

## Puntos cerrados por los cambios incorporados en `main`

Los PR #4 y #5 completaron o documentaron bases jurídicas, consentimiento publicitario y ATT, control de edad, aceptación de términos, eliminación de cuentas invitadas, verificación de titularidad, exportación de datos, colisión de cuentas, ofertas y cancelaciones, reportes de jugadores/grupos/anuncios, catálogo de Picture Cross, listas de palabras y avisos de software de código abierto. Esos puntos se retiraron del seguimiento activo al resolver el conflicto con `main`.
