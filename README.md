# Daylo Games — documentación legal

Este repositorio público contiene únicamente los documentos legales y el sitio que los publica. Los textos de [`documents/es/`](documents/es/) están en preparación y todavía no son políticas vigentes.

GitHub Pages publica el sitio en `https://daylogames.github.io/legal/`. El flujo manual **Publish legal site** genera páginas rotuladas en `/es/` y redirecciones desde `/borradores/es/`, y compila el directorio `site/` con Jekyll.

Para publicar, seleccionar **GitHub Actions** como fuente en **Settings → Pages** y ejecutar el flujo desde **Actions**. Antes de distribuir la app, completar los pendientes y aprobar los documentos. Las versiones finales deben tener fecha de vigencia y conservar las mismas URLs.

Las páginas aprobadas se agregan en `site/es/<ruta>/index.md` y `site/en/<ruta>/index.md`, con `layout: default` y sin `generated_preview: true`. El generador preserva esas páginas. Los borradores conservan el aviso de preparación y `noindex`.
