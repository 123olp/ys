#!/usr/bin/env python3
"""拒绝在静态 Wiki 中重写 MediaWiki/Vector 原生交互。"""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPORTER = ROOT / "scripts" / "export-pages-snapshot.py"
STATIC_OUTPUT = ROOT / "runtime" / "pages" / "wiki"

BANNED_PATHS = (
    ROOT / "vector-upstream" / "appearance-controls.html",
    ROOT / "scripts" / "vector-client-preferences-static.js",
)
BANNED_EXPORTER_MARKERS = (
    "install_static_vector_appearance",
    "VECTOR_APPEARANCE_CONTROLS",
    "VECTOR_CLIENT_PREFERENCES_SCRIPT",
    "skins.vector.clientPreferences&only=styles",
    "vector-feature-appearance-pinned-clientpref-0 "
    ".vector-user-links .vector-appearance-landmark",
)


def main() -> int:
    issues: list[str] = []
    for path in BANNED_PATHS:
        if path.exists():
            issues.append(f"存在自写或冻结的 Vector 交互实现: {path.relative_to(ROOT)}")

    exporter = EXPORTER.read_text(encoding="utf-8")
    for marker in BANNED_EXPORTER_MARKERS:
        if marker in exporter:
            issues.append(f"导出器仍接管 Vector 原生运行时: {marker}")

    if STATIC_OUTPUT.exists():
        for page in STATIC_OUTPUT.rglob("*.html"):
            document = page.read_text(encoding="utf-8")
            if "/assets/vector-client-preferences.js" in document:
                issues.append(
                    f"静态发布物包含自写 Vector 运行时: {page.relative_to(ROOT)}"
                )
                break

    if issues:
        print("MediaWiki 原生 UI 所有权门禁失败:", file=sys.stderr)
        for issue in issues:
            print(f"- {issue}", file=sys.stderr)
        return 1

    print("MediaWiki 原生 UI 所有权门禁: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
