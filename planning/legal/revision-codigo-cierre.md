# Revisión de código para el plan de cierre

Fecha: 8 de octubre de 2026. Referencia: [plan-de-cierre.md](plan-de-cierre.md).

Se revisaron `daily-games-mobile` en `cba649a` y `daily-games-api` en `5e00bae`, sin cambios locales al comenzar. Son los mismos commits citados por el plan. Esta revisión contrasta el código con las decisiones del plan; no comprueba producción ni revalida requisitos jurídicos. No se accedió a credenciales, consolas ni datos de usuarios. No se modificó código ni se ejecutaron purgas, migraciones o compras.

## Resultado

**Falta implementación para cerrar el producto.** Los pendientes principales del plan siguen abiertos. Se puede avanzar con preparación documental y configuración, pero el código actual no permite dar por cumplidos el acceso 18+, la aceptación legal, la conservación de invitados ni el borrado completo recuperable.

Los detalles más relevantes añadidos por esta revisión son:

- La purga elimina el registro local sin reintentar el borrado del cliente RevenueCat. Una eliminación interrumpida puede perder su referencia local dejando datos en ese proveedor.
- Las denuncias dentro de grupos son denuncias de jugadores; no existe un destino de denuncia para el grupo o su nombre.
- `account_resolutions` conserva identificadores sin relaciones que permitan su borrado en cascada y no aparece en la exportación revisada.
- Webhooks posteriores al borrado pueden volver a registrar el identificador de la cuenta en `revenuecat_events`, aunque no activen beneficios.
- La oferta introductoria pierde duración/ciclos al transformarse para la UI y siempre se presenta como «primer mes», también en modalidad anual.

## Cambios de código prioritarios

### 1. Conservar invitados inactivos — alta, API

**Evidencia:** `daily-games-api/scripts/purge-stale-guests.ts:123` selecciona invitados con `isAnonymous=true`, `linkedAt=null`, `deletedAt=null` y última actividad anterior al umbral de 90 días. En `:164` los combina con las eliminaciones solicitadas y en `:178` elimina sus filas. No filtra compras o saldo. El límite predeterminado es 1.000 por cada población, no 1.000 entre ambas.

**Consecuencia:** ejecutar el comando con `--apply` contradice la decisión de no eliminar cuentas ni saldos por inactividad, también para invitados con compras. No hace falta introducir vencimiento de monedas: el problema encontrado es el borrado de la cuenta que las contiene.

**Trabajo:** quitar la selección de invitados vivos del proceso de lanzamiento; mantener un proceso explícito para las cuentas cuya eliminación fue solicitada. Actualizar el nombre/descripción del comando y `docs/deployment.md:126`, que todavía recomienda programar `purge:guests --apply` con el comportamiento anterior.

**Cierre:** un invitado antiguo con saldo comprado y otro con saldo ganado sobreviven al job; una cuenta con eliminación solicitada completa sus etapas. Comprobar la configuración de cualquier job existente antes de activarlo o reutilizarlo.

### 2. Completar eliminaciones sin depender de la sesión — alta, API

**Evidencia:** `src/modules/users/users.service.ts:1471` marca `deletedAt`, borra Supabase Auth, borra RevenueCat y después ejecuta la purga parcial. Hay reintentos idempotentes y pruebas de fallos de Supabase y purga local. `scripts/purge-stale-guests.ts:175` solo llama a Supabase y elimina `users`; no llama a RevenueCat ni comprueba que las etapas anteriores hayan terminado.

**Caso concreto:** Auth se elimina, RevenueCat devuelve error, y el cliente abandona el flujo o pierde/vence su token. El registro queda marcado. Si el job lo elimina después de siete días, desaparece la referencia local sin haber completado RevenueCat. Si no corre ningún job, los datos pendientes quedan sin completar por esa vía. No se encontró un worker de recuperación independiente de la sesión.

