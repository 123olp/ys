#!/usr/bin/env python3
"""审计 C2 长尾第十三批研究域晋升队列。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
QUEUE_PATH = ROOT / "docs/reference/human-infra-c2-longtail-thirteenth-batch-promotion-queue.json"
COVERAGE_PATH = ROOT / "docs/reference/human-infra-c2-longtail-coverage-register.json"
PREVIOUS_BATCHES = [
    ROOT / "docs/reference/human-infra-c2-longtail-first-batch-promotion-queue.json",
    ROOT / "docs/reference/human-infra-c2-longtail-second-batch-promotion-queue.json",
    ROOT / "docs/reference/human-infra-c2-longtail-third-batch-promotion-queue.json",
    ROOT / "docs/reference/human-infra-c2-longtail-fourth-batch-promotion-queue.json",
    ROOT / "docs/reference/human-infra-c2-longtail-fifth-batch-promotion-queue.json",
    ROOT / "docs/reference/human-infra-c2-longtail-sixth-batch-promotion-queue.json",
    ROOT / "docs/reference/human-infra-c2-longtail-seventh-batch-promotion-queue.json",
    ROOT / "docs/reference/human-infra-c2-longtail-eighth-batch-promotion-queue.json",
    ROOT / "docs/reference/human-infra-c2-longtail-ninth-batch-promotion-queue.json",
    ROOT / "docs/reference/human-infra-c2-longtail-tenth-batch-promotion-queue.json",
    ROOT / "docs/reference/human-infra-c2-longtail-eleventh-batch-promotion-queue.json",
    ROOT / "docs/reference/human-infra-c2-longtail-twelfth-batch-promotion-queue.json",
]

SCHEMA = "human-infra.c2-longtail-thirteenth-batch-promotion-queue.v1"
STATUS = "active-thirteenth-batch-queue-model-blocked"
BATCH_ID = "C2-LT-B13"
EXPECTED_ROWS = 12
EXPECTED_SOURCES = 24
REGISTER_LINK = "human-infra-c2-longtail-thirteenth-batch-promotion-queue.json"
SCRIPT_LINK = "audit_human_infra_c2_longtail_thirteenth_batch_promotion_queue.py"

REQUIRED_BLOCKED_USES = {
    "calibrated-prediction",
    "individual-advice",
    "individual-death-date-output",
    "intervention-ranking",
    "clinical-validity-claim",
    "domain-claim-upgrade",
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
    "docs/AGENTS.md": REGISTER_LINK,
    "docs/reference/README.md": REGISTER_LINK,
    "docs/reference/human-infra-maturity-roadmap.md": REGISTER_LINK,
    "docs/reference/human-infra-maturity-gap-register.json": REGISTER_LINK,
    "Makefile": "c2-longtail-thirteenth-batch-promotion-audit",
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


def require_list(value: Any, context: str, errors: list[str]) -> list[Any]:
    if not isinstance(value, list):
        fail(errors, f"{context} must be a list")
        return []
    return value


def repo_path(relative_path: Any, context: str, errors: list[str]) -> Path | None:
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
    return {row["domainId"]: row for row in rows if isinstance(row, dict) and isinstance(row.get("domainId"), str)}


def validate_candidate_source(ref: Any, row_index: int, source_index: int, seen_refs: set[str], errors: list[str]) -> None:
    context = f"batchRows[{row_index}].candidateSourceRefs[{source_index}]"
    if not isinstance(ref, dict):
        fail(errors, f"{context} must be an object")
        return
    source_id = require_string(ref.get("sourceRefId"), f"{context}.sourceRefId", errors)
    if source_id:
        if source_id in seen_refs:
            fail(errors, f"duplicate sourceRefId: {source_id}")
        seen_refs.add(source_id)
        if not source_id.startswith("C2LTB13-SRC-"):
            fail(errors, f"{context}.sourceRefId must start with C2LTB13-SRC-")
    require_string(ref.get("title"), f"{context}.title", errors)
    url = require_string(ref.get("url"), f"{context}.url", errors)
    if url and not url.startswith(("https://", "http://")):
        fail(errors, f"{context}.url must be http(s)")
    require_string(ref.get("evidenceRole"), f"{context}.evidenceRole", errors)
    if set(require_list(ref.get("requiredExtraction"), f"{context}.requiredExtraction", errors)) != REQUIRED_EXTRACTION_FIELDS:
        fail(errors, f"{context}.requiredExtraction must match required field set")
    if ref.get("reviewStatus") != "candidate-not-yet-source-carded":
        fail(errors, f"{context}.reviewStatus must be candidate-not-yet-source-carded")
    if ref.get("selectionTrace") != "web-checked-source-candidate-2026-07-11":
        fail(errors, f"{context}.selectionTrace must record 2026-07-11 web check")
    check = ref.get("sourceCheck")
    if not isinstance(check, dict):
        fail(errors, f"{context}.sourceCheck must be an object")
        return
    if check.get("statusCode") != 200:
        fail(errors, f"{context}.sourceCheck.statusCode must be 200")
    if not isinstance(check.get("contentLengthBytes"), int) or check["contentLengthBytes"] <= 1000:
        fail(errors, f"{context}.sourceCheck.contentLengthBytes must be > 1000")


def validate_index_links(errors: list[str]) -> None:
    for relative_path, needle in REQUIRED_INDEX_LINKS.items():
        path = ROOT / relative_path
        if not path.exists():
            fail(errors, f"missing index target: {relative_path}")
            continue
        if needle not in path.read_text(encoding="utf-8"):
            fail(errors, f"{relative_path} must reference {needle}")


def main() -> int:
    errors: list[str] = []
    data = load_json(QUEUE_PATH, errors, "C2-LT-B13 promotion queue")
    coverage = coverage_by_domain(errors)
    previous = previous_domains(errors)

    if data:
        if data.get("schemaVersion") != SCHEMA:
            fail(errors, f"schemaVersion must be {SCHEMA}")
        if data.get("status") != STATUS:
            fail(errors, f"status must be {STATUS}")
        if set(require_list(data.get("blockedUses"), "blockedUses", errors)) != REQUIRED_BLOCKED_USES:
            fail(errors, "blockedUses must match required blocked-use set")

        source = data.get("sourceOfTruth")
        if not isinstance(source, dict) or "twelfthBatchPromotionQueue" not in source:
            fail(errors, "sourceOfTruth must include previous B1-B12 queues")
        elif any(repo_path(value, f"sourceOfTruth.{key}", errors) is None for key, value in source.items()):
            pass

        scope = data.get("scope")
        if not isinstance(scope, dict):
            fail(errors, "scope must be an object")
        else:
            if scope.get("batchId") != BATCH_ID:
                fail(errors, f"scope.batchId must be {BATCH_ID}")
            if scope.get("batchDomainCount") != EXPECTED_ROWS:
                fail(errors, f"scope.batchDomainCount must be {EXPECTED_ROWS}")
            if set(require_list(scope.get("requiredArtifactClasses"), "scope.requiredArtifactClasses", errors)) != REQUIRED_ARTIFACTS:
                fail(errors, "scope.requiredArtifactClasses must match required artifact set")
            non_claims = " ".join(str(item) for item in require_list(scope.get("nonClaims"), "scope.nonClaims", errors))
            for phrase in [
                "does not complete Source Cards",
                "does not complete independent fresh review",
                "does not admit any domain into calibrated prediction",
                "B1/B2/B3/B4/B5/B6/B7/B8/B9/B10/B11/B12",
            ]:
                if phrase not in non_claims:
                    fail(errors, f"scope.nonClaims missing phrase: {phrase}")

        rows = data.get("batchRows")
        if not isinstance(rows, list) or len(rows) != EXPECTED_ROWS:
            fail(errors, f"batchRows must contain {EXPECTED_ROWS} rows")
            rows = []
        seen_domains: set[str] = set()
        seen_refs: set[str] = set()
        for index, row in enumerate(rows):
            if not isinstance(row, dict):
                fail(errors, f"batchRows[{index}] must be an object")
                continue
            domain_id = require_string(row.get("domainId"), f"batchRows[{index}].domainId", errors)
            if domain_id:
                if domain_id in seen_domains:
                    fail(errors, f"duplicate domainId: {domain_id}")
                seen_domains.add(domain_id)
                if domain_id in previous:
                    fail(errors, f"{domain_id} already appears in previous C2-LT batch")
                coverage_row = coverage.get(domain_id)
                if not coverage_row:
                    fail(errors, f"{domain_id} missing from coverage register")
                elif coverage_row.get("coverageStatus") != "c2-longtail-uncovered":
                    fail(errors, f"{domain_id} must remain c2-longtail-uncovered in coverage register")
            if row.get("batchId") != BATCH_ID:
                fail(errors, f"batchRows[{index}].batchId must be {BATCH_ID}")
            repo_path(row.get("localDomainPath"), f"batchRows[{index}].localDomainPath", errors)
            require_string(row.get("selectionReason"), f"batchRows[{index}].selectionReason", errors)
            require_string(row.get("claimSeed"), f"batchRows[{index}].claimSeed", errors)
            require_list(row.get("variableSeed"), f"batchRows[{index}].variableSeed", errors)
            if set(require_list(row.get("promotionSteps"), f"batchRows[{index}].promotionSteps", errors)) != REQUIRED_PROMOTION_STEPS:
                fail(errors, f"batchRows[{index}].promotionSteps must match required set")
            if set(require_list(row.get("blockedUses"), f"batchRows[{index}].blockedUses", errors)) != REQUIRED_BLOCKED_USES:
                fail(errors, f"batchRows[{index}].blockedUses must match required blocked-use set")
            if "blocked" not in require_string(row.get("modelAdmissionDecision"), f"batchRows[{index}].modelAdmissionDecision", errors):
                fail(errors, f"batchRows[{index}].modelAdmissionDecision must contain blocked")
            sources = require_list(row.get("candidateSourceRefs"), f"batchRows[{index}].candidateSourceRefs", errors)
            if len(sources) != 2:
                fail(errors, f"batchRows[{index}].candidateSourceRefs must contain exactly 2 sources")
            for source_index, source_ref in enumerate(sources):
                validate_candidate_source(source_ref, index, source_index, seen_refs, errors)

        aggregate = data.get("aggregateDecision")
        if not isinstance(aggregate, dict):
            fail(errors, "aggregateDecision must be an object")
        else:
            if aggregate.get("selectedDomainCount") != EXPECTED_ROWS:
                fail(errors, f"aggregateDecision.selectedDomainCount must be {EXPECTED_ROWS}")
            if aggregate.get("candidateSourceCount") != EXPECTED_SOURCES:
                fail(errors, f"aggregateDecision.candidateSourceCount must be {EXPECTED_SOURCES}")
            if aggregate.get("modelAdmission") != "blocked":
                fail(errors, "aggregateDecision.modelAdmission must be blocked")

    validate_index_links(errors)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"C2-LT-B13 promotion queue audit ok: domains={EXPECTED_ROWS} sources={EXPECTED_SOURCES}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
