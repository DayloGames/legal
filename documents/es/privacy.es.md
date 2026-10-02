# Política de privacidad de [PENDIENTE: nombre público]

BORRADOR — no vigente ni listo para publicar. Versión de trabajo 0.1, 2 de octubre de 2026. Los pendientes deben resolverse y eliminarse antes de publicación.

## 1. Quién trata tus datos

[PENDIENTE: persona o razón social], con domicilio de contacto en [PENDIENTE: domicilio y país], es responsable del servicio [PENDIENTE: nombre público], al que llamamos «la app» en esta política.

Para consultas de privacidad y solicitudes sobre tus datos: [PENDIENTE: email de privacidad atendido]. Para ayuda general, consultá [Soporte](support.es.md).

## 2. Datos que usamos

**Cuenta y acceso.** Al comenzar a usar la app se crea una cuenta de invitado con un identificador técnico para guardar tu progreso. Aunque no escribas tu email, esta cuenta genera datos vinculados a tu actividad. Si vinculás Google o Apple, nuestro servicio de autenticación recibe identificadores y la información que esos proveedores facilitan para el acceso, que puede incluir email y datos de perfil. Apple puede proporcionar un email privado y el nombre que autorizaste; la implementación actual guarda nombre y apellido en el servicio de autenticación. Estos datos de acceso no se usan como tu nombre público automáticamente.

**Perfil y preferencias.** Guardamos el nombre de usuario que elegís, tu código de amigo, avatar y artículos seleccionados, idioma, tema y datos de configuración necesarios para sincronizar preferencias. Usamos la zona horaria del dispositivo para organizar días y rachas; esto no requiere ubicación GPS.

**Partidas y progreso.** Guardamos partidas, tableros en curso, resultados enviados, tiempos, errores, pistas, días completados, rachas, experiencia, logros y desbloqueos para operar el juego, permitir reanudarlo y revisar resultados o posibles abusos.

**Economía y compras.** Guardamos saldo y movimientos de monedas/tokens, artículos obtenidos y datos de compras como producto, tienda, identificador de transacción, fechas, devoluciones y estado de suscripción. Los pagos los procesa la tienda correspondiente; la app no solicita tu número completo de tarjeta.

**Funciones sociales.** Guardamos solicitudes y relaciones de amistad, grupos, nombres de grupo, membresías, roles, códigos de acceso, rankings, invitaciones y cumplimiento de hitos de referidos.

**Bloqueos y reportes.** Guardamos bloqueos y denuncias, incluyendo cuentas involucradas, razón, nombre denunciado al momento del reporte y la nota que decidas escribir. Evitá incluir información sensible o datos de otras personas que no sean necesarios.

**Datos técnicos.** La conexión con nuestros servicios puede generar IP y metadatos de red, dispositivo y solicitudes. Los servicios de diagnóstico pueden recibir errores, información de rendimiento, registros técnicos e identificadores de cuenta. Los servicios publicitarios pueden procesar señales de dispositivo, identificadores y actividad publicitaria según tus preferencias y la configuración aplicable.

**Soporte.** Si nos contactás, tratamos tus datos de contacto y la información que aportes para atender la consulta.

## 3. Para qué y con qué fundamento

Usamos los datos para operar cuentas y partidas, sincronizar progreso, ofrecer funciones sociales, entregar bienes y beneficios, verificar compras y recompensas, atender solicitudes, prevenir fraude y abuso, y diagnosticar fallos. Si hay publicidad, usamos los datos correspondientes para servirla y gestionar sus preferencias.

[PENDIENTE: identificar las bases jurídicas por finalidad y mercados: prestación del servicio, obligaciones aplicables, consentimiento cuando corresponda y otros fundamentos admisibles. Precisar el tratamiento de publicidad y diagnóstico; no atribuir consentimiento a la mera lectura de esta política.]

## 4. Qué pueden ver otras personas

Tu nombre elegido, código de amigo y avatar pueden ser visibles al interactuar con otros jugadores. Los amigos pueden ver información de progreso, racha, nivel o logros que muestre la función. Los miembros de tus grupos pueden ver tu participación y resultados de ranking.

Los grupos se comparten mediante códigos; tratá sus códigos como invitaciones y compartilos con cuidado. Bloquear a alguien limita las interacciones y visibilidad entre ambas cuentas en las funciones que aplican ese control; no lo expulsa automáticamente de un grupo compartido ni oculta tu información a sus demás miembros.

Si participás en referidos, quien te invitó puede conocer el cumplimiento de los hitos que generan recompensas, como la vinculación de una cuenta y determinados avances de juego.

No mostramos tu email de acceso en los perfiles sociales de la app. Tampoco entregamos automáticamente al denunciado la identidad de quien lo reportó.

