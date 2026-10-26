# Seguimiento interno de información legal faltante

Este archivo reúne las verificaciones y los datos que todavía faltan. No se copia al directorio `site/` ni se publica en el sitio legal. Quitar los avisos de los documentos públicos no significa que estos puntos estén resueltos.

Última revisión: 26 de octubre de 2026.

## Prioridad alta — operación, privacidad y derechos

### 1. Bases jurídicas por finalidad y mercado

- **Documento relacionado:** Política de privacidad, §3.
- **Falta:** asignar una base jurídica concreta a cada finalidad (prestación del servicio, cumplimiento de obligaciones, prevención de abuso, publicidad, diagnóstico, soporte y funciones sociales) para Argentina y cada mercado futuro.
- **Definición necesaria:** determinar cuándo se usa consentimiento, cuándo resulta aplicable otra base y cómo se documenta la elección. La lectura de la política no debe considerarse consentimiento.
- **Criterio de cierre:** matriz finalidad/dato/base jurídica/mercado revisada y texto público actualizado.

### 2. Inventario real de proveedores y encargados

- **Documento relacionado:** Política de privacidad, §5.
- **Falta:** confirmar servicios activos y configuración de Supabase, Render, Cloudflare/R2, Sentry, AdMob, RevenueCat, Apple y Google; identificar partners publicitarios, entidades contratadas y cualquier proveedor usado para soporte.
- **Datos a reunir:** entidad legal, función, categorías de datos, región de procesamiento, plazo de retención, subencargados y enlace de privacidad.
- **Criterio de cierre:** inventario contrastado contra producción y consolas, con enlaces y texto público corregidos.

### 3. Transferencias internacionales

- **Documento relacionado:** Política de privacidad, §6.
- **Falta:** países o regiones reales de almacenamiento y acceso para cada proveedor, mecanismo jurídico aplicable a cada transferencia y salvaguardas disponibles.
- **Criterio de cierre:** mapa de transferencias validado, mecanismo documentado y canal definido para solicitar información sobre salvaguardas.

### 4. Flujo de privacidad publicitaria y ATT

- **Documento relacionado:** Política de privacidad, §7.
- **Falta:** verificar en builds y consolas el flujo real de consentimiento, rechazo y revocación; revisar ATT en iOS y el acceso a “Privacidad de anuncios”.
- **Definición necesaria:** tratamiento para usuarios según edad y región, estado por defecto y efecto de retirar una autorización.
- **Criterio de cierre:** pruebas en iOS y Android, capturas/registro del flujo y descripción pública consistente con la implementación.

### 5. Cumplimiento de plazos de conservación

- **Documentos relacionados:** Política de privacidad, §9; Eliminación de cuenta, §3.
- **Falta:** comprobar en producción los plazos declarados, incluida la limpieza diaria, copias de seguridad y eliminación en proveedores.
- **Datos a completar:** retención efectiva de registros técnicos de Sentry, Render y Cloudflare, además de cualquier otro proveedor confirmado.
- **Criterio de cierre:** prueba de punta a punta con fechas, jobs monitoreados y tabla de retención actualizada si existen diferencias.

### 6. Procedimiento de acceso, corrección, exportación y supresión

- **Documentos relacionados:** Política de privacidad, §10; Eliminación de cuenta, §2.
- **Falta:** definir verificación segura de titularidad, responsables, pasos de ejecución, alcance sobre registros/proveedores, excepciones de retención y confirmación del resultado.
- **También falta:** verificar qué exportación ofrece la versión final y cómo se entrega lo que no incluya la descarga automática.
- **Criterio de cierre:** procedimiento documentado y ensayado que permita cumplir los plazos legales, con plantillas de respuesta y evidencia de ejecución.

### 7. Control de edad mínima

- **Documento relacionado:** Política de privacidad, §11.
- **Falta:** comprobar que el primer uso incluya la declaración de tener 18 años o más y que no pueda omitirse por rutas alternativas.
- **Criterio de cierre:** prueba en instalación limpia y cuentas nuevas de iOS y Android, con comportamiento definido ante una edad no admitida.

### 8. Aceptación de términos

- **Documento relacionado:** Términos de uso, §1.
- **Falta:** implementar y verificar aceptación explícita antes del uso y antes de crear contenido social, incluida la reaceptación cuando haya cambios relevantes.
- **Datos a guardar:** versión aceptada, identidad, fecha/hora y contexto de aceptación.
- **Criterio de cierre:** flujo probado, registro auditable y versión de los términos alineada con backend y app.

### 9. Seguimiento de soporte y vencimientos

- **Documento relacionado:** Soporte, sección “Contacto”.
- **Falta:** poner en funcionamiento un procedimiento para registrar recepción, prioridad, responsable, vencimiento legal, estado y resolución de consultas, reportes y solicitudes de datos.
- **Restricción:** no asumir respuesta garantizada en 24 horas ni revisión diaria si la operación no puede sostenerlo.
- **Criterio de cierre:** bandeja o sistema operativo probado, alertas de vencimiento y responsable de cobertura definido.

## Prioridad alta — compras y cuentas

### 10. Conservación de saldos y compras al resolver cuentas duplicadas

- **Documento relacionado:** Términos de uso, §3.
- **Falta:** validar qué ocurre con monedas, tokens, compras no consumibles y suscripciones cuando el usuario elige cuál cuenta conservar.
- **Criterio de cierre:** reglas de merge/reemplazo documentadas, confirmación clara en UI y casos de prueba sin pérdida silenciosa de bienes pagados.

### 11. Ofertas introductorias

