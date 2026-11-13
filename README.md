# Daylo Games — documentación legal

Este repositorio público contiene los documentos legales de Daylo Games y el sitio que los publica. Los textos fuente están en [`documents/es/`](documents/es/).

La [propuesta de reglas de Versus](propuestas/versus/01-reglas-versus.es.md), su [integración en los términos](propuestas/versus/02-integracion-y-futuras-recompensas.es.md) y la [guía de comunicación para iOS y Android](propuestas/versus/03-comunicacion-y-lanzamiento.es.md) son borradores de trabajo. No se incluyen en el sitio legal ni están vigentes; los archivos del repositorio sí son públicos.

GitHub Pages publica el sitio en `https://daylogames.github.io/legal/`, y el sitio `daylo-web` (Cloudflare Worker) lo sirve también en `https://daylogames.com/legal/` mediante un proxy en `src/pages/legal/[...path].ts`. El flujo manual **Publish legal site** genera las páginas en `/es/`, conserva redirecciones desde las antiguas rutas `/borradores/es/` y compila el directorio `site/` con Jekyll.

El [plan de modales legales para mobile](propuestas/versus/04-plan-modales-legales-mobile.es.md) distingue el primer inicio de los avisos por actualización; todavía no está implementado.

Para publicar, seleccionar **GitHub Actions** como fuente en **Settings → Pages** y ejecutar el flujo desde **Actions**. Las actualizaciones deben conservar las mismas URLs.

Si se agrega una página mantenida manualmente en `site/es/<ruta>/index.md` o `site/en/<ruta>/index.md`, debe usar `layout: default` y no incluir `generated_page: true`; el generador la preservará. El seguimiento de información y verificaciones todavía necesarias está en [`PENDIENTES.md`](PENDIENTES.md) y no forma parte del sitio publicado.
