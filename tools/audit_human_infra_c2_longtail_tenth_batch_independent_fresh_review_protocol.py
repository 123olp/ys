#!/usr/bin/env python3
"""审计 C2 长尾第十批 independent fresh review 协议。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PROTOCOL_PATH = ROOT / "docs/reference/human-infra-c2-longtail-tenth-batch-independent-fresh-review-protocol.json"
LOCAL_REVIEW_PATH = ROOT / "docs/reference/human-infra-c2-longtail-tenth-batch-local-review-register.json"
EXTRACTION_PATH = ROOT / "docs/reference/human-infra-c2-longtail-tenth-batch-source-extraction-register.json"

SCHEMA = "human-infra.c2-longtail-tenth-batch-independent-fresh-review-protocol.v1"
STATUS = "active-review-protocol"
PROTOCOL_LINK = "human-infra-c2-longtail-tenth-batch-independent-fresh-review-protocol.json"
AUDIT_SCRIPT = "audit_human_infra_c2_longtail_tenth_batch_independent_fresh_review_protocol.py"
AUDIT_TARGET = "c2-longtail-tenth-batch-independent-fresh-review-protocol-audit"
EXPECTED_TASK_IDS = [f"C2LTB10-EXT-{index:03d}" for index in range(1, 25)]
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
    "adviceUseBoundaryVerdict",
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
    "medical-advice",
    "device-advice",
    "renal-dialysis-advice",
    "vision-rehabilitation-advice",
    "hearing-device-advice",
    "wound-care-advice",
    "burn-care-advice",
    "emergency-care-advice",
    "caregiver-advice",
    "nutrition-advice",
    "swallowing-advice",
}
REQUIRED_INDEX_FILES = [
    "docs/AGENTS.md",
    "docs/reference/README.md",
    "docs/reference/human-infra-maturity-roadmap.md",
    "docs/reference/human-infra-maturity-gap-register.json",
    "tools/README.md",
    "tools/AGENTS.md",
    "Makefile",
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
    local = load_json(LOCAL_REVIEW_PATH, errors, "C2-LT-B10 local review register")
    batches = local.get("reviewBatches") if local else None
    if not isinstance(batches, list):
        fail(errors, "local review register reviewBatches must be a list")
        return local, []
    source_resolution_count = local.get("scope", {}).get("sourceResolutionIssueCount") if isinstance(local.get("scope"), dict) else None
    if source_resolution_count != 0:
        fail(errors, "C2-LT-B10 local review must preserve sourceResolutionIssueCount=0 for this protocol")
    return local, [batch for batch in batches if isinstance(batch, dict)]


def extraction_domain_count(errors: list[str]) -> int:
    extraction = load_json(EXTRACTION_PATH, errors, "C2-LT-B10 source extraction register")
    rows = extraction.get("extractedRows") if extraction else None
    if not isinstance(rows, list):
        fail(errors, "source extraction register extractedRows must be a list")
        return 0
    task_ids = [row.get("taskId") for row in rows if isinstance(row, dict)]
    if task_ids != EXPECTED_TASK_IDS:
        fail(errors, "source extraction register rows must cover C2LTB10-EXT-001 through C2LTB10-EXT-024")
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
        fail(errors, "blockedUses must match required B10 blocked uses")
    rules = " ".join(require_string_list(protocol.get("promotionRules"), "promotionRules", errors, 5))
    for phrase in REQUIRED_VERDICTS | REQUIRED_DECISIONS:
        if phrase not in rules:
            fail(errors, f"promotionRules must mention {phrase}")
    for phrase in ["model admission", "advice", "clinical-validity"]:
        if phrase not in rules:
            fail(errors, f"promotionRules must preserve {phrase} boundary")


def validate_scope(protocol: dict[str, Any], domain_count: int, errors: list[str]) -> None:
    scope = protocol.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return
    expected_counts = {
        "localReviewedExtractionTaskCount": len(EXPECTED_TASK_IDS),
        "coveredDomainCount": domain_count,
        "batchCount": 2,
        "sourceResolutionIssueCount": 0,
        "protocolEmbeddedVerdictCount": 0,
    }
    for key, expected in expected_counts.items():
        value = require_int(scope.get(key), f"scope.{key}", errors)
        if value is not None and value != expected:
            fail(errors, f"scope.{key} must equal {expected}")
    selection_rule = require_string(scope.get("selectionRule"), "scope.selectionRule", errors)
    for phrase in ["independent fresh review", "advice-use", "model-admission"]:
        if phrase not in selection_rule:
            fail(errors, f"scope.selectionRule must mention {phrase}")
    non_claims = " ".join(require_string_list(scope.get("nonClaims"), "scope.nonClaims", errors, 3))
    for phrase in ["not an independent fresh review verdict register", "does not complete", "does not authorize calibrated prediction"]:
        if phrase not in non_claims:
            fail(errors, f"scope.nonClaims must mention {phrase!r}")
    for phrase in ["medical advice", "device advice", "renal dialysis advice", "swallowing advice"]:
        if phrase not in non_claims:
            fail(errors, f"scope.nonClaims must preserve B10 advice boundary: {phrase}")


def validate_batches(protocol: dict[str, Any], local_batches: list[dict[str, Any]], errors: list[str]) -> None:
    protocol_batches = protocol.get("reviewBatches")
    if not isinstance(protocol_batches, list) or len(protocol_batches) != len(local_batches):
        fail(errors, "reviewBatches must match local review batch count")
        return
    covered: list[str] = []
    for index, batch in enumerate(protocol_batches):
        context = f"reviewBatches[{index}]"
        if not isinstance(batch, dict):
            fail(errors, f"{context} must be an object")
            continue
        local = local_batches[index]
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
        focus = str(batch.get("reviewFocus", ""))
        for phrase in ["independent fresh review", "no", "advice", "artifact promotion"]:
            if phrase not in focus:
                fail(errors, f"{context}.reviewFocus must preserve {phrase} boundary")
        covered.extend(batch.get("taskIds", []))
    if covered != EXPECTED_TASK_IDS:
        fail(errors, "reviewBatches must cover C2LTB10-EXT-001 through C2LTB10-EXT-024 exactly once in order")


def validate_index_links(protocol: dict[str, Any], errors: list[str]) -> None:
    index_requirements = require_string_list(protocol.get("indexRequirements"), "indexRequirements", errors, len(REQUIRED_INDEX_FILES))
    if sorted(index_requirements) != sorted(REQUIRED_INDEX_FILES):
        fail(errors, "indexRequirements must list the required index files")
    for relative_path in REQUIRED_INDEX_FILES:
        target = repo_path(relative_path, f"indexRequirements.{relative_path}", errors)
        if not target:
            continue
        text = target.read_text(encoding="utf-8")
        if relative_path == "Makefile":
            if AUDIT_TARGET not in text:
                fail(errors, "Makefile must expose tenth-batch independent fresh review protocol audit target")
            if AUDIT_SCRIPT not in text:
                fail(errors, "Makefile must run tenth-batch independent fresh review protocol audit script")
        elif PROTOCOL_LINK not in text:
            fail(errors, f"{relative_path} must link {PROTOCOL_LINK}")


def main() -> int:
    errors: list[str] = []
    protocol = load_json(PROTOCOL_PATH, errors, "C2-LT-B10 independent fresh review protocol")
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
    print("C2 longtail tenth-batch independent fresh review protocol audit ok: tasks=24 batches=2 verdicts=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
