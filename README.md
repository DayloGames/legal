# Daylo Games — documentación legal

Repositorio público para preparar y publicar la documentación de Daylo Games. **Actualmente hay vistas previas de los borradores en Pages, pero no políticas vigentes.** Los textos en [`planning/legal/public/`](planning/legal/public/) son borradores con decisiones pendientes; no deben enlazarse desde la app ni desde las tiendas como documentos finales.

- [`planning/legal/`](planning/legal/README.md): borradores, auditoría, inventario, benchmark y registro de variables. Todo este directorio es visible en GitHub.
- [`planning/mobile/`](planning/mobile/legal-integration.md): plan de integración en la app.
- [`site/`](site/): única entrada al sitio de GitHub Pages. Contiene una portada y vistas previas generadas en `/borradores/`; no contiene políticas vigentes.

## Publicación con GitHub Pages

Hosting inicial confirmado: **GitHub Pages**, con dirección prevista `https://daylogames.github.io/legal/`. El dominio propio se evaluará más adelante. Ver [rutas, publicación y migración](planning/legal/publicacion-y-migracion.md); las rutas finales aún no contienen documentos aprobados.

1. En **Settings → Pages → Build and deployment**, elegir **GitHub Actions** como fuente. No elegir «Deploy from a branch»: esa opción no aísla `site/` de `planning/`.
2. En **Actions → Publish legal site → Run workflow**, ejecutar el flujo manual para publicar la portada y las vistas previas rotuladas `/borradores/`. El workflow genera las vistas desde `planning/legal/public/` y compila con Jekyll `site/`. No crea rutas legales definitivas.
3. Cuando se defina un dominio propio, configurarlo en **Settings → Pages → Custom domain**, completar DNS según GitHub y activar **Enforce HTTPS**. Mientras tanto el sitio queda bajo la URL de proyecto `https://daylogames.github.io/legal/` si Pages está habilitado.
4. Al aprobar documentos: mover la versión final a `site/es/<ruta>/index.md` y `site/en/<ruta>/index.md`, con front matter de Jekyll y `layout: default`; convertir los enlaces entre borradores (`*.es.md`) en rutas del sitio, y actualizar portada, fecha de vigencia y versiones anteriores. Quitar `noindex` de `site/_layouts/default.html` cuando el sitio ya contenga páginas aprobadas. Probar las URL públicas antes de configurar app/tiendas. Solo los borradores expresamente generados en `/borradores/` salen de `planning/`; las rutas legales definitivas salen de `site/es/` y `site/en/`.
5. Si se usa AdMob, publicar `site/app-ads.txt` con el fragmento real de la cuenta. Comprobar que responde en la **raíz del hostname** usado como sitio del desarrollador en las tiendas. Una ruta de proyecto como `/legal/app-ads.txt` no equivale a `https://daylogames.github.io/app-ads.txt`; por eso conviene un dominio propio apuntado directamente a este sitio o alojar el archivo en otro sitio del desarrollador que controle la raíz.
6. Antes de actualizar la app o fichas de tiendas, confirmar identidad, contacto, edad/mercados, conservación, proveedores, compras y borrado en producción. Ver [matriz de requisitos para Argentina y tiendas](planning/legal/requisitos-argentina-y-tiendas.md), [decisiones pendientes](planning/legal/README.md#decisiones-pendientes) y [registro de variables](planning/legal/variables-y-cambios.md).

El workflow solo se ejecuta manualmente por ahora. Las vistas previas tienen aviso de borrador y `noindex`; no deben enlazarse desde la app o las tiendas. Cuando las políticas estén aprobadas, puede añadirse publicación en cada push a `main` tras controles de revisión y ausencia de marcadores `[PENDIENTE:]` en `site/`.

## Fuentes de la configuración

- [GitHub: fuente de publicación y visibilidad del sitio](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).
- [GitHub: workflows de Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).
- [GitHub: dominio propio](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site).
- [AdMob: ubicación de app-ads.txt](https://support.google.com/admob/answer/9363762?hl=en).
