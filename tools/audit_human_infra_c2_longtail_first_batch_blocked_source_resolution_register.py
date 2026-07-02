#!/usr/bin/env python3
"""审计 C2-LT-B1 blocked source resolution 账本。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = ROOT / "docs/reference/human-infra-c2-longtail-first-batch-blocked-source-resolution-register.json"
VERDICT_PATH = ROOT / "docs/reference/human-infra-c2-longtail-first-batch-independent-fresh-review-verdict-register.json"
EXTRACTION_PATH = ROOT / "docs/reference/human-infra-c2-longtail-first-batch-source-extraction-register.json"

SCHEMA = "human-infra.c2ltb1-blocked-source-resolution-register.v1"
STATUS = "active-c2ltb1-blocked-source-resolution-register-model-blocked"
REGISTER_LINK = "human-infra-c2-longtail-first-batch-blocked-source-resolution-register.json"
SCRIPT_LINK = "audit_human_infra_c2_longtail_first_batch_blocked_source_resolution_register.py"

ELIGIBLE_DECISION = "eligible-for-bounded-artifact-fill"
RESOLUTION_STATUS = "candidate-resolution-prepared-not-fresh-reviewed"
RESOLUTION_DECISION = "blocked-pending-resolution-fresh-review"
MODEL_DECISION = "blocked-pending-source-resolution-independent-fresh-review-and-reviewed-artifact-gates"

SOURCE_OF_TRUTH_KEYS = {
    "sourceExtractionRegister",
    "independentFreshReviewVerdictRegister",
    "reviewedCardArtifactRegister",
    "evidencePolicy",
    "maturityGapRegister",
}

REQUIRED_BLOCKED_USES = {
    "calibrated-prediction",
    "individual-advice",
    "individual-death-date-output",
    "intervention-ranking",
    "clinical-validity-claim",
    "domain-claim-upgrade",
}

REQUIRED_ROW_FIELDS = {
    "resolutionId",
    "taskId",
    "domainId",
    "localDomainPath",
    "sourceRefId",
    "originalSourceTitle",
    "originalSourceUrl",
    "priorReviewerVerdict",
    "priorArtifactPromotionDecision",
    "priorReviewerNote",
    "sourceResolutionDecision",
    "sourceResolutionStatus",
    "sourceResolutionCandidates",
    "requiredFreshReviewActions",
    "artifactPromotionDecision",
    "modelAdmissionDecision",
    "blockedUses",
}

REQUIRED_CANDIDATE_FIELDS = {
    "candidateId",
    "candidateRole",
    "title",
    "url",
    "sourceType",
    "resolutionFinding",
    "useBoundary",
}

REQUIRED_INDEX_FILES = [
    "README.md",
    "AGENTS.md",
    "docs/AGENTS.md",
    "docs/reference/README.md",
    "docs/reference/human-infra-maturity-roadmap.md",
    "tools/README.md",
    "tools/AGENTS.md",
]


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


def load_task_rows(path: Path, key: str, errors: list[str], context: str) -> dict[str, dict[str, Any]]:
    data = load_json(path, errors, context)
    rows = data.get(key) if data else None
    if not isinstance(rows, list):
        fail(errors, f"{context}.{key} must be a list")
        return {}
    result: dict[str, dict[str, Any]] = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"{context}.{key}[{index}] must be an object")
            continue
        task_id = require_string(row.get("taskId"), f"{context}.{key}[{index}].taskId", errors)
        if task_id:
            result[task_id] = row
    return result


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


def validate_scope(
    register: dict[str, Any],
    reviews: dict[str, dict[str, Any]],
    rows: list[dict[str, Any]],
    errors: list[str],
) -> set[str]:
    scope = register.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return set()
    if scope.get("batchId") != "C2-LT-B1":
        fail(errors, "scope.batchId must be C2-LT-B1")
    if scope.get("resolutionLevel") != "c2ltb1-noneligible-fresh-review-row-source-resolution-v0.1":
        fail(errors, "scope.resolutionLevel is invalid")

    blocked_ids = {
        task_id
        for task_id, review in reviews.items()
        if review.get("artifactPromotionDecision") != ELIGIBLE_DECISION
    }
    candidate_count = sum(len(row.get("sourceResolutionCandidates", [])) for row in rows)
    expected = {
        "totalFreshReviewVerdictRowCount": len(reviews),
        "eligibleFreshReviewVerdictRowCount": sum(
            1 for review in reviews.values() if review.get("artifactPromotionDecision") == ELIGIBLE_DECISION
        ),
        "blockedResolutionRowCount": len(blocked_ids),
        "downgradeBeforeFillRowCount": sum(
            1 for review in reviews.values() if review.get("artifactPromotionDecision") == "downgrade-before-fill"
        ),
        "cannotEvaluateRowCount": sum(
            1 for review in reviews.values() if review.get("artifactPromotionDecision") == "blocked-cannot-evaluate"
        ),
        "resolutionCandidateCount": candidate_count,
    }
    for key, value in expected.items():
        actual = require_int(scope.get(key), f"scope.{key}", errors)
        if actual is not None and actual != value:
            fail(errors, f"scope.{key} must equal {value}")
    non_claims = require_string_list(scope.get("nonClaims"), "scope.nonClaims", errors, min_len=4)
    required_phrases = ["does not change", "does not create reviewed artifacts", "does not authorize"]
    for phrase in required_phrases:
        if not any(phrase in item for item in non_claims):
            fail(errors, f"scope.nonClaims must include phrase: {phrase}")
    return blocked_ids


def validate_candidates(row: dict[str, Any], row_index: int, errors: list[str]) -> int:
    candidates = row.get("sourceResolutionCandidates")
    if not isinstance(candidates, list) or len(candidates) < 2:
        fail(errors, f"resolutionRows[{row_index}].sourceResolutionCandidates must contain at least 2 candidates")
        return 0
    seen: set[str] = set()
    for candidate_index, candidate in enumerate(candidates):
        if not isinstance(candidate, dict):
            fail(errors, f"resolutionRows[{row_index}].sourceResolutionCandidates[{candidate_index}] must be an object")
            continue
        missing = REQUIRED_CANDIDATE_FIELDS - set(candidate)
        if missing:
            fail(
                errors,
                f"resolutionRows[{row_index}].sourceResolutionCandidates[{candidate_index}] missing fields: {sorted(missing)}",
            )
        candidate_id = require_string(
            candidate.get("candidateId"),
            f"resolutionRows[{row_index}].sourceResolutionCandidates[{candidate_index}].candidateId",
            errors,
        )
        if candidate_id in seen:
            fail(errors, f"duplicate candidateId in resolutionRows[{row_index}]: {candidate_id}")
        seen.add(candidate_id)
        url = require_string(
            candidate.get("url"),
            f"resolutionRows[{row_index}].sourceResolutionCandidates[{candidate_index}].url",
            errors,
        )
        if url and not url.startswith("https://"):
            fail(errors, f"candidate URL must be https: {url}")
        for field in REQUIRED_CANDIDATE_FIELDS - {"candidateId", "url"}:
            require_string(
                candidate.get(field),
                f"resolutionRows[{row_index}].sourceResolutionCandidates[{candidate_index}].{field}",
                errors,
            )
    return len(candidates)


def validate_rows(
    register: dict[str, Any],
    reviews: dict[str, dict[str, Any]],
    extractions: dict[str, dict[str, Any]],
    blocked_ids: set[str],
    errors: list[str],
) -> int:
    rows = register.get("resolutionRows")
    if not isinstance(rows, list):
        fail(errors, "resolutionRows must be a list")
        return 0
    row_ids: set[str] = set()
    candidate_count = 0
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"resolutionRows[{index}] must be an object")
            continue
        missing = REQUIRED_ROW_FIELDS - set(row)
        if missing:
            fail(errors, f"resolutionRows[{index}] missing fields: {sorted(missing)}")
        task_id = require_string(row.get("taskId"), f"resolutionRows[{index}].taskId", errors)
        if not task_id:
            continue
        row_ids.add(task_id)
        if task_id not in blocked_ids:
            fail(errors, f"resolutionRows[{index}] taskId is not a blocked fresh-review row: {task_id}")
        review = reviews.get(task_id, {})
        extraction = extractions.get(task_id, {})
        field_pairs = {
            "domainId": review.get("domainId"),
            "originalSourceTitle": review.get("reviewedSourceTitle"),
            "originalSourceUrl": review.get("reviewedSourceUrl"),
            "priorReviewerVerdict": review.get("reviewerVerdict"),
            "priorArtifactPromotionDecision": review.get("artifactPromotionDecision"),
            "priorReviewerNote": review.get("reviewerNote"),
            "localDomainPath": extraction.get("localDomainPath"),
            "sourceRefId": extraction.get("sourceRefId"),
        }
        for field, expected in field_pairs.items():
            if expected and row.get(field) != expected:
                fail(errors, f"resolutionRows[{index}].{field} must match source row for {task_id}")
        if row.get("sourceResolutionStatus") != RESOLUTION_STATUS:
            fail(errors, f"resolutionRows[{index}].sourceResolutionStatus is invalid")
        if row.get("artifactPromotionDecision") != RESOLUTION_DECISION:
            fail(errors, f"resolutionRows[{index}].artifactPromotionDecision must stay blocked")
        if row.get("modelAdmissionDecision") != MODEL_DECISION:
            fail(errors, f"resolutionRows[{index}].modelAdmissionDecision is invalid")
        blocked_uses = set(require_string_list(row.get("blockedUses"), f"resolutionRows[{index}].blockedUses", errors))
        if blocked_uses != REQUIRED_BLOCKED_USES:
            fail(errors, f"resolutionRows[{index}].blockedUses must match required blocked uses")
        require_string_list(
            row.get("requiredFreshReviewActions"),
            f"resolutionRows[{index}].requiredFreshReviewActions",
            errors,
            min_len=5,
        )
        candidate_count += validate_candidates(row, index, errors)
    if row_ids != blocked_ids:
        fail(errors, "resolutionRows taskIds must exactly match non-eligible fresh-review rows")
    return candidate_count


def validate_index_requirements(register: dict[str, Any], errors: list[str]) -> None:
    requirements = require_string_list(register.get("indexRequirements"), "indexRequirements", errors, min_len=1)
    if set(requirements) != set(REQUIRED_INDEX_FILES):
        fail(errors, "indexRequirements must match required index files")
    for relative_path in REQUIRED_INDEX_FILES:
        target = repo_path(relative_path, f"indexRequirements.{relative_path}", errors)
        if target is None:
            continue
        text = target.read_text(encoding="utf-8")
        if REGISTER_LINK not in text:
            fail(errors, f"{relative_path} must reference {REGISTER_LINK}")
        if relative_path.startswith("tools/") and SCRIPT_LINK not in text:
            fail(errors, f"{relative_path} must reference {SCRIPT_LINK}")


def validate_summary(register: dict[str, Any], rows: list[dict[str, Any]], candidate_count: int, errors: list[str]) -> None:
    summary = register.get("summary")
    if not isinstance(summary, dict):
        fail(errors, "summary must be an object")
        return
    expected = {
        "blockedRowCount": len(rows),
        "sourceResolutionCandidateCount": candidate_count,
    }
    for key, value in expected.items():
        actual = require_int(summary.get(key), f"summary.{key}", errors)
        if actual is not None and actual != value:
            fail(errors, f"summary.{key} must equal {value}")
    if summary.get("modelAdmissionDecision") != "blocked-for-all-resolution-rows":
        fail(errors, "summary.modelAdmissionDecision must keep model admission blocked")
    require_string(summary.get("nextWorkOrder"), "summary.nextWorkOrder", errors)


def main() -> int:
    errors: list[str] = []
    register = load_json(REGISTER_PATH, errors, "blocked source resolution register")
    reviews = load_task_rows(VERDICT_PATH, "sourceTaskFreshReviews", errors, "fresh review verdict register")
    extractions = load_task_rows(EXTRACTION_PATH, "extractedRows", errors, "source extraction register")

    if register:
        if register.get("schemaVersion") != SCHEMA:
            fail(errors, f"schemaVersion must be {SCHEMA}")
        if register.get("status") != STATUS:
            fail(errors, f"status must be {STATUS}")
        require_string(register.get("registerId"), "registerId", errors)
        require_string(register.get("purpose"), "purpose", errors)
        blocked_uses = set(require_string_list(register.get("blockedUses"), "blockedUses", errors))
        if blocked_uses != REQUIRED_BLOCKED_USES:
            fail(errors, "blockedUses must match required blocked uses")
        validate_source_of_truth(register, errors)
        rows = register.get("resolutionRows") if isinstance(register.get("resolutionRows"), list) else []
        blocked_ids = validate_scope(register, reviews, rows, errors)
        candidate_count = validate_rows(register, reviews, extractions, blocked_ids, errors)
        validate_index_requirements(register, errors)
        validate_summary(register, rows, candidate_count, errors)

    if errors:
        print("C2-LT-B1 blocked source resolution audit failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        "C2-LT-B1 blocked source resolution audit ok: "
        f"rows={len(register.get('resolutionRows', []))} "
        f"candidates={sum(len(row['sourceResolutionCandidates']) for row in register.get('resolutionRows', []))}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
