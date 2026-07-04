#!/usr/bin/env python3
"""审计 C2 长尾第十批 independent fresh-review verdict 账本。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = (
    ROOT
    / "docs/reference/human-infra-c2-longtail-tenth-batch-independent-fresh-review-verdict-register.json"
)
PROTOCOL_PATH = ROOT / "docs/reference/human-infra-c2-longtail-tenth-batch-independent-fresh-review-protocol.json"
EXTRACTION_PATH = ROOT / "docs/reference/human-infra-c2-longtail-tenth-batch-source-extraction-register.json"

SCHEMA = "human-infra.c2-longtail-tenth-batch-independent-fresh-review-verdict-register.v1"
STATUS = "active-c2ltb10-independent-fresh-review-verdict-register-model-blocked"
EXPECTED_TASK_IDS = [f"C2LTB10-EXT-{index:03d}" for index in range(1, 25)]
ELIGIBLE_DECISION = "eligible-for-bounded-reviewed-artifact-prep"
MODEL_DECISION = "blocked-pending-b10-reviewed-artifact-gates-and-calibrated-model-validation"
ARTIFACT_TYPES = [
    "reviewed-source-card",
    "reviewed-variable-card",
    "reviewed-endpoint-card",
    "reviewed-uncertainty-card",
    "reviewed-transfer-boundary-card",
    "reviewed-downgrade-check",
]
SOURCE_OF_TRUTH_KEYS = {
    "independentFreshReviewProtocol",
    "localReviewRegister",
    "sourceExtractionRegister",
    "evidencePolicy",
    "maturityGapRegister",
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def load_json(path: Path, errors: list[str], context: str) -> dict[str, Any]:
    if not path.exists():
        fail(errors, f"missing {context}: {path.relative_to(ROOT)}")
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(errors, f"invalid JSON in {context}: {exc}")
        return {}
    if not isinstance(data, dict):
        fail(errors, f"{context} must be a JSON object")
        return {}
    return data


def require_string(value: Any, context: str, errors: list[str]) -> str:
    if not isinstance(value, str) or not value.strip():
        fail(errors, f"{context} must be a non-empty string")
        return ""
    return value


def require_int(value: Any, context: str, errors: list[str]) -> int | None:
    if not isinstance(value, int):
        fail(errors, f"{context} must be an integer")
        return None
    return value


def require_string_list(value: Any, context: str, errors: list[str], min_len: int = 1) -> list[str]:
    if not isinstance(value, list) or len(value) < min_len:
        fail(errors, f"{context} must be a list with at least {min_len} item(s)")
        return []
    result: list[str] = []
    for index, item in enumerate(value):
        if not isinstance(item, str) or not item.strip():
            fail(errors, f"{context}[{index}] must be a non-empty string")
            continue
        result.append(item)
    return result


def repo_path(relative_path: str, context: str, errors: list[str]) -> Path | None:
    value = require_string(relative_path, context, errors)
    if not value:
        return None
    if value.startswith(("http://", "https://")):
        fail(errors, f"{context} must be a local path, not URL")
        return None
    target = (ROOT / value).resolve()
    try:
        target.relative_to(ROOT)
    except ValueError:
        fail(errors, f"{context} escapes repository: {value}")
        return None
    if not target.exists():
        fail(errors, f"{context} does not exist: {value}")
        return None
    return target


def extraction_rows(errors: list[str]) -> dict[str, dict[str, Any]]:
    data = load_json(EXTRACTION_PATH, errors, "C2-LT-B10 source extraction register")
    rows = data.get("extractedRows") if data else None
    if not isinstance(rows, list):
        fail(errors, "source extraction register extractedRows must be a list")
        return {}
    result: dict[str, dict[str, Any]] = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"extractedRows[{index}] must be an object")
            continue
        task_id = require_string(row.get("taskId"), f"extractedRows[{index}].taskId", errors)
        if task_id:
            result[task_id] = row
    if list(result) != EXPECTED_TASK_IDS:
        fail(errors, "source extraction rows must be ordered as C2LTB10-EXT-001 through C2LTB10-EXT-024")
    return result


def required_blocked_uses(errors: list[str]) -> set[str]:
    protocol = load_json(PROTOCOL_PATH, errors, "C2-LT-B10 independent fresh review protocol")
    return set(require_string_list(protocol.get("blockedUses"), "protocol.blockedUses", errors, 17))


def validate_source_of_truth(register: dict[str, Any], errors: list[str]) -> None:
    source = register.get("sourceOfTruth")
    if not isinstance(source, dict):
        fail(errors, "sourceOfTruth must be an object")
        return
    if set(source) != SOURCE_OF_TRUTH_KEYS:
        fail(errors, "sourceOfTruth must contain exactly the required keys")
    for key in SOURCE_OF_TRUTH_KEYS:
        value = source.get(key)
        if value:
            repo_path(value, f"sourceOfTruth.{key}", errors)


def validate_reviews(register: dict[str, Any], rows_by_task: dict[str, dict[str, Any]], blocked_uses: set[str], errors: list[str]) -> None:
    reviews = register.get("freshReviewVerdicts")
    if not isinstance(reviews, list):
        fail(errors, "freshReviewVerdicts must be a list")
        return
    if len(reviews) != len(EXPECTED_TASK_IDS):
        fail(errors, "freshReviewVerdicts must contain 24 rows")

    seen: list[str] = []
    for index, review in enumerate(reviews):
        if not isinstance(review, dict):
            fail(errors, f"freshReviewVerdicts[{index}] must be an object")
            continue
        review_id = require_string(review.get("reviewId"), f"review[{index}].reviewId", errors)
        expected_review_id = f"C2LTB10-FRV-{index + 1:03d}"
        if review_id and review_id != expected_review_id:
            fail(errors, f"{review_id} must be {expected_review_id}")
        task_id = require_string(review.get("taskId"), f"{review_id}.taskId", errors)
        seen.append(task_id)
        source = rows_by_task.get(task_id)
        if not source:
            fail(errors, f"{review_id}.taskId has no extraction row: {task_id}")
            continue
        for field in ["domainId", "localDomainPath", "sourceRefId", "sourceTitle", "sourceUrl"]:
            if review.get(field) != source.get(field):
                fail(errors, f"{review_id}.{field} must match extraction row")
        if review.get("batchId") != "C2-LT-B10":
            fail(errors, f"{review_id}.batchId must be C2-LT-B10")
        if review.get("freshReviewDate") != "2026-07-04":
            fail(errors, f"{review_id}.freshReviewDate must be 2026-07-04")
        if review.get("reviewerVerdict") != ELIGIBLE_DECISION:
            fail(errors, f"{review_id}.reviewerVerdict must stay eligible only for bounded artifact prep")
        if review.get("artifactPromotionDecision") != ELIGIBLE_DECISION:
            fail(errors, f"{review_id}.artifactPromotionDecision must stay eligible only for bounded artifact prep")
        if review.get("modelAdmissionDecision") != MODEL_DECISION:
            fail(errors, f"{review_id}.modelAdmissionDecision must keep model admission blocked")
        if set(require_string_list(review.get("allowedArtifactTypes"), f"{review_id}.allowedArtifactTypes", errors, 6)) != set(ARTIFACT_TYPES):
            fail(errors, f"{review_id}.allowedArtifactTypes must match required artifact types")
        if set(require_string_list(review.get("blockedUses"), f"{review_id}.blockedUses", errors, 17)) != blocked_uses:
            fail(errors, f"{review_id}.blockedUses must match protocol blocked uses")
        trace = review.get("reviewEvidenceTrace")
        if not isinstance(trace, list) or len(trace) < 3:
            fail(errors, f"{review_id}.reviewEvidenceTrace must contain source, extraction and local-review evidence")
        else:
            urls = [item.get("url") for item in trace if isinstance(item, dict)]
            if source.get("sourceUrl") not in urls:
                fail(errors, f"{review_id}.reviewEvidenceTrace must include source URL")
        for field in [
            "sourceIdentityVerdict",
            "sourceContextVerdict",
            "exactClaimUseVerdict",
            "domainTransferVerdict",
            "modelPositionVerdict",
            "uncertaintyBoundaryVerdict",
            "downgradeVerdict",
            "blockedUseVerdict",
            "adviceUseBoundaryVerdict",
            "freshReviewFinding",
            "downgradeOrBlockReason",
            "nextAction",
        ]:
            require_string(review.get(field), f"{review_id}.{field}", errors)
        boundary_text = " ".join(str(review.get(field, "")) for field in ["freshReviewFinding", "nextAction"])
        for phrase in ["advice", "model admission"]:
            if phrase not in boundary_text:
                fail(errors, f"{review_id} must preserve {phrase} boundary")
    if seen != EXPECTED_TASK_IDS:
        fail(errors, "freshReviewVerdicts must cover C2LTB10-EXT-001 through C2LTB10-EXT-024 in order")


def validate_scope(register: dict[str, Any], errors: list[str]) -> None:
    scope = register.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return
    expected_counts = {
        "reviewedTaskCount": 24,
        "eligibleForBoundedArtifactPrepCount": 24,
        "downgradeBeforeFillCount": 0,
        "rejectedNoFillCount": 0,
        "blockedCannotEvaluateCount": 0,
        "modelAdmissionCount": 0,
        "adviceUseAdmissionCount": 0,
    }
    if scope.get("batchId") != "C2-LT-B10":
        fail(errors, "scope.batchId must be C2-LT-B10")
    for key, expected in expected_counts.items():
        value = require_int(scope.get(key), f"scope.{key}", errors)
        if value is not None and value != expected:
            fail(errors, f"scope.{key} must equal {expected}")
    if require_string_list(scope.get("reviewedTaskIds"), "scope.reviewedTaskIds", errors, 24) != EXPECTED_TASK_IDS:
        fail(errors, "scope.reviewedTaskIds must cover all C2LTB10 task IDs")


def main() -> int:
    errors: list[str] = []
    register = load_json(REGISTER_PATH, errors, "C2-LT-B10 independent fresh review verdict register")
    rows = extraction_rows(errors)
    blocked_uses = required_blocked_uses(errors)

    if register:
        if register.get("schemaVersion") != SCHEMA:
            fail(errors, f"schemaVersion must be {SCHEMA}")
        if register.get("status") != STATUS:
            fail(errors, f"status must be {STATUS}")
        require_string(register.get("registerId"), "registerId", errors)
        require_string(register.get("purpose"), "purpose", errors)
        validate_source_of_truth(register, errors)
        validate_scope(register, errors)
        if set(require_string_list(register.get("blockedUses"), "blockedUses", errors, 17)) != blocked_uses:
            fail(errors, "blockedUses must match protocol blocked uses")
        validate_reviews(register, rows, blocked_uses, errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("C2 longtail tenth-batch independent fresh review verdict audit ok: reviews=24 eligible=24 model_admission=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
