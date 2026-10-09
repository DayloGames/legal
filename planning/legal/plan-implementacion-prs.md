# Plan de implementación del cierre, PR por PR

Fecha: 8 de octubre de 2026. Basado en [plan-de-cierre.md](plan-de-cierre.md) y [revision-codigo-cierre.md](revision-codigo-cierre.md).

## Forma de trabajo acordada

- Trabajar un PR por vez, en una rama del repositorio correspondiente creada desde `main` actualizado o apilada sobre el PR dependiente cuando el usuario lo autorice.
- Al terminar cada cambio: mostrar alcance, validación, pendientes y listado de archivos modificados/nuevos; dejarlo sin commit ni push.
- Hacer commit, push y abrir PR con descripción cuando el usuario lo indique. Todos los PRs de esta sesión se crean en draft. No hacer merge ni desplegar por esa instrucción.
- Empezar el PR siguiente y crear su rama solo cuando el usuario indique avanzar. Comprobar que las dependencias necesarias estén incorporadas a `main`; documentar la base cuando se trabaje con PRs apilados autorizados.
- Cada fila es un PR de un solo repositorio. Los cambios que cruzan API/mobile están separados para que la dependencia y el orden de despliegue sean explícitos.
- Si una decisión pendiente condiciona una implementación, resolverla antes de ese PR; no inventar plazos, ofertas ni garantías de recuperación.

## Secuencia

