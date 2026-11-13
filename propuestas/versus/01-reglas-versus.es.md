# Reglas del modo Versus de Daylo Games

**BORRADOR de trabajo — no vigente.** Preparado el 9 de noviembre de 2026 y actualizado el 10 de noviembre de 2026 tras revisar nuevamente la API y la app, para el lanzamiento en Argentina. Antes de publicarlo: completar fecha y versión, contrastar con la versión de producción y revisar jurídicamente. Las notas entre corchetes son instrucciones internas y deben eliminarse del texto público.

Versión propuesta: `versus-v1`. Vigentes desde: **[FECHA DE ENTRADA EN VIGENCIA]**.

## 1. Responsable y alcance

Versus es un modo competitivo de juegos de lógica y palabras de Daylo Games, organizado y operado por **Guido Tomas Botta**, persona física en Argentina, con domicilio de contacto en **Calle 152 6352, Oficina 314 Downtown, B1886 Guillermo Enrique Hudson, provincia de Buenos Aires, Argentina**. Contacto: **support@daylogames.com**.

Estas reglas complementan los [Términos de uso](https://daylogames.com/legal/es/terms/), las [Condiciones de compras y suscripciones](https://daylogames.com/legal/es/purchases/) y las [Reglas de comunidad](https://daylogames.com/legal/es/community/). La [Política de privacidad](https://daylogames.com/legal/es/privacy/) explica el tratamiento de datos. Estas reglas describen específicamente Versus, sin reducir tus derechos legales ni las condiciones de compras ya realizadas.

## 2. Quiénes participan y cómo se crea un desafío

El modo está disponible para personas de **18 años o más en Argentina**, con una cuenta habilitada y un nombre de usuario. No requiere una suscripción para participar.

Quien crea el desafío elige entre **1 y 7 amigos** de Daylo Games y entre **2 y 6 juegos diferentes** del catálogo habilitado. Se invita, por lo tanto, a un total de **2 a 8 jugadores**, incluido quien lo crea. Las dificultades disponibles se muestran al configurar el desafío.

Daylo selecciona un puzzle para cada juego dentro del catálogo y las dificultades elegidas. Todos los participantes reciben el mismo puzzle en cada juego del desafío. La selección del contenido no implica un sorteo de premios. Los puzzles pueden haber estado disponibles antes en otras modalidades.

Un invitado puede rechazar el desafío antes de iniciar o abandonar cualquiera de sus juegos; el rechazo es definitivo para ese desafío y lo excluye de su clasificación. Quien lo crea no tiene esa opción de rechazo. Recibir una invitación no genera un cobro al invitado.

No hace falta que todos jueguen al mismo tiempo ni que todos los invitados lleguen a jugar. La falta de respuesta de un invitado no cancela automáticamente el desafío.

## 3. Costo y ausencia de premios

Crear un Versus cuesta **30 tokens por desafío**, a cargo únicamente de quien lo crea. Los invitados participan sin gastar monedas ni tokens. Antes de confirmar, la app muestra la cantidad exacta que se descontará y solicita confirmar el gasto. El descuento se realiza una sola vez al crearse correctamente el desafío; no se cobra por un intento de creación fallido ni nuevamente por reintentar la misma solicitud. Si el saldo no alcanza, el desafío no se crea y no se realiza el descuento.

El costo corresponde a crear el desafío, independientemente de su resultado y de cuántos invitados decidan jugar. Si todos rechazan o no juegan, no hay devolución automática por esa sola circunstancia. Los errores de cobro, fallas del servicio y demás derechos legales pueden reclamarse según §7. Una membresía no exime de este costo salvo que su oferta lo indique expresamente.

Versus **no entrega premios ni recompensas por participar, ganar o alcanzar una posición**: no otorga monedas, tokens, artículos, dinero, bienes físicos, descuentos ni beneficios canjeables fuera de Daylo. Los puntos, posiciones y estadísticas son únicamente registros competitivos; no integran un saldo gastable o canjeable.

No hay un pozo formado por aportes de jugadores ni transferencia de saldos de los perdedores a los ganadores. No se permite usar este modo para organizar apuestas, pagos o acuerdos de premio entre participantes.

Los costos de tu conexión o del servicio de tu dispositivo dependen de sus respectivos proveedores.

## 4. Plazo, intentos y reloj

Cada desafío permanece abierto durante **48 horas desde su creación**, con independencia de cuándo lo vea cada invitado. La app muestra su vencimiento. Puede cerrarse antes cuando todos los participantes que no lo hayan rechazado hayan terminado, perdido o abandonado todos sus juegos.

Cada jugador dispone de una participación por juego. Podés retomar un juego todavía abierto dentro del plazo; volver a abrirlo no reinicia el reloj ni permite repetir un resultado ya finalizado. Salir puede hacer que pierdas el estado local del tablero.

El tiempo empieza cuando se inicia el juego en el servidor y **no se pausa** al salir, cerrar la app, cambiar de dispositivo o perder conexión. El servidor verifica el tiempo, con una tolerancia técnica de hasta **tres segundos** por carga y comunicación. Un cronómetro redondeado en pantalla no implica que dos tiempos registrados sean iguales.

En Versus **no hay pistas**. Perder, abandonar o no enviar una solución válida antes del cierre da **0 puntos** para ese juego. Un resultado debe llegar al servidor y ser validado dentro del plazo; el envío local por sí solo no lo confirma. Los controles contra envíos inválidos reiterados pueden limitar temporalmente nuevos intentos de validación.

## 5. Puntuación y empates

En cada juego se ordenan de menor a mayor los tiempos de las soluciones válidas. Dos tiempos registrados exactamente iguales comparten el mejor puesto correspondiente; el siguiente puesto salta las posiciones compartidas, por ejemplo: 1.º, 2.º, 2.º, 4.º.

Para cada solución válida, los puntos se calculan así: **10 × (N − puesto) / (N − 1)**, redondeados al entero más próximo, con los medios puntos hacia arriba. **N** es el número de participantes que no rechazaron el desafío al cierre, incluidos quienes no jugaron o no resolvieron. Quien no resolvió no tiene puesto en ese juego y suma 0.

Por ejemplo, con cuatro participantes los puestos 1.º, 2.º, 3.º y 4.º otorgan 10, 7, 3 y 0 puntos. Si solo queda un participante porque los demás rechazaron, obtiene 10 puntos por cada juego resuelto; no se cancela automáticamente por quedar solo.

La clasificación final aplica estos criterios, en este orden:

1. Mayor suma de puntos.
2. Mayor cantidad de primeros puestos en juegos, incluidos los compartidos.
3. Mayor cantidad de juegos resueltos.
4. Menor suma de los tiempos de los juegos resueltos.

Si persiste la igualdad, se comparte el puesto final. No se utiliza un sorteo para desempatar. Una clasificación con cero puntos tampoco genera derecho a recompensa alguna.

Los resultados de los demás no se adelantan durante el desafío. Al cerrarse, se publican las posiciones y los puntos correspondientes; su confirmación puede requerir procesamiento o actualización de la app.

## 6. Juego limpio

No está permitido obtener ventaja mediante automatización, programas que resuelvan por vos, modificación del cliente, manipulación de tiempos o comunicaciones, explotación de errores, cuentas múltiples para alterar el resultado, suplantación, colusión ni intercambio de soluciones durante el desafío.

Daylo puede investigar anomalías y adoptar medidas proporcionales, como invalidar resultados obtenidos indebidamente, excluir a un participante o suspender su acceso conforme a las Reglas de comunidad. Comunicaremos la medida y cómo pedir revisión, salvo que una restricción legal o la protección de la investigación justifique diferir detalles. Una sospecha no implica por sí sola la pérdida de compras o saldos legítimos.

## 7. Fallas, interrupciones, cancelación y reclamos

La conexión, el dispositivo y los servicios técnicos pueden afectar una partida. Si salís o perdés conexión, el reloj sigue corriendo y el plazo de 48 horas continúa. Una desconexión no garantiza una repetición ni la corrección de un tiempo.

Si existe una falla de Daylo que impida jugar o validar resultados de manera razonable, o se detecta un problema de integridad, podemos suspender o anular los resultados afectados o cancelar el desafío, procurando una solución proporcional y explicando el motivo. Cuando corresponda por una falla del servicio, se restituirán los tokens efectivamente cobrados por la creación. Esto no reemplaza otras reparaciones o devoluciones que correspondan por ley.

No prometemos restaurar una posición concreta cuando el resultado no pueda verificarse. Revisaremos el caso y los registros disponibles; un error de Daylo no queda automáticamente a cargo del usuario.

Para reclamar, escribí a **support@daylogames.com** con tu código de amigo, el desafío, el juego, la fecha aproximada y una descripción del problema. No envíes contraseñas ni tokens de sesión. Recomendamos avisar cuanto antes para facilitar la revisión de registros temporales; esa recomendación no acorta plazos legales ni exige renunciar a derechos.

## 8. Visibilidad e historial

Los participantes pueden ver los nombres, avatares y el progreso de juego que muestra la función, y al cierre las posiciones y puntos. Los resultados pueden integrar tus estadísticas y comparaciones con amigos, según las funciones de Daylo y las reglas de bloqueo y eliminación.

El historial visible de desafíos finalizados abarca **30 días**; no es un archivo permanente. Las estadísticas acumuladas pueden mantenerse mientras conserves tu cuenta. Los plazos de conservación de los distintos datos se explican en la Política de privacidad.

## 9. Cambios futuros

Daylo puede ofrecer nuevas versiones de Versus con configuraciones diferentes, informadas antes de crear o comenzar a jugar. Los cambios relevantes de costo, puntuación, plazo o recompensas se comunicarán antes de aplicarse y se pedirá aceptación cuando corresponda. No se incorporan retroactivamente a un desafío ya creado, salvo medidas justificadas para corregir fallas o proteger la integridad, con las reparaciones que correspondan.

Esta versión no promete premios futuros. Agregar recompensas requiere publicar previamente sus condiciones específicas, incluidos destinatarios, cantidades, empates, entrega y cancelación; no basta con modificar un mensaje comercial.

## 10. Apple, Google y derechos legales

Apple y Google no organizan, patrocinan, administran ni participan en los desafíos de Versus. El responsable de este modo es el identificado en §1.

Se aplica la legislación de la República Argentina y se conservan los derechos irrenunciables de consumidores y usuarios. Podés acudir a las autoridades o tribunales competentes sin agotar previamente el canal de soporte. Estas reglas no establecen una exención general de responsabilidad ni una renuncia a reclamos.
