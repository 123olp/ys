#!/usr/bin/env python3
"""Validate the NHANES public-use LMF disclosure review execution register."""

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
DEFAULT_REGISTER = MANUAL_DIR / "life_path_nhanes_public_lmf_disclosure_review_execution_register.json"
DEFAULT_TEMPLATE = MANUAL_DIR / "life_path_nhanes_public_lmf_disclosure_review_template.json"
DEFAULT_OUT = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhanes-public-lmf-disclosure-review-execution-validation.json"
)

REQUIRED_SLOT_IDS = {
    "output-artifact-identity",
    "source-and-cycle-binding",
    "survey-design-trace",
    "domain-and-dof-trace",
    "effective-sample-ci-trace",
    "disclosure-envelope-trace",
    "small-cell-suppression-review",
    "low-dof-suppression-review",
    "rse-ci-width-review",
    "forbidden-field-scan",
    "row-level-and-identifier-scan",
    "public-ai-and-third-party-upload-scan",
    "output-hash-and-retention-plan",
    "second-reviewer-signoff",
    "release-decision-record",
}
MACHINE_PREFILL_ALLOWED_SLOT_IDS = {
    "output-artifact-identity",
    "source-and-cycle-binding",
    "survey-design-trace",
    "domain-and-dof-trace",
    "forbidden-field-scan",
    "row-level-and-identifier-scan",
    "public-ai-and-third-party-upload-scan",
    "output-hash-and-retention-plan",
}
FORBIDDEN_TRACKED_KEYS = {
    "SEQN",
    "recordCount",
    "deathCount",
    "unweightedCount",
    "weightedCount",
    "weightedSum",
    "weightedRate",
    "weightedMortalityRate",
    "mortalityRate",
    "standardError",
    "relativeStandardError",
    "confidenceInterval95",
    "ciLower",
    "ciUpper",
    "individualRiskScore",
    "deathDate",
    "rawRows",
    "publicAiPrompt",
    "publicAiResponse",
}
REQUIRED_FALSE_DECISIONS = {
    "reviewedOutputArtifactHashPresent",
    "allRequiredSlotsCompleted",
    "secondReviewerSignoffPresent",
    "publicDisclosureReviewComplete",
    "realWeightedOutputReviewed",
    "realWeightedOutputReleased",
    "publicWeightedDomainOutputAllowed",
    "realDesignBasedIntervalsAllowed",
    "publicOutputImplementationAllowed",
    "calibrationAllowed",
    "individualPredictionAllowed",
    "medicalAdviceAllowed",
}
REQUIRED_TRUE_DECISIONS = {
    "executionRegisterValidated",
    "reviewTemplateValidated",
    "localPacketRunwayAvailable",
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


def validate_template_binding(register: dict[str, Any], template: dict[str, Any], errors: list[str]) -> None:
    upstream = register.get("upstreamTemplate")
    if not isinstance(upstream, dict):
        fail(errors, "upstreamTemplate must be an object")
        return
    if upstream.get("path") != (
        "domains/c1-boundary-rewriting/longevity-evidence/data/manual/"
        "life_path_nhanes_public_lmf_disclosure_review_template.json"
    ):
        fail(errors, "upstreamTemplate.path mismatch")
    if upstream.get("validationPath") != (
        "web/src/data/life-path-nhanes-public-lmf-disclosure-review-template-validation.json"
    ):
        fail(errors, "upstreamTemplate.validationPath mismatch")

    if template.get("schemaVersion") != "human-infra.nhanes-public-lmf-disclosure-review-template.v1":
        fail(errors, "upstream template schemaVersion mismatch")
    if template.get("status") != "template-ready-review-not-complete-no-real-output":
        fail(errors, "upstream template status mismatch")
    template_slots = template.get("requiredReviewSlots")
    if not isinstance(template_slots, list):
        fail(errors, "upstream template requiredReviewSlots must be a list")
        return
    template_slot_ids = {slot.get("slotId") for slot in template_slots if isinstance(slot, dict)}
    if template_slot_ids != REQUIRED_SLOT_IDS:
        fail(errors, "upstream template slot ids mismatch")
    if any(not isinstance(slot, dict) or slot.get("status") != "pending" for slot in template_slots):
        fail(errors, "upstream template slots must remain pending")


def validate_local_packet_runway(register: dict[str, Any], errors: list[str]) -> None:
    runway = register.get("localPacketRunway")
    if not isinstance(runway, dict):
        fail(errors, "localPacketRunway must be an object")
        return
    if runway.get("defaultIgnoredPacketPath") != (
        "build/reports/nhanes-public-lmf-local-disclosure-review-packet/validation.json"
    ):
        fail(errors, "localPacketRunway.defaultIgnoredPacketPath mismatch")
    if runway.get("makeTarget") != "nhanes-public-lmf-local-disclosure-review-packet-audit":
        fail(errors, "localPacketRunway.makeTarget mismatch")
    for key in (
        "packetRequiredForRealReview",
        "packetMayBindRealLocalOutputHash",
    ):
        require_bool(runway, key, True, errors, "localPacketRunway")
    for key in (
        "packetRequiredForDefaultCheck",
        "packetMayContainRealWeightedValues",
        "packetMayContainRealDesignBasedIntervals",
        "trackedPacketAllowed",
        "webPacketAllowed",
    ):
        require_bool(runway, key, False, errors, "localPacketRunway")


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
    if decision.get("releaseDecision") != "blocked-pending-human-disclosure-review":
        fail(errors, "currentDecision.releaseDecision mismatch")
    if "human disclosure review" not in str(decision.get("reason", "")):
        fail(errors, "currentDecision.reason must explain missing human disclosure review")


def validate_slots(register: dict[str, Any], errors: list[str]) -> dict[str, int]:
    slots = register.get("reviewSlotExecution")
    summary = {
        "slotCount": 0,
        "machinePrefillAllowedSlotCount": 0,
        "humanReviewedSlotCount": 0,
        "completedSlotCount": 0,
    }
    if not isinstance(slots, list):
        fail(errors, "reviewSlotExecution must be a list")
        return summary

    observed: set[str] = set()
    for index, slot in enumerate(slots):
        if not isinstance(slot, dict):
            fail(errors, f"reviewSlotExecution[{index}] must be an object")
            continue
        slot_id = slot.get("slotId")
        if isinstance(slot_id, str):
            observed.add(slot_id)
        else:
            fail(errors, f"reviewSlotExecution[{index}].slotId must be a string")
            continue
        if slot.get("templateStatus") != "defined":
            fail(errors, f"slot {slot_id} templateStatus must be defined")
        if slot.get("blocksRelease") is not True:
            fail(errors, f"slot {slot_id} must block release")
        if slot.get("reviewEvidenceRef") is not None:
            fail(errors, f"slot {slot_id} must not carry review evidence before human review")
        if slot.get("reviewerSignoff") is not None:
            fail(errors, f"slot {slot_id} must not carry reviewerSignoff before human review")

        status = slot.get("executionStatus")
        if slot_id in MACHINE_PREFILL_ALLOWED_SLOT_IDS:
            if status != "machine-prefill-allowed-pending-human-review":
                fail(errors, f"slot {slot_id} must be machine-prefill-allowed-pending-human-review")
            summary["machinePrefillAllowedSlotCount"] += 1
        elif status != "pending-human-review":
            fail(errors, f"slot {slot_id} must be pending-human-review")
        if status in {"human-reviewed", "complete", "release-approved"}:
            summary["humanReviewedSlotCount"] += 1
            summary["completedSlotCount"] += 1

    missing = sorted(REQUIRED_SLOT_IDS - observed)
    extra = sorted(observed - REQUIRED_SLOT_IDS)
    if missing:
        fail(errors, f"missing review slots: {missing}")
    if extra:
        fail(errors, f"unexpected review slots: {extra}")
    summary["slotCount"] = len(observed)
    return summary


def validate_completion(register: dict[str, Any], slot_summary: dict[str, int], errors: list[str]) -> None:
    completion = register.get("completionState")
    if not isinstance(completion, dict):
        fail(errors, "completionState must be an object")
        return
    expected = {
        "requiredSlotCount": len(REQUIRED_SLOT_IDS),
        "machinePrefillAllowedSlotCount": len(MACHINE_PREFILL_ALLOWED_SLOT_IDS),
        "humanReviewedSlotCount": 0,
        "completedSlotCount": 0,
        "pendingHumanReviewSlotCount": len(REQUIRED_SLOT_IDS),
        "reviewedOutputArtifactHash": None,
        "secondReviewerSignoffPresent": False,
        "releaseDecision": "blocked-pending-human-disclosure-review",
        "publicDisclosureReviewComplete": False,
        "publicWeightedDomainOutputAllowed": False,
        "calibrationAllowed": False,
        "individualPredictionAllowed": False,
    }
    for key, expected_value in expected.items():
        if completion.get(key) != expected_value:
            fail(errors, f"completionState.{key} mismatch")
    if slot_summary["slotCount"] != len(REQUIRED_SLOT_IDS):
        fail(errors, "completionState cannot match because slot count is wrong")
    if slot_summary["machinePrefillAllowedSlotCount"] != len(MACHINE_PREFILL_ALLOWED_SLOT_IDS):
        fail(errors, "completionState cannot match because machine-prefill slot count is wrong")


def validate_state_machine(register: dict[str, Any], errors: list[str]) -> None:
    machine = register.get("releaseStateMachine")
    if not isinstance(machine, dict):
        fail(errors, "releaseStateMachine must be an object")
        return
    if machine.get("currentState") != "blocked-pending-human-disclosure-review":
        fail(errors, "releaseStateMachine.currentState mismatch")
    next_states = set(machine.get("allowedNextStates", []))
    if next_states != {"packet-attached-pending-human-review", "cannot-evaluate"}:
        fail(errors, "releaseStateMachine.allowedNextStates mismatch")
    forbidden = set(machine.get("forbiddenDirectTransitions", []))
    for state in (
        "release-approved",
        "public-weighted-output-implemented",
        "calibration-enabled",
        "individual-prediction-enabled",
    ):
        if state not in forbidden:
            fail(errors, f"releaseStateMachine.forbiddenDirectTransitions missing {state}")
    path_text = " ".join(str(item) for item in machine.get("minimumReleasePath", []))
    for token in ("human-reviewed", "second-reviewer", "release-decision", "implementation"):
        if token not in path_text:
            fail(errors, f"releaseStateMachine.minimumReleasePath missing {token}")


def validate_forbidden_keys(register: dict[str, Any], errors: list[str]) -> None:
    forbidden_list = register.get("forbiddenTrackedFields")
    if not isinstance(forbidden_list, list):
        fail(errors, "forbiddenTrackedFields must be a list")
        return
    forbidden_set = {str(item) for item in forbidden_list}
    missing = sorted(FORBIDDEN_TRACKED_KEYS - forbidden_set)
    if missing:
        fail(errors, f"forbiddenTrackedFields missing values: {missing}")

    key_hits = sorted(collect_keys(register) & FORBIDDEN_TRACKED_KEYS)
    allowed_hits = collect_keys({"forbiddenTrackedFields": forbidden_list})
    unexpected = sorted(set(key_hits) - allowed_hits)
    if unexpected:
        fail(errors, f"forbidden tracked field names appear outside forbiddenTrackedFields: {unexpected}")


def validate_boundary(register: dict[str, Any], errors: list[str]) -> None:
    boundary = register.get("nonProofBoundary")
    if not isinstance(boundary, dict):
        fail(errors, "nonProofBoundary must be an object")
        return
    confirms = " ".join(str(item) for item in boundary.get("confirms", []))
    does_not = " ".join(str(item) for item in boundary.get("doesNotConfirm", []))
    for token in ("machine-auditable", "review slots", "public weighted-domain output remains blocked"):
        if token not in confirms:
            fail(errors, f"nonProofBoundary.confirms missing token: {token}")
    for token in ("public disclosure review completion", "calibration", "individual prediction"):
        if token not in does_not:
            fail(errors, f"nonProofBoundary.doesNotConfirm missing token: {token}")


def validate_register(register: dict[str, Any], template: dict[str, Any]) -> tuple[list[str], dict[str, int]]:
    errors: list[str] = []
    if register.get("schemaVersion") != (
        "human-infra.nhanes-public-lmf-disclosure-review-execution-register.v1"
    ):
        fail(errors, "schemaVersion mismatch")
    if register.get("registerId") != "nhanes-public-lmf-2017-2018-disclosure-review-execution-register":
        fail(errors, "registerId mismatch")
    if register.get("status") != "execution-register-ready-public-review-not-complete-release-blocked":
        fail(errors, "status mismatch")
    if register.get("sourceId") != "nhanes-public-lmf-2017-2018":
        fail(errors, "sourceId mismatch")
    if register.get("reviewType") != "real-public-weighted-domain-output-disclosure-review-execution":
        fail(errors, "reviewType mismatch")
    if register.get("reviewer") != "tradecatlabs":
        fail(errors, "reviewer mismatch")

    validate_template_binding(register, template, errors)
    validate_local_packet_runway(register, errors)
    validate_decision(register, errors)
    slot_summary = validate_slots(register, errors)
    validate_completion(register, slot_summary, errors)
    validate_state_machine(register, errors)
    validate_forbidden_keys(register, errors)
    validate_boundary(register, errors)
    return errors, slot_summary


def build_validation(
    register_path: Path,
    template_path: Path,
    output_path: Path,
    register: dict[str, Any],
    template: dict[str, Any],
    errors: list[str],
    slot_summary: dict[str, int],
) -> dict[str, Any]:
    completion = register.get("completionState", {})
    return {
        "schemaVersion": "human-infra.nhanes-public-lmf-disclosure-review-execution-validation.v1",
        "status": "pass" if not errors else "fail",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "registerPath": repo_rel(register_path),
        "registerSha256": sha256_file(register_path),
        "templatePath": repo_rel(template_path),
        "templateSha256": sha256_file(template_path),
        "validationPath": repo_rel(output_path),
        "summary": {
            "sourceId": register.get("sourceId"),
            "requiredSlotCount": len(REQUIRED_SLOT_IDS),
            "observedSlotCount": slot_summary["slotCount"],
            "machinePrefillAllowedSlotCount": slot_summary["machinePrefillAllowedSlotCount"],
            "humanReviewedSlotCount": completion.get("humanReviewedSlotCount"),
            "completedSlotCount": completion.get("completedSlotCount"),
            "pendingHumanReviewSlotCount": completion.get("pendingHumanReviewSlotCount"),
            "reviewedOutputArtifactHashPresent": completion.get("reviewedOutputArtifactHash") is not None,
            "secondReviewerSignoffPresent": completion.get("secondReviewerSignoffPresent"),
            "releaseDecision": completion.get("releaseDecision"),
            "publicDisclosureReviewComplete": completion.get("publicDisclosureReviewComplete"),
            "publicWeightedDomainOutputAllowed": completion.get("publicWeightedDomainOutputAllowed"),
            "templateSlotCount": len(template.get("requiredReviewSlots", [])),
        },
        "boundary": {
            "executionRegisterValidated": not errors,
            "containsRealWeightedValues": False,
            "containsRealDesignBasedIntervals": False,
            "containsRowLevelData": False,
            "publicDisclosureReviewComplete": False,
            "publicWeightedDomainOutputAllowed": False,
            "publicOutputImplementationAllowed": False,
            "calibrationAllowed": False,
            "individualPredictionAllowed": False,
        },
        "errors": errors,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--register", type=Path, default=DEFAULT_REGISTER)
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    register_path = args.register.resolve()
    template_path = args.template.resolve()
    output_path = args.out.resolve()
    register = load_json(register_path)
    template = load_json(template_path)
    errors, slot_summary = validate_register(register, template)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    validation = build_validation(register_path, template_path, output_path, register, template, errors, slot_summary)
    output_path.write_text(json.dumps(validation, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if errors:
        for error in errors:
            print(f"NHANES public LMF disclosure review execution error: {error}")
        return 1
    print(
        "NHANES public LMF disclosure review execution ok: "
        f"slots={validation['summary']['requiredSlotCount']} "
        f"completed={validation['summary']['completedSlotCount']} "
        "boundary=release-blocked"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
