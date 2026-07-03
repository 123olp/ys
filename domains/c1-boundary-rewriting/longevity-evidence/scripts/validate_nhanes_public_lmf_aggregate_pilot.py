#!/usr/bin/env python3
"""验证 NHANES public-use LMF 聚合试运行输出。"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
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
    / "life_path_nhanes_public_lmf_aggregate_pilot.json"
)
DEFAULT_OUTPUT = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhanes-public-lmf-aggregate-pilot-validation.json"
)

REQUIRED_STATUS = "public-real-data-aggregate-pilot-not-weighted-not-calibrated"
REQUIRED_SOURCE_URLS = {
    "linkedMortalityPage": "https://www.cdc.gov/nchs/linked-data/mortality-files/index.html",
    "fileDescription": "https://www.cdc.gov/nchs/data/datalinkage/public-use-linked-mortality-file-description.pdf",
    "dataDictionary": "https://www.cdc.gov/nchs/data/datalinkage/public-use-linked-mortality-files-data-dictionary.pdf",
    "rReadInProgram": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/datalinkage/linked_mortality/R_ReadInProgramAllSurveys.R",
    "nhanes2017_2018PublicLmf": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/datalinkage/linked_mortality/NHANES_2017_2018_MORT_2019_PUBLIC.dat",
    "nhanes2017_2018DemoXpt": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/DEMO_J.XPT",
    "nhanes2017_2018DemoDocumentation": "https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/DEMO_J.htm",
}
REQUIRED_BLOCKED_USES = {
    "individual prediction",
    "individual death-date output",
    "medical advice",
    "calibrated Human Infra prediction",
    "intervention effect estimation",
    "causal claim",
    "survey-population inference",
    "small-cell public export",
}
REQUIRED_FALSE_BOUNDARY_FLAGS = {
    "rawRowsPersisted",
    "individualRowsInOutput",
    "surveyVarianceEstimated",
    "weightedPopulationEstimateClaimed",
    "calibrationClaimed",
}
EXPECTED_COUNTS = {
    "rawLmfRecordsReadInTemp": 9254,
    "rawDemoRecordsReadInTemp": 9254,
    "joinedRecordsInTemp": 9254,
    "eligibleAdultRecordsInTemp": 5809,
    "eligibleAdultDeaths": 145,
}
EXPECTED_CELL_KEYS = {
    "sex",
    "ageBand",
    "records",
    "suppressed",
    "deaths",
    "assumedAlive",
    "personMonthsExamTotal",
    "meanFollowupYearsExam",
    "unweightedMortalityFraction",
    "mecWeightSumDiagnostic",
    "mecWeightedDeathCountDiagnostic",
}
EXPECTED_AGE_BANDS = {"18-39", "40-59", "60-79", "80+"}
EXPECTED_SEX = {"male", "female"}
HEX_64 = re.compile(r"^[0-9a-f]{64}$")
FORBIDDEN_ROW_KEYS = {
    "SEQN",
    "RIDAGEYR",
    "RIAGENDR",
    "RIDRETH3",
    "WTMEC2YR",
    "SDMVSTRA",
    "SDMVPSU",
    "individualRows",
    "rawRows",
    "deathDate",
    "predictedDeathDate",
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("NHANES public LMF aggregate pilot must be a JSON object")
    return data


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def has_forbidden_key(value: Any) -> str | None:
    if isinstance(value, dict):
        for key, child in value.items():
            if key in FORBIDDEN_ROW_KEYS:
                return key
            nested = has_forbidden_key(child)
            if nested:
                return nested
    elif isinstance(value, list):
        for child in value:
            nested = has_forbidden_key(child)
            if nested:
                return nested
    return None


def validate_payload(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if data.get("schemaVersion") != "human-infra.nhanes-public-lmf-aggregate-pilot.v1":
        fail(errors, "schemaVersion mismatch")
    if data.get("status") != REQUIRED_STATUS:
        fail(errors, "status must preserve aggregate-only non-calibrated boundary")
    if data.get("sourceAuthority") != "CDC/NCHS public-use NHANES Linked Mortality File":
        fail(errors, "sourceAuthority must be CDC/NCHS public-use NHANES LMF")
    if data.get("sourceUrls") != REQUIRED_SOURCE_URLS:
        fail(errors, "sourceUrls must match official CDC/NCHS URLs")

    hashes = data.get("sourceHashes")
    if not isinstance(hashes, dict):
        fail(errors, "sourceHashes must be an object")
        hashes = {}
    for key in (
        "nhanesPublicLmf2017_2018Sha256",
        "nhanesDemo2017_2018Sha256",
        "cdcRReadInProgramSha256",
    ):
        if not isinstance(hashes.get(key), str) or not HEX_64.match(hashes[key]):
            fail(errors, f"{key} must be a sha256 hex digest")

    scope = data.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        scope = {}
    if scope.get("survey") != "NHANES" or scope.get("cycle") != "2017-2018":
        fail(errors, "scope must bind NHANES 2017-2018")
    if scope.get("joinKey") != "SEQN":
        fail(errors, "scope.joinKey must be SEQN")
    if scope.get("grouping") != ["sex", "ageBand"]:
        fail(errors, "scope.grouping must be sex × ageBand")
    if scope.get("minimumCellCount") != 20:
        fail(errors, "scope.minimumCellCount must be 20")

    fixed_width = data.get("lmfFixedWidthContract")
    if fixed_width != {
        "seqn": "columns 1-6",
        "eligstat": "column 15",
        "mortstat": "column 16",
        "ucodLeading": "columns 17-19",
        "diabetes": "column 20",
        "hyperten": "column 21",
        "permthInt": "columns 43-45",
        "permthExm": "columns 46-48",
    }:
        fail(errors, "lmfFixedWidthContract must match the CDC read-in fields used locally")

    boundary = data.get("modelUseBoundary")
    if not isinstance(boundary, dict):
        fail(errors, "modelUseBoundary must be an object")
        boundary = {}
    if set(boundary.get("blockedUses", [])) != REQUIRED_BLOCKED_USES:
        fail(errors, "blockedUses must preserve all prohibited uses")
    for flag in REQUIRED_FALSE_BOUNDARY_FLAGS:
        if boundary.get(flag) is not False:
            fail(errors, f"{flag} must be false")

    forbidden = has_forbidden_key(data)
    if forbidden:
        fail(errors, f"row-level key leaked into aggregate output: {forbidden}")

    aggregate = data.get("aggregate")
    if not isinstance(aggregate, dict):
        fail(errors, "aggregate must be an object")
        aggregate = {}
    for key, expected in EXPECTED_COUNTS.items():
        if aggregate.get(key) != expected:
            fail(errors, f"{key} expected {expected}, found {aggregate.get(key)!r}")

    cells = aggregate.get("aggregateCells")
    if not isinstance(cells, list) or len(cells) != 8:
        fail(errors, "aggregateCells must contain 8 sex × age-band cells")
        cells = []

    sex_seen: set[str] = set()
    age_seen: set[str] = set()
    record_sum = 0
    death_sum = 0
    for cell in cells:
        if not isinstance(cell, dict):
            fail(errors, "each aggregate cell must be an object")
            continue
        if set(cell) != EXPECTED_CELL_KEYS:
            fail(errors, f"unexpected aggregate cell keys: {sorted(cell)}")
            continue
        sex_seen.add(str(cell.get("sex")))
        age_seen.add(str(cell.get("ageBand")))
        if cell.get("suppressed") is not False:
            fail(errors, "all current aggregate cells must be unsuppressed")
        if not isinstance(cell.get("records"), int) or cell["records"] < 20:
            fail(errors, "records must be integer >= 20")
        if not isinstance(cell.get("deaths"), int) or cell["deaths"] < 0:
            fail(errors, "deaths must be non-negative integer")
        if cell.get("assumedAlive") != cell.get("records") - cell.get("deaths"):
            fail(errors, "assumedAlive must equal records - deaths")
        record_sum += int(cell.get("records", 0))
        death_sum += int(cell.get("deaths", 0))

    if sex_seen != EXPECTED_SEX or age_seen != EXPECTED_AGE_BANDS:
        fail(errors, "aggregate cells must cover male/female and all four age bands")
    if record_sum != EXPECTED_COUNTS["eligibleAdultRecordsInTemp"]:
        fail(errors, "aggregate cell records do not sum to eligible adult records")
    if death_sum != EXPECTED_COUNTS["eligibleAdultDeaths"]:
        fail(errors, "aggregate cell deaths do not sum to eligible adult deaths")

    return errors


def build_validation(data_path: Path, output_path: Path, errors: list[str], data: dict[str, Any]) -> dict[str, Any]:
    status = "pass" if not errors else "fail"
    aggregate = data.get("aggregate") if isinstance(data, dict) else {}
    cells = aggregate.get("aggregateCells") if isinstance(aggregate, dict) else []
    return {
        "schemaVersion": "human-infra.nhanes-public-lmf-aggregate-pilot-validation.v1",
        "status": status,
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "aggregatePath": str(data_path.relative_to(REPO_ROOT)),
        "aggregateSha256": sha256_file(data_path),
        "validationPath": str(output_path.relative_to(REPO_ROOT)),
        "summary": {
            "aggregateCells": len(cells) if isinstance(cells, list) else 0,
            "eligibleAdultRecords": aggregate.get("eligibleAdultRecordsInTemp")
            if isinstance(aggregate, dict)
            else None,
            "eligibleAdultDeaths": aggregate.get("eligibleAdultDeaths")
            if isinstance(aggregate, dict)
            else None,
            "errors": errors,
        },
        "boundary": {
            "rawRowsPersisted": False,
            "individualRowsInOutput": False,
            "individualPredictionAllowed": False,
            "individualDeathDateAllowed": False,
            "calibrationClaimed": False,
            "surveyPopulationInferenceClaimed": False,
            "causalClaimAllowed": False,
            "medicalAdviceAllowed": False,
        },
        "nonProofNote": (
            "This validation proves only that the public NHANES-LMF aggregate pilot "
            "has official-source hashes, aggregate cells and prohibited-use boundaries. "
            "It does not prove calibrated prediction, survey-weighted inference, "
            "external validation, intervention effects or individual use."
        ),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--no-write", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_path = args.input.resolve()
    output_path = args.out.resolve()
    data = load_json(input_path)
    errors = validate_payload(data)
    validation = build_validation(input_path, output_path, errors, data)
    if not args.no_write:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open("w", encoding="utf-8") as handle:
            json.dump(validation, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("NHANES public LMF aggregate pilot ok: cells=8 boundary=aggregate-only")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
