# Daylo Games — documentación legal

Repositorio público para preparar y publicar la documentación de Daylo Games. **Las rutas estables de Pages muestran documentos en preparación, todavía no vigentes.** Los textos en [`planning/legal/public/`](planning/legal/public/) son borradores con decisiones pendientes. Sus URLs estables pueden cargarse en configuraciones de preparación; antes de distribuir la app en producción deben contener las versiones aprobadas.

- [`planning/legal/`](planning/legal/README.md): borradores, auditoría, inventario, benchmark y registro de variables. Todo este directorio es visible en GitHub.
- [`planning/mobile/`](planning/mobile/legal-integration.md): plan de integración en la app.
- [`site/`](site/): única entrada al sitio de GitHub Pages. Contiene una portada; el build genera documentos rotulados en `/es/` y redirecciones desde `/borradores/es/`. No contiene políticas vigentes.

## Publicación con GitHub Pages

Hosting inicial confirmado: **GitHub Pages**, con dirección prevista `https://daylogames.github.io/legal/`. El dominio propio se evaluará más adelante. Ver [rutas, publicación y migración](planning/legal/publicacion-y-migracion.md); las rutas finales aún no contienen documentos aprobados.

1. En **Settings → Pages → Build and deployment**, elegir **GitHub Actions** como fuente. No elegir «Deploy from a branch»: esa opción no aísla `site/` de `planning/`.
2. En **Actions → Publish legal site → Run workflow**, ejecutar el flujo manual. El workflow genera documentos rotulados desde `planning/legal/public/` en las rutas estables `/es/<ruta>/`, agrega redirecciones desde `/borradores/es/` y compila con Jekyll `site/`. El segmento `/borradores/` ya no forma parte de los enlaces que se configuran para el lanzamiento.
3. Cuando se defina un dominio propio, configurarlo en **Settings → Pages → Custom domain**, completar DNS según GitHub y activar **Enforce HTTPS**. Mientras tanto el sitio queda bajo la URL de proyecto `https://daylogames.github.io/legal/` si Pages está habilitado.
4. Al aprobar documentos: crear la versión final en `site/es/<ruta>/index.md` y `site/en/<ruta>/index.md`, con front matter Jekyll y `layout: default`, sin `generated_preview: true`. El generador preserva las páginas independientes ya existentes en `site/es/`. Convertir enlaces de archivos en rutas del sitio; actualizar portada, fecha de vigencia y versiones anteriores. Revisar `noindex` al aprobar: los borradores deben conservarlo. Probar las mismas URLs estables antes de distribuir la app; no será necesario cambiar `/es/<ruta>/` por haber terminado los textos.
5. Si se usa AdMob, publicar `site/app-ads.txt` con el fragmento real de la cuenta. Comprobar que responde en la **raíz del hostname** usado como sitio del desarrollador en las tiendas. Una ruta de proyecto como `/legal/app-ads.txt` no equivale a `https://daylogames.github.io/app-ads.txt`; por eso conviene un dominio propio apuntado directamente a este sitio o alojar el archivo en otro sitio del desarrollador que controle la raíz.
6. Antes de actualizar la app o fichas de tiendas, confirmar identidad, contacto, edad/mercados, conservación, proveedores, compras y borrado en producción. Ver [matriz de requisitos para Argentina y tiendas](planning/legal/requisitos-argentina-y-tiendas.md), [decisiones pendientes](planning/legal/README.md#decisiones-pendientes) y [registro de variables](planning/legal/variables-y-cambios.md).

El workflow solo se ejecuta manualmente por ahora. Los documentos generados tienen aviso de preparación y `noindex`; se permite cargar sus rutas estables en configuraciones previas al lanzamiento. No distribuir la app en producción hasta cerrar los pendientes y publicar las versiones aprobadas. Cuando las políticas estén aprobadas, puede añadirse publicación en cada push a `main` tras controles de revisión y ausencia de marcadores `[PENDIENTE:]` en `site/`.

## Fuentes de la configuración

- [GitHub: fuente de publicación y visibilidad del sitio](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).
- [GitHub: workflows de Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).
- [GitHub: dominio propio](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site).
- [AdMob: ubicación de app-ads.txt](https://support.google.com/admob/answer/9363762?hl=en).
