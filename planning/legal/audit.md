# Revisión técnica para los documentos legales

Fecha: 2026-10-02. Código local limpio al comenzar: API `4d48996`, mobile `54b9657`.

Alcance: manifiestos y configuración, esquema/migraciones, autenticación, ciclo de vida de cuentas, exposición social, moderación, referidos, economía, compras, ads, telemetría, almacenamiento, despliegue y fuentes de contenido. Es una revisión del código y documentación local; no una inspección de las consolas de producción, contratos o tráfico real de los SDK. No se ejecutaron operaciones contra usuarios ni datos reales.

## Lo que cambió respecto de la guía anterior

| Hallazgo actual | Evidencia | Implicación |
| --- | --- | --- |
| Se crea una identidad invitada al abrir, sin registro manual | Mobile `src/auth/AuthContext.tsx`; API `docs/authentication.md` | Invitado no significa sin datos ni sin cuenta técnica. Avisar antes del primer tratamiento que lo requiera. |
| Google en ambas plataformas, Apple en iOS, mediante Supabase | Mobile `src/auth/socialAuth.ts`, `src/auth/supabase.ts` | Incluir a Supabase y proveedores de acceso. |
| Apple solicita nombre y email; guarda nombre/apellido en metadata | Mobile `src/auth/socialAuth.ts:169` y `:217` | No afirmar que jamás se recibe nombre real. Evaluar suprimir esa captura por minimización. |
| Dos monedas, ambas comprables y obtenibles por otras vías | API `prisma/schema.prisma`, `src/modules/billing/store-catalog.ts`, `docs/billing.md` | La separación coin/token es funcional; no equivale a separar saldos comprados/ganados. El ledger conserva el origen. |
| Membresías Calm y Pro con variantes mensual/anual | API `src/modules/billing/membership.ts`; mobile `src/store/BalanceStoreScreen.tsx` | Calm elimina interstitials, no los rewarded opcionales. Pro abre archivo y etapas sin tokens, manteniendo requisitos de progreso. |
| Anuncios interstitials y rewarded; UMP integrado | Mobile `src/ads/AdsProvider.tsx`, `useRewardedPlacement.ts`, `usePostGameInterstitial.ts` | Publicidad y consentimiento deben describirse. UMP se inicializa antes de Auth en el árbol. |
| Rewarded transmite el identificador de cuenta a Google para SSV | Mobile `src/ads/useRewardedPlacement.ts` | Informar identificadores vinculados a anuncios/recompensas. |
| Nombres, amigos, grupos por código y rankings de grupo | API `src/modules/friends/`, `src/modules/groups/`; mobile `src/features/friends/` | No describir un ranking mundial ni un buscador público de grupos que no aparecen en esta implementación. |
| Referidos con hitos, vínculo social y recompensas | API `src/modules/invites/` | Informar que el invitador puede conocer cumplimiento de hitos; incluir reglas de programa. |
| Reportar/bloquear usuarios y filtrar nombres | API `src/modules/moderation/`, `users/username.ts`, `groups/group-name.ts` | Reglas de comunidad justificadas por funcionalidad actual; operación humana pendiente de validar. |
| Exportación API, cliente y hook; no entrada visible encontrada | API `users.controller.ts`, `users.service.ts`; mobile `src/api/hooks/useExportAccount.ts` | No prometer que ya existe un botón de descargar datos. |
| Sentry en API y mobile | API `src/observability/`; mobile `src/lib/sentry.ts`, `src/lib/logger.ts` | No afirmar ausencia de analytics/diagnóstico ni datos totalmente anónimos. |
| Supabase, Render y Cloudflare en arquitectura documentada | API `docs/deployment.md`, `render.yaml` | Confirmar uso real, regiones, contratos y retención. Storage admite Supabase o R2. |
| Créditos de Picture Cross y fuentes de diccionarios | API `CREDITS.md`, `scripts/picture-cross/catalog/`, `scripts/anygram/README.md` | Publicar atribuciones pertinentes y completar avisos de software/diccionarios. |

## Diferencias entre la promesa y la implementación

### 1. Acceso a documentos y aceptación

