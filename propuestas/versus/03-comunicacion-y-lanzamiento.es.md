# Cómo comunicar y lanzar la actualización de términos de Versus

Guía interna preparada el **9 de noviembre de 2026** y actualizada el **10 de noviembre de 2026** tras revisar nuevamente la API y la app. Los textos están listos para adaptar; las versiones, fechas y enlaces deben coincidir con lo efectivamente publicado. No se publicó ni se modificó la app como parte de esta propuesta.

## 1. Publicación y aviso a usuarios de iOS y Android

Recomendación para este cambio: publicar términos y reglas accesibles, mostrar un resumen dentro de la app y obtener una acción afirmativa antes del primer uso de Versus bajo las nuevas reglas. Incluirlo también en las novedades de las tiendas. Las notas de una actualización no prueban que cada usuario haya leído o aceptado un contrato.

Para una función opcional nueva, permitir «Ahora no» y mantener el acceso a las funciones anteriores que no dependan del cambio, siempre que sea viable. No condicionar la gestión de suscripciones, compras, soporte o eliminación de cuenta a aceptar una función nueva. Un cambio material sobre funciones existentes exige decidir el tratamiento de quienes no aceptan y de las prestaciones pagadas afectadas.

No surge de las fuentes aquí consultadas un plazo único de preaviso de 15 o 30 días para toda actualización de estos términos en ambas tiendas. Definir una fecha real y aviso suficiente según el alcance, los términos vigentes y la ley aplicable. Si se agrega un costo, el precio debe estar visible antes de cada confirmación; un aviso general anterior no lo reemplaza.

### Aviso dentro de la app

> **Actualizamos los Términos de uso**
>
> Incorporamos las reglas de Versus: crear cuesta 30 tokens, solo para quien lo crea, y los invitados juegan gratis. Explicamos el plazo para jugar, la puntuación, los empates y qué ocurre ante interrupciones o trampas. En esta versión no hay premios ni recompensas por participar o ganar.
>
> La nueva versión **[VERSIÓN]** rige desde el **[FECHA]**. Podés consultar los textos completos antes de decidir.
>
> **Ver Términos de uso · Ver Reglas de Versus**
>
> Al tocar «Aceptar y continuar a Versus», aceptás los Términos de uso y las Reglas de Versus indicados.
>
> **Aceptar y continuar a Versus** · **Ahora no**

Si la actualización también modifica compras, enlazar ese documento y resumir el cambio real. Informar privacidad por separado cuando cambie el tratamiento de datos; aceptar términos no equivale a consentir publicidad o seguimiento.

### Resumen antes de crear o jugar

> **Versus entre amigos**
>
> De 2 a 8 jugadores invitados, de 2 a 6 juegos y 48 horas desde la creación. El reloj de cada juego no se pausa y no hay pistas. Gana la mejor clasificación por puntos y desempates. Sin premios ni recompensas.
>
> **Crear cuesta 30 tokens, solo para quien lo crea. Los invitados juegan gratis. Se cobra por crear el desafío aunque después tus amigos no jueguen.**
>
> **Ver reglas completas**

La app ya muestra el precio junto a «Enviar versus» y abre una confirmación con costo, saldo y aviso de gratuidad para invitados. Conservar esa información; un texto como «Crear por 30 tokens» es una alternativa de presentación. Para invitados, «Jugar». No hace falta repetir un checkbox por cada juego si ya se aceptó la misma versión y no cambian las condiciones; sí debe seguir disponible el enlace y mostrarse cualquier costo antes de confirmarlo.

## 2. Evidencia de aceptación y límites de la implementación actual

Conservar la identidad de cuenta, fecha del servidor, versión exacta de términos y reglas, idioma y acción afirmativa. Mantener copia inmutable de cada versión y del resumen presentado; una URL cuyo contenido se reemplaza no basta para reconstruir qué se aceptó. Definir retención, acceso y tratamiento de estos registros en privacidad, minimizando los datos.

La base existente permite registrar una aceptación por usuario y versión de términos/comunidad. No tiene una versión de reglas de Versus independiente. Se puede incorporar el anexo a una versión inmutable de términos o agregar un registro específico; en ambos casos hay que poder identificar qué texto se aceptó y cuándo. Idealmente, el desafío conserva la versión de reglas y, si se cobra, el precio confirmado.

