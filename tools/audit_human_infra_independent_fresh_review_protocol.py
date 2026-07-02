#!/usr/bin/env python3
"""审计 Human Infra 独立 fresh review 协议与卡片晋升预注册账本的一致性。"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PROTOCOL_PATH = ROOT / "docs/reference/human-infra-independent-fresh-review-protocol.json"
PREP_PATH = ROOT / "docs/reference/human-infra-card-promotion-prep-register.json"

SCHEMA = "human-infra.independent-fresh-review-protocol.v1"
STATUS = "active-review-protocol-no-verdicts-yet"
PROTOCOL_LINK = "human-infra-independent-fresh-review-protocol.json"

SOURCE_OF_TRUTH_KEYS = {
    "cardPromotionPrepRegister",
    "sourceCardSystem",
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

REQUIRED_BATCH_IDS = {
    "FRB-01-method-statistical-model-standards",
    "FRB-02-biological-aging-mechanisms",
    "FRB-03-subject-continuity-capability-cognition",
    "FRB-04-digital-twin-ai-governance-future-waiting",
}

REQUIRED_INDEX_FILES = [
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


def load_prep(errors: list[str]) -> tuple[dict[str, Any], Counter[str]]:
    prep = load_json(PREP_PATH, errors, "card-promotion prep register")
    packets = prep.get("promotionPackets") if prep else None
    if not isinstance(packets, list):
        fail(errors, "card-promotion prep register promotionPackets must be a list")
        return prep, Counter()
    source_counts: Counter[str] = Counter()
    for index, packet in enumerate(packets):
        if not isinstance(packet, dict):
            fail(errors, f"promotionPackets[{index}] must be an object")
            continue
        source_id = require_string(packet.get("sourceCardId"), f"promotionPackets[{index}].sourceCardId", errors)
        if source_id:
            source_counts[source_id] += 1
    return prep, source_counts


def validate_source_of_truth(protocol: dict[str, Any], errors: list[str]) -> None:
    source = protocol.get("sourceOfTruth")
    if not isinstance(source, dict):
        fail(errors, "sourceOfTruth must be an object")
        return
    if set(source) != SOURCE_OF_TRUTH_KEYS:
        fail(errors, "sourceOfTruth must contain exactly the required keys")
    for key in SOURCE_OF_TRUTH_KEYS:
        value = require_string(source.get(key), f"sourceOfTruth.{key}", errors)
        if value:
            repo_path(value, f"sourceOfTruth.{key}", errors)


def validate_scope(protocol: dict[str, Any], prep: dict[str, Any], source_counts: Counter[str], errors: list[str]) -> None:
    scope = protocol.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return
    prep_scope = prep.get("scope", {}) if isinstance(prep.get("scope"), dict) else {}
    expected_packets = int(prep_scope.get("artifactPackCount", 0))
    expected_sources = len(source_counts)

    packet_count = require_int(scope.get("preparedPromotionPacketCount"), "scope.preparedPromotionPacketCount", errors)
    if packet_count is not None and packet_count != expected_packets:
        fail(errors, f"scope.preparedPromotionPacketCount must equal prep artifactPackCount={expected_packets}")

    source_count = require_int(scope.get("coveredSourceAnchorCount"), "scope.coveredSourceAnchorCount", errors)
    if source_count is not None and source_count != expected_sources:
        fail(errors, f"scope.coveredSourceAnchorCount must equal prep source count={expected_sources}")

    batch_count = require_int(scope.get("batchCount"), "scope.batchCount", errors)
    if batch_count is not None and batch_count != len(REQUIRED_BATCH_IDS):
        fail(errors, f"scope.batchCount must equal {len(REQUIRED_BATCH_IDS)}")

    reviewed = require_int(scope.get("currentReviewedPacketCount"), "scope.currentReviewedPacketCount", errors)
    if reviewed != 0:
        fail(errors, "scope.currentReviewedPacketCount must remain 0 until verdict artifacts exist")

    require_string(scope.get("selectionRule"), "scope.selectionRule", errors)
    non_claims = require_string_list(scope.get("nonClaims"), "scope.nonClaims", errors, 3)
    joined = " ".join(non_claims)
    for phrase in ["not an independent fresh review verdict", "does not complete", "does not authorize calibrated prediction"]:
        if phrase not in joined:
            fail(errors, f"scope.nonClaims must mention {phrase!r}")


def validate_contract(protocol: dict[str, Any], prep: dict[str, Any], errors: list[str]) -> None:
    fields = set(require_string_list(protocol.get("requiredReviewFields"), "requiredReviewFields", errors, len(REQUIRED_REVIEW_FIELDS)))
    if fields != REQUIRED_REVIEW_FIELDS:
        fail(errors, "requiredReviewFields must contain every required review field")

    artifact_contract = prep.get("artifactContract", {}) if isinstance(prep.get("artifactContract"), dict) else {}
    expected_verdicts = set(artifact_contract.get("requiredReviewerVerdicts", []))
    expected_blocked = set(artifact_contract.get("requiredBlockedUses", []))

    verdicts = set(require_string_list(protocol.get("verdictTaxonomy"), "verdictTaxonomy", errors, len(expected_verdicts)))
    if verdicts != expected_verdicts:
        fail(errors, "verdictTaxonomy must match card-promotion prep requiredReviewerVerdicts")

    blocked = set(require_string_list(protocol.get("blockedUses"), "blockedUses", errors, len(expected_blocked)))
    if blocked != expected_blocked:
        fail(errors, "blockedUses must match card-promotion prep requiredBlockedUses")

    rules = require_string_list(protocol.get("promotionRules"), "promotionRules", errors, 4)
    joined_rules = " ".join(rules)
    for verdict in ["support-with-boundary", "downgrade-required", "reject-source-context-mismatch", "cannot-evaluate-insufficient-context"]:
        if verdict not in joined_rules:
            fail(errors, f"promotionRules must mention {verdict}")


def validate_batches(protocol: dict[str, Any], source_counts: Counter[str], errors: list[str]) -> tuple[int, int]:
    batches = protocol.get("reviewBatches")
    if not isinstance(batches, list) or len(batches) != len(REQUIRED_BATCH_IDS):
        fail(errors, f"reviewBatches must contain {len(REQUIRED_BATCH_IDS)} batches")
        return 0, 0

    seen_batches: set[str] = set()
    batched_source_counts: Counter[str] = Counter()
    packet_total = 0
    for index, batch in enumerate(batches):
        if not isinstance(batch, dict):
            fail(errors, f"reviewBatches[{index}] must be an object")
            continue
        batch_id = require_string(batch.get("batchId"), f"reviewBatches[{index}].batchId", errors)
        if batch_id in seen_batches:
            fail(errors, f"duplicate batchId: {batch_id}")
        seen_batches.add(batch_id)
        for field in ["batchLabel", "reviewPriority", "reviewFocus"]:
            require_string(batch.get(field), f"{batch_id}.{field}", errors)
        packet_count = require_int(batch.get("packetCount"), f"{batch_id}.packetCount", errors)
        if packet_count is not None:
            packet_total += packet_count
        counts = batch.get("sourceAnchorCounts")
        if not isinstance(counts, dict) or not counts:
            fail(errors, f"{batch_id}.sourceAnchorCounts must be a non-empty object")
            continue
        source_total = 0
        for source_id, count in counts.items():
            if not isinstance(source_id, str) or not source_id:
                fail(errors, f"{batch_id}.sourceAnchorCounts has invalid source id")
                continue
            if source_id in batched_source_counts:
                fail(errors, f"source anchor appears in multiple batches: {source_id}")
            value = require_int(count, f"{batch_id}.sourceAnchorCounts.{source_id}", errors)
            if value is not None:
                source_total += value
                batched_source_counts[source_id] += value
        if packet_count is not None and source_total != packet_count:
            fail(errors, f"{batch_id}.packetCount must equal sum(sourceAnchorCounts)={source_total}")

    if seen_batches != REQUIRED_BATCH_IDS:
        fail(errors, "reviewBatches must contain exactly the required batch IDs")
    if batched_source_counts != source_counts:
        fail(errors, "reviewBatches sourceAnchorCounts must exactly match prep register source counts")
    return len(seen_batches), packet_total


def validate_index_requirements(protocol: dict[str, Any], errors: list[str]) -> None:
    index_requirements = require_string_list(protocol.get("indexRequirements"), "indexRequirements", errors, len(REQUIRED_INDEX_FILES))
    if sorted(index_requirements) != sorted(REQUIRED_INDEX_FILES):
        fail(errors, "indexRequirements must list the required index files")
    for relative_path in REQUIRED_INDEX_FILES:
        target = repo_path(relative_path, f"indexRequirements.{relative_path}", errors)
        if target and PROTOCOL_LINK not in target.read_text(encoding="utf-8"):
            fail(errors, f"{relative_path} must link {PROTOCOL_LINK}")


def validate_protocol(protocol: dict[str, Any], prep: dict[str, Any], source_counts: Counter[str], errors: list[str]) -> tuple[int, int]:
    if protocol.get("schemaVersion") != SCHEMA:
        fail(errors, f"schemaVersion must be {SCHEMA}")
    if protocol.get("status") != STATUS:
        fail(errors, f"status must be {STATUS}")
    require_string(protocol.get("registerId"), "registerId", errors)
    require_string(protocol.get("purpose"), "purpose", errors)
    validate_source_of_truth(protocol, errors)
    validate_scope(protocol, prep, source_counts, errors)
    validate_contract(protocol, prep, errors)
    batch_count, packet_total = validate_batches(protocol, source_counts, errors)
    validate_index_requirements(protocol, errors)
    return batch_count, packet_total


def main() -> int:
    errors: list[str] = []
    prep, source_counts = load_prep(errors)
    protocol = load_json(PROTOCOL_PATH, errors, "independent fresh review protocol")
    batch_count = packet_total = 0
    if protocol and prep:
        batch_count, packet_total = validate_protocol(protocol, prep, source_counts, errors)

    if errors:
        print("independent fresh review protocol audit failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"independent fresh review protocol audit ok: batches={batch_count} packets={packet_total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
