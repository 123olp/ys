#!/usr/bin/env python3
"""Validate the NHANES public-use LMF public output implementation review execution register.

This gate records implementation-review execution state only. It does not read
ignored local weighted outputs, approve publication, or expose rates, intervals,
row counts, identifiers, calibration inputs, or individual predictions.
"""

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
DEFAULT_REGISTER = (
    MANUAL_DIR / "life_path_nhanes_public_lmf_public_output_implementation_review_execution_register.json"
)
DEFAULT_TEMPLATE = (
    MANUAL_DIR / "life_path_nhanes_public_lmf_public_output_implementation_review_template.json"
)
DEFAULT_TEMPLATE_VALIDATION = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhanes-public-lmf-public-output-implementation-review-template-validation.json"
)
DEFAULT_OUT = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhanes-public-lmf-public-output-implementation-review-execution-validation.json"
)

REQUIRED_SLOT_IDS = {
    "reviewed-artifact-binding",
    "redacted-summary-binding",
    "front-end-json-source-binding",
    "no-real-values-scan-binding",
    "static-build-artifact-review",
    "page-rendering-boundary-review",
    "cache-and-cdn-invalidation-plan",
    "rollback-and-removal-plan",
    "accessibility-and-labeling-review",
    "user-facing-boundary-copy-review",
    "second-reviewer-implementation-signoff",
    "final-public-implementation-decision",
}

