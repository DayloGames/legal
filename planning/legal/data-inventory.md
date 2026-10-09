# Inventario, conservación y solicitudes de datos

Interno. Borrador 2026-10-02. La columna de finalidad describe el uso observado; una finalidad no es una base jurídica. Asignar base por tratamiento, responsable y mercado antes de aprobar privacidad.

## Inventario inicial

| Categoría | Datos y origen | Uso observado | Destinatarios/visibilidad | Fuente |
| --- | --- | --- | --- | --- |
| Identidad invitada | Supabase ID, sesiones/tokens, condición anónima, creación y actividad | Autenticación, persistencia, recuperación | Supabase; API | Mobile `src/auth/`; API `User` |
| Identidad vinculada | Email/relay, IDs Google/Apple y metadata de identidad; nombre/apellido Apple guardados expresamente | Acceso y vinculación | Supabase, proveedor de login; no email público en API social revisada | Mobile `src/auth/socialAuth.ts` |
| Perfil | Username, friendCode, avatar elegido, cambio de nombre | Identificación social y personalización | Supabase DB/API; otros jugadores según función | `User`, `UserAvatarSlot`, `friends/` |
| Preferencias | Idioma, tema, timestamps, zona horaria en requests y racha | Localización, calendario y reconciliación | Dispositivo, API/DB | `User`; mobile `src/preferences/`, `src/api/client.ts` |
| Juego | Tableros/progreso/resultados, tiempos, errores, pistas, sesiones, completados | Reanudar, validar resultados y detectar abuso | API/DB; resúmenes con amigos y rankings | `GameSession`, `HintUse`, `groups/` |
| Progresión/economía | XP, racha, logros, saldo, movimientos, desbloqueos, cosméticos | Recompensas y uso de bienes digitales | API/DB; algunos logros/racha/nivel a amigos | Modelos de progresión y wallet |
| Amigos/grupos | Solicitudes, pares, membresías, roles, joinCode, nombre/privacidad del grupo | Funciones sociales y rankings | API/DB y jugadores autorizados | `Friendship`, `Group`, `GroupMember` |
| Referidos | Invitador/invitado, fecha y hitos, recompensas ganadas/cobradas | Programa de invitación y antifraude | API/DB; estado de hitos al invitador | `Referral`, `ReferralReward`, `invites/` |
| Moderación | IDs denunciante/denunciado, nombre copiado, razón, nota libre hasta 1.000 caracteres; bloqueos | Protección de comunidad, investigación | API/DB, personal autorizado; lista de bloqueos propia | `UserReport`, `UserBlock` |
| Compras | ID cuenta, producto/transacción/tienda, fechas, entorno, devolución, entitlement/vencimiento; eventos | Validación, entrega, restauración y soporte | Apple/Google, RevenueCat, API/DB | `billing/`, `StorePurchase`, `UserEntitlement`, `RevenueCatEvent` |
| Ads/consentimiento | Decisiones UMP; señales SDK de dispositivo/ads según configuración; cuenta y placement en SSV, ID transacción y recompensa | Publicidad, consentimiento y entrega de rewards | Google/partners configurados; API registra recompensa | Mobile `src/ads/`; API `ads/` |
| Diagnóstico | ID de cuenta en backend y logs móviles, requestId, rutas, errores, rendimiento, dispositivo y headers según SDK | Operación, seguridad y fallos | Sentry si habilitado; logs de hosting | API `src/observability/`; mobile `src/lib/sentry.ts` |
| Tráfico | IP, requests, metadatos de conexión, país aproximado derivado de red cuando disponible | Entrega de API/assets, WAF y seguridad | Cloudflare/Render/Supabase/storage según despliegue | `docs/deployment.md`, configuración de headers Sentry |
| Resolución de cuentas | IDs de dos cuentas, elección y estado/fechas | Resolver colisiones y reintentos | API/DB | `AccountResolution`, `UsersService` |
| Almacenamiento local | Sesión en SecureStore; preferencias y frecuencia de ads en AsyncStorage; cachés en memoria/SDK | Mantener sesión y experiencia | Dispositivo; revisar backups del SO | Mobile `src/auth/storage.ts`, `preferences/storage.ts`, `ads/postGameFrequency.ts` |
| Soporte futuro | Email, solicitud, evidencias mínimas, resolución | Atender derechos/reclamos | Buzón y proveedores todavía por definir | No canal configurado encontrado |