**Trabajo:** persistir etapas o una tarea de eliminación, recuperar fallos desde un worker/job y purgar la referencia final solo después de confirmar las etapas necesarias. Aprovechar la idempotencia existente. Registrar último error, intentos y antigüedad para operación/alertas. Cubrir fallos de RevenueCat y pérdida de sesión, además de Supabase y base de datos.

**Configuración adicional:** Supabase Admin puede quedar sin configurar y el endpoint responderá 503. `src/modules/billing/revenuecat.client.ts:172` considera éxito no tener clave secreta; para un entorno que usa RevenueCat, comprobar que esa ausencia no oculte un proveedor que sí conserva datos. El cron no está definido en `render.yaml` ni en los workflows revisados; los documentos lo señalan pendiente. Esto no acredita el estado de una consola externa.

**Cierre:** después de cada fallo simulado, la eliminación termina sin otra acción del usuario y queda evidencia de cada proveedor. Frecuencia, capacidad y plazo máximo deben comprobarse con el job real; las constantes 7/90 días no bastan para prometer plazos.

### 3. Implementar elegibilidad 18+ y ordenar el arranque — alta, mobile y API

**Evidencia:** `daily-games-mobile/app/_layout.tsx:33` inicia Sentry al importar el módulo. En `:104` monta Ads/Auth y posteriormente Purchases. `src/auth/AuthContext.tsx:58` crea un invitado automáticamente; `src/ads/AdsProvider.tsx:40` solicita UMP al arrancar; `src/purchases/PurchasesProvider.tsx:161` configura RevenueCat con el identificador Supabase. No se encontró pantalla/estado de elegibilidad ni registro de categoría de edad en el modelo `User` o controles de edad en los endpoints revisados.

**Trabajo:** implementar el flujo neutral aprobado en [edad-y-consentimiento.md](edad-y-consentimiento.md), con acceso inicial a legal/soporte y tratamiento explícito de menores y edad desconocida. Ordenar creación de cuenta e inicialización de SDK conforme a la información, elegibilidad y fundamentos decididos por finalidad. Incluir las sesiones existentes y los caminos que crean nuevos invitados tras borrar o perder una cuenta. Si se persiste elegibilidad, validarla en servidor en las operaciones afectadas; una bandera local no protege llamadas directas.

No se propone pedir DNI ni almacenar fecha de nacimiento completa. La autodeclaración y su eventual registro describen una decisión de producto, no una verificación de identidad.

**Ya existe:** UMP consulta `canRequestAds` antes de inicializar anuncios y contempla fallo de primera consulta. Hay formulario de opciones publicitarias cuando UMP lo requiere. `app.json` configura `delayAppMeasurementInit` y el texto de tracking en ambos idiomas. Esto es una base útil; no resuelve la elegibilidad ni demuestra qué transmite una build nativa.

**Cierre:** primer uso, menor, edad desconocida, adulto y sesiones preexistentes probados en release, con observación de tráfico antes/después. Verificar UMP/ATT y configuración real, sin confundirlos con aceptación de términos.

### 4. Registrar aceptación y permitir acceso legal estable — alta, mobile y API

**Evidencia:** `daily-games-mobile/src/config/env.ts:14` permite URLs opcionales e ignora URLs inválidas. `src/store/BalanceStoreScreen.tsx:243` solo muestra enlaces si existen; en las rutas/pantallas revisadas no se encontró un centro legal/soporte. El esquema y API no incluyen registro de aceptación con versión/idioma/fecha.

`daily-games-api/src/modules/users/users.service.ts:600` permite editar nombres sin ese control. `src/modules/groups/groups.service.ts:258` exige nombre para crear grupo; `UsersService.requireUsername` comprueba el nombre, no aceptación o elegibilidad.

**Trabajo:** acceso inicial y desde ajustes a términos, privacidad, comunidad, compras, soporte, eliminación y créditos. Configurar rutas finales por idioma y comprobarlas en la build de lanzamiento; evitar que un error de configuración quite silenciosamente enlaces necesarios. Registrar aceptación explícita con versión, idioma y fecha de servidor, separada de publicidad, y comprobarla antes de publicar nombres/crear grupos en backend. Definir qué ocurre con cuentas existentes, nuevas versiones y recuperación/colisión de cuentas.

