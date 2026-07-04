#!/usr/bin/env python3
"""Validate the NHATS route-value crosswalk assembly protocol."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[4]
MANUAL_DIR = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
)
DEFAULT_PROTOCOL = MANUAL_DIR / "life_path_nhats_route_value_crosswalk_assembly_protocol.json"
DEFAULT_CAPTURE_REVIEW = (
    MANUAL_DIR / "life_path_nhats_colectica_capture_packet_review_execution_register.json"
)
DEFAULT_CAPTURE_TASKS = MANUAL_DIR / "life_path_nhats_colectica_capture_task_register.json"
DEFAULT_ROUTE_READINESS = MANUAL_DIR / "life_path_nhats_route_classifier_readiness.json"
DEFAULT_OUT = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhats-route-value-crosswalk-assembly-validation.json"
)

REQUIRED_ROUTE_FIELDS = {
    "identity_join_key",
    "round13_baseline_eligibility",
    "round14_interview_status",
    "proxy_status",
    "facility_residential_status",
    "death_decedent_indicator",
    "nonresponse_missing_code",
    "design_weight_linkage",
    "disclosure_cell_count",
}
REQUIRED_TRUE_DECISIONS = {
    "assemblyProtocolReady",
    "sensitiveDeathDateFieldsExcluded",
}
REQUIRED_FALSE_DECISIONS = {
    "reviewedCapturePacketsAttached",
    "valueLabelsConfirmed",
    "questionTextConfirmed",
    "universeSkipLogicConfirmed",
    "routeValueCrosswalkConfirmed",
    "variableSpecificMissingCodeMapConfirmed",
    "secondReviewerSignoff",
    "routeClassifierAllowed",
    "realExtractionAllowed",
    "aggregateCohortFlowAllowed",
    "weightedRouteCountsAllowed",
    "publicExportAllowed",
    "calibrationAllowed",
    "individualPredictionAllowed",
}
PROHIBITED_KEYS = {
    "rawValueLabels",
    "rawColecticaExport",
    "credential",
    "cookie",
    "sessionToken",
    "deathDate",
    "deathMonth",
    "deathYear",
    "predictedDeathDate",
    "individualPrediction",
    "rowLevelData",
    "realWeightedCount",
}


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def repo_rel(path: Path) -> str:
    return str(path.resolve().relative_to(REPO_ROOT))


def row_ids(rows: Any, key: str = "id") -> set[str]:
    if not isinstance(rows, list):
        return set()
    return {
        str(row[key])
        for row in rows
        if isinstance(row, dict) and isinstance(row.get(key), str)
    }


def collect_keys(value: Any) -> set[str]:
    keys: set[str] = set()
    if isinstance(value, dict):
        for key, child in value.items():
            keys.add(str(key))
            keys.update(collect_keys(child))
    elif isinstance(value, list):
        for child in value:
            keys.update(collect_keys(child))
    return keys


def has_text(value: Any, needle: str) -> bool:
    return needle.lower() in json.dumps(value, ensure_ascii=False).lower()


def add_check(checks: list[dict[str, Any]], check_id: str, passed: bool, detail: str) -> None:
    checks.append(
        {
            "id": check_id,
            "status": "PASS" if passed else "FAIL",
            "detail": detail,
        }
    )


def summarize(checks: list[dict[str, Any]]) -> dict[str, int]:
    return {
        "pass": sum(1 for check in checks if check["status"] == "PASS"),
        "fail": sum(1 for check in checks if check["status"] == "FAIL"),
    }


def expected_task_ids(capture_tasks: dict[str, Any]) -> dict[str, set[str]]:
    groups = capture_tasks.get("captureTaskGroups")
    expected: dict[str, set[str]] = {}
    if not isinstance(groups, list):
        return expected
    for group in groups:
        if not isinstance(group, dict):
            continue
        field_id = group.get("requiredRouteFieldId")
        tasks = group.get("tasks")
        if not isinstance(field_id, str) or not isinstance(tasks, list):
            continue
        expected[field_id] = {
            str(task["taskId"])
            for task in tasks
            if isinstance(task, dict) and isinstance(task.get("taskId"), str)
        }
    return expected


def validate_protocol(
    protocol: dict[str, Any],
    capture_review: dict[str, Any],
    capture_tasks: dict[str, Any],
    route_readiness: dict[str, Any],
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    add_check(
        checks,
        "schema-version",
        protocol.get("schemaVersion")
        == "human-infra.life-path-nhats-route-value-crosswalk-assembly-protocol.v1",
        f"schemaVersion={protocol.get('schemaVersion')!r}",
    )
    identity_ok = (
        protocol.get("sourceId") == "nhats"
        and protocol.get("status") == "protocol-only-crosswalk-not-assembled"
        and protocol.get("capturePacketReviewExecutionRegisterId")
        == capture_review.get("executionRegisterId")
        and protocol.get("captureTaskRegisterId") == capture_tasks.get("taskRegisterId")
        and protocol.get("routeClassifierReadinessId") == route_readiness.get("readinessId")
    )
    add_check(
        checks,
        "protocol-identity-and-upstreams",
        identity_ok,
        "protocol must bind NHATS, capture review execution, capture task register and route-classifier readiness",
    )

    decision = protocol.get("currentDecision")
    decision_ok = isinstance(decision, dict)
    if isinstance(decision, dict):
        for key in REQUIRED_TRUE_DECISIONS:
            decision_ok = decision_ok and decision.get(key) is True
        for key in REQUIRED_FALSE_DECISIONS:
            decision_ok = decision_ok and decision.get(key) is False
    add_check(
        checks,
        "decision-boundary",
        decision_ok,
        "only the assembly protocol and sensitive death-field exclusion may be true; every data/model action must remain false",
    )

    bindings = protocol.get("sourceBindings")
    binding_paths = {
        str(row.get("path", ""))
        for row in bindings
        if isinstance(row, dict)
    } if isinstance(bindings, list) else set()
    binding_ok = {
        "domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_colectica_capture_packet_review_execution_register.json",
        "domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_colectica_capture_task_register.json",
        "domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_route_classifier_readiness.json",
        "domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_missingness_route_protocol.json",
        "domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_colectica_value_label_review_execution_register.json",
    }.issubset(binding_paths)
    add_check(
        checks,
        "source-bindings",
        binding_ok,
        "source bindings must include the five upstream NHATS route/capture/value-label records",
    )

    units = protocol.get("assemblyUnits")
    unit_fields = row_ids(units, key="requiredRouteFieldId")
    expected_tasks = expected_task_ids(capture_tasks)
    units_ok = isinstance(units, list) and len(units) == 9
    if isinstance(units, list):
        for unit in units:
            if not isinstance(unit, dict):
                units_ok = False
                continue
            field_id = unit.get("requiredRouteFieldId")
            task_ids = set(unit.get("sourceTaskIds", []))
            units_ok = (
                units_ok
                and isinstance(field_id, str)
                and field_id in REQUIRED_ROUTE_FIELDS
                and task_ids == expected_tasks.get(field_id, set())
                and unit.get("assemblyStatus") == "pending-reviewed-capture-packets"
                and unit.get("reviewedCapturePacketRequired") is True
                and unit.get("valueLabelRowsAttached") is False
                and unit.get("routeValueRowsAttached") is False
                and unit.get("variableSpecificMissingCodeRowsAttached") is False
                and unit.get("secondReviewerSignoff") is False
                and unit.get("routeClassifierAllowed") is False
            )
    add_check(
        checks,
        "assembly-units-cover-route-fields",
        REQUIRED_ROUTE_FIELDS == unit_fields and units_ok,
        f"missing={sorted(REQUIRED_ROUTE_FIELDS - unit_fields)}",
    )

    death_unit = next(
        (
            unit
            for unit in units or []
            if isinstance(unit, dict)
            and unit.get("requiredRouteFieldId") == "death_decedent_indicator"
        ),
        {},
    )
    add_check(
        checks,
        "death-sensitive-field-exclusion",
        isinstance(death_unit, dict)
        and death_unit.get("sensitiveDeathDateFieldsExcluded") is True
        and has_text(death_unit, "death month/year"),
        "death/decedent unit must explicitly exclude sensitive month/year timing fields",
    )

    summary = protocol.get("summary")
    summary_ok = (
        isinstance(summary, dict)
        and summary.get("assemblyUnitCount") == 9
        and summary.get("routeFieldFamiliesCovered") == 9
        and summary.get("reviewedCapturePacketsAttached") == 0
        and summary.get("routeValueRowsConfirmed") == 0
        and summary.get("variableSpecificMissingCodeMapsConfirmed") == 0
        and summary.get("secondReviewerSignoffs") == 0
        and summary.get("routeClassifierAdmissions") == 0
        and summary.get("realExtractionAdmissions") == 0
        and summary.get("calibrationAdmissions") == 0
        and summary.get("individualPredictionAdmissions") == 0
    )
    add_check(
        checks,
        "summary-counts-stay-blocked",
        summary_ok,
        "summary must keep reviewed packets, rows, maps, signoffs and all admissions at zero",
    )

    blocked_until = protocol.get("blockedUntil")
    blocked_ok = (
        isinstance(blocked_until, list)
        and has_text(blocked_until, "capture packet")
        and has_text(blocked_until, "value labels")
        and has_text(blocked_until, "Route-value")
        and has_text(blocked_until, "Variable-specific missing-code")
        and has_text(blocked_until, "second reviewer")
    )
    add_check(
        checks,
        "blocked-until-evidence",
        blocked_ok,
        "blockedUntil must require packets, labels, crosswalk rows, variable-specific missing-code maps and second review",
    )

    prohibited = protocol.get("prohibitedActions")
    prohibited_ok = (
        isinstance(prohibited, list)
        and has_text(prohibited, "candidate variable names")
        and has_text(prohibited, "-1/-7/-8/-9")
        and has_text(prohibited, "credentials")
        and has_text(prohibited, "death month")
        and has_text(prohibited, "route-classifier code")
        and has_text(prohibited, "individual prediction")
    )
    add_check(
        checks,
        "prohibited-actions",
        prohibited_ok,
        "protocol must prohibit inference from names, negative-code overuse, credential/raw storage, sensitive death fields and model actions",
    )

    prohibited_keys_found = collect_keys(protocol) & PROHIBITED_KEYS
    add_check(
        checks,
        "no-prohibited-key-shapes",
        not prohibited_keys_found,
        f"prohibited_keys_found={sorted(prohibited_keys_found)}",
    )

    add_check(
        checks,
        "inherits-empty-capture-review",
        capture_review.get("status")
        == "execution-register-empty-controlled-capture-not-started"
        and capture_review.get("summary", {}).get("packetsReceived") == 0
        and capture_review.get("summary", {}).get("slotsClosed") == 0,
        "upstream capture review execution must still have zero packets and zero closed slots",
    )

    add_check(
        checks,
        "downstream-route-classifier-stays-blocked",
        route_readiness.get("currentDecision", {}).get("routeClassifierReady") is False
        and route_readiness.get("currentDecision", {}).get("routeValueCrosswalkConfirmed") is False
        and route_readiness.get("currentDecision", {}).get(
            "variableSpecificMissingCodeMapConfirmed"
        )
        is False,
        "downstream route-classifier readiness must remain blocked by crosswalk and missing-code map gates",
    )
    return checks


def build_report(
    protocol_path: Path,
    capture_review_path: Path,
    capture_tasks_path: Path,
    route_readiness_path: Path,
) -> dict[str, Any]:
    protocol = load_json(protocol_path)
    capture_review = load_json(capture_review_path)
    capture_tasks = load_json(capture_tasks_path)
    route_readiness = load_json(route_readiness_path)
    checks = validate_protocol(protocol, capture_review, capture_tasks, route_readiness)
    summary = summarize(checks)
    return {
        "schemaVersion": "human-infra.validation-report.v1",
        "validationId": "life-path-nhats-route-value-crosswalk-assembly-validation",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "overallStatus": "PASS" if summary["fail"] == 0 else "FAIL",
        "summary": summary,
        "protocol": {
            "path": repo_rel(protocol_path),
            "sha256": sha256_file(protocol_path),
            "protocolId": protocol.get("protocolId"),
            "status": protocol.get("status"),
        },
        "upstreams": [
            {
                "path": repo_rel(capture_review_path),
                "sha256": sha256_file(capture_review_path),
                "id": capture_review.get("executionRegisterId"),
            },
            {
                "path": repo_rel(capture_tasks_path),
                "sha256": sha256_file(capture_tasks_path),
                "id": capture_tasks.get("taskRegisterId"),
            },
            {
                "path": repo_rel(route_readiness_path),
                "sha256": sha256_file(route_readiness_path),
                "id": route_readiness.get("readinessId"),
            },
        ],
        "assemblySummary": protocol.get("summary"),
        "checks": checks,
        "boundary": "This validation proves only that a blocked route-value crosswalk assembly protocol exists, covers the nine route-field families, and keeps all rows, maps, signoffs, classifier, extraction, calibration and individual prediction admissions at zero. It does not prove Colectica login, reviewed packets, value labels, route values, real missing-code maps, route classifier readiness or model validity.",
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate NHATS route-value crosswalk assembly protocol."
    )
    parser.add_argument("--protocol", type=Path, default=DEFAULT_PROTOCOL)
    parser.add_argument("--capture-review", type=Path, default=DEFAULT_CAPTURE_REVIEW)
    parser.add_argument("--capture-tasks", type=Path, default=DEFAULT_CAPTURE_TASKS)
    parser.add_argument("--route-readiness", type=Path, default=DEFAULT_ROUTE_READINESS)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report = build_report(
        args.protocol,
        args.capture_review,
        args.capture_tasks,
        args.route_readiness,
    )
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report["summary"], ensure_ascii=False))
    return 0 if report["overallStatus"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