- URLs de términos y privacidad opcionales en mobile `src/config/env.ts` y `.env.example`; se muestran en tienda solo si están configuradas.
- No se encontró centro legal/soporte general ni acceso a documentos antes del primer uso.
- No se encontró registro persistente de versión aceptada de términos, reglas sociales o edad. `User` no tiene esos campos ni un modelo de aceptación.
- Hace falta aceptación explícita previa a crear nombres/grupos, acorde a Google UGC. Propuesta: un consentimiento contractual que incorpore los anexos y una verificación en backend antes de escribir contenido social.
- La privacidad informa; sus bases de tratamiento y consentimientos específicos deben definirse por finalidad. No resolver todo con «acepto la privacidad».

### 2. Eliminación y conservación

`UsersService.deleteAccount` primero marca `deletedAt` y quita username, después elimina Supabase Auth y cliente RevenueCat, y finalmente purga parte de los datos. Cada integración debe estar configurada y responder para completar el flujo. No se comprobó su despliegue.

- **Temporalmente quedan** usuario técnico con campos restantes, sesiones (incluyen `result` y `progress`), wallets, ledger, pistas y compras. No están anonimizados por el solo hecho de quitar username: siguen enlazados al ID.
- `scripts/purge-stale-guests.ts`: umbral de tombstones de **7 días**, invitados inactivos **90 días** por defecto, lotes de **1.000**. Son criterios de elegibilidad del script, no garantías de borrado a plazo. No se encontró programación del job en `render.yaml`/CI inspeccionados. Confirmar cron externo, frecuencia, capacidad y alertas.
- El script de purga elimina Supabase y usuario local, pero no llama a `RevenueCat.deleteCustomer`. Invitados purgados por inactividad pueden dejar clientes RevenueCat y eventos sin FK. Revisar también clientes creados sin compra.
- `UserReport` conserva IDs, nombre denunciado y nota después del borrado; no hay TTL encontrado. `AccountResolution` tampoco tiene FK al usuario ni purga/exportación en los métodos revisados.
- Un webhook posterior puede volver a registrar un `RevenueCatEvent` con el ID de un usuario eliminado. Definir redacción y TTL para eventos de cuentas inexistentes.
- `purgeDomainRows` elimina membresía de grupo pero no transfiere propietario ni elimina grupos vacíos como sí hace `GroupsService.leave`. El nombre del grupo creado puede permanecer. Resolver tratamiento de contenido y continuidad de grupos.
- Backups, Sentry, registros de infraestructura y buzón de soporte no se borran con `DELETE /users/me`. Definir ventanas y solicitudes a proveedores.
- El texto móvil «todos sus datos» y «progreso, wallet e historial» no explica las excepciones ni que la suscripción continúa. Cambiarlo antes de publicar.
- La app oculta borrar cuenta a invitados aunque tienen identidad, progreso y pueden comprar. Evaluar acceso a eliminación y solicitudes de derechos para ellos.
- Al borrar o cerrar sesión, mobile crea una nueva cuenta invitada. Explicarlo y permitir salir sin seguir creando datos si ese es el propósito del usuario.

No justificar conservación genérica «por ley» sin identificar finalidad, fundamento y plazo. El resguardo contra tokens antiguos necesita un registro mínimo; no demuestra por sí mismo necesidad de retener partidas completas.

### 3. Acceso y exportación

- Exporta hasta **10.000 filas por colección**, con total y señal de truncamiento. Soporte debe poder completar una solicitud mayor.
- No incluye todo lo que procesan Supabase, Sentry, ads, infraestructura, soporte o registros de resolución de cuentas.
- Reportes y bloqueos recibidos se excluyen para proteger a terceros; una solicitud legal exige revisión, no una negativa general automática.
- Proponer botón de descarga/compartir archivo protegido, con advertencia de datos personales y canal para completar solicitudes.

### 4. Edad, ads y telemetría

