# Integración de Versus en los documentos generales y futuras recompensas

**BORRADOR interno — no vigente.** Preparado el 9 de noviembre de 2026 y actualizado el 10 de noviembre de 2026 tras comprobar el cobro de 30 tokens al creador. Acompaña a [las reglas propuestas](01-reglas-versus.es.md). Las cláusulas siguientes son textos para integrar; las instrucciones editoriales no deben publicarse. No modificar la fecha vigente hasta fijar el lanzamiento.

## 1. Términos generales: incorporación del anexo

En §1, agregar las Reglas de Versus a los documentos incorporados. En §4, agregar:

> **Modo Versus.** Daylo ofrece desafíos competitivos entre amigos, sujetos a las [Reglas del modo Versus](https://daylogames.com/legal/es/versus/). Allí se explican la participación, los costos que correspondan, el plazo, la puntuación, los empates, las incidencias y el juego limpio. La app debe mostrar las condiciones aplicables antes de crear un desafío o comenzar a jugar. Los puntos y posiciones de Versus son registros competitivos y no equivalen a monedas, tokens ni premios. En su versión actual, Versus no entrega recompensas por participar ni por ganar y no forma un pozo entre jugadores. Las condiciones de un desafío no se modifican retroactivamente por publicar una nueva versión de estas reglas, sin perjuicio de correcciones justificadas por fallas o fraude y de los derechos que correspondan.

La URL `/versus/` es una ruta propuesta: debe existir y abrirse correctamente antes de incorporar este enlace al texto vigente y a la app.

## 2. Términos generales: bienes virtuales

Reemplazo propuesto para el primer párrafo de §6, manteniendo el resto de esa sección:

> Las **monedas** y los **tokens** son dos bienes virtuales distintos para usar exclusivamente dentro de Daylo Games, según las funciones y precios informados antes de cada operación. Las monedas sirven para pistas y personalización; los tokens, para los accesos y funciones identificados en la app y en las Condiciones de compras. No existe conversión entre ambos saldos. No son depósitos, criptomonedas ni instrumentos de inversión; no otorgan un derecho de rescate por dinero, bienes físicos, tarjetas de regalo ni otros premios o beneficios externos. No se transfieren entre jugadores y no se autoriza su venta o intercambio fuera del servicio. Esto no elimina tus derechos a una devolución o reparación cuando corresponda por una compra o falla del servicio.
>
> Podemos otorgar saldos conforme a promociones informadas, consumirlos al confirmar funciones que los requieran y corregir movimientos duplicados, errores comprobados, fraude o reembolsos de tienda, con información y posibilidad de revisión cuando corresponda. No podemos descontarlos arbitrariamente ni modificar retroactivamente una compra. **Las monedas y tokens no vencen por el paso del tiempo ni por inactividad mientras se conserve la cuenta**. La pérdida de acceso, la eliminación y las compras se rigen por las condiciones específicas y los derechos legales aplicables.

No incorporar una autorización general para «vencer» saldos: contradice las condiciones vigentes y la regla de Apple sobre moneda comprada mediante IAP. [Apple, §3.1.1](https://developer.apple.com/app-store/review/guidelines/#in-app-purchase).

## 3. Compras: incluir la creación con tokens

La API y la app actuales implementan la creación por 30 tokens. Reemplazar el punto de tokens de §2 del documento de compras por:

> **Tokens:** sirven para abrir días anteriores y etapas de desafíos, según los requisitos de progreso, y para crear desafíos Versus. Crear un Versus cuesta **30 tokens por desafío**, únicamente para quien lo crea. La app muestra el costo y pide confirmación antes de descontarlo. El gasto no se redistribuye entre los participantes; los invitados participan sin gastar tokens. Si el desafío no llega a crearse, no se realiza el cobro. Versus no entrega premios ni recompensas por participar o ganar. Sus condiciones se explican en las Reglas de Versus.

La implementación revisada no exime del costo de creación a suscriptores Pro. No presentar ese beneficio como incluido en una membresía sin que la oferta y la implementación lo garanticen.

## 4. Privacidad: incluir el funcionamiento de Versus

Texto propuesto para completar §4, además de amigos y grupos:

> En Versus, los demás participantes pueden ver tu nombre, código de amigo, avatar y progreso de participación, y al cierre las posiciones y puntos que muestre la función. Los resultados también se utilizan para tus estadísticas de Versus y las comparaciones con amigos. Los bloqueos y la eliminación de cuenta pueden ocultar o retirar datos conforme al funcionamiento de esas funciones.

Antes de completar §9, verificar en producción los plazos del proceso de limpieza. El código local elimina las jugadas detalladas una vez pasados 30 días desde el vencimiento y los desafíos una vez pasados 90 días, mediante un proceso periódico; las estadísticas acumuladas siguen ligadas a la cuenta. El historial visible de 30 días es una ventana de consulta, no el plazo de borrado de todos los datos. Incorporar también la finalidad y el plazo real del registro de aceptación de documentos; no inventar una retención que no esté definida.

## 5. Plantilla para una futura versión con recompensas virtuales fijas

**No publicar ni habilitar como parte de la versión sin premios.** Esta plantilla requiere completar todos los campos y verificar la mecánica, las políticas de tiendas y el encuadre legal antes de activarla. No cubre un pozo ni premios externos.

> **Recompensas de esta edición.** En el desafío **[IDENTIFICACIÓN Y VERSIÓN]**, Daylo otorga **[CANTIDAD Y TIPO EXACTOS DE BIEN VIRTUAL]** a **[PUESTOS O CONDICIONES; NÚMERO DE BENEFICIARIOS]**. La recompensa está predefinida por Daylo y no se calcula a partir de los tokens aportados por otros jugadores ni se transfiere desde sus saldos. El costo de crear el desafío es **[CANTIDAD Y MONEDA VIRTUAL; QUIÉN PAGA; O GRATUITO]**, informado antes de confirmar.
>
> El desafío admite **[MÍNIMO Y MÁXIMO]** participantes y **[CONDICIÓN PARA CONSIDERARLO VÁLIDO]**. Abre **[FECHA Y HORA, ZONA HORARIA]** y cierra **[FECHA Y HORA, ZONA HORARIA]**. La clasificación se define según **[REGLA Y VERSIÓN]**. Ante empate que alcance un puesto premiado se aplica **[REPARTO EXACTO, REDONDEOS Y DESTINO DEL REMANENTE, O RECOMPENSA COMPLETA PARA CADA EMPATADO]**. Si no hay resultados válidos, **[CONSECUENCIA]**.
>
> Se acredita en la cuenta participante dentro de **[PLAZO MÁXIMO CONCRETO]** desde el cierre y validación. Una verificación de integridad pendiente se comunica, con motivo y **[PLAZO DE REVISIÓN Y CANAL]**. No requiere comprar otro producto para recibirla. Los bienes otorgados solo se usan dentro de Daylo, no se transfieren entre jugadores ni se canjean por dinero o beneficios externos. Los saldos de monedas y tokens conservan las condiciones de no vencimiento.
>
> Si Daylo cancela el desafío o no se alcanza el mínimo exigido, **[RESTITUCIÓN DEL COSTO, DESTINATARIO Y PLAZO]**. Si una falla impide entregar la recompensa anunciada, se informa y se ofrece **[SOLUCIÓN CONCRETA, SIN SUSTITUCIÓN UNILATERAL POR MENOR VALOR]**, respetando los derechos legales. El abandono y el fraude se tratan según **[REGLAS EXACTAS]**, sin afectar saldos o compras ajenos a la infracción.
>
> Organiza y responde **Guido Tomas Botta**, con los datos de contacto indicados en las Reglas de Versus. Apple y Google no patrocinan, organizan ni administran esta edición.

Conservar la ficha y las reglas que correspondían a cada desafío; cambiar la oferta solo para desafíos futuros. La estructura con recompensas predefinidas facilita explicar el producto, pero no garantiza por sí misma que no sea una actividad regulada.

## 6. Límites jurídicos de esta base

Esta propuesta sirve para informar y documentar el acuerdo; **no garantiza inmunidad frente a reclamos ni aprobación de las tiendas**. Requiere revisión profesional para los mercados habilitados, inicialmente Argentina. Los artículos 4 y 37 de la [Ley 24.240](https://www.argentina.gob.ar/normativa/nacional/ley-24240-638/actualizacion) exigen información clara y limitan las cláusulas abusivas; una aceptación no convalida renuncias a derechos del consumidor.

No incorporar un pozo, premios en dinero, tarjetas de regalo, descuentos externos, bienes revendibles o transferencias entre jugadores bajo esta misma redacción. Esos cambios necesitan un análisis nuevo de la mecánica y de las jurisdicciones donde se ofrezca.

La prohibición general de Google citada en la sugerencia se refiere a participar con dinero o artículos comprados para obtener un premio con valor monetario real. El apartado de fidelización trata recompensas con valor real asociadas a transacciones; no es una obligación general de proporción fija para toda recompensa interna de un videojuego. Esta distinción no acredita por sí sola que una variante concreta esté permitida. [Política de Google Play](https://support.google.com/googleplay/android-developer/answer/9877032?hl=en).
