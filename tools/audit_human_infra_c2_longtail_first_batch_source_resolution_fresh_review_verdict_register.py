#!/usr/bin/env python3
"""审计 C2-LT-B1 source-resolution fresh review 判定账本。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = (
    ROOT
    / "docs/reference/human-infra-c2-longtail-first-batch-source-resolution-fresh-review-verdict-register.json"
)
BLOCKED_RESOLUTION_PATH = (
    ROOT / "docs/reference/human-infra-c2-longtail-first-batch-blocked-source-resolution-register.json"
)

SCHEMA = "human-infra.c2ltb1-source-resolution-fresh-review-verdict-register.v1"
STATUS = "active-c2ltb1-source-resolution-fresh-review-verdict-register-model-blocked"
REGISTER_LINK = "human-infra-c2-longtail-first-batch-source-resolution-fresh-review-verdict-register.json"
SCRIPT_LINK = (
    "audit_human_infra_c2_longtail_first_batch_source_resolution_fresh_review_verdict_register.py"
)

SOURCE_OF_TRUTH_KEYS = {
    "blockedSourceResolutionRegister",
    "originalFreshReviewVerdictRegister",
    "sourceExtractionRegister",
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
    "reviewId",
    "taskId",
    "domainId",
    "localDomainPath",
    "priorReviewerVerdict",
    "priorArtifactPromotionDecision",
    "sourceResolutionDecision",
    "freshReviewDate",
    "freshReviewMode",
    "candidateVerdicts",
    "selectedResolutionCandidates",
    "routeOnlyOrContextCandidates",
    "sourceResolutionReviewerVerdict",
    "sourceResolutionFinding",
    "nextAction",
    "artifactPromotionDecision",
    "modelAdmissionDecision",
    "blockedUses",
}

REQUIRED_CANDIDATE_FIELDS = {
    "candidateId",
    "candidateRole",
    "url",
    "sourceIdentityVerdict",
    "sourceContextVerdict",
    "resolutionUseRole",
    "resolutionUseVerdict",
    "freshReviewFinding",
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


def validate_scope(register: dict[str, Any], reviews: list[dict[str, Any]], errors: list[str]) -> None:
    scope = register.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return
    if scope.get("batchId") != "C2-LT-B1":
        fail(errors, "scope.batchId must be C2-LT-B1")
    if scope.get("reviewLevel") != "c2ltb1-source-resolution-fresh-review-v0.1":
        fail(errors, "scope.reviewLevel is invalid")
    candidate_count = sum(len(row.get("candidateVerdicts", [])) for row in reviews)
    expected = {
        "blockedResolutionRowCount": 6,
        "reviewedResolutionRowCount": len(reviews),
        "resolutionCandidateCount": candidate_count,
        "readyForCorrectedReextractionRowCount": len(reviews),
        "directArtifactFillRowCount": 0,
        "modelAdmissionOpenedRowCount": 0,
    }
    for key, value in expected.items():
        actual = require_int(scope.get(key), f"scope.{key}", errors)
        if actual is not None and actual != value:
            fail(errors, f"scope.{key} must equal {value}")
    non_claims = require_string_list(scope.get("nonClaims"), "scope.nonClaims", errors, min_len=4)
    required_phrases = ["does not change", "does not create reviewed artifacts", "does not authorize"]
    non_claim_text = "\n".join(non_claims)
    for phrase in required_phrases:
        if phrase not in non_claim_text:
            fail(errors, f"scope.nonClaims missing phrase: {phrase}")


def validate_reviews(
    register: dict[str, Any],
    blocked_register: dict[str, Any],
    errors: list[str],
) -> list[dict[str, Any]]:
    reviews = register.get("sourceResolutionFreshReviews")
    if not isinstance(reviews, list):
        fail(errors, "sourceResolutionFreshReviews must be a list")
        return []
    blocked_rows = blocked_register.get("resolutionRows")
    if not isinstance(blocked_rows, list):
        fail(errors, "blocked source resolution register must contain resolutionRows")
        return reviews

    expected_rows = {row.get("taskId"): row for row in blocked_rows if isinstance(row, dict)}
    seen_task_ids: set[str] = set()
    seen_review_ids: set[str] = set()

    for index, review in enumerate(reviews):
        if not isinstance(review, dict):
            fail(errors, f"sourceResolutionFreshReviews[{index}] must be an object")
            continue
        missing = REQUIRED_ROW_FIELDS - set(review)
        if missing:
            fail(errors, f"review[{index}] missing fields: {sorted(missing)}")

        review_id = require_string(review.get("reviewId"), f"review[{index}].reviewId", errors)
        if review_id:
            if review_id in seen_review_ids:
                fail(errors, f"duplicate reviewId: {review_id}")
            seen_review_ids.add(review_id)

        task_id = require_string(review.get("taskId"), f"{review_id}.taskId", errors)
        if task_id:
            if task_id in seen_task_ids:
                fail(errors, f"duplicate taskId: {task_id}")
            seen_task_ids.add(task_id)
            expected = expected_rows.get(task_id)
            if not expected:
                fail(errors, f"{review_id} references task outside blocked rows: {task_id}")
            else:
                for key in ("domainId", "localDomainPath", "priorReviewerVerdict", "priorArtifactPromotionDecision"):
                    if review.get(key) != expected.get(key):
                        fail(errors, f"{review_id}.{key} does not match blocked source resolution row")

        if review.get("freshReviewDate") != "2026-07-02":
            fail(errors, f"{review_id}.freshReviewDate must be 2026-07-02")
        if review.get("freshReviewMode") != "source-resolution-fresh-review-primary-or-authoritative-source-check":
            fail(errors, f"{review_id}.freshReviewMode is invalid")
        if review.get("artifactPromotionDecision") != "blocked-pending-corrected-source-reextraction-and-fresh-review":
            fail(errors, f"{review_id}.artifactPromotionDecision must remain blocked")
        if review.get("modelAdmissionDecision") != "blocked":
            fail(errors, f"{review_id}.modelAdmissionDecision must be blocked")
        if set(require_string_list(review.get("blockedUses"), f"{review_id}.blockedUses", errors)) != REQUIRED_BLOCKED_USES:
            fail(errors, f"{review_id}.blockedUses must match required blocked uses")

        selected = set(require_string_list(review.get("selectedResolutionCandidates"), f"{review_id}.selectedResolutionCandidates", errors))
        route_only = set(require_string_list(review.get("routeOnlyOrContextCandidates"), f"{review_id}.routeOnlyOrContextCandidates", errors, min_len=0))
        candidate_verdicts = review.get("candidateVerdicts")
        if not isinstance(candidate_verdicts, list) or not candidate_verdicts:
            fail(errors, f"{review_id}.candidateVerdicts must be a non-empty list")
            continue

        expected_candidate_ids = {
            candidate.get("candidateId")
            for candidate in expected_rows.get(task_id, {}).get("sourceResolutionCandidates", [])
            if isinstance(candidate, dict)
        }
        actual_candidate_ids: set[str] = set()
        for candidate_index, candidate in enumerate(candidate_verdicts):
            if not isinstance(candidate, dict):
                fail(errors, f"{review_id}.candidateVerdicts[{candidate_index}] must be an object")
                continue
            missing_candidate = REQUIRED_CANDIDATE_FIELDS - set(candidate)
            if missing_candidate:
                fail(
                    errors,
                    f"{review_id}.candidateVerdicts[{candidate_index}] missing fields: {sorted(missing_candidate)}",
                )
            candidate_id = require_string(
                candidate.get("candidateId"),
                f"{review_id}.candidateVerdicts[{candidate_index}].candidateId",
                errors,
            )
            if candidate_id:
                if candidate_id in actual_candidate_ids:
                    fail(errors, f"{review_id} has duplicate candidate verdict: {candidate_id}")
                actual_candidate_ids.add(candidate_id)
            url = require_string(candidate.get("url"), f"{review_id}.{candidate_id}.url", errors)
            if url and not url.startswith("https://"):
                fail(errors, f"{review_id}.{candidate_id}.url must be https")
            if candidate.get("sourceIdentityVerdict") != "source-identity-supported-for-resolution-candidate":
                fail(errors, f"{review_id}.{candidate_id}.sourceIdentityVerdict is invalid")
            use_verdict = require_string(
                candidate.get("resolutionUseVerdict"),
                f"{review_id}.{candidate_id}.resolutionUseVerdict",
                errors,
            )
            if candidate_id in route_only and use_verdict != "route-only-or-context-do-not-fill-artifact":
                fail(errors, f"{review_id}.{candidate_id} route-only candidate has invalid use verdict")
            if candidate_id in selected and use_verdict != "usable-for-corrected-reextraction-not-direct-artifact-fill":
                fail(errors, f"{review_id}.{candidate_id} selected candidate has invalid use verdict")

        if actual_candidate_ids != expected_candidate_ids:
            fail(errors, f"{review_id}.candidateVerdicts must cover the blocked register candidate set")
        if selected | route_only != actual_candidate_ids:
            fail(errors, f"{review_id} selected + routeOnly candidates must cover all candidate verdicts")
        if selected & route_only:
            fail(errors, f"{review_id} candidate cannot be both selected and route-only")
        if not selected:
            fail(errors, f"{review_id} must select at least one corrected candidate")

    if seen_task_ids != set(expected_rows):
        fail(errors, "sourceResolutionFreshReviews must cover exactly the blocked resolution row task IDs")
    return reviews


def validate_index_links(register: dict[str, Any], errors: list[str]) -> None:
    index_files = register.get("indexRequirements")
    if index_files != REQUIRED_INDEX_FILES:
        fail(errors, "indexRequirements must match required index file list")
    for relative_path in REQUIRED_INDEX_FILES:
        path = ROOT / relative_path
        if not path.exists():
            fail(errors, f"missing index file: {relative_path}")
            continue
        text = path.read_text(encoding="utf-8")
        if REGISTER_LINK not in text:
            fail(errors, f"index file does not reference register: {relative_path}")
    for relative_path in ["Makefile", "tools/README.md", "tools/AGENTS.md"]:
        path = ROOT / relative_path
        text = path.read_text(encoding="utf-8")
        if SCRIPT_LINK not in text:
            fail(errors, f"{relative_path} does not reference audit script")


def validate_summary(register: dict[str, Any], reviews: list[dict[str, Any]], errors: list[str]) -> None:
    summary = register.get("summary")
    if not isinstance(summary, dict):
        fail(errors, "summary must be an object")
        return
    candidate_count = sum(len(review.get("candidateVerdicts", [])) for review in reviews)
    expected = {
        "reviewedResolutionRows": len(reviews),
        "sourceResolutionCandidateCount": candidate_count,
        "readyForCorrectedReextractionRows": len(reviews),
        "directArtifactFillRows": 0,
    }
    for key, value in expected.items():
        actual = require_int(summary.get(key), f"summary.{key}", errors)
        if actual is not None and actual != value:
            fail(errors, f"summary.{key} must equal {value}")
    if summary.get("modelAdmissionDecision") != "blocked-for-all-source-resolution-fresh-review-rows":
        fail(errors, "summary.modelAdmissionDecision must keep model admission blocked")
    next_work = require_string(summary.get("nextWorkOrder"), "summary.nextWorkOrder", errors)
    if next_work and "corrected source re-extraction" not in next_work:
        fail(errors, "summary.nextWorkOrder must require corrected source re-extraction")


def main() -> int:
    errors: list[str] = []
    register = load_json(REGISTER_PATH, errors, "source-resolution fresh review verdict register")
    blocked_register = load_json(BLOCKED_RESOLUTION_PATH, errors, "blocked source resolution register")

    if register:
        if register.get("schemaVersion") != SCHEMA:
            fail(errors, f"schemaVersion must be {SCHEMA}")
        if register.get("status") != STATUS:
            fail(errors, f"status must be {STATUS}")
        require_string(register.get("registerId"), "registerId", errors)
        require_string(register.get("purpose"), "purpose", errors)
        if set(require_string_list(register.get("blockedUses"), "blockedUses", errors)) != REQUIRED_BLOCKED_USES:
            fail(errors, "blockedUses must match required blocked uses")
        validate_source_of_truth(register, errors)
        reviews = validate_reviews(register, blocked_register, errors)
        validate_scope(register, reviews, errors)
        validate_index_links(register, errors)
        validate_summary(register, reviews, errors)

    if errors:
        print("C2-LT-B1 source-resolution fresh review verdict audit failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("C2-LT-B1 source-resolution fresh review verdict audit passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
