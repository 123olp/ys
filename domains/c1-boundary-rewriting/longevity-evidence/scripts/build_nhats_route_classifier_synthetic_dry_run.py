#!/usr/bin/env python3
"""Run a synthetic-only NHATS route-classifier dry run.

This local report reuses the missingness-route synthetic envelope validator to
prove that the route-classifier logic can be exercised on synthetic cases while
the real NHATS route classifier, extraction, aggregation, calibration and
individual prediction gates remain blocked.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from validate_nhats_missingness_route_map import (
    DEFAULT_PROTOCOL as DEFAULT_MISSINGNESS_PROTOCOL,
    DEFAULT_TEST_CASES as DEFAULT_MISSINGNESS_TEST_CASES,
    load_json,
    repo_rel,
    validate_protocol,
    validate_route_envelope,
)
from validate_nhats_route_classifier_readiness import (
    DEFAULT_REGISTER as DEFAULT_ROUTE_READINESS,
)


REPO_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_CROSSWALK_HANDOFF = (
    REPO_ROOT
    / "build"
    / "reports"
    / "nhats-route-value-crosswalk-entry-handoff"
    / "draft-nhats-route-value-crosswalk-identity_join_key-handoff.json"
)
DEFAULT_OUT = (
    REPO_ROOT
    / "build"
    / "reports"
    / "nhats-route-classifier-synthetic-dry-run"
    / "route-classifier-synthetic-dry-run.json"
)
DEFAULT_SUMMARY_OUT = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhats-route-classifier-synthetic-dry-run-validation.json"
)
DRY_RUN_SCHEMA = "human-infra.life-path-nhats-route-classifier-synthetic-dry-run.v1"
REQUIRED_FALSE_DECISIONS = {
    "routeClassifierReady",
    "classifierCodeAllowed",
    "realExtractionAllowed",
    "aggregateCohortFlowAllowed",
    "weightedRouteCountsAllowed",
    "publicExportAllowed",
    "calibrationAllowed",
    "individualPredictionAllowed",
}
HANDOFF_REQUIRED_FALSE_DECISIONS = {
    "reviewHandoffAllowed",
    "realEntryAttached",
    "assemblyUnitClosureAllowed",
    "routeClassifierAllowed",
    "realExtractionAllowed",
    "aggregateCohortFlowAllowed",
    "weightedRouteCountsAllowed",
    "publicExportAllowed",
    "calibrationAllowed",
    "individualPredictionAllowed",
}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def evaluate_cases(
    *,
    protocol: dict[str, Any],
    test_cases: dict[str, Any],
) -> tuple[list[dict[str, Any]], list[str]]:
    failures: list[str] = []
    protocol_reasons = validate_protocol(protocol)
    if protocol_reasons:
        failures.extend(f"protocol: {reason}" for reason in protocol_reasons)

    boundary = test_cases.get("currentBoundary")
    if test_cases.get("schemaVersion") != "human-infra.life-path-nhats-missingness-route-test-cases.v1":
        failures.append("test cases schemaVersion mismatch")
    if test_cases.get("sourceId") != protocol.get("sourceId"):
        failures.append("test cases sourceId must match protocol")
    if test_cases.get("protocolId") != protocol.get("protocolId"):
        failures.append("test cases protocolId must match protocol")
    if not isinstance(boundary, dict):
        failures.append("test cases currentBoundary must be an object")
    elif (
        boundary.get("containsRealNhatsData") is not False
        or boundary.get("containsSyntheticOnly") is not True
        or boundary.get("routeMapProofOnly") is not True
        or boundary.get("calibrationAllowed") is not False
        or boundary.get("individualPredictionAllowed") is not False
    ):
        failures.append("test cases boundary must remain synthetic-only and non-calibrated")

    rows: list[dict[str, Any]] = []
    cases = test_cases.get("cases")
    if not isinstance(cases, list) or not cases:
        failures.append("synthetic route test cases must be a non-empty list")
        return rows, failures

    for case in cases:
        if not isinstance(case, dict):
            failures.append("each synthetic route case must be an object")
            continue
        case_id = case.get("id")
        expected = case.get("expectedDecision")
        envelope = case.get("routeEnvelope")
        if not isinstance(envelope, dict):
            observed, route_class, reasons = (
                "block-route-classification",
                None,
                ["routeEnvelope must be an object"],
            )
        else:
            observed, route_class, reasons = validate_route_envelope(envelope, protocol)
        status = "PASS" if observed == expected else "FAIL"
        if status == "FAIL":
            failures.append(f"{case_id}: expected {expected}, observed {observed}")
        rows.append(
            {
                "caseId": case_id,
                "expectedDecision": expected,
                "observedDecision": observed,
                "observedRouteClass": route_class,
                "status": status,
                "reasons": reasons,
            }
        )
    return rows, failures


def readiness_blocked(readiness: dict[str, Any]) -> tuple[bool, list[str]]:
    failures: list[str] = []
    decision = readiness.get("currentDecision")
    if readiness.get("status") != "blocked-colectica-and-real-data-required":
        failures.append("route-classifier readiness status must remain blocked")
    if not isinstance(decision, dict):
        failures.append("route-classifier readiness currentDecision must be an object")
        return False, failures
    for key in sorted(REQUIRED_FALSE_DECISIONS):
        if decision.get(key) is not False:
            failures.append(f"route-classifier readiness {key} must remain false")
    return not failures, failures


def handoff_blocked(handoff: dict[str, Any]) -> tuple[bool, list[str]]:
    failures: list[str] = []
    decision = handoff.get("currentDecision")
    if handoff.get("status") != "pass":
        failures.append("crosswalk handoff status must be pass")
    if not isinstance(decision, dict):
        failures.append("crosswalk handoff currentDecision must be an object")
        return False, failures
    for key in sorted(HANDOFF_REQUIRED_FALSE_DECISIONS):
        if decision.get(key) is not False:
            failures.append(f"crosswalk handoff {key} must remain false")
    if decision.get("modelG4") != "blocked":
        failures.append("crosswalk handoff modelG4 must remain blocked")
    return not failures, failures


def build_report(
    *,
    readiness_path: Path,
    missingness_protocol_path: Path,
    missingness_test_cases_path: Path,
    crosswalk_handoff_path: Path,
) -> dict[str, Any]:
    readiness = load_json(readiness_path)
    protocol = load_json(missingness_protocol_path)
    test_cases = load_json(missingness_test_cases_path)
    handoff = load_json(crosswalk_handoff_path)

    case_rows, failures = evaluate_cases(protocol=protocol, test_cases=test_cases)
    readiness_ok, readiness_failures = readiness_blocked(readiness)
    handoff_ok, handoff_failures = handoff_blocked(handoff)
    failures.extend(readiness_failures)
    failures.extend(handoff_failures)

    allowed_count = sum(1 for row in case_rows if row["observedDecision"] == "allow-route-classification")
    blocked_count = sum(1 for row in case_rows if row["observedDecision"] == "block-route-classification")
    pass_count = sum(1 for row in case_rows if row["status"] == "PASS")
    observed_classes = sorted(
        {
            str(row["observedRouteClass"])
            for row in case_rows
            if isinstance(row.get("observedRouteClass"), str)
        }
    )
    status = "pass" if not failures and readiness_ok and handoff_ok else "fail"

    return {
        "schemaVersion": DRY_RUN_SCHEMA,
        "dryRunId": "nhats-r13-r14-route-classifier-synthetic-dry-run",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "status": status,
        "sourceRefs": {
            "routeClassifierReadinessPath": repo_rel(readiness_path),
            "routeClassifierReadinessSha256": sha256_file(readiness_path),
            "missingnessRouteProtocolPath": repo_rel(missingness_protocol_path),
            "missingnessRouteProtocolSha256": sha256_file(missingness_protocol_path),
            "missingnessRouteTestCasesPath": repo_rel(missingness_test_cases_path),
            "missingnessRouteTestCasesSha256": sha256_file(missingness_test_cases_path),
            "routeValueCrosswalkEntryHandoffPath": repo_rel(crosswalk_handoff_path),
            "routeValueCrosswalkEntryHandoffSha256": sha256_file(crosswalk_handoff_path),
            "classifierLogicSource": "domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_missingness_route_map.py::validate_route_envelope",
        },
        "currentDecision": {
            "syntheticDryRunGenerated": True,
            "syntheticRouteClassifierLogicRunnable": status == "pass",
            "routeClassifierReady": False,
            "classifierCodeAllowed": False,
            "realExtractionAllowed": False,
            "aggregateCohortFlowAllowed": False,
            "weightedRouteCountsAllowed": False,
            "publicExportAllowed": False,
            "calibrationAllowed": False,
            "individualPredictionAllowed": False,
            "modelG4": "blocked",
            "reason": (
                "Synthetic route envelope logic can be exercised locally, but real NHATS "
                "route classification remains blocked by Colectica review, route-value "
                "crosswalk, variable-specific missing-code map, real data access, survey "
                "design, disclosure review and second-reviewer gates."
            ),
        },
        "summary": {
            "caseCount": len(case_rows),
            "pass": pass_count,
            "fail": len(case_rows) - pass_count,
            "allowedCount": allowed_count,
            "blockedCount": blocked_count,
            "observedRouteClasses": observed_classes,
            "crosswalkHandoffState": handoff.get("currentDecision", {}).get("handoffState"),
            "crosswalkReviewHandoffAllowed": handoff.get("currentDecision", {}).get(
                "reviewHandoffAllowed"
            ),
        },
        "cases": case_rows,
        "hardBoundaries": [
            "This dry-run only evaluates synthetic route envelopes.",
            "It does not read or write raw NHATS rows, weighted route counts, individual mortality timestamps or individual predictions.",
            "A passing synthetic dry-run cannot promote routeClassifierReady, classifierCodeAllowed, extraction, aggregation, calibration or public export.",
        ],
        "failures": failures,
    }


def build_public_summary(report: dict[str, Any]) -> dict[str, Any]:
    """Build a deterministic tracked summary without copying volatile report fields."""

    source_refs = report["sourceRefs"]
    return {
        "schemaVersion": (
            "human-infra.life-path-nhats-route-classifier-synthetic-dry-run-validation.v1"
        ),
        "status": report["status"].upper(),
        "sourceRefs": {
            "routeClassifierReadinessPath": source_refs["routeClassifierReadinessPath"],
            "routeClassifierReadinessSha256": source_refs["routeClassifierReadinessSha256"],
            "missingnessRouteProtocolPath": source_refs["missingnessRouteProtocolPath"],
            "missingnessRouteProtocolSha256": source_refs[
                "missingnessRouteProtocolSha256"
            ],
            "missingnessRouteTestCasesPath": source_refs["missingnessRouteTestCasesPath"],
            "missingnessRouteTestCasesSha256": source_refs[
                "missingnessRouteTestCasesSha256"
            ],
            "classifierLogicSource": source_refs["classifierLogicSource"],
        },
        "currentDecision": {
            "syntheticRouteClassifierLogicRunnable": report["currentDecision"][
                "syntheticRouteClassifierLogicRunnable"
            ],
            "routeClassifierReady": report["currentDecision"]["routeClassifierReady"],
            "classifierCodeAllowed": report["currentDecision"]["classifierCodeAllowed"],
            "realExtractionAllowed": report["currentDecision"]["realExtractionAllowed"],
            "aggregateCohortFlowAllowed": report["currentDecision"][
                "aggregateCohortFlowAllowed"
            ],
            "weightedRouteCountsAllowed": report["currentDecision"][
                "weightedRouteCountsAllowed"
            ],
            "publicExportAllowed": report["currentDecision"]["publicExportAllowed"],
            "calibrationAllowed": report["currentDecision"]["calibrationAllowed"],
            "individualPredictionAllowed": report["currentDecision"][
                "individualPredictionAllowed"
            ],
            "modelG4": report["currentDecision"]["modelG4"],
        },
        "summary": report["summary"],
        "caseResults": [
            {
                "caseId": row["caseId"],
                "expectedDecision": row["expectedDecision"],
                "observedDecision": row["observedDecision"],
                "observedRouteClass": row["observedRouteClass"],
                "status": row["status"],
            }
            for row in report["cases"]
        ],
        "hardBoundaries": report["hardBoundaries"],
        "failures": report["failures"],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--route-readiness", type=Path, default=DEFAULT_ROUTE_READINESS)
    parser.add_argument("--missingness-protocol", type=Path, default=DEFAULT_MISSINGNESS_PROTOCOL)
    parser.add_argument("--missingness-test-cases", type=Path, default=DEFAULT_MISSINGNESS_TEST_CASES)
    parser.add_argument("--crosswalk-handoff", type=Path, default=DEFAULT_CROSSWALK_HANDOFF)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--summary-out", type=Path, default=DEFAULT_SUMMARY_OUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        report = build_report(
            readiness_path=args.route_readiness.resolve(),
            missingness_protocol_path=args.missingness_protocol.resolve(),
            missingness_test_cases_path=args.missingness_test_cases.resolve(),
            crosswalk_handoff_path=args.crosswalk_handoff.resolve(),
        )
        out = args.out.resolve()
        write_json(out, report)
        summary_out = args.summary_out.resolve()
        write_json(summary_out, build_public_summary(report))
        if report["status"] != "pass":
            for failure in report["failures"]:
                print(f"ERROR: {failure}", file=sys.stderr)
            return 1
        print(
            "NHATS route-classifier synthetic dry-run ok: "
            f"cases={report['summary']['caseCount']} "
            f"allowed={report['summary']['allowedCount']} "
            f"blocked={report['summary']['blockedCount']} model_g4=blocked"
        )
        return 0
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
