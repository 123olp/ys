#!/usr/bin/env python3
"""审计 C2-LT-B2 独立 fresh review 协议。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PROTOCOL_PATH = ROOT / "docs/reference/human-infra-c2-longtail-second-batch-independent-fresh-review-protocol.json"
LOCAL_REVIEW_PATH = ROOT / "docs/reference/human-infra-c2-longtail-second-batch-local-review-register.json"
EXTRACTION_PATH = ROOT / "docs/reference/human-infra-c2-longtail-second-batch-source-extraction-register.json"

SCHEMA = "human-infra.c2-longtail-second-batch-independent-fresh-review-protocol.v1"
STATUS = "active-review-protocol"
PROTOCOL_LINK = "human-infra-c2-longtail-second-batch-independent-fresh-review-protocol.json"
EXPECTED_TASK_IDS = [f"C2LTB2-EXT-{index:03d}" for index in range(1, 25)]
REQUIRED_SOURCE_OF_TRUTH = {
    "localReviewRegister",
    "sourceExtractionRegister",
    "sourceExtractionQueue",
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
REQUIRED_VERDICTS = {
    "support-with-boundary",
    "bounded-support",
    "downgrade-required",
    "reject-source-context-mismatch",
    "cannot-evaluate-insufficient-context",
}
REQUIRED_DECISIONS = {
    "eligible-for-bounded-artifact-fill",
    "downgrade-before-fill",
    "rejected-no-fill",
    "blocked-cannot-evaluate",
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


def local_review_batches(errors: list[str]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    local = load_json(LOCAL_REVIEW_PATH, errors, "C2-LT-B2 local review register")
    batches = local.get("reviewBatches") if local else None
    if not isinstance(batches, list):
        fail(errors, "local review register reviewBatches must be a list")
        return local, []
    return local, [batch for batch in batches if isinstance(batch, dict)]


def extraction_domain_count(errors: list[str]) -> int:
    extraction = load_json(EXTRACTION_PATH, errors, "C2-LT-B2 source extraction register")
    rows = extraction.get("extractedRows") if extraction else None
    if not isinstance(rows, list):
        fail(errors, "source extraction register extractedRows must be a list")
        return 0
    return len({row.get("domainId") for row in rows if isinstance(row, dict)})


def validate_top_level(protocol: dict[str, Any], errors: list[str]) -> None:
    if protocol.get("schemaVersion") != SCHEMA:
        fail(errors, f"schemaVersion must be {SCHEMA}")
    if protocol.get("status") != STATUS:
        fail(errors, f"status must be {STATUS}")
    require_string(protocol.get("registerId"), "registerId", errors)
    require_string(protocol.get("purpose"), "purpose", errors)

    source = protocol.get("sourceOfTruth")
    if not isinstance(source, dict):
        fail(errors, "sourceOfTruth must be an object")
    else:
        if set(source) != REQUIRED_SOURCE_OF_TRUTH:
            fail(errors, "sourceOfTruth must contain exactly the required keys")
        for key in REQUIRED_SOURCE_OF_TRUTH:
            value = require_string(source.get(key), f"sourceOfTruth.{key}", errors)
            if value:
                repo_path(value, f"sourceOfTruth.{key}", errors)

    if set(require_string_list(protocol.get("requiredReviewFields"), "requiredReviewFields", errors, len(REQUIRED_REVIEW_FIELDS))) != REQUIRED_REVIEW_FIELDS:
        fail(errors, "requiredReviewFields must match required review fields")
    if set(require_string_list(protocol.get("verdictTaxonomy"), "verdictTaxonomy", errors, len(REQUIRED_VERDICTS))) != REQUIRED_VERDICTS:
        fail(errors, "verdictTaxonomy must match required verdicts")
    if set(require_string_list(protocol.get("artifactPromotionDecisions"), "artifactPromotionDecisions", errors, len(REQUIRED_DECISIONS))) != REQUIRED_DECISIONS:
        fail(errors, "artifactPromotionDecisions must match required decisions")
    if set(require_string_list(protocol.get("blockedUses"), "blockedUses", errors, len(REQUIRED_BLOCKED_USES))) != REQUIRED_BLOCKED_USES:
        fail(errors, "blockedUses must match required blocked uses")
    rules = " ".join(require_string_list(protocol.get("promotionRules"), "promotionRules", errors, 4))
    for phrase in REQUIRED_VERDICTS | REQUIRED_DECISIONS:
        if phrase not in rules:
            fail(errors, f"promotionRules must mention {phrase}")


def validate_scope(protocol: dict[str, Any], domain_count: int, errors: list[str]) -> None:
    scope = protocol.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return
    expected_counts = {
        "localReviewedExtractionTaskCount": len(EXPECTED_TASK_IDS),
        "coveredDomainCount": domain_count,
        "batchCount": 2,
        "protocolEmbeddedVerdictCount": 0,
    }
    for key, expected in expected_counts.items():
        value = require_int(scope.get(key), f"scope.{key}", errors)
        if value is not None and value != expected:
            fail(errors, f"scope.{key} must equal {expected}")
    require_string(scope.get("selectionRule"), "scope.selectionRule", errors)
    non_claims = " ".join(require_string_list(scope.get("nonClaims"), "scope.nonClaims", errors, 3))
    for phrase in ["not an independent fresh review verdict register", "does not complete", "does not authorize calibrated prediction"]:
        if phrase not in non_claims:
            fail(errors, f"scope.nonClaims must mention {phrase!r}")


def validate_batches(protocol: dict[str, Any], local_batches: list[dict[str, Any]], errors: list[str]) -> None:
    protocol_batches = protocol.get("reviewBatches")
    if not isinstance(protocol_batches, list) or len(protocol_batches) != len(local_batches):
        fail(errors, "reviewBatches must match local review batch count")
        return
    covered: list[str] = []
    local_by_index = list(local_batches)
    for index, batch in enumerate(protocol_batches):
        context = f"reviewBatches[{index}]"
        if not isinstance(batch, dict):
            fail(errors, f"{context} must be an object")
            continue
        local = local_by_index[index]
        require_string(batch.get("batchId"), f"{context}.batchId", errors)
        if batch.get("sourceLocalReviewBatchId") != local.get("reviewBatchId"):
            fail(errors, f"{context}.sourceLocalReviewBatchId must match local review batch")
        if batch.get("taskIds") != local.get("taskIds"):
            fail(errors, f"{context}.taskIds must match local review batch")
        if set(batch.get("domainIds", [])) != set(local.get("domainIds", [])):
            fail(errors, f"{context}.domainIds must match local review batch")
        task_count = require_int(batch.get("taskCount"), f"{context}.taskCount", errors)
        if task_count is not None and task_count != len(local.get("taskIds", [])):
            fail(errors, f"{context}.taskCount must match local review task count")
        for field in ["batchLabel", "reviewPriority", "reviewFocus"]:
            require_string(batch.get(field), f"{context}.{field}", errors)
        covered.extend(batch.get("taskIds", []))
    if covered != EXPECTED_TASK_IDS:
        fail(errors, "reviewBatches must cover C2LTB2-EXT-001 through C2LTB2-EXT-024 exactly once in order")


def validate_index_links(protocol: dict[str, Any], errors: list[str]) -> None:
    index_requirements = require_string_list(protocol.get("indexRequirements"), "indexRequirements", errors, len(REQUIRED_INDEX_FILES))
    if sorted(index_requirements) != sorted(REQUIRED_INDEX_FILES):
        fail(errors, "indexRequirements must list the required index files")
    for relative_path in REQUIRED_INDEX_FILES:
        target = repo_path(relative_path, f"indexRequirements.{relative_path}", errors)
        if target and PROTOCOL_LINK not in target.read_text(encoding="utf-8"):
            fail(errors, f"{relative_path} must link {PROTOCOL_LINK}")


def main() -> int:
    errors: list[str] = []
    protocol = load_json(PROTOCOL_PATH, errors, "C2-LT-B2 independent fresh review protocol")
    _, local_batches = local_review_batches(errors)
    domain_count = extraction_domain_count(errors)
    if protocol:
        validate_top_level(protocol, errors)
        validate_scope(protocol, domain_count, errors)
        validate_batches(protocol, local_batches, errors)
        validate_index_links(protocol, errors)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("C2 longtail second-batch independent fresh review protocol audit ok: tasks=24 batches=2")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