- No se encontró pantalla de edad ni edad/categoría persistida en el esquema.
- No se encontraron llamadas propias a configuración por menores, TFUA o TFCD. No equivale a verificar comportamiento del SDK o configuración de AdMob.
- Existe texto ATT en configuración; no se encontró una llamada propia a pedir ATT. UMP puede coordinar mensajes según consola. Verificar en una compilación nativa y consola antes de afirmar cumplimiento o ausencia de tracking.
- Sentry inicializa al cargar `app/_layout.tsx`; Auth crea invitado en montaje; AdsProvider inicializa consentimiento en montaje. Diseñar qué comienza antes de información/edad/aceptación según las bases aplicables.
- Backend redacta cuerpos, cookies, datos SQL y ciertos headers; adjunta ID de cuenta a Sentry. Mobile registra user IDs y contextos de error, sin una capa equivalente de redacción en `src/lib/sentry.ts`. Auditar tokens/metadata en logs y breadcrumbs, captura automática nativa y retención.
- No se encontró analytics de marketing independiente, chat, agenda, subida de fotos, GPS preciso, push token ni retirada/conversión de moneda en los flujos revisados. Verificar permisos finales del binario, no solo `package.json`.

### 5. Comunidad

- Reportes actuales apuntan a **usuario** por friend code; no existe denuncia con groupId en el controller revisado. Preparar reporte de nombre/grupo o un contacto público atendido con instrucciones, sin afirmar que ya hay un botón para grupos.
- Guardar un reporte no supone revisión, notificación, resolución, apelación o sanción implementadas. No se encontró panel/cola administrativa en estos repositorios.
- El bloqueo corta amistad y oculta pares en rankings compartidos; no expulsa del grupo ni recalcula el ranking excluyendo al usuario bloqueado. Los otros miembros pueden seguir viéndolo.
- Grupos públicos/privados se unen por código hoy; nombres y resultados son visibles según el contexto. No prometer que «privado» implica aprobación manual del propietario.

### 6. Compras y avisos

- Precios se obtienen de tiendas mediante RevenueCat; no escribir precios fijos en el anexo.
- Compras están condicionadas a keys/configuración y `BILLING_ENABLED`; integración presente no acredita disponibilidad comercial actual.
- La descripción de Calm «experiencia sin anuncios» debe aclarar los rewarded voluntarios. La lista de perks es más precisa.
- El disclaimer español usa regla de 24 horas para ambas tiendas. Validar textos por plataforma, pruebas, promociones y cambios de precio en vez de exportar indiscriminadamente condiciones de Apple a Google.
- Revisar la oferta introductoria: texto «primer mes» debe corresponder a duración y modalidad reales, también en anual.
- Restaurar suscripciones no implica restaurar todos los consumibles ya entregados. Explicar protección mediante cuenta y recuperación de invitados.
- La app tiene transferencia de compras al resolver cuentas; verificar que no reasigne compras de terceros ni destruya derechos pagados sin explicación y confirmación.

### 7. Licencias y contenido

- `CREDITS.md` ya atribuye Lorc y Delapouite, CC BY 3.0, y describe adaptación a grillas. Mantener generación desde catálogo y hacer accesible en app/sitio para lo efectivamente distribuido.
- README Anygram advierte SCOWL y cracklib-small para fuentes inglesas. Confirmar archivos reales, textos de licencia y qué partes/datos se redistribuyen. No declarar todo dominio público.
- Validar también avisos de bibliotecas, iconos y fuentes, derechos de avatares, contratos/cesiones y activos de IA. El crédito inicial no sustituye un inventario completo de la versión.
- La selección de imágenes incluye referencias como armas/alcohol; responder clasificación etaria sobre el contenido publicado real, no sobre el género «puzzle».

## Orden propuesto

1. Identidad, nombre, buzón, mercados y edad.
2. Conservación y eliminación completa, incluida operación del job y proveedores.
3. Documentos ES/EN y sitio con soporte externo efectivo.
4. Acceso legal, información inicial y registro de aceptación; controles de menores/consentimiento según alcance.
5. Operación de moderación, créditos y formularios de tiendas.
6. Validación de flujos reales en builds nativas y consolas antes de envío.

Estas tareas son el resultado de la revisión. Este cambio crea documentación; no implementa ni certifica los controles pendientes.