## Proveedores: completar por entorno

Hosting legal confirmado el 8 de octubre: **GitHub Pages**, con URL de proyecto prevista `https://daylogames.github.io/legal/`. Incluir tráfico/IP del sitio y configuración contractual/retención/transferencias en la revisión de proveedores. [Plan de publicación y migración](publicacion-y-migracion.md).

Confirmación del usuario: **Supabase, Render, Cloudflare/R2, Sentry, Google AdMob y RevenueCat activos en producción**. No se inspeccionaron consolas. Esta confirmación no determina servicios específicos, regiones, contratos, partners publicitarios, retención ni eliminación; completar esos datos por proveedor.

Supabase (Auth, Postgres y Storage si se usa); Render (API); Cloudflare/R2 (uso confirmado; funciones/configuración exactas por verificar); Sentry (mobile y backend); Google AdMob y partners elegidos; RevenueCat; Apple/Google (acceso y pagos); hosting del sitio; proveedor del buzón de soporte. Expo/EAS aparece en desarrollo/build: determinar si hay servicios runtime adicionales antes de incluirlo como destinatario de datos de jugadores.

Para cada uno registrar: entidad contratada, función jurídica real, servicio/configuración, región, datos, acceso de personal, DPA/contrato, subencargados, transferencias y salvaguardas, retención, procedimiento de eliminación, responsable interno y última revisión. No asignar automáticamente rol de encargado a todos los proveedores: tiendas y proveedores publicitarios pueden actuar con fines propios.

## Conservación: observado versus propuesta

Decisión posterior de la sesión: los plazos de reportes y resoluciones siguen
pendientes y el usuario indicó conservar esos registros por ahora. El cambio 4
de API implementa acceso protegido a metadatos y minimización de webhooks; no
introduce expiración ni afirma anonimización de registros retenidos. La evidencia
es local, publicada en draft y pendiente de revisión/despliegue; ver
[plan de implementación](plan-implementacion-prs.md).


| Datos | Código actual | Decisión/acción necesaria |
| --- | --- | --- |
| Cuenta activa o inactiva, progreso y economía | Sin expiración general encontrada | Decisión de lanzamiento: conservar cuentas aunque dejen de usarse. Definir necesidad y retención por categoría de registros; no equivale a guardar todo indefinidamente. |
| Invitado inactivo | Código corregido en API #87: no selecciona invitados por inactividad | Decisión de lanzamiento: conservar invitados inactivos, con o sin compras. Verificar despliegue y proceso efectivo de eliminaciones solicitadas. |
| Cuenta eliminada y tablas protegidas | Tombstone elegible tras 7 días; máximo 1.000 por pasada | Minimizar retención residual; aprobar fundamento y plazo real; comprobar TTL máximo de tokens y completar fallos parciales. |
| Reportes | Conservados sin TTL ni FK; API #90 exporta metadatos de reportes propios, sin contenido sensible | Plazo de cierre/investigación y retención posterior; acceso restringido; anonimización/borrado; justificación. |
| Resolución de cuentas | Persistente sin FK; API #90 agrega exportación/paginación de metadatos sin IDs ajenos, conserva tareas y registros completos | TTL por necesidad de reintento/seguridad y tratamiento en solicitudes. |
| Eventos RevenueCat | API #90 minimiza IDs de cuentas ausentes/eliminadas y serializa escrituras con el tombstone | Minimizar eventos de cuentas inexistentes y definir TTL. |
| Grupos/nombres | Membership borrada; grupo puede quedar vacío/sin owner | Reasignación, borrado o anonimización del contenido según situación. |
| Registros y Sentry | Dependientes de plan/configuración | Fijar plazos reales por logs, errores, traces y métricas; comprobar filtros móviles. |
| Backups | Documentación recomienda backups; configuración no comprobada | Ventana real, control de acceso y reaplicación de eliminaciones al restaurar. |
| Compras/documentación fiscal | Compras técnicas se purgan junto a cuenta | Contador/legal debe definir documentos que deben conservarse y cómo separarlos/minimizarlos. No inventar obligación contable de retener partidas. |
| Soporte | Sin sistema definido | Plazo de ticket, adjuntos, eliminación y acceso. |

