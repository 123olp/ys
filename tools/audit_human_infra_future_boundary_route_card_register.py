#!/usr/bin/env python3
"""审计 future-boundary route card register 的本地契约。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = ROOT / "docs/reference/human-infra-future-boundary-route-card-register.json"

EXPECTED_SCHEMA = "human-infra.future-boundary-route-card-register.v1"
EXPECTED_STATUS = "active-route-card-register-model-blocked"

REQUIRED_ROUTE_FAMILIES = {
    "future-waiting",
    "biological-stasis",
    "neuro-identity-continuity",
    "ai-enabled-acceleration",
}

REQUIRED_GATE_DIMENSIONS = {
    "technical-window",
    "access",
    "adoption",
    "duration",
    "composability",
    "tail-risk",
    "opportunity-cost",
}

REQUIRED_BLOCKED_USES = {
    "calibrated-prediction",
    "individual-advice",
    "individual-death-date-output",
    "intervention-ranking",
    "clinical-validity-claim",
    "engineering-feasibility-claim",
    "route-feasibility-promise",
}

REQUIRED_CARD_FIELDS = {
    "routeId",
    "routeFamily",
    "routeName",
    "routeStatus",
    "routeType",
    "primaryDomainPath",
    "supportingDomainPaths",
    "reviewedArtifactSupport",
    "claimBoundary",
    "effectChain",
    "gateCoverage",
    "abortGates",
    "sourceRefs",
    "modelAdmissionDecision",
}


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
    if not isinstance(value, list) or not value:
        fail(errors, f"{path} must be a non-empty list")
        return []
    return value


def validate_local_path(relative: str, path: str, errors: list[str]) -> None:
    if relative.startswith("http://") or relative.startswith("https://"):
        fail(errors, f"{path} must be a local repository path, not URL")
        return
    target = (ROOT / relative).resolve()
    try:
        target.relative_to(ROOT)
    except ValueError:
        fail(errors, f"{path} escapes repository: {relative}")
        return
    if not target.exists():
        fail(errors, f"{path} does not exist: {relative}")


def load_register(errors: list[str]) -> dict[str, Any]:
    if not REGISTER_PATH.exists():
        fail(errors, f"missing register: {REGISTER_PATH.relative_to(ROOT)}")
        return {}
    try:
        data = json.loads(REGISTER_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(errors, f"invalid JSON: {exc}")
        return {}
    if not isinstance(data, dict):
        fail(errors, "register must be a JSON object")
        return {}
    return data


def validate_source_of_truth(data: dict[str, Any], errors: list[str]) -> None:
    source = data.get("sourceOfTruth")
    if not isinstance(source, dict) or not source:
        fail(errors, "sourceOfTruth must be a non-empty object")
        return
    for key, value in source.items():
        rel = require_string(value, f"sourceOfTruth.{key}", errors)
        if rel:
            validate_local_path(rel, f"sourceOfTruth.{key}", errors)


def validate_scope(data: dict[str, Any], errors: list[str]) -> None:
    scope = data.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return

    if scope.get("routeCardLevel") != "future-boundary-route-probability-gate":
        fail(errors, "scope.routeCardLevel must be future-boundary-route-probability-gate")

    count = require_int(scope.get("routeCardCount"), "scope.routeCardCount", errors)
    if count is not None and count != 4:
        fail(errors, "scope.routeCardCount must be 4")

    families = set(require_list(scope.get("coveredRouteFamilies"), "scope.coveredRouteFamilies", errors))
    if families != REQUIRED_ROUTE_FAMILIES:
        fail(errors, f"scope.coveredRouteFamilies must be {sorted(REQUIRED_ROUTE_FAMILIES)}")

    dimensions = set(require_list(scope.get("requiredGateDimensions"), "scope.requiredGateDimensions", errors))
    if dimensions != REQUIRED_GATE_DIMENSIONS:
        fail(errors, f"scope.requiredGateDimensions must be {sorted(REQUIRED_GATE_DIMENSIONS)}")

    non_claims = require_list(scope.get("nonClaims"), "scope.nonClaims", errors)
    required_phrases = [
        "does not prove route feasibility",
        "does not open calibrated model admission",
        "does not permit individual advice",
        "does not output individual death dates",
    ]
    for phrase in required_phrases:
        if phrase not in non_claims:
            fail(errors, f"scope.nonClaims missing: {phrase}")


def validate_blocked_uses(data: dict[str, Any], errors: list[str]) -> None:
    blocked = set(require_list(data.get("blockedUses"), "blockedUses", errors))
    missing = REQUIRED_BLOCKED_USES - blocked
    if missing:
        fail(errors, f"blockedUses missing: {sorted(missing)}")


def validate_taxonomy(data: dict[str, Any], errors: list[str]) -> None:
    taxonomy = data.get("gateDimensionTaxonomy")
    items = require_list(taxonomy, "gateDimensionTaxonomy", errors)
    seen: set[str] = set()
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            fail(errors, f"gateDimensionTaxonomy[{index}] must be an object")
            continue
        dimension = require_string(item.get("dimension"), f"gateDimensionTaxonomy[{index}].dimension", errors)
        require_string(item.get("meaning"), f"gateDimensionTaxonomy[{index}].meaning", errors)
        if dimension:
            seen.add(dimension)
    if seen != REQUIRED_GATE_DIMENSIONS:
        fail(errors, f"gateDimensionTaxonomy dimensions must be {sorted(REQUIRED_GATE_DIMENSIONS)}")


def validate_reviewed_support(card: dict[str, Any], card_path: str, errors: list[str]) -> None:
    support = card.get("reviewedArtifactSupport")
    if not isinstance(support, dict):
        fail(errors, f"{card_path}.reviewedArtifactSupport must be an object")
        return
    domain_ids = support.get("domainIds")
    if not isinstance(domain_ids, list):
        fail(errors, f"{card_path}.reviewedArtifactSupport.domainIds must be a list")
    count = require_int(
        support.get("minimumReviewedArtifactCount"),
        f"{card_path}.reviewedArtifactSupport.minimumReviewedArtifactCount",
        errors,
    )
    if count is not None and count < 0:
        fail(errors, f"{card_path}.reviewedArtifactSupport.minimumReviewedArtifactCount must be >= 0")
    require_string(support.get("interpretation"), f"{card_path}.reviewedArtifactSupport.interpretation", errors)


def validate_claim_boundary(card: dict[str, Any], card_path: str, errors: list[str]) -> None:
    boundary = card.get("claimBoundary")
    if not isinstance(boundary, dict):
        fail(errors, f"{card_path}.claimBoundary must be an object")
        return
    for field in ["directClaim", "supportedClaim", "forbiddenInference"]:
        require_string(boundary.get(field), f"{card_path}.claimBoundary.{field}", errors)


def validate_effect_chain(card: dict[str, Any], card_path: str, errors: list[str]) -> None:
    chain = card.get("effectChain")
    if not isinstance(chain, dict):
        fail(errors, f"{card_path}.effectChain must be an object")
        return
    for field in ["directEffect", "firstOrderEffect", "secondOrderEffect", "multiOrderEffect"]:
        require_string(chain.get(field), f"{card_path}.effectChain.{field}", errors)
    for field in ["positiveChain", "negativeChain"]:
        items = require_list(chain.get(field), f"{card_path}.effectChain.{field}", errors)
        if len(items) < 4:
            fail(errors, f"{card_path}.effectChain.{field} must contain at least 4 nodes")
        for index, item in enumerate(items):
            require_string(item, f"{card_path}.effectChain.{field}[{index}]", errors)


def validate_gate_coverage(card: dict[str, Any], card_path: str, errors: list[str]) -> None:
    gates = require_list(card.get("gateCoverage"), f"{card_path}.gateCoverage", errors)
    seen_dimensions: set[str] = set()
    gate_ids: set[str] = set()
    for index, gate in enumerate(gates):
        gate_path = f"{card_path}.gateCoverage[{index}]"
        if not isinstance(gate, dict):
            fail(errors, f"{gate_path} must be an object")
            continue
        dimension = require_string(gate.get("dimension"), f"{gate_path}.dimension", errors)
        gate_id = require_string(gate.get("gateId"), f"{gate_path}.gateId", errors)
        require_string(gate.get("gateQuestion"), f"{gate_path}.gateQuestion", errors)
        require_string(gate.get("currentStatus"), f"{gate_path}.currentStatus", errors)
        if dimension:
            seen_dimensions.add(dimension)
            if dimension not in REQUIRED_GATE_DIMENSIONS:
                fail(errors, f"{gate_path}.dimension is not registered: {dimension}")
        if gate_id:
            if gate_id in gate_ids:
                fail(errors, f"{card_path} duplicate gateId: {gate_id}")
            gate_ids.add(gate_id)
    missing_dimensions = REQUIRED_GATE_DIMENSIONS - seen_dimensions
    if missing_dimensions:
        fail(errors, f"{card_path}.gateCoverage missing dimensions: {sorted(missing_dimensions)}")


def validate_route_card(card: Any, index: int, route_ids: set[str], families: set[str], errors: list[str]) -> None:
    card_path = f"routeCards[{index}]"
    if not isinstance(card, dict):
        fail(errors, f"{card_path} must be an object")
        return

    missing_fields = REQUIRED_CARD_FIELDS - set(card)
    if missing_fields:
        fail(errors, f"{card_path} missing fields: {sorted(missing_fields)}")
        return

    route_id = require_string(card.get("routeId"), f"{card_path}.routeId", errors)
    if route_id:
        if route_id in route_ids:
            fail(errors, f"duplicate routeId: {route_id}")
        route_ids.add(route_id)

    family = require_string(card.get("routeFamily"), f"{card_path}.routeFamily", errors)
    if family:
        families.add(family)
        if family not in REQUIRED_ROUTE_FAMILIES:
            fail(errors, f"{card_path}.routeFamily is not required: {family}")

    if card.get("routeStatus") != "route-card-active-model-blocked":
        fail(errors, f"{card_path}.routeStatus must be route-card-active-model-blocked")

    primary = require_string(card.get("primaryDomainPath"), f"{card_path}.primaryDomainPath", errors)
    if primary:
        validate_local_path(primary, f"{card_path}.primaryDomainPath", errors)

    for field in ["supportingDomainPaths", "sourceRefs", "abortGates"]:
        items = require_list(card.get(field), f"{card_path}.{field}", errors)
        for item_index, item in enumerate(items):
            value = require_string(item, f"{card_path}.{field}[{item_index}]", errors)
            if value and field in {"supportingDomainPaths", "sourceRefs"}:
                validate_local_path(value, f"{card_path}.{field}[{item_index}]", errors)
    if len(card.get("abortGates", [])) < 3:
        fail(errors, f"{card_path}.abortGates must contain at least 3 abort gates")

    validate_reviewed_support(card, card_path, errors)
    validate_claim_boundary(card, card_path, errors)
    validate_effect_chain(card, card_path, errors)
    validate_gate_coverage(card, card_path, errors)

    decision = require_string(card.get("modelAdmissionDecision"), f"{card_path}.modelAdmissionDecision", errors)
    if decision and "blocked" not in decision:
        fail(errors, f"{card_path}.modelAdmissionDecision must keep model admission blocked")


def validate_route_cards(data: dict[str, Any], errors: list[str]) -> None:
    cards = require_list(data.get("routeCards"), "routeCards", errors)
    if len(cards) != 4:
        fail(errors, "routeCards must contain exactly 4 cards")

    route_ids: set[str] = set()
    families: set[str] = set()
    for index, card in enumerate(cards):
        validate_route_card(card, index, route_ids, families, errors)

    if families != REQUIRED_ROUTE_FAMILIES:
        fail(errors, f"routeCards families must be {sorted(REQUIRED_ROUTE_FAMILIES)}")


def main() -> int:
    errors: list[str] = []
    data = load_register(errors)
    if data:
        if data.get("schemaVersion") != EXPECTED_SCHEMA:
            fail(errors, f"schemaVersion must be {EXPECTED_SCHEMA}")
        if data.get("status") != EXPECTED_STATUS:
            fail(errors, f"status must be {EXPECTED_STATUS}")
        require_string(data.get("registerId"), "registerId", errors)
        require_string(data.get("purpose"), "purpose", errors)
        validate_source_of_truth(data, errors)
        validate_scope(data, errors)
        validate_blocked_uses(data, errors)
        validate_taxonomy(data, errors)
        validate_route_cards(data, errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    route_count = len(data.get("routeCards", []))
    gate_count = sum(len(card.get("gateCoverage", [])) for card in data.get("routeCards", []))
    print(f"future-boundary route card register audit ok: routes={route_count} gates={gate_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
