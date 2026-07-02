#!/usr/bin/env python3
"""审计 C2-LT-B3 独立 fresh review verdict 账本。"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
VERDICT_PATH = ROOT / "docs/reference/human-infra-c2-longtail-third-batch-independent-fresh-review-verdict-register.json"
PROTOCOL_PATH = ROOT / "docs/reference/human-infra-c2-longtail-third-batch-independent-fresh-review-protocol.json"
EXTRACTION_PATH = ROOT / "docs/reference/human-infra-c2-longtail-third-batch-source-extraction-register.json"
SOURCE_RESOLUTION_PATH = ROOT / "docs/reference/human-infra-c2-longtail-third-batch-source-resolution-register.json"

SCHEMA = "human-infra.c2-longtail-third-batch-independent-fresh-review-verdict-register.v1"
STATUS = "active-fresh-review-verdict-register-complete"
VERDICT_LINK = "human-infra-c2-longtail-third-batch-independent-fresh-review-verdict-register.json"
EXPECTED_TASK_IDS = [f"C2LTB3-EXT-{index:03d}" for index in range(1, 25)]
EXPECTED_SOURCE_RESOLUTION_IDS = {
    "C2LTB3-EXT-007",
    "C2LTB3-EXT-010",
    "C2LTB3-EXT-011",
    "C2LTB3-EXT-012",
    "C2LTB3-EXT-020",
}
EXPECTED_DOWNGRADE_IDS = {"C2LTB3-EXT-022"}
REQUIRED_SOURCE_OF_TRUTH = {
    "independentFreshReviewProtocol",
    "localReviewRegister",
    "sourceExtractionRegister",
    "sourceResolutionRegister",
    "evidencePolicy",
    "maturityGapRegister",
}
REQUIRED_REVIEW_FIELDS = {
    "sourceIdentityVerdict",
    "sourceResolutionVerdict",
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


def repo_path(relative_path: str, context: str, errors: list[str]) -> None:
    rel = require_string(relative_path, context, errors)
    if not rel:
        return
    if rel.startswith(("http://", "https://")):
        fail(errors, f"{context} must be a local path, not URL")
        return
    target = (ROOT / rel).resolve()
    try:
        target.relative_to(ROOT)
    except ValueError:
        fail(errors, f"{context} escapes repository: {rel}")
        return
    if not target.exists():
        fail(errors, f"{context} does not exist: {rel}")


def protocol_task_ids(protocol: dict[str, Any], errors: list[str]) -> list[str]:
    batches = protocol.get("reviewBatches")
    if not isinstance(batches, list):
        fail(errors, "protocol.reviewBatches must be a list")
        return []
    task_ids: list[str] = []
    for index, batch in enumerate(batches):
        if not isinstance(batch, dict):
            fail(errors, f"protocol.reviewBatches[{index}] must be an object")
            continue
        task_ids.extend(require_string_list(batch.get("taskIds"), f"protocol.reviewBatches[{index}].taskIds", errors))
    return task_ids


def extraction_rows(errors: list[str]) -> dict[str, dict[str, Any]]:
    extraction = load_json(EXTRACTION_PATH, errors, "C2-LT-B3 source extraction register")
    rows = extraction.get("extractedRows") if extraction else None
    if not isinstance(rows, list):
        fail(errors, "source extraction register extractedRows must be a list")
        return {}
    return {row.get("taskId"): row for row in rows if isinstance(row, dict) and isinstance(row.get("taskId"), str)}


def source_resolution_ids(errors: list[str]) -> set[str]:
    register = load_json(SOURCE_RESOLUTION_PATH, errors, "C2-LT-B3 source-resolution register")
    rows = register.get("resolutionRows") if register else None
    if not isinstance(rows, list):
        fail(errors, "source-resolution register resolutionRows must be a list")
        return set()
    result: set[str] = set()
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"resolutionRows[{index}] must be an object")
            continue
        task_id = require_string(row.get("taskId"), f"resolutionRows[{index}].taskId", errors)
        if task_id:
            result.add(task_id)
    return result


def validate_top_level(verdict: dict[str, Any], protocol: dict[str, Any], errors: list[str]) -> None:
    if verdict.get("schemaVersion") != SCHEMA:
        fail(errors, f"schemaVersion must be {SCHEMA}")
    if verdict.get("status") != STATUS:
        fail(errors, f"status must be {STATUS}")
    require_string(verdict.get("registerId"), "registerId", errors)
    require_string(verdict.get("purpose"), "purpose", errors)

    source = verdict.get("sourceOfTruth")
    if not isinstance(source, dict):
        fail(errors, "sourceOfTruth must be an object")
    else:
        if set(source) != REQUIRED_SOURCE_OF_TRUTH:
            fail(errors, "sourceOfTruth must contain exactly the required keys")
        for key in REQUIRED_SOURCE_OF_TRUTH:
            repo_path(source.get(key), f"sourceOfTruth.{key}", errors)

    if set(require_string_list(verdict.get("requiredReviewFields"), "requiredReviewFields", errors, len(REQUIRED_REVIEW_FIELDS))) != REQUIRED_REVIEW_FIELDS:
        fail(errors, "requiredReviewFields must match C2-LT-B3 protocol fields")
    if set(require_string_list(verdict.get("verdictTaxonomy"), "verdictTaxonomy", errors)) != set(protocol.get("verdictTaxonomy", [])):
        fail(errors, "verdictTaxonomy must match protocol verdictTaxonomy")
    if set(require_string_list(verdict.get("artifactPromotionDecisions"), "artifactPromotionDecisions", errors)) != set(protocol.get("artifactPromotionDecisions", [])):
        fail(errors, "artifactPromotionDecisions must match protocol artifactPromotionDecisions")
    if set(require_string_list(verdict.get("blockedUses"), "blockedUses", errors, len(REQUIRED_BLOCKED_USES))) != REQUIRED_BLOCKED_USES:
        fail(errors, "blockedUses must match required blocked uses")


def validate_scope(verdict: dict[str, Any], task_ids: list[str], issue_ids: set[str], errors: list[str]) -> None:
    scope = verdict.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return
    expected_counts = {
        "reviewedBatchCount": 2,
        "totalLocalReviewedExtractionTaskCount": len(EXPECTED_TASK_IDS),
        "reviewedExtractionTaskCount": len(EXPECTED_TASK_IDS),
        "remainingExtractionTaskCount": 0,
        "reviewedDomainCount": 12,
        "sourceResolutionIssueCount": len(EXPECTED_SOURCE_RESOLUTION_IDS),
        "sourceResolutionSupportedCount": len(EXPECTED_SOURCE_RESOLUTION_IDS),
        "boundedArtifactEligibleCount": 18,
        "correctedSourceReextractionEligibleCount": len(EXPECTED_SOURCE_RESOLUTION_IDS),
        "downgradeBeforeFillCount": len(EXPECTED_DOWNGRADE_IDS),
    }
    for key, expected in expected_counts.items():
        value = require_int(scope.get(key), f"scope.{key}", errors)
        if value is not None and value != expected:
            fail(errors, f"scope.{key} must equal {expected}")
    if task_ids != EXPECTED_TASK_IDS:
        fail(errors, "protocol task order must equal C2LTB3-EXT-001..024")
    if issue_ids != EXPECTED_SOURCE_RESOLUTION_IDS:
        fail(errors, "source-resolution issue IDs must match expected C2-LT-B3 issue rows")
    non_claims = " ".join(require_string_list(scope.get("nonClaims"), "scope.nonClaims", errors, 5))
    for phrase in [
        "not a completed Source Card set",
        "does not authorize calibrated prediction",
        "source-resolution-supported",
        "downgrade-required",
    ]:
        if phrase not in non_claims:
            fail(errors, f"scope.nonClaims must mention {phrase!r}")


def validate_reviews(
    verdict: dict[str, Any],
    task_ids: list[str],
    rows: dict[str, dict[str, Any]],
    protocol: dict[str, Any],
    errors: list[str],
) -> None:
    reviews = verdict.get("sourceTaskFreshReviews")
    if not isinstance(reviews, list):
        fail(errors, "sourceTaskFreshReviews must be a list")
        return
    if [review.get("taskId") for review in reviews if isinstance(review, dict)] != task_ids:
        fail(errors, "sourceTaskFreshReviews must cover protocol task IDs in order")

    allowed_verdicts = set(protocol.get("verdictTaxonomy", []))
    allowed_decisions = set(protocol.get("artifactPromotionDecisions", []))
    verdict_counts: Counter[str] = Counter()
    decision_counts: Counter[str] = Counter()

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
            fail(errors, f"{context}.domainId must match extraction register")
        if review.get("reviewedSourceTitle") != row.get("sourceTitle"):
            fail(errors, f"{context}.reviewedSourceTitle must match extraction register")
        if review.get("reviewedSourceUrl") != row.get("sourceUrl"):
            fail(errors, f"{context}.reviewedSourceUrl must match extraction register")

        for field in REQUIRED_REVIEW_FIELDS | {
            "freshReviewDate",
            "freshReviewMode",
            "registeredSourceRole",
            "registeredExactClaimUse",
            "registeredTransferBoundary",
            "modelAdmissionDecision",
        }:
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
        decision = require_string(review.get("artifactPromotionDecision"), f"{context}.artifactPromotionDecision", errors)
        if reviewer_verdict and reviewer_verdict not in allowed_verdicts:
            fail(errors, f"{context}.reviewerVerdict must be in protocol verdictTaxonomy")
        if decision and decision not in allowed_decisions:
            fail(errors, f"{context}.artifactPromotionDecision must be in protocol artifactPromotionDecisions")
        verdict_counts[reviewer_verdict] += 1
        decision_counts[decision] += 1

        if "blocked" not in str(review.get("blockedUseVerdict", "")):
            fail(errors, f"{context}.blockedUseVerdict must keep blocked uses blocked")
        if "blocked" not in str(review.get("modelPositionVerdict", "")):
            fail(errors, f"{context}.modelPositionVerdict must keep model admission blocked")
        if "blocked" not in str(review.get("modelAdmissionDecision", "")):
            fail(errors, f"{context}.modelAdmissionDecision must remain blocked")

        resolution_evidence = review.get("sourceResolutionEvidence")
        if task_id in EXPECTED_SOURCE_RESOLUTION_IDS:
            if reviewer_verdict != "source-resolution-supported":
                fail(errors, f"{context} is a source-resolution issue row and must be source-resolution-supported")
            if decision != "eligible-for-corrected-source-reextraction":
                fail(errors, f"{context} is a source-resolution issue row and must route to corrected-source re-extraction")
            if not isinstance(resolution_evidence, list) or not resolution_evidence:
                fail(errors, f"{context}.sourceResolutionEvidence must be non-empty for issue rows")
        elif resolution_evidence not in ([], None):
            fail(errors, f"{context}.sourceResolutionEvidence must be empty for non-issue rows")

        if task_id in EXPECTED_DOWNGRADE_IDS:
            if reviewer_verdict != "downgrade-required" or decision != "downgrade-before-fill":
                fail(errors, f"{context} must be downgrade-required / downgrade-before-fill")

    expected_verdict_counts = {
        "support-with-boundary": 12,
        "bounded-support": 6,
        "source-resolution-supported": 5,
        "downgrade-required": 1,
    }
    expected_decision_counts = {
        "eligible-for-bounded-artifact-fill": 18,
        "eligible-for-corrected-source-reextraction": 5,
        "downgrade-before-fill": 1,
    }
    if dict(verdict_counts) != expected_verdict_counts:
        fail(errors, f"reviewer verdict counts must equal {expected_verdict_counts}, got {dict(verdict_counts)}")
    if dict(decision_counts) != expected_decision_counts:
        fail(errors, f"artifact decision counts must equal {expected_decision_counts}, got {dict(decision_counts)}")


def validate_coverage(verdict: dict[str, Any], task_ids: list[str], protocol: dict[str, Any], errors: list[str]) -> None:
    coverage = verdict.get("taskCoverage")
    if not isinstance(coverage, list):
        fail(errors, "taskCoverage must be a list")
        return
    if [item.get("taskId") for item in coverage if isinstance(item, dict)] != task_ids:
        fail(errors, "taskCoverage must cover protocol task IDs in order")
    allowed_verdicts = set(protocol.get("verdictTaxonomy", []))
    allowed_decisions = set(protocol.get("artifactPromotionDecisions", []))
    for index, item in enumerate(coverage):
        if not isinstance(item, dict):
            fail(errors, f"taskCoverage[{index}] must be an object")
            continue
        if item.get("reviewerVerdict") not in allowed_verdicts:
            fail(errors, f"taskCoverage[{index}].reviewerVerdict must be in protocol taxonomy")
        if item.get("artifactPromotionDecision") not in allowed_decisions:
            fail(errors, f"taskCoverage[{index}].artifactPromotionDecision must be in protocol decisions")
        if "blocked" not in str(item.get("modelAdmissionDecision", "")):
            fail(errors, f"taskCoverage[{index}].modelAdmissionDecision must remain blocked")


def validate_summary(verdict: dict[str, Any], errors: list[str]) -> None:
    if verdict.get("remainingFreshReviewBatches") != []:
        fail(errors, "remainingFreshReviewBatches must be empty for complete C2-LT-B3 verdict register")
    summary = verdict.get("summary")
    if not isinstance(summary, dict):
        fail(errors, "summary must be an object")
        return
    if summary.get("reviewerVerdictCounts") != {
        "support-with-boundary": 12,
        "bounded-support": 6,
        "source-resolution-supported": 5,
        "downgrade-required": 1,
    }:
        fail(errors, "summary.reviewerVerdictCounts must match expected counts")
    if summary.get("artifactPromotionDecisionCounts") != {
        "eligible-for-bounded-artifact-fill": 18,
        "eligible-for-corrected-source-reextraction": 5,
        "downgrade-before-fill": 1,
    }:
        fail(errors, "summary.artifactPromotionDecisionCounts must match expected counts")
    next_step = require_string(summary.get("nextRequiredStep"), "summary.nextRequiredStep", errors)
    for phrase in ["corrected-source re-extraction", "downgrade-before-fill", "bounded reviewed artifacts"]:
        if phrase not in next_step:
            fail(errors, f"summary.nextRequiredStep must mention {phrase!r}")


def validate_index_links(errors: list[str]) -> None:
    for relative_path in REQUIRED_INDEX_FILES:
        path = ROOT / relative_path
        if not path.exists():
            fail(errors, f"missing index: {relative_path}")
            continue
        if VERDICT_LINK not in path.read_text(encoding="utf-8"):
            fail(errors, f"{relative_path} must link {VERDICT_LINK}")


def main() -> int:
    errors: list[str] = []
    verdict = load_json(VERDICT_PATH, errors, "C2-LT-B3 independent fresh review verdict register")
    protocol = load_json(PROTOCOL_PATH, errors, "C2-LT-B3 independent fresh review protocol")
    rows = extraction_rows(errors)
    issue_ids = source_resolution_ids(errors)
    task_ids = protocol_task_ids(protocol, errors)

    if verdict and protocol:
        validate_top_level(verdict, protocol, errors)
        validate_scope(verdict, task_ids, issue_ids, errors)
        validate_reviews(verdict, task_ids, rows, protocol, errors)
        validate_coverage(verdict, task_ids, protocol, errors)
        validate_summary(verdict, errors)
    validate_index_links(errors)

    if errors:
        print("C2-LT-B3 independent fresh review verdict audit failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(
        "C2-LT-B3 independent fresh review verdict audit ok: "
        "reviewed=24 bounded_artifact=18 corrected_reextraction=5 downgrade=1"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
