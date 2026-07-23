#!/usr/bin/env python3
"""把候选清单嵌入元页面，生成无需本地服务器的单文件浏览器。"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TEMPLATE = ROOT / "tools/tech-tree-reference-capture/viewer/index.html"
MANIFEST = ROOT / "docs/reference/tech-tree-web-candidates/candidates.json"
OUTPUT = ROOT / "build/reference-captures/tech-tree/viewer/index.html"


def main() -> None:
    template = TEMPLATE.read_text(encoding="utf-8")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    payload = json.dumps(manifest, ensure_ascii=False).replace("</script", "<\\/script")
    marker = "  <script>\n"
    if marker not in template:
        raise RuntimeError("viewer template script marker not found")

    embedded = (
        f'  <script id="candidate-manifest" type="application/json">{payload}</script>\n'
        + marker
    )
    output = template.replace(marker, embedded, 1)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(output, encoding="utf-8")
    print(OUTPUT)


if __name__ == "__main__":
    main()
