# Documentación legal de Daily Games / Daylo

Estado: borradores de trabajo, no publicados. Revisión del código: 2 de octubre de 2026.

Estos documentos se construyeron a partir de ambos repositorios actuales. La guía anterior de Downloads es una referencia histórica, no una fuente de decisiones vigentes. Las propuestas de este directorio tampoco se convierten por sí mismas en políticas aprobadas.

La matriz inicial de requisitos de tiendas y Argentina está en [requisitos-argentina-y-tiendas.md](requisitos-argentina-y-tiendas.md).

La [guía de cierre para el lanzamiento](plan-de-cierre.md) organiza las decisiones, verificaciones técnicas y publicación, con una comprobación parcial del código local del 7 de octubre de 2026.

La [guía operativa de soporte, derechos y reportes](operacion-soporte-y-plazos.md) explica cómo identificar pedidos, qué plazos corresponden y cómo organizarse en el buzón. Es material para el equipo, visible en este repositorio público; no guardar aquí casos reales.

El [inventario de licencias y recursos](inventario-licencias.md) coteja Picture Cross, identifica fuentes de diccionarios y registra las licencias declaradas por las dependencias directas de mobile. Distingue evidencia local de derechos y avisos todavía por verificar.

La comparación de documentos oficiales de Puzzle Page, Everyday Puzzles y Minipuzzles está en [market-benchmark.md](market-benchmark.md). Es material de investigación interno, no parte del sitio público.

Los números, plazos, límites y demás datos que pueden cambiar se mantienen en [variables-y-cambios.md](variables-y-cambios.md), con su fuente primaria y las páginas que habría que revisar. También es un documento interno.

## Qué preparar

| Documento público | Archivo | URL propuesta | Uso |
| --- | --- | --- | --- |
| Política de privacidad | [privacy.es.md](public/privacy.es.md) | `/es/privacy/` | Datos, proveedores, conservación y derechos. En la tienda y dentro de la app. |
| Términos de uso | [terms.es.md](public/terms.es.md) | `/es/terms/` | Cuenta, juego, comunidad y relación contractual. |
| Reglas de comunidad | [community.es.md](public/community.es.md) | `/es/community/` | Nombres, grupos, reportes, bloqueo y juego limpio. Referenciadas por los términos. |
| Compras y suscripciones | [purchases.es.md](public/purchases.es.md) | `/es/purchases/` | Monedas, tokens, Calm/Pro, anuncios opcionales y referidos. Anexo de los términos. |
| Soporte | [support.es.md](public/support.es.md) | `/es/support/` | Contacto y ayuda con cuenta, compras y moderación. |
| Eliminación de cuenta | [delete-account.es.md](public/delete-account.es.md) | `/es/delete-account/` | Solicitud externa y explicación de sus efectos. |
| Créditos y licencias | [credits.es.md](public/credits.es.md) | `/es/credits/` | Atribuciones de imágenes y avisos de terceros. |

Separar comunidad y compras permite enlazarlas desde la función correspondiente. Siguen formando parte de los términos; no son siete acuerdos que el usuario deba aceptar en siete casillas. No hace falta un documento autónomo de cookies de la app: describir almacenamiento local y SDK en privacidad. El futuro sitio deberá evaluar sus propias tecnologías y proveedores.

Privacidad es un requisito general de tiendas. Eliminación externa aplica al permitir creación de cuenta; soporte y contacto deben ser efectivos. Las suscripciones de Apple requieren enlaces a términos y privacidad en app y metadata. Las reglas de contenido deben estar definidas y aceptadas antes de crear UGC en Google; una página separada de comunidad es una decisión editorial. Separar compras también es una decisión editorial. Créditos depende de las licencias efectivamente utilizadas: aquí existen assets atribuidos CC BY 3.0 y otras fuentes que revisar.

La [guía de publicación y migración](publicacion-y-migracion.md) registra GitHub Pages como hosting inicial, rutas previstas y ubicación separada de `app-ads.txt`.

## Dónde van

**Ahora:** todos los borradores y la investigación se trasladaron a `planning/legal/`; la integración móvil está en [legal-integration.md](../mobile/legal-integration.md). Estos archivos son visibles en el repositorio público. Pages genera vistas previas rotuladas bajo `/borradores/` a partir de `public/`; las demás notas de `planning/` no aparecen en el sitio. Las páginas vigentes, cuando se aprueben, tendrán su fuente en `site/`. No se modificaron pantallas, bases, SDK ni configuración de producción.

**Publicación propuesta:** este repositorio dedicado usa GitHub Pages mediante Actions y compila únicamente `site/`. Al aprobar cada documento, copiar su versión final desde `planning/legal/public/` a la ruta correspondiente de `site/`, retirar notas y marcadores, agregar traducción y archivar la versión previa. Preferir un dominio propio estable con HTTPS. No enlazar borradores desde la app ni desde las tiendas. Las vistas previas de Pages tienen aviso de borrador y no son rutas de políticas vigentes.

**Idiomas:** español e inglés, como la app. Los borradores iniciales son españoles; producir la versión inglesa después de cerrar las decisiones evita dos textos divergentes. No lanzar una ficha inglesa con enlaces que aparenten ofrecer una política inglesa inexistente. Definir cómo resolver idioma y conservar enlaces estables.

