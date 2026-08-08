#!/usr/bin/env python3
"""Reject private product sources that re-enter the public research repository."""

from __future__ import annotations

import hashlib
import re
import subprocess
import sys


FORBIDDEN_PREFIXES = (
    "wiki/",
    "docs/reference/history-timeline/",
    "docs/reference/tech-tree-web-candidates/",
    "tools/tech-tree-reference-capture/",
)
FORBIDDEN_EXACT = {
    "docs/publications/effective-immortality-guide.md",
    "docs/publications/health-handbook.md",
    "docs/publications/history-of-immortality.md",
    "docs/source-notes/2026-08-06-human-immortality-research-major-events-timeline.md",
    "docs/templates/history-event.md",
    "governance/control-plane/history-timeline-contract.v1.yaml",
}
FORBIDDEN_TOOL = re.compile(
    r"^tools/(?:.*history_timeline.*|history_timeline_rounds_.*\.json)$"
)


def location_id(path: str) -> str:
    return hashlib.sha256(path.encode("utf-8", errors="surrogateescape")).hexdigest()[:16]


def main() -> int:
    try:
        result = subprocess.run(
            ["git", "ls-files"], check=True, capture_output=True, text=True
        )
    except (OSError, subprocess.CalledProcessError):
        print("public product boundary: ERROR (trusted input unavailable)", file=sys.stderr)
        return 2

    findings = []
    for path in result.stdout.splitlines():
        if path in FORBIDDEN_EXACT or path.startswith(FORBIDDEN_PREFIXES) or FORBIDDEN_TOOL.match(path):
            findings.append(path)

    if findings:
        print(f"public product boundary: FAIL ({len(findings)} finding(s))", file=sys.stderr)
        for path in findings[:20]:
            print(f"- private-product-source location_id={location_id(path)}", file=sys.stderr)
        return 1

    print("public product boundary: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