## 5. Servicios que intervienen

La arquitectura incluye los siguientes servicios, cuya configuración de producción debe confirmarse antes de publicar esta lista:

| Servicio | Función y datos principales |
| --- | --- |
| Supabase | Autenticación, identidades de acceso y base de datos con perfil, juego, economía y funciones sociales; imágenes de catálogo si se utiliza su almacenamiento. |
| Render | Alojamiento del backend y procesamiento de solicitudes y registros técnicos. |
| Cloudflare | Entrega y protección del tráfico; imágenes si se utiliza R2. |
| Sentry | Diagnóstico de fallos, registros y rendimiento, con datos técnicos e identificadores cuando está habilitado. |
| Google AdMob y proveedores configurados | Publicidad y consentimiento; identificación de cuenta y verificación de recompensas de anuncios opcionales. |
| RevenueCat | Verificación y gestión de compras/suscripciones asociadas a tu identificador de cuenta. |
| Apple y Google | Inicio de sesión y pagos mediante sus tiendas, bajo sus propias condiciones y políticas. |

[PENDIENTE: confirmar servicios habilitados, partners publicitarios, entidades contratadas, hosting del sitio, proveedor de soporte y enlaces a información relevante.]

## 6. Tratamiento internacional

Los servicios utilizados pueden procesar datos fuera de tu país. [PENDIENTE: países/regiones reales de almacenamiento y acceso, mecanismos de transferencia aplicables y cómo solicitar información sobre las salvaguardas.]

## 7. Publicidad y preferencias

La app puede mostrar anuncios entre partidas y ofrecer anuncios voluntarios a cambio de recompensas. Según tu región y la configuración aplicable, te presentamos opciones de privacidad publicitaria. Cuando esa opción corresponde, podés revisarlas en **Cuenta → Privacidad de anuncios**.

La autorización de publicidad o tracking que corresponda se solicita de forma separada de las condiciones de uso. [PENDIENTE: describir el flujo real de consentimiento, rechazo, revocación y ATT en iOS tras verificar build y consola; especificar tratamiento por edad.]

## 8. Almacenamiento en tu dispositivo

Usamos almacenamiento local para mantener la sesión, preferencias, frecuencia de anuncios y datos necesarios de los servicios integrados. Eliminar la app o sus datos locales puede hacer que pierdas acceso al progreso de invitado. Desinstalar no constituye una solicitud de eliminación de datos del servidor ni cancela una suscripción.

## 9. Conservación y eliminación

Conservamos datos mientras resultan necesarios para las finalidades explicadas, sujeto a los plazos que se indican a continuación.

[PENDIENTE: completar plazos aprobados para cuentas activas/inactivas, invitados, registros de juego/economía, compras, reportes, resolución de cuentas, logs, soporte, proveedores y backups.]

Al solicitar eliminación, la cuenta queda inhabilitada y se eliminan la identidad de acceso y datos operativos mediante el proceso correspondiente. Algunos registros pueden conservarse durante un período limitado para seguridad, investigación de reportes u obligaciones específicas. [PENDIENTE: enumerar categorías concretas, fundamento y plazo real, incluida purga diferida de partidas y movimientos; no afirmar que el ID residual es anónimo.]

Las copias de seguridad y los sistemas de terceros pueden tener ciclos distintos, que deben informarse aquí: [PENDIENTE: ventanas y procedimiento]. Consultá [Eliminación de cuenta](delete-account.es.md) para los pasos y efectos sobre progreso y compras.

## 10. Tus derechos

Podés solicitar acceso, corrección o eliminación de tus datos y ejercer otros derechos que correspondan por tu legislación. Escribí a [PENDIENTE: email de privacidad]. Podremos pedir información mínima para verificar que la solicitud es tuya, sin pedir tu contraseña.

[PENDIENTE: plazos aplicables, autoridad de control y vías de reclamo por mercados; canal de exportación disponible y cómo completar datos que no cubra la descarga de la app.]

## 11. Edad de acceso

[PENDIENTE: edad mínima, países, tratamiento de adolescentes, controles implementados y procedimiento ante datos de personas que no pueden usar el servicio. No asumir 16+ ni prometer que no se reciben datos de menores sin controles efectivos.]

## 12. Seguridad y cambios

Aplicamos medidas técnicas y organizativas acordes al servicio, como controles de acceso y protección de comunicaciones. No prometemos ausencia absoluta de incidentes.

Publicaremos cambios con su fecha de vigencia y te informaremos los cambios relevantes por los canales adecuados. Cuando una modificación requiera consentimiento, lo solicitaremos antes del tratamiento correspondiente.
