#!/usr/bin/env python3
"""Validate the NHANES public-use LMF public output implementation review template.

This is a template gate only. It does not read ignored local weighted outputs,
does not approve publication, and does not expose rates, intervals, row counts
or record-level data.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_TEMPLATE = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
    / "life_path_nhanes_public_lmf_public_output_implementation_review_template.json"
)
DEFAULT_OUT = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhanes-public-lmf-public-output-implementation-review-template-validation.json"
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

REQUIRED_PREREQUISITE_FIELDS = {
    "disclosureReviewExecutionValidationPath",
    "publicWebNoRealValuesValidationPath",
    "localRunEvidenceManifestValidationPath",
    "weightedDomainOutputReadinessValidationPath",
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


def as_set(value: Any) -> set[str]:
    if not isinstance(value, list):
        return set()
    return {str(item) for item in value}


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


def validate_prerequisites(template: dict[str, Any], errors: list[str]) -> None:
    prerequisites = template.get("reviewPrerequisites")
    if not isinstance(prerequisites, dict):
        fail(errors, "reviewPrerequisites must be an object")
        return

    observed = set(prerequisites)
    missing = sorted(REQUIRED_PREREQUISITE_FIELDS - observed)
    extra = sorted(observed - REQUIRED_PREREQUISITE_FIELDS)
    if missing:
        fail(errors, f"reviewPrerequisites missing fields: {missing}")
    if extra:
        fail(errors, f"reviewPrerequisites has unexpected fields: {extra}")

    for field in sorted(REQUIRED_PREREQUISITE_FIELDS):
        value = prerequisites.get(field)
        if not isinstance(value, str) or not value:
            fail(errors, f"reviewPrerequisites.{field} must be set")
            continue
        path = REPO_ROOT / value
        if not path.exists():
            fail(errors, f"reviewPrerequisites.{field} path does not exist: {value}")


def validate_slots(template: dict[str, Any], errors: list[str]) -> tuple[int, int, int]:
    slots = template.get("requiredImplementationReviewSlots")
    if not isinstance(slots, list):
        fail(errors, "requiredImplementationReviewSlots must be a list")
        return 0, 0, 0

    observed: set[str] = set()
    pending = 0
    completed = 0
    for index, slot in enumerate(slots):
        if not isinstance(slot, dict):
            fail(errors, f"requiredImplementationReviewSlots[{index}] must be an object")
            continue
        slot_id = slot.get("slotId")
        if isinstance(slot_id, str):
            observed.add(slot_id)
        else:
            fail(errors, f"requiredImplementationReviewSlots[{index}].slotId must be a string")
        status = slot.get("status")
        if status == "pending":
            pending += 1
        elif status == "complete":
            completed += 1
            fail(errors, f"slot {slot_id} must remain pending until real implementation review is completed")
        else:
            fail(errors, f"slot {slot_id} must have status pending")
        if slot.get("requiredForCompletion") is not True:
            fail(errors, f"slot {slot_id} must be requiredForCompletion")
        if not str(slot.get("expectedEvidence", "")).strip():
            fail(errors, f"slot {slot_id} must include expectedEvidence")

    missing = sorted(REQUIRED_SLOT_IDS - observed)
    extra = sorted(observed - REQUIRED_SLOT_IDS)
    if missing:
        fail(errors, f"missing required implementation review slots: {missing}")
    if extra:
        fail(errors, f"unexpected implementation review slots: {extra}")
    return len(observed), pending, completed


def validate_template(template: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if template.get("schemaVersion") != (
        "human-infra.nhanes-public-lmf-public-output-implementation-review-template.v1"
    ):
        fail(errors, "schemaVersion mismatch")
    if template.get("templateId") != (
        "nhanes-public-lmf-2017-2018-public-output-implementation-review-template"
    ):
        fail(errors, "templateId mismatch")
    if template.get("status") != "template-ready-review-not-complete-no-public-output":
        fail(errors, "status mismatch")
    if template.get("sourceId") != "nhanes-public-lmf-2017-2018":
        fail(errors, "sourceId must be nhanes-public-lmf-2017-2018")
    if template.get("reviewType") != "public-output-implementation-review-template":
        fail(errors, "reviewType mismatch")

    allowed_template_fields = as_set(template.get("allowedTemplateFields"))
    extra_top_level = sorted(set(template) - allowed_template_fields)
    if extra_top_level:
        fail(errors, f"top-level fields outside allowedTemplateFields: {extra_top_level}")

    unexpected_public_keys = sorted(collect_keys(template) & FORBIDDEN_PUBLIC_KEYS)
    if unexpected_public_keys:
        fail(errors, f"template uses forbidden public value names as JSON keys: {unexpected_public_keys}")

    decision = template.get("currentDecision")
    if not isinstance(decision, dict):
        fail(errors, "currentDecision must be an object")
    else:
        require_bool(decision, "templateValidationAllowed", True, errors, "currentDecision")
        for key in (
            "implementationReviewComplete",
            "approvedOutputArtifactBound",
            "reviewedOutputArtifactHashBound",
            "frontEndArtifactReviewed",
            "publicOutputImplementationAllowed",
            "publicWeightedDomainOutputAllowed",
            "realWeightedOutputImplemented",
            "realWeightedOutputReviewed",
            "realWeightedOutputReleased",
            "calibrationAllowed",
            "individualPredictionAllowed",
            "medicalAdviceAllowed",
        ):
            require_bool(decision, key, False, errors, "currentDecision")

    validate_prerequisites(template, errors)
    slot_count, pending_count, completed_count = validate_slots(template, errors)

    rules = template.get("implementationReviewRules")
    if not isinstance(rules, dict):
        fail(errors, "implementationReviewRules must be an object")
        rules = {}
    for key in (
        "reviewTemplateOnly",
        "requiresCompletedDisclosureReview",
        "requiresReviewedArtifactHash",
        "requiresFrontEndJsonSourceBinding",
        "requiresFreshNoRealValuesScan",
        "requiresStaticBuildReview",
        "requiresPageRenderingBoundaryReview",
        "requiresSecondReviewer",
        "requiresRollbackPlan",
    ):
        require_bool(rules, key, True, errors, "implementationReviewRules")
    for key in (
        "allowsPublicImplementationWithoutAllSlotsComplete",
        "allowsUnreviewedTrackedOutput",
        "allowsIgnoredLocalOutputRead",
        "allowsCalibrationInput",
        "allowsIndividualPrediction",
        "allowsMedicalAdvice",
    ):
        require_bool(rules, key, False, errors, "implementationReviewRules")

    criteria = template.get("implementationCompletionCriteria")
    if not isinstance(criteria, dict):
        fail(errors, "implementationCompletionCriteria must be an object")
        criteria = {}
    expected_criteria = {
        "requiredSlotTotal": len(REQUIRED_SLOT_IDS),
        "requiredCompletedSlotTotal": len(REQUIRED_SLOT_IDS),
        "currentCompletedSlotTotal": 0,
        "currentPendingSlotTotal": len(REQUIRED_SLOT_IDS),
        "requiresAllSlotsComplete": True,
        "requiresApprovedOutputArtifactHash": True,
        "requiresSecondReviewer": True,
        "requiresNoRealValuesScanPass": True,
        "requiresRollbackPlan": True,
        "implementationReviewComplete": False,
        "publicImplementationAllowed": False,
    }
    for key, expected in expected_criteria.items():
        if criteria.get(key) != expected:
            fail(errors, f"implementationCompletionCriteria.{key} mismatch")
    if slot_count != len(REQUIRED_SLOT_IDS):
        fail(errors, "required implementation review slot count mismatch")
    if pending_count != len(REQUIRED_SLOT_IDS) or completed_count != 0:
        fail(errors, "implementation review slots must all be pending")

    blocked_names = as_set(template.get("blockedPublishedValueNames"))
    missing_blocked_names = sorted(FORBIDDEN_PUBLIC_KEYS - blocked_names)
    if missing_blocked_names:
        fail(errors, f"blockedPublishedValueNames missing values: {missing_blocked_names}")

    source_trace = as_set(template.get("sourceTrace"))
    for value in template.get("reviewPrerequisites", {}).values() if isinstance(template.get("reviewPrerequisites"), dict) else []:
        if isinstance(value, str) and value not in source_trace:
            fail(errors, f"sourceTrace missing prerequisite path: {value}")

    boundary = template.get("nonProofBoundary")
    if not isinstance(boundary, dict):
        fail(errors, "nonProofBoundary must be an object")
    else:
        confirms = " ".join(str(item) for item in boundary.get("confirms", []))
        does_not_confirm = " ".join(str(item) for item in boundary.get("doesNotConfirm", []))
        for token in ("template", "12 required implementation review slots", "no real NHANES output values"):
            if token not in confirms:
                fail(errors, f"nonProofBoundary.confirms missing token: {token}")
        for token in ("reviewed public output artifact approval", "calibration", "individual prediction"):
            if token not in does_not_confirm:
                fail(errors, f"nonProofBoundary.doesNotConfirm missing token: {token}")

    return errors


def build_validation(template_path: Path, output_path: Path, template: dict[str, Any], errors: list[str]) -> dict[str, Any]:
    slots = template.get("requiredImplementationReviewSlots", [])
    pending_count = sum(1 for slot in slots if isinstance(slot, dict) and slot.get("status") == "pending")
    completed_count = sum(1 for slot in slots if isinstance(slot, dict) and slot.get("status") == "complete")
    return {
        "schemaVersion": (
            "human-infra.nhanes-public-lmf-public-output-implementation-review-template-validation.v1"
        ),
        "status": "PASS" if not errors else "FAIL",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "templatePath": repo_rel(template_path),
        "templateSha256": sha256_file(template_path),
        "validationPath": repo_rel(output_path),
        "summary": {
            "sourceId": template.get("sourceId"),
            "reviewSlotTotal": len(REQUIRED_SLOT_IDS),
            "pendingReviewSlotTotal": pending_count,
            "completedReviewSlotTotal": completed_count,
            "implementationReviewComplete": template.get("currentDecision", {}).get(
                "implementationReviewComplete"
            ),
            "publicOutputImplementationAllowed": template.get("currentDecision", {}).get(
                "publicOutputImplementationAllowed"
            ),
            "publicWeightedDomainOutputAllowed": template.get("currentDecision", {}).get(
                "publicWeightedDomainOutputAllowed"
            ),
            "realWeightedOutputImplemented": template.get("currentDecision", {}).get(
                "realWeightedOutputImplemented"
            ),
            "realWeightedOutputReviewed": template.get("currentDecision", {}).get(
                "realWeightedOutputReviewed"
            ),
            "realWeightedOutputReleased": template.get("currentDecision", {}).get(
                "realWeightedOutputReleased"
            ),
            "calibrationAllowed": template.get("currentDecision", {}).get("calibrationAllowed"),
            "individualPredictionAllowed": template.get("currentDecision", {}).get(
                "individualPredictionAllowed"
            ),
            "medicalAdviceAllowed": template.get("currentDecision", {}).get("medicalAdviceAllowed"),
            "blockedPublishedValueNameTotal": len(as_set(template.get("blockedPublishedValueNames"))),
        },
        "boundary": {
            "templateValidated": not errors,
            "containsRealNhanesOutput": False,
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
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    template_path = args.template.resolve()
    output_path = args.out.resolve()
    template = load_json(template_path)
    errors = validate_template(template)
    validation = build_validation(template_path, output_path, template, errors)
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
            print(f"NHANES public LMF public output implementation review template error: {error}")
        return 1
    print(
        "NHANES public LMF public output implementation review template ok: "
        f"slots={validation['summary']['reviewSlotTotal']} "
        "boundary=no-public-output"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
