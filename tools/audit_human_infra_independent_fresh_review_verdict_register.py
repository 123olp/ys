#!/usr/bin/env python3
"""审计 Human Infra 独立 fresh review verdict register 的覆盖、边界和索引一致性。"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
VERDICT_PATH = ROOT / "docs/reference/human-infra-independent-fresh-review-verdict-register.json"
PROTOCOL_PATH = ROOT / "docs/reference/human-infra-independent-fresh-review-protocol.json"
PREP_PATH = ROOT / "docs/reference/human-infra-card-promotion-prep-register.json"
LOCAL_REVIEW_PATH = ROOT / "docs/reference/human-infra-source-context-local-review-register.json"
EXTRACTION_PATH = ROOT / "docs/reference/human-infra-domain-source-specific-extraction-register.json"

SCHEMA = "human-infra.independent-fresh-review-verdict-register.v1"
STATUS = "active-fresh-review-verdict-register-partial"
VERDICT_LINK = "human-infra-independent-fresh-review-verdict-register.json"

SOURCE_OF_TRUTH_KEYS = {
    "independentFreshReviewProtocol",
    "cardPromotionPrepRegister",
    "sourceContextLocalReviewRegister",
    "domainSourceSpecificExtractionRegister",
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

REQUIRED_INDEX_FILES = [
    "docs/reference/README.md",
    "docs/reference/human-infra-maturity-roadmap.md",
    "tools/README.md",
]

ALLOWED_ARTIFACT_PROMOTION_DECISIONS = {
    "eligible-for-bounded-artifact-fill",
    "downgrade-before-fill",
    "rejected-no-fill",
    "blocked-cannot-evaluate",
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


def get_protocol_batch(protocol: dict[str, Any], batch_id: str, errors: list[str]) -> dict[str, Any]:
    batches = protocol.get("reviewBatches")
    if not isinstance(batches, list):
        fail(errors, "protocol.reviewBatches must be a list")
        return {}
    matches = [batch for batch in batches if isinstance(batch, dict) and batch.get("batchId") == batch_id]
    if len(matches) != 1:
        fail(errors, f"protocol must contain exactly one batch {batch_id}")
        return {}
    return matches[0]


def validate_source_of_truth(register: dict[str, Any], errors: list[str]) -> None:
    source = register.get("sourceOfTruth")
    if not isinstance(source, dict):
        fail(errors, "sourceOfTruth must be an object")
        return
    if set(source) != SOURCE_OF_TRUTH_KEYS:
        fail(errors, "sourceOfTruth must contain exactly the required keys")
    for key in SOURCE_OF_TRUTH_KEYS:
        value = require_string(source.get(key), f"sourceOfTruth.{key}", errors)
        if value:
            repo_path(value, f"sourceOfTruth.{key}", errors)


def validate_scope(
    register: dict[str, Any],
    prep: dict[str, Any],
    batch: dict[str, Any],
    packet_count: int,
    errors: list[str],
) -> None:
    scope = register.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return
    batch_id = require_string(scope.get("reviewedBatchId"), "scope.reviewedBatchId", errors)
    if batch_id and batch_id != batch.get("batchId"):
        fail(errors, "scope.reviewedBatchId must match the reviewed protocol batch")

    prep_scope = prep.get("scope", {}) if isinstance(prep.get("scope"), dict) else {}
    total = require_int(scope.get("totalPreparedPromotionPacketCount"), "scope.totalPreparedPromotionPacketCount", errors)
    expected_total = int(prep_scope.get("artifactPackCount", 0))
    if total is not None and total != expected_total:
        fail(errors, f"scope.totalPreparedPromotionPacketCount must equal prep artifactPackCount={expected_total}")

    reviewed = require_int(scope.get("reviewedPromotionPacketCount"), "scope.reviewedPromotionPacketCount", errors)
    if reviewed is not None and reviewed != packet_count:
        fail(errors, f"scope.reviewedPromotionPacketCount must equal covered packet count={packet_count}")
    if reviewed is not None and reviewed != batch.get("packetCount"):
        fail(errors, "scope.reviewedPromotionPacketCount must match protocol batch packetCount")

    remaining = require_int(scope.get("remainingPreparedPromotionPacketCount"), "scope.remainingPreparedPromotionPacketCount", errors)
    if remaining is not None and total is not None and reviewed is not None and remaining != total - reviewed:
        fail(errors, "scope.remainingPreparedPromotionPacketCount must equal total-reviewed")

    reviewed_sources = require_int(scope.get("reviewedSourceAnchorCount"), "scope.reviewedSourceAnchorCount", errors)
    source_counts = batch.get("sourceAnchorCounts")
    if isinstance(source_counts, dict) and reviewed_sources is not None and reviewed_sources != len(source_counts):
        fail(errors, "scope.reviewedSourceAnchorCount must match protocol batch source count")

    require_string(scope.get("reviewMode"), "scope.reviewMode", errors)
    require_string(scope.get("artifactPromotionDecision"), "scope.artifactPromotionDecision", errors)
    non_claims = require_string_list(scope.get("nonClaims"), "scope.nonClaims", errors, 3)
    joined = " ".join(non_claims)
    for phrase in [
        "not a completed Source Card set",
        "does not authorize calibrated prediction",
        "remaining prepared packs still require fresh review",
    ]:
        if phrase not in joined:
            fail(errors, f"scope.nonClaims must mention {phrase!r}")


def validate_contract(register: dict[str, Any], prep: dict[str, Any], errors: list[str]) -> None:
    fields = set(require_string_list(register.get("requiredReviewFields"), "requiredReviewFields", errors, len(REQUIRED_REVIEW_FIELDS)))
    if fields != REQUIRED_REVIEW_FIELDS:
        fail(errors, "requiredReviewFields must contain exactly the required review fields")

    artifact_contract = prep.get("artifactContract", {}) if isinstance(prep.get("artifactContract"), dict) else {}
    expected_verdicts = set(artifact_contract.get("requiredReviewerVerdicts", []))
    verdicts = set(require_string_list(register.get("verdictTaxonomy"), "verdictTaxonomy", errors, len(expected_verdicts)))
    if verdicts != expected_verdicts:
        fail(errors, "verdictTaxonomy must match prep register requiredReviewerVerdicts")

    expected_blocked = set(artifact_contract.get("requiredBlockedUses", []))
    blocked = set(require_string_list(register.get("blockedUses"), "blockedUses", errors, len(expected_blocked)))
    if blocked != expected_blocked:
        fail(errors, "blockedUses must match prep register requiredBlockedUses")

    decisions = set(require_string_list(register.get("artifactPromotionDecisions"), "artifactPromotionDecisions", errors, len(ALLOWED_ARTIFACT_PROMOTION_DECISIONS)))
    if decisions != ALLOWED_ARTIFACT_PROMOTION_DECISIONS:
        fail(errors, "artifactPromotionDecisions must contain the allowed decision set")


def build_expected_packets(prep: dict[str, Any], source_ids: set[str], errors: list[str]) -> list[dict[str, Any]]:
    packets = prep.get("promotionPackets")
    if not isinstance(packets, list):
        fail(errors, "prep promotionPackets must be a list")
        return []
    result: list[dict[str, Any]] = []
    for index, packet in enumerate(packets):
        if not isinstance(packet, dict):
            fail(errors, f"prep promotionPackets[{index}] must be an object")
            continue
        if packet.get("sourceCardId") in source_ids:
            result.append(packet)
    return result


def validate_source_reviews(
    register: dict[str, Any],
    batch: dict[str, Any],
    local_review: dict[str, Any],
    extraction: dict[str, Any],
    prep: dict[str, Any],
    errors: list[str],
) -> tuple[set[str], Counter[str]]:
    source_counts = batch.get("sourceAnchorCounts")
    if not isinstance(source_counts, dict):
        fail(errors, "protocol batch sourceAnchorCounts must be an object")
        return set(), Counter()
    expected_source_ids = set(source_counts)
    local_by_source = {
        review.get("sourceCardId"): review
        for review in local_review.get("localReviews", [])
        if isinstance(review, dict)
    }
    extraction_rows = [
        row
        for row in extraction.get("completedRows", [])
        if isinstance(row, dict) and row.get("sourceCardId") in expected_source_ids
    ]
    extraction_by_source: dict[str, list[dict[str, Any]]] = {}
    for row in extraction_rows:
        extraction_by_source.setdefault(row["sourceCardId"], []).append(row)

    reviews = register.get("sourceAnchorFreshReviews")
    if not isinstance(reviews, list):
        fail(errors, "sourceAnchorFreshReviews must be a list")
        return set(), Counter()
    if len(reviews) != len(expected_source_ids):
        fail(errors, "sourceAnchorFreshReviews length must match reviewed batch source count")

    blocked_required = set(register.get("blockedUses", []))
    protocol_verdicts = set(register.get("verdictTaxonomy", []))
    seen_sources: set[str] = set()
    covered_task_ids: set[str] = set()
    source_packet_counts: Counter[str] = Counter()

    for index, review in enumerate(reviews):
        if not isinstance(review, dict):
            fail(errors, f"sourceAnchorFreshReviews[{index}] must be an object")
            continue
        source_id = require_string(review.get("sourceCardId"), f"sourceAnchorFreshReviews[{index}].sourceCardId", errors)
        if not source_id:
            continue
        if source_id not in expected_source_ids:
            fail(errors, f"sourceAnchorFreshReviews contains source outside reviewed batch: {source_id}")
        if source_id in seen_sources:
            fail(errors, f"duplicate sourceAnchorFreshReviews sourceCardId: {source_id}")
        seen_sources.add(source_id)

        local = local_by_source.get(source_id)
        if not local:
            fail(errors, f"source review lacks matching local source-context review: {source_id}")
        else:
            for field in ["reviewedSourceTitle", "sourceType"]:
                if review.get(field) != local.get(field):
                    fail(errors, f"{source_id}.{field} must match local source-context review")
            if set(review.get("blockedUses", [])) != set(local.get("blockedUses", [])):
                fail(errors, f"{source_id}.blockedUses must match local source-context review")

        rows = extraction_by_source.get(source_id, [])
        if not rows:
            fail(errors, f"source review lacks matching extraction rows: {source_id}")
        else:
            if review.get("registeredSourceRole") != rows[0].get("sourceRole"):
                fail(errors, f"{source_id}.registeredSourceRole must match extraction sourceRole")
            expected_claims = sorted({row.get("exactClaimUse") for row in rows if row.get("exactClaimUse")})
            if sorted(review.get("registeredExactClaimUses", [])) != expected_claims:
                fail(errors, f"{source_id}.registeredExactClaimUses must match extraction rows")
            expected_boundaries = sorted({row.get("transferBoundary") for row in rows if row.get("transferBoundary")})
            if sorted(review.get("registeredTransferBoundaries", [])) != expected_boundaries:
                fail(errors, f"{source_id}.registeredTransferBoundaries must match extraction rows")

        for field in REQUIRED_REVIEW_FIELDS:
            require_string(review.get(field), f"{source_id}.{field}", errors)
        verdict = require_string(review.get("reviewerVerdict"), f"{source_id}.reviewerVerdict", errors)
        if verdict and verdict not in protocol_verdicts:
            fail(errors, f"{source_id}.reviewerVerdict is not in verdictTaxonomy")
        decision = require_string(review.get("artifactPromotionDecision"), f"{source_id}.artifactPromotionDecision", errors)
        if decision and decision not in ALLOWED_ARTIFACT_PROMOTION_DECISIONS:
            fail(errors, f"{source_id}.artifactPromotionDecision is invalid")
        if set(review.get("blockedUses", [])) != blocked_required:
            fail(errors, f"{source_id}.blockedUses must match register blockedUses")

        evidence = review.get("freshReviewEvidence")
        if not isinstance(evidence, list) or not evidence:
            fail(errors, f"{source_id}.freshReviewEvidence must be a non-empty list")
        else:
            for e_index, item in enumerate(evidence):
                if not isinstance(item, dict):
                    fail(errors, f"{source_id}.freshReviewEvidence[{e_index}] must be an object")
                    continue
                url = require_string(item.get("url"), f"{source_id}.freshReviewEvidence[{e_index}].url", errors)
                if url and not url.startswith("https://"):
                    fail(errors, f"{source_id}.freshReviewEvidence[{e_index}].url must be https")
                require_string(item.get("evidenceType"), f"{source_id}.freshReviewEvidence[{e_index}].evidenceType", errors)
                require_string(item.get("finding"), f"{source_id}.freshReviewEvidence[{e_index}].finding", errors)

        affected_ids = set(require_string_list(review.get("affectedPromotionTaskIds"), f"{source_id}.affectedPromotionTaskIds", errors, 1))
        expected_packets = build_expected_packets(prep, {source_id}, errors)
        expected_ids = {packet.get("promotionTaskId") for packet in expected_packets}
        if affected_ids != expected_ids:
            fail(errors, f"{source_id}.affectedPromotionTaskIds must match prep promotion packets for that source")
        count = require_int(review.get("affectedPromotionTaskCount"), f"{source_id}.affectedPromotionTaskCount", errors)
        if count is not None and count != len(expected_ids):
            fail(errors, f"{source_id}.affectedPromotionTaskCount must equal affectedPromotionTaskIds length")
        covered_task_ids.update(affected_ids)
        source_packet_counts[source_id] = len(affected_ids)

    if seen_sources != expected_source_ids:
        fail(errors, "sourceAnchorFreshReviews must cover exactly the reviewed batch source anchors")
    return covered_task_ids, source_packet_counts


def validate_packet_coverage(
    register: dict[str, Any],
    expected_packets: list[dict[str, Any]],
    covered_task_ids: set[str],
    source_packet_counts: Counter[str],
    batch: dict[str, Any],
    errors: list[str],
) -> int:
    coverage = register.get("packetCoverage")
    if not isinstance(coverage, list):
        fail(errors, "packetCoverage must be a list")
        return 0
    expected_by_id = {packet["promotionTaskId"]: packet for packet in expected_packets if isinstance(packet.get("promotionTaskId"), str)}
    coverage_ids: set[str] = set()
    allowed_verdicts = set(register.get("verdictTaxonomy", []))
    for index, row in enumerate(coverage):
        if not isinstance(row, dict):
            fail(errors, f"packetCoverage[{index}] must be an object")
            continue
        task_id = require_string(row.get("promotionTaskId"), f"packetCoverage[{index}].promotionTaskId", errors)
        packet = expected_by_id.get(task_id)
        if not packet:
            fail(errors, f"packetCoverage[{index}] references unknown reviewed packet: {task_id}")
            continue
        coverage_ids.add(task_id)
        for field in ["domainId", "fieldCardId", "sourceCardId"]:
            if row.get(field) != packet.get(field):
                fail(errors, f"packetCoverage[{index}].{field} must match prep register")
        verdict = require_string(row.get("reviewerVerdict"), f"packetCoverage[{index}].reviewerVerdict", errors)
        if verdict and verdict not in allowed_verdicts:
            fail(errors, f"packetCoverage[{index}].reviewerVerdict is not in verdictTaxonomy")
        decision = require_string(row.get("artifactPromotionDecision"), f"packetCoverage[{index}].artifactPromotionDecision", errors)
        if decision and decision not in ALLOWED_ARTIFACT_PROMOTION_DECISIONS:
            fail(errors, f"packetCoverage[{index}].artifactPromotionDecision is invalid")
        model_decision = require_string(row.get("modelAdmissionDecision"), f"packetCoverage[{index}].modelAdmissionDecision", errors)
        if model_decision and "blocked" not in model_decision:
            fail(errors, f"packetCoverage[{index}].modelAdmissionDecision must remain blocked")
    expected_ids = set(expected_by_id)
    if coverage_ids != expected_ids:
        fail(errors, "packetCoverage must cover exactly the reviewed prep packets")
    if coverage_ids != covered_task_ids:
        fail(errors, "packetCoverage must match sourceAnchorFreshReviews affectedPromotionTaskIds")

    expected_source_counts = Counter(packet["sourceCardId"] for packet in expected_packets)
    if source_packet_counts != expected_source_counts:
        fail(errors, "sourceAnchorFreshReviews source packet counts must match prep reviewed packet counts")
    batch_counts = Counter(batch.get("sourceAnchorCounts", {}))
    if source_packet_counts != batch_counts:
        fail(errors, "sourceAnchorFreshReviews source packet counts must match protocol batch sourceAnchorCounts")
    return len(coverage_ids)


def validate_index_requirements(register: dict[str, Any], errors: list[str]) -> None:
    index_requirements = require_string_list(register.get("indexRequirements"), "indexRequirements", errors, len(REQUIRED_INDEX_FILES))
    if sorted(index_requirements) != sorted(REQUIRED_INDEX_FILES):
        fail(errors, "indexRequirements must list the required index files")
    for relative_path in REQUIRED_INDEX_FILES:
        target = repo_path(relative_path, f"indexRequirements.{relative_path}", errors)
        if target and VERDICT_LINK not in target.read_text(encoding="utf-8"):
            fail(errors, f"{relative_path} must link {VERDICT_LINK}")


def validate_register(
    register: dict[str, Any],
    protocol: dict[str, Any],
    prep: dict[str, Any],
    local_review: dict[str, Any],
    extraction: dict[str, Any],
    errors: list[str],
) -> tuple[int, int]:
    if register.get("schemaVersion") != SCHEMA:
        fail(errors, f"schemaVersion must be {SCHEMA}")
    if register.get("status") != STATUS:
        fail(errors, f"status must be {STATUS}")
    require_string(register.get("registerId"), "registerId", errors)
    require_string(register.get("purpose"), "purpose", errors)
    validate_source_of_truth(register, errors)
    validate_contract(register, prep, errors)

    scope = register.get("scope") if isinstance(register.get("scope"), dict) else {}
    batch_id = scope.get("reviewedBatchId", "")
    batch = get_protocol_batch(protocol, batch_id, errors)
    source_counts = batch.get("sourceAnchorCounts") if isinstance(batch.get("sourceAnchorCounts"), dict) else {}
    expected_packets = build_expected_packets(prep, set(source_counts), errors)
    validate_scope(register, prep, batch, len(expected_packets), errors)
    covered_task_ids, source_packet_counts = validate_source_reviews(register, batch, local_review, extraction, prep, errors)
    packet_count = validate_packet_coverage(register, expected_packets, covered_task_ids, source_packet_counts, batch, errors)
    validate_index_requirements(register, errors)
    return len(source_counts), packet_count


def main() -> int:
    errors: list[str] = []
    register = load_json(VERDICT_PATH, errors, "independent fresh review verdict register")
    protocol = load_json(PROTOCOL_PATH, errors, "independent fresh review protocol")
    prep = load_json(PREP_PATH, errors, "card-promotion prep register")
    local_review = load_json(LOCAL_REVIEW_PATH, errors, "source-context local review register")
    extraction = load_json(EXTRACTION_PATH, errors, "domain-source extraction register")
    source_count = packet_count = 0
    if register and protocol and prep and local_review and extraction:
        source_count, packet_count = validate_register(register, protocol, prep, local_review, extraction, errors)

    if errors:
        print("independent fresh review verdict register audit failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"independent fresh review verdict register audit ok: sources={source_count} packets={packet_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
