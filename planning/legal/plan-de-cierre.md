# Guía para cerrar la versión legal de lanzamiento

Revisión: 7 de octubre de 2026. Estado: preparación; no aprueba ni publica políticas.

Se revisaron los documentos de este repositorio y puntos concretos del código local de API `5e00bae`, mobile `cba649a` y backoffice `d890a8c`. Es una comprobación parcial de los pendientes de la [auditoría del 2 de octubre](audit.md), no una nueva auditoría integral ni una inspección de producción. No se accedió a consolas, credenciales ni datos de usuarios.

## 1. Resolver primero estas decisiones

Completar lo conocido; lo demás sigue pendiente. Registrar decisiones aprobadas en [variables-y-cambios.md](variables-y-cambios.md) y trasladarlas a los textos afectados.

| Decisión | Información necesaria | Estado |
| --- | --- | --- |
| Marca | Nombre exacto para app, sitio y fichas | Confirmado: Daylo Games |
| Prestadores | Identidad, responsabilidades sobre datos, domicilio válido y titularidad de cuentas/contratos | Confirmado: Guido Tomas Botta y Gianluca Belinche, ambos personas físicas en Argentina. Responsabilidades sobre datos, domicilio y titularidad por precisar |
| Alcance | Países habilitados en cada tienda y plataformas de lanzamiento | Confirmado: Argentina; plataformas por confirmar |
| Edad | Aplicar edad mínima, definir edad desconocida y atender datos de menores detectados | Confirmado: **18+ en Argentina**; implementación pendiente; ver [decisión](edad-y-consentimiento.md) |
| Contacto | Buzón atendido, persona que lo revisa e idiomas; puede ser uno para soporte, privacidad y apelaciones | Email confirmado: dailygamesbb@gmail.com; ambos prestadores atenderán soporte, borrado/derechos y reportes; atención en español e inglés confirmada; objetivo de primera respuesta útil hasta 10 hábiles para consultas generales; sin revisión diaria garantizada. [Guía operativa](operacion-soporte-y-plazos.md) creada; puesta en funcionamiento por verificar |
| Sitio | URLs, idiomas y futura migración | Confirmado: GitHub Pages en `https://daylogames.github.io/legal/` para lanzamiento; dominio propio futuro opcional. [Plan de publicación](publicacion-y-migracion.md); rutas finales y verificación pendientes |
| Monetización | Catálogo, precios, periodicidades, promociones, ads y recuperación de compras de invitados | Confirmado para lanzamiento: anuncios, packs de monedas/tokens y Calm/Pro, ambos mensuales y anuales. Precios, promociones y oferta/configuración efectiva por verificar; compras como invitado permitidas; advertencias, protección y recuperación pendientes de definir/verificar |

No incorporar domicilio personal ni documentación de identidad a estas notas públicas para discutir opciones. Los datos identificatorios exigibles sí deberán figurar en la versión pública cuando se defina el responsable y un domicilio válido.

Todas las monedas y tokens, comprados o ganados por juego, anuncios y referidos, **no vencen mientras la cuenta se conserve**, por decisión del usuario. No se eliminarán cuentas ni saldos por inactividad en el lanzamiento inicial, incluidos invitados con o sin compras. Falta resolver derechos y saldos ante eliminación o cierre y recuperación al perder sesión.

Pruebas gratuitas y promociones introductorias **por definir**. Los documentos contemplan ofertas sin fijar precios; la app debe informar condiciones específicas antes de confirmar y reflejar lo configurado en la tienda. No se aprobó una oferta concreta ni se descartaron promociones.

## 2. Corregir o verificar el producto antes de prometerlo

| Prioridad | Hallazgo local actual | Condición de cierre |
| --- | --- | --- |
| Alta | `AccountSettingsScreen.tsx` oculta eliminar cuenta cuando `isAnonymous` es verdadero | Invitados y vinculados pueden iniciar borrado; probar ambos flujos |
| Alta | `deleteAccount` borra Auth y RevenueCat antes de la purga parcial; el script mantiene umbrales de 7/90 días y 1.000 filas por lote | Proceso completo probado, reintentos, programación/capacidad/alertas y plazos por categoría confirmados; incluir proveedores y backups |
| Alta | `purge:guests` selecciona invitados inactivos y tombstones; no se verificó cron de producción | Separar ambos procesos: conservar inactivos según decisión y completar eliminaciones solicitadas. Ajustar selección antes de ejecutar; verificar programación/capacidad/alertas |
| Alta | Mobile sigue diciendo «todos sus datos»; no explica ahí los residuos ni cancelación de suscripciones | Mensaje preciso, categorías/plazos publicados y acceso a gestión de suscripciones |
| Alta | Términos/privacidad son URLs opcionales en `env.ts`; no se encontró un registro de aceptación legal en el esquema revisado | Documentos accesibles a invitados; aceptación antes de nombres/grupos y evidencia de versión/idioma/fecha |
| Alta | Sentry se inicia al importar el layout; AdsProvider y AuthProvider se montan al arrancar | Definir información, edad, fundamentos y consentimientos por finalidad; probar qué datos se transmiten antes y después |
| Alta | Backoffice local permite descubrir endpoints/scripts/modelos y consultar datos | Operadores de atención confirmados: Guido Tomas Botta y Gianluca Belinche. Definir y verificar el procedimiento de reportes, acciones, avisos y revisión; probar denuncia de nombres y grupos. La herramienta sola no acredita moderación operativa |
| Media | Persisten textos universales de «24 horas» y oferta «primer mes» | Condiciones verificadas por plataforma y oferta real, incluida modalidad anual |
| Media | Créditos contienen atribuciones y notas pendientes sobre diccionarios y otros recursos | Inventario de lo distribuido, licencias y avisos completos; comprobar originales y adaptaciones |

