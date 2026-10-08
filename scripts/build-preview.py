#!/usr/bin/env python3
"""Serve labeled drafts at stable legal URLs until approved pages replace them."""
from pathlib import Path
import json
import re

root = Path(__file__).resolve().parents[1]
source = root / "planning/legal/public"
destination = root / "site/es"
legacy_destination = root / "site/borradores/es"
generated = 0

for draft in sorted(source.glob("*.es.md")):
    slug = draft.name.removesuffix(".es.md")
    text = draft.read_text(encoding="utf-8")
    text = re.sub(r"\]\(([a-z-]+)\.es\.md\)", r"](../\1/)", text)
    output = destination / slug / "index.md"
    # Preserve approved pages committed to site/es. Refresh only our generated
    # drafts on subsequent local runs; never overwrite an independently authored page.
    if not output.exists() or "\ngenerated_preview: true\n" in output.read_text(encoding="utf-8"):
        title = text.splitlines()[0].removeprefix("# ")
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(
            "---\nlayout: default\ntitle: " + json.dumps(title, ensure_ascii=False) + "\n"
            "generated_preview: true\npermalink: /es/" + slug + "/\n---\n\n"
            "> **BORRADOR DE TRABAJO — NO VIGENTE.** Esta URL es estable y puede "
            "configurarse durante la preparación del lanzamiento. El documento contiene "
            "pendientes y debe completarse antes de distribuir la app en producción.\n\n" + text,
            encoding="utf-8",
        )
        generated += 1

    legacy = legacy_destination / slug / "index.md"
    legacy.parent.mkdir(parents=True, exist_ok=True)
    legacy.write_text(
        "---\nlayout: redirect\nredirect_to: /es/" + slug + "/\n"
        "permalink: /borradores/es/" + slug + "/\n---\n",
        encoding="utf-8",
    )

print("Generated", generated, "drafts at stable legal URLs and", len(list(source.glob("*.es.md"))), "legacy redirects")