**Cierre:** sin aceptación vigente no se puede publicar contenido, tampoco llamando directamente a la API. Aceptar registra la evidencia correcta; reintentar no duplica el acto. Invitados y personas aún no elegibles pueden consultar legal/soporte. Cuando se agregue el registro, incluirlo en la política de conservación y en la exportación/borrado correspondientes.

### 5. Habilitar borrado de invitados y explicar sus efectos — alta, mobile

**Evidencia:** `src/profile/AccountSettingsScreen.tsx:160` oculta simultáneamente salir y eliminar para anónimos. La API `DELETE /users/me` no impone esa distinción: la limitación encontrada está en la UI.

`src/i18n/locales/es.json:1261` y su equivalente inglés prometen «todos sus datos», mientras `UsersService.purgeDomainRows` conserva temporalmente sesiones, billeteras, ledger, usos de pistas y compras. Los reportes sobreviven y hay otros residuos descritos más abajo. La confirmación no advierte que borrar no cancela suscripciones. La gestión de suscripción existe en la tienda (`BalanceStoreScreen.tsx:237`), pero no está junto al borrado.

**Trabajo:** separar la condición de salir de la de eliminar y permitir iniciar borrado a invitados. Mostrar efectos sobre progreso/saldo, residuos/plazos definidos, y advertencia/acceso a cancelación de suscripciones. Revisar el retorno actual a un invitado nuevo (`AccountSettingsScreen.tsx:69`) para que sea coherente con el nuevo arranque legal y no cree otra cuenta automáticamente contra lo informado.

**Cierre:** invitados y vinculados pueden iniciar y completar la operación. Probar fallos, pérdida de sesión y usuario con suscripción activa, con texto ES/EN que coincida con el proceso real.

### 6. Denunciar grupos y ejecutar acciones de moderación — alta, mobile y API; parte operativa

**Evidencia:** `src/modules/moderation/moderation.controller.ts:38` solo acepta `friendCode`, razón y nota. `ModerationService.report` guarda una denuncia de jugador y copia su nombre. En mobile, `app/(tabs)/friends/group/[groupId]/index.tsx:80` reporta al miembro seleccionado, no al grupo. No se encontró endpoint/modelo de denuncia del grupo o su nombre.

`prisma/schema.prisma:1096` tiene reportes sin estado de resolución, decisión u operador. La búsqueda dirigida no encontró suspensión de cuenta ni una restricción de moderación aplicada por los servicios. Hay validación de nombres, bloqueo entre jugadores y límites de frecuencia; no equivalen a una decisión operativa del equipo.

**Trabajo:** permitir denunciar un grupo conservando identificador y nombre relevante. Elegir un mecanismo acotado y autorizado para revisar reportes, retirar/renombrar contenido y restringir reincidencia, con registro de acción y revisión. Si requiere suspensión, el servidor debe hacerla efectiva, no solo ocultarla en mobile. El backoffice queda fuera de esta revisión: puede servir de interfaz, pero hay que comprobar sus capacidades concretas y permisos.

No es imprescindible construir un backoffice nuevo si un procedimiento con herramientas existentes realiza y documenta esas acciones. Sí hay un hueco concreto en las denuncias de grupos dentro de los dos repositorios revisados.

**Cierre:** pruebas de denuncia de jugador y grupo, acción efectiva, aviso y revisión con los operadores previstos por el plan. La atención y sus plazos necesitan una prueba operativa además del código.

## Otros pendientes para el cierre

### Conservación, exportación y datos residuales — alta para definir; implementación según categoría

