# Edad, aceptación y publicidad para Daylo Games

Evaluación y decisión: 7 de octubre de 2026. Alcance inicial confirmado: **Argentina, 18+**. El usuario aprobó esta edad para el lanzamiento inicial. Este documento no modifica la app; implementación y comprobaciones pendientes.

## Decisión aprobada para el lanzamiento

El lanzamiento inicial será para personas de **18 años o más en Argentina**. No se admite a menores mediante autorización parental. Aplicar la restricción antes de los tratamientos afectados, definir edad desconocida y la atención de datos de menores detectados, y alinear tiendas y marketing.

La comparación siguiente se conserva como fundamento de la decisión. 16+ y 13+ no son audiencias aprobadas; una ampliación requiere revisar controles, textos, publicidad y compras.

| Opción | Consecuencia | Trabajo específico |
| --- | --- | --- |
| 18+ | No se admite deliberadamente a menores; reduce complejidad de consentimiento/capacidad | Aplicar la restricción de manera coherente, definir edad desconocida y datos de menores detectados, alinear tiendas y marketing |
| 16+ | Admite menores de 16–17; no equivale a mayoría de edad | Distinguir adolescentes/adultos, avisos comprensibles, tratamiento publicitario adecuado, revisar capacidad/representación en términos y compras |
| 13+ | Añade adolescentes de 13–15 | Revisión más amplia de comprensión, consentimiento parental cuando corresponda, seguridad social y requisitos de publicidad/tiendas por jurisdicción |

En Argentina la mayoría de edad es a los 18. La AAIP aplica autonomía progresiva al consentimiento de datos de menores; cuando el menor no tiene capacidad suficiente, requiere consentimiento de su representante y esfuerzos razonables de verificación. No fija un umbral general de 16 que habilite todos los tratamientos. Consentir datos y tener capacidad para contratar/comprar no son equivalentes. Fuentes: [Código Civil y Comercial, arts. 25–26](https://www.argentina.gob.ar/normativa/nacional/ley-26994-235975/actualizacion), [Resolución AAIP 4/2019, anexo, criterio 5](https://www.argentina.gob.ar/normativa/318874_res4AAIP_pdf/archivo).

## Qué significa aceptar

1. **Edad/elegibilidad:** determina acceso y trato por edad. Propuesta: pantalla neutral antes de crear invitado o iniciar los servicios afectados; guardar la categoría mínima necesaria y definir cuándo actualizarla. No solicitar DNI ni conservar fecha de nacimiento completa por defecto. Una autodeclaración no acredita por sí sola cumplimiento en cualquier mercado.
2. **Términos:** acto explícito con enlaces a términos, comunidad y compras incorporadas. Propuesta: registrar versión, idioma y fecha de servidor; verificar antes de permitir publicar nombres/grupos. Google exige aceptación previa al contenido de usuarios, no un mecanismo universal específico de registro: [UGC](https://support.google.com/googleplay/android-developer/answer/9876937?hl=en).
3. **Datos y publicidad:** informar privacidad y definir fundamento por finalidad. Consentimientos específicos, cuando correspondan, separados de la aceptación contractual y revocables. Ni «leí privacidad» ni «acepto términos» autorizan automáticamente publicidad personalizada/tracking. UMP y ATT tienen ámbitos propios; no comprueban edad/capacidad para comprar.

## Referencia para una eventual ampliación a 16+ (fuera del lanzamiento aprobado)

- No admitir menores de 16. Para edad desconocida, propuesta de lanzamiento: no inicializar publicidad hasta resolver elegibilidad/categoría; permitir consultar legal y soporte.
- Para 16–17, propuesta de producto: anuncios con tratamiento adolescente, sin personalización ni remarketing; categorías y creatividades apropiadas. Incluir anuncios con recompensa en esa configuración. Si la revisión local exige un tratamiento más restrictivo, aplicarlo.
- AdMob dispone actualmente de TFAT con `CHILD`, `TEEN` y `UNSPECIFIED`; `TEEN` deshabilita personalización/remarketing y aplica protecciones para adolescentes. TFCD/TFUA están deprecados en la configuración publicitaria del SDK. No inferir que UMP o todos los partners de mediación quedan configurados automáticamente: verificar cada integración. Fuentes: [AdMob](https://support.google.com/admob/answer/6219315?hl=en-GB), [SDK Android](https://developers.google.com/admob/android/targeting).
- Revisar compras de adolescentes con asesoramiento local: representación/autorización y evidencia necesarias según el acto. Una casilla «mis padres aceptan» no demuestra que hayan participado. Alternativa de producto para disminuir complejidad: restringir compras a adultos inicialmente; requiere controlar la categoría en app y servidor y revisar compras/restauraciones existentes.
- Declarar audiencia real 16–17 y 18+ en Google Play; clasificar el contenido real en ambas tiendas. No confundir edad de acceso con clasificación de contenido, ni asumir que 16+ evita reglas locales sobre niños. [Google Play](https://support.google.com/googleplay/android-developer/answer/9867159?hl=en).

Apple exige anuncios acordes a la clasificación y posibilidad de reportar anuncios inapropiados; también aplica al lanzamiento 18+. [App Review 2.5.18](https://developer.apple.com/app-store/review/guidelines/).

## Evidencia local y tareas comunes

`AdsProvider.tsx` llama a `AdsConsent.gatherConsent()` sin categoría de edad y después inicializa ads. No se encontró configuración propia `setRequestConfiguration` por edad en `src/ads`. La versión instalada de `react-native-google-mobile-ads` sí declara `ageRestrictedTreatment` en `src/types/RequestConfiguration.ts`; verificar la compilación nativa y adaptación en ambas plataformas antes de darlo por resuelto.

Para cualquier edad elegida hay que implementar o verificar acceso legal inicial, aceptación, borrado de invitados, purga/conservación, moderación y declaraciones de tiendas. Diseñar el arranque de Auth/Ads/Sentry según información y fundamentos aplicables. No se requiere por regla general DNI, selfie ni siete casillas legales; el control concreto debe ser proporcionado al tratamiento y mercados.

Con 18+ sigue siendo necesario aplicar la elegibilidad; no basta escribirla en términos mientras el funcionamiento y marketing admiten menores. Puede utilizarse la restricción de menores de Google Play cuando esté disponible, como complemento del flujo de la app, no como prueba universal de edad en ambas plataformas.
