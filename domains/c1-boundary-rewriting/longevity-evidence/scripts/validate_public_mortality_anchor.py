#!/usr/bin/env python3
"""Validate the public aggregate mortality anchor used by the life-path model."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_INPUT = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
    / "life_path_public_mortality_anchor.json"
)
REQUIRED_BLOCKED_USES = {
    "individual prediction",
    "individual death-date output",
    "medical advice",
    "calibrated Human Infra prediction",
    "intervention effect estimation",
    "LEV proof",
}
REQUIRED_SEX_GROUPS = {"male", "female"}
REQUIRED_SOURCE_URLS = {
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Publications/NVSR/72-12/Table02.xlsx",
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Publications/NVSR/72-12/Table03.xlsx",
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("anchor must be a JSON object")
    return data


def validate_anchor(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if data.get("schemaVersion") != "human-infra.life-path-public-mortality-anchor.v1":
        fail(errors, "schemaVersion mismatch")
    if data.get("status") != "public-aggregate-baseline-anchor-not-calibrated-model":
        fail(errors, "status must keep non-calibrated boundary")
    if data.get("sourceAuthority") != "National Center for Health Statistics, National Vital Statistics System":
        fail(errors, "sourceAuthority must be NCHS/NVSS")
    if not str(data.get("reportUrl", "")).startswith("https://www.cdc.gov/nchs/data/nvsr/"):
        fail(errors, "reportUrl must point to the NCHS NVSR report")

    scope = data.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        scope = {}
    if scope.get("geography") != "United States":
        fail(errors, "scope.geography must be United States")
    if scope.get("periodYear") != 2021:
        fail(errors, "scope.periodYear must be 2021")
    if scope.get("ageMin") != 40 or scope.get("ageMax") != 100:
        fail(errors, "scope must cover ages 40-100")
    if set(scope.get("sexGroups", [])) != REQUIRED_SEX_GROUPS:
        fail(errors, "scope.sexGroups must include male and female")

    boundary = data.get("modelUseBoundary")
    if not isinstance(boundary, dict):
        fail(errors, "modelUseBoundary must be an object")
        boundary = {}
    if set(boundary.get("blockedUses", [])) != REQUIRED_BLOCKED_USES:
        fail(errors, "blockedUses do not preserve prohibited uses")
    for key in ("noIndividualRows", "noInterventionEffects", "noCalibrationClaim"):
        if boundary.get(key) is not True:
            fail(errors, f"{key} must be true")

    source_urls = {
        row.get("url")
        for row in data.get("sourceTables", [])
        if isinstance(row, dict)
    }
    if source_urls != REQUIRED_SOURCE_URLS:
        fail(errors, "sourceTables must include the two official NCHS xlsx URLs")

    tables = data.get("tables")
    if not isinstance(tables, list) or len(tables) != 2:
        fail(errors, "tables must contain two sex-specific tables")
        return errors

    seen_sex: set[str] = set()
    for table in tables:
        if not isinstance(table, dict):
            fail(errors, "each table must be an object")
            continue
        sex = table.get("sex")
        if sex not in REQUIRED_SEX_GROUPS:
            fail(errors, f"unexpected sex group: {sex}")
            continue
        seen_sex.add(str(sex))
        rows = table.get("rows")
        if not isinstance(rows, list) or len(rows) != 61:
            fail(errors, f"{sex}.rows must contain 61 ages")
            continue
        last_lx = float("inf")
        last_ex = float("inf")
        expected_age = 40
        for row in rows:
            age = row.get("age")
            if age != expected_age:
                fail(errors, f"{sex}.rows expected age {expected_age}, found {age}")
                break
            qx = row.get("qx")
            lx = row.get("lx")
            ex = row.get("ex")
            if not isinstance(qx, (int, float)) or not 0 <= float(qx) <= 1:
                fail(errors, f"{sex} age {age} qx must be within [0,1]")
            if not isinstance(lx, (int, float)) or float(lx) < 0:
                fail(errors, f"{sex} age {age} lx must be non-negative")
            elif float(lx) > last_lx + 1e-6:
                fail(errors, f"{sex} lx must be non-increasing at age {age}")
            if not isinstance(ex, (int, float)) or float(ex) < 0:
                fail(errors, f"{sex} age {age} ex must be non-negative")
            elif float(ex) > last_ex + 1.5:
                fail(errors, f"{sex} ex jumped unexpectedly at age {age}")
            last_lx = float(lx)
            last_ex = float(ex)
            expected_age += 1

    if seen_sex != REQUIRED_SEX_GROUPS:
        fail(errors, "missing one sex-specific table")
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    data = load_json(args.input)
    errors = validate_anchor(data)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("public mortality anchor ok: sex_groups=2 ages=40-100 boundary=aggregate-only")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