FORBIDDEN_PUBLIC_KEYS = {
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

REQUIRED_FALSE_DECISIONS = {
    "reviewedOutputArtifactHashPresent",
    "frontEndArtifactReviewed",
    "allRequiredSlotsCompleted",
    "secondReviewerSignoffPresent",
    "finalImplementationDecisionPresent",
    "implementationReviewComplete",
    "publicOutputImplementationAllowed",
    "publicWeightedDomainOutputAllowed",
    "realWeightedOutputImplemented",
    "realWeightedOutputReviewed",
    "realWeightedOutputReleased",
    "calibrationAllowed",
    "individualPredictionAllowed",
    "medicalAdviceAllowed",
}
REQUIRED_TRUE_DECISIONS = {
    "executionRegisterValidated",
    "reviewTemplateValidated",
}


def load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
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
        for key, nested in value.items():
            keys.add(str(key))
            keys.update(collect_keys(nested))
    elif isinstance(value, list):
        for item in value:
            keys.update(collect_keys(item))
    return keys


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def require_bool(data: dict[str, Any], key: str, expected: bool, errors: list[str], prefix: str) -> None:
    if data.get(key) is not expected:
        fail(errors, f"{prefix}.{key} must be {expected}")


def validate_template_binding(
    register: dict[str, Any],
    template: dict[str, Any],
    template_validation: dict[str, Any],
    errors: list[str],
) -> None:
    upstream = register.get("upstreamTemplate")
    if not isinstance(upstream, dict):
        fail(errors, "upstreamTemplate must be an object")
        return
    if upstream.get("path") != (
        "domains/c1-boundary-rewriting/longevity-evidence/data/manual/"
        "life_path_nhanes_public_lmf_public_output_implementation_review_template.json"
    ):
        fail(errors, "upstreamTemplate.path mismatch")
    if upstream.get("validationPath") != (
        "web/src/data/life-path-nhanes-public-lmf-public-output-implementation-review-template-validation.json"
    ):
        fail(errors, "upstreamTemplate.validationPath mismatch")

    if template.get("schemaVersion") != (
        "human-infra.nhanes-public-lmf-public-output-implementation-review-template.v1"
    ):
        fail(errors, "upstream template schemaVersion mismatch")
    if template.get("status") != "template-ready-review-not-complete-no-public-output":
        fail(errors, "upstream template status mismatch")
    template_slots = template.get("requiredImplementationReviewSlots")
    if not isinstance(template_slots, list):
        fail(errors, "upstream template requiredImplementationReviewSlots must be a list")
        return
    template_slot_ids = {slot.get("slotId") for slot in template_slots if isinstance(slot, dict)}
    if template_slot_ids != REQUIRED_SLOT_IDS:
        fail(errors, "upstream template slot ids mismatch")
    if any(not isinstance(slot, dict) or slot.get("status") != "pending" for slot in template_slots):
        fail(errors, "upstream template slots must remain pending")

    if template_validation.get("status") != "PASS":
        fail(errors, "template validation status must be PASS")
    summary = template_validation.get("summary")
    if not isinstance(summary, dict):
        fail(errors, "template validation summary must be an object")
        return
    if summary.get("reviewSlotTotal") != len(REQUIRED_SLOT_IDS):
        fail(errors, "template validation reviewSlotTotal mismatch")
    if summary.get("pendingReviewSlotTotal") != len(REQUIRED_SLOT_IDS):
        fail(errors, "template validation pendingReviewSlotTotal mismatch")
    if summary.get("completedReviewSlotTotal") != 0:
        fail(errors, "template validation completedReviewSlotTotal must be 0")


def validate_decision(register: dict[str, Any], errors: list[str]) -> None:
    decision = register.get("currentDecision")
    if not isinstance(decision, dict):
        fail(errors, "currentDecision must be an object")
        return
    for key in REQUIRED_TRUE_DECISIONS:
        require_bool(decision, key, True, errors, "currentDecision")
    for key in REQUIRED_FALSE_DECISIONS:
        require_bool(decision, key, False, errors, "currentDecision")
    if decision.get("humanReviewedSlotCount") != 0:
        fail(errors, "currentDecision.humanReviewedSlotCount must be 0")
    if decision.get("releaseDecision") != "blocked-pending-public-output-implementation-review":
        fail(errors, "currentDecision.releaseDecision mismatch")
    if "implementation review" not in str(decision.get("reason", "")):
        fail(errors, "currentDecision.reason must explain missing implementation review")


def validate_slots(register: dict[str, Any], errors: list[str]) -> dict[str, int]:
    slots = register.get("implementationReviewSlotExecution")
    summary = {
        "slotCount": 0,
        "machinePrefillAllowedSlotCount": 0,
        "humanReviewedSlotCount": 0,
        "completedSlotCount": 0,
    }
    if not isinstance(slots, list):
        fail(errors, "implementationReviewSlotExecution must be a list")
        return summary

    observed: set[str] = set()
    for index, slot in enumerate(slots):
        if not isinstance(slot, dict):
            fail(errors, f"implementationReviewSlotExecution[{index}] must be an object")
            continue
        slot_id = slot.get("slotId")
        if isinstance(slot_id, str):
            observed.add(slot_id)
        else:
            fail(errors, f"implementationReviewSlotExecution[{index}].slotId must be a string")
            continue
        if slot.get("templateStatus") != "defined":
            fail(errors, f"slot {slot_id} templateStatus must be defined")
        if slot.get("executionStatus") != "pending-human-review":
            fail(errors, f"slot {slot_id} executionStatus must be pending-human-review")
        if slot.get("machinePrefillAllowed") is not False:
            fail(errors, f"slot {slot_id} machinePrefillAllowed must be false")
        if slot.get("blocksRelease") is not True:
            fail(errors, f"slot {slot_id} must block release")
        if slot.get("reviewEvidenceRef") is not None:
            fail(errors, f"slot {slot_id} must not carry review evidence before human review")
        if slot.get("reviewerSignoff") is not None:
            fail(errors, f"slot {slot_id} must not carry reviewer signoff before human review")
        if slot.get("completedAt") is not None:
            fail(errors, f"slot {slot_id} must not carry completedAt before human review")

    missing = sorted(REQUIRED_SLOT_IDS - observed)
    extra = sorted(observed - REQUIRED_SLOT_IDS)
    if missing:
        fail(errors, f"missing implementation review slots: {missing}")
    if extra:
        fail(errors, f"unexpected implementation review slots: {extra}")
    summary["slotCount"] = len(observed)
    return summary


def validate_completion(register: dict[str, Any], slot_summary: dict[str, int], errors: list[str]) -> None:
    completion = register.get("completionState")
    if not isinstance(completion, dict):
        fail(errors, "completionState must be an object")
        return
    expected = {
        "requiredSlotCount": len(REQUIRED_SLOT_IDS),
        "machinePrefillAllowedSlotCount": 0,
        "humanReviewedSlotCount": 0,
        "completedSlotCount": 0,
        "pendingHumanReviewSlotCount": len(REQUIRED_SLOT_IDS),
        "reviewedOutputArtifactHashPresent": False,
        "frontEndArtifactReviewed": False,
        "secondReviewerSignoffPresent": False,
        "finalImplementationDecisionPresent": False,
        "releaseDecision": "blocked-pending-public-output-implementation-review",
        "implementationReviewComplete": False,
        "publicOutputImplementationAllowed": False,
        "publicWeightedDomainOutputAllowed": False,
        "realWeightedOutputImplemented": False,
        "realWeightedOutputReviewed": False,
        "realWeightedOutputReleased": False,
        "calibrationAllowed": False,
        "individualPredictionAllowed": False,
        "medicalAdviceAllowed": False,
    }
    for key, expected_value in expected.items():
        if completion.get(key) != expected_value:
            fail(errors, f"completionState.{key} mismatch")
    if slot_summary["slotCount"] != len(REQUIRED_SLOT_IDS):
        fail(errors, "completionState cannot match because slot count is wrong")


def validate_state_machine(register: dict[str, Any], errors: list[str]) -> None:
    machine = register.get("releaseStateMachine")
    if not isinstance(machine, dict):
        fail(errors, "releaseStateMachine must be an object")
        return
    if machine.get("currentState") != "blocked-pending-public-output-implementation-review":
        fail(errors, "releaseStateMachine.currentState mismatch")
    if set(machine.get("allowedNextStates", [])) != {
        "artifact-attached-pending-implementation-review",
        "cannot-evaluate",
    }:
        fail(errors, "releaseStateMachine.allowedNextStates mismatch")
    forbidden = set(machine.get("forbiddenDirectTransitions", []))
    for state in (
        "public-implementation-approved",
        "public-weighted-output-implemented",
        "calibration-enabled",
        "individual-prediction-enabled",
    ):
        if state not in forbidden:
            fail(errors, f"releaseStateMachine.forbiddenDirectTransitions missing {state}")
    path_text = " ".join(str(item) for item in machine.get("minimumReleasePath", []))
    for token in ("human-disclosure", "artifact-hash", "human-reviewed", "second", "decision"):
        if token not in path_text:
            fail(errors, f"releaseStateMachine.minimumReleasePath missing {token}")


def validate_boundary(register: dict[str, Any], errors: list[str]) -> None:
    boundary = register.get("nonProofBoundary")
    if not isinstance(boundary, dict):
        fail(errors, "nonProofBoundary must be an object")
        return
    confirms = " ".join(str(item) for item in boundary.get("confirms", []))
    does_not = " ".join(str(item) for item in boundary.get("doesNotConfirm", []))
    for token in ("machine-auditable", "12 implementation review slots", "public weighted-domain output remains blocked"):
        if token not in confirms:
            fail(errors, f"nonProofBoundary.confirms missing token: {token}")
    for token in ("implementation review completion", "calibration", "individual prediction"):
        if token not in does_not:
            fail(errors, f"nonProofBoundary.doesNotConfirm missing token: {token}")


def validate_register(
    register: dict[str, Any],
    template: dict[str, Any],
    template_validation: dict[str, Any],
) -> tuple[list[str], dict[str, int]]:
    errors: list[str] = []
    if register.get("schemaVersion") != (
        "human-infra.nhanes-public-lmf-public-output-implementation-review-execution-register.v1"
    ):
        fail(errors, "schemaVersion mismatch")
    if register.get("registerId") != (
        "nhanes-public-lmf-2017-2018-public-output-implementation-review-execution-register"
    ):
        fail(errors, "registerId mismatch")
    if register.get("status") != "execution-register-ready-implementation-review-not-complete-release-blocked":
        fail(errors, "status mismatch")
    if register.get("sourceId") != "nhanes-public-lmf-2017-2018":
        fail(errors, "sourceId mismatch")
    if register.get("reviewType") != "public-output-implementation-review-execution":
        fail(errors, "reviewType mismatch")
    if register.get("reviewer") != "tradecatlabs":
        fail(errors, "reviewer mismatch")

    validate_template_binding(register, template, template_validation, errors)
    validate_decision(register, errors)
    slot_summary = validate_slots(register, errors)
    validate_completion(register, slot_summary, errors)
    validate_state_machine(register, errors)
    validate_boundary(register, errors)
    return errors, slot_summary


def build_validation(
    register_path: Path,
    template_path: Path,
    template_validation_path: Path,
    output_path: Path,
    register: dict[str, Any],
    errors: list[str],
    slot_summary: dict[str, int],
) -> dict[str, Any]:
    completion = register.get("completionState", {})
    return {
        "schemaVersion": (
            "human-infra.nhanes-public-lmf-public-output-implementation-review-execution-validation.v1"
        ),
        "status": "PASS" if not errors else "FAIL",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "registerPath": repo_rel(register_path),
        "registerSha256": sha256_file(register_path),
        "templatePath": repo_rel(template_path),
        "templateSha256": sha256_file(template_path),
        "templateValidationPath": repo_rel(template_validation_path),
        "templateValidationSha256": sha256_file(template_validation_path),
        "validationPath": repo_rel(output_path),
        "summary": {
            "sourceId": register.get("sourceId"),
            "reviewSlotTotal": len(REQUIRED_SLOT_IDS),
            "observedReviewSlotTotal": slot_summary["slotCount"],
            "pendingReviewSlotTotal": completion.get("pendingHumanReviewSlotCount"),
            "completedReviewSlotTotal": completion.get("completedSlotCount"),
            "humanReviewedSlotTotal": completion.get("humanReviewedSlotCount"),
            "machinePrefillAllowedSlotTotal": completion.get("machinePrefillAllowedSlotCount"),
            "reviewedOutputArtifactHashPresent": completion.get("reviewedOutputArtifactHashPresent"),
            "frontEndArtifactReviewed": completion.get("frontEndArtifactReviewed"),
            "secondReviewerSignoffPresent": completion.get("secondReviewerSignoffPresent"),
            "finalImplementationDecisionPresent": completion.get("finalImplementationDecisionPresent"),
            "releaseDecision": completion.get("releaseDecision"),
            "implementationReviewComplete": completion.get("implementationReviewComplete"),
            "publicOutputImplementationAllowed": completion.get("publicOutputImplementationAllowed"),
            "publicWeightedDomainOutputAllowed": completion.get("publicWeightedDomainOutputAllowed"),
            "realWeightedOutputImplemented": completion.get("realWeightedOutputImplemented"),
            "realWeightedOutputReviewed": completion.get("realWeightedOutputReviewed"),
            "realWeightedOutputReleased": completion.get("realWeightedOutputReleased"),
            "calibrationAllowed": completion.get("calibrationAllowed"),
            "individualPredictionAllowed": completion.get("individualPredictionAllowed"),
            "medicalAdviceAllowed": completion.get("medicalAdviceAllowed"),
        },
        "boundary": {
            "executionRegisterValidated": not errors,
            "containsRealNhanesOutput": False,
            "containsRowLevelData": False,
            "implementationReviewComplete": False,
            "publicOutputImplementationAllowed": False,
            "publicWeightedDomainOutputAllowed": False,
            "realWeightedOutputImplemented": False,
            "realWeightedOutputReviewed": False,
            "realWeightedOutputReleased": False,
            "calibrationAllowed": False,
            "individualPredictionAllowed": False,
            "medicalAdviceAllowed": False,
        },
        "errors": errors,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--register", type=Path, default=DEFAULT_REGISTER)
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument("--template-validation", type=Path, default=DEFAULT_TEMPLATE_VALIDATION)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    register_path = args.register.resolve()
    template_path = args.template.resolve()
    template_validation_path = args.template_validation.resolve()
    output_path = args.out.resolve()

    register = load_json(register_path)
    template = load_json(template_path)
    template_validation = load_json(template_validation_path)
    errors, slot_summary = validate_register(register, template, template_validation)

    validation = build_validation(
        register_path,
        template_path,
        template_validation_path,
        output_path,
        register,
        errors,
        slot_summary,
    )
    unexpected_output_keys = sorted(collect_keys(validation) & FORBIDDEN_PUBLIC_KEYS)
    if unexpected_output_keys:
        validation["errors"].append(
            f"validation output uses forbidden public value names as JSON keys: {unexpected_output_keys}"
        )
        validation["status"] = "FAIL"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(validation, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if validation["errors"]:
        for error in validation["errors"]:
            print(f"NHANES public LMF public output implementation review execution error: {error}")
        return 1
    print(
        "NHANES public LMF public output implementation review execution ok: "
        f"slots={validation['summary']['reviewSlotTotal']} "
        f"completed={validation['summary']['completedReviewSlotTotal']} "
        "boundary=release-blocked"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