| PR | Repo | Cambio y criterio de terminado | Dependencias / decisiones |
| --- | --- | --- | --- |
| 1 | API | **Conservar invitados inactivos.** Quitar selección/borrado por inactividad, ofrecer `purge:deleted` para cuentas marcadas, dejar alias seguro del comando anterior y rechazar `--days`. Actualizar documentación y probar invitados antiguos con/sin compras, dry-run, corte de tombstones y fallos. | Primero. Conserva el proceso existente de tombstones; la recuperación de proveedores se completa en PR 2. No requiere migración. |
| 2 | API | **Borrado recuperable sin sesión.** Persistir etapas/estado de eliminación, recuperar fallos de Auth/RevenueCat/base desde job, conservar referencia hasta confirmar etapas y exponer evidencia de intentos/antigüedad/errores para operación. Probar pérdida de sesión, reinicio y errores en cada proveedor. | PR 1. Confirmar configuración efectiva de RevenueCat/Supabase y política operativa; las constantes actuales no son plazos públicos aprobados. |
| 3a | API / función Supabase | **Revocación Apple al borrar.** Endpoint de captura, token cifrado, verificación de identidad, revocación recuperable antes de Auth y exportación de metadatos. | PR 2. Configuración/despliegue y evidencia de revocación real pendientes. |
| 3b | Mobile | **Captura y reautorización Apple.** Enviar el código nativo tras autenticarse, usar la sesión secundaria en colisiones, permitir reautorizar y detectar revocación confirmada. | PR 3a desplegado antes de liberar mobile. Verificación en iOS físico pendiente. |
| 4 | API | **Residuos y exportación.** Tratar `account_resolutions`, reportes y webhooks tardíos según conservación aprobada; evitar reconstruir identificadores innecesarios después del borrado. Ajustar exportación/redacción/paginación cuando haga falta. Probar retención, tareas pendientes y datos de terceros. | PR 2. Decisión del usuario: conservar reportes y resoluciones mientras sus plazos sigan pendientes. Exportar metadatos protegidos y corregir webhooks; conservación de logs/backups/proveedores sigue pendiente. |
| 5 | Mobile | **Borrado de invitados y aviso de cancelación.** Mostrar eliminar para invitados y vinculados, separar salir de eliminar, describir progreso/saldos/residuos y acceso a gestión de suscripciones. Probar éxito/fallo y retorno tras borrar. | PR 2; texto de conservación coordinado con PR 4. El retorno se adapta nuevamente al arranque de PR 9. |
| 6 | Mobile | **Centro legal y soporte.** Enlaces ES/EN a términos, privacidad, comunidad, compras, soporte y eliminación desde un acceso inicial y ajustes; comprobar configuración de release y acceso sin sesión. | Rutas/versión documental disponibles. Debe poder usarse fuera de Auth/Ads/Purchases para integrarlo al PR 9. Créditos finales se incorporan en PR 16. |
| 7 | API | **Contrato y registro de elegibilidad/aceptación.** Registro mínimo de categoría 18+, versión de términos/reglas, idioma y fecha de servidor; endpoints idempotentes, política vigente y tratamiento de exportación/borrado/cambio de identidad. | PR 4 y versión/idiomas legales definidos. Compatible con clientes anteriores durante la transición: no activar aún el bloqueo social de PR 10. No guardar DNI ni fecha de nacimiento completa por defecto. |
| 8 | Mobile | **Estabilizar pruebas nativas de los flujos afectados.** Resolver el log asíncrono Expo detectado, con pruebas ejecutadas hasta exit 0 y mocks que no oculten fallos de producto. | Antes del trabajo sustancial en onboarding/mobile. Si el problema ya desapareció en `main`, registrar la ejecución limpia sin un PR vacío. |
| 9 | Mobile | **Arranque 18+ y aceptación explícita.** Flujo neutral, rechazo/edad desconocida, acceso legal/soporte y aceptación versionada. Ordenar inicio de Auth/Ads/RevenueCat/Sentry según decisiones por finalidad; adaptar sesiones existentes, eliminación, recuperación y colisiones. | PR 5–8. Definir información/fundamentos/consentimientos por finalidad. Validar tráfico y UMP/ATT en release; no suponer consentimiento obligatorio para todo SDK. |
| 10 | API | **Exigir elegibilidad y aceptación antes de publicar.** Activar controles backend para nombres/grupos y demás operaciones afectadas. Probar llamadas directas, versiones obsoletas, clientes existentes y excepciones para acceso legal/borrado/soporte. | PR 7 y cliente PR 9 disponible. Acordar activación y transición; el despliegue de este control requiere coordinar la versión mobile. |
| 11 | API | **Denuncias de grupos.** Destino jugador/grupo, captura de contenido denunciado, acceso autorizado y límites; mantener el contrato de denuncias de jugadores. | PR 10. No exponer denunciantes a otros jugadores. |
| 12 | Mobile | **Denunciar grupos desde la app.** Entrada visible, razones, envío/confirmación/errores y contexto correcto del grupo. Conservar denuncias/bloqueos de jugadores. | PR 11 y PR 8. |
| 13 | API | **Acciones y registro de moderación.** Mecanismo restringido para resolver reportes, retirar/renombrar contenido y aplicar restricciones con historial de operador/decisión. Pruebas de efectividad y permisos. | PR 11. Definir procedimiento, avisos y revisión. Evaluar el backoffice existente antes de elegir interfaz; si requiere cambios en ese repo, incorporarlos como PR separado al plan. |
| 14 | Mobile | **Compras invitadas: advertencia y recuperación.** Informar antes de comprar, facilitar vinculación y explicar restauración/saldo. Cubrir pérdida de sesión, cambios de identidad y compras conservadas, sin prohibir las compras invitadas aprobadas. | PR 9. Decidir recuperación de saldos y verificar configuración RevenueCat/tiendas. Si hace falta una operación backend de transferencia, agregar un PR API previo con control contra doble acreditación. |
| 15 | Mobile | **Ofertas y cancelación por plataforma.** Conservar duración/ciclos de la oferta y describir trial/intro/precio posterior reales, incluido anual. Reemplazar texto universal de 24 horas por condiciones verificadas. | Oferta efectiva y modalidades de tiendas definidas. Pruebas de mensual/anual, elegibilidad y ausencia de promoción. |
| 16 | Mobile | **Marca y avisos de release.** Nombre público Daylo Games, acceso a créditos/avisos finales de recursos y dependencias distribuidas, sin cambiar IDs internos por la marca. | Inventario/licencias originales y build real revisados; URLs finales disponibles. |
| 17 | Mobile | **Reportar anuncios inapropiados.** Verificar qué aporta el SDK; si falta una vía utilizable, agregar reporte/soporte con contexto de anuncio apropiado, sin confundirlo con privacidad UMP. | PR 6 y PR 9, procedimiento de atención y verificación nativa. Si el SDK ya lo cubre, registrar evidencia sin un PR vacío. |
| 18 | Legal / configuración de release | **Textos finales y evidencia de lanzamiento.** Ajustar documentos al producto probado, publicar rutas/idiomas, configurar URLs y declaraciones de tiendas, resolver `app-ads.txt` y registrar recorridos release. | PRs anteriores y decisiones legales/operativas completas. Publicación, configuración externa y despliegues se realizan con autorización específica; este plan no los ejecuta. |

La lista se ajustará con lo que revele cada PR. Las tareas opcionales no justifican agregar código cuando una verificación demuestra que el funcionamiento ya está cubierto.

## Trabajo externo que acompaña los PRs

- Confirmar identidad/domicilio, plataformas, países habilitados, versiones documentales y términos revisados.
- Definir conservación por categoría, incluyendo compras, reportes, resoluciones, logs, soporte y backups; implementar y comprobar el job de borrado corregido con capacidad/alertas.
- Verificar Supabase/Render/Cloudflare/Sentry/AdMob/RevenueCat y tiendas: regiones, contratos, configuración, retención y borrado reales.
- Probar el buzón y el circuito de soporte/derechos/moderación con los operadores previstos.
- Completar licencias originales e inventario de recursos, dependencias y avisos de la build distribuida.
- Validar en dispositivos release primer uso, sesiones existentes, rechazo/revocación publicitaria, compras/restauración/cancelación, reportes, borrado y solicitud externa. Guardar evidencia mínima sin datos personales en este repositorio.

