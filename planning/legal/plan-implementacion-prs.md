# Plan de implementación del cierre, PR por PR

Fecha: 8 de octubre de 2026. Basado en [plan-de-cierre.md](plan-de-cierre.md) y [revision-codigo-cierre.md](revision-codigo-cierre.md).

## Forma de trabajo acordada

- Trabajar un PR por vez, en una rama del repositorio correspondiente creada desde `main` actualizado.
- Al terminar cada cambio: mostrar alcance, validación, pendientes y listado de archivos modificados/nuevos; dejarlo sin commit ni push.
- Hacer commit, push y abrir PR con descripción cuando el usuario lo indique. Todos los PRs de esta sesión se crean en draft. No hacer merge ni desplegar por esa instrucción.
- Empezar el PR siguiente y crear su rama solo cuando el usuario indique avanzar. Comprobar que las dependencias necesarias estén incorporadas a `main`; no construir accidentalmente el siguiente PR sobre la rama anterior.
- Cada fila es un PR de un solo repositorio. Los cambios que cruzan API/mobile están separados para que la dependencia y el orden de despliegue sean explícitos.
- Si una decisión pendiente condiciona una implementación, resolverla antes de ese PR; no inventar plazos, ofertas ni garantías de recuperación.

## Secuencia

| PR | Repo | Cambio y criterio de terminado | Dependencias / decisiones |
| --- | --- | --- | --- |
| 1 | API | **Conservar invitados inactivos.** Quitar selección/borrado por inactividad, ofrecer `purge:deleted` para cuentas marcadas, dejar alias seguro del comando anterior y rechazar `--days`. Actualizar documentación y probar invitados antiguos con/sin compras, dry-run, corte de tombstones y fallos. | Primero. Conserva el proceso existente de tombstones; la recuperación de proveedores se completa en PR 2. No requiere migración. |
| 2 | API | **Borrado recuperable sin sesión.** Persistir etapas/estado de eliminación, recuperar fallos de Auth/RevenueCat/base desde job, conservar referencia hasta confirmar etapas y exponer evidencia de intentos/antigüedad/errores para operación. Probar pérdida de sesión, reinicio y errores en cada proveedor. | PR 1. Confirmar configuración efectiva de RevenueCat/Supabase y política operativa; las constantes actuales no son plazos públicos aprobados. |
| 3 | API / función Supabase | **Revocación Apple al borrar, si falta.** Verificar integración real y agregar revocación recuperable si no está cubierta. Completar pruebas del proveedor y la función desplegada. | PR 2. Credenciales/configuración Apple y evidencia Supabase. Si ya está cubierto, registrar evidencia y cerrar esta tarea sin un PR vacío. |
| 4 | API | **Residuos y exportación.** Tratar `account_resolutions`, reportes y webhooks tardíos según conservación aprobada; evitar reconstruir identificadores innecesarios después del borrado. Ajustar exportación/redacción/paginación cuando haga falta. Probar retención, tareas pendientes y datos de terceros. | PR 2. Definir plazos por categoría, alcance del acceso y tratamiento de logs/backups/proveedores. No borrar resoluciones aún pendientes. |
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

PR 1 implementado y listo para revisión en `daily-games-api`, rama `fix/preserve-inactive-guests`, desde `main` actualizado a `6cbfeb2`. `daily-games-mobile` está en `main` actualizado a `524e8d1`. El usuario autorizó commit, push y publicación de PRs draft para este cambio y sus documentos de revisión/planificación. No se inició el PR 2 ni se creó rama para cambios siguientes.

Validación del PR 1:

- `pnpm typecheck`: aprobado, después de regenerar el cliente Prisma por los cambios de esquema ya presentes en `main`.
- ESLint sin warnings y Prettier para los archivos TypeScript/package afectados; `git diff --check` aprobado.
- 16 pruebas unitarias del comando y 37 pruebas existentes de usuarios: aprobadas.
- 2 pruebas nuevas de integración contra PostgreSQL 16 temporal: aprobadas. Cubren invitados con saldo ganado/comprado, compras conservadas, cuenta vinculada, cascadas, dry-run, límite del lote y frontera de siete días.
- Arranque real de `pnpm purge:deleted --limit=1` en dry-run contra esa base: exit 0. Invocación real del alias con `--apply --days=90`: rechazo esperado, exit 1 antes de abrir conexiones.

No se aplicaron migraciones ni purgas a producción. La base temporal se creó con las migraciones existentes; este PR no agrega migraciones. La recuperación de RevenueCat y demás etapas del borrado sigue en PR 2.
