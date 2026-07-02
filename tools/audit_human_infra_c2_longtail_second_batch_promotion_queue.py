#!/usr/bin/env python3
"""审计 C2 长尾第二批研究域晋升队列。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
QUEUE_PATH = ROOT / "docs/reference/human-infra-c2-longtail-second-batch-promotion-queue.json"
COVERAGE_PATH = ROOT / "docs/reference/human-infra-c2-longtail-coverage-register.json"
FIRST_BATCH_PATH = ROOT / "docs/reference/human-infra-c2-longtail-first-batch-promotion-queue.json"

SCHEMA = "human-infra.c2-longtail-second-batch-promotion-queue.v1"
STATUS = "active-second-batch-queue-model-blocked"
EXPECTED_BATCH_ID = "C2-LT-B2"
EXPECTED_COVERAGE_STATUS = "c2-longtail-uncovered"
REGISTER_LINK = "human-infra-c2-longtail-second-batch-promotion-queue.json"
SCRIPT_LINK = "audit_human_infra_c2_longtail_second_batch_promotion_queue.py"

SOURCE_OF_TRUTH_KEYS = {
    "c2LongtailCoverageRegister",
    "firstBatchPromotionQueue",
    "domainClassification",
    "sourceCardSystem",
    "maturityGapRegister",
    "maturityRoadmap",
}

REQUIRED_ARTIFACTS = {
    "domain-claim-evidence-row",
    "domain-source-card-field-extraction",
    "domain-source-specific-deep-read",
    "source-context-local-review",
    "independent-fresh-review-verdict",
    "reviewed-source-card",
    "variable-card",
    "endpoint-card",
    "uncertainty-card",
    "transfer-boundary-card",
    "downgrade-check",
}

REQUIRED_BLOCKED_USES = {
    "calibrated-prediction",
    "individual-advice",
    "individual-death-date-output",
    "intervention-ranking",
    "clinical-validity-claim",
    "domain-claim-upgrade",
}

REQUIRED_PROMOTION_STEPS = {
    "create-domain-claim-evidence-row",
    "extract-domain-source-card-fields",
    "run-source-specific-deep-read",
    "perform-local-source-context-review",
    "send-through-independent-fresh-review",
    "promote-reviewed-source-variable-endpoint-uncertainty-transfer-downgrade-cards",
}

REQUIRED_SOURCE_EXTRACTION_FIELDS = {
    "exact-claim-or-recommendation",
    "endpoint-definition",
    "population-or-setting-boundary",
    "effect-or-mechanism-signal",
    "uncertainty-bias-transfer-boundary",
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


def load_json(path: Path, errors: list[str], label: str) -> dict[str, Any]:
    if not path.exists():
        fail(errors, f"missing {label}: {path.relative_to(ROOT)}")
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(errors, f"invalid JSON in {label}: {exc}")
        return {}
    if not isinstance(data, dict):
        fail(errors, f"{label} must be a JSON object")
        return {}
    return data


def require_string(value: Any, path: str, errors: list[str]) -> str:
    if not isinstance(value, str) or not value.strip():
        fail(errors, f"{path} must be a non-empty string")
        return ""
    return value


def require_int(value: Any, path: str, errors: list[str]) -> int | None:
    if not isinstance(value, int):
        fail(errors, f"{path} must be integer")
        return None
    return value


def require_list(value: Any, path: str, errors: list[str]) -> list[Any]:
    if not isinstance(value, list):
        fail(errors, f"{path} must be a list")
        return []
    return value


def repo_path(relative_path: str, path: str, errors: list[str]) -> Path | None:
    rel = require_string(relative_path, path, errors)
    if not rel:
        return None
    if rel.startswith(("http://", "https://")):
        fail(errors, f"{path} must be a repository-local path")
        return None
    target = (ROOT / rel).resolve()
    try:
        target.relative_to(ROOT)
    except ValueError:
        fail(errors, f"{path} escapes repository: {rel}")
        return None
    if not target.exists():
        fail(errors, f"{path} does not exist: {rel}")
        return None
    return target


def validate_source_of_truth(data: dict[str, Any], errors: list[str]) -> None:
    source = data.get("sourceOfTruth")
    if not isinstance(source, dict) or not source:
        fail(errors, "sourceOfTruth must be a non-empty object")
        return
    if set(source) != SOURCE_OF_TRUTH_KEYS:
        fail(errors, "sourceOfTruth must contain exactly the required keys")
    for key in SOURCE_OF_TRUTH_KEYS:
        repo_path(source.get(key), f"sourceOfTruth.{key}", errors)


def validate_scope(data: dict[str, Any], row_count: int, errors: list[str]) -> None:
    scope = data.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return
    if scope.get("batchId") != EXPECTED_BATCH_ID:
        fail(errors, f"scope.batchId must be {EXPECTED_BATCH_ID}")
    count = require_int(scope.get("batchDomainCount"), "scope.batchDomainCount", errors)
    if count != row_count:
        fail(errors, f"scope.batchDomainCount must equal batchRows count {row_count}")
    require_string(scope.get("selectionRule"), "scope.selectionRule", errors)
    if set(require_list(scope.get("requiredArtifactClasses"), "scope.requiredArtifactClasses", errors)) != REQUIRED_ARTIFACTS:
        fail(errors, f"scope.requiredArtifactClasses must be {sorted(REQUIRED_ARTIFACTS)}")
    non_claims = require_list(scope.get("nonClaims"), "scope.nonClaims", errors)
    if len(non_claims) < 5:
        fail(errors, "scope.nonClaims must contain at least 5 non-claims")
    joined = " ".join(str(item) for item in non_claims)
    for phrase in [
        "does not complete Source Cards",
        "does not complete independent fresh review",
        "does not admit any domain into calibrated prediction",
        "does not mark C2-LT-B1 corrected blocked rows as resolved",
    ]:
        if phrase not in joined:
            fail(errors, f"scope.nonClaims must include phrase: {phrase}")


def validate_candidate_source(ref: Any, path: str, seen_refs: set[str], errors: list[str]) -> None:
    if not isinstance(ref, dict):
        fail(errors, f"{path} must be an object")
        return
    source_ref_id = require_string(ref.get("sourceRefId"), f"{path}.sourceRefId", errors)
    if source_ref_id:
        if source_ref_id in seen_refs:
            fail(errors, f"duplicate sourceRefId: {source_ref_id}")
        seen_refs.add(source_ref_id)
        if not source_ref_id.startswith("C2LTB2-SRC-"):
            fail(errors, f"{path}.sourceRefId must start with C2LTB2-SRC-")
    require_string(ref.get("title"), f"{path}.title", errors)
    url = require_string(ref.get("url"), f"{path}.url", errors)
    if url and not url.startswith(("https://", "http://")):
        fail(errors, f"{path}.url must be URL")
    role = require_string(ref.get("evidenceRole"), f"{path}.evidenceRole", errors)
    if role and not role.endswith("-candidate"):
        fail(errors, f"{path}.evidenceRole must end with -candidate")
    fields = set(require_list(ref.get("requiredExtraction"), f"{path}.requiredExtraction", errors))
    if fields != REQUIRED_SOURCE_EXTRACTION_FIELDS:
        fail(errors, f"{path}.requiredExtraction must be {sorted(REQUIRED_SOURCE_EXTRACTION_FIELDS)}")
    if ref.get("reviewStatus") != "candidate-not-yet-source-carded":
        fail(errors, f"{path}.reviewStatus must remain candidate-not-yet-source-carded")
    if ref.get("selectionTrace") != "web-checked-source-candidate-2026-07-02":
        fail(errors, f"{path}.selectionTrace must record the web-checked source candidate date")


def validate_row(
    row: Any,
    index: int,
    coverage_by_domain: dict[str, dict[str, Any]],
    first_batch_domains: set[str],
    seen_domains: set[str],
    seen_refs: set[str],
    errors: list[str],
) -> None:
    path = f"batchRows[{index}]"
    if not isinstance(row, dict):
        fail(errors, f"{path} must be an object")
        return

    if row.get("batchId") != EXPECTED_BATCH_ID:
        fail(errors, f"{path}.batchId must be {EXPECTED_BATCH_ID}")
    rank = require_int(row.get("priorityRank"), f"{path}.priorityRank", errors)
    if rank is not None and rank != index + 1:
        fail(errors, f"{path}.priorityRank must be {index + 1}")

    domain_id = require_string(row.get("domainId"), f"{path}.domainId", errors)
    if not domain_id:
        return
    if domain_id in seen_domains:
        fail(errors, f"duplicate queued domain: {domain_id}")
    seen_domains.add(domain_id)
    if domain_id in first_batch_domains:
        fail(errors, f"{domain_id} must not duplicate C2-LT-B1")

    coverage = coverage_by_domain.get(domain_id)
    if coverage is None:
        fail(errors, f"{path}.domainId not found in C2 coverage register: {domain_id}")
        return
    if coverage.get("coverageStatus") != EXPECTED_COVERAGE_STATUS:
        fail(errors, f"{domain_id} must be {EXPECTED_COVERAGE_STATUS}")
    if row.get("triageBucket") != coverage.get("triageBucket"):
        fail(errors, f"{domain_id}.triageBucket does not match coverage register")
    if row.get("localDomainPath") != coverage.get("physicalPath"):
        fail(errors, f"{domain_id}.localDomainPath does not match coverage register")
    domain_dir = repo_path(row.get("localDomainPath"), f"{path}.localDomainPath", errors)
    if domain_dir is not None:
        for filename in ["README.md", "AGENTS.md"]:
            if not (domain_dir / filename).exists():
                fail(errors, f"{domain_id} missing {filename}")

    require_string(row.get("selectionReason"), f"{path}.selectionReason", errors)
    require_string(row.get("claimSeed"), f"{path}.claimSeed", errors)
    variables = require_list(row.get("variableSeed"), f"{path}.variableSeed", errors)
    if len(variables) < 4:
        fail(errors, f"{path}.variableSeed must contain at least 4 variables")

    refs = require_list(row.get("candidateSourceRefs"), f"{path}.candidateSourceRefs", errors)
    if len(refs) < 2:
        fail(errors, f"{path}.candidateSourceRefs must contain at least 2 candidate sources")
    for ref_index, ref in enumerate(refs):
        validate_candidate_source(ref, f"{path}.candidateSourceRefs[{ref_index}]", seen_refs, errors)

    if set(require_list(row.get("requiredArtifactClasses"), f"{path}.requiredArtifactClasses", errors)) != REQUIRED_ARTIFACTS:
        fail(errors, f"{domain_id}.requiredArtifactClasses must be {sorted(REQUIRED_ARTIFACTS)}")
    if set(require_list(row.get("promotionSteps"), f"{path}.promotionSteps", errors)) != REQUIRED_PROMOTION_STEPS:
        fail(errors, f"{domain_id}.promotionSteps must be {sorted(REQUIRED_PROMOTION_STEPS)}")
    if set(require_list(row.get("blockedUses"), f"{path}.blockedUses", errors)) != REQUIRED_BLOCKED_USES:
        fail(errors, f"{domain_id}.blockedUses must be {sorted(REQUIRED_BLOCKED_USES)}")
    decision = require_string(row.get("modelAdmissionDecision"), f"{path}.modelAdmissionDecision", errors)
    if decision and "blocked" not in decision:
        fail(errors, f"{domain_id}.modelAdmissionDecision must contain blocked")
    require_string(row.get("nextAction"), f"{path}.nextAction", errors)


def validate_indexes(errors: list[str]) -> None:
    for relative_path in REQUIRED_INDEX_FILES:
        target = repo_path(relative_path, f"index file {relative_path}", errors)
        if not target:
            continue
        text = target.read_text(encoding="utf-8")
        if REGISTER_LINK not in text:
            fail(errors, f"{relative_path} must reference {REGISTER_LINK}")
    for relative_path in ["Makefile", "tools/README.md", "tools/AGENTS.md"]:
        target = repo_path(relative_path, f"script index {relative_path}", errors)
        if target and SCRIPT_LINK not in target.read_text(encoding="utf-8"):
            fail(errors, f"{relative_path} must reference {SCRIPT_LINK}")


def validate_summary(data: dict[str, Any], rows: list[Any], errors: list[str]) -> None:
    summary = data.get("summary")
    if not isinstance(summary, dict):
        fail(errors, "summary must be an object")
        return
    valid_rows = [row for row in rows if isinstance(row, dict)]
    if summary.get("batchId") != EXPECTED_BATCH_ID:
        fail(errors, "summary.batchId must be C2-LT-B2")
    if summary.get("batchDomainCount") != len(valid_rows):
        fail(errors, "summary.batchDomainCount must match batchRows")
    source_count = sum(len(row.get("candidateSourceRefs", [])) for row in valid_rows)
    if summary.get("candidateSourceCount") != source_count:
        fail(errors, "summary.candidateSourceCount must match candidate sources")
    if summary.get("selectedDomainIds") != [row.get("domainId") for row in valid_rows]:
        fail(errors, "summary.selectedDomainIds must preserve batch row order")
    if "blocked" not in str(summary.get("modelAdmissionDecision", "")):
        fail(errors, "summary.modelAdmissionDecision must remain blocked")
    require_string(summary.get("nextWorkOrder"), "summary.nextWorkOrder", errors)


def main() -> int:
    errors: list[str] = []
    queue = load_json(QUEUE_PATH, errors, "C2 longtail second-batch queue")
    coverage = load_json(COVERAGE_PATH, errors, "C2 longtail coverage register")
    first_batch = load_json(FIRST_BATCH_PATH, errors, "C2 longtail first-batch queue")

    if queue:
        if queue.get("schemaVersion") != SCHEMA:
            fail(errors, f"schemaVersion must be {SCHEMA}")
        if queue.get("status") != STATUS:
            fail(errors, f"status must be {STATUS}")
        require_string(queue.get("queueId"), "queueId", errors)
        require_string(queue.get("purpose"), "purpose", errors)
        validate_source_of_truth(queue, errors)
        if set(require_list(queue.get("blockedUses"), "blockedUses", errors)) != REQUIRED_BLOCKED_USES:
            fail(errors, f"blockedUses must be {sorted(REQUIRED_BLOCKED_USES)}")

    coverage_rows = coverage.get("coverageRows") if coverage else None
    if not isinstance(coverage_rows, list):
        fail(errors, "coverage register coverageRows must be a list")
        coverage_rows = []
    coverage_by_domain = {
        row.get("domainId"): row
        for row in coverage_rows
        if isinstance(row, dict) and isinstance(row.get("domainId"), str)
    }

    first_rows = first_batch.get("batchRows") if first_batch else []
    if not isinstance(first_rows, list):
        fail(errors, "first batch queue batchRows must be a list")
        first_rows = []
    first_batch_domains = {row.get("domainId") for row in first_rows if isinstance(row, dict)}

    rows = queue.get("batchRows") if queue else []
    if not isinstance(rows, list):
        fail(errors, "batchRows must be a list")
        rows = []
    validate_scope(queue, len(rows), errors)

    seen_domains: set[str] = set()
    seen_refs: set[str] = set()
    for index, row in enumerate(rows):
        validate_row(row, index, coverage_by_domain, first_batch_domains, seen_domains, seen_refs, errors)
    validate_indexes(errors)
    validate_summary(queue, rows, errors)

    if errors:
        print("C2 longtail second-batch promotion queue audit failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(
        "C2 longtail second-batch promotion queue audit ok: "
        f"batch=C2-LT-B2 domains={len(seen_domains)} candidate_sources={len(seen_refs)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
