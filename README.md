# Daylo Games — documentación legal

Este repositorio público contiene los documentos legales de Daylo Games y el sitio que los publica. Los textos fuente están en [`documents/es/`](documents/es/).

GitHub Pages publica el sitio en `https://daylogames.github.io/legal/`. El flujo manual **Publish legal site** genera las páginas en `/es/`, conserva redirecciones desde las antiguas rutas `/borradores/es/` y compila el directorio `site/` con Jekyll.

Para publicar, seleccionar **GitHub Actions** como fuente en **Settings → Pages** y ejecutar el flujo desde **Actions**. Las actualizaciones deben conservar las mismas URLs.

Si se agrega una página mantenida manualmente en `site/es/<ruta>/index.md` o `site/en/<ruta>/index.md`, debe usar `layout: default` y no incluir `generated_page: true`; el generador la preservará. El seguimiento de información y verificaciones todavía necesarias está en [`PENDIENTES.md`](PENDIENTES.md) y no forma parte del sitio publicado.
