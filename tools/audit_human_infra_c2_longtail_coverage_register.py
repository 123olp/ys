#!/usr/bin/env python3
"""审计 C2 长尾研究域覆盖缺口账本。"""

from __future__ import annotations

import csv
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = ROOT / "docs/reference/human-infra-c2-longtail-coverage-register.json"
CLASSIFICATION_PATH = ROOT / "domains/_possibility-space-control/classification.tsv"
REVIEWED_ARTIFACT_PATH = ROOT / "docs/reference/human-infra-reviewed-card-artifact-register.json"
CLAIM_MATRIX_PATH = ROOT / "docs/reference/human-infra-domain-claim-evidence-matrix.json"

SCHEMA = "human-infra.c2-longtail-coverage-register.v1"
STATUS = "active-c2-longtail-coverage-register-model-blocked"

REQUIRED_MISSING_ARTIFACTS = {
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

STATUS_COVERED = "priority-reviewed-artifact-covered"
STATUS_UNCOVERED = "c2-longtail-uncovered"


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


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
    if not isinstance(relative_path, str) or not relative_path.strip():
        fail(errors, f"{path} must be a non-empty local path")
        return None
    if relative_path.startswith(("http://", "https://")):
        fail(errors, f"{path} must be local, not URL")
        return None
    target = (ROOT / relative_path).resolve()
    try:
        target.relative_to(ROOT)
    except ValueError:
        fail(errors, f"{path} escapes repository: {relative_path}")
        return None
    if not target.exists():
        fail(errors, f"{path} does not exist: {relative_path}")
        return None
    return target


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


def load_c2_classification(errors: list[str]) -> dict[str, dict[str, str]]:
    if not CLASSIFICATION_PATH.exists():
        fail(errors, f"missing classification: {CLASSIFICATION_PATH.relative_to(ROOT)}")
        return {}
    result: dict[str, dict[str, str]] = {}
    with CLASSIFICATION_PATH.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        required = {"domain", "tier", "tier_name", "control_axis", "physical_path", "rationale", "review_status"}
        if set(reader.fieldnames or []) != required:
            fail(errors, "classification.tsv headers changed")
            return {}
        for row in reader:
            if row["tier"] != "C2":
                continue
            domain = row["domain"]
            if domain in result:
                fail(errors, f"duplicate C2 classification domain: {domain}")
            result[domain] = row
    return result


def reviewed_counts(errors: list[str]) -> Counter[str]:
    data = load_json(REVIEWED_ARTIFACT_PATH, errors, "reviewed artifact register")
    artifacts = data.get("reviewedArtifacts") if data else None
    if not isinstance(artifacts, list):
        fail(errors, "reviewed artifact register reviewedArtifacts must be a list")
        return Counter()
    counts: Counter[str] = Counter()
    for index, artifact in enumerate(artifacts):
        if not isinstance(artifact, dict):
            fail(errors, f"reviewedArtifacts[{index}] must be an object")
            continue
        domain_id = artifact.get("domainId")
        if not isinstance(domain_id, str) or not domain_id:
            fail(errors, f"reviewedArtifacts[{index}].domainId missing")
            continue
        counts[domain_id] += 1
    return counts


def matrix_domains(errors: list[str]) -> set[str]:
    data = load_json(CLAIM_MATRIX_PATH, errors, "domain claim-evidence matrix")
    rows = data.get("domainClaimRows") if data else None
    if not isinstance(rows, list):
        fail(errors, "domain claim-evidence matrix domainClaimRows must be a list")
        return set()
    result: set[str] = set()
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"domainClaimRows[{index}] must be an object")
            continue
        domain_id = row.get("domainId")
        if not isinstance(domain_id, str) or not domain_id:
            fail(errors, f"domainClaimRows[{index}].domainId missing")
            continue
        if domain_id in result:
            fail(errors, f"duplicate domain claim matrix row: {domain_id}")
        result.add(domain_id)
    return result


