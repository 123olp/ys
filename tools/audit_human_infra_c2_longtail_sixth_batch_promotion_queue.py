#!/usr/bin/env python3
"""审计 C2 长尾第六批研究域晋升队列。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
QUEUE_PATH = ROOT / "docs/reference/human-infra-c2-longtail-sixth-batch-promotion-queue.json"
COVERAGE_PATH = ROOT / "docs/reference/human-infra-c2-longtail-coverage-register.json"
PREVIOUS_BATCHES = [
    ROOT / "docs/reference/human-infra-c2-longtail-first-batch-promotion-queue.json",
    ROOT / "docs/reference/human-infra-c2-longtail-second-batch-promotion-queue.json",
    ROOT / "docs/reference/human-infra-c2-longtail-third-batch-promotion-queue.json",
    ROOT / "docs/reference/human-infra-c2-longtail-fourth-batch-promotion-queue.json",
    ROOT / "docs/reference/human-infra-c2-longtail-fifth-batch-promotion-queue.json",
]

SCHEMA = "human-infra.c2-longtail-sixth-batch-promotion-queue.v1"
STATUS = "active-sixth-batch-queue-model-blocked"
BATCH_ID = "C2-LT-B6"
EXPECTED_COVERAGE_STATUS = "c2-longtail-uncovered"
REGISTER_LINK = "human-infra-c2-longtail-sixth-batch-promotion-queue.json"
SCRIPT_LINK = "audit_human_infra_c2_longtail_sixth_batch_promotion_queue.py"

REQUIRED_SOURCE_OF_TRUTH = {
    "c2LongtailCoverageRegister",
    "firstBatchPromotionQueue",
    "secondBatchPromotionQueue",
    "thirdBatchPromotionQueue",
    "fourthBatchPromotionQueue",
    "fifthBatchPromotionQueue",
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
REQUIRED_EXTRACTION_FIELDS = {
    "exact-claim-or-recommendation",
    "endpoint-definition",
    "population-or-setting-boundary",
    "effect-or-mechanism-signal",
    "uncertainty-bias-transfer-boundary",
}
REQUIRED_INDEX_LINKS = {
    "README.md": REGISTER_LINK,
    "docs/AGENTS.md": REGISTER_LINK,
    "docs/reference/README.md": REGISTER_LINK,
    "docs/reference/human-infra-maturity-roadmap.md": REGISTER_LINK,
    "docs/reference/human-infra-maturity-gap-register.json": REGISTER_LINK,
    "Makefile": "c2-longtail-sixth-batch-promotion-audit",
    "tools/README.md": SCRIPT_LINK,
    "tools/AGENTS.md": SCRIPT_LINK,
}


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


def require_string(value: Any, context: str, errors: list[str]) -> str:
    if not isinstance(value, str) or not value.strip():
        fail(errors, f"{context} must be a non-empty string")
        return ""
    return value


def require_int(value: Any, context: str, errors: list[str]) -> int | None:
    if not isinstance(value, int):
        fail(errors, f"{context} must be integer")
        return None
    return value


def require_list(value: Any, context: str, errors: list[str]) -> list[Any]:
    if not isinstance(value, list):
        fail(errors, f"{context} must be a list")
        return []
    return value


def repo_path(relative_path: str, context: str, errors: list[str]) -> Path | None:
    rel = require_string(relative_path, context, errors)
    if not rel:
        return None
    if rel.startswith(("http://", "https://")):
        fail(errors, f"{context} must be repository-local path, not URL")
        return None
    target = (ROOT / rel).resolve()
    try:
        target.relative_to(ROOT)
    except ValueError:
        fail(errors, f"{context} escapes repository: {rel}")
        return None
    if not target.exists():
        fail(errors, f"{context} does not exist: {rel}")
        return None
    return target


def previous_domains(errors: list[str]) -> set[str]:
    domains: set[str] = set()
    for path in PREVIOUS_BATCHES:
        data = load_json(path, errors, path.name)
        for row in data.get("batchRows", []):
            if isinstance(row, dict) and isinstance(row.get("domainId"), str):
                domains.add(row["domainId"])
    return domains


def coverage_by_domain(errors: list[str]) -> dict[str, dict[str, Any]]:
    data = load_json(COVERAGE_PATH, errors, "C2 coverage register")
    rows = data.get("coverageRows")
    if not isinstance(rows, list):
        fail(errors, "coverageRows must be a list")
        return {}
    result: dict[str, dict[str, Any]] = {}
    for row in rows:
        if isinstance(row, dict) and isinstance(row.get("domainId"), str):
            result[row["domainId"]] = row
    return result


def validate_source_of_truth(data: dict[str, Any], errors: list[str]) -> None:
    source = data.get("sourceOfTruth")
    if not isinstance(source, dict):
        fail(errors, "sourceOfTruth must be an object")
        return
    if set(source) != REQUIRED_SOURCE_OF_TRUTH:
        fail(errors, "sourceOfTruth must contain exactly the required keys")
    for key in REQUIRED_SOURCE_OF_TRUTH:
        repo_path(source.get(key), f"sourceOfTruth.{key}", errors)


def validate_scope(data: dict[str, Any], row_count: int, errors: list[str]) -> None:
    scope = data.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return
    if scope.get("batchId") != BATCH_ID:
        fail(errors, f"scope.batchId must be {BATCH_ID}")
    if require_int(scope.get("batchDomainCount"), "scope.batchDomainCount", errors) != row_count:
        fail(errors, "scope.batchDomainCount must match batchRows length")
    if set(require_list(scope.get("requiredArtifactClasses"), "scope.requiredArtifactClasses", errors)) != REQUIRED_ARTIFACTS:
        fail(errors, "scope.requiredArtifactClasses must match the Source Card promotion artifact set")
    non_claims = " ".join(str(item) for item in require_list(scope.get("nonClaims"), "scope.nonClaims", errors))
    for phrase in [
        "does not complete Source Cards",
        "does not complete independent fresh review",
        "does not admit any domain into calibrated prediction",
        "does not mark any C2-LT-B1/B2/B3/B4/B5",
    ]:
        if phrase not in non_claims:
            fail(errors, f"scope.nonClaims missing phrase: {phrase}")


def validate_candidate_source(ref: Any, context: str, seen_refs: set[str], errors: list[str]) -> None:
    if not isinstance(ref, dict):
        fail(errors, f"{context} must be an object")
        return
    source_id = require_string(ref.get("sourceRefId"), f"{context}.sourceRefId", errors)
    if source_id:
        if source_id in seen_refs:
            fail(errors, f"duplicate sourceRefId: {source_id}")
        seen_refs.add(source_id)
        if not source_id.startswith("C2LTB6-SRC-"):
            fail(errors, f"{context}.sourceRefId must start with C2LTB6-SRC-")
    require_string(ref.get("title"), f"{context}.title", errors)
    url = require_string(ref.get("url"), f"{context}.url", errors)
    if url and not url.startswith(("https://", "http://")):
        fail(errors, f"{context}.url must be http(s)")
    role = require_string(ref.get("evidenceRole"), f"{context}.evidenceRole", errors)
    if role and not role.endswith("-candidate"):
        fail(errors, f"{context}.evidenceRole must end with -candidate")
    if set(require_list(ref.get("requiredExtraction"), f"{context}.requiredExtraction", errors)) != REQUIRED_EXTRACTION_FIELDS:
        fail(errors, f"{context}.requiredExtraction must match required extraction fields")
    if ref.get("reviewStatus") != "candidate-not-yet-source-carded":
        fail(errors, f"{context}.reviewStatus must remain candidate-not-yet-source-carded")
    if ref.get("selectionTrace") != "web-checked-source-candidate-2026-07-03":
        fail(errors, f"{context}.selectionTrace must record web-checked-source-candidate-2026-07-03")


def validate_row(
    row: Any,
    index: int,
    coverage: dict[str, dict[str, Any]],
    previous: set[str],
    seen_domains: set[str],
    seen_refs: set[str],
    errors: list[str],
) -> None:
    context = f"batchRows[{index}]"
    if not isinstance(row, dict):
        fail(errors, f"{context} must be an object")
        return
    if row.get("batchId") != BATCH_ID:
        fail(errors, f"{context}.batchId must be {BATCH_ID}")
    if require_int(row.get("priorityRank"), f"{context}.priorityRank", errors) != index + 1:
        fail(errors, f"{context}.priorityRank must be {index + 1}")
    domain_id = require_string(row.get("domainId"), f"{context}.domainId", errors)
    if not domain_id:
        return
    if domain_id in seen_domains:
        fail(errors, f"duplicate queued domain: {domain_id}")
    seen_domains.add(domain_id)
    if domain_id in previous:
        fail(errors, f"{domain_id} must not duplicate C2-LT-B1/B2/B3/B4/B5")
    coverage_row = coverage.get(domain_id)
    if coverage_row is None:
        fail(errors, f"{domain_id} is missing from C2 coverage register")
        return
    if coverage_row.get("coverageStatus") != EXPECTED_COVERAGE_STATUS:
        fail(errors, f"{domain_id} must be {EXPECTED_COVERAGE_STATUS}")
    if row.get("triageBucket") != coverage_row.get("triageBucket"):
        fail(errors, f"{domain_id}.triageBucket must match coverage register")
    if row.get("localDomainPath") != coverage_row.get("physicalPath"):
        fail(errors, f"{domain_id}.localDomainPath must match coverage register")
    domain_dir = repo_path(row.get("localDomainPath"), f"{context}.localDomainPath", errors)
    if domain_dir is not None:
        for filename in ["README.md", "AGENTS.md"]:
            if not (domain_dir / filename).exists():
                fail(errors, f"{domain_id} missing {filename}")
    require_string(row.get("selectionReason"), f"{domain_id}.selectionReason", errors)
    require_string(row.get("claimSeed"), f"{domain_id}.claimSeed", errors)
    if len(require_list(row.get("variableSeed"), f"{domain_id}.variableSeed", errors)) < 5:
        fail(errors, f"{domain_id}.variableSeed must include at least 5 variables")
    sources = require_list(row.get("candidateSourceRefs"), f"{domain_id}.candidateSourceRefs", errors)
    if len(sources) != 2:
        fail(errors, f"{domain_id}.candidateSourceRefs must contain exactly 2 sources")
    for source_index, source in enumerate(sources):
        validate_candidate_source(source, f"{domain_id}.candidateSourceRefs[{source_index}]", seen_refs, errors)
    if set(require_list(row.get("requiredArtifactClasses"), f"{domain_id}.requiredArtifactClasses", errors)) != REQUIRED_ARTIFACTS:
        fail(errors, f"{domain_id}.requiredArtifactClasses must match required artifacts")
    if set(require_list(row.get("promotionSteps"), f"{domain_id}.promotionSteps", errors)) != REQUIRED_PROMOTION_STEPS:
        fail(errors, f"{domain_id}.promotionSteps must match required promotion steps")
    if set(require_list(row.get("blockedUses"), f"{domain_id}.blockedUses", errors)) != REQUIRED_BLOCKED_USES:
        fail(errors, f"{domain_id}.blockedUses must match required blocked uses")
    if row.get("modelAdmissionDecision") != "blocked-pending-c2-longtail-sixth-batch-source-card-promotion":
        fail(errors, f"{domain_id}.modelAdmissionDecision must keep model admission blocked")
    if "before any artifact promotion or model admission" not in str(row.get("nextAction", "")):
        fail(errors, f"{domain_id}.nextAction must preserve artifact/model admission boundary")


def validate_indexes(errors: list[str]) -> None:
    for relative_path, needle in REQUIRED_INDEX_LINKS.items():
        path = ROOT / relative_path
        if not path.exists():
            fail(errors, f"missing index file: {relative_path}")
            continue
        text = path.read_text(encoding="utf-8")
        if needle not in text:
            fail(errors, f"{relative_path} must link {needle}")


def validate() -> list[str]:
    errors: list[str] = []
    data = load_json(QUEUE_PATH, errors, "sixth batch promotion queue")
    if not data:
        return errors
    if data.get("schemaVersion") != SCHEMA:
        fail(errors, f"schemaVersion must be {SCHEMA}")
    if data.get("status") != STATUS:
        fail(errors, f"status must be {STATUS}")
    validate_source_of_truth(data, errors)
    if set(require_list(data.get("blockedUses"), "blockedUses", errors)) != REQUIRED_BLOCKED_USES:
        fail(errors, "blockedUses must match required blocked uses")
    rows = require_list(data.get("batchRows"), "batchRows", errors)
    if len(rows) != 12:
        fail(errors, "batchRows must contain 12 domains")
    validate_scope(data, len(rows), errors)
    coverage = coverage_by_domain(errors)
    previous = previous_domains(errors)
    seen_domains: set[str] = set()
    seen_refs: set[str] = set()
    for index, row in enumerate(rows):
        validate_row(row, index, coverage, previous, seen_domains, seen_refs, errors)
    aggregate = data.get("aggregateDecision")
    if not isinstance(aggregate, dict):
        fail(errors, "aggregateDecision must be an object")
    else:
        expected = {
            "queuedDomainCount": 12,
            "candidateSourceCount": 24,
            "reviewedArtifactCount": 0,
            "modelAdmissionsOpened": 0,
            "highestAllowedUse": "candidate-source-routing-only",
            "nextRequiredGate": "c2-longtail-sixth-batch-source-extraction-queue",
        }
        for key, value in expected.items():
            if aggregate.get(key) != value:
                fail(errors, f"aggregateDecision.{key} must be {value!r}")
    validate_indexes(errors)
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("model C2 longtail sixth batch promotion audit failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("c2 longtail sixth batch promotion audit ok: domains=12 sources=24 model_admission=blocked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
