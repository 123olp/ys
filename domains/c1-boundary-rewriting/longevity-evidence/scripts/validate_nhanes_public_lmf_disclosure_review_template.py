#!/usr/bin/env python3
"""Validate the NHANES public-use LMF disclosure review template."""

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
    / "life_path_nhanes_public_lmf_disclosure_review_template.json"
)
DEFAULT_OUT = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhanes-public-lmf-disclosure-review-template-validation.json"
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
REQUIRED_FORBIDDEN_FIELDS = {
    "SEQN",
    "recordCount",
    "deathCount",
    "unweightedCount",
    "weightedCount",
    "weightedSum",
    "weightedRate",
    "mortalityRate",
    "ciLower",
    "ciUpper",
    "standardError",
    "relativeStandardError",
    "individualRiskScore",
    "deathDate",
    "rawRows",
    "publicAiPrompt",
    "publicAiResponse",
}
REQUIRED_SOURCE_TRACE = {
    "https://wwwn.cdc.gov/nchs/nhanes/tutorials/varianceestimation.aspx",
    "https://wwwn.cdc.gov/nchs/nhanes/tutorials/reliabilityofestimates.aspx",
    "https://www.cdc.gov/nchs/data/series/sr_02/sr02_175.pdf",
    "https://www.cdc.gov/nchs/data/series/sr_02/sr02-200.pdf",
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

    for field in (
        "disclosureOutputEnvelopeValidationPath",
        "effectiveSampleCiPublicationValidationPath",
        "weightedOutputImplementationPreflightValidationPath",
        "weightedDomainOutputReadinessPath",
    ):
        value = prerequisites.get(field)
        if not isinstance(value, str) or not value:
            fail(errors, f"reviewPrerequisites.{field} must be set")
            continue
        path = REPO_ROOT / value
        if not path.exists():
            fail(errors, f"reviewPrerequisites.{field} path does not exist: {value}")


def validate_slots(template: dict[str, Any], errors: list[str]) -> tuple[int, int]:
    slots = template.get("requiredReviewSlots")
    if not isinstance(slots, list):
        fail(errors, "requiredReviewSlots must be a list")
        return 0, 0

    observed: set[str] = set()
    pending = 0
    for index, slot in enumerate(slots):
        if not isinstance(slot, dict):
            fail(errors, f"requiredReviewSlots[{index}] must be an object")
            continue
        slot_id = slot.get("slotId")
        if isinstance(slot_id, str):
            observed.add(slot_id)
        else:
            fail(errors, f"requiredReviewSlots[{index}].slotId must be a string")
        if slot.get("status") == "pending":
            pending += 1
        else:
            fail(errors, f"slot {slot_id} must remain pending until a real disclosure review is completed")
        if slot.get("requiredForCompletion") is not True:
            fail(errors, f"slot {slot_id} must be requiredForCompletion")
        if not str(slot.get("expectedEvidence", "")).strip():
            fail(errors, f"slot {slot_id} must include expectedEvidence")

    missing = sorted(REQUIRED_SLOT_IDS - observed)
    extra = sorted(observed - REQUIRED_SLOT_IDS)
    if missing:
        fail(errors, f"missing required review slots: {missing}")
    if extra:
        fail(errors, f"unexpected review slots: {extra}")
    return len(observed), pending


def validate_template(template: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if template.get("schemaVersion") != "human-infra.nhanes-public-lmf-disclosure-review-template.v1":
        fail(errors, "schemaVersion mismatch")
    if template.get("templateId") != "nhanes-public-lmf-2017-2018-disclosure-review-template":
        fail(errors, "templateId mismatch")
    if template.get("status") != "template-ready-review-not-complete-no-real-output":
        fail(errors, "status mismatch")
    if template.get("sourceId") != "nhanes-public-lmf-2017-2018":
        fail(errors, "sourceId must be nhanes-public-lmf-2017-2018")
    if template.get("reviewType") != "real-public-weighted-domain-output-disclosure-review-template":
        fail(errors, "reviewType mismatch")

    decision = template.get("currentDecision")
    if not isinstance(decision, dict):
        fail(errors, "currentDecision must be an object")
    else:
        require_bool(decision, "templateValidationAllowed", True, errors, "currentDecision")
        for key in (
            "publicDisclosureReviewComplete",
            "realWeightedOutputReviewed",
            "realWeightedOutputReleased",
            "publicWeightedDomainOutputAllowed",
            "realDesignBasedIntervalsAllowed",
            "rowLevelExportAllowed",
            "identifierExportAllowed",
            "publicAiUploadAllowed",
            "calibrationAllowed",
            "individualPredictionAllowed",
        ):
            require_bool(decision, key, False, errors, "currentDecision")

    validate_prerequisites(template, errors)
    slot_count, pending_count = validate_slots(template, errors)

    rules = template.get("reviewRules")
    if not isinstance(rules, dict):
        fail(errors, "reviewRules must be an object")
        rules = {}
    for key in (
        "aggregateOnly",
        "reviewTemplateOnly",
        "requiresOutputArtifactHash",
        "requiresSecondReviewer",
        "requiresSuppressionReview",
        "requiresEffectiveSampleCiReview",
        "requiresDofSparseDomainReview",
        "requiresForbiddenFieldScan",
        "requiresRetentionPlan",
    ):
        require_bool(rules, key, True, errors, "reviewRules")
    for key in (
        "publicReleaseAllowedWithoutCompletedReview",
        "realWeightedValuesAllowedInTemplate",
        "rowLevelDataAllowedInTemplate",
        "identifierAllowedInTemplate",
        "publicAiUploadAllowed",
    ):
        require_bool(rules, key, False, errors, "reviewRules")

    forbidden = as_set(template.get("forbiddenPersistedFields"))
    missing_forbidden = sorted(REQUIRED_FORBIDDEN_FIELDS - forbidden)
    if missing_forbidden:
        fail(errors, f"forbiddenPersistedFields missing values: {missing_forbidden}")

    allowed_template_fields = as_set(template.get("allowedTemplateFields"))
    observed_top_level = set(template)
    extra_top_level = sorted(observed_top_level - allowed_template_fields)
    if extra_top_level:
        fail(errors, f"top-level fields outside allowedTemplateFields: {extra_top_level}")
    prohibited_key_hits = sorted(collect_keys(template) & REQUIRED_FORBIDDEN_FIELDS)
    # These names are allowed only inside the explicit forbiddenPersistedFields list.
    allowed_hits = collect_keys({"forbiddenPersistedFields": template.get("forbiddenPersistedFields", [])})
    unexpected_hits = sorted(set(prohibited_key_hits) - allowed_hits)
    if unexpected_hits:
        fail(errors, f"forbidden persisted field names appear outside the forbidden list: {unexpected_hits}")

    criteria = template.get("reviewCompletionCriteria")
    if not isinstance(criteria, dict):
        fail(errors, "reviewCompletionCriteria must be an object")
        criteria = {}
    expected_criteria = {
        "requiredSlotCount": len(REQUIRED_SLOT_IDS),
        "requiredCompletedSlotCount": len(REQUIRED_SLOT_IDS),
        "requiresAllSlotsComplete": True,
        "requiresSecondReviewer": True,
        "requiresNoForbiddenPersistedFields": True,
        "requiresNoUnsuppressedSmallCells": True,
        "requiresNoLowDofUnsuppressedCells": True,
        "requiresNoRowLevelData": True,
        "requiresNoPublicAiUpload": True,
        "requiresReviewedOutputHash": True,
        "requiresExplicitReleaseDecision": True,
        "currentCompletedSlotCount": 0,
        "publicDisclosureReviewComplete": False,
    }
    for key, expected in expected_criteria.items():
        if criteria.get(key) != expected:
            fail(errors, f"reviewCompletionCriteria.{key} mismatch")
    if slot_count != len(REQUIRED_SLOT_IDS) or pending_count != len(REQUIRED_SLOT_IDS):
        fail(errors, "required review slot count or pending count mismatch")

    source_trace = as_set(template.get("sourceTrace"))
    missing_sources = sorted(REQUIRED_SOURCE_TRACE - source_trace)
    if missing_sources:
        fail(errors, f"sourceTrace missing required official sources: {missing_sources}")

    boundary = template.get("nonProofBoundary")
    if not isinstance(boundary, dict):
        fail(errors, "nonProofBoundary must be an object")
    else:
        confirms = " ".join(str(item) for item in boundary.get("confirms", []))
        does_not_confirm = " ".join(str(item) for item in boundary.get("doesNotConfirm", []))
        for token in ("template", "review slots", "no real weighted-domain output values"):
            if token not in confirms:
                fail(errors, f"nonProofBoundary.confirms missing token: {token}")
        for token in ("real public disclosure review completion", "calibration", "individual prediction"):
            if token not in does_not_confirm:
                fail(errors, f"nonProofBoundary.doesNotConfirm missing token: {token}")

    return errors


def build_validation(template_path: Path, output_path: Path, template: dict[str, Any], errors: list[str]) -> dict[str, Any]:
    slots = template.get("requiredReviewSlots", [])
    pending_count = sum(1 for slot in slots if isinstance(slot, dict) and slot.get("status") == "pending")
    return {
        "schemaVersion": "human-infra.nhanes-public-lmf-disclosure-review-template-validation.v1",
        "overallStatus": "PASS" if not errors else "FAIL",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "templatePath": repo_rel(template_path),
        "templateSha256": sha256_file(template_path),
        "validationPath": repo_rel(output_path),
        "summary": {
            "sourceId": template.get("sourceId"),
            "requiredSlotCount": len(REQUIRED_SLOT_IDS),
            "pendingSlotCount": pending_count,
            "publicDisclosureReviewComplete": template.get("currentDecision", {}).get(
                "publicDisclosureReviewComplete"
            ),
            "publicWeightedDomainOutputAllowed": template.get("currentDecision", {}).get(
                "publicWeightedDomainOutputAllowed"
            ),
            "templateReviewOnly": template.get("reviewRules", {}).get("reviewTemplateOnly"),
            "forbiddenPersistedFieldCount": len(as_set(template.get("forbiddenPersistedFields"))),
        },
        "boundary": {
            "templateValidated": not errors,
            "containsRealNhanesOutput": False,
            "realWeightedOutputReviewed": False,
            "weightedDomainOutputImplemented": False,
            "publicWeightedDomainOutputAllowed": False,
            "calibrationAllowed": False,
            "individualPredictionAllowed": False,
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
    output_path.parent.mkdir(parents=True, exist_ok=True)
    validation = build_validation(template_path, output_path, template, errors)
    output_path.write_text(json.dumps(validation, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if errors:
        for error in errors:
            print(f"NHANES public LMF disclosure review template error: {error}")
        return 1
    print(
        "NHANES public LMF disclosure review template ok: "
        f"slots={validation['summary']['requiredSlotCount']} "
        "boundary=no-real-output"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
