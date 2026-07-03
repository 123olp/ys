#!/usr/bin/env python3
"""Validate the NHATS L4 readiness runway.

The runway is a gate register, not a model. It proves that the repository can
say exactly why NHATS remains below L4 calibrated-model admission.
"""

from __future__ import annotations

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
DEFAULT_RUNWAY = MANUAL_DIR / "life_path_nhats_l4_readiness_runway.json"
DEFAULT_OUT = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhats-l4-readiness-runway-validation.json"
)

REQUIRED_SCHEMA = "human-infra.life-path-nhats-l4-readiness-runway.v1"
REQUIRED_STATUS = "runway-only-l4-blocked"
REQUIRED_GATE_IDS = {
    "RW-G01-estimand-and-model-boundary",
    "RW-G02-controlled-access-and-storage",
    "RW-G03-colectica-authenticated-capture",
    "RW-G04-exact-variable-and-value-label-confirmation",
    "RW-G05-endpoint-route-and-missingness-classifier",
    "RW-G06-preoutcome-aggregation-rules",
    "RW-G07-survey-design-and-weighting",
    "RW-G08-disclosure-control-and-public-output",
    "RW-G09-real-extraction-and-cohort-flow",
    "RW-G10-validation-and-calibration",
    "RW-G11-model-admission-registry-update",
    "RW-G12-individual-use-hard-abort",
}
REQUIRED_SOURCE_BINDINGS = {
    "modelAdmissionContractPath",
    "modelAdmissionCandidateRegistryPath",
    "calibrationReadinessPath",
    "acquisitionReadinessPath",
    "controlledStorageDestructionPlanPath",
    "syntheticStorageDestructionDrillPath",
    "fileTierTablePath",
    "firstEstimandProtocolPath",
    "variableConfirmationMatrixPath",
    "cohortFlowEndpointProtocolPath",
    "disclosureControlPolicyPath",
    "surveyDesignProtocolPath",
    "missingnessRouteProtocolPath",
    "routeFieldDiscoveryRegisterPath",
    "colecticaValueLabelReviewProtocolPath",
    "colecticaValueLabelReviewExecutionRegisterPath",
    "colecticaAccessRouteProbeRegisterPath",
    "colecticaAuthenticatedCaptureTemplatePath",
    "l2VariableFamilyAdmissionRegisterPath",
    "preOutcomeAggregationProtocolPath",
}
REQUIRED_FALSE_DECISIONS = {
    "governedDataAccessExecuted",
    "controlledWorkspaceExecuted",
    "colecticaAuthenticatedCapturesComplete",
    "exactVariablesConfirmed",
    "valueLabelsConfirmed",
    "questionTextUniverseSkipLogicConfirmed",
    "routeClassifierReady",
    "realExtractionAllowed",
    "cohortFlowReady",
    "surveyDesignReady",
    "weightedEstimatesAllowed",
    "disclosureReviewComplete",
    "externalValidationReady",
    "calibrationAllowed",
    "l4AdmissionAllowed",
    "individualPredictionAllowed",
}
REQUIRED_TRUE_DECISIONS = {
    "narrowEstimandSelected",
    "l2VariableFamiliesMapped",
    "preOutcomeAggregationRulesFrozen",
    "l4RunwayAuditable",
}
PROHIBITED_KEYS = {
    "rawNhatsData",
    "rowLevelData",
    "deathDate",
    "individualDeathDate",
    "predictedDeathDate",
    "hazardRatio",
    "coefficient",
    "calibratedRisk",
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


def add_check(checks: list[dict[str, Any]], check_id: str, passed: bool, detail: str) -> None:
    checks.append({"id": check_id, "status": "PASS" if passed else "FAIL", "detail": detail})


def summarize(checks: list[dict[str, Any]]) -> dict[str, int]:
    return {
        "pass": sum(1 for check in checks if check["status"] == "PASS"),
        "fail": sum(1 for check in checks if check["status"] == "FAIL"),
    }


def source_path(relative_path: str) -> Path:
    path = (REPO_ROOT / relative_path).resolve()
    path.relative_to(REPO_ROOT)
    return path


def validate_runway(runway: dict[str, Any]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []

    add_check(
        checks,
        "schema-version",
        runway.get("schemaVersion") == REQUIRED_SCHEMA,
        f"schemaVersion={runway.get('schemaVersion')!r}",
    )
    add_check(
        checks,
        "identity-and-status",
        runway.get("sourceId") == "nhats"
        and runway.get("status") == REQUIRED_STATUS
        and runway.get("currentDecision", {}).get("l4AdmissionAllowed") is False,
        "runway must be NHATS-specific and keep L4 admission blocked",
    )

    decision = runway.get("currentDecision")
    decision_ok = isinstance(decision, dict)
    if decision_ok:
        for field in REQUIRED_TRUE_DECISIONS:
            decision_ok = decision_ok and decision.get(field) is True
        for field in REQUIRED_FALSE_DECISIONS:
            decision_ok = decision_ok and decision.get(field) is False
    add_check(
        checks,
        "current-decision-boundary",
        decision_ok,
        "runway may be auditable, but governed access, field confirmation, real extraction, calibration, L4 and individual prediction must remain false",
    )

    source_bindings = runway.get("sourceBindings")
    sources_ok = isinstance(source_bindings, dict) and REQUIRED_SOURCE_BINDINGS.issubset(source_bindings)
    missing_sources = sorted(REQUIRED_SOURCE_BINDINGS - set(source_bindings or {}))
    add_check(
        checks,
        "source-bindings-present",
        sources_ok,
        f"missing={missing_sources}",
    )
    source_hashes: dict[str, str] = {}
    if isinstance(source_bindings, dict):
        for key, relative in source_bindings.items():
            if not isinstance(relative, str):
                add_check(checks, f"source-{key}", False, "source path must be string")
                continue
            try:
                path = source_path(relative)
            except ValueError:
                add_check(checks, f"source-{key}", False, "source path escapes repository")
                continue
            add_check(
                checks,
                f"source-{key}",
                path.exists(),
                relative,
            )
            if path.exists():
                source_hashes[relative] = sha256_file(path)

    gates = runway.get("readinessGates")
    observed_gate_ids: set[str] = set()
    status_counts = {"pass": 0, "partial": 0, "blocked": 0}
    gate_shape_ok = isinstance(gates, list) and len(gates) == len(REQUIRED_GATE_IDS)
    if isinstance(gates, list):
        for index, gate in enumerate(gates):
            if not isinstance(gate, dict):
                gate_shape_ok = False
                continue
            gate_id = gate.get("gateId")
            if isinstance(gate_id, str):
                observed_gate_ids.add(gate_id)
            status = gate.get("status")
            if status in status_counts:
                status_counts[status] += 1
            else:
                gate_shape_ok = False
            if status in {"partial", "blocked"} and not gate.get("missingEvidence"):
                gate_shape_ok = False
            if status == "blocked" and gate.get("blocksL4") is not True:
                gate_shape_ok = False
            if not isinstance(gate.get("admissionGateRefs"), list) or not gate["admissionGateRefs"]:
                gate_shape_ok = False
            if not isinstance(gate.get("evidencePaths"), list) or not gate["evidencePaths"]:
                gate_shape_ok = False
            if not isinstance(gate.get("nextAction"), str) or not gate["nextAction"].strip():
                gate_shape_ok = False
            for relative in gate.get("evidencePaths", []):
                if not isinstance(relative, str):
                    gate_shape_ok = False
                    continue
                try:
                    path = source_path(relative)
                except ValueError:
                    gate_shape_ok = False
                    continue
                if not path.exists():
                    gate_shape_ok = False
    add_check(
        checks,
        "readiness-gates-complete",
        gate_shape_ok and observed_gate_ids == REQUIRED_GATE_IDS,
        f"observed={len(observed_gate_ids)} status_counts={status_counts}",
    )
    add_check(
        checks,
        "l4-remains-blocked",
        status_counts["blocked"] >= 7
        and status_counts["partial"] >= 2
        and status_counts["pass"] >= 3
        and runway.get("summary", {}).get("l4AdmissionAllowed") is False
        and runway.get("summary", {}).get("calibratedPredictionAvailable") is False
        and runway.get("summary", {}).get("individualUseAllowed") is False,
        f"status_counts={status_counts}",
    )

    sequence = runway.get("nextRunnableSequence")
    add_check(
        checks,
        "next-runnable-sequence",
        isinstance(sequence, list)
        and len(sequence) >= 6
        and "Colectica" in " ".join(str(item) for item in sequence),
        "runway must expose the next concrete L4 unlock sequence",
    )

    hard_boundaries = set(runway.get("hardBoundaries", []))
    add_check(
        checks,
        "hard-boundaries",
        {
            "no raw NHATS data in repository",
            "no credentials in repository",
            "no row-level output",
            "no individual death-date output",
            "no calibration claim before L4 gates pass",
        }.issubset(hard_boundaries),
        "hard boundaries must block raw data, credentials, row-level output, individual output and calibration claims",
    )

    forbidden_present = sorted(PROHIBITED_KEYS & collect_keys(runway))
    add_check(
        checks,
        "no-prohibited-output-keys",
        not forbidden_present,
        f"forbidden_present={forbidden_present}",
    )

    return checks


def build_report(runway_path: Path, output_path: Path) -> dict[str, Any]:
    runway = load_json(runway_path)
    checks = validate_runway(runway)
    summary = summarize(checks)
    source_bindings = runway.get("sourceBindings", {})
    source_hashes: dict[str, str] = {}
    if isinstance(source_bindings, dict):
        for relative in source_bindings.values():
            if isinstance(relative, str):
                path = source_path(relative)
                if path.exists():
                    source_hashes[relative] = sha256_file(path)

    report = {
        "schemaVersion": "human-infra.life-path-nhats-l4-readiness-runway-validation.v1",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "runwayPath": repo_rel(runway_path),
        "runwaySha256": sha256_file(runway_path),
        "runwayId": runway.get("runwayId"),
        "status": "PASS" if summary["fail"] == 0 else "FAIL",
        "checks": checks,
        "summary": summary,
        "gateStatusCounts": runway.get("summary", {}),
        "sourceHashes": source_hashes,
        "boundary": "This validation proves only that the L4 readiness runway is auditable and still blocks calibrated, public, row-level and individual use.",
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return report


def main() -> int:
    report = build_report(DEFAULT_RUNWAY, DEFAULT_OUT)
    print(f"wrote {repo_rel(DEFAULT_OUT)}")
    print(f"status={report['status']} checks={report['summary']}")
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