No publicar «eliminamos todo en 7 días» ni «los invitados se borran automáticamente a los 90 días» basándose solamente en constantes. Para completar eliminaciones solicitadas, la propuesta operativa es un job supervisado con suficiente capacidad. Su diseño/implementación sigue pendiente y debe excluir las cuentas no eliminadas que solo están inactivas.

## Atención de derechos: procedimiento documentado

La [guía de soporte, derechos y reportes](operacion-soporte-y-plazos.md) organiza identificación, plazos y seguimiento. Está documentada, pero falta ponerla en funcionamiento y verificarla. Soporte general tiene un objetivo de primera respuesta útil hasta 10 días hábiles; los plazos de derechos y prioridades de urgencia son distintos.

1. Buzón público atendido por ambos prestadores, en español e inglés. Se prevé revisión frecuente, sin garantizar revisión diaria o respuesta en 24 horas. Registrar solicitud, fecha de ingreso, jurisdicción, alcance y vencimiento aplicable. No contar desde la fecha en que se decide leer el mensaje; habilitar seguimiento y cobertura para evitar vencimientos. El método está documentado en la guía; puesta en funcionamiento y verificación pendientes.
2. Verificar titularidad con los mínimos datos necesarios. Priorizar sesión o email vinculado; no pedir contraseñas, tokens ni documento de identidad por defecto.
3. Reunir datos de API, Supabase, proveedores, soporte y registros relevantes. La exportación actual no sustituye ese relevamiento y puede truncarse.
4. Proteger información de terceros al responder. Examinar cada excepción y explicar límites; no revelar denunciantes por defecto.
5. Aplicar corrección/eliminación, gestionar terceros y confirmar qué se retuvo, motivo y plazo.
6. Dar seguimiento a errores parciales, jobs y restauraciones de backup; conservar solo evidencia mínima de atención durante el plazo aprobado.

Referencia argentina a revisar para el procedimiento: Ley 25.326 art. 14 establece diez días corridos para acceso desde intimación fehaciente; art. 16 establece hasta cinco días hábiles para rectificación/actualización/supresión desde reclamo o detección. No usar un SLA genérico de 30 días para todas las solicitudes. Las excepciones y otros mercados requieren análisis específico. [Texto oficial](https://www.argentina.gob.ar/normativa/nacional/64790/texto).

## Declaraciones de tiendas: hoja de trabajo

Evaluar por definiciones de cada tienda, no copiar categorías entre formularios: identificadores de usuario, datos de contacto/nombre recibidos en Auth, actividad de juego/usuario, compras, contenido de usuarios, diagnóstico/rendimiento y datos de publicidad/dispositivo. Separar datos recolectados, compartidos, vinculados al usuario, tracking, tratamiento transitorio y opcionalidad según SDK/entorno final. Verificar también SDK nativos, privacy manifests y permisos del binario.

Pendientes: tráfico de prueba de build release, configuración UMP/ATT, partners de ads, Sentry efectivo, consolas de hosting/retención, regiones y contratos. Esta tabla no es un formulario listo para enviar.