También verificar la revocación de tokens de Sign in with Apple al borrar: no se encontró una llamada propia en la búsqueda dirigida, pero eso no permite concluir qué hace la integración de Supabase desplegada.

Apple exige iniciar borrado dentro de la app, incluidas cuentas invitadas; un email externo no sustituye ese flujo para esta app. Google permite un email atendido como vía de solicitud en el recurso web externo. Suscripciones y eliminación son acciones distintas. Fuentes: [Apple](https://developer.apple.com/help/app-review/guideline-reference/5-1-1-account-deletion), [Google Play](https://support.google.com/googleplay/android-developer/answer/13327111?hl=en).

Google exige aceptación de términos/reglas antes de crear contenido de usuarios y moderación efectiva: [política UGC](https://support.google.com/googleplay/android-developer/answer/9876937?hl=en). Registrar versión/idioma/fecha y validarlo en backend es la propuesta de implementación del repositorio.

## 3. Reunir evidencia de producción

El usuario confirmó **Supabase, Render, Cloudflare/R2, Sentry, Google AdMob y RevenueCat en producción**. La confirmación no acredita regiones, contratos ni configuración efectiva. Completar [data-inventory.md](data-inventory.md) para cada servicio realmente activo: entidad/función, región, datos tratados, contrato, mecanismo de transferencia, retención y borrado. Revisar Supabase, Render, Cloudflare/R2, Sentry, AdMob/partners, RevenueCat, Apple/Google, hosting web y buzón; quitar servicios no utilizados.

Definir conservación por categoría con finalidad, fundamento, plazo, mecanismo de borrado y responsable de comprobarlo. Incluir reportes, resolución de cuentas, eventos de compras, invitados con compras, logs, soporte y backups. No convertir constantes del código en garantías públicas.

Para Argentina, revisar con el responsable y asesoramiento local los fundamentos de cada tratamiento, inscripción aplicable, transferencias, contratación con menores, consumo, ley aplicable y límites de responsabilidad. Fuentes: [Ley 25.326 actualizada](https://www.argentina.gob.ar/normativa/nacional/ley-25326-64790/actualizacion), [AAIP: transferencias](https://www.argentina.gob.ar/transferencias-internacionales) y [matriz del repositorio](requisitos-argentina-y-tiendas.md). Los artículos 14 y 16 contemplan plazos diferentes para acceso y rectificación/supresión; no adoptar un plazo universal de 30 días.

## 4. Cerrar textos y publicación

1. Completar privacidad, términos, comunidad, compras, soporte, eliminación y créditos con decisiones y funcionamiento verificados. Retirar notas editoriales y todos los marcadores pendientes.
2. Revisar jurídicamente las cláusulas dependientes del responsable y mercados. Fijar versión y fecha de vigencia; traducir al inglés si ese idioma forma parte del lanzamiento y conservar ambas versiones coherentes.
3. Crear las páginas finales en `site/es/<ruta>/index.md` y, cuando corresponda, `site/en/<ruta>/index.md`. Convertir enlaces relativos de archivos en rutas de sitio. Actualizar portada e idioma del HTML; conservar `noindex` en las vistas de borrador aunque las páginas finales sean indexables.
4. Comprobar privacidad, soporte y eliminación desde un teléfono sin la app, sin login y sin restricciones de acceso. Ejecutar una solicitud de prueba de punta a punta con cuenta de prueba.
5. Configurar las URLs finales en app y tiendas; completar App Privacy y Data safety a partir de la build y SDK/configuración reales. Comprobar UMP/ATT, permisos y avisos nativos aplicables.
6. Si se utiliza AdMob, obtener el identificador real de `app-ads.txt` y publicarlo en la raíz del hostname del sitio de desarrollador. La ruta de proyecto `/legal/` no resuelve por sí sola esa ubicación.
7. Validar en builds nativas release: primer uso, aceptación social, invitado/vinculado, rechazo/revocación publicitaria, compras/restauración/cancelación, borrado y solicitud externa. Guardar evidencia mínima de resultados, sin datos personales en el repositorio público.

## Criterio para declarar la versión lista

Avance documental: se completó la autoridad de control/vía de denuncia de privacidad y se redactaron las cláusulas generales de responsabilidad y ley aplicable para Argentina, sin límite contractual de indemnización ni jurisdicción exclusiva. Los textos siguen siendo borradores para revisión jurídica. Se creó el [inventario de licencias](inventario-licencias.md); atribuciones de Picture Cross coinciden con el catálogo local, pero release, originales, diccionarios y avisos completos siguen pendientes. La [guía de atención](operacion-soporte-y-plazos.md) incluye ahora revisión específica de bajas contractuales y posibles plazos más cortos que soporte general.

Documentos sin pendientes, identidad/contacto efectivos, funcionamiento coincidente, evidencia de conservación/borrado y moderación, licencias completas, URLs finales probadas y declaraciones de tiendas consistentes. Publicar HTML final no completa por sí solo la preparación legal de la app.
