#!/usr/bin/env python3
"""审计 Human Infra 核心主张证据矩阵的本地契约。"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MATRIX_PATH = ROOT / "docs/reference/human-infra-core-claim-evidence-matrix.md"

REQUIRED_SECTIONS = [
    "# Human Infra Core Claim-Evidence Matrix",
    "## 使用边界",
    "## Source Anchor Cards",
    "## Core Claim Register",
    "## Claim-Evidence Matrix",
    "## Method Translation Contract",
    "## Project-Level Evidence Gates",
    "## Current Project Status",
    "## Source Traceability",
    "Last reviewed: 2026-07-02.",
]

REQUIRED_SOURCE_IDS = [f"SA{i}" for i in range(1, 9)]
REQUIRED_CLAIM_IDS = [f"HI-CL{i}" for i in range(1, 8)]

REQUIRED_GATE_IDS = [
    "claim-type",
    "source-role",
    "scope-boundary",
    "model-position",
    "falsifier",
    "prohibited-use",
]

REQUIRED_BOUNDARY_PHRASES = [
    "不证明",
    "不提供",
    "禁止外推",
    "个体死亡日期",
    "个体医学建议",
    "未验证校准",
]

REQUIRED_METHOD_URLS = [
    "https://plato.stanford.edu/entries/capability-approach/",
    "https://iep.utm.edu/sen-cap/",
    "https://www.who.int/about/governance/constitution",
    "https://www.bmj.com/content/374/bmj.n2061",
    "https://www.tripod-statement.org/",
    "https://www.bmj.com/content/385/bmj-2023-078378",
    "https://www.probast.org/",
    "https://pubmed.ncbi.nlm.nih.gov/40127903/",
    "https://www.valueinhealthjournal.com/article/S1098-3015(12)01656-7/fulltext",
    "https://github.com/OHDSI/PatientLevelPrediction",
    "https://www.ohdsi.org/web/wiki/doku.php?id=projects:workgroups:patient-level_prediction",
    "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0033317",
]

INDEX_REFERENCES = [
    "README.md",
    "docs/README.md",
    "docs/AGENTS.md",
    "docs/reference/README.md",
    "docs/reference/human-infra-maturity-roadmap.md",
]

MATRIX_LINK = "human-infra-core-claim-evidence-matrix.md"


def count_identifier(text: str, identifier: str) -> int:
    """统计 Markdown 中一个带反引号或裸写的稳定 ID。"""
    pattern = rf"(?<![A-Z0-9-])`?{re.escape(identifier)}`?(?![A-Z0-9-])"
    return len(re.findall(pattern, text))


def read_text(path: Path, errors: list[str]) -> str:
    if not path.exists():
        errors.append(f"missing file: {path.relative_to(ROOT)}")
        return ""
    return path.read_text(encoding="utf-8")


def main() -> int:
    errors: list[str] = []
    matrix = read_text(MATRIX_PATH, errors)

    for section in REQUIRED_SECTIONS:
        if section not in matrix:
            errors.append(f"missing matrix section or marker: {section}")

    for source_id in REQUIRED_SOURCE_IDS:
        if count_identifier(matrix, source_id) < 2:
            errors.append(f"source anchor is not registered and reused: {source_id}")

    for claim_id in REQUIRED_CLAIM_IDS:
        if count_identifier(matrix, claim_id) < 2:
            errors.append(f"claim is not registered and mapped: {claim_id}")

    for gate_id in REQUIRED_GATE_IDS:
        if f"`{gate_id}`" not in matrix:
            errors.append(f"missing project evidence gate: {gate_id}")

    for phrase in REQUIRED_BOUNDARY_PHRASES:
        if phrase not in matrix:
            errors.append(f"missing boundary phrase: {phrase}")

    for url in REQUIRED_METHOD_URLS:
        if url not in matrix:
            errors.append(f"missing method anchor URL: {url}")

    for relative_path in INDEX_REFERENCES:
        text = read_text(ROOT / relative_path, errors)
        if text and MATRIX_LINK not in text:
            errors.append(f"index does not link core matrix: {relative_path}")

    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1

    print(
        "core claim evidence matrix audit ok: "
        f"sources={len(REQUIRED_SOURCE_IDS)} "
        f"claims={len(REQUIRED_CLAIM_IDS)} "
        f"gates={len(REQUIRED_GATE_IDS)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