**AdMob:** publicar también `/app-ads.txt` en la raíz del hostname que aparece como sitio del desarrollador en las tiendas, con el fragmento real obtenido de AdMob. Una ruta de proyecto como `usuario.github.io/proyecto/app-ads.txt` no equivale a `usuario.github.io/app-ads.txt`. Resolverlo con el sitio raíz o dominio propio. No se creó un archivo con identificadores inferidos.

**Dentro de la app:** legal y soporte accesibles también a invitados; términos y privacidad antes del primer uso; reglas antes de crear contenido social; enlaces comerciales junto a las ofertas; cuenta y datos en Ajustes. Ver el plan móvil para el orden de inicialización.

## Decisiones pendientes

Los marcadores `[PENDIENTE: ...]` son preguntas que deben resolverse antes de publicar. La fecha de revisión no es una fecha de entrada en vigencia.

| Decisión | Por qué cambia los textos |
| --- | --- |
| Nombre público: Daily Games o Daylo | Las traducciones comerciales usan Daylo; los repositorios y metadatos aún dicen Daily Games/mobile. Unificar. |
| Domicilio, responsabilidades sobre datos y titularidad contractual | Prestadores confirmados: Guido Tomas Botta y Gianluca Belinche, ambos personas físicas en Argentina. Completar domicilio válido y confirmar responsabilidades sobre datos y cuentas/contratos. |
| Email real de soporte y privacidad | Necesario para que las páginas permitan consultas y solicitudes reales. Puede ser un único buzón atendido. |
| Aplicación de edad y países confirmados | Lanzamiento inicial **18+ en Argentina**, aprobado el 7 de octubre de 2026. Falta implementar/verificar elegibilidad, edad desconocida y datos de menores detectados. Expansión futura por evaluar. |
| Regiones y configuraciones reales de proveedores | El usuario confirmó Supabase, Render, Cloudflare/R2, Sentry, AdMob y RevenueCat en producción. Falta verificar servicios/configuración, regiones, contratos, partners, retención y eliminación. |
| Plazos y fundamentos de conservación | El script contiene umbrales, no acredita ejecución ni justifica conservar datos. |
| Nombre Apple: conservar o eliminar su captura | El login actual guarda nombre y apellido en Supabase aunque no los usa como nombre público. |
| Moderación: proceso de revisión y apelaciones | Ambos prestadores atenderán reportes; falta definir/verificar revisión, medidas, avisos y apelaciones. |
| Protección y recuperación de compras de invitados | Comprar como invitado está permitido. Definir advertencias, verificación de titularidad y cómo atender la pérdida de acceso a saldo comprado. |

## Cómo cerrar y mantener

1. Resolver las decisiones anteriores y revisar [audit.md](audit.md).
2. Ajustar funcionamiento y textos juntos, particularmente eliminación, menores y aceptación.
3. Completar [data-inventory.md](data-inventory.md), proveedores, bases jurídicas y conservación. Validar las cláusulas jurídicas de los mercados elegidos con asesoramiento acorde al lanzamiento.
4. Revisar derechos/licencias y generar los avisos de terceros de la versión que se distribuye.
5. Reescribir los borradores sin notas editoriales ni marcadores; asignar versión y fecha de vigencia, y traducirlos.
6. Renderizar y revisar el sitio; probar enlaces y canal externo de eliminación desde un celular sin la app instalada.
7. Configurar URLs en las tiendas, app, AdMob/UMP y materiales de suscripción. Completar las declaraciones de datos con evidencia de SDK y configuración real.
8. Probar los flujos de aceptación, rechazo publicitario, compras, eliminación y solicitudes de derechos. Publicar cuando documentos y funcionamiento coincidan.

Conservar versiones publicadas de términos, anexos y privacidad, con fecha de vigencia y resumen de cambios. Registrar versión, idioma y fecha de aceptación de los términos; los consentimientos opcionales van separados. Un cambio sustancial necesita el aviso y, cuando corresponda, la nueva aceptación o consentimiento adecuados, no solamente reemplazar el archivo web.

## Fuentes oficiales revisadas

- [Apple: App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/).
- [Apple: eliminación de cuenta](https://developer.apple.com/support/offering-account-deletion-in-your-app/).
- [Apple: información de suscripciones](https://developer.apple.com/app-store/subscriptions/).
- [Google Play: datos de usuarios](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en).
- [Google Play: eliminación de cuenta](https://support.google.com/googleplay/android-developer/answer/13327111?hl=en).
- [Google Play: contenido de usuarios](https://support.google.com/googleplay/android-developer/answer/9876937?hl=en).
- [Google AdMob: consentimiento en EEE, Reino Unido y Suiza](https://support.google.com/admob/answer/13554116?hl=en-GB).
- [Google AdMob: publicación de app-ads.txt](https://support.google.com/admob/answer/9363762?hl=en).
- [AAIP: derechos sobre datos personales](https://www.argentina.gob.ar/aaip/datospersonales/derechos).
- [Argentina: Ley 25.326, texto oficial](https://www.argentina.gob.ar/normativa/nacional/64790/texto).
- [Creative Commons: condiciones de atribución CC BY 3.0](https://creativecommons.org/licenses/by/3.0/).

Las obligaciones legales dependen del responsable, mercados, edades y prácticas finales. Los requisitos de tiendas aquí identificados no sustituyen ese análisis territorial.
