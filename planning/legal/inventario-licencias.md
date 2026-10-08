# Inventario de licencias y recursos para cerrar créditos

Revisión local: 7 de octubre de 2026. Material para el equipo, visible en el repositorio público. No certifica derechos ni sustituye avisos de la versión distribuida.

## Picture Cross

Se cotejaron los 378 JSON del catálogo local con los identificadores de [créditos](public/credits.es.md): las 251 obras atribuidas coinciden, sin obras faltantes ni sobrantes en esa comparación.

- 37 obras atribuidas a Delapouite y 214 a Lorc, adaptadas a 330 tableros en total; metadata `CC-BY-3.0`.
- 48 tableros sin licencia/atribución de tercero en metadata: eso no prueba autoría ni propiedad. Confirmar derechos con sus creadores.
- El catálogo local no demuestra qué contenido quedó publicado en producción ni qué partidas se distribuyen. Comparar el inventario de release y contenido servido antes de cerrar el crédito.
- Falta cotejar los originales y enlaces de cada obra. No se inventaron URLs de originales a partir de nombres de archivo.

La [licencia CC BY 3.0](https://creativecommons.org/licenses/by/3.0/) permite adaptación/uso comercial con condiciones de atribución; conservar autores, título cuando corresponda, avisos recibidos, enlace a licencia/material y explicación de adaptación. No atribuir respaldo de los autores.

## Listas de palabras: fuentes encontradas

| Uso | Evidencia local | Fuentes identificadas | Qué falta verificar |
| --- | --- | --- | --- |
| Anygram EN | `scripts/anygram/README.md`; `words.en.txt` | Intersección de SCOWL/wamerican y cracklib-small, menos bloqueadas | Versiones originales, avisos y licencia de cada fuente; no basta el copyright abreviado del README |
| Anygram ES | `scripts/anygram/build-words-es.sh`; `sources.es.sha256` | wspanish 1.0.28, corpus fijo de Gutenberg, Common Voice en commit 2d05d6a840f15361938145738d10d290c50800fd | Licencias originales, autores/obras y derechos territoriales; trazabilidad de las listas ya utilizadas y contenido publicado |
| Wordle EN/ES | `scripts/wordle/build-words.sh`; `sources.sha256` | ENABLE en commit 694bf9529e986f9175dcbf5fe5875d111941b708, wspanish 1.0.28, Common Voice en el commit anterior | Licencias originales y avisos; correspondencia con listas servidas y respuestas de release |

Los scripts identifican Common Voice como CC0 y wspanish/ENABLE como fuentes de dominio público. Esas declaraciones locales orientan la revisión; no se trataron como comprobación independiente. La verificación web de los archivos originales de Common Voice/ENABLE no pudo completarse en esta revisión. En particular, dominio público de libros en EE.UU. no acredita por sí solo el estado de cada obra en Argentina.

Fuente de trazabilidad: repositorio hermano `daily-games-api`. No se regeneraron listas ni se modificó contenido publicado.

## Dependencias directas runtime de mobile

Se leyeron `package.json` de mobile y los paquetes instalados localmente: 37 dependencias directas runtime, 36 declaran MIT y una Apache-2.0. La columna de archivos solo busca avisos en la raíz del paquete. No considera dependencias transitivas, Pods/Gradle, SDK incluidos indirectamente, herramientas de build ni el binario final.

| Paquete | Versión instalada | Licencia declarada | Archivos encontrados en raíz |
| --- | --- | --- | --- |
| `@expo/vector-icons` | 15.1.1 | MIT | LICENSE |
| `@react-native-async-storage/async-storage` | 2.2.0 | MIT | LICENSE |
| `@react-native-community/netinfo` | 12.0.1 | MIT | LICENSE |
| `@react-native-google-signin/google-signin` | 16.1.5 | MIT | LICENSE |
| `@sentry/react-native` | 7.11.0 | MIT | LICENSE.md |
| `@supabase/supabase-js` | 2.112.4 | MIT | LICENSE |
| `@tanstack/react-query` | 5.102.2 | MIT | LICENSE |
| `expo` | 57.0.22 | MIT | LICENSE |
| `expo-apple-authentication` | 57.0.2 | MIT | LICENSE |
| `expo-build-properties` | 57.0.22 | MIT | LICENSE |
| `expo-constants` | 57.0.18 | MIT | LICENSE |
| `expo-crypto` | 57.0.3 | MIT | LICENSE |
| `expo-dev-client` | 57.0.19 | MIT | LICENSE |
| `expo-font` | 57.0.4 | MIT | LICENSE |
| `expo-haptics` | 57.0.3 | MIT | LICENSE |
| `expo-image` | 57.0.5 | MIT | LICENSE |
| `expo-linear-gradient` | 57.0.2 | MIT | LICENSE |
| `expo-linking` | 57.0.10 | MIT | LICENSE |
| `expo-localization` | 57.0.2 | MIT | LICENSE |
| `expo-router` | 57.0.21 | MIT | No encontrado en raíz |
| `expo-secure-store` | 57.0.4 | MIT | LICENSE |
| `expo-status-bar` | 57.0.1 | MIT | LICENSE |
| `expo-system-ui` | 57.0.4 | MIT | LICENSE |
| `expo-web-browser` | 57.0.3 | MIT | LICENSE |
| `i18next` | 26.4.0 | MIT | LICENSE |
| `react` | 19.2.3 | MIT | LICENSE |
| `react-i18next` | 17.0.12 | MIT | LICENSE |
| `react-native` | 0.86.3 | MIT | LICENSE |
| `react-native-gesture-handler` | 2.32.0 | MIT | LICENSE |
| `react-native-google-mobile-ads` | 17.2.0 | Apache-2.0 | LICENSE |
| `react-native-purchases` | 10.11.0 | MIT | LICENSE |
| `react-native-reanimated` | 4.5.1 | MIT | LICENSE |
| `react-native-safe-area-context` | 5.7.0 | MIT | LICENSE |
| `react-native-screens` | 4.26.2 | MIT | LICENSE |
| `react-native-svg` | 15.15.4 | MIT | LICENSE |
| `react-native-worklets` | 0.10.1 | MIT | LICENSE |
| `zod` | 4.4.3 | MIT | LICENSE |

La licencia declarada no prueba que un aviso abreviado cubra todos los archivos del paquete. Reunir textos y notices aplicables de dependencias efectivamente distribuidas, incluidas transitivas y nativas, antes de generar una página/archivo final de avisos. Conservar copyrights y avisos según cada licencia.

No se encontraron fuentes `.ttf` en `mobile/assets` en la búsqueda local. Eso no demuestra ausencia de fuentes: las dependencias de iconos pueden incorporarlas. Inventariar fuentes/iconos de la build real y sus licencias.

## Recursos del equipo y criterio de cierre

La [documentación oficial de generación de imágenes de ChatGPT](https://learn.chatgpt.com/docs/image-generation) indica que atribuir OpenAI por imágenes generadas es opcional. La mención en créditos describe el proceso elegido por el equipo; no se considera prueba de derechos exclusivos ni reemplazo de revisar las condiciones contractuales aplicables a su cuenta y fecha de generación.

El usuario confirmó que el logo, avatares e ilustraciones propios se elaboran mediante **generación con IA y modificaciones posteriores por el equipo**, con participación alta de IA. El usuario confirmó **ChatGPT Plus con cuenta personal para todos esos recursos**, generados durante los últimos 45 días: aproximadamente **23 de agosto a 7 de octubre de 2026**. Es un intervalo orientativo basado en la declaración del usuario, no una comprobación de cada archivo.

El 8 de octubre de 2026 el usuario confirmó que generaron los recursos **solo con descripciones escritas, sin subir imágenes de referencia**. No se informó utilización de imágenes ajenas como entradas. Esta declaración describe el proceso; no constituye una revisión de cada prompt o archivo.

Herramienta, plan, período y tipo de entrada quedan identificados. Sigue pendiente cotejar las condiciones contractuales aplicables a esa cuenta/período y revisar prompts y archivos finales; la documentación de producto consultada sobre atribución no establece por sí sola todos los permisos contractuales. No se considera cerrada la revisión solo por tratarse de un plan pago.

Registrar por recurso o lote: herramienta/modelo y fecha, cuenta/plan utilizado, condiciones aplicables entonces, descripciones escritas, salida inicial, modificaciones propias y archivo final. Si en futuras piezas se incorporan imágenes de referencia, registrar además su fuente y permiso de uso. Mantener archivos de trabajo y evidencias en un espacio privado; este inventario público solo debe contener el resumen necesario. Comprobar el derecho a utilizar las entradas y distribuir comercialmente el resultado. Las condiciones del proveedor no prueban por sí solas exclusividad ni ausencia de derechos ajenos.

Cotejar también los 48 tableros sin atribución y materiales promocionales con ese proceso; no asumir su origen únicamente por falta de metadata. Los materiales de game-icons.net conservan atribuciones/licencia aun cuando se editen con IA. Si alguna pieza deriva de un diseñador/banco de recursos, verificar además permiso/cesión y condiciones de esa fuente.

Créditos quedará cerrado cuando el inventario corresponda a lo distribuido, las fuentes/licencias originales estén comprobadas, estén disponibles los avisos exigibles y se pruebe acceso a ellos desde app/sitio. Mantener el marcador de pendiente hasta entonces.
