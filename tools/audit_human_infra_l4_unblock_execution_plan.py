#!/usr/bin/env python3
"""审计 Human Infra L4 模型解阻执行计划。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PLAN_PATH = ROOT / "docs/reference/human-infra-l4-unblock-execution-plan.json"

SCHEMA = "human-infra.l4-unblock-execution-plan.v1"
STATUS = "active-execution-plan-l4-still-blocked"
PLAN_LINK = "human-infra-l4-unblock-execution-plan.json"
SCRIPT_LINK = "audit_human_infra_l4_unblock_execution_plan.py"

REQUIRED_SOURCE_KEYS = {
    "l4ReadinessBlockerMatrix",
    "l4EvidenceIntakeRegister",
    "l4ValidationCalibrationReportingContract",
    "modelAdmissionContract",
    "modelAdmissionCandidateRegistry",
    "maturityGapRegister",
    "nhanesDisclosureReviewExecutionRegister",
    "nhanesLocalRunEvidenceManifest",
    "nhanesPublicWebNoRealValuesGate",
    "nhatsL4ReadinessRunway",
    "calibrationReadiness",
}
REQUIRED_WORK_ORDERS = [
    "L4WO-01-nhats-governed-access-and-workspace",
    "L4WO-02-nhats-exact-field-value-confirmation",
    "L4WO-03-nhats-real-extraction-cohort-flow",
    "L4WO-04-nhanes-human-disclosure-review",
    "L4WO-05-validation-calibration-diagnostics",
]
REQUIRED_BLOCKERS = {
    "L4B-01-governed-data-access",
    "L4B-02-exact-field-value-confirmation",
    "L4B-03-real-extraction-cohort-flow",
    "L4B-04-disclosure-review-public-output",
    "L4B-05-survey-design-weighted-estimates",
    "L4B-06-validation-calibration",
}
REQUIRED_CANDIDATES = {
    "L4C-NHANES-PUBLIC-LMF-WEIGHTED-DOMAIN",
    "L4C-NHATS-R13-R14-FUNCTIONAL-SURVIVAL",
}
REQUIRED_FALSE_DECISION_KEYS = {
    "l4AggregateCalibratedAdmissionAllowed",
    "publicWeightedDomainOutputAllowed",
    "calibratedPredictionAvailable",
    "individualUseAllowed",
}
REQUIRED_TRUE_DECISION_KEYS = {
    "humanOnlyEvidenceStillRequired",
    "externalGovernedAccessStillRequired",
}
REQUIRED_FORBIDDEN_AFTER_EVIDENCE = {
    "individual prediction",
    "individual death-date output",
}
REQUIRED_INDEX_LINKS = {
    "README.md": PLAN_LINK,
    "docs/AGENTS.md": PLAN_LINK,
    "docs/reference/README.md": PLAN_LINK,
    "docs/reference/human-infra-maturity-roadmap.md": PLAN_LINK,
    "docs/reference/human-infra-maturity-gap-register.json": PLAN_LINK,
    "docs/reference/human-infra-model-admission-candidate-registry.json": PLAN_LINK,
    "docs/reference/human-infra-l4-model-readiness-blocker-matrix.json": PLAN_LINK,
    "Makefile": "l4-unblock-execution-plan-audit",
    "tools/README.md": SCRIPT_LINK,
    "tools/AGENTS.md": SCRIPT_LINK,
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
        fail(errors, f"invalid {context} JSON: {exc}")
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


def require_bool(value: Any, context: str, errors: list[str]) -> bool | None:
    if not isinstance(value, bool):
        fail(errors, f"{context} must be boolean")
        return None
    return value


def require_list(value: Any, context: str, errors: list[str], min_len: int = 1) -> list[Any]:
    if not isinstance(value, list) or len(value) < min_len:
        fail(errors, f"{context} must be a list with at least {min_len} item(s)")
        return []
    return value


def require_string_list(value: Any, context: str, errors: list[str], min_len: int = 1) -> list[str]:
    result: list[str] = []
    for index, item in enumerate(require_list(value, context, errors, min_len)):
        if not isinstance(item, str) or not item.strip():
            fail(errors, f"{context}[{index}] must be a non-empty string")
            continue
        result.append(item)
    return result


def repo_path(relative_path: str, context: str, errors: list[str]) -> Path | None:
    value = require_string(relative_path, context, errors)
    if not value:
        return None
    if value.startswith(("http://", "https://")):
        fail(errors, f"{context} must be a local repository path, not URL")
        return None
    target = (ROOT / value).resolve()
    try:
        target.relative_to(ROOT)
    except ValueError:
        fail(errors, f"{context} escapes repository: {value}")
        return None
    if not target.exists():
        fail(errors, f"{context} does not exist: {value}")
        return None
    return target


def validate_source_of_truth(plan: dict[str, Any], errors: list[str]) -> None:
    source = plan.get("sourceOfTruth")
    if not isinstance(source, dict):
        fail(errors, "sourceOfTruth must be an object")
        return
    if set(source) != REQUIRED_SOURCE_KEYS:
        fail(errors, "sourceOfTruth must contain exactly the required keys")
    for key, value in source.items():
        repo_path(value, f"sourceOfTruth.{key}", errors)


def validate_current_decision(plan: dict[str, Any], errors: list[str]) -> None:
    decision = plan.get("currentDecision")
    if not isinstance(decision, dict):
        fail(errors, "currentDecision must be an object")
        return
    if "L3" not in require_string(decision.get("highestCurrentModelLevel"), "currentDecision.highestCurrentModelLevel", errors):
        fail(errors, "currentDecision.highestCurrentModelLevel must remain L3")
    for key in REQUIRED_FALSE_DECISION_KEYS:
        if require_bool(decision.get(key), f"currentDecision.{key}", errors) is not False:
            fail(errors, f"currentDecision.{key} must be false")
    for key in REQUIRED_TRUE_DECISION_KEYS:
        if require_bool(decision.get(key), f"currentDecision.{key}", errors) is not True:
            fail(errors, f"currentDecision.{key} must be true")
    reason = require_string(decision.get("reason"), "currentDecision.reason", errors)
    for phrase in ["NHANES", "NHATS", "calibration"]:
        if phrase not in reason:
            fail(errors, f"currentDecision.reason must mention {phrase}")


def validate_work_orders(plan: dict[str, Any], errors: list[str]) -> None:
    orders = plan.get("executionWorkOrders")
    if not isinstance(orders, list):
        fail(errors, "executionWorkOrders must be a list")
        return
    observed_order_ids: list[str] = []
    covered_blockers: set[str] = set()
    seen: set[str] = set()
    for index, order in enumerate(orders):
        if not isinstance(order, dict):
            fail(errors, f"executionWorkOrders[{index}] must be an object")
            continue
        work_order_id = require_string(order.get("workOrderId"), f"executionWorkOrders[{index}].workOrderId", errors)
        observed_order_ids.append(work_order_id)
        seen.add(work_order_id)
        if order.get("priority") != index + 1:
            fail(errors, f"{work_order_id}.priority must be {index + 1}")
        status = require_string(order.get("status"), f"{work_order_id}.status", errors)
        if "blocked" not in status:
            fail(errors, f"{work_order_id}.status must remain blocked before direct evidence exists")
        candidate = require_string(order.get("candidatePath"), f"{work_order_id}.candidatePath", errors)
        if candidate not in REQUIRED_CANDIDATES:
            fail(errors, f"{work_order_id}.candidatePath must be a known L4 candidate")
        blocks = set(require_string_list(order.get("blocks"), f"{work_order_id}.blocks", errors))
        if not blocks <= REQUIRED_BLOCKERS:
            fail(errors, f"{work_order_id}.blocks contains unknown blocker")
        covered_blockers.update(blocks)

        dependencies = require_string_list(order.get("dependsOn"), f"{work_order_id}.dependsOn", errors, min_len=0)
        for dependency in dependencies:
            if dependency not in seen:
                fail(errors, f"{work_order_id}.dependsOn contains unmet or forward dependency {dependency}")

        require_string(order.get("executionMode"), f"{work_order_id}.executionMode", errors)
        require_string_list(order.get("requiredDirectEvidence"), f"{work_order_id}.requiredDirectEvidence", errors, min_len=4)
        insufficient = " ".join(require_string_list(order.get("notSufficientEvidence"), f"{work_order_id}.notSufficientEvidence", errors, min_len=3))
        if "alone" not in insufficient and "AI" not in insufficient and "machine-prefill" not in insufficient:
            fail(errors, f"{work_order_id}.notSufficientEvidence must reject placeholder or AI-only evidence")
        commands = require_string_list(order.get("validationCommands"), f"{work_order_id}.validationCommands", errors, min_len=2)
        if not all(command.startswith("make ") for command in commands):
            fail(errors, f"{work_order_id}.validationCommands must be make targets")
        require_string_list(order.get("allowedAfterEvidence"), f"{work_order_id}.allowedAfterEvidence", errors)
        forbidden_text = " ".join(require_string_list(order.get("stillForbiddenAfterEvidence"), f"{work_order_id}.stillForbiddenAfterEvidence", errors, min_len=2))
        for phrase in REQUIRED_FORBIDDEN_AFTER_EVIDENCE:
            if phrase not in forbidden_text:
                fail(errors, f"{work_order_id}.stillForbiddenAfterEvidence must include {phrase!r}")

    if observed_order_ids != REQUIRED_WORK_ORDERS:
        fail(errors, f"executionWorkOrders order mismatch: {observed_order_ids}")
    missing = REQUIRED_BLOCKERS - covered_blockers
    if missing:
        fail(errors, f"executionWorkOrders do not cover blockers: {sorted(missing)}")


def validate_admission_rule(plan: dict[str, Any], errors: list[str]) -> None:
    rule = plan.get("admissionReadinessRule")
    if not isinstance(rule, dict):
        fail(errors, "admissionReadinessRule must be an object")
        return
    minimum = " ".join(require_string_list(rule.get("minimumToOpenL4Review"), "admissionReadinessRule.minimumToOpenL4Review", errors, min_len=4))
    for phrase in ["all executionWorkOrders", "blocker matrix", "candidate registry", "maturity gap"]:
        if phrase not in minimum:
            fail(errors, f"admissionReadinessRule.minimumToOpenL4Review must mention {phrase}")
    false_keys = set(require_string_list(rule.get("mustRemainFalseUntilReview"), "admissionReadinessRule.mustRemainFalseUntilReview", errors, min_len=4))
    missing = REQUIRED_FALSE_DECISION_KEYS - false_keys
    if missing:
        fail(errors, f"admissionReadinessRule.mustRemainFalseUntilReview missing {sorted(missing)}")


def validate_boundaries(plan: dict[str, Any], errors: list[str]) -> None:
    boundaries = " ".join(require_string_list(plan.get("hardBoundaries"), "hardBoundaries", errors, min_len=6))
    for phrase in [
        "No individual death-date output.",
        "No individual medical advice.",
        "No calibration claim before validation and calibration diagnostics.",
        "No AI-only signoff",
    ]:
        if phrase not in boundaries:
            fail(errors, f"hardBoundaries missing {phrase!r}")


def validate_index_links(errors: list[str]) -> None:
    for relative_path, needle in REQUIRED_INDEX_LINKS.items():
        path = ROOT / relative_path
        if not path.exists():
            fail(errors, f"missing index file: {relative_path}")
            continue
        text = path.read_text(encoding="utf-8")
        if needle not in text:
            fail(errors, f"{relative_path} missing reference to {needle}")


def main() -> int:
    errors: list[str] = []
    plan = load_json(PLAN_PATH, errors, "L4 unblock execution plan")
    if plan:
        if plan.get("schemaVersion") != SCHEMA:
            fail(errors, "schemaVersion mismatch")
        if plan.get("status") != STATUS:
            fail(errors, "status mismatch")
        require_string(plan.get("planId"), "planId", errors)
        require_string(plan.get("owner"), "owner", errors)
        validate_source_of_truth(plan, errors)
        validate_current_decision(plan, errors)
        validate_work_orders(plan, errors)
        validate_admission_rule(plan, errors)
        validate_boundaries(plan, errors)
    validate_index_links(errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    order_count = len(plan.get("executionWorkOrders", []))
    print(f"L4 unblock execution plan audit ok: work_orders={order_count} l4=blocked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