- `account_resolutions` (`prisma/schema.prisma:1023`) conserva ambos IDs sin claves foráneas. No se encontró limpieza por eliminación/antigüedad ni inclusión en `UserExport`. Incorporar la categoría al inventario; definir su necesidad, plazo, limpieza y acceso con protección de datos de la otra cuenta. No borrar tareas pendientes que todavía se necesitan para recuperar una resolución.
- `user_reports` (`schema.prisma:1096`) conserva IDs, nombre y nota sin cascada. Su supervivencia es deliberada; no se encontró mecanismo de expiración. Definir conservación y acceso con redacción cuando corresponda, sin revelar denunciantes al denunciado.
- `BillingService.handleEvent` (`src/modules/billing/billing.service.ts:145`) guarda `appUserId` incluso cuando el evento se ignora por no existir cuenta viva. Una entrega posterior a `purgeDomainRows` puede reintroducir ese ID en `revenuecat_events`; esa tabla tampoco tiene cascada. Definir retención/minimización y cubrir el webhook tardío.
- Sentry recibe identificadores: mobile los agrega a logs de Auth; API usa `Sentry.setUser` y atributos en `src/observability/sentry-user.interceptor.ts:25`. Hay reducción de cuerpos/headers en la API, pero el borrado revisado no gestiona Sentry, logs externos, soporte ni backups. Determinar qué se resuelve mediante configuración y procedimiento y qué requiere automatización.
- La exportación ya existe y señala colecciones truncadas (`exportData:1233`). Verificar cómo soporte entrega datos completos cuando supera el límite y los conservados por otros proveedores. Un test de simetría entre exportación y purga no descubre por sí solo categorías excluidas de ambas.

### Compras de invitados y recuperación — alta, mobile; backend según decisión

Las compras no exigen vincular identidad. Hay compra/restauración, sincronización y resolución de colisiones, pero no se encontró advertencia específica previa a comprar como invitado ni un flujo de recuperación de su saldo al perder sesión.

`PurchasesProvider` identifica también al invitado con su UUID. `BillingService.grantPurchases:286` no vuelve a acreditar una transacción ya registrada: **restaurar no equivale a recuperar el saldo comprado de una cuenta invitada perdida**. Definir la recuperación y presentar sus límites antes de comprar, con acceso a vinculación sin prohibir la compra invitada aprobada. Confirmar el comportamiento efectivo de transferencias/restauración de RevenueCat y tiendas. Si la recuperación elegida incluye transferir saldos mediante soporte, implementar la operación necesaria y evitar doble acreditación.

### Oferta introductoria y condiciones — media, mobile

`src/purchases/storeOffers.ts:59` conserva únicamente el precio introductorio. Pierde duración y ciclos. `BalanceStoreScreen.tsx:380` utiliza siempre `store.memberships.introOffer`, cuyo texto ES/EN dice «primer mes» y «/mes», incluso con la opción anual. `locales/es.json:1351` y EN usan una instrucción universal de 24 horas para ambas tiendas.

Conservar metadata suficiente para describir oferta/duración y precio posterior, o no mostrar una descripción específica hasta poder expresarla correctamente. Adaptar textos a la plataforma y oferta realmente habilitada. Ya existen precios de tienda, mensual/anual, elegibilidad introductoria consultada en iOS y gestión de suscripciones; conservar esas bases.

### Revocación Apple — verificación externa y posible implementación

La Edge Function (`supabase/functions/delete-user/index.ts:86`) solo llama a `supabase.auth.admin.deleteUser`. La búsqueda revisada no encontró intercambio/revocación propia de tokens Apple; `docs/roadmap.md:8` también lo marca pendiente. `socialAuth.ts` tiene login Apple, pero no un flujo propio de revocación. Verificar qué cubre la integración Supabase efectiva. Si no lo cubre, completar ese paso en el proceso recuperable de borrado. No concluir que ocurre por el solo hecho de eliminar Auth.

### Créditos, avisos y marca — media, assets/configuración/UI