def validate_source_of_truth(data: dict[str, Any], errors: list[str]) -> None:
    source = data.get("sourceOfTruth")
    if not isinstance(source, dict) or not source:
        fail(errors, "sourceOfTruth must be a non-empty object")
        return
    for key, value in source.items():
        rel = require_string(value, f"sourceOfTruth.{key}", errors)
        if rel:
            repo_path(rel, f"sourceOfTruth.{key}", errors)


def validate_scope(
    data: dict[str, Any],
    c2_rows: dict[str, dict[str, str]],
    counts: Counter[str],
    errors: list[str],
) -> None:
    scope = data.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return

    total = len(c2_rows)
    covered = sum(1 for domain in c2_rows if counts.get(domain, 0) > 0)
    uncovered = total - covered

    expected_values = {
        "coverageLevel": "all-c2-domain-gap-register",
        "c2DomainCount": total,
        "priorityReviewedC2Count": covered,
        "longTailC2Count": uncovered,
    }
    for key, expected in expected_values.items():
        value = scope.get(key)
        if isinstance(expected, int):
            actual = require_int(value, f"scope.{key}", errors)
        else:
            actual = require_string(value, f"scope.{key}", errors)
        if actual != expected:
            fail(errors, f"scope.{key} must be {expected!r}")

    missing = set(require_list(scope.get("requiredMissingArtifactClasses"), "scope.requiredMissingArtifactClasses", errors))
    if missing != REQUIRED_MISSING_ARTIFACTS:
        fail(errors, f"scope.requiredMissingArtifactClasses must be {sorted(REQUIRED_MISSING_ARTIFACTS)}")

    limitations = require_list(scope.get("currentLimitations"), "scope.currentLimitations", errors)
    if len(limitations) < 3:
        fail(errors, "scope.currentLimitations must contain at least 3 limitations")


def validate_blocked_uses(data: dict[str, Any], errors: list[str]) -> None:
    blocked = set(require_list(data.get("blockedUses"), "blockedUses", errors))
    missing = REQUIRED_BLOCKED_USES - blocked
    if missing:
        fail(errors, f"blockedUses missing: {sorted(missing)}")


def validate_summary(data: dict[str, Any], rows: list[dict[str, Any]], errors: list[str]) -> None:
    summary = data.get("coverageSummary")
    if not isinstance(summary, dict):
        fail(errors, "coverageSummary must be an object")
        return
    status_counts = Counter(row.get("coverageStatus") for row in rows)
    for key, expected in {
        "priorityReviewedArtifactCovered": status_counts[STATUS_COVERED],
        "c2LongTailUncovered": status_counts[STATUS_UNCOVERED],
    }.items():
        actual = require_int(summary.get(key), f"coverageSummary.{key}", errors)
        if actual != expected:
            fail(errors, f"coverageSummary.{key} must be {expected}")
    buckets = summary.get("triageBuckets")
    if not isinstance(buckets, dict) or not buckets:
        fail(errors, "coverageSummary.triageBuckets must be a non-empty object")


