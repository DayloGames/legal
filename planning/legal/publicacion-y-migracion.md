# Publicación inicial y futura migración — Daylo Games

Decisión del usuario, 8 de octubre de 2026: usar **GitHub Pages** para el lanzamiento. Un dominio propio podrá evaluarse después. Esta guía no publica ni aprueba los documentos.

## Dirección y rutas

Repositorio: `DayloGames/legal`. Origen previsto: `https://daylogames.github.io`. Ruta de proyecto: `/legal`. Comprobar la URL devuelta por el despliegue antes de configurar tiendas o app.

| Documento | URL estable en español |
| --- | --- |
| Privacidad | `https://daylogames.github.io/legal/es/privacy/` |
| Términos | `https://daylogames.github.io/legal/es/terms/` |
| Comunidad | `https://daylogames.github.io/legal/es/community/` |
| Compras | `https://daylogames.github.io/legal/es/purchases/` |
| Soporte | `https://daylogames.github.io/legal/es/support/` |
| Eliminación | `https://daylogames.github.io/legal/es/delete-account/` |
| Créditos | `https://daylogames.github.io/legal/es/credits/` |

Estas rutas estables se habilitan con documentos en preparación, por decisión del usuario del 8 de octubre de 2026. Pueden cargarse ahora en configuraciones de la app y tiendas; nada se distribuirá en producción hasta completar los textos y funcionamiento. Las versiones aprobadas reemplazarán los borradores en las mismas URLs. Las traducciones usarán `/en/` cuando estén preparadas. Las rutas antiguas `/legal/borradores/es/` redirigen a `/legal/es/` mediante una página de transición.

En `site/_config.yml`, `url` es el origen sin `/legal` y `baseurl` es `/legal`. Enlaces y recursos de Jekyll deben respetar ese prefijo; para rutas internas absolutas, usar el filtro `relative_url`. Comprobar el HTML generado antes de publicar.

## Publicación cuando se cierren los documentos

1. Completar decisiones, retirar marcadores y revisar contenido/funcionamiento. Mantener la publicación manual mientras solo existan borradores.
2. Crear fuentes finales en `site/es/<ruta>/index.md`, con `layout: default` y sin `generated_preview: true`, y traducciones cuando correspondan. El generador no sobrescribe páginas finales existentes. No copiar notas internas a `site/`.
3. Actualizar portada, fecha/versión, enlaces e idioma del HTML. Mantener las vistas de borrador señalizadas y no indexables aunque las políticas finales sí sean indexables.
4. Ejecutar el flujo de Pages y comprobar las siete rutas en un teléfono sin login, incluidas soporte y solicitud externa de eliminación. Configurar solo URLs verificadas en app y consolas.
5. Conservar versiones anteriores y registrar qué versión está en cada build y ficha de tienda.

GitHub Pages registra IP de visitantes con fines de seguridad según [GitHub Docs](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages). Incluir el hosting en privacidad y en proveedores; no afirmar que visitar el sitio no genera datos.

## AdMob: ubicación independiente de las páginas legales

Si el sitio de desarrollador usa `https://daylogames.github.io/legal/`, AdMob busca **`https://daylogames.github.io/app-ads.txt`**, no `/legal/app-ads.txt`. [Guía oficial de AdMob](https://support.google.com/admob/answer/9363762?hl=en).

Una opción con GitHub Pages es publicar el archivo real en el sitio raíz de la organización, desde un repositorio `DayloGames/daylogames.github.io`. Puede coexistir con las políticas en `DayloGames/legal`, sin comprar un dominio. Confirmar si el sitio raíz existe y obtener el fragmento real de AdMob antes de implementarlo. No se creó otro repositorio ni un publisher ID supuesto.

Fragmento, hosting raíz, URL de desarrollador en fichas y verificación de AdMob siguen pendientes. Publicar estas páginas no los resuelve automáticamente.

## Migración futura

- Preparar hostname, HTTPS y rutas nuevas antes de cambiar enlaces; conservar versiones y contenido coherente durante el cambio.
- Si solo se agrega un dominio propio a Pages, revisar DNS, `url`/`baseurl` y redirecciones. Verificar rutas antiguas, incluido `/legal/`; no asumir que el dominio preserva todas las rutas por sí solo.
- Si se cambia de hosting, mantener URLs antiguas útiles mediante redirecciones apropiadas o páginas de transición con enlace directo. Probar antes de retirarlas.
- Actualizar enlaces de app, App Store Connect, Play Console y otras consolas; revisar sitio de desarrollador, `app-ads.txt`, privacidad del hosting y canal de eliminación.
- Mantener acceso para builds antiguas que todavía apuntan a Pages. Migrar URLs no cambia por sí solo condiciones del servicio; revisar avisos si cambian prácticas/proveedores.

Fuentes de GitHub: [sitios de proyecto y organización](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages), [dominio propio](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site). Verificar nuevamente al migrar.
