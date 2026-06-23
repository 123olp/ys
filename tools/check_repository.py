#!/usr/bin/env python3
"""检查 Human Infra 知识仓库的基础结构。"""

from __future__ import annotations

import sys
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    ".editorconfig",
    ".gitattributes",
    ".gitignore",
    "AGENTS.md",
    "CHANGELOG.md",
    "CITATION.cff",
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING.md",
    "GOVERNANCE.md",
    "LICENSE.md",
    "Makefile",
    "README.md",
    "SECURITY.md",
    "SUPPORT.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/ISSUE_TEMPLATE/documentation.yml",
    ".github/ISSUE_TEMPLATE/research-note.yml",
    ".github/ISSUE_TEMPLATE/data-pipeline.yml",
    "tools/README.md",
    "docs/README.md",
    "docs/AGENTS.md",
    "docs/decisions/README.md",
    "docs/decisions/0001-adopt-docs-as-code-knowledge-base-structure.md",
    "docs/decisions/0002-adopt-local-quality-gates.md",
    "docs/decisions/0003-add-future-waiting-domain.md",
    "docs/explanations/README.md",
    "docs/how-to/README.md",
    "docs/how-to/add-domain.md",
    "docs/how-to/add-source-note.md",
    "docs/how-to/contribute-docs.md",
    "docs/how-to/run-quality-checks.md",
    "docs/reference/README.md",
    "docs/source-notes/README.md",
    "docs/templates/README.md",
    "docs/tutorials/README.md",
    "docs/reference/document-lifecycle.md",
    "docs/reference/domain-map.md",
    "docs/reference/evidence-policy.md",
    "docs/reference/ethics-and-safety-boundaries.md",
    "docs/reference/glossary.md",
    "docs/reference/repository-standards.md",
    "docs/reference/review-checklists.md",
    "docs/reference/source-management.md",
    "docs/reference/writing-style-guide.md",
    "docs/explanations/human-runtime-infrastructure.md",
    "docs/templates/decision-record.md",
    "docs/templates/domain-readme.md",
    "docs/templates/reference-doc.md",
    "docs/templates/source-note.md",
    "domains/README.md",
    "domains/AGENTS.md",
    "domains/future-waiting/README.md",
    "domains/future-waiting/AGENTS.md",
    "domains/future-waiting/paths/black-hole-waiting-room.md",
    "domains/longevity-evidence/README.md",
    "domains/longevity-evidence/AGENTS.md",
    "domains/longevity-evidence/docs/README.md",
    "domains/disembodied-cns/README.md",
    "domains/disembodied-cns/AGENTS.md",
    "domains/memory-editing/README.md",
    "domains/memory-editing/AGENTS.md",
]

REQUIRED_DIRS = [
    ".github/ISSUE_TEMPLATE",
    "docs/decisions",
    "docs/explanations",
    "docs/how-to",
    "docs/reference",
    "docs/source-notes",
    "docs/templates",
    "docs/tutorials",
    "domains/future-waiting",
    "domains/future-waiting/paths",
    "domains",
    "tools",
]

FORBIDDEN_NAME_PARTS = [
    "新建 文本文档",
]

MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
IGNORED_LINK_PREFIXES = (
    "#",
    "http://",
    "https://",
    "mailto:",
)


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT))


def iter_markdown_without_code(path: Path) -> list[tuple[int, str]]:
    lines: list[tuple[int, str]] = []
    in_fence = False
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence:
            lines.append((lineno, line))
    return lines


def check_local_markdown_links(errors: list[str]) -> None:
    for path in ROOT.rglob("*.md"):
        rel = relative(path)
        if rel.startswith(".history/"):
            continue
        for lineno, line in iter_markdown_without_code(path):
            for match in MARKDOWN_LINK_RE.finditer(line):
                target = match.group(1).strip()
                if target.startswith("<") and target.endswith(">"):
                    target = target[1:-1]
                if target.startswith(IGNORED_LINK_PREFIXES):
                    continue
                target_path = target.split("#", 1)[0]
                if not target_path:
                    continue
                resolved = (path.parent / target_path).resolve()
                try:
                    resolved.relative_to(ROOT)
                except ValueError:
                    errors.append(f"markdown link escapes repository: {rel}:{lineno}: {target}")
                    continue
                if not resolved.exists():
                    errors.append(f"broken markdown link: {rel}:{lineno}: {target}")


def main() -> int:
    errors: list[str] = []

    for name in REQUIRED_FILES:
        path = ROOT / name
        if not path.is_file():
            errors.append(f"missing file: {name}")

    for name in REQUIRED_DIRS:
        path = ROOT / name
        if not path.is_dir():
            errors.append(f"missing directory: {name}")

    for path in ROOT.rglob("*"):
        rel = relative(path)
        if any(part in rel for part in FORBIDDEN_NAME_PARTS):
            if ".history/" not in rel:
                errors.append(f"temporary filename still active: {rel}")
        if path.is_dir() and path.name == "__pycache__":
            errors.append(f"python cache directory present: {rel}")

    check_local_markdown_links(errors)

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print("repository structure ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
