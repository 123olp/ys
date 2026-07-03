#!/usr/bin/env python3
"""Validate the NHATS registration evidence template."""

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
DEFAULT_TEMPLATE = MANUAL_DIR / "life_path_nhats_registration_evidence_template.json"
DEFAULT_ACQUISITION_READINESS = MANUAL_DIR / "life_path_nhats_acquisition_readiness.json"
DEFAULT_OFFICIAL_SOURCE_REFRESH = (
    MANUAL_DIR / "life_path_nhats_official_source_refresh_register.json"
)
DEFAULT_OUT = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhats-registration-evidence-template-validation.json"
)

REQUIRED_SCHEMA = "human-infra.life-path-nhats-registration-evidence-template.v1"
REQUIRED_STATUS = "template-only-registration-not-complete"
REQUIRED_TRUE_DECISIONS = {"templateReady"}
REQUIRED_FALSE_DECISIONS = {
    "registeredAccountConfirmed",
    "permittedUserBoundaryConfirmed",
    "conditionsOfUseAttested",
    "fileTierApprovalRecorded",
    "controlledWorkspaceProvisioned",
    "nonRepositoryEvidenceRecorded",
    "secondReviewerSignoff",
    "downloadAllowed",
    "extractionScriptAllowed",
    "rawDataAllowedInRepository",
    "publicAiUploadAllowed",
    "calibrationAllowed",
    "individualPredictionAllowed",
}
REQUIRED_SLOT_IDS = {
    "registered-account-status",
    "permitted-user-boundary",
    "conditions-of-use-attestation",
    "public-use-file-access-tier",
    "sensitive-restricted-approval-boundary",
    "controlled-workspace-linkage",
    "no-public-secret-storage",
    "second-reviewer-signoff",
}
REQUIRED_PROHIBITED_PHRASES = {
    "download NHATS or NSOC files",
    "real extraction scripts",
    "credentials",
    "raw NHATS",
    "public AI systems",
    "calibration",
    "individual prediction",
}
PROHIBITED_KEYS = {
    "password",
    "sessionCookie",
    "sessionCookies",
    "authToken",
    "downloadToken",
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


def row_ids(rows: Any, key: str = "id") -> set[str]:
    if not isinstance(rows, list):
        return set()
    return {
        str(row[key])
        for row in rows
        if isinstance(row, dict) and isinstance(row.get(key), str)
    }


def add_check(checks: list[dict[str, Any]], check_id: str, passed: bool, detail: str) -> None:
    checks.append({"id": check_id, "status": "PASS" if passed else "FAIL", "detail": detail})


def summarize(checks: list[dict[str, Any]]) -> dict[str, int]:
    return {
        "pass": sum(1 for check in checks if check["status"] == "PASS"),
        "fail": sum(1 for check in checks if check["status"] == "FAIL"),
    }


def validate_template(template: dict[str, Any]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []

    add_check(
        checks,
        "schema-version",
        template.get("schemaVersion") == REQUIRED_SCHEMA,
        f"schemaVersion={template.get('schemaVersion')!r}",
    )

    identity_ok = (
        template.get("sourceId") == "nhats"
        and template.get("templateId") == "nhats-registration-evidence-template-2026-07-03"
        and template.get("acquisitionReadinessId") == "nhats-acquisition-readiness-2026-07-02"
        and template.get("officialSourceRefreshRegisterId")
        == "nhats-official-source-refresh-2026-07-03"
        and template.get("status") == REQUIRED_STATUS
    )
    add_check(
        checks,
        "template-identity",
        identity_ok,
        "template must bind NHATS acquisition readiness and official source refresh while staying template-only",
    )

    decision = template.get("currentDecision")
    decision_ok = isinstance(decision, dict)
    if isinstance(decision, dict):
        for field in REQUIRED_TRUE_DECISIONS:
            decision_ok = decision_ok and decision.get(field) is True
        for field in REQUIRED_FALSE_DECISIONS:
            decision_ok = decision_ok and decision.get(field) is False
    add_check(
        checks,
        "decision-boundary",
        decision_ok,
        "only templateReady may be true; registration, download, extraction, raw data, public AI upload, calibration and individual prediction must remain false",
    )

    source_bindings = template.get("sourceBindings")
    expected_bindings = {
        "acquisitionReadinessPath": repo_rel(DEFAULT_ACQUISITION_READINESS),
        "officialSourceRefreshRegisterPath": repo_rel(DEFAULT_OFFICIAL_SOURCE_REFRESH),
    }
    bindings_ok = isinstance(source_bindings, dict) and all(
        source_bindings.get(key) == expected for key, expected in expected_bindings.items()
    )
    add_check(
        checks,
        "source-bindings",
        bindings_ok
        and DEFAULT_ACQUISITION_READINESS.exists()
        and DEFAULT_OFFICIAL_SOURCE_REFRESH.exists(),
        "template must point to current acquisition-readiness and official-source-refresh registers",
    )

    slots = template.get("evidenceSlots")
    slot_ids = row_ids(slots)
    slots_ok = isinstance(slots, list) and all(
        isinstance(slot, dict)
        and slot.get("currentStatus") == "missing"
        and slot.get("blocksExtraction") is True
        and isinstance(slot.get("requiredEvidence"), str)
        and isinstance(slot.get("repositoryRepresentation"), str)
        for slot in slots
    )
    add_check(
        checks,
        "evidence-slots",
        slots_ok and REQUIRED_SLOT_IDS.issubset(slot_ids),
        f"missing={sorted(REQUIRED_SLOT_IDS - slot_ids)}",
    )

    allowed_fields = set(template.get("allowedRepositoryFields") or [])
    forbidden_fields = set(template.get("forbiddenRepositoryFields") or [])
    field_policy_ok = {
        "redactedRegistrationStatus",
        "fileTierDecision",
        "nonSensitiveEvidenceHash",
        "secondReviewStatus",
    }.issubset(allowed_fields) and {
        "password",
        "sessionCookie",
        "authToken",
        "downloadToken",
        "rawNhatsData",
        "rowLevelData",
        "individualDeathDate",
    }.issubset(forbidden_fields)
    add_check(
        checks,
        "repository-field-policy",
        field_policy_ok,
        "template must separate allowed redacted metadata from forbidden private or row-level fields",
    )

    blocked_until = template.get("blockedUntil")
    blocked_ok = isinstance(blocked_until, list) and all(
        has_text(blocked_until, phrase)
        for phrase in [
            "registered account",
            "permitted user",
            "Conditions of Use",
            "file tiers",
            "controlled workspace",
            "second reviewer",
        ]
    )
    add_check(
        checks,
        "blocked-until",
        blocked_ok,
        "template must keep account, user boundary, conditions, file tier, workspace and second review as blockers",
    )

    prohibited_actions = template.get("prohibitedActions")
    prohibited_ok = isinstance(prohibited_actions, list) and all(
        has_text(prohibited_actions, phrase) for phrase in REQUIRED_PROHIBITED_PHRASES
    )
    add_check(
        checks,
        "prohibited-actions",
        prohibited_ok,
        "template must block download, real extraction scripts, credentials, raw data, public AI upload, calibration and individual prediction",
    )

    gate_impact = template.get("gateImpact")
    gate_impact_ok = isinstance(gate_impact, dict) and (
        gate_impact.get("acquisitionGateId") == "registration-status"
        and gate_impact.get("acquisitionGateStatus") == "partial-template-only"
        and gate_impact.get("registrationEvidenceComplete") is False
        and gate_impact.get("downloadStillBlocked") is True
        and gate_impact.get("extractionStillBlocked") is True
        and gate_impact.get("calibrationStillBlocked") is True
        and gate_impact.get("individualPredictionStillBlocked") is True
    )
    add_check(
        checks,
        "gate-impact",
        gate_impact_ok,
        "template may move registration-status to partial-template-only but must keep download, extraction, calibration and individual prediction blocked",
    )

    source_trace = set(template.get("sourceTrace") or [])
    add_check(
        checks,
        "source-trace",
        {
            "https://www.nhats.org/data-access",
            "https://www.nhats.org/conditions-of-use",
            repo_rel(DEFAULT_ACQUISITION_READINESS),
            repo_rel(DEFAULT_OFFICIAL_SOURCE_REFRESH),
        }.issubset(source_trace),
        "template must trace official public access pages and local upstream registers",
    )

    key_hits = sorted(collect_keys(template) & PROHIBITED_KEYS)
    add_check(
        checks,
        "no-credential-or-raw-data-keys",
        not key_hits,
        f"prohibited_keys={key_hits}",
    )

    return checks


def build_report(template_path: Path, template: dict[str, Any]) -> dict[str, Any]:
    checks = validate_template(template)
    decision = template.get("currentDecision") if isinstance(template.get("currentDecision"), dict) else {}
    return {
        "schemaVersion": "human-infra.life-path-nhats-registration-evidence-template-validation.v1",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "templatePath": repo_rel(template_path),
        "templateSha256": sha256_file(template_path),
        "acquisitionReadinessPath": repo_rel(DEFAULT_ACQUISITION_READINESS),
        "acquisitionReadinessSha256": sha256_file(DEFAULT_ACQUISITION_READINESS),
        "officialSourceRefreshRegisterPath": repo_rel(DEFAULT_OFFICIAL_SOURCE_REFRESH),
        "officialSourceRefreshRegisterSha256": sha256_file(DEFAULT_OFFICIAL_SOURCE_REFRESH),
        "templateId": template.get("templateId"),
        "overallStatus": "PASS" if summarize(checks)["fail"] == 0 else "FAIL",
        "summary": summarize(checks),
        "boundary": {
            "templateReady": decision.get("templateReady"),
            "registeredAccountConfirmed": decision.get("registeredAccountConfirmed"),
            "downloadAllowed": decision.get("downloadAllowed"),
            "extractionScriptAllowed": decision.get("extractionScriptAllowed"),
            "rawDataAllowedInRepository": decision.get("rawDataAllowedInRepository"),
            "publicAiUploadAllowed": decision.get("publicAiUploadAllowed"),
            "calibrationAllowed": decision.get("calibrationAllowed"),
            "individualPredictionAllowed": decision.get("individualPredictionAllowed"),
        },
        "checks": checks,
        "note": "This validation proves only that the NHATS registration evidence template exists and keeps all real registration, download, extraction, calibration and individual-use actions blocked. It does not prove NHATS registration, data access approval, controlled workspace execution or model readiness.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    template_path = args.template.resolve()
    out_path = args.out.resolve()
    template = load_json(template_path)
    report = build_report(template_path, template)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as handle:
        json.dump(report, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(f"wrote {repo_rel(out_path)}")
    print(f"status={report['overallStatus']} checks={report['summary']}")
    return 0 if report["overallStatus"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
