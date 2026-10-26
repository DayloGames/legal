#!/usr/bin/env python3
"""Build the Spanish legal documents at their stable public URLs."""
from pathlib import Path
import json
import re

root = Path(__file__).resolve().parents[1]
source = root / "documents/es"
destination = root / "site/es"
legacy_destination = root / "site/borradores/es"
generated = 0

for draft in sorted(source.glob("*.es.md")):
    slug = draft.name.removesuffix(".es.md")
    text = draft.read_text(encoding="utf-8")
    text = re.sub(r"\]\(([a-z-]+)\.es\.md\)", r"](../\1/)", text)
    output = destination / slug / "index.md"
    # Refresh generated pages while preserving independently authored pages.
    existing = output.read_text(encoding="utf-8") if output.exists() else ""
    if not output.exists() or any(
        marker in existing for marker in ("\ngenerated_page: true\n", "\ngenerated_preview: true\n")
    ):
        title = text.splitlines()[0].removeprefix("# ")
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(
            "---\nlayout: default\ntitle: " + json.dumps(title, ensure_ascii=False) + "\n"
            "generated_page: true\npermalink: /es/" + slug + "/\n---\n\n" + text,
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

print("Generated", generated, "legal pages and", len(list(source.glob("*.es.md"))), "legacy redirects")
