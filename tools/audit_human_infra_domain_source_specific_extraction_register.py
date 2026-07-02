#!/usr/bin/env python3
"""审计域-来源精读完成寄存器。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = ROOT / "docs/reference/human-infra-domain-source-specific-extraction-register.json"
QUEUE_PATH = ROOT / "docs/reference/human-infra-domain-source-specific-extraction-queue.json"
FIELD_REGISTER_PATH = ROOT / "docs/reference/human-infra-domain-source-card-field-extraction.json"
SOURCE_EXTRACTION_PATH = ROOT / "docs/reference/human-infra-falsifier-source-card-extraction.json"

SCHEMA = "human-infra.domain-source-specific-extraction-register.v1"
STATUS = "all-queued-source-specific-extractions-complete-pending-fresh-review"
REGISTER_LINK = "human-infra-domain-source-specific-extraction-register.json"
EXPECTED_SOURCES = {
    "SA-KAPLAN-MEIER-1958": {
        "role": "survival-function-and-censoring-method-anchor",
        "decision": "qualitative-method-support-only-blocked-for-calibrated-prediction",
        "row_status": "completed-first-wave-method-anchor-field-extraction",
        "blocked": {
            "calibrated-prediction",
            "individual-recommendation",
            "intervention-ranking",
            "individual-death-date-output",
        },
    },
    "SA-COX-1972": {
        "role": "hazard-function-and-covariate-risk-method-anchor",
        "decision": "qualitative-method-support-only-blocked-for-calibrated-prediction",
        "row_status": "completed-first-wave-method-anchor-field-extraction",
        "blocked": {
            "calibrated-prediction",
            "individual-recommendation",
            "intervention-ranking",
            "individual-death-date-output",
        },
    },
    "SA-TARGET-TRIAL-2022": {
        "role": "intervention-causal-design-method-anchor",
        "decision": "causal-design-support-only-blocked-for-effect-claim",
        "row_status": "completed-first-wave-method-anchor-field-extraction",
        "blocked": {
            "calibrated-prediction",
            "individual-recommendation",
            "intervention-ranking",
            "domain-claim-upgrade",
        },
    },
    "SA-TRIPOD-AI-2024": {
        "role": "prediction-model-reporting-and-validation-method-anchor",
        "decision": "prediction-reporting-support-only-blocked-for-clinical-prediction",
        "row_status": "completed-first-wave-method-anchor-field-extraction",
        "blocked": {
            "calibrated-prediction",
            "individual-recommendation",
            "intervention-ranking",
            "individual-death-date-output",
        },
    },
    "SA-HALLMARKS-AGING-2023": {
        "role": "expanded-aging-hallmark-mechanism-taxonomy-anchor",
        "decision": "mechanism-taxonomy-support-only-blocked-for-intervention-effect-claim",
        "row_status": "completed-second-wave-biological-mechanism-field-extraction",
        "blocked": {
            "calibrated-prediction",
            "individual-recommendation",
            "intervention-ranking",
            "domain-claim-upgrade",
        },
    },
    "SA-HALLMARKS-AGING-2013": {
        "role": "baseline-aging-hallmark-mechanism-taxonomy-anchor",
        "decision": "mechanism-taxonomy-support-only-blocked-for-intervention-effect-claim",
        "row_status": "completed-second-wave-biological-mechanism-field-extraction",
        "blocked": {
            "calibrated-prediction",
            "individual-recommendation",
            "intervention-ranking",
            "domain-claim-upgrade",
        },
    },
    "SA-HALLMARKS-CANCER-2022": {
        "role": "cancer-risk-and-tumor-capability-abort-gate-anchor",
        "decision": "adverse-mechanism-support-only-blocked-for-safety-or-benefit-claim",
        "row_status": "completed-second-wave-biological-mechanism-field-extraction",
        "blocked": {
            "calibrated-prediction",
            "individual-recommendation",
            "intervention-ranking",
            "domain-claim-upgrade",
        },
    },
    "SA-YAMANAKA-IPS-2006": {
        "role": "cell-identity-reprogramming-foundation-anchor",
        "decision": "cell-state-transition-support-only-blocked-for-rejuvenation-claim",
        "row_status": "completed-second-wave-biological-mechanism-field-extraction",
        "blocked": {
            "calibrated-prediction",
            "individual-recommendation",
            "intervention-ranking",
            "domain-claim-upgrade",
        },
    },
    "SA-PARTIAL-REPROGRAMMING-2016": {
        "role": "partial-reprogramming-controlled-window-route-anchor",
        "decision": "preclinical-route-support-only-blocked-for-clinical-rejuvenation-claim",
        "row_status": "completed-second-wave-biological-mechanism-field-extraction",
        "blocked": {
            "calibrated-prediction",
            "individual-recommendation",
            "intervention-ranking",
            "domain-claim-upgrade",
        },
    },
    "SA-IMMUNOSENESCENCE-2024": {
        "role": "immune-aging-multichannel-maintenance-anchor",
        "decision": "immune-mechanism-support-only-blocked-for-treatment-or-boost-claim",
        "row_status": "completed-second-wave-biological-mechanism-field-extraction",
        "blocked": {
            "calibrated-prediction",
            "individual-recommendation",
            "intervention-ranking",
            "domain-claim-upgrade",
        },
    },
    "SA-GRIMAGE-2019": {
        "role": "biological-age-risk-marker-observation-anchor",
        "decision": "biomarker-observation-support-only-blocked-for-causal-or-predictive-claim",
        "row_status": "completed-second-wave-biological-mechanism-field-extraction",
        "blocked": {
            "calibrated-prediction",
            "individual-recommendation",
            "intervention-ranking",
            "individual-death-date-output",
        },
    },
    "SA-WHO-CONSTITUTION": {
        "role": "health-functioning-wellbeing-value-anchor",
        "decision": "value-definition-support-only-blocked-for-intervention-or-prediction-claim",
        "row_status": "completed-third-wave-continuity-governance-and-future-path-field-extraction",
        "blocked": {
            "calibrated-prediction",
            "individual-recommendation",
            "intervention-ranking",
            "domain-claim-upgrade",
        },
    },
    "SA-CAPABILITY-APPROACH": {
        "role": "capability-option-value-and-functioning-value-anchor",
        "decision": "value-framework-support-only-blocked-for-effect-claim",
        "row_status": "completed-third-wave-continuity-governance-and-future-path-field-extraction",
        "blocked": {
            "calibrated-prediction",
            "individual-recommendation",
            "intervention-ranking",
            "domain-claim-upgrade",
        },
    },
    "SA-EXTENDED-MIND-1998": {
        "role": "extended-cognition-tool-dependence-continuity-anchor",
        "decision": "cognitive-infrastructure-support-only-blocked-for-performance-or-continuity-claim",
        "row_status": "completed-third-wave-continuity-governance-and-future-path-field-extraction",
        "blocked": {
            "calibrated-prediction",
            "individual-recommendation",
            "intervention-ranking",
            "domain-claim-upgrade",
        },
    },
    "SA-DYNAMIC-DIGITAL-TWIN-2022": {
        "role": "subject-state-modeling-architecture-anchor",
        "decision": "modeling-architecture-support-only-blocked-for-prediction-or-treatment-claim",
        "row_status": "completed-third-wave-continuity-governance-and-future-path-field-extraction",
        "blocked": {
            "calibrated-prediction",
            "individual-recommendation",
            "intervention-ranking",
            "domain-claim-upgrade",
        },
    },
    "SA-BRAIN-PRESERVATION-2024": {
        "role": "brain-information-preservation-and-continuity-boundary-anchor",
        "decision": "preservation-structure-support-only-blocked-for-revival-or-identity-claim",
        "row_status": "completed-third-wave-continuity-governance-and-future-path-field-extraction",
        "blocked": {
            "calibrated-prediction",
            "individual-recommendation",
            "intervention-ranking",
            "domain-claim-upgrade",
        },
    },
    "SA-GPS-RELATIVITY-2003": {
        "role": "proper-time-reference-frame-accounting-anchor",
        "decision": "time-accounting-support-only-blocked-for-waiting-feasibility-claim",
        "row_status": "completed-third-wave-continuity-governance-and-future-path-field-extraction",
        "blocked": {
            "calibrated-prediction",
            "individual-recommendation",
            "intervention-ranking",
            "domain-claim-upgrade",
        },
    },
    "SA-NASA-BLACK-HOLES": {
        "role": "black-hole-public-boundary-and-hazard-explainer-anchor",
        "decision": "public-explainer-support-only-blocked-for-engineering-feasibility-claim",
        "row_status": "completed-third-wave-continuity-governance-and-future-path-field-extraction",
        "blocked": {
            "calibrated-prediction",
            "individual-recommendation",
            "intervention-ranking",
            "domain-claim-upgrade",
        },
    },
    "SA-NIST-AI-RMF-2023": {
        "role": "ai-risk-governance-and-trustworthiness-anchor",
        "decision": "ai-governance-support-only-blocked-for-autonomous-action-claim",
        "row_status": "completed-third-wave-continuity-governance-and-future-path-field-extraction",
        "blocked": {
            "calibrated-prediction",
            "individual-recommendation",
            "intervention-ranking",
            "domain-claim-upgrade",
        },
    },
    "SA-NCI-SCREENING-BIAS": {
        "role": "screening-endpoint-bias-and-harm-boundary-anchor",
        "decision": "endpoint-bias-support-only-blocked-for-screening-benefit-claim",
        "row_status": "completed-third-wave-continuity-governance-and-future-path-field-extraction",
        "blocked": {
            "calibrated-prediction",
            "individual-recommendation",
            "intervention-ranking",
            "domain-claim-upgrade",
        },
    },
}

SOURCE_OF_TRUTH_KEYS = [
    "domainSourceSpecificExtractionQueue",
    "domainSourceCardFieldExtraction",
    "sourceCardExtractionRegister",
    "sourceCardSystem",
    "maturityGapRegister",
]

REQUIRED_ROW_FIELDS = [
    "domainId",
    "domainClaimId",
    "fieldCardId",
    "sourceCardId",
    "extractionStatus",
    "sourceRole",
    "exactClaimUse",
    "endpointDefinition",
    "populationOrSample",
    "effectOrMechanismSignal",
    "uncertaintyOrBias",
    "transferBoundary",
    "modelAdmissionDecision",
    "blockedUses",
    "nextAction",
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


def source_extraction_ids(errors: list[str]) -> set[str]:
    data = load_json(SOURCE_EXTRACTION_PATH, errors, "source-card extraction register")
    cards = data.get("sourceCards") if data else None
    if not isinstance(cards, list):
        fail(errors, "source-card extraction sourceCards must be a list")
        return set()
    result: set[str] = set()
    for index, card in enumerate(cards):
        if not isinstance(card, dict):
            fail(errors, f"sourceCards[{index}] must be an object")
            continue
        source_id = card.get("sourceId")
        if not isinstance(source_id, str) or not source_id.strip():
            fail(errors, f"sourceCards[{index}].sourceId missing")
            continue
        result.add(source_id)
    return result


def derived_field_context(errors: list[str]) -> tuple[dict[tuple[str, str], dict[str, Any]], int, int, int]:
    data = load_json(FIELD_REGISTER_PATH, errors, "domain source-card field extraction register")
    rows = data.get("fieldRows") if data else None
    if not isinstance(rows, list):
        fail(errors, "domain field extraction fieldRows must be a list")
        return ({}, 0, 0, 0)

    extracted_sources = source_extraction_ids(errors)
    context: dict[tuple[str, str], dict[str, Any]] = {}
    domain_ids: set[str] = set()
    source_ids: set[str] = set()

    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"fieldRows[{index}] must be an object")
            continue
        domain_id = require_string(row.get("domainId"), f"fieldRows[{index}].domainId", errors)
        require_string(row.get("domainClaimId"), f"{domain_id}.domainClaimId", errors)
        require_string(row.get("fieldCardId"), f"{domain_id}.fieldCardId", errors)
        source_cards = require_string_list(row.get("sourceCardIds"), f"{domain_id}.sourceCardIds", errors, 1)
        if domain_id:
            domain_ids.add(domain_id)
        for source_id in source_cards:
            if source_id not in extracted_sources:
                fail(errors, f"{domain_id} references source without field extraction: {source_id}")
            context[(domain_id, source_id)] = row
            source_ids.add(source_id)

    return (context, len(domain_ids), len(rows), len(context))


def validate_source_of_truth(data: dict[str, Any], errors: list[str]) -> None:
    source = data.get("sourceOfTruth")
    if not isinstance(source, dict):
        fail(errors, "sourceOfTruth must be an object")
        return
    for key in SOURCE_OF_TRUTH_KEYS:
        value = require_string(source.get(key), f"sourceOfTruth.{key}", errors)
        if value:
            repo_path(value, f"sourceOfTruth.{key}", errors)


def validate_scope(scope: Any, completed_count: int, touched_fields: int, queued_count: int, errors: list[str]) -> None:
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return
    if scope.get("coverageLevel") != "full-queue-source-specific-field-extractions":
        fail(errors, "scope.coverageLevel must be full-queue-source-specific-field-extractions")
    if scope.get("derivedTaskUnit") != "domainId + sourceCardId":
        fail(errors, "scope.derivedTaskUnit must be domainId + sourceCardId")
    expected_counts = {
        "queuedTaskCount": queued_count,
        "completedTaskCount": completed_count,
        "remainingQueuedTaskCount": queued_count - completed_count,
        "completedFieldRowCount": touched_fields,
        "completedSourceAnchorCount": len(EXPECTED_SOURCES),
    }
    for key, expected in expected_counts.items():
        value = require_int(scope.get(key), f"scope.{key}", errors)
        if value is not None and value != expected:
            fail(errors, f"scope.{key} must equal {expected}")
    source_anchors = set(require_string_list(scope.get("completedSourceAnchors"), "scope.completedSourceAnchors", errors, len(EXPECTED_SOURCES)))
    if source_anchors != set(EXPECTED_SOURCES):
        fail(errors, "scope.completedSourceAnchors must equal all registered source anchors")
    require_string(scope.get("selectionRule"), "scope.selectionRule", errors)
    require_string_list(scope.get("currentLimitations"), "scope.currentLimitations", errors, 3)


def validate_anchor_decisions(decisions: Any, errors: list[str]) -> None:
    if not isinstance(decisions, list):
        fail(errors, "sourceAnchorDecisions must be a list")
        return
    seen: set[str] = set()
    for index, item in enumerate(decisions):
        if not isinstance(item, dict):
            fail(errors, f"sourceAnchorDecisions[{index}] must be an object")
            continue
        source_id = require_string(item.get("sourceCardId"), f"sourceAnchorDecisions[{index}].sourceCardId", errors)
        if source_id in seen:
            fail(errors, f"duplicate sourceAnchorDecision: {source_id}")
        seen.add(source_id)
        expected = EXPECTED_SOURCES.get(source_id)
        if expected is None:
            fail(errors, f"unexpected sourceAnchorDecision: {source_id}")
            continue
        if item.get("sourceRole") != expected["role"]:
            fail(errors, f"{source_id}.sourceRole mismatch")
        if item.get("modelAdmissionDecision") != expected["decision"]:
            fail(errors, f"{source_id}.modelAdmissionDecision mismatch")
        blocked = set(require_string_list(item.get("blockedUses"), f"{source_id}.blockedUses", errors, len(expected["blocked"])))
        if blocked != expected["blocked"]:
            fail(errors, f"{source_id}.blockedUses must equal expected blocked uses")
        require_string(item.get("transferBoundary"), f"{source_id}.transferBoundary", errors)
    if seen != set(EXPECTED_SOURCES):
        fail(errors, "sourceAnchorDecisions must contain every registered source anchor")


def validate_completed_rows(rows: Any, field_context: dict[tuple[str, str], dict[str, Any]], errors: list[str]) -> tuple[int, int]:
    if not isinstance(rows, list):
        fail(errors, "completedRows must be a list")
        return (0, 0)

    seen: set[tuple[str, str]] = set()
    touched_fields: set[str] = set()

    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"completedRows[{index}] must be an object")
            continue
        for key in REQUIRED_ROW_FIELDS:
            if key == "blockedUses":
                require_string_list(row.get(key), f"completedRows[{index}].{key}", errors, 4)
            else:
                require_string(row.get(key), f"completedRows[{index}].{key}", errors)

        domain_id = row.get("domainId")
        source_id = row.get("sourceCardId")
        if not isinstance(domain_id, str) or not isinstance(source_id, str):
            continue
        key = (domain_id, source_id)
        if key in seen:
            fail(errors, f"duplicate completed row: {domain_id}/{source_id}")
        seen.add(key)
        field_row = field_context.get(key)
        if field_row is None:
            fail(errors, f"completed row is not in queue-derived field context: {domain_id}/{source_id}")
            continue

        if source_id not in EXPECTED_SOURCES:
            fail(errors, f"completed row uses source outside registered source anchors: {domain_id}/{source_id}")
            continue
        expected = EXPECTED_SOURCES[source_id]
        if row.get("domainClaimId") != field_row.get("domainClaimId"):
            fail(errors, f"{domain_id}/{source_id} domainClaimId mismatch")
        if row.get("fieldCardId") != field_row.get("fieldCardId"):
            fail(errors, f"{domain_id}/{source_id} fieldCardId mismatch")
        if row.get("extractionStatus") != expected["row_status"]:
            fail(errors, f"{domain_id}/{source_id} extractionStatus mismatch")
        if row.get("sourceRole") != expected["role"]:
            fail(errors, f"{domain_id}/{source_id} sourceRole mismatch")
        if row.get("modelAdmissionDecision") != expected["decision"]:
            fail(errors, f"{domain_id}/{source_id} modelAdmissionDecision mismatch")
        blocked = set(require_string_list(row.get("blockedUses"), f"{domain_id}/{source_id}.blockedUses", errors, len(expected["blocked"])))
        if blocked != expected["blocked"]:
            fail(errors, f"{domain_id}/{source_id}.blockedUses must equal expected blocked uses")

        endpoints = field_row.get("endpointCandidates")
        if isinstance(endpoints, list):
            endpoint_text = str(row.get("endpointDefinition", ""))
            for endpoint in endpoints:
                if isinstance(endpoint, str) and endpoint not in endpoint_text:
                    fail(errors, f"{domain_id}/{source_id} endpointDefinition missing endpoint candidate: {endpoint}")
        touched_fields.add(str(field_row.get("fieldCardId")))

    return (len(seen), len(touched_fields))


def validate_index_links(paths: Any, errors: list[str]) -> None:
    for relative_path in require_string_list(paths, "indexRequirements", errors, 2):
        target = repo_path(relative_path, f"indexRequirements:{relative_path}", errors)
        if target is None:
            continue
        if REGISTER_LINK not in target.read_text(encoding="utf-8"):
            fail(errors, f"index does not link domain-source extraction register: {relative_path}")


def main() -> int:
    errors: list[str] = []
    data = load_json(REGISTER_PATH, errors, "domain-source extraction register")
    field_context, _domain_count, _field_count, queued_count = derived_field_context(errors)

    if not data:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    if data.get("schemaVersion") != SCHEMA:
        fail(errors, f"schemaVersion must be {SCHEMA}")
    if data.get("status") != STATUS:
        fail(errors, f"status must be {STATUS}")
    require_string(data.get("registerId"), "registerId", errors)
    require_string(data.get("purpose"), "purpose", errors)

    validate_source_of_truth(data, errors)
    completed_count, touched_fields = validate_completed_rows(data.get("completedRows"), field_context, errors)
    validate_scope(data.get("scope"), completed_count, touched_fields, queued_count, errors)
    validate_anchor_decisions(data.get("sourceAnchorDecisions"), errors)
    require_string_list(data.get("nonClaims"), "nonClaims", errors, 4)
    validate_index_links(data.get("indexRequirements"), errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(
        "domain-source extraction register audit ok: "
        f"completed={completed_count} remaining={queued_count - completed_count} field_rows={touched_fields}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