No se encontró acceso a créditos/avisos desde las pantallas revisadas. Reunir el inventario de release, avisos de dependencias incluidas y recursos distribuidos, usando [inventario-licencias.md](inventario-licencias.md); agregar acceso a la versión final. La comprobación de fuentes/licencias originales es una tarea separada del desarrollo de esa pantalla.

`app.json:3` todavía define el nombre «Daylo», frente a la marca exacta aprobada «Daylo Games». Alinear el nombre público de app y fichas; los IDs internos no requieren renombrarse por ese motivo.

### Reportes de anuncios — gap de producto a resolver para cierre

En los providers/hooks/pantallas revisados no se encontró una vía propia para reportar anuncios inapropiados. El documento de edad pide verificar esa posibilidad también en 18+. Comprobar primero si la build/SDK aporta una vía utilizable; si no, agregar una entrada de soporte/reporte con contexto suficiente para investigar el anuncio. No confundir cambiar preferencias UMP con reportar una creatividad.

## Trabajo que depende de configuración o evidencia externa

Estos puntos no se cierran agregando por sí solos un endpoint:

- URLs HTML finales y acceso sin login desde un teléfono; configuración efectiva de enlaces en la build y fichas.
- Países/plataformas de lanzamiento y audiencia declarada; no se deduce de los identificadores iOS/Android.
- Catálogo, productos, ofertas, grupos de suscripción, transferencias y credenciales de RevenueCat. `render.yaml` declara `BILLING_ENABLED=false`; el valor real desplegado no se inspeccionó.
- UMP/ATT reales y transmisiones de cada SDK en una build release; manifiestos y declaraciones App Privacy/Data safety del binario distribuido.
- Programación del job de borrado corregido, capacidad, alertas, retención de proveedores y comportamiento de backups.
- `app-ads.txt` en la raíz del hostname correspondiente: publicación del sitio, no cambio de API/mobile.
- Contratos/regiones/transferencias, identidad/domicilio público, condiciones jurídicas y atención efectiva del buzón.

## Orden propuesto de implementación

1. **Conservación y borrado:** corregir selección del job y documentación; completar recuperación independiente de sesión, proveedores y datos residuales; habilitar borrado invitado y corregir avisos.
2. **Arranque legal:** acceso a documentos/soporte, elegibilidad 18+, inicio de SDK según decisiones, aceptación versionada y control backend. Incorporar cuentas existentes y cambios de identidad.
3. **Social:** denuncia de grupos, acciones de moderación y procedimiento verificable.
4. **Monetización:** advertencia/recuperación de invitados, cancelación, ofertas según duración/plataforma y webhooks posteriores al borrado.
5. **Release:** nombre público, créditos/avisos, URLs definitivas, configuración real y recorrido nativo completo con evidencia.

Los pasos 1–4 dan información necesaria para terminar los textos sin prometer un funcionamiento que el producto todavía no tiene.

## Verificación realizada

Se ejecutaron suites locales existentes, con proveedores simulados:

| Proyecto | Selección | Resultado |
| --- | --- | --- |
| API | Ciclo de vida, exportación, cliente Supabase Admin, moderación y cliente RevenueCat | 5 suites, 48 tests aprobados; exit 0 |
| Mobile | PurchasesProvider, gateway RevenueCat, pantalla de tienda, configuración de URLs, hooks sociales y manejo de cuenta eliminada | 6 suites, 49 tests aprobados, pero **exit 1** por `Cannot log after tests are done`, asociado a carga asíncrona de `ExpoModulesCoreJSLogger` |

El primer intento falló por acceso de Watchman a su estado fuera del sandbox. Se reintentó con autorización y `--watchman=false`; los resultados anteriores corresponden al reintento. El fallo final de mobile se conserva como pendiente del harness de pruebas, sin atribuirle por sí solo un fallo de la app release.

Las suites API muestran que parte del proceso de borrado se puede reintentar, pero no demuestran la recuperación por job, la purga real con permisos de producción, el borrado de proveedores ni los flujos nativos. No se ejecutó la suite completa ni integración contra base de datos, y no se añadió código de pruebas en esta revisión.