def validate_row(
    row: Any,
    index: int,
    c2_rows: dict[str, dict[str, str]],
    counts: Counter[str],
    claim_domains: set[str],
    seen: set[str],
    errors: list[str],
) -> None:
    path = f"coverageRows[{index}]"
    if not isinstance(row, dict):
        fail(errors, f"{path} must be an object")
        return
    domain_id = require_string(row.get("domainId"), f"{path}.domainId", errors)
    if not domain_id:
        return
    if domain_id in seen:
        fail(errors, f"duplicate coverage row: {domain_id}")
    seen.add(domain_id)
    classification = c2_rows.get(domain_id)
    if classification is None:
        fail(errors, f"{path}.domainId is not C2 classification domain: {domain_id}")
        return

    expected_fields = {
        "tier": classification["tier"],
        "tierName": classification["tier_name"],
        "controlAxis": classification["control_axis"],
        "physicalPath": classification["physical_path"],
        "reviewStatus": classification["review_status"],
    }
    for key, expected in expected_fields.items():
        actual = require_string(row.get(key), f"{path}.{key}", errors)
        if actual != expected:
            fail(errors, f"{path}.{key} must be {expected!r}")
    repo_path(classification["physical_path"], f"{path}.physicalPath", errors)
    domain_path = ROOT / classification["physical_path"]
    for required_doc in ["README.md", "AGENTS.md"]:
        if not (domain_path / required_doc).exists():
            fail(errors, f"{domain_id} missing {required_doc}")

    reviewed_count = require_int(row.get("reviewedArtifactCount"), f"{path}.reviewedArtifactCount", errors)
    expected_count = counts.get(domain_id, 0)
    if reviewed_count != expected_count:
        fail(errors, f"{path}.reviewedArtifactCount must be {expected_count}")

    in_claim = row.get("inDomainClaimEvidenceMatrix")
    if not isinstance(in_claim, bool):
        fail(errors, f"{path}.inDomainClaimEvidenceMatrix must be boolean")
    elif in_claim != (domain_id in claim_domains):
        fail(errors, f"{path}.inDomainClaimEvidenceMatrix mismatch for {domain_id}")

    status = require_string(row.get("coverageStatus"), f"{path}.coverageStatus", errors)
    missing = set(require_list(row.get("missingArtifactClasses"), f"{path}.missingArtifactClasses", errors))
    if expected_count > 0:
        if status != STATUS_COVERED:
            fail(errors, f"{path}.coverageStatus must be {STATUS_COVERED}")
        if missing:
            fail(errors, f"{path}.missingArtifactClasses must be empty for covered domain")
    else:
        if status != STATUS_UNCOVERED:
            fail(errors, f"{path}.coverageStatus must be {STATUS_UNCOVERED}")
        if missing != REQUIRED_MISSING_ARTIFACTS:
            fail(errors, f"{path}.missingArtifactClasses must list all required missing artifacts")

    require_string(row.get("triageBucket"), f"{path}.triageBucket", errors)
    require_string(row.get("nextAction"), f"{path}.nextAction", errors)
    decision = require_string(row.get("modelAdmissionDecision"), f"{path}.modelAdmissionDecision", errors)
    if "blocked" not in decision:
        fail(errors, f"{path}.modelAdmissionDecision must keep model admission blocked")


def main() -> int:
    errors: list[str] = []
    data = load_json(REGISTER_PATH, errors, "C2 longtail coverage register")
    c2_rows = load_c2_classification(errors)
    counts = reviewed_counts(errors)
    claim_domains = matrix_domains(errors)

    if data:
        if data.get("schemaVersion") != SCHEMA:
            fail(errors, f"schemaVersion must be {SCHEMA}")
        if data.get("status") != STATUS:
            fail(errors, f"status must be {STATUS}")
        require_string(data.get("registerId"), "registerId", errors)
        require_string(data.get("purpose"), "purpose", errors)
        validate_source_of_truth(data, errors)
        validate_scope(data, c2_rows, counts, errors)
        validate_blocked_uses(data, errors)

        rows = data.get("coverageRows")
        if not isinstance(rows, list):
            fail(errors, "coverageRows must be a list")
            rows = []
        if len(rows) != len(c2_rows):
            fail(errors, f"coverageRows must contain every C2 domain ({len(c2_rows)})")

        seen: set[str] = set()
        for index, row in enumerate(rows):
            validate_row(row, index, c2_rows, counts, claim_domains, seen, errors)
        missing_domains = set(c2_rows) - seen
        if missing_domains:
            fail(errors, f"coverageRows missing C2 domains: {sorted(missing_domains)[:10]}")
        validate_summary(data, rows, errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    covered = sum(1 for row in data.get("coverageRows", []) if row.get("coverageStatus") == STATUS_COVERED)
    uncovered = sum(1 for row in data.get("coverageRows", []) if row.get("coverageStatus") == STATUS_UNCOVERED)
    print(f"C2 longtail coverage register audit ok: c2={covered + uncovered} covered={covered} longtail={uncovered}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