Implementación de cobro comprobada en los repositorios locales el 10 de noviembre de 2026:

- **API:** `src/modules/versus/limits.ts` fija `VERSUS_PRICE_TOKENS = 30`; `GET /versus/games` devuelve `price`. `versus.service.ts` crea el desafío y descuenta tokens únicamente al creador mediante `WalletService.spend`, en la misma transacción. Si falta saldo, la operación se revierte; los reintentos con la misma clave recuperan el desafío sin cobrar otra vez.
- **App:** `app/(tabs)/friends/versus/new.tsx` muestra el precio y solicita confirmación con `PurchaseConfirmationModal`; informa que los invitados no pagan y contempla saldo insuficiente. `useCreateVersus` conserva la clave para reintentos y actualiza los saldos tras el éxito.
- **Sin premios:** el cierre calcula clasificación y estadísticas, sin otorgar dinero, monedas, tokens u otras recompensas. El costo es por creación; no forma un pozo.
- Hay pruebas unitarias del precio y el cobro al creador, y pruebas de integración que cubren invitados sin cobro, saldo insuficiente, reintentos y creaciones concurrentes. La presencia de esas pruebas no equivale a haber ejecutado la suite de integración ni a verificar producción.

Puntos que siguen pendientes en el código local revisado:

- `daily-games-mobile/src/legal/StartupAgreementGate.tsx` deja entrar cuando existe una aceptación local, sin comprobar allí la versión nueva.
- `src/legal/acceptanceSync.ts` detecta el cambio de versión y borra la aceptación local, pero el mensaje reaparece **en el siguiente inicio**. Cambiar solo `LEGAL_TERMS_VERSION` no demuestra que se aceptó antes de jugar en la sesión actual.
- La API registra la aceptación en `src/modules/legal/legal-acceptance.service.ts`; no se identificó en el flujo revisado de Versus una comprobación que impida crear o jugar sin aceptar la versión vigente. Implementar el control en el acceso a Versus, incluida la validación del servidor, antes de basar el lanzamiento en esa exigencia.
- `src/legal/links.ts` todavía no incluye una página `versus`; agregar acceso desde Legal y desde crear/ver el desafío. Las reglas deben poder consultarse también antes de aceptar.

Se actualizaron las reglas y las cláusulas propuestas para reflejar el cobro ya implementado. No se modificaron los controles de aceptación ni los enlaces de la app como parte de esta revisión. Falta contrastar el despliegue con el código local y disponer de un procedimiento para corregir cobros o restituir tokens cuando corresponda.

## 3. App Store: qué anunciar y dónde