- **Documento relacionado:** Compras, §3.
- **Falta:** comprobar que la app muestra duración, elegibilidad y precio real de cada oferta configurada, incluidas las opciones anuales.
- **Criterio de cierre:** contraste de productos de App Store Connect y Play Console contra paywalls reales en ambas plataformas.

### 12. Renovación, cancelación, pruebas y cambios de precio

- **Documento relacionado:** Compras, §4.
- **Falta:** validar por plataforma los textos sobre cancelación, pruebas, momento de los cargos, upgrades/downgrades y cambios de precio.
- **Restricción:** no aplicar automáticamente una regla de 24 horas a ambas tiendas.
- **Criterio de cierre:** texto separado cuando Apple y Google difieran, revisado contra configuración y documentación vigente de cada tienda.

### 13. Restaurar compras y transferencia de suscripciones

- **Documento relacionado:** Compras, §5.
- **Falta:** probar “Restaurar compras” en iOS y Android con una cuenta de juego nueva y verificar el comportamiento de transferencia de RevenueCat.
- **También falta:** implementar y probar el aviso previo a comprar desde una cuenta de invitado.
- **Criterio de cierre:** matriz de casos (misma/diferente cuenta de tienda y juego, dispositivo nuevo, cuenta invitada/vinculada) con resultados esperados y comprobados.

### 14. Eliminación desde cuentas invitadas

- **Documento relacionado:** Eliminación de cuenta, §1.
- **Falta:** verificar los rótulos y la ruta final `Perfil → Cuenta → Eliminar cuenta`, y ofrecer una alternativa operativa a usuarios invitados.
- **Criterio de cierre:** eliminación iniciable y comprobada tanto para cuentas vinculadas como invitadas, con instrucciones públicas actualizadas si cambia la ruta.

### 15. Sesión posterior a eliminar una cuenta

- **Documento relacionado:** Eliminación de cuenta, §5.
- **Falta:** decidir si debe ofrecerse salir de la app en vez de crear inmediatamente una nueva identidad invitada y comunicar claramente el efecto antes de confirmar.
- **Criterio de cierre:** decisión de producto documentada, UI implementada y prueba de que la nueva identidad no recupera ni queda vinculada a datos eliminados.

### 16. Coherencia del programa de referidos

- **Documento relacionado:** Compras, §8.
- **Falta:** contrastar con la interfaz los siete días de elegibilidad, límite mensual de cinco referidos, zona horaria, hitos, cantidades, estados y acción para reclamar recompensas.
- **Criterio de cierre:** texto, UI y reglas de backend coincidentes para todos los casos límite.

## Prioridad media — comunidad

### 17. Ubicación y alcance de Reportar

- **Documento relacionado:** Reglas de comunidad, §3.
- **Falta:** confirmar en la versión final desde qué pantallas se puede reportar a un jugador y resolver la denuncia de grupos o documentar el canal alternativo.
- **Criterio de cierre:** rutas probadas, motivos disponibles inventariados y reglas públicas consistentes con la UI.

## Prioridad alta — créditos, licencias y activos

### 18. Catálogo distribuido de Picture Cross

- **Documento relacionado:** Créditos, “Imágenes de Picture Cross”.
- **Falta:** comparar el inventario publicado con los tableros incluidos en la release, agregar enlaces originales cuando correspondan y conservar los avisos entregados por cada fuente.
- **Criterio de cierre:** cada asset distribuido trazable a autor, fuente, licencia y transformación; ninguna atribución requerida ausente.

### 19. Recursos generados con ChatGPT

- **Documento relacionado:** Créditos, “Recursos realizados por el equipo con IA”.
- **Falta:** identificar las condiciones contractuales aplicables a la cuenta ChatGPT Plus personal durante agosto–octubre de 2026 y revisar prompts, referencias y archivos finales.
- **Criterio de cierre:** permisos de uso comercial y distribución comprobados para el proceso utilizado, con excepciones o reemplazos documentados.

### 20. Inventario de componentes y avisos

- **Documento relacionado:** Créditos, “Diccionarios, software, iconos y otros recursos”.
- **Falta:** inventariar bibliotecas, listas de palabras, iconos, fuentes y otros assets realmente incluidos en las builds y servicios distribuidos.
- **Criterio de cierre:** SBOM/inventario por versión con licencia, copyright, texto de aviso y obligación de atribución o entrega de código cuando corresponda.

### 21. Cadena de fuentes de los diccionarios

- **Documento relacionado:** Créditos, “Diccionarios, software, iconos y otros recursos”.
- **Falta:** confirmar fuentes y versiones efectivas de SCOWL, cracklib-small, wspanish, Project Gutenberg, Mozilla Common Voice y ENABLE.
- **Revisión necesaria:** licencias originales, cadena de derivación, alcance territorial —incluida Argentina— y avisos exigibles. Un README que diga “dominio público” no alcanza por sí solo.
- **Criterio de cierre:** cada lista de palabras trazable a sus fuentes y versiones, con revisión de licencia y avisos incluidos.

## Cierre transversal

### 22. Revisión legal y aprobación de versión

- **Alcance:** Política de privacidad, Términos, Reglas de comunidad, Compras, Soporte, Eliminación de cuenta y Créditos.
- **Falta:** revisión integral por una persona profesional competente para los mercados donde se distribuirá la app y aprobación de una versión identificable.
- **Criterio de cierre:** versión, fecha, responsable de aprobación y registro de cambios conservados.

### 23. Mercados e idiomas futuros

- **Falta:** antes de distribuir fuera de Argentina, revisar jurisdicción, consumidor, privacidad, menores, publicidad, tiendas, domicilio/canales obligatorios y traducciones para cada país.
- **Criterio de cierre:** checklist por mercado e idioma, traducción revisada y contenido publicado en su ruta estable antes de habilitar la distribución.
