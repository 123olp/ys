#!/usr/bin/env python3
"""Validate the NHANES public-use LMF public release gate.

This gate does not read ignored local weighted outputs and does not publish
rates, intervals, row counts, or record-level data. It only joins already
tracked validation artifacts into a machine-readable release decision.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[4]
WEB_DATA_DIR = REPO_ROOT / "web" / "src" / "data"

DEFAULT_DISCLOSURE_EXECUTION = (
    WEB_DATA_DIR / "life-path-nhanes-public-lmf-disclosure-review-execution-validation.json"
)
DEFAULT_NO_REAL_VALUES = (
    WEB_DATA_DIR / "life-path-nhanes-public-lmf-public-web-data-no-real-values-validation.json"
)
DEFAULT_LOCAL_MANIFEST = (
    WEB_DATA_DIR / "life-path-nhanes-public-lmf-local-run-evidence-manifest-validation.json"
)
DEFAULT_READINESS = (
    WEB_DATA_DIR / "life-path-nhanes-public-lmf-weighted-domain-output-readiness-validation.json"
)
DEFAULT_IMPLEMENTATION_REVIEW = (
    WEB_DATA_DIR
    / "life-path-nhanes-public-lmf-public-output-implementation-review-template-validation.json"
)
DEFAULT_IMPLEMENTATION_EXECUTION = (
    WEB_DATA_DIR
    / "life-path-nhanes-public-lmf-public-output-implementation-review-execution-validation.json"
)
DEFAULT_OUT = WEB_DATA_DIR / "life-path-nhanes-public-lmf-public-release-gate-validation.json"

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


def require_status(data: dict[str, Any], expected: str, path: str, errors: list[str]) -> None:
    observed = data.get("status")
    if not isinstance(observed, str) or observed.lower() != expected.lower():
        fail(errors, f"{path}.status must be {expected}")


def require_false(data: dict[str, Any], key: str, path: str, errors: list[str]) -> None:
    if data.get(key) is not False:
        fail(errors, f"{path}.{key} must be false")


def require_true(data: dict[str, Any], key: str, path: str, errors: list[str]) -> None:
    if data.get(key) is not True:
        fail(errors, f"{path}.{key} must be true")


def validate_disclosure_execution(data: dict[str, Any], errors: list[str]) -> None:
    require_status(data, "pass", "disclosureExecution", errors)
    summary = data.get("summary")
    boundary = data.get("boundary")
    if not isinstance(summary, dict):
        fail(errors, "disclosureExecution.summary must be an object")
        return
    if not isinstance(boundary, dict):
        fail(errors, "disclosureExecution.boundary must be an object")
        return
    if summary.get("requiredSlotCount") != 15:
        fail(errors, "disclosureExecution.summary.requiredSlotCount must be 15")
    if summary.get("completedSlotCount") != 0:
        fail(errors, "disclosureExecution.summary.completedSlotCount must be 0")
    if summary.get("humanReviewedSlotCount") != 0:
        fail(errors, "disclosureExecution.summary.humanReviewedSlotCount must be 0")
    if summary.get("releaseDecision") != "blocked-pending-human-disclosure-review":
        fail(errors, "disclosureExecution.summary.releaseDecision mismatch")
    for key in (
        "publicDisclosureReviewComplete",
        "publicWeightedDomainOutputAllowed",
    ):
        require_false(summary, key, "disclosureExecution.summary", errors)
    for key in (
        "containsRealWeightedValues",
        "containsRealDesignBasedIntervals",
        "containsRowLevelData",
        "publicDisclosureReviewComplete",
        "publicWeightedDomainOutputAllowed",
        "publicOutputImplementationAllowed",
        "calibrationAllowed",
        "individualPredictionAllowed",
    ):
        require_false(boundary, key, "disclosureExecution.boundary", errors)
    if data.get("errors") not in ([], None):
        fail(errors, "disclosureExecution.errors must be empty")


def validate_no_real_values(data: dict[str, Any], errors: list[str]) -> None:
    require_status(data, "PASS", "noRealValues", errors)
    summary = data.get("summary")
    if not isinstance(summary, dict):
        fail(errors, "noRealValues.summary must be an object")
        return
    if summary.get("forbiddenKeyHitCount") != 0:
        fail(errors, "noRealValues.summary.forbiddenKeyHitCount must be 0")
    if summary.get("booleanBoundaryIssueCount") != 0:
        fail(errors, "noRealValues.summary.booleanBoundaryIssueCount must be 0")
    if summary.get("publicWebDataContainsRealWeightedValues") is not False:
        fail(errors, "noRealValues.summary.publicWebDataContainsRealWeightedValues must be false")
    if summary.get("publicWebDataContainsRowLevelValues") is not False:
        fail(errors, "noRealValues.summary.publicWebDataContainsRowLevelValues must be false")
    if data.get("errors") not in ([], None):
        fail(errors, "noRealValues.errors must be empty")


def validate_local_manifest(data: dict[str, Any], errors: list[str]) -> None:
    require_status(data, "PASS", "localRunEvidenceManifest", errors)
    summary = data.get("summary")
    if not isinstance(summary, dict):
        fail(errors, "localRunEvidenceManifest.summary must be an object")
        return
    if summary.get("cellCount") != 8:
        fail(errors, "localRunEvidenceManifest.summary.cellCount must be 8")
    require_true(summary, "trackedValuesOmitted", "localRunEvidenceManifest.summary", errors)
    require_false(summary, "publicWeightedDomainOutputAllowed", "localRunEvidenceManifest.summary", errors)
    if summary.get("humanReviewedSlotCount") != 0:
        fail(errors, "localRunEvidenceManifest.summary.humanReviewedSlotCount must be 0")
    if data.get("errors") not in ([], None):
        fail(errors, "localRunEvidenceManifest.errors must be empty")


def validate_readiness(data: dict[str, Any], errors: list[str]) -> None:
    require_status(data, "pass", "weightedDomainReadiness", errors)
    summary = data.get("summary")
    if not isinstance(summary, dict):
        fail(errors, "weightedDomainReadiness.summary must be an object")
        return
    if summary.get("readyGateCount") != 12:
        fail(errors, "weightedDomainReadiness.summary.readyGateCount must be 12")
    if summary.get("blockedGateCount") != 2:
        fail(errors, "weightedDomainReadiness.summary.blockedGateCount must be 2")
    for key in (
        "controlledRuntimeSmokePassed",
        "publicDataDomainIndicatorEvaluated",
        "publicDataDofSparseReviewComplete",
        "publicDisclosureReviewTemplateValidated",
        "publicDisclosureReviewExecutionRegistered",
        "localOnlyWeightedDomainOutputRunwayReady",
        "localDisclosureReviewPacketRunwayReady",
        "cleanCheckoutDefaultCheckIndependent",
    ):
        require_true(summary, key, "weightedDomainReadiness.summary", errors)
    require_false(summary, "publicDisclosureReviewComplete", "weightedDomainReadiness.summary", errors)
    require_false(summary, "weightedDomainOutputAllowed", "weightedDomainReadiness.summary", errors)
    if data.get("errors") not in ([], None):
        fail(errors, "weightedDomainReadiness.errors must be empty")


def validate_implementation_review(data: dict[str, Any], errors: list[str]) -> None:
    require_status(data, "PASS", "publicOutputImplementationReview", errors)
    summary = data.get("summary")
    boundary = data.get("boundary")
    if not isinstance(summary, dict):
        fail(errors, "publicOutputImplementationReview.summary must be an object")
        return
    if not isinstance(boundary, dict):
        fail(errors, "publicOutputImplementationReview.boundary must be an object")
        return
    if summary.get("reviewSlotTotal") != 12:
        fail(errors, "publicOutputImplementationReview.summary.reviewSlotTotal must be 12")
    if summary.get("pendingReviewSlotTotal") != 12:
        fail(errors, "publicOutputImplementationReview.summary.pendingReviewSlotTotal must be 12")
    if summary.get("completedReviewSlotTotal") != 0:
        fail(errors, "publicOutputImplementationReview.summary.completedReviewSlotTotal must be 0")
    for key in (
        "implementationReviewComplete",
        "publicOutputImplementationAllowed",
        "publicWeightedDomainOutputAllowed",
        "realWeightedOutputImplemented",
        "realWeightedOutputReviewed",
        "realWeightedOutputReleased",
        "calibrationAllowed",
        "individualPredictionAllowed",
        "medicalAdviceAllowed",
    ):
        require_false(summary, key, "publicOutputImplementationReview.summary", errors)
        require_false(boundary, key, "publicOutputImplementationReview.boundary", errors)
    require_true(boundary, "templateValidated", "publicOutputImplementationReview.boundary", errors)
    require_false(boundary, "containsRealNhanesOutput", "publicOutputImplementationReview.boundary", errors)
    if data.get("errors") not in ([], None):
        fail(errors, "publicOutputImplementationReview.errors must be empty")


def validate_implementation_execution(data: dict[str, Any], errors: list[str]) -> None:
    require_status(data, "PASS", "publicOutputImplementationExecution", errors)
    summary = data.get("summary")
    boundary = data.get("boundary")
    if not isinstance(summary, dict):
        fail(errors, "publicOutputImplementationExecution.summary must be an object")
        return
    if not isinstance(boundary, dict):
        fail(errors, "publicOutputImplementationExecution.boundary must be an object")
        return
    if summary.get("reviewSlotTotal") != 12:
        fail(errors, "publicOutputImplementationExecution.summary.reviewSlotTotal must be 12")
    if summary.get("pendingReviewSlotTotal") != 12:
        fail(errors, "publicOutputImplementationExecution.summary.pendingReviewSlotTotal must be 12")
    if summary.get("completedReviewSlotTotal") != 0:
        fail(errors, "publicOutputImplementationExecution.summary.completedReviewSlotTotal must be 0")
    if summary.get("humanReviewedSlotTotal") != 0:
        fail(errors, "publicOutputImplementationExecution.summary.humanReviewedSlotTotal must be 0")
    if summary.get("machinePrefillAllowedSlotTotal") != 0:
        fail(errors, "publicOutputImplementationExecution.summary.machinePrefillAllowedSlotTotal must be 0")
    if summary.get("releaseDecision") != "blocked-pending-public-output-implementation-review":
        fail(errors, "publicOutputImplementationExecution.summary.releaseDecision mismatch")
    for key in (
        "reviewedOutputArtifactHashPresent",
        "frontEndArtifactReviewed",
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
    ):
        require_false(summary, key, "publicOutputImplementationExecution.summary", errors)
    require_true(boundary, "executionRegisterValidated", "publicOutputImplementationExecution.boundary", errors)
    for key in (
        "containsRealNhanesOutput",
        "containsRowLevelData",
        "implementationReviewComplete",
        "publicOutputImplementationAllowed",
        "publicWeightedDomainOutputAllowed",
        "realWeightedOutputImplemented",
        "realWeightedOutputReviewed",
        "realWeightedOutputReleased",
        "calibrationAllowed",
        "individualPredictionAllowed",
        "medicalAdviceAllowed",
    ):
        require_false(boundary, key, "publicOutputImplementationExecution.boundary", errors)
    if data.get("errors") not in ([], None):
        fail(errors, "publicOutputImplementationExecution.errors must be empty")


def validate_output_shape(output: dict[str, Any], errors: list[str]) -> None:
    unexpected_keys = sorted(collect_keys(output) & FORBIDDEN_PUBLIC_KEYS)
    if unexpected_keys:
        fail(errors, f"public release gate output contains forbidden keys: {unexpected_keys}")
    decision = output.get("currentDecision")
    if not isinstance(decision, dict):
        fail(errors, "currentDecision must be an object")
        return
    for key in (
        "publicReleaseAllowed",
        "publicWeightedDomainOutputAllowed",
        "realDesignBasedIntervalsAllowed",
        "publicOutputImplementationAllowed",
        "calibrationAllowed",
        "individualPredictionAllowed",
        "medicalAdviceAllowed",
    ):
        require_false(decision, key, "currentDecision", errors)


def build_input_record(path: Path, data: dict[str, Any], *, include_sha: bool = True) -> dict[str, Any]:
    record = {
        "path": repo_rel(path),
        "status": data.get("status"),
    }
    if include_sha:
        record["sha256"] = sha256_file(path)
    return record


def build_release_gate(
    disclosure_path: Path,
    disclosure: dict[str, Any],
    no_real_path: Path,
    no_real: dict[str, Any],
    local_manifest_path: Path,
    local_manifest: dict[str, Any],
    readiness_path: Path,
    readiness: dict[str, Any],
    implementation_review_path: Path,
    implementation_review: dict[str, Any],
    implementation_execution_path: Path,
    implementation_execution: dict[str, Any],
    output_path: Path,
    validation_errors: list[str],
) -> dict[str, Any]:
    release_blockers = [
        {
            "blockerId": "human-disclosure-review",
            "status": "missing",
            "required": True,
            "evidenceNeeded": "All 15 disclosure review slots completed by a human reviewer.",
        },
        {
            "blockerId": "second-reviewer-signoff",
            "status": "missing",
            "required": True,
            "evidenceNeeded": "Independent second reviewer signoff attached to the release record.",
        },
        {
            "blockerId": "reviewed-output-hash",
            "status": "missing",
            "required": True,
            "evidenceNeeded": "Reviewed output artifact hash bound to a release decision.",
        },
        {
            "blockerId": "suppression-and-reliability-review",
            "status": "missing",
            "required": True,
            "evidenceNeeded": "Suppression, domain DOF, effective sample, RSE and interval-width review.",
        },
        {
            "blockerId": "public-output-implementation-review",
            "status": "missing",
            "required": True,
            "evidenceNeeded": (
                "All 12 public-output implementation review execution slots completed after "
                "disclosure approval, with reviewed artifact binding, fresh no-real-values scan, "
                "static build review, rollback plan and second reviewer signoff."
            ),
        },
    ]
    readiness_summary = readiness.get("summary", {})
    disclosure_summary = disclosure.get("summary", {})
    local_summary = local_manifest.get("summary", {})
    no_real_summary = no_real.get("summary", {})
    implementation_summary = implementation_review.get("summary", {})
    implementation_execution_summary = implementation_execution.get("summary", {})
    return {
        "schemaVersion": "human-infra.nhanes-public-lmf-public-release-gate-validation.v1",
        "status": "pass" if not validation_errors else "fail",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "sourceId": readiness_summary.get("sourceId", "nhanes-public-lmf-2017-2018"),
        "validationPath": repo_rel(output_path),
        "inputs": [
            build_input_record(disclosure_path, disclosure),
            build_input_record(no_real_path, no_real, include_sha=False),
            build_input_record(local_manifest_path, local_manifest),
            build_input_record(readiness_path, readiness),
            build_input_record(implementation_review_path, implementation_review),
            build_input_record(implementation_execution_path, implementation_execution),
        ],
        "currentDecision": {
            "releaseGateEvaluated": not validation_errors,
            "releaseDecision": "blocked-pending-human-disclosure-review",
            "publicReleaseAllowed": False,
            "publicWeightedDomainOutputAllowed": False,
            "realDesignBasedIntervalsAllowed": False,
            "publicOutputImplementationAllowed": False,
            "calibrationAllowed": False,
            "individualPredictionAllowed": False,
            "medicalAdviceAllowed": False,
        },
        "gateSummary": {
            "upstreamReadyGateCount": readiness_summary.get("readyGateCount"),
            "upstreamBlockedGateCount": readiness_summary.get("blockedGateCount"),
            "requiredDisclosureSlotTotal": disclosure_summary.get("requiredSlotCount"),
            "completedDisclosureSlotTotal": disclosure_summary.get("completedSlotCount"),
            "humanReviewedSlotTotal": disclosure_summary.get("humanReviewedSlotCount"),
            "publicWebForbiddenKeyHits": no_real_summary.get("forbiddenKeyHitCount"),
            "publicWebBoundaryIssues": no_real_summary.get("booleanBoundaryIssueCount"),
            "localRunCellTotal": local_summary.get("cellCount"),
            "localManifestTrackedValuesOmitted": local_summary.get("trackedValuesOmitted"),
            "ignoredLocalRealValuesExist": local_summary.get("containsRealWeightedRatesInIgnoredReport"),
            "publicImplementationReviewSlotTotal": implementation_summary.get("reviewSlotTotal"),
            "pendingPublicImplementationReviewSlotTotal": implementation_summary.get("pendingReviewSlotTotal"),
            "completedPublicImplementationReviewSlotTotal": implementation_summary.get(
                "completedReviewSlotTotal"
            ),
            "publicImplementationReviewComplete": implementation_summary.get(
                "implementationReviewComplete"
            ),
            "publicImplementationExecutionSlotTotal": implementation_execution_summary.get(
                "reviewSlotTotal"
            ),
            "pendingPublicImplementationExecutionSlotTotal": implementation_execution_summary.get(
                "pendingReviewSlotTotal"
            ),
            "completedPublicImplementationExecutionSlotTotal": implementation_execution_summary.get(
                "completedReviewSlotTotal"
            ),
            "publicImplementationExecutionComplete": implementation_execution_summary.get(
                "implementationReviewComplete"
            ),
            "publicWebDataClean": no_real_summary.get("publicWebDataContainsRealWeightedValues") is False
            and no_real_summary.get("publicWebDataContainsRowLevelValues") is False,
        },
        "releaseBlockers": release_blockers,
        "allowedNextStates": [
            "packet-attached-pending-human-review",
            "cannot-evaluate",
        ],
        "forbiddenDirectTransitions": [
            "release-approved",
            "public-weighted-output-implemented",
            "calibration-enabled",
            "individual-prediction-enabled",
        ],
        "nonProofBoundary": {
            "confirms": [
                "tracked public Web data has no real weighted values or row-level values",
                "the local weighted-domain output path remains ignored and redacted in tracked artifacts",
                "the public-output implementation review template is present and still pending",
                "the public-output implementation review execution register is present and still pending",
                "the release gate is machine-readable and still blocks public release",
            ],
            "doesNotConfirm": [
                "human disclosure review completion",
                "second reviewer signoff",
                "public output implementation review completion",
                "public weighted-domain output permission",
                "public design-based interval release",
                "external validation",
                "calibration",
                "individual prediction",
                "medical advice",
            ],
        },
        "errors": validation_errors,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--disclosure-execution", type=Path, default=DEFAULT_DISCLOSURE_EXECUTION)
    parser.add_argument("--no-real-values", type=Path, default=DEFAULT_NO_REAL_VALUES)
    parser.add_argument("--local-manifest", type=Path, default=DEFAULT_LOCAL_MANIFEST)
    parser.add_argument("--readiness", type=Path, default=DEFAULT_READINESS)
    parser.add_argument("--implementation-review", type=Path, default=DEFAULT_IMPLEMENTATION_REVIEW)
    parser.add_argument("--implementation-execution", type=Path, default=DEFAULT_IMPLEMENTATION_EXECUTION)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    disclosure_path = args.disclosure_execution.resolve()
    no_real_path = args.no_real_values.resolve()
    local_manifest_path = args.local_manifest.resolve()
    readiness_path = args.readiness.resolve()
    implementation_review_path = args.implementation_review.resolve()
    implementation_execution_path = args.implementation_execution.resolve()
    output_path = args.out.resolve()

    errors: list[str] = []
    disclosure = load_json(disclosure_path)
    no_real = load_json(no_real_path)
    local_manifest = load_json(local_manifest_path)
    readiness = load_json(readiness_path)
    implementation_review = load_json(implementation_review_path)
    implementation_execution = load_json(implementation_execution_path)

    validate_disclosure_execution(disclosure, errors)
    validate_no_real_values(no_real, errors)
    validate_local_manifest(local_manifest, errors)
    validate_readiness(readiness, errors)
    validate_implementation_review(implementation_review, errors)
    validate_implementation_execution(implementation_execution, errors)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output = build_release_gate(
        disclosure_path,
        disclosure,
        no_real_path,
        no_real,
        local_manifest_path,
        local_manifest,
        readiness_path,
        readiness,
        implementation_review_path,
        implementation_review,
        implementation_execution_path,
        implementation_execution,
        output_path,
        list(errors),
    )
    validate_output_shape(output, errors)
    output["status"] = "pass" if not errors else "fail"
    output["errors"] = errors
    output_path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    if errors:
        for error in errors:
            print(f"NHANES public LMF public release gate error: {error}")
        return 1
    print(
        "NHANES public LMF public release gate ok: "
        "decision=blocked-pending-human-disclosure-review "
        f"blockers={len(output['releaseBlockers'])}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