En **App Store Connect → Apps → Daylo → versión de iOS → What’s New in this Version / Novedades**, incluir el resumen del cambio junto con la función nueva. Apple documenta ese campo como las novedades de cada versión. [Referencia oficial](https://developer.apple.com/help/app-store-connect/reference/app-information/platform-version-information/).

Texto propuesto:

> Nuevo Versus: desafiá a tus amigos a resolver los mismos juegos y compará resultados. Crear un desafío cuesta 30 tokens; los invitados juegan gratis. No hay premios. Actualizamos los Términos de uso e incorporamos las Reglas de Versus sobre participación, puntuación e incidencias. Consultá los documentos en la sección Legal y antes de jugar Versus.

Mantener enlaces funcionales de términos, compras y privacidad en la app y los que correspondan en la ficha de tienda. Revisar las declaraciones de contenido y edad contra el producto real; que tus términos exijan 18 años no determina por sí solo la clasificación de la tienda.

Si utilizás la EULA estándar de Apple, actualizar tus términos del servicio no exige por sí solo sustituirla. Si ya utilizás una **EULA personalizada**, revisar y actualizar su texto en **App Information → License Agreement → Edit**, para los territorios correspondientes. No pegar estos términos como reemplazo sin adaptarlos a los [mínimos de EULA de Apple](https://www.apple.com/legal/internet-services/itunes/dev/minterms/). [Cómo gestionar la EULA](https://developer.apple.com/help/app-store-connect/manage-app-information/provide-a-custom-license-agreement/).

Apple exige reglas en la app y aclaración de su falta de participación para concursos, sorteos y rifas (§5.3.2). Versus sin premios se describe como modo competitivo; la guía no concluye que todo enfrentamiento sea un concurso regulado. Mantener reglas accesibles y la aclaración permite informar su funcionamiento también si cambia la mecánica. [App Review Guidelines, §5.3](https://developer.apple.com/app-store/review/guidelines/#gaming-gambling-and-lotteries).

### Nota para App Review

Usar después de publicar las reglas y comprobar los enlaces y el acceso de revisión:

> Versus is an asynchronous competitive puzzle mode between existing friends. The same puzzles are used for all participants. This version awards no prizes or rewards: no cash, physical goods, coins, tokens, gift cards, or redeemable benefits. Scores and standings are competition records only. There is no player-funded prize pool or transfer between players.
>
> Only the creator spends 30 in-app tokens to create a match; invitees join for free. The app displays the price and asks for confirmation before creation.
>
> Rules: [PUBLIC RULES URL]. In-app location: [ACTUAL PATH]. Review access: [TEST ACCOUNT / STEPS TO REACH A CHALLENGE].

Cuando esté implementada la aceptación previa a Versus, añadir: «The updated terms and rules are presented for acceptance before the first Versus use under this version». Facilitar un desafío accesible al revisor y la información necesaria para comprobarlo.

## 4. Google Play: qué anunciar y dónde

En **Play Console → Daylo → Test and release → Production → Create/Edit release**, completar las **notas de la versión**. Google admite hasta **500 caracteres Unicode por idioma**. [Instrucciones oficiales](https://support.google.com/googleplay/android-developer/answer/9859348?hl=en).

Se puede usar el mismo texto de novedades anterior, que queda por debajo de ese límite. Añadirlo en cada idioma de la ficha que se mantenga.

Revisar en **App content / Contenido de la aplicación** las declaraciones que realmente cambien: audiencia, clasificación de contenido, acceso para revisión y Seguridad de los datos, según corresponda. Mantener actualizada la URL de privacidad y enlazar los términos y reglas desde la app y el sitio. El campo de política de privacidad debe apuntar a privacidad; no usarlo para reemplazarla por los términos. [Guía de App content](https://support.google.com/googleplay/android-developer/answer/9859455?hl=en).

No hay que presentar un modo sin premios como un programa de fidelización con premios reales. Si después hay recompensas, analizar su naturaleza y la forma de acceso antes de completar declaraciones o habilitarlas. [Política de juegos y concursos de Google Play](https://support.google.com/googleplay/android-developer/answer/9877032?hl=en).

## 5. Secuencia de lanzamiento recomendada

1. Contrastar el despliegue con la implementación verificada: 30 tokens por crear, invitados gratis y sin premios. El descuento único y la confirmación de precio ya están implementados; verificar su funcionamiento en la versión de lanzamiento y definir el procedimiento de restitución.
2. Completar fecha y versiones y conservar las anteriores. Preparar una copia inmutable de términos y anexo con su historial de cambios.
3. Integrar las cláusulas de `02-integracion-y-futuras-recompensas.es.md` y publicar las reglas definitivas como `documents/es/versus.es.md`. El generador actual crea la ruta `/es/versus/`; resolver también la navegación y la exposición bajo el dominio que utiliza la app.
4. Verificar los enlaces: el README del repo menciona `daylogames.github.io/legal/`, mientras la app usa `daylogames.com/legal/es/`. Comprobar que ambos sirven la versión correcta y que las rutas no cambian.
5. Implementar el aviso, enlaces y aceptación de la versión antes del uso, y probar con usuario nuevo, existente, invitado, sesión abierta y versión anterior de la app. Si no se puede consultar o registrar la versión nueva, permitir reintentar o posponer Versus, sin registrar una aceptación ficticia.
6. Publicar las páginas antes de hacer que la app o la API exijan su aceptación. Coordinar `LEGAL_TERMS_VERSION` con el despliegue; cambiar la versión de comunidad solo si ese documento también cambia. Durante un despliegue gradual, impedir que clientes anteriores eludan el control o cobren bajo reglas distintas.
7. Completar las novedades, acceso de revisión y declaraciones de tiendas. Lanzar cuando el texto, las funciones y las fechas coincidan. Conservar evidencia de publicación y del aviso mostrado.

No es necesario enviar un email o push a todos por el solo hecho de este cambio. Puede complementar el aviso cuando sea apropiado y exista un canal habilitado; no sustituye la comunicación dentro de la app ni la aceptación cuando corresponda.
