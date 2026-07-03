#!/usr/bin/env python3
"""Validate the NHATS synthetic storage/destruction drill register."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[4]
MANUAL_DIR = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
)
DEFAULT_DRILL = MANUAL_DIR / "life_path_nhats_synthetic_storage_destruction_drill.json"
DEFAULT_PLAN = MANUAL_DIR / "life_path_nhats_controlled_storage_destruction_plan.json"
DEFAULT_ACQUISITION_READINESS = MANUAL_DIR / "life_path_nhats_acquisition_readiness.json"
DEFAULT_OUT = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhats-synthetic-storage-destruction-drill-validation.json"
)

REQUIRED_STEP_IDS = {
    "create-synthetic-zones",
    "write-synthetic-files",
    "hash-synthetic-files",
    "delete-temporary-root",
    "confirm-absence",
}
REQUIRED_ZONES = {
    "raw-download-zone",
    "working-extract-zone",
    "aggregate-output-zone",
}
REQUIRED_ARTIFACT_IDS = {
    "synthetic-public-round-file",
    "synthetic-working-extract",
    "synthetic-aggregate-output",
}
EXPECTED_HASHES = {
    "synthetic-aggregate-output": "46a2d465b1997c4e67d8ed4fff4fe1ea2a37bce3d49c928d8094b36942a90c93",
    "synthetic-public-round-file": "7b342c1e6b523c59f15f29d2dad29f66d04e3fa4fb145a76abd2238a4080e9ee",
    "synthetic-working-extract": "f836cb5583337365d8207ecf6b0684f76e7eb4323269e1663257469604da374f",
}
REQUIRED_FALSE_BOUNDARY = {
    "containsRawNhatsData",
    "containsRawNsocData",
    "containsRowLevelNhatsData",
    "containsIdentifiers",
    "downloadedOfficialFiles",
    "usedNhatsCredentials",
    "usedSessionCookies",
    "publicAiUploadUsed",
    "repositoryRawDataWritten",
    "repositoryRowLevelDataWritten",
    "temporarySyntheticFilesRetained",
    "calibrationAllowed",
    "individualPredictionAllowed",
}
PROHIBITED_KEYS = {
    "password",
    "sessionCookie",
    "sessionCookies",
    "authToken",
    "rawNhatsData",
    "rawNsocData",
    "rowLevelData",
    "individualIdentifier",
    "deathDate",
    "individualDeathDate",
    "predictedDeathDate",
}


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def repo_rel(path: Path) -> str:
    return str(path.resolve().relative_to(REPO_ROOT))


def row_ids(rows: Any, key: str = "id") -> set[str]:
    if not isinstance(rows, list):
        return set()
    return {
        str(row[key])
        for row in rows
        if isinstance(row, dict) and isinstance(row.get(key), str)
    }


def collect_keys(value: Any) -> set[str]:
    keys: set[str] = set()
    if isinstance(value, dict):
        for key, child in value.items():
            keys.add(str(key))
            keys.update(collect_keys(child))
    elif isinstance(value, list):
        for child in value:
            keys.update(collect_keys(child))
    return keys


def has_text(value: Any, needle: str) -> bool:
    return needle.lower() in json.dumps(value, ensure_ascii=False).lower()


def add_check(checks: list[dict[str, Any]], check_id: str, passed: bool, detail: str) -> None:
    checks.append({"id": check_id, "status": "PASS" if passed else "FAIL", "detail": detail})


def summarize(checks: list[dict[str, Any]]) -> dict[str, int]:
    return {
        "pass": sum(1 for check in checks if check["status"] == "PASS"),
        "fail": sum(1 for check in checks if check["status"] == "FAIL"),
    }


def validate_drill(
    drill: dict[str, Any],
    plan: dict[str, Any],
    plan_path: Path,
    acquisition_readiness: dict[str, Any],
    acquisition_readiness_path: Path,
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []

    add_check(
        checks,
        "schema-version",
        drill.get("schemaVersion")
        == "human-infra.life-path-nhats-synthetic-storage-destruction-drill.v1",
        f"schemaVersion={drill.get('schemaVersion')!r}",
    )

    identity_ok = (
        drill.get("sourceId") == "nhats"
        and drill.get("drillId") == "nhats-synthetic-storage-destruction-drill-2026-07-03"
        and drill.get("planId") == plan.get("planId")
        and drill.get("planPath") == repo_rel(plan_path)
        and drill.get("acquisitionReadinessId")
        == acquisition_readiness.get("acquisitionReadinessId")
        and drill.get("acquisitionReadinessPath") == repo_rel(acquisition_readiness_path)
        and drill.get("status") == "synthetic-drill-completed-no-nhats-data"
    )
    add_check(
        checks,
        "drill-identity",
        identity_ok,
        "drill must bind the current NHATS plan and acquisition-readiness register",
    )

    plan_binding_ok = (
        plan.get("syntheticDrillId") == drill.get("drillId")
        and plan.get("syntheticDrillPath") == "domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_synthetic_storage_destruction_drill.json"
    )
    add_check(
        checks,
        "plan-backlink",
        plan_binding_ok,
        "controlled storage/destruction plan must link back to this synthetic drill",
    )

    boundary = drill.get("executionBoundary")
    boundary_ok = isinstance(boundary, dict) and boundary.get("syntheticOnly") is True
    if isinstance(boundary, dict):
        for field in REQUIRED_FALSE_BOUNDARY:
            boundary_ok = boundary_ok and boundary.get(field) is False
    add_check(
        checks,
        "synthetic-only-boundary",
        boundary_ok,
        "drill must be synthetic-only and keep raw data, credentials, public AI, calibration and individual prediction false",
    )

    workspace = drill.get("temporaryWorkspace")
    workspace_ok = (
        isinstance(workspace, dict)
        and isinstance(workspace.get("temporaryRoot"), str)
        and workspace["temporaryRoot"].startswith("/tmp/")
        and workspace.get("rootExistsAfterDeletion") is False
        and workspace.get("notAControlledNhatsWorkspace") is True
        and workspace.get("notARegistrationEvidence") is True
        and workspace.get("notADataAccessEvidence") is True
    )
    add_check(
        checks,
        "temporary-workspace-destroyed",
        workspace_ok,
        "temporary /tmp synthetic root must be recorded as absent after deletion and not treated as governed NHATS evidence",
    )

    steps = drill.get("steps")
    step_ids = row_ids(steps)
    steps_ok = isinstance(steps, list) and REQUIRED_STEP_IDS.issubset(step_ids)
    if isinstance(steps, list):
        for step in steps:
            steps_ok = steps_ok and isinstance(step, dict) and step.get("status") == "pass"
    add_check(
        checks,
        "drill-step-coverage",
        steps_ok,
        f"missing={sorted(REQUIRED_STEP_IDS - step_ids)}",
    )

    artifacts = drill.get("syntheticArtifacts")
    artifact_ids = row_ids(artifacts)
    artifact_ok = isinstance(artifacts, list) and REQUIRED_ARTIFACT_IDS.issubset(artifact_ids)
    zones: set[str] = set()
    hashes: dict[str, str] = {}
    if isinstance(artifacts, list):
        for artifact in artifacts:
            if not isinstance(artifact, dict):
                artifact_ok = False
                continue
            artifact_id = str(artifact.get("id"))
            zones.add(str(artifact.get("zone")))
            hashes[artifact_id] = str(artifact.get("sha256"))
            artifact_ok = (
                artifact_ok
                and artifact.get("destructionStatus") == "destroyed"
                and artifact.get("containsRawOrRowLevelData") is False
                and isinstance(artifact.get("temporaryRelativePath"), str)
                and len(str(artifact.get("sha256"))) == 64
            )
    add_check(
        checks,
        "synthetic-artifact-destruction",
        artifact_ok and REQUIRED_ZONES.issubset(zones),
        f"artifact_ids={sorted(artifact_ids)} zones={sorted(zones)}",
    )

    hash_ok = all(hashes.get(artifact_id) == digest for artifact_id, digest in EXPECTED_HASHES.items())
    add_check(
        checks,
        "synthetic-artifact-hashes",
        hash_ok,
        "synthetic artifact hashes must match the recorded create-hash-delete drill output",
    )

    command = drill.get("commandEvidence")
    command_ok = (
        isinstance(command, dict)
        and command.get("commandClass") == "local-shell-synthetic-filesystem-drill"
        and set(command.get("createdZones", [])) == REQUIRED_ZONES
        and command.get("finalObservation") == "DRILL_ROOT_EXISTS_AFTER_DELETE=0"
        and has_text(command.get("storedEvidencePolicy", ""), "Only synthetic artifact hashes")
    )
    add_check(
        checks,
        "command-evidence-boundary",
        command_ok,
        "command evidence must record only synthetic hashes and absence confirmation",
    )

    readiness = drill.get("readinessImpact")
    readiness_ok = (
        isinstance(readiness, dict)
        and readiness.get("syntheticDrillStatus") == "complete"
        and readiness.get("storageDestructionGateStatus") == "partial"
        and readiness.get("downloadStillBlocked") is True
        and readiness.get("extractionStillBlocked") is True
        and readiness.get("calibrationStillBlocked") is True
        and readiness.get("individualPredictionStillBlocked") is True
    )
    add_check(
        checks,
        "readiness-impact-still-blocking",
        readiness_ok,
        "synthetic drill may only prove drill mechanics while keeping storage gate partial and all model/data actions blocked",
    )

    prohibited_interpretations_ok = (
        has_text(drill.get("prohibitedInterpretations", []), "does not prove NHATS registration")
        and has_text(drill.get("prohibitedInterpretations", []), "does not authorize download")
        and has_text(drill.get("prohibitedInterpretations", []), "does not validate calibration")
    )
    add_check(
        checks,
        "prohibited-interpretations",
        prohibited_interpretations_ok,
        "drill must explicitly forbid registration, access, download, extraction, calibration and prediction interpretations",
    )

    key_set = collect_keys(drill)
    prohibited_keys = sorted(key_set & PROHIBITED_KEYS)
    add_check(
        checks,
        "no-secret-raw-row-level-keys",
        not prohibited_keys,
        f"prohibited_keys={prohibited_keys}",
    )

    source_trace_ok = has_text(drill.get("sourceTrace", []), repo_rel(plan_path)) and has_text(
        drill.get("sourceTrace", []),
        repo_rel(acquisition_readiness_path),
    )
    add_check(
        checks,
        "source-trace",
        source_trace_ok,
        "drill must cite the storage/destruction plan and acquisition-readiness register",
    )

    return checks


def build_report(
    drill_path: Path,
    plan_path: Path,
    acquisition_readiness_path: Path,
    drill: dict[str, Any],
    plan: dict[str, Any],
    acquisition_readiness: dict[str, Any],
) -> dict[str, Any]:
    checks = validate_drill(
        drill,
        plan,
        plan_path,
        acquisition_readiness,
        acquisition_readiness_path,
    )
    summary = summarize(checks)
    return {
        "schemaVersion": "human-infra.life-path-nhats-synthetic-storage-destruction-drill-validation.v1",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "sourceId": drill.get("sourceId"),
        "drillId": drill.get("drillId"),
        "drillPath": repo_rel(drill_path),
        "drillSha256": sha256_file(drill_path),
        "planId": plan.get("planId"),
        "planPath": repo_rel(plan_path),
        "planSha256": sha256_file(plan_path),
        "acquisitionReadinessId": acquisition_readiness.get("acquisitionReadinessId"),
        "acquisitionReadinessPath": repo_rel(acquisition_readiness_path),
        "acquisitionReadinessSha256": sha256_file(acquisition_readiness_path),
        "overallStatus": "PASS" if summary["fail"] == 0 else "FAIL",
        "summary": summary,
        "checks": checks,
        "readinessImpact": drill.get("readinessImpact"),
        "boundary": {
            "syntheticOnly": True,
            "officialFilesDownloaded": False,
            "rawDataInRepository": False,
            "rowLevelDataInRepository": False,
            "publicAiUploadUsed": False,
            "calibrationAllowed": False,
            "individualPredictionAllowed": False
        },
        "note": "This validation proves only that a synthetic create-hash-delete drill record is internally consistent. It does not prove NHATS registration, governed workspace provisioning, NHATS download, extraction, calibration, validation or individual prediction."
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--drill", type=Path, default=DEFAULT_DRILL)
    parser.add_argument("--plan", type=Path, default=DEFAULT_PLAN)
    parser.add_argument(
        "--acquisition-readiness",
        type=Path,
        default=DEFAULT_ACQUISITION_READINESS,
    )
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    drill = load_json(args.drill)
    plan = load_json(args.plan)
    acquisition_readiness = load_json(args.acquisition_readiness)
    report = build_report(
        args.drill,
        args.plan,
        args.acquisition_readiness,
        drill,
        plan,
        acquisition_readiness,
    )
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        "nhats synthetic storage/destruction drill validation:",
        report["overallStatus"],
        report["summary"],
    )
    return 0 if report["overallStatus"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
