#!/usr/bin/env python3
"""Validate the NHATS L2 variable-family admission register."""

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
DEFAULT_REGISTER = (
    MANUAL_DIR / "life_path_nhats_l2_variable_family_admission_register.json"
)
DEFAULT_FIRST_ESTIMAND_PROTOCOL = (
    MANUAL_DIR / "life_path_nhats_first_estimand_protocol.json"
)
DEFAULT_VARIABLE_CONFIRMATION_MATRIX = (
    MANUAL_DIR / "life_path_nhats_variable_confirmation_matrix.json"
)
DEFAULT_MODEL_ADMISSION_CONTRACT = (
    REPO_ROOT / "docs" / "reference" / "human-infra-model-admission-contract.json"
)
DEFAULT_MODEL_ADMISSION_CANDIDATE_REGISTRY = (
    REPO_ROOT
    / "docs"
    / "reference"
    / "human-infra-model-admission-candidate-registry.json"
)
DEFAULT_AUTHENTICATED_CAPTURE_TEMPLATE = (
    MANUAL_DIR / "life_path_nhats_colectica_authenticated_capture_template.json"
)
DEFAULT_OUT = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhats-l2-variable-family-admission-validation.json"
)

REQUIRED_FAMILIES = {
    "design_identity_route",
    "survey_design",
    "endpoint_censoring",
    "baseline_function",
    "baseline_cognition_attention",
    "baseline_support_environment",
}
REQUIRED_FALSE_DECISIONS = {
    "exactVariablesConfirmed",
    "colecticaValueLabelsConfirmed",
    "colecticaAuthenticatedCapturesComplete",
    "governedDataAccessReady",
    "cohortFlowReady",
    "surveyDesignReady",
    "realExtractionAllowed",
    "l4AdmissionAllowed",
    "calibrationAllowed",
    "individualPredictionAllowed",
}
REQUIRED_TRUE_DECISIONS = {
    "narrowEstimandSelected",
    "l2CandidateFamiliesMapped",
}
REQUIRED_BLOCKED_BEFORE_L4 = {
    "MODEL-G3-real-data-access",
    "MODEL-G4-field-and-value-confirmation",
    "MODEL-G5-real-extraction-and-cohort-flow",
    "MODEL-G6-survey-design-and-weighted-estimates",
    "MODEL-G7-external-validation-and-calibration",
    "MAC-G4-data-access",
    "MAC-G5-variable-confirmation",
    "MAC-G6-extraction-and-cohort-flow",
    "MAC-G7-validation-calibration",
}
REQUIRED_ABORTS = {
    "ABORT-1-no-source-identity",
    "ABORT-2-biomarker-to-lifespan-leap",
    "ABORT-3-animal-to-human-effect-leap",
    "ABORT-4-no-comparator-or-time-zero",
    "ABORT-5-individual-output",
    "ABORT-6-raw-data-exposure",
}
REQUIRED_BLOCKED_USES = {
    "individual-death-date-output",
    "individual-advice",
    "calibrated-prediction",
}
PROHIBITED_KEYS = {
    "rowLevelData",
    "rawNhatsData",
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


def row_ids(rows: Any, key: str) -> set[str]:
    if not isinstance(rows, list):
        return set()
    return {
        str(row[key])
        for row in rows
        if isinstance(row, dict) and isinstance(row.get(key), str)
    }


def add_check(checks: list[dict[str, Any]], check_id: str, passed: bool, detail: str) -> None:
    checks.append({"id": check_id, "status": "PASS" if passed else "FAIL", "detail": detail})


def summarize(checks: list[dict[str, Any]]) -> dict[str, int]:
    return {
        "pass": sum(1 for check in checks if check["status"] == "PASS"),
        "fail": sum(1 for check in checks if check["status"] == "FAIL"),
    }


def validate_register(
    register: dict[str, Any],
    first_estimand: dict[str, Any],
    matrix: dict[str, Any],
    contract: dict[str, Any],
    candidate_registry: dict[str, Any],
    capture_template: dict[str, Any],
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []

    add_check(
        checks,
        "schema-version",
        register.get("schemaVersion")
        == "human-infra.life-path-nhats-l2-variable-family-admission.v1",
        f"schemaVersion={register.get('schemaVersion')!r}",
    )
    add_check(
        checks,
        "register-identity",
        register.get("sourceId") == "nhats"
        and register.get("status") == "l2-variable-family-mapping-only-l4-blocked"
        and register.get("protocolId") == first_estimand.get("protocolId")
        and register.get("variableConfirmationMatrixId") == matrix.get("matrixId")
        and register.get("modelAdmissionContractId") == contract.get("contractId")
        and register.get("modelAdmissionCandidateRegistryId")
        == candidate_registry.get("registryId"),
        "register must bind NHATS, first estimand, variable matrix and model admission truth sources",
    )

    decision = register.get("currentDecision")
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
        "narrow estimand and L2 mappings may be true, while exact variables, real extraction, L4, calibration and individual prediction remain false",
    )

    source = register.get("sourceBindings")
    expected_sources = {
        "firstEstimandProtocolPath",
        "variableConfirmationMatrixPath",
        "modelAdmissionContractPath",
        "modelAdmissionCandidateRegistryPath",
        "authenticatedCaptureTemplatePath",
    }
    source_ok = isinstance(source, dict) and expected_sources.issubset(set(source))
    add_check(
        checks,
        "source-bindings-present",
        source_ok,
        f"missing={sorted(expected_sources - set(source or {}))}",
    )

    target = register.get("targetEstimand")
    target_ok = (
        isinstance(target, dict)
        and target.get("id") == first_estimand.get("estimand", {}).get("id")
        and target.get("admissionLevel") == "L2-estimand-design-only"
        and set(target.get("blockedUses", [])) >= REQUIRED_BLOCKED_USES
    )
    add_check(
        checks,
        "target-estimand-boundary",
        target_ok,
        "target estimand must be L2 design-only and block individual/calibrated uses",
    )

    observed_families = row_ids(register.get("candidateFamilyMappings"), "familyId")
    add_check(
        checks,
        "required-family-mappings",
        observed_families == REQUIRED_FAMILIES,
        f"observed={sorted(observed_families)}",
    )

    first_predictor_ids = row_ids(first_estimand.get("predictorFamilies"), "id")
    matrix_group_ids = row_ids(matrix.get("candidateVariableGroups"), "id")
    mappings = register.get("candidateFamilyMappings")
    mappings_ok = isinstance(mappings, list) and len(mappings) == len(REQUIRED_FAMILIES)
    if isinstance(mappings, list):
        for mapping in mappings:
            if not isinstance(mapping, dict):
                mappings_ok = False
                continue
            predictor_ids = set(mapping.get("predictorFamilyIds", []))
            variable_group_ids = set(mapping.get("variableGroupIds", []))
            if not predictor_ids.issubset(first_predictor_ids):
                mappings_ok = False
            if not variable_group_ids.issubset(matrix_group_ids):
                mappings_ok = False
            if not str(mapping.get("admissionLevel", "")).startswith("L2"):
                mappings_ok = False
            if mapping.get("promotionAllowed") is not False:
                mappings_ok = False
            if not mapping.get("requiredBeforePromotion"):
                mappings_ok = False
            if "pending" not in str(mapping.get("currentStatus", "")):
                mappings_ok = False
    add_check(
        checks,
        "mapping-crosswalk-and-promotion-boundary",
        mappings_ok,
        "every mapping must point to existing estimand/matrix families, stay L2 and keep promotionAllowed=false",
    )

    blockers = set(register.get("blockedBeforeL4", []))
    add_check(
        checks,
        "l4-blockers-complete",
        REQUIRED_BLOCKED_BEFORE_L4.issubset(blockers),
        f"missing={sorted(REQUIRED_BLOCKED_BEFORE_L4 - blockers)}",
    )
    add_check(
        checks,
        "hard-abort-inheritance",
        set(register.get("hardAbortInheritance", [])) == REQUIRED_ABORTS,
        "register must inherit all model-admission hard abort gates",
    )

    summary = register.get("summary")
    summary_ok = (
        isinstance(summary, dict)
        and summary.get("targetEstimands") == 1
        and summary.get("candidateFamilyMappings") == 6
        and summary.get("l2CandidateFamilies") == 6
        and summary.get("l4Admissions") == 0
        and summary.get("l5Admissions") == 0
        and summary.get("calibratedPredictionAvailable") is False
        and summary.get("individualUseAllowed") is False
    )
    add_check(
        checks,
        "summary-boundary",
        summary_ok,
        "summary must report six L2 families, zero L4/L5 admissions and no calibrated or individual use",
    )

    prohibited_present = sorted(PROHIBITED_KEYS & collect_keys(register))
    add_check(
        checks,
        "prohibited-keys-absent",
        not prohibited_present,
        f"present={prohibited_present}",
    )

    capture_decision = capture_template.get("currentDecision")
    capture_boundary_ok = (
        isinstance(capture_decision, dict)
        and capture_decision.get("templateReady") is True
        and capture_decision.get("authenticatedVariablePagesCaptured") is False
        and capture_decision.get("valueLabelsConfirmed") is False
        and capture_decision.get("routeClassifierAllowed") is False
        and capture_decision.get("calibrationAllowed") is False
        and capture_decision.get("individualPredictionAllowed") is False
    )
    add_check(
        checks,
        "capture-template-boundary-inherited",
        capture_boundary_ok,
        "L2 family admission must inherit authenticated capture template blockers",
    )
    return checks


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate NHATS L2 variable-family model-admission register."
    )
    parser.add_argument("--register", type=Path, default=DEFAULT_REGISTER)
    parser.add_argument(
        "--first-estimand-protocol",
        type=Path,
        default=DEFAULT_FIRST_ESTIMAND_PROTOCOL,
    )
    parser.add_argument(
        "--variable-confirmation-matrix",
        type=Path,
        default=DEFAULT_VARIABLE_CONFIRMATION_MATRIX,
    )
    parser.add_argument(
        "--model-admission-contract",
        type=Path,
        default=DEFAULT_MODEL_ADMISSION_CONTRACT,
    )
    parser.add_argument(
        "--model-admission-candidate-registry",
        type=Path,
        default=DEFAULT_MODEL_ADMISSION_CANDIDATE_REGISTRY,
    )
    parser.add_argument(
        "--authenticated-capture-template",
        type=Path,
        default=DEFAULT_AUTHENTICATED_CAPTURE_TEMPLATE,
    )
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    register_path = args.register.resolve()
    first_estimand_path = args.first_estimand_protocol.resolve()
    matrix_path = args.variable_confirmation_matrix.resolve()
    contract_path = args.model_admission_contract.resolve()
    candidate_registry_path = args.model_admission_candidate_registry.resolve()
    capture_template_path = args.authenticated_capture_template.resolve()

    register = load_json(register_path)
    first_estimand = load_json(first_estimand_path)
    matrix = load_json(matrix_path)
    contract = load_json(contract_path)
    candidate_registry = load_json(candidate_registry_path)
    capture_template = load_json(capture_template_path)
    checks = validate_register(
        register,
        first_estimand,
        matrix,
        contract,
        candidate_registry,
        capture_template,
    )
    summary = summarize(checks)
    payload = {
        "schemaVersion": "human-infra.life-path-nhats-l2-variable-family-admission-validation.v1",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "registerPath": repo_rel(register_path),
        "registerSha256": sha256_file(register_path),
        "firstEstimandProtocolPath": repo_rel(first_estimand_path),
        "firstEstimandProtocolSha256": sha256_file(first_estimand_path),
        "variableConfirmationMatrixPath": repo_rel(matrix_path),
        "variableConfirmationMatrixSha256": sha256_file(matrix_path),
        "modelAdmissionContractPath": repo_rel(contract_path),
        "modelAdmissionContractSha256": sha256_file(contract_path),
        "modelAdmissionCandidateRegistryPath": repo_rel(candidate_registry_path),
        "modelAdmissionCandidateRegistrySha256": sha256_file(candidate_registry_path),
        "authenticatedCaptureTemplatePath": repo_rel(capture_template_path),
        "authenticatedCaptureTemplateSha256": sha256_file(capture_template_path),
        "overallStatus": "PASS" if summary["fail"] == 0 else "FAIL",
        "summary": summary,
        "targetEstimand": register.get("targetEstimand", {}),
        "boundary": register.get("currentDecision", {}),
        "candidateFamilyCount": len(register.get("candidateFamilyMappings", [])),
        "l4Admissions": register.get("summary", {}).get("l4Admissions"),
        "l5Admissions": register.get("summary", {}).get("l5Admissions"),
        "checks": checks,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {repo_rel(args.out.resolve())}")
    print(f"status={payload['overallStatus']} checks={summary}")
    return 0 if payload["overallStatus"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
