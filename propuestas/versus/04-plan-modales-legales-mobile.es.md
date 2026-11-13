# Plan breve: modales de aceptación y actualización legal

Propuesta del 13 de noviembre de 2026. Alcance: plan de implementación; no se modificó mobile ni la API.

## 1. Primer inicio: cambiar solo la presentación

En `src/legal/StartupAgreementGate.tsx`, reemplazar la pantalla completa por un modal con el estilo de los modales de Daylo y un fondo visual de carga, sin montar la app detrás. El fondo puede tener un indicador o skeleton decorativo; no inicia nuevas consultas.

Conservar el momento de liberación del splash, `warmUpStartup()`, la consulta de política, el guardado y la sincronización de aceptación, así como el montaje de sesión, anuncios, compras y datos solo después de aceptar. No mover esos proveedores para poder dibujar el fondo. El modal debe adaptarse a textos grandes, pantallas pequeñas y tema claro/oscuro. Cerrar con Atrás o tocar el fondo no implica aceptar ni habilita la app.

Título: **«Aceptá los Términos de uso»**. Conservar en la descripción la declaración de 18 años, las reglas de comunidad y el enlace informativo a privacidad. Botón: **«Aceptar y continuar»**. Actualizar español e inglés.

## 2. Conservar la diferencia entre primer uso y actualización

En `acceptanceStorage.ts` y `acceptanceSync.ts`, conservar la aceptación anterior cuando se detecten versiones diferentes, en lugar de borrarla. Representar por separado «nunca aceptó» y «ya aceptó, hay una actualización pendiente».

Migrar los registros actuales sin volver a clasificar como usuario nuevo a quien ya tiene una aceptación, incluso si sus versiones quedaron pendientes de verificar por falta de conexión. No marcar como aceptada una versión que la persona no confirmó.

## 3. Actualizaciones: modal sobre la app que carga normalmente

Agregar un host de actualizaciones junto a `LegalAcceptanceSync`, dentro de la app ya montada. Consultar versiones al iniciar sesión y al volver al primer plano o recuperar conexión, evitando consultas simultáneas. Si hay cambios, mostrar el aviso en esa sesión en un momento seguro, sin interrumpir un juego cronometrado.

Mantener montados navegación, proveedores y consultas: los datos cargan detrás del modal sin esperar a la nueva aceptación y sin repetir el bloqueo del primer inicio. El modal bloquea la interacción que corresponda, no la carga. Un reinicio con una actualización pendiente mantiene este comportamiento.

Título general: **«Actualizamos nuestros documentos»**; si cambia solo términos, **«Actualizamos los Términos de uso»**. Mostrar un resumen breve y enlaces a los documentos afectados. Para cambios que requieren aceptación: **«Aceptar cambios»** y una salida explícita como **«Ahora no»**, manteniendo el aviso pendiente y definiendo qué funciones requieren aceptarlo. Un aviso meramente informativo puede usar **«Entendido»**. No confundir cerrar, leer o continuar con aceptar.

## 4. API: permitir también actualizaciones de privacidad

Hoy `/legal/policy` y el registro de aceptación solo versionan términos y comunidad. Ampliar el contrato de forma compatible con clientes anteriores: versión de privacidad y metadatos de publicación, resumen, enlaces y tipo de acción requerida por documento. Mantener los campos existentes durante la transición y definir el comportamiento de los clientes anteriores.

Registrar por cuenta y versión la aceptación o la constancia de aviso según corresponda, con fecha del servidor. Un aviso de privacidad no debe fabricar una nueva aceptación de términos ni consentimiento publicitario. Si la política cambia mientras el modal está abierto, actualizar el aviso antes de registrar la confirmación. Publicar los textos antes de activar sus versiones en la API.

## 5. Validación y orden de trabajo

Primero implementar la presentación inicial y sus textos. Después, el estado persistido, el contrato compatible de API y el host de actualizaciones. Por último, probar los dos recorridos:

- Primer uso: el modal aparece sobre el fondo de carga; aceptar conserva el orden actual de arranque y no inicia sesión, anuncios ni compras antes de tiempo.
- Usuario existente: los datos cargan mientras aparece el aviso nuevo, sin desmontar proveedores ni perder navegación; no se muestra de nuevo la presentación de primer uso.
- Cubrir términos, comunidad y privacidad; sin cambios no se repite el aviso. Verificar además falta de conexión, reintento, reinicio, cambio de cuenta, política actualizada durante la confirmación y migración de registros existentes.
