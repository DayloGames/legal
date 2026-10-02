#!/usr/bin/env python3
"""Generate clearly labeled, non-canonical Pages previews from legal drafts."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
source = root / "documents/es"
destination = root / "site/borradores/es"

for draft in sorted(source.glob("*.es.md")):
    slug = draft.name.removesuffix(".es.md")
    text = draft.read_text(encoding="utf-8")
    text = re.sub(r"\]\(([a-z-]+)\.es\.md\)", r"](../\1/)", text)
    output = destination / slug / "index.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        "---\nlayout: default\ntitle: Borrador de " + slug + " — Daylo\n"
        "permalink: /borradores/es/" + slug + "/\n---\n\n"
        "> **BORRADOR DE TRABAJO — NO VIGENTE.** Este texto contiene datos por definir "
        "y no debe usarse como política de la app.\n\n" + text,
        encoding="utf-8",
    )

print("Generated", len(list(source.glob("*.es.md"))), "draft previews")
