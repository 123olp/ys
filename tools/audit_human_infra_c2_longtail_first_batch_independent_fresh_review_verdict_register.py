#!/usr/bin/env python3
"""审计 C2-LT-B1 独立 fresh review verdict 账本。"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
VERDICT_PATH = ROOT / "docs/reference/human-infra-c2-longtail-first-batch-independent-fresh-review-verdict-register.json"
PROTOCOL_PATH = ROOT / "docs/reference/human-infra-c2-longtail-first-batch-independent-fresh-review-protocol.json"
LOCAL_REVIEW_PATH = ROOT / "docs/reference/human-infra-c2-longtail-first-batch-local-review-register.json"
EXTRACTION_PATH = ROOT / "docs/reference/human-infra-c2-longtail-first-batch-source-extraction-register.json"

SCHEMA = "human-infra.c2-longtail-first-batch-independent-fresh-review-verdict-register.v1"
PARTIAL_STATUS = "active-fresh-review-verdict-register-partial"
COMPLETE_STATUS = "active-fresh-review-verdict-register-complete"
VERDICT_LINK = "human-infra-c2-longtail-first-batch-independent-fresh-review-verdict-register.json"
REQUIRED_SOURCE_OF_TRUTH = {
    "independentFreshReviewProtocol",
    "localReviewRegister",
    "sourceExtractionRegister",
    "evidencePolicy",
    "maturityGapRegister",
}
REQUIRED_REVIEW_FIELDS = {
    "sourceIdentityVerdict",
    "sourceContextVerdict",
    "exactClaimUseVerdict",
    "domainTransferVerdict",
    "modelPositionVerdict",
    "uncertaintyBoundaryVerdict",
    "downgradeVerdict",
    "blockedUseVerdict",
    "reviewerNote",
}
REQUIRED_BLOCKED_USES = {
    "calibrated-prediction",
    "individual-advice",
    "individual-death-date-output",
    "intervention-ranking",
    "clinical-validity-claim",
    "domain-claim-upgrade",
}
ALLOWED_STATUSES = {PARTIAL_STATUS, COMPLETE_STATUS}
REQUIRED_INDEX_FILES = [
    "README.md",
    "docs/reference/README.md",
    "docs/reference/human-infra-maturity-roadmap.md",
    "tools/README.md",
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
    if not isinstance(relative_path, str) or not relative_path.strip():
        fail(errors, f"{context} must be a non-empty local path")
        return None
    if relative_path.startswith(("http://", "https://")):
        fail(errors, f"{context} must be a local path, not URL")
        return None
    target = (ROOT / relative_path).resolve()
    try:
        target.relative_to(ROOT)
    except ValueError:
        fail(errors, f"{context} escapes repository: {relative_path}")
        return None
    if not target.exists():
        fail(errors, f"{context} does not exist: {relative_path}")
        return None
    return target


def protocol_batches(protocol: dict[str, Any], errors: list[str]) -> list[dict[str, Any]]:
    batches = protocol.get("reviewBatches")
    if not isinstance(batches, list):
        fail(errors, "protocol.reviewBatches must be a list")
        return []
    return [batch for batch in batches if isinstance(batch, dict)]


def extraction_rows(errors: list[str]) -> dict[str, dict[str, Any]]:
    extraction = load_json(EXTRACTION_PATH, errors, "C2-LT-B1 source extraction register")
    rows = extraction.get("extractedRows") if extraction else None
    if not isinstance(rows, list):
        fail(errors, "source extraction register extractedRows must be a list")
        return {}
    return {row.get("taskId"): row for row in rows if isinstance(row, dict) and isinstance(row.get("taskId"), str)}


def validate_top_level(verdict: dict[str, Any], protocol: dict[str, Any], errors: list[str]) -> None:
    if verdict.get("schemaVersion") != SCHEMA:
        fail(errors, f"schemaVersion must be {SCHEMA}")
    if verdict.get("status") not in ALLOWED_STATUSES:
        fail(errors, f"status must be one of {sorted(ALLOWED_STATUSES)}")
    require_string(verdict.get("registerId"), "registerId", errors)
    require_string(verdict.get("purpose"), "purpose", errors)

    source = verdict.get("sourceOfTruth")
    if not isinstance(source, dict):
        fail(errors, "sourceOfTruth must be an object")
    else:
        if set(source) != REQUIRED_SOURCE_OF_TRUTH:
            fail(errors, "sourceOfTruth must contain exactly the required keys")
        for key in REQUIRED_SOURCE_OF_TRUTH:
            value = require_string(source.get(key), f"sourceOfTruth.{key}", errors)
            if value:
                repo_path(value, f"sourceOfTruth.{key}", errors)

    if set(require_string_list(verdict.get("requiredReviewFields"), "requiredReviewFields", errors, len(REQUIRED_REVIEW_FIELDS))) != REQUIRED_REVIEW_FIELDS:
        fail(errors, "requiredReviewFields must match required review fields")
    protocol_verdicts = set(protocol.get("verdictTaxonomy", []))
    protocol_decisions = set(protocol.get("artifactPromotionDecisions", []))
    if set(require_string_list(verdict.get("verdictTaxonomy"), "verdictTaxonomy", errors, len(protocol_verdicts))) != protocol_verdicts:
        fail(errors, "verdictTaxonomy must match protocol verdictTaxonomy")
    if set(require_string_list(verdict.get("artifactPromotionDecisions"), "artifactPromotionDecisions", errors, len(protocol_decisions))) != protocol_decisions:
        fail(errors, "artifactPromotionDecisions must match protocol artifactPromotionDecisions")
    if set(require_string_list(verdict.get("blockedUses"), "blockedUses", errors, len(REQUIRED_BLOCKED_USES))) != REQUIRED_BLOCKED_USES:
        fail(errors, "blockedUses must match required blocked uses")


def validate_scope(verdict: dict[str, Any], batches: list[dict[str, Any]], errors: list[str]) -> tuple[list[dict[str, Any]], list[str]]:
    scope = verdict.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return [], []
    reviewed_batch_ids = require_string_list(scope.get("reviewedBatchIds"), "scope.reviewedBatchIds", errors, 1)
    by_id = {batch.get("batchId"): batch for batch in batches}
    reviewed_batches = []
    for batch_id in reviewed_batch_ids:
        batch = by_id.get(batch_id)
        if not batch:
            fail(errors, f"scope.reviewedBatchIds contains unknown batch: {batch_id}")
            continue
        reviewed_batches.append(batch)
    reviewed_task_ids = [task_id for batch in reviewed_batches for task_id in batch.get("taskIds", [])]
    remaining_batches = [batch.get("batchId") for batch in batches if batch.get("batchId") not in set(reviewed_batch_ids)]

    expected_counts = {
        "reviewedBatchCount": len(reviewed_batch_ids),
        "totalLocalReviewedExtractionTaskCount": 48,
        "reviewedExtractionTaskCount": len(reviewed_task_ids),
        "remainingExtractionTaskCount": 48 - len(reviewed_task_ids),
        "reviewedDomainCount": len({domain for batch in reviewed_batches for domain in batch.get("domainIds", [])}),
    }
    for key, expected in expected_counts.items():
        value = require_int(scope.get(key), f"scope.{key}", errors)
        if value is not None and value != expected:
            fail(errors, f"scope.{key} must equal {expected}")
    if verdict.get("status") == PARTIAL_STATUS and scope.get("remainingExtractionTaskCount") == 0:
        fail(errors, "partial status cannot have zero remainingExtractionTaskCount")
    if verdict.get("status") == COMPLETE_STATUS and scope.get("remainingExtractionTaskCount") != 0:
        fail(errors, "complete status requires zero remainingExtractionTaskCount")
    require_string(scope.get("reviewMode"), "scope.reviewMode", errors)
    require_string(scope.get("artifactPromotionDecision"), "scope.artifactPromotionDecision", errors)
    non_claims = " ".join(require_string_list(scope.get("nonClaims"), "scope.nonClaims", errors, 4))
    for phrase in ["not a completed Source Card set", "does not authorize calibrated prediction", "remaining prepared rows still require fresh review"]:
        if verdict.get("status") == PARTIAL_STATUS and phrase not in non_claims:
            fail(errors, f"scope.nonClaims must mention {phrase!r}")
    return reviewed_batches, remaining_batches


def validate_reviews(
    verdict: dict[str, Any],
    reviewed_batches: list[dict[str, Any]],
    rows: dict[str, dict[str, Any]],
    protocol: dict[str, Any],
    errors: list[str],
) -> None:
    reviewed_task_ids = [task_id for batch in reviewed_batches for task_id in batch.get("taskIds", [])]
    protocol_verdicts = set(protocol.get("verdictTaxonomy", []))
    protocol_decisions = set(protocol.get("artifactPromotionDecisions", []))

    reviews = verdict.get("sourceTaskFreshReviews")
    if not isinstance(reviews, list):
        fail(errors, "sourceTaskFreshReviews must be a list")
        return
    if [review.get("taskId") for review in reviews if isinstance(review, dict)] != reviewed_task_ids:
        fail(errors, "sourceTaskFreshReviews must cover reviewed protocol task IDs in order")

    for index, review in enumerate(reviews):
        context = f"sourceTaskFreshReviews[{index}]"
        if not isinstance(review, dict):
            fail(errors, f"{context} must be an object")
            continue
        task_id = require_string(review.get("taskId"), f"{context}.taskId", errors)
        row = rows.get(task_id)
        if not row:
            fail(errors, f"{context}.taskId missing from extraction register")
            continue
        if review.get("domainId") != row.get("domainId"):
            fail(errors, f"{context}.domainId must match extraction row")
        if review.get("reviewedSourceTitle") != row.get("sourceTitle"):
            fail(errors, f"{context}.reviewedSourceTitle must match extraction row")
        if review.get("reviewedSourceUrl") != row.get("sourceUrl"):
            fail(errors, f"{context}.reviewedSourceUrl must match extraction row")
        for field in REQUIRED_REVIEW_FIELDS | {"freshReviewDate", "freshReviewMode", "registeredSourceRole", "registeredExactClaimUse", "registeredTransferBoundary"}:
            require_string(review.get(field), f"{context}.{field}", errors)
        evidence = review.get("freshReviewEvidence")
        if not isinstance(evidence, list) or not evidence:
            fail(errors, f"{context}.freshReviewEvidence must be a non-empty list")
        else:
            for evidence_index, item in enumerate(evidence):
                if not isinstance(item, dict):
                    fail(errors, f"{context}.freshReviewEvidence[{evidence_index}] must be an object")
                    continue
                require_string(item.get("url"), f"{context}.freshReviewEvidence[{evidence_index}].url", errors)
                require_string(item.get("evidenceType"), f"{context}.freshReviewEvidence[{evidence_index}].evidenceType", errors)
                require_string(item.get("finding"), f"{context}.freshReviewEvidence[{evidence_index}].finding", errors)
        reviewer_verdict = require_string(review.get("reviewerVerdict"), f"{context}.reviewerVerdict", errors)
        if reviewer_verdict and reviewer_verdict not in protocol_verdicts:
            fail(errors, f"{context}.reviewerVerdict must be in protocol taxonomy")
        decision = require_string(review.get("artifactPromotionDecision"), f"{context}.artifactPromotionDecision", errors)
        if decision and decision not in protocol_decisions:
            fail(errors, f"{context}.artifactPromotionDecision must be in protocol decisions")
        if "blocked" not in str(review.get("blockedUseVerdict", "")):
            fail(errors, f"{context}.blockedUseVerdict must keep blocked uses blocked")
        if "blocked" not in str(review.get("modelPositionVerdict", "")):
            fail(errors, f"{context}.modelPositionVerdict must keep model admission blocked")


def validate_coverage(verdict: dict[str, Any], reviewed_batches: list[dict[str, Any]], protocol: dict[str, Any], errors: list[str]) -> None:
    reviewed_task_ids = [task_id for batch in reviewed_batches for task_id in batch.get("taskIds", [])]
    protocol_verdicts = set(protocol.get("verdictTaxonomy", []))
    protocol_decisions = set(protocol.get("artifactPromotionDecisions", []))
    coverage = verdict.get("taskCoverage")
    if not isinstance(coverage, list):
        fail(errors, "taskCoverage must be a list")
        return
    if [item.get("taskId") for item in coverage if isinstance(item, dict)] != reviewed_task_ids:
        fail(errors, "taskCoverage must cover reviewed task IDs in order")
    for index, item in enumerate(coverage):
        if not isinstance(item, dict):
            fail(errors, f"taskCoverage[{index}] must be an object")
            continue
        if item.get("reviewerVerdict") not in protocol_verdicts:
            fail(errors, f"taskCoverage[{index}].reviewerVerdict must be in protocol taxonomy")
        if item.get("artifactPromotionDecision") not in protocol_decisions:
            fail(errors, f"taskCoverage[{index}].artifactPromotionDecision must be in protocol decisions")
        if "blocked" not in str(item.get("modelAdmissionDecision", "")):
            fail(errors, f"taskCoverage[{index}].modelAdmissionDecision must remain blocked")


def validate_remaining_and_summaries(
    verdict: dict[str, Any],
    reviewed_batches: list[dict[str, Any]],
    remaining_batches: list[str],
    errors: list[str],
) -> None:
    remaining = require_string_list(verdict.get("remainingFreshReviewBatches"), "remainingFreshReviewBatches", errors, 0)
    if remaining != remaining_batches:
        fail(errors, "remainingFreshReviewBatches must list unreviewed protocol batches in order")
    summaries = verdict.get("batchSummaries")
    if not isinstance(summaries, list):
        fail(errors, "batchSummaries must be a list")
        return
    reviewed_batch_ids = verdict.get("scope", {}).get("reviewedBatchIds", []) if isinstance(verdict.get("scope"), dict) else []
    if [summary.get("batchId") for summary in summaries if isinstance(summary, dict)] != reviewed_batch_ids:
        fail(errors, "batchSummaries must match reviewedBatchIds")
    coverage_by_task = {
        item.get("taskId"): item
        for item in verdict.get("taskCoverage", [])
        if isinstance(item, dict)
    }
    protocol_batch_by_id = {batch.get("batchId"): batch for batch in reviewed_batches}
    for index, summary in enumerate(summaries):
        if not isinstance(summary, dict):
            fail(errors, f"batchSummaries[{index}] must be an object")
            continue
        batch = protocol_batch_by_id.get(summary.get("batchId"))
        if not batch:
            fail(errors, f"batchSummaries[{index}].batchId must match a reviewed protocol batch")
            continue
        batch_coverage = [coverage_by_task.get(task_id) for task_id in batch.get("taskIds", [])]
        if any(item is None for item in batch_coverage):
            fail(errors, f"batchSummaries[{index}] references taskCoverage outside reviewed tasks")
            continue
        verdict_counts = Counter(item.get("reviewerVerdict") for item in batch_coverage if isinstance(item, dict))
        decision_counts = Counter(item.get("artifactPromotionDecision") for item in batch_coverage if isinstance(item, dict))
        if summary.get("taskCount") != len(batch.get("taskIds", [])):
            fail(errors, f"batchSummaries[{index}].taskCount must match protocol batch")
        if set(summary.get("domainIds", [])) != set(batch.get("domainIds", [])):
            fail(errors, f"batchSummaries[{index}].domainIds must match protocol batch")
        if summary.get("reviewerVerdictCounts") != dict(verdict_counts):
            fail(errors, f"batchSummaries[{index}].reviewerVerdictCounts must match taskCoverage")
        if summary.get("artifactPromotionDecisionCounts") != dict(decision_counts):
            fail(errors, f"batchSummaries[{index}].artifactPromotionDecisionCounts must match taskCoverage")
        if "blocked" not in str(summary.get("modelAdmissionDecision", "")):
            fail(errors, f"batchSummaries[{index}].modelAdmissionDecision must remain blocked")


def validate_index_links(verdict: dict[str, Any], errors: list[str]) -> None:
    index_requirements = require_string_list(verdict.get("indexRequirements"), "indexRequirements", errors, len(REQUIRED_INDEX_FILES))
    if sorted(index_requirements) != sorted(REQUIRED_INDEX_FILES):
        fail(errors, "indexRequirements must list the required index files")
    for relative_path in REQUIRED_INDEX_FILES:
        target = repo_path(relative_path, f"indexRequirements.{relative_path}", errors)
        if target and VERDICT_LINK not in target.read_text(encoding="utf-8"):
            fail(errors, f"{relative_path} must link {VERDICT_LINK}")


def main() -> int:
    errors: list[str] = []
    verdict = load_json(VERDICT_PATH, errors, "C2-LT-B1 independent fresh review verdict register")
    protocol = load_json(PROTOCOL_PATH, errors, "C2-LT-B1 independent fresh review protocol")
    # 保持本地复核账本存在；verdict 必须建立在其之后。
    load_json(LOCAL_REVIEW_PATH, errors, "C2-LT-B1 local review register")
    rows = extraction_rows(errors)
    batches = protocol_batches(protocol, errors)
    if verdict and protocol:
        validate_top_level(verdict, protocol, errors)
        reviewed_batches, remaining_batches = validate_scope(verdict, batches, errors)
        validate_reviews(verdict, reviewed_batches, rows, protocol, errors)
        validate_coverage(verdict, reviewed_batches, protocol, errors)
        validate_remaining_and_summaries(verdict, reviewed_batches, remaining_batches, errors)
        validate_index_links(verdict, errors)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    reviewed = verdict.get("scope", {}).get("reviewedExtractionTaskCount", 0)
    remaining = verdict.get("scope", {}).get("remainingExtractionTaskCount", 0)
    print(f"C2 longtail first-batch independent fresh review verdict audit ok: reviewed={reviewed} remaining={remaining}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
