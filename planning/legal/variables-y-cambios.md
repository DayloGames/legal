# Registro de valores y datos cambiantes

Interno. Revisión inicial: 2 de octubre de 2026. Este registro cubre los borradores de `planning/legal/public/`, el plan de integración móvil y los valores del producto que pueden terminar en ayuda, tiendas o políticas. **No es una configuración que modifique la app automáticamente.** El código, las consolas de proveedores y las decisiones aprobadas siguen siendo las fuentes de verdad indicadas en cada caso.

Estados: **código** = observado en esta revisión, sujeto a verificación en la versión distribuida; **pendiente** = decidir o comprobar antes de publicar; **externo** = determinado por ley, tienda o licencia, no editable por nosotros.

## Reglas numéricas del producto

| Dato | Valor observado | Fuente primaria | Texto/superficies a revisar si cambia |
| --- | --- | --- | --- |
| Antigüedad máxima para usar una invitación | 7 días desde la creación de la cuenta invitada | [InvitesService](https://github.com/guidobotta/daily-games-api/blob/main/src/modules/invites/invites.service.ts), `NEW_ACCOUNT_DAYS` | [Compras §8](public/purchases.es.md), [app ES](https://github.com/guidobotta/daily-games-mobile/blob/main/src/i18n/locales/es.json), [app EN](https://github.com/guidobotta/daily-games-mobile/blob/main/src/i18n/locales/en.json), futuras FAQ y ofertas de referidos. |
| Referidos recompensables por mes | 5 referidos distintos; el límite afecta recompensas, no el registro de la invitación. Verificar el corte/calendario usado en producción. | [ReferralMilestonesService](https://github.com/guidobotta/daily-games-api/blob/main/src/modules/invites/referral-milestones.service.ts), `MONTHLY_REWARDED_REFERRALS` y `startOfMonth()` | [Compras §8](public/purchases.es.md), pantallas de invitación ES/EN y futuras FAQ. La app recibe el límite de la API, pero también hay texto explicativo. |
| Racha del tercer hito de referido | 3 días desde la vinculación | [referral-rewards.ts](https://github.com/guidobotta/daily-games-api/blob/main/src/modules/invites/referral-rewards.ts), `REFERRAL_STREAK_DAYS` | [Compras §8](public/purchases.es.md), descripción de hitos ES/EN y futuras FAQ. |
| Premios por hito de referido | 20 monedas al vincular; 3 tokens por primer día completo; 80 monedas por la racha. No figuran como cantidades fijas en el borrador público actual. | [referral-rewards.ts](https://github.com/guidobotta/daily-games-api/blob/main/src/modules/invites/referral-rewards.ts), `REFERRAL_REWARDS` | Pantalla de invitación/API, futuras FAQ, promociones y cualquier texto público que anuncie importes. No duplicar cantidades si la UI ya las recibe de API. |
| Nombre de usuario | 3–20 caracteres; espera de 24 horas entre cambios | [username.ts](https://github.com/guidobotta/daily-games-api/blob/main/src/modules/users/username.ts), `USERNAME_MIN_LENGTH`, `USERNAME_MAX_LENGTH`, `USERNAME_CHANGE_COOLDOWN_MS` | [Comunidad §2](public/community.es.md), validación y mensajes ES/EN. |
| Nombre de grupo | 3–40 caracteres | [group-name.ts](https://github.com/guidobotta/daily-games-api/blob/main/src/modules/groups/group-name.ts), `GROUP_NAME_MIN_LENGTH`, `GROUP_NAME_MAX_LENGTH` | [Comunidad §2](public/community.es.md), formularios y mensajes ES/EN. |
| Capacidad de grupos | 50 miembros por grupo; 20 grupos por usuario. Aún no está expresado como cifra en el borrador público. | [groups.service.ts](https://github.com/guidobotta/daily-games-api/blob/main/src/modules/groups/groups.service.ts), `MAX_GROUP_MEMBERS`, `MAX_GROUPS_PER_USER` | Ayuda/FAQ y mensajes de error de grupos si se decide explicitar los límites. |
| Nota de reporte | Hasta 1.000 caracteres; cifra interna, no publicada en comunidad. | [moderation.controller.ts](https://github.com/guidobotta/daily-games-api/blob/main/src/modules/moderation/moderation.controller.ts), `MAX_NOTE_LENGTH` | Formulario de reporte, mensajes y futura FAQ si se anuncia el límite. |

Los números de recompensas, grupos y reportes son valores de producto. Al cambiarlos, revisar además las pruebas y el comportamiento del backend; cambiar solo la página legal dejaría la app incoherente.

## Compras, suscripciones y publicidad

| Dato | Valor/estado actual | Fuente primaria | Revisar si cambia |
| --- | --- | --- | --- |
| Planes y períodos | Calm y Pro; variantes mensual y anual. Beneficios descritos en el anexo, sujetos a confirmar con tiendas y RevenueCat. | [membership.ts](https://github.com/guidobotta/daily-games-api/blob/main/src/modules/billing/membership.ts), [billing.md](https://github.com/guidobotta/daily-games-api/blob/main/docs/billing.md), consolas de App Store/Google Play/RevenueCat | [Compras §3–5](public/purchases.es.md), [Términos §6](public/terms.es.md), [Soporte](public/support.es.md), textos ES/EN de tienda, fichas de tiendas y ofertas. |
| Packs | 6 productos de monedas y 6 de tokens. Cantidades actuales: monedas 600, 1.500, 4.000, 9.000, 20.000, 50.000; tokens 5, 15, 40, 90, 200, 500. El código las llama **provisorias**. | [store-catalog.ts](https://github.com/guidobotta/daily-games-api/blob/main/src/modules/billing/store-catalog.ts), `STORE_PRODUCTS` | Catálogo servido por API, pantallas, promociones y cualquier futura cifra publicada. Los IDs de producto son slots estables; el tamaño del pack puede cambiar sin renombrar el ID. |
| Precios, monedas locales, impuestos, pruebas y promociones | Variables por tienda, región, producto y momento; no hay precios fijos en los documentos. | App Store Connect, Google Play Console y RevenueCat; valor mostrado por el SDK | Pantalla de compra, metadatos de tienda, [Compras §1/3/4](public/purchases.es.md) y soporte. No introducir una tabla manual de precios en la política. |
| Texto de cancelación «24 horas» | Aparece en el descargo ES/EN de la **app** para ambas tiendas; el anexo público lo señala como pendiente de validación por plataforma. No tratarlo como regla universal aprobada. | [app ES](https://github.com/guidobotta/daily-games-mobile/blob/main/src/i18n/locales/es.json), [app EN](https://github.com/guidobotta/daily-games-mobile/blob/main/src/i18n/locales/en.json), términos vigentes de cada tienda | [Compras §4](public/purchases.es.md), oferta y texto móvil antes de distribuir. |
| Oferta «primer mes» | Texto fijo ES/EN de la app cuando existe `introPrice`; aún hay que verificar duración y modalidad real, especialmente la variante anual. | [BalanceStoreScreen.tsx](https://github.com/guidobotta/daily-games-mobile/blob/main/src/store/BalanceStoreScreen.tsx), [app ES](https://github.com/guidobotta/daily-games-mobile/blob/main/src/i18n/locales/es.json), RevenueCat/tiendas | Oferta en app, [Compras §3–4](public/purchases.es.md), metadatos/promociones. |
| Efecto de Calm/Pro sobre anuncios | Calm quita interstitials; los rewarded optativos continúan. Pro incorpora Calm y beneficios de acceso. | [membership.ts](https://github.com/guidobotta/daily-games-api/blob/main/src/modules/billing/membership.ts), configuración/compilación final de ads | [Compras §3/7](public/purchases.es.md), [Términos §6](public/terms.es.md), [Privacidad §7](public/privacy.es.md), tienda y ayuda. |
| Vencimiento de saldos comprados | No se observó vencimiento programado; regla contractual aún **pendiente**. | Código de wallet/billing y decisión comercial/jurídica | [Compras §2](public/purchases.es.md), cierres de cuenta/inactividad y mensajes comerciales. |

## Conservación, borrado y derechos

**No convertir umbrales técnicos en promesas al público.** El script de purga necesita ejecución, capacidad, seguimiento y tratamiento de proveedores para sostener un plazo real de eliminación.

| Dato | Código observado / estado | Fuente primaria | Documento/superficie a revisar |
| --- | --- | --- | --- |
| Invitados inactivos | Elegibles para purga tras **90 días** por defecto; `--days` lo modifica. Ejecución periódica no verificada. | [purge-stale-guests.ts](https://github.com/guidobotta/daily-games-api/blob/main/scripts/purge-stale-guests.ts), `DEFAULT_INACTIVE_DAYS` | [Inventario](data-inventory.md), [Privacidad §9](public/privacy.es.md), [Eliminación](public/delete-account.es.md), soporte. Decidir plazo aprobado y proceso real. |
| Cuenta eliminada / tombstone | Elegible tras **7 días** en el script; conserva filas vinculadas hasta la purga. No es garantía de eliminación a los siete días. | [purge-stale-guests.ts](https://github.com/guidobotta/daily-games-api/blob/main/scripts/purge-stale-guests.ts), `TOMBSTONE_DAYS` | [Inventario](data-inventory.md), [Privacidad §9](public/privacy.es.md), [Eliminación](public/delete-account.es.md) y texto móvil de confirmación. |
| Capacidad de purga | **1.000** cuentas por ejecución por defecto; parámetro `--limit` modificable. Afecta cuánto tarda en procesarse una cola. | [purge-stale-guests.ts](https://github.com/guidobotta/daily-games-api/blob/main/scripts/purge-stale-guests.ts), `DEFAULT_LIMIT` | Plan operativo, alertas y cualquier plazo de eliminación que se prometa. |
| Exportación de datos | Hasta **10.000 filas por colección** en respuesta API; señala truncamiento. No equivale a límite del derecho de acceso. | [users.service.ts](https://github.com/guidobotta/daily-games-api/blob/main/src/modules/users/users.service.ts), `EXPORT_ROW_CAP` | [Auditoría](audit.md), [Inventario](data-inventory.md), procedimiento de soporte y cualquier futura pantalla de descarga. |
| Cuentas vinculadas inactivas | Sin vencimiento general observado. **Pendiente** decidir por categoría. | Esquema/API, [inventario](data-inventory.md) | [Privacidad §9](public/privacy.es.md), [Eliminación](public/delete-account.es.md). |
| Partidas, wallet, compras, reportes, resolución de cuentas y eventos | Plazos/fundamentos finales **pendientes**; algunas filas siguen vinculadas a una cuenta borrada y otras carecen de TTL. | [Inventario](data-inventory.md), implementación y decisiones de conservación | [Privacidad §9](public/privacy.es.md), [Eliminación](public/delete-account.es.md), procedimientos internos. Registrar plazo por categoría, no uno global. |
| Logs, Sentry, soporte y backups | Ventanas reales de retención **pendientes de verificar** en consolas/proveedores. | Configuración de producción y contratos; [inventario](data-inventory.md) | [Privacidad §5/9](public/privacy.es.md), [Eliminación](public/delete-account.es.md), atención de solicitudes. |
| Plazo de respuesta de soporte | Objetivo interno **pendiente**; no prometer uno sin capacidad operativa. | Decisión operativa y legislación aplicable | [Soporte](public/support.es.md), FAQ, avisos automáticos. |
| Plazos legales para derechos | **Externos**, dependen de jurisdicción y tipo de solicitud. El [inventario](data-inventory.md) anota referencias argentinas para revisar; no son un SLA universal. | Textos legales oficiales vigentes y asesoramiento por mercado | [Privacidad §10](public/privacy.es.md), [Soporte](public/support.es.md), procedimiento interno. |

## Datos no numéricos que también cambian

| Dato | Estado / fuente de verdad | Revisar si cambia |
| --- | --- | --- |
| Marca pública y nombres de planes | **Pendiente** decidir Daily Games/Daylo y confirmar Calm/Pro. Marketing, app, tiendas y responsable deben coincidir. | Títulos de los siete [documentos públicos](public/), [README](README.md), traducciones ES/EN, iconos/fichas y sitio. |
| Responsable legal, domicilio, país, emails de soporte y privacidad | **Pendiente**; completar con datos reales y buzones atendidos. | [Privacidad](public/privacy.es.md), [Términos](public/terms.es.md), [Soporte](public/support.es.md), [Eliminación](public/delete-account.es.md), [Comunidad](public/community.es.md), tiendas, sitio y app. |
| Países de lanzamiento y edad mínima por país | **Pendiente**; no reutilizar el 16+ de la guía histórica ni la clasificación etaria de una tienda como regla contractual. | [Privacidad §10–11](public/privacy.es.md), [Términos §2](public/terms.es.md), consentimiento/ads, onboarding, fichas de tiendas y controles de backend. |
| Proveedores, partners publicitarios, regiones, transferencias y opciones de consentimiento | **Pendiente** confirmar entorno de producción y configuración real. | [Privacidad §5–7](public/privacy.es.md), [Inventario](data-inventory.md), declaraciones de Apple/Google, UMP/ATT y sitio. |
| Moderación, reporte y apelaciones | **Pendiente** designar responsables y proceso efectivo; el código solo registra/ejecuta algunas acciones. | [Comunidad](public/community.es.md), [Términos §5/8](public/terms.es.md), [Soporte](public/support.es.md), pantallas sociales. |
| URLs públicas e idiomas | **Pendiente** dominio/rutas ES/EN y despliegue. Configuración móvil actual tiene `EXPO_PUBLIC_TERMS_URL` y `EXPO_PUBLIC_PRIVACY_URL`. | [README](README.md), [integración móvil](../mobile/legal-integration.md), [env.ts](https://github.com/guidobotta/daily-games-mobile/blob/main/src/config/env.ts), `.env` de release, metadatos de tiendas, enlaces de AdMob y sitio. |
| IDs de app, productos y publicidad | Identificadores de bundle/package, productos de las tiendas, RevenueCat y `app-ads.txt` deben salir de sus consolas y configuración reales. No inventar valores ni exponer claves privadas. | [billing.md](https://github.com/guidobotta/daily-games-api/blob/main/docs/billing.md), [store-catalog.ts](https://github.com/guidobotta/daily-games-api/blob/main/src/modules/billing/store-catalog.ts), configuración de release, fichas de tiendas, [README](README.md) y archivo `app-ads.txt` del hostname público. |
| Versión y fecha de vigencia | Los encabezados actuales dicen **borrador 0.1 / 2-10-2026**. No son fecha de vigencia. | Cada archivo de [public/](public/), traducciones, sitio, registro de aceptación y archivo de versiones. |
| Licencias y atribuciones | [Créditos](public/credits.es.md) menciona **CC BY 3.0** y tamaños de grilla. La versión de licencia pertenece a la obra fuente: no cambiarla como una regla comercial. | Catálogo de assets y avisos de la versión distribuida; revisar nuevas obras, titulares, URLs y transformaciones. |

## Procedimiento cada vez que cambie algo

1. Identificar la **fuente de verdad** de la fila: código, configuración de producción, tienda, decisión comercial o norma externa. Registrar quién aprobó el cambio y cuándo entra en vigor.
2. Actualizar el comportamiento y las superficies de la última columna: documentos ES/EN, app, FAQ, tiendas, sitio, formularios de privacidad y soporte según corresponda. Una corrección editorial no cambia por sí sola el producto.
3. Si afecta privacidad, menores, compras o una condición contractual, revisar si requiere aviso previo, nueva aceptación o consentimiento específico. Conservar la versión publicada anterior.
4. Probar la función y los enlaces reales en una build/entorno representativo. Confirmar que el texto público describe lo que sucede, incluido borrado en proveedores y casos de invitado.
5. Actualizar **este registro** con el nuevo valor, fuente y fecha de revisión. Buscar el valor anterior en ambos repositorios para encontrar copias olvidadas.

Las cifras de competidores del [benchmark](market-benchmark.md) son **referencias externas**, no variables propias de Daily Games. Los números de artículos legales, IDs de URLs, versiones de licencias y fechas históricas tampoco deben reemplazarse mediante una búsqueda global.

## Historial de este registro

| Fecha | Cambio | Estado |
| --- | --- | --- |
| 2026-10-02 | Inventario inicial de reglas, datos pendientes y lugares donde actualizar textos. | Borrador interno; valores de producción por verificar. |
