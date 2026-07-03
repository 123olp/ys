#!/usr/bin/env python3
"""Validate the NHATS controlled storage and destruction plan."""

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
DEFAULT_PLAN = MANUAL_DIR / "life_path_nhats_controlled_storage_destruction_plan.json"
DEFAULT_ACQUISITION_READINESS = MANUAL_DIR / "life_path_nhats_acquisition_readiness.json"
DEFAULT_OUT = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhats-controlled-storage-destruction-validation.json"
)

REQUIRED_FALSE_DECISIONS = {
    "planExecuted",
    "registrationRecorded",
    "controlledWorkspaceProvisioned",
    "accessLogInitialized",
    "dataInventoryInitialized",
    "downloadAllowed",
    "extractionScriptAllowed",
    "rawDataAllowedInRepository",
    "publicAiUploadAllowed",
    "publicExportAllowed",
    "calibrationAllowed",
    "individualPredictionAllowed",
}
REQUIRED_REQUIRED_ZONES = {
    "raw-download-zone",
    "working-extract-zone",
    "aggregate-output-zone",
}
REQUIRED_INVENTORY_SLOTS = {
    "file-family",
    "round",
    "access-tier",
    "local-controlled-path",
    "sha256",
    "retention-class",
    "destruction-status",
}
REQUIRED_DESTRUCTION_STEPS = {
    "freeze-workspace",
    "inventory-match",
    "delete-controlled-copies",
    "review-derived-outputs",
    "record-destruction-log",
    "second-reviewer-signoff",
}
REQUIRED_LOG_FIELDS = {
    "eventId",
    "timestamp",
    "actorBoundary",
    "action",
    "fileFamily",
    "round",
    "accessTier",
    "controlledPathAlias",
    "containsRawOrRowLevelData",
    "repositoryExportRequested",
    "publicAiUploadRequested",
    "disclosureReviewStatus",
    "destructionStatus",
    "reviewerNotes",
    "secondReviewerSignoff",
}
REQUIRED_PROHIBITED_ACTIONS = {
    "download NHATS or NSOC files before every acquisition-readiness gate is ready",
    "place raw NHATS or NSOC files in this repository",
    "place row-level derived NHATS or NSOC extracts in this repository",
    "store NHATS credentials, cookies or tokens in this repository",
    "upload raw or row-level NHATS or NSOC data to public LLMs or AI platforms",
    "export small cells or unsuppressed sensitive tabulations",
    "write extraction scripts before exact fields, file tiers, survey design and disclosure gates pass",
    "claim calibration, validation, intervention effect or individual prediction before governed cohort diagnostics exist",
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
REPOSITORY_PATH_PREFIXES = {
    "docs/",
    "domains/",
    "tools/",
    "web/",
    "README.md",
    "AGENTS.md",
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


def as_set(value: Any) -> set[str]:
    if not isinstance(value, list):
        return set()
    return {str(item) for item in value}


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


def validate_plan(
    plan: dict[str, Any],
    acquisition_readiness: dict[str, Any],
    acquisition_readiness_path: Path,
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []

    add_check(
        checks,
        "schema-version",
        plan.get("schemaVersion")
        == "human-infra.life-path-nhats-controlled-storage-destruction-plan.v1",
        f"schemaVersion={plan.get('schemaVersion')!r}",
    )

    identity_ok = (
        plan.get("sourceId") == "nhats"
        and plan.get("planId") == "nhats-controlled-storage-destruction-plan-2026-07-03"
        and plan.get("acquisitionReadinessId")
        == acquisition_readiness.get("acquisitionReadinessId")
        and plan.get("acquisitionReadinessPath") == repo_rel(acquisition_readiness_path)
        and plan.get("status") == "plan-only-not-executed-no-data-acquired"
    )
    add_check(
        checks,
        "plan-identity",
        identity_ok,
        "plan must bind NHATS acquisition readiness while staying plan-only and no-data-acquired",
    )

    decision = plan.get("currentDecision")
    decision_ok = isinstance(decision, dict) and decision.get("planDefined") is True
    if isinstance(decision, dict):
        for field in REQUIRED_FALSE_DECISIONS:
            decision_ok = decision_ok and decision.get(field) is False
    add_check(
        checks,
        "current-decision-boundary",
        decision_ok,
        "only planDefined may be true; execution, download, extraction, repository raw data, public AI, calibration and individual prediction must remain false",
    )

    boundary = plan.get("storageBoundary")
    workspace_ok = False
    forbidden_locations_ok = False
    zones_ok = False
    if isinstance(boundary, dict):
        root = boundary.get("controlledWorkspaceRoot")
        workspace_ok = (
            isinstance(root, str)
            and root.startswith("<controlled-non-repository-workspace>")
            and not any(root.startswith(prefix) for prefix in REPOSITORY_PATH_PREFIXES)
        )
        forbidden_locations = as_set(boundary.get("explicitlyForbiddenLocations"))
        forbidden_locations_ok = any("public LLM" in item for item in forbidden_locations) and {
            "docs/",
            "domains/",
            "web/",
            "tools/",
        }.issubset(forbidden_locations)
        zones = boundary.get("requiredOutsideRepositoryZones")
        zones_ok = isinstance(zones, list) and REQUIRED_REQUIRED_ZONES.issubset(row_ids(zones))
        if isinstance(zones, list):
            for zone in zones:
                zones_ok = zones_ok and isinstance(zone, dict) and zone.get("status") == "not-created"
    add_check(
        checks,
        "controlled-workspace-outside-repo",
        workspace_ok,
        "controlled workspace root must be a non-repository placeholder, not a repository path",
    )
    add_check(
        checks,
        "repository-forbidden-locations",
        forbidden_locations_ok,
        "plan must explicitly forbid raw, row-level, credential or public AI locations including docs/domains/web/tools",
    )
    add_check(
        checks,
        "outside-repository-zones",
        zones_ok,
        "raw, working extract and aggregate output zones must be required outside the repository and not yet created",
    )

    access = plan.get("accessControl")
    access_ok = (
        isinstance(access, dict)
        and access.get("authorizedUserBoundaryRecordedOutsideRepo") is False
        and access.get("leastPrivilegeRequired") is True
        and access.get("credentialStorageInRepositoryAllowed") is False
        and access.get("sessionCookieStorageAllowed") is False
        and access.get("publicAiAccessAllowed") is False
        and isinstance(access.get("requiredPreDownloadEvidence"), list)
        and len(access["requiredPreDownloadEvidence"]) >= 6
    )
    add_check(
        checks,
        "access-control-boundary",
        access_ok,
        "access control must require least privilege while keeping registration, credentials, cookies and public AI blocked",
    )

    inventory = plan.get("inventorySlots")
    inventory_ok = isinstance(inventory, list) and REQUIRED_INVENTORY_SLOTS.issubset(
        row_ids(inventory)
    )
    if isinstance(inventory, list):
        for slot in inventory:
            inventory_ok = (
                inventory_ok
                and isinstance(slot, dict)
                and slot.get("required") is True
                and slot.get("status") == "empty"
            )
    add_check(
        checks,
        "inventory-slots-empty",
        inventory_ok,
        "inventory must define required slots and keep every slot empty before data acquisition",
    )

    destruction = plan.get("destructionProtocol")
    destruction_ok = (
        isinstance(destruction, dict)
        and destruction.get("status") == "defined-only-not-tested"
        and isinstance(destruction.get("triggerEvents"), list)
        and len(destruction["triggerEvents"]) >= 5
        and REQUIRED_DESTRUCTION_STEPS.issubset(row_ids(destruction.get("requiredSteps")))
    )
    if isinstance(destruction, dict) and isinstance(destruction.get("requiredSteps"), list):
        for step in destruction["requiredSteps"]:
            destruction_ok = (
                destruction_ok
                and isinstance(step, dict)
                and step.get("status") == "defined"
            )
    add_check(
        checks,
        "destruction-protocol-defined-only",
        destruction_ok,
        "destruction protocol must define trigger events and required steps but remain untested",
    )

    audit_log = plan.get("auditLogTemplate")
    audit_log_ok = (
        isinstance(audit_log, dict)
        and audit_log.get("status") == "template-only-no-log-created"
        and REQUIRED_LOG_FIELDS.issubset(as_set(audit_log.get("requiredFields")))
        and PROHIBITED_KEYS.issubset(as_set(audit_log.get("prohibitedFields")))
    )
    add_check(
        checks,
        "audit-log-template",
        audit_log_ok,
        "audit log template must contain required fields, prohibited fields and no created log",
    )

    readiness_impact = plan.get("readinessImpact")
    impact_ok = (
        isinstance(readiness_impact, dict)
        and readiness_impact.get("storageDestructionGateStatus") == "partial"
        and readiness_impact.get("extractionStillBlocked") is True
        and readiness_impact.get("downloadStillBlocked") is True
        and readiness_impact.get("calibrationStillBlocked") is True
    )
    add_check(
        checks,
        "readiness-impact-partial-blocking",
        impact_ok,
        "plan may only move storage/destruction to partial while keeping extraction, download and calibration blocked",
    )

    allowed_ai_ok = (
        has_text(plan.get("allowedAiInputs", []), "public NHATS documentation URLs")
        and has_text(plan.get("allowedAiInputs", []), "synthetic")
        and has_text(plan.get("allowedAiInputs", []), "aggregate non-disclosive")
    )
    add_check(
        checks,
        "allowed-ai-input-boundary",
        allowed_ai_ok,
        "allowed AI inputs must stay limited to public docs, plan metadata, synthetic examples and aggregate non-disclosive outputs",
    )

    missing_prohibited = sorted(REQUIRED_PROHIBITED_ACTIONS - as_set(plan.get("prohibitedActions")))
    add_check(
        checks,
        "prohibited-actions",
        not missing_prohibited,
        f"missing={missing_prohibited}",
    )

    key_set = collect_keys(plan)
    prohibited_keys = sorted(key_set & PROHIBITED_KEYS)
    add_check(
        checks,
        "no-secret-raw-row-level-keys",
        not prohibited_keys,
        f"prohibited_keys={prohibited_keys}",
    )

    source_trace_ok = (
        has_text(plan.get("sourceTrace", []), "https://www.nhats.org/data-access")
        and has_text(plan.get("sourceTrace", []), "https://www.nhats.org/conditions-of-use")
        and has_text(plan.get("sourceTrace", []), repo_rel(acquisition_readiness_path))
    )
    add_check(
        checks,
        "source-trace",
        source_trace_ok,
        "plan must cite official NHATS access/conditions and acquisition-readiness register",
    )

    return checks


def build_report(
    plan_path: Path,
    acquisition_readiness_path: Path,
    plan: dict[str, Any],
    acquisition_readiness: dict[str, Any],
) -> dict[str, Any]:
    checks = validate_plan(plan, acquisition_readiness, acquisition_readiness_path)
    summary = summarize(checks)
    return {
        "schemaVersion": "human-infra.life-path-nhats-controlled-storage-destruction-plan-validation.v1",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "sourceId": plan.get("sourceId"),
        "planId": plan.get("planId"),
        "planPath": repo_rel(plan_path),
        "planSha256": sha256_file(plan_path),
        "acquisitionReadinessId": acquisition_readiness.get("acquisitionReadinessId"),
        "acquisitionReadinessPath": repo_rel(acquisition_readiness_path),
        "acquisitionReadinessSha256": sha256_file(acquisition_readiness_path),
        "overallStatus": "PASS" if summary["fail"] == 0 else "FAIL",
        "summary": summary,
        "checks": checks,
        "readinessImpact": plan.get("readinessImpact"),
        "boundary": {
            "planDefined": True,
            "planExecuted": False,
            "downloadAllowed": False,
            "extractionScriptAllowed": False,
            "rawDataAllowedInRepository": False,
            "publicAiUploadAllowed": False,
            "calibrationAllowed": False,
            "individualPredictionAllowed": False
        },
        "note": "This validation proves only that a controlled storage/destruction plan exists and still blocks acquisition. It does not prove registration, governed workspace provisioning, NHATS download, extraction, calibration, validation or individual prediction."
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
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
    plan = load_json(args.plan)
    acquisition_readiness = load_json(args.acquisition_readiness)
    report = build_report(
        args.plan,
        args.acquisition_readiness,
        plan,
        acquisition_readiness,
    )
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        "nhats controlled storage/destruction validation:",
        report["overallStatus"],
        report["summary"],
    )
    return 0 if report["overallStatus"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
