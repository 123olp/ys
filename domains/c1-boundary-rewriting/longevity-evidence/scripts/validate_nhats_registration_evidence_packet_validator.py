#!/usr/bin/env python3
"""Validate future NHATS registration evidence packet preflight semantics."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
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
DEFAULT_TEST_CASES = (
    MANUAL_DIR / "life_path_nhats_registration_evidence_packet_validator_test_cases.json"
)
DEFAULT_TEMPLATE = MANUAL_DIR / "life_path_nhats_registration_evidence_template.json"
DEFAULT_OUT = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhats-registration-evidence-packet-validator-validation.json"
)

TEST_CASES_SCHEMA = (
    "human-infra.life-path-nhats-registration-evidence-packet-validator-test-cases.v1"
)
VALIDATION_SCHEMA = (
    "human-infra.life-path-nhats-registration-evidence-packet-validator-validation.v1"
)
PACKET_SCHEMA = "human-infra.life-path-nhats-registration-evidence-packet.v1"
HASH_RE = re.compile(r"^sha256:[a-fA-F0-9]{64}$")

VERDICT_REVIEWABLE = "reviewable-but-still-blocked"
VERDICT_CANNOT_EVALUATE = "cannot-evaluate"
VERDICT_REJECTED = "rejected"
ALLOWED_VERDICTS = {VERDICT_REVIEWABLE, VERDICT_CANNOT_EVALUATE, VERDICT_REJECTED}

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
REQUIRED_PACKET_FIELDS = {
    "packetSchema",
    "packetId",
    "sourceId",
    "templateId",
    "acquisitionReadinessId",
    "evidenceDate",
    "evidenceSlotIds",
    "redactedRegistrationStatus",
    "conditionsOfUseAttestation",
    "controlledWorkspaceLinkage",
    "noPublicSecretStorageCheck",
    "secondReviewStatus",
    "downloadAllowed",
    "extractionScriptAllowed",
    "rawDataAllowedInRepository",
    "publicAiUploadAllowed",
    "calibrationAllowed",
    "individualPredictionAllowed",
}
REQUIRED_FALSE_FIELDS = {
    "downloadAllowed",
    "extractionScriptAllowed",
    "rawDataAllowedInRepository",
    "publicAiUploadAllowed",
    "calibrationAllowed",
    "individualPredictionAllowed",
}
PROHIBITED_KEYS = {
    "password",
    "sessionCookie",
    "sessionCookies",
    "authToken",
    "accessToken",
    "downloadToken",
    "privateAccountProfile",
    "accountEmail",
    "accountId",
    "rawNhatsData",
    "rawNsocData",
    "rowLevelData",
    "individualIdentifier",
    "deathDate",
    "individualDeathDate",
    "predictedDeathDate",
}
REQUIRED_BLOCKED_DECISION = {
    "realRegistrationEvidenceAttached": False,
    "registrationGateClosureAllowed": False,
    "downloadAllowed": False,
    "extractionScriptAllowed": False,
    "rawDataAllowedInRepository": False,
    "publicAiUploadAllowed": False,
    "calibrationAllowed": False,
    "individualPredictionAllowed": False,
}


def load_json(path: Path, label: str) -> dict[str, Any]:
    if not path.exists():
        raise ValueError(f"missing {label}: {repo_rel(path)}")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid {label} JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"{label} must be a JSON object")
    return data


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def repo_rel(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


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


def hash_fields_are_valid(value: Any) -> bool:
    if isinstance(value, dict):
        for key, child in value.items():
            if str(key).endswith("Hash") and (
                not isinstance(child, str) or not HASH_RE.fullmatch(child)
            ):
                return False
            if not hash_fields_are_valid(child):
                return False
        return True
    if isinstance(value, list):
        return all(hash_fields_are_valid(child) for child in value)
    return True


def section_hashes_are_valid(section: Any) -> bool:
    if not isinstance(section, dict):
        return False
    for key, value in section.items():
        if key.endswith("Hash") and (not isinstance(value, str) or not HASH_RE.fullmatch(value)):
            return False
    return True


def evaluate_packet(packet: Any, template: dict[str, Any]) -> dict[str, Any]:
    reject_reasons: list[str] = []
    cannot_evaluate_reasons: list[str] = []

    if not isinstance(packet, dict):
        return {
            **REQUIRED_BLOCKED_DECISION,
            "packetId": None,
            "verdict": VERDICT_REJECTED,
            "rejectReasons": ["packet must be a JSON object"],
            "cannotEvaluateReasons": [],
            "missingSlotIds": sorted(REQUIRED_SLOT_IDS),
        }

    missing_fields = sorted(REQUIRED_PACKET_FIELDS - set(packet))
    if missing_fields:
        cannot_evaluate_reasons.append(f"missing required fields: {', '.join(missing_fields)}")

    forbidden_keys = sorted(collect_keys(packet) & PROHIBITED_KEYS)
    if forbidden_keys:
        reject_reasons.append(f"forbidden keys present: {', '.join(forbidden_keys)}")

    if packet.get("packetSchema") != PACKET_SCHEMA:
        reject_reasons.append("packetSchema mismatch")
    if packet.get("sourceId") != "nhats":
        reject_reasons.append("sourceId must be nhats")
    if packet.get("templateId") != template.get("templateId"):
        reject_reasons.append("templateId does not match registration evidence template")
    if packet.get("acquisitionReadinessId") != template.get("acquisitionReadinessId"):
        reject_reasons.append("acquisitionReadinessId does not match template")

    for field in REQUIRED_FALSE_FIELDS:
        if packet.get(field) is not False:
            reject_reasons.append(f"{field} must be false")

    conditions = packet.get("conditionsOfUseAttestation")
    if isinstance(conditions, dict):
        if conditions.get("attested") is not True:
            cannot_evaluate_reasons.append("conditionsOfUseAttestation.attested must be true")
        if conditions.get("publicAiUploadAllowed") is not False:
            reject_reasons.append("conditionsOfUseAttestation.publicAiUploadAllowed must be false")
        if conditions.get("unauthorizedSharingAllowed") not in {False, None}:
            reject_reasons.append("conditionsOfUseAttestation.unauthorizedSharingAllowed must be false")
    elif "conditionsOfUseAttestation" in packet:
        cannot_evaluate_reasons.append("conditionsOfUseAttestation must be an object")

    workspace = packet.get("controlledWorkspaceLinkage")
    if isinstance(workspace, dict):
        if workspace.get("provisionedOutsideRepository") is not True:
            cannot_evaluate_reasons.append("controlledWorkspaceLinkage.provisionedOutsideRepository must be true")
        if not section_hashes_are_valid(workspace):
            cannot_evaluate_reasons.append("controlledWorkspaceLinkage hash fields must be sha256-prefixed digests")
    elif "controlledWorkspaceLinkage" in packet:
        cannot_evaluate_reasons.append("controlledWorkspaceLinkage must be an object")

    no_secret = packet.get("noPublicSecretStorageCheck")
    if isinstance(no_secret, dict):
        if no_secret.get("passed") is not True:
            cannot_evaluate_reasons.append("noPublicSecretStorageCheck.passed must be true")
        if no_secret.get("credentialAbsent") is not True:
            cannot_evaluate_reasons.append("noPublicSecretStorageCheck.credentialAbsent must be true")
        if no_secret.get("rawDataAbsent") is not True:
            cannot_evaluate_reasons.append("noPublicSecretStorageCheck.rawDataAbsent must be true")
        if not section_hashes_are_valid(no_secret):
            cannot_evaluate_reasons.append("noPublicSecretStorageCheck hash fields must be sha256-prefixed digests")
    elif "noPublicSecretStorageCheck" in packet:
        cannot_evaluate_reasons.append("noPublicSecretStorageCheck must be an object")

    second_review = packet.get("secondReviewStatus")
    if isinstance(second_review, dict):
        status = str(second_review.get("status", "")).lower()
        reviewer_role = str(second_review.get("reviewerRole", "")).lower()
        if "signed-off" not in status:
            cannot_evaluate_reasons.append("secondReviewStatus.status must be signed-off")
        if "independent" not in reviewer_role or "human" not in reviewer_role:
            cannot_evaluate_reasons.append("secondReviewStatus.reviewerRole must identify an independent human reviewer")
        if not section_hashes_are_valid(second_review):
            cannot_evaluate_reasons.append("secondReviewStatus hash fields must be sha256-prefixed digests")
    elif "secondReviewStatus" in packet:
        cannot_evaluate_reasons.append("secondReviewStatus must be an object")

    slot_ids = set(packet.get("evidenceSlotIds") or [])
    missing_slot_ids = sorted(REQUIRED_SLOT_IDS - {str(slot_id) for slot_id in slot_ids})
    if missing_slot_ids:
        cannot_evaluate_reasons.append(f"missing evidence slots: {', '.join(missing_slot_ids)}")

    if not hash_fields_are_valid(packet):
        reject_reasons.append("one or more hash-like fields are malformed")

    if reject_reasons:
        verdict = VERDICT_REJECTED
    elif cannot_evaluate_reasons:
        verdict = VERDICT_CANNOT_EVALUATE
    else:
        verdict = VERDICT_REVIEWABLE

    return {
        **REQUIRED_BLOCKED_DECISION,
        "packetId": packet.get("packetId"),
        "verdict": verdict,
        "rejectReasons": reject_reasons,
        "cannotEvaluateReasons": cannot_evaluate_reasons,
        "missingSlotIds": missing_slot_ids,
    }


def validate_test_cases(
    test_cases: dict[str, Any],
    template: dict[str, Any],
) -> dict[str, Any]:
    if test_cases.get("schemaVersion") != TEST_CASES_SCHEMA:
        raise ValueError("test case schemaVersion mismatch")
    if test_cases.get("status") != "synthetic-validator-test-cases-only-registration-still-blocked":
        raise ValueError("test cases must remain synthetic-only and registration-still-blocked")

    bindings = test_cases.get("sourceBindings")
    expected_template_path = repo_rel(DEFAULT_TEMPLATE)
    if not isinstance(bindings, dict) or bindings.get("registrationEvidenceTemplatePath") != expected_template_path:
        raise ValueError("test case sourceBindings do not match validator defaults")

    raw_cases = test_cases.get("testCases")
    if not isinstance(raw_cases, list) or len(raw_cases) < 5:
        raise ValueError("testCases must contain at least five cases")

    case_results: list[dict[str, Any]] = []
    failures: list[str] = []
    counts = {VERDICT_REVIEWABLE: 0, VERDICT_CANNOT_EVALUATE: 0, VERDICT_REJECTED: 0}
    for index, case in enumerate(raw_cases):
        if not isinstance(case, dict):
            failures.append(f"testCases[{index}] must be an object")
            continue
        case_id = str(case.get("caseId", f"case-{index}"))
        expected = case.get("expectedVerdict")
        if expected not in ALLOWED_VERDICTS:
            failures.append(f"{case_id} has invalid expectedVerdict")
            continue
        result = evaluate_packet(case.get("packet"), template)
        verdict = result["verdict"]
        counts[verdict] = counts.get(verdict, 0) + 1
        blocked_ok = all(result.get(key) is value for key, value in REQUIRED_BLOCKED_DECISION.items())
        passed = verdict == expected and blocked_ok
        if not passed:
            failures.append(f"{case_id} expected {expected}, got {verdict}")
        case_results.append(
            {
                "caseId": case_id,
                "expectedVerdict": expected,
                "actualVerdict": verdict,
                "passed": passed,
                "rejectReasons": result["rejectReasons"],
                "cannotEvaluateReasons": result["cannotEvaluateReasons"],
                "missingSlotIds": result["missingSlotIds"],
            }
        )

    if counts[VERDICT_REVIEWABLE] < 1:
        failures.append("at least one reviewable-but-still-blocked case is required")
    if counts[VERDICT_CANNOT_EVALUATE] < 1:
        failures.append("at least one cannot-evaluate case is required")
    if counts[VERDICT_REJECTED] < 3:
        failures.append("at least three rejected cases are required")

    return {
        "schemaVersion": VALIDATION_SCHEMA,
        "validationId": "nhats-registration-evidence-packet-validator-validation-2026-07-04",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "status": "pass" if not failures else "fail",
        "sourceRefs": {
            "testCasesPath": repo_rel(DEFAULT_TEST_CASES),
            "testCasesSha256": sha256_file(DEFAULT_TEST_CASES),
            "registrationEvidenceTemplatePath": repo_rel(DEFAULT_TEMPLATE),
            "registrationEvidenceTemplateSha256": sha256_file(DEFAULT_TEMPLATE),
            "validator": "domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_registration_evidence_packet_validator.py",
        },
        "currentDecision": {
            "validatorReady": not failures,
            "testCaseCount": len(raw_cases),
            "reviewableButStillBlockedCount": counts[VERDICT_REVIEWABLE],
            "cannotEvaluateCount": counts[VERDICT_CANNOT_EVALUATE],
            "rejectedCount": counts[VERDICT_REJECTED],
            **REQUIRED_BLOCKED_DECISION,
            "reason": "This validator only checks synthetic future NHATS registration evidence packet shapes. It does not attach real registration proof, close registration gates, authorize download, create extraction scripts, store raw data, calibrate a model or support individual use.",
        },
        "caseResults": case_results,
        "hardBoundaries": [
            "Validator pass does not prove NHATS registration, data access, workspace execution or model readiness.",
            "A reviewable registration packet remains blocked until external controlled evidence, human review and second-reviewer signoff are available outside this repository.",
            "No output from this validator can authorize download, extraction, raw-data storage, public AI upload, calibration, validation or individual prediction.",
        ],
        "failures": failures,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--test-cases", type=Path, default=DEFAULT_TEST_CASES)
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument("--packet", type=Path, help="Optional single packet JSON to evaluate.")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        template = load_json(args.template.resolve(), "registration evidence template")
        if args.packet:
            packet = load_json(args.packet.resolve(), "registration evidence packet")
            validation = {
                "schemaVersion": VALIDATION_SCHEMA,
                "generatedAt": datetime.now(timezone.utc).isoformat(),
                "status": "single-packet-evaluated-registration-still-blocked",
                "currentDecision": {"validatorReady": True, **REQUIRED_BLOCKED_DECISION},
                "packetResult": evaluate_packet(packet, template),
            }
        else:
            test_cases = load_json(args.test_cases.resolve(), "registration evidence packet validator test cases")
            validation = validate_test_cases(test_cases, template)
        write_json(args.out.resolve(), validation)
        if validation["status"] == "fail":
            for failure in validation.get("failures", []):
                print(f"ERROR: {failure}", file=sys.stderr)
            return 1
        decision = validation["currentDecision"]
        print(
            "NHATS registration evidence packet validator ok: "
            f"cases={decision.get('testCaseCount', 1)} "
            f"reviewable={decision.get('reviewableButStillBlockedCount', 0)} "
            f"cannot_evaluate={decision.get('cannotEvaluateCount', 0)} "
            f"rejected={decision.get('rejectedCount', 0)} registration=blocked"
        )
        return 0
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
