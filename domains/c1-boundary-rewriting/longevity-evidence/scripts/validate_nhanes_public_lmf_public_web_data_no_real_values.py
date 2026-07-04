#!/usr/bin/env python3
"""验证 NHANES public-use LMF 前端公开数据不含真实加权输出值。"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[4]
WEB_DATA_DIR = REPO_ROOT / "web" / "src" / "data"
OUTPUT_PATH = WEB_DATA_DIR / "life-path-nhanes-public-lmf-public-web-data-no-real-values-validation.json"

PUBLIC_WEB_GLOB = "life-path-nhanes-public-lmf-*.json"

FORBIDDEN_VALUE_KEYS = {
    "SEQN",
    "RIDAGEYR",
    "RIAGENDR",
    "rawRows",
    "rowLevelData",
    "deathDate",
    "individualRiskScore",
    "weightedMortalityRate",
    "weightedRate",
    "weightedDeaths",
    "weightSum",
    "standardError",
    "confidenceInterval95",
    "confidenceIntervalLower",
    "confidenceIntervalUpper",
    "ciLower",
    "ciUpper",
    "relativeStandardError",
    "recordCount",
    "deathCount",
    "unweightedCount",
    "unweightedDeaths",
}

MUST_BE_FALSE_IF_PRESENT = {
    "publicWeightedDomainOutputAllowed",
    "realWeightedRatesComputed",
    "realWeightedOutputPresent",
    "realWeightedOutputImplemented",
    "realWeightedOutputReviewed",
    "realWeightedOutputReleased",
    "calibrationAllowed",
    "individualPredictionAllowed",
    "medicalAdviceAllowed",
}

MUST_BE_TRUE_IF_PRESENT = {
    "trackedValuesOmitted",
}


def repo_rel(path: Path) -> str:
    return str(path.resolve().relative_to(REPO_ROOT))


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def walk(value: Any, path: str = "$") -> list[tuple[str, str, Any]]:
    rows: list[tuple[str, str, Any]] = []
    if isinstance(value, dict):
        for key, nested in value.items():
            child_path = f"{path}.{key}"
            rows.append((child_path, str(key), nested))
            rows.extend(walk(nested, child_path))
    elif isinstance(value, list):
        for index, nested in enumerate(value):
            rows.extend(walk(nested, f"{path}[{index}]"))
    return rows


def validate_file(path: Path) -> list[str]:
    errors: list[str] = []
    data = load_json(path)
    for json_path, key, value in walk(data):
        if key in FORBIDDEN_VALUE_KEYS:
            errors.append(f"{repo_rel(path)} contains forbidden public value key at {json_path}")
        if key in MUST_BE_FALSE_IF_PRESENT and value is not False:
            errors.append(f"{repo_rel(path)} requires {json_path} to be false")
        if key in MUST_BE_TRUE_IF_PRESENT and value is not True:
            errors.append(f"{repo_rel(path)} requires {json_path} to be true")
    return errors


def main() -> int:
    files = sorted(WEB_DATA_DIR.glob(PUBLIC_WEB_GLOB))
    errors: list[str] = []
    checked: list[str] = []

    for path in files:
        if not path.is_file():
            continue
        checked.append(repo_rel(path))
        try:
            errors.extend(validate_file(path))
        except json.JSONDecodeError as exc:
            errors.append(f"{repo_rel(path)} is not valid JSON: {exc}")

    output = {
        "schemaVersion": "human-infra.nhanes-public-lmf-public-web-data-no-real-values-validation.v1",
        "status": "PASS" if not errors else "FAIL",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "scanScope": {
            "glob": f"{repo_rel(WEB_DATA_DIR)}/{PUBLIC_WEB_GLOB}",
            "fileCount": len(checked),
            "files": checked,
        },
        "policy": {
            "forbiddenValueKeys": sorted(FORBIDDEN_VALUE_KEYS),
            "mustBeFalseIfPresent": sorted(MUST_BE_FALSE_IF_PRESENT),
            "mustBeTrueIfPresent": sorted(MUST_BE_TRUE_IF_PRESENT),
            "ignoredLocalOutputsAllowed": False,
            "publicWeightedDomainOutputAllowed": False,
            "calibrationAllowed": False,
            "individualPredictionAllowed": False,
        },
        "summary": {
            "forbiddenKeyHitCount": sum("forbidden public value key" in error for error in errors),
            "booleanBoundaryIssueCount": len(errors)
            - sum("forbidden public value key" in error for error in errors),
            "publicWebDataContainsRealWeightedValues": False if not errors else None,
            "publicWebDataContainsRowLevelValues": False if not errors else None,
        },
        "errors": errors,
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {repo_rel(OUTPUT_PATH)}")
    print(f"status={output['status']} files={len(checked)} errors={len(errors)}")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