## Estado de ejecución

PR 1 publicado como draft [API #87](https://github.com/DayloGames/daylo-api/pull/87),
rama `fix/preserve-inactive-guests`. PR 2 publicado como draft
[API #88](https://github.com/DayloGames/daylo-api/pull/88), commit `14b0487`,
rama `fix/resumable-account-deletion` basada en la rama del #87.

Cambio 3 publicado en draft:
[API #89](https://github.com/DayloGames/daylo-api/pull/89), commit `1a6ae79`,
rama `fix/apple-token-revocation` sobre #88; y
[Mobile #155](https://github.com/DayloGames/daylo-mobile/pull/155), commit `0bd5ddb`,
rama `fix/apple-token-capture` desde `main` `524e8d1`. Se amplió el alcance a Mobile
porque el flujo nativo descartaba `authorizationCode`: la API no podía recuperar
tokens históricos desde un ID token Supabase. Incluye captura bajo la identidad
correcta, cifrado, revocación antes de Auth, reintentos, conservación durante
colisiones, metadatos de exportación y detección local de revocación.

Validación local del cambio 3: typecheck y ESLint de archivos afectados;
185 pruebas API de usuarios/configuración, 20 de comandos/función y 19 HTTP;
42 de integración con las migraciones sobre PostgreSQL 16 temporal; 781 pruebas
unitarias Mobile y 11 nativas de AuthProvider/acciones sociales (exit 0). Los 338 tests nativos existentes
pasan sus assertions, pero el proceso termina con exit 1 por un log tardío de
Expo. Se reprodujo el mismo error sobre `main` sin estos cambios: continúa
pendiente de PR 8.

La configuración/despliegue Supabase/Apple y la prueba en iOS físico siguen
pendientes. No se configura producción desde este cambio. El comportamiento
histórico sin token se registra como `unavailable`, permite borrar la cuenta y
muestra instrucciones de revocación manual; no se declara una revocación que
no pudo comprobarse. Detalles operativos en `daily-games-api/docs/apple-revocation.md`.

Cambio 4 publicado como [API #90](https://github.com/DayloGames/daylo-api/pull/90)
en draft, commit `bc8a09f`, rama `fix/deletion-residual-data`
sobre el commit `1a6ae79` del draft #89. El usuario confirmó que reportes y resoluciones deben conservarse
por ahora, sin plazos aprobados: no se agregó TTL ni borrado de esas categorías.

Incluye comprobación de cuenta viva bajo bloqueo transaccional para receipts,
membresías, grants y refunds; minimización de IDs históricos para cuentas
ausentes/eliminadas; exportación de metadatos de resoluciones y reportes propios
sin IDs ajenos, notas, nombres copiados ni datos de denunciantes; endpoint de
paginación con autorización por solicitante. La migración agrega índices y
minimiza receipts; conserva invitados inactivos y registros retenidos.

Validación: typecheck, ESLint/formato de archivos afectados y diff limpio;
207 tests de usuarios/billing, 16 del comando de borrado, 21 HTTP y 58 de
integración en PostgreSQL 16 temporal. Incluye carrera real del webhook contra
el tombstone, lectura del proveedor que termina después del borrado, reintentos,
redacción, paginación, retención tras purga y minimización histórica. La suite
HTTP conserva el warning de open handles de Jest, con exit 0.

Continúan pendientes los plazos/fundamentos por categoría, la revisión de
contenido sensible en solicitudes de acceso, los registros que excedan los
caps operativos, y conservación/borrado en proveedores/logs/backups. El rollout
debe drenar handlers antiguos de billing para que no reintroduzcan IDs después
del backfill. No se ejecutó la migración contra producción.

Validación del PR 1:

- `pnpm typecheck`: aprobado, después de regenerar el cliente Prisma por los cambios de esquema ya presentes en `main`.
- ESLint sin warnings y Prettier para los archivos TypeScript/package afectados; `git diff --check` aprobado.
- 16 pruebas unitarias del comando y 37 pruebas existentes de usuarios: aprobadas.
- 2 pruebas nuevas de integración contra PostgreSQL 16 temporal: aprobadas. Cubren invitados con saldo ganado/comprado, compras conservadas, cuenta vinculada, cascadas, dry-run, límite del lote y frontera de siete días.
- Arranque real de `pnpm purge:deleted --limit=1` en dry-run contra esa base: exit 0. Invocación real del alias con `--apply --days=90`: rechazo esperado, exit 1 antes de abrir conexiones.

No se aplicaron migraciones ni purgas a producción. La base temporal se creó con las migraciones existentes; este PR no agrega migraciones. La recuperación de proveedores se implementó después en PR 2; la evidencia anterior corresponde exclusivamente al PR 1.
