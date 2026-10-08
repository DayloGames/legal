# Integración de documentos legales

Propuesta basada en la revisión del 2 de octubre de 2026. Este cambio solo agrega documentación; las pantallas y controles descritos como pendientes no están implementados.

La fuente de los borradores y decisiones está en [planning/legal/README.md](../legal/README.md). No duplicar los textos completos en dos repositorios: el directorio `site/` será la fuente publicada; la app consume URLs y versiones. Si se incluye una copia offline, generarla desde la misma versión aprobada.

## Rutas y puntos de entrada propuestos

| Punto | Propuesta | Código actual relacionado |
| --- | --- | --- |
| Perfil → Legal y ayuda | Privacidad, términos, comunidad, compras, soporte, eliminación y créditos; visible para invitados | `app/(tabs)/profile/index.tsx` y layouts de profile/user |
| Primer uso | Información de cuenta invitada, documentos accesibles y aceptación contractual según política aprobada | `app/_layout.tsx`, `src/auth/AuthContext.tsx` |
| Edad | Aplicar **18+ en Argentina**, decidido el 7 de octubre de 2026; no habilitar menores con autorización parental; definir edad desconocida antes de activar tratamientos afectados | No control encontrado; implementación pendiente |
| Acceso Google/Apple | Documentos y aclaración de vinculación; no confundir login del proveedor con aceptación de la app | `src/auth/components/SocialContinueCard.tsx` |
| Primer nombre/grupo | Aceptación de términos que incorporen comunidad antes de crear contenido; validación servidor | `src/profile/RequireUsernameModal.tsx`, `src/features/friends/` |
| Tienda | Términos, privacidad y compras junto a ofertas; URL válida obligatoria para vender | `src/store/BalanceStoreScreen.tsx`, `src/config/env.ts` |
| Cuenta → Datos | Descargar/compartir exportación y canal para completarla; borrar cuenta accesible a invitados según decisión | `src/profile/AccountSettingsScreen.tsx`, `src/api/hooks/useExportAccount.ts` |
| Preferencias publicitarias | Mantener UMP y reabrir opciones cuando corresponda | `src/ads/AdsProvider.tsx`, `AccountSettingsScreen.tsx` |
| Confirmación de borrado | Explicar pérdida de acceso, retención limitada y suscripción que continúa; enlaces a gestionarla | `src/i18n/locales/es.json`, `en.json`, `AccountSettingsScreen.tsx` |
| Comunidad | Mantener reportar/bloquear; agregar reporte de grupos/contacto y apelación operativa | `src/features/friends/api/useModeration.ts` |

## URLs

Hosting aprobado para el lanzamiento: **GitHub Pages**, origen `https://daylogames.github.io` y base de proyecto `/legal`. Por ejemplo, privacidad final tendrá la URL prevista `https://daylogames.github.io/legal/es/privacy/`; verificar publicación antes de usarla. La [guía de publicación y migración](../legal/publicacion-y-migracion.md) enumera rutas y cómo mantener acceso si luego se utiliza un dominio propio.

Actualmente existen `EXPO_PUBLIC_TERMS_URL` y `EXPO_PUBLIC_PRIVACY_URL`, opcionales y enlazadas solo desde tienda si se configuran. Propuesta: URLs canónicas de documentos aprobados por idioma y un origen HTTPS público estable; agregar soporte, compras, comunidad, eliminación y créditos.

Puede usarse una configuración central `src/legal/` con `{ version, locale, url }`, sin adivinar hostname ni tomar emails del usuario de GitHub. Mostrar enlaces en Ajustes aunque billing esté apagado. Usar rutas servidas por el sitio y probar subdirectorios/base paths si es GitHub Pages. Evitar un enlace silenciosamente inexistente.

Antes de una release, comprobar que los enlaces están configurados, responden, corresponden a la versión publicada y no llevan a borradores. Validar ofertas de suscripción también cuando la configuración legal falta: no presentar venta sin avisos requeridos.

## Orden de inicio

Hoy Sentry inicializa al importar el layout; AdsProvider monta fuera de AuthProvider; Auth crea invitado automáticamente. Agregar una casilla al login social no cubre lo que ocurrió antes.

La edad aprobada para el lanzamiento inicial en Argentina es **18+**. Diseñar un control de elegibilidad antes de crear invitado o inicializar los servicios afectados, conservando solo la evidencia necesaria; no habilitar acceso a menores de 18 ni tratar edad desconocida como adulto. Definir las bases por finalidad y el flujo de información/aceptación/consentimiento, junto con qué servicios pueden inicializar antes de cada decisión. Mantener documentos y soporte accesibles si no se acepta. La aceptación contractual no habilita automáticamente ads personalizados, ATT, marketing ni todas las capturas diagnósticas.

Propuesta de registro backend de aceptación: usuario, versión de términos, versiones de anexos incorporados, idioma, timestamp del servidor y origen de la acción. Minimizar datos adicionales; no agregar IP por costumbre. Para invitados, precisar el punto en que se crea identidad. Backend debe verificar aceptación cuando la política lo exija para publicar nombres/grupos. Diseñar migración y tratamiento de cuentas existentes.

## Conservación de cuentas y purga

Decisión de lanzamiento: conservar cuentas invitadas y vinculadas aunque dejen de usarse, con o sin compras; no caducan sus monedas/tokens por inactividad. El script de API `purge-stale-guests.ts` actualmente selecciona invitados inactivos tras 90 días por defecto además de cuentas ya eliminadas. Separar las selecciones antes de ejecutar en producción: la inactividad no debe provocar borrado, pero deben completarse las eliminaciones solicitadas. La retención de logs y otros registros requiere plazos propios. Esta documentación no modifica el script.

## Textos que necesitan ajustes

- Borrado: reemplazar «eliminá tu cuenta y todos sus datos» por una explicación acorde al proceso completo y sus excepciones, con enlace a la política de eliminación.
- Borrado: advertir que no cancela suscripciones y ofrecer gestionarlas sin impedir eliminación inmediata.
- Invitado: explicar datos creados y riesgo de pérdida de progreso/saldo. Definir recuperación de compras antes de exigir o sugerir vinculación.
- Calm: aclarar que quita anuncios entre partidas y que rewarded voluntarios permanecen.
- Suscripción: validar la cláusula de 24 horas por tienda y la promoción «primer mes» por modalidad/duración real.
- Colisión: explicar qué sucede con saldo, compras y beneficios en cada elección, sin prometer sumar o restaurar todo.
- Grupos: no presentar «privado» como admisión manual o seguridad basada exclusivamente en la etiqueta; acceso actual por código.

## Verificación al implementar

Usar build nativa release y dispositivos para comprobar primer uso, invitado/vinculado, documentos ES/EN, rechazo y revocación de ads, ATT según configuración, compras/cancelación/restauración, borrado y creación posterior de invitado. Revisar permisos/SDK y sus declaraciones de datos reales. Probar solicitudes externas sin la app y exportaciones grandes con truncamiento.

No instalar nuevos SDK ni modificar schema o flujos como efecto implícito de estos borradores. Cada implementación debe seguir las decisiones aprobadas y mantener pruebas proporcionadas a sus cambios.
