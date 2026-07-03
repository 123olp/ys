#!/usr/bin/env python3
"""验证 NHANES public-use LMF weighted-domain output readiness 契约。"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_INPUT = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
    / "life_path_nhanes_public_lmf_weighted_domain_output_readiness.json"
)
DEFAULT_OUTPUT = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhanes-public-lmf-weighted-domain-output-readiness-validation.json"
)

REQUIRED_STATUS = "public-real-data-weighted-domain-output-blocked-safety-gates-registered"
REQUIRED_SOURCE_URLS = {
    "varianceEstimationTutorial": "https://wwwn.cdc.gov/nchs/nhanes/tutorials/varianceestimation.aspx",
    "weightingTutorial": "https://wwwn.cdc.gov/nchs/nhanes/tutorials/weighting.aspx",
    "surveySubsetDocumentation": "https://r-survey.r-forge.r-project.org/survey/html/subset.survey.design.html",
    "linkedMortalityPage": "https://www.cdc.gov/nchs/linked-data/mortality-files/index.html",
}
REQUIRED_GATE_IDS = {
    "upstream-weighted-estimator-readiness-validated",
    "controlled-r-survey-runtime-smoke-passed",
    "domain-indicator-contract-registered",
    "dof-sparse-domain-contract-registered",
    "disclosure-contract-registered",
    "public-domain-indicator-diagnostic-complete",
    "public-data-dof-sparse-review-not-complete",
    "public-output-disclosure-not-reviewed",
    "weighted-domain-output-not-implemented",
}
REQUIRED_BLOCKED_USES = {
    "survey-population inference",
    "weighted domain mortality rate publication",
    "design-based confidence interval output",
    "calibrated Human Infra prediction",
    "intervention effect estimation",
    "causal claim",
    "individual prediction",
    "individual death-date output",
    "medical advice",
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def rel(path: Path) -> str:
    return str(path.relative_to(REPO_ROOT))


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def require_bool(data: dict[str, Any], key: str, expected: bool, errors: list[str], prefix: str) -> None:
    if data.get(key) is not expected:
        fail(errors, f"{prefix}.{key} must be {expected}")


def validate_weighted_estimator_upstream(data: dict[str, Any], errors: list[str]) -> None:
    upstream = data.get("upstreamWeightedEstimatorReadiness")
    if not isinstance(upstream, dict):
        fail(errors, "upstreamWeightedEstimatorReadiness must be an object")
        return

    readiness_path_text = upstream.get("path")
    validation_path_text = upstream.get("validationPath")
    readiness_sha256: str | None = None
    if not isinstance(readiness_path_text, str):
        fail(errors, "upstreamWeightedEstimatorReadiness.path must be set")
    else:
        readiness_path = REPO_ROOT / readiness_path_text
        if not readiness_path.exists():
            fail(errors, "upstream weighted-estimator readiness path does not exist")
        else:
            readiness_sha256 = sha256_file(readiness_path)
            if upstream.get("sha256") != readiness_sha256:
                fail(errors, "upstream weighted-estimator readiness sha256 is stale")
            readiness = load_json(readiness_path)
            if readiness.get("schemaVersion") != (
                "human-infra.nhanes-public-lmf-weighted-estimator-readiness.v1"
            ):
                fail(errors, "upstream weighted-estimator schemaVersion mismatch")
            if readiness.get("gateSummary", {}).get("weightedDomainInferenceAllowed") is not False:
                fail(errors, "upstream weighted-estimator must still block weighted inference")

    if not isinstance(validation_path_text, str):
        fail(errors, "upstreamWeightedEstimatorReadiness.validationPath must be set")
    else:
        validation_path = REPO_ROOT / validation_path_text
        if not validation_path.exists():
            fail(errors, "upstream weighted-estimator validation path does not exist")
        else:
            validation = load_json(validation_path)
            if validation.get("schemaVersion") != (
                "human-infra.nhanes-public-lmf-weighted-estimator-readiness-validation.v1"
            ):
                fail(errors, "upstream weighted-estimator validation schemaVersion mismatch")
            if validation.get("status") != "pass":
                fail(errors, "upstream weighted-estimator validation must pass")
            if validation.get("readinessPath") != readiness_path_text:
                fail(errors, "upstream weighted-estimator validation path mismatch")
            if readiness_sha256 and validation.get("readinessSha256") != readiness_sha256:
                fail(errors, "upstream weighted-estimator validation readinessSha256 is stale")


def validate_runtime_upstream(data: dict[str, Any], errors: list[str]) -> None:
    upstream = data.get("upstreamRuntimeSmokeReadiness")
    if not isinstance(upstream, dict):
        fail(errors, "upstreamRuntimeSmokeReadiness must be an object")
        return

    readiness_path_text = upstream.get("path")
    readiness_sha256: str | None = None
    if not isinstance(readiness_path_text, str):
        fail(errors, "upstreamRuntimeSmokeReadiness.path must be set")
    else:
        readiness_path = REPO_ROOT / readiness_path_text
        if not readiness_path.exists():
            fail(errors, "upstream runtime smoke readiness path does not exist")
        else:
            readiness_sha256 = sha256_file(readiness_path)
            if upstream.get("sha256") != readiness_sha256:
                fail(errors, "upstream runtime smoke readiness sha256 is stale")
            readiness = load_json(readiness_path)
            if readiness.get("schemaVersion") != (
                "human-infra.nhanes-public-lmf-r-survey-runtime-smoke-readiness.v1"
            ):
                fail(errors, "upstream runtime smoke schemaVersion mismatch")

    default_validation_path_text = upstream.get("defaultValidationPath")
    if not isinstance(default_validation_path_text, str):
        fail(errors, "upstreamRuntimeSmokeReadiness.defaultValidationPath must be set")
    else:
        default_validation_path = REPO_ROOT / default_validation_path_text
        if not default_validation_path.exists():
            fail(errors, "default runtime smoke validation path does not exist")
        else:
            validation = load_json(default_validation_path)
            if validation.get("schemaVersion") != (
                "human-infra.nhanes-public-lmf-r-survey-runtime-smoke-validation.v1"
            ):
                fail(errors, "default runtime smoke validation schemaVersion mismatch")
            if validation.get("status") != "pass":
                fail(errors, "default runtime smoke validation must pass")
            if validation.get("readinessPath") != readiness_path_text:
                fail(errors, "default runtime smoke validation path mismatch")
            if readiness_sha256 and validation.get("readinessSha256") != readiness_sha256:
                fail(errors, "default runtime smoke validation readinessSha256 is stale")
            if validation.get("summary", {}).get("weightedDomainOutputAllowed") is not False:
                fail(errors, "default runtime smoke validation must still block weighted output")

    controlled_validation_path_text = upstream.get("controlledValidationPath")
    if not isinstance(controlled_validation_path_text, str):
        fail(errors, "upstreamRuntimeSmokeReadiness.controlledValidationPath must be set")
    else:
        controlled_validation_path = REPO_ROOT / controlled_validation_path_text
        if not controlled_validation_path.exists():
            fail(errors, "controlled runtime smoke validation path does not exist")
        else:
            validation = load_json(controlled_validation_path)
            if validation.get("schemaVersion") != (
                "human-infra.nhanes-public-lmf-r-survey-runtime-smoke-validation.v1"
            ):
                fail(errors, "controlled runtime smoke validation schemaVersion mismatch")
            if validation.get("status") != "pass":
                fail(errors, "controlled runtime smoke validation must pass")
            if validation.get("readinessPath") != readiness_path_text:
                fail(errors, "controlled runtime smoke validation path mismatch")
            if readiness_sha256 and validation.get("readinessSha256") != readiness_sha256:
                fail(errors, "controlled runtime smoke validation readinessSha256 is stale")
            summary = validation.get("summary", {})
            if summary.get("smokeStatus") != "ready-synthetic-r-survey-smoke-passed":
                fail(errors, "controlled runtime smoke must pass synthetic R survey smoke")
            if summary.get("weightedDomainOutputAllowed") is not False:
                fail(errors, "controlled runtime smoke validation must still block weighted output")


def validate_domain_indicator_diagnostic_upstream(data: dict[str, Any], errors: list[str]) -> None:
    upstream = data.get("upstreamDomainIndicatorDiagnostic")
    if not isinstance(upstream, dict):
        fail(errors, "upstreamDomainIndicatorDiagnostic must be an object")
        return

    diagnostic_path_text = upstream.get("path")
    validation_path_text = upstream.get("validationPath")
    diagnostic_sha256: str | None = None
    if not isinstance(diagnostic_path_text, str):
        fail(errors, "upstreamDomainIndicatorDiagnostic.path must be set")
    else:
        diagnostic_path = REPO_ROOT / diagnostic_path_text
        if not diagnostic_path.exists():
            fail(errors, "upstream domain indicator diagnostic path does not exist")
        else:
            diagnostic_sha256 = sha256_file(diagnostic_path)
            if upstream.get("sha256") != diagnostic_sha256:
                fail(errors, "upstream domain indicator diagnostic sha256 is stale")
            diagnostic = load_json(diagnostic_path)
            if diagnostic.get("schemaVersion") != (
                "human-infra.nhanes-public-lmf-domain-indicator-diagnostic.v1"
            ):
                fail(errors, "upstream domain indicator diagnostic schemaVersion mismatch")
            if diagnostic.get("status") != (
                "public-real-data-domain-indicator-metadata-diagnostic-no-weighted-output"
            ):
                fail(errors, "upstream domain indicator diagnostic status mismatch")
            summary = diagnostic.get("gateSummary", {})
            if summary.get("domainIndicatorMetadataDiagnosticComplete") is not True:
                fail(errors, "upstream domain indicator diagnostic must be complete")
            if summary.get("weightedDomainOutputAllowed") is not False:
                fail(errors, "upstream domain indicator diagnostic must still block weighted output")

    if not isinstance(validation_path_text, str):
        fail(errors, "upstreamDomainIndicatorDiagnostic.validationPath must be set")
    else:
        validation_path = REPO_ROOT / validation_path_text
        if not validation_path.exists():
            fail(errors, "upstream domain indicator diagnostic validation path does not exist")
        else:
            validation = load_json(validation_path)
            if validation.get("schemaVersion") != (
                "human-infra.nhanes-public-lmf-domain-indicator-diagnostic-validation.v1"
            ):
                fail(errors, "upstream domain indicator diagnostic validation schemaVersion mismatch")
            if validation.get("status") != "pass":
                fail(errors, "upstream domain indicator diagnostic validation must pass")
            if validation.get("diagnosticPath") != diagnostic_path_text:
                fail(errors, "upstream domain indicator diagnostic validation path mismatch")
            if diagnostic_sha256 and validation.get("diagnosticSha256") != diagnostic_sha256:
                fail(errors, "upstream domain indicator diagnostic validation diagnosticSha256 is stale")
            summary = validation.get("summary", {})
            if summary.get("domainIndicatorMetadataDiagnosticComplete") is not True:
                fail(errors, "upstream domain indicator diagnostic validation must be complete")
            if summary.get("weightedDomainOutputAllowed") is not False:
                fail(errors, "upstream domain indicator diagnostic validation must block weighted output")
            if summary.get("recordCountsRepeatedByThisDiagnostic") is not False:
                fail(errors, "domain indicator diagnostic must not repeat record counts")
            if summary.get("deathCountsRepeatedByThisDiagnostic") is not False:
                fail(errors, "domain indicator diagnostic must not repeat death counts")
            if summary.get("weightedSumsRepeatedByThisDiagnostic") is not False:
                fail(errors, "domain indicator diagnostic must not repeat weighted sums")


def validate_contract(data: dict[str, Any], errors: list[str]) -> None:
    contract = data.get("outputSafetyContract")
    if not isinstance(contract, dict):
        fail(errors, "outputSafetyContract must be an object")
        return

    domain = contract.get("domainIndicatorContract")
    if not isinstance(domain, dict):
        fail(errors, "domainIndicatorContract must be an object")
        domain = {}
    for key in (
        "domainIndicatorRequired",
        "requiresFullDesignInputBeforeDomain",
        "syntheticDomainSubsetSmokeProvenByControlledRuntime",
    ):
        require_bool(domain, key, True, errors, "domainIndicatorContract")
    require_bool(domain, "rowDropBeforeDesignAllowed", False, errors, "domainIndicatorContract")
    require_bool(domain, "publicDataDomainIndicatorEvaluated", True, errors, "domainIndicatorContract")
    require_bool(domain, "domainIndicatorMetadataDiagnosticComplete", True, errors, "domainIndicatorContract")
    require_bool(
        domain,
        "publicRecordCountsRepeatedByDomainDiagnostic",
        False,
        errors,
        "domainIndicatorContract",
    )
    require_bool(
        domain,
        "publicWeightedSumsRepeatedByDomainDiagnostic",
        False,
        errors,
        "domainIndicatorContract",
    )
    if domain.get("domainIndicatorMetadataDiagnosticPath") != (
        "domains/c1-boundary-rewriting/longevity-evidence/data/manual/"
        "life_path_nhanes_public_lmf_domain_indicator_diagnostic.json"
    ):
        fail(errors, "domainIndicatorContract.domainIndicatorMetadataDiagnosticPath mismatch")
    if domain.get("domainIndicatorTiming") != "after design object creation":
        fail(errors, "domainIndicatorContract.domainIndicatorTiming mismatch")

    dof = contract.get("dofSparseDomainContract")
    if not isinstance(dof, dict):
        fail(errors, "dofSparseDomainContract must be an object")
        dof = {}
    for key in (
        "domainDegreesOfFreedomDiagnosticRequired",
        "minimumPsuPerReportedStratumDiagnosticRequired",
        "lonelyPsuPolicyRequired",
        "emptyDomainPolicyRequired",
        "sparseDomainSuppressionPolicyRequired",
    ):
        require_bool(dof, key, True, errors, "dofSparseDomainContract")
    require_bool(dof, "publicDataDofSparseReviewComplete", False, errors, "dofSparseDomainContract")

    disclosure = contract.get("disclosureContract")
    if not isinstance(disclosure, dict):
        fail(errors, "disclosureContract must be an object")
        disclosure = {}
    for key in (
        "publicOutputDisclosureReviewRequired",
        "cellCountDisclosureDiagnosticRequired",
        "dominanceOrIdentifiabilityReviewRequired",
        "publicOutputSuppressionPolicyRequired",
    ):
        require_bool(disclosure, key, True, errors, "disclosureContract")
    require_bool(disclosure, "publicDisclosureReviewComplete", False, errors, "disclosureContract")

    output = contract.get("outputState")
    if not isinstance(output, dict):
        fail(errors, "outputState must be an object")
        output = {}
    for key in (
        "weightedDomainOutputImplemented",
        "publicWeightedDomainCellsAllowed",
        "publicWeightedDomainRatesAllowed",
        "publicDesignBasedIntervalsAllowed",
        "calibrationAllowed",
        "individualPredictionAllowed",
        "medicalAdviceAllowed",
    ):
        require_bool(output, key, False, errors, "outputState")


def validate_gates(data: dict[str, Any], errors: list[str]) -> None:
    gates = data.get("readinessGates")
    observed_ids: set[str] = set()
    ready = partial = blocked = 0
    if not isinstance(gates, list):
        fail(errors, "readinessGates must be a list")
        gates = []
    for gate in gates:
        if not isinstance(gate, dict):
            fail(errors, "readinessGates entries must be objects")
            continue
        gate_id = gate.get("id")
        if isinstance(gate_id, str):
            observed_ids.add(gate_id)
        status = gate.get("status")
        if status == "ready":
            ready += 1
            require_bool(gate, "blocksWeightedDomainOutput", False, errors, str(gate_id))
        elif status == "partial":
            partial += 1
            require_bool(gate, "blocksWeightedDomainOutput", True, errors, str(gate_id))
        elif status == "blocked":
            blocked += 1
            require_bool(gate, "blocksWeightedDomainOutput", True, errors, str(gate_id))
        else:
            fail(errors, f"unexpected gate status for {gate_id}: {status!r}")
        if not str(gate.get("evidence", "")).strip():
            fail(errors, f"readiness gate {gate_id} must include evidence")

    missing = sorted(REQUIRED_GATE_IDS - observed_ids)
    if missing:
        fail(errors, f"missing readiness gates: {missing}")

    expected_summary = {
        "requiredGateCount": len(REQUIRED_GATE_IDS),
        "readyGateCount": ready,
        "partialGateCount": partial,
        "blockedGateCount": blocked,
        "controlledRuntimeSmokePassed": True,
        "syntheticDomainSubsetSmokePassed": True,
        "publicDataDomainIndicatorEvaluated": True,
        "publicDataDofSparseReviewComplete": False,
        "publicDisclosureReviewComplete": False,
        "weightedDomainOutputAllowed": False,
    }
    if data.get("gateSummary") != expected_summary:
        fail(errors, f"gateSummary mismatch: expected {expected_summary}, found {data.get('gateSummary')}")
    if ready != 6 or partial != 0 or blocked != 3:
        fail(errors, "weighted-domain output readiness must remain 6 ready, 0 partial, 3 blocked")


def validate_payload(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if data.get("schemaVersion") != (
        "human-infra.nhanes-public-lmf-weighted-domain-output-readiness.v1"
    ):
        fail(errors, "schemaVersion mismatch")
    if data.get("readinessId") != "nhanes-public-lmf-2017-2018-weighted-domain-output-readiness":
        fail(errors, "readinessId mismatch")
    if data.get("status") != REQUIRED_STATUS:
        fail(errors, "status must keep public weighted-domain output blocked")
    if data.get("sourceId") != "nhanes-public-lmf-2017-2018":
        fail(errors, "sourceId must bind NHANES public LMF 2017-2018")
    if data.get("officialSourceTrace") != REQUIRED_SOURCE_URLS:
        fail(errors, "officialSourceTrace must match required sources")

    validate_weighted_estimator_upstream(data, errors)
    validate_runtime_upstream(data, errors)
    validate_domain_indicator_diagnostic_upstream(data, errors)

    findings = data.get("sourceFindings")
    if not isinstance(findings, list) or len(findings) < 3:
        fail(errors, "sourceFindings must include at least three source-backed findings")
    else:
        findings_text = json.dumps(findings, ensure_ascii=False)
        for token in ("domain", "full", "subset", "degrees of freedom"):
            if token not in findings_text:
                fail(errors, f"sourceFindings missing token: {token}")
        for finding in findings:
            if not isinstance(finding, dict):
                fail(errors, "sourceFindings entries must be objects")
                continue
            source_url = str(finding.get("sourceUrl", ""))
            if not (source_url.startswith("https://") or source_url.startswith("domains/")):
                fail(errors, "sourceFindings sourceUrl must use HTTPS or a local repository path")
            if not str(finding.get("observedFact", "")).strip():
                fail(errors, "sourceFindings observedFact must be non-empty")
            if not str(finding.get("modelConsequence", "")).strip():
                fail(errors, "sourceFindings modelConsequence must be non-empty")

    validate_contract(data, errors)
    validate_gates(data, errors)

    if set(data.get("blockedUses", [])) != REQUIRED_BLOCKED_USES:
        fail(errors, "blockedUses must preserve all prohibited inference and individual-use actions")
    if not isinstance(data.get("allowedUses"), list) or len(data["allowedUses"]) < 3:
        fail(errors, "allowedUses must list gate-only uses")
    if not isinstance(data.get("nextWork"), list) or len(data["nextWork"]) < 3:
        fail(errors, "nextWork must list DOF/sparse-domain, disclosure and output implementation work")
    return errors


def build_validation(readiness_path: Path, output_path: Path, errors: list[str], data: dict[str, Any]) -> dict[str, Any]:
    return {
        "schemaVersion": "human-infra.nhanes-public-lmf-weighted-domain-output-readiness-validation.v1",
        "status": "pass" if not errors else "fail",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "readinessPath": rel(readiness_path),
        "readinessSha256": sha256_file(readiness_path),
        "validationPath": rel(output_path),
        "summary": {
            "sourceId": data.get("sourceId"),
            "readyGateCount": data.get("gateSummary", {}).get("readyGateCount"),
            "blockedGateCount": data.get("gateSummary", {}).get("blockedGateCount"),
            "controlledRuntimeSmokePassed": data.get("gateSummary", {}).get("controlledRuntimeSmokePassed"),
            "syntheticDomainSubsetSmokePassed": data.get("gateSummary", {}).get("syntheticDomainSubsetSmokePassed"),
            "publicDataDomainIndicatorEvaluated": data.get("gateSummary", {}).get("publicDataDomainIndicatorEvaluated"),
            "publicDataDofSparseReviewComplete": data.get("gateSummary", {}).get("publicDataDofSparseReviewComplete"),
            "publicDisclosureReviewComplete": data.get("gateSummary", {}).get("publicDisclosureReviewComplete"),
            "weightedDomainOutputAllowed": data.get("gateSummary", {}).get("weightedDomainOutputAllowed"),
        },
        "nonProofBoundary": {
            "confirms": [
                "controlled synthetic R survey domain subset smoke is available",
                "public aggregate domain indicator metadata diagnostic is complete without repeating counts or weighted sums",
                "domain indicator, DOF/sparse-domain and disclosure gates are registered",
                "public weighted-domain output remains blocked",
            ],
            "doesNotConfirm": [
                "public NHANES weighted domain output",
                "domain degrees-of-freedom or sparse-domain adequacy",
                "design-based confidence intervals",
                "disclosure-reviewed public output",
                "calibration",
                "individual prediction",
                "medical advice",
            ],
        },
        "errors": errors,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    readiness_path = args.input.resolve()
    output_path = args.out.resolve()
    data = load_json(readiness_path)
    errors = validate_payload(data)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output = build_validation(readiness_path, output_path, errors, data)
    output_path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if errors:
        for error in errors:
            print(f"NHANES public LMF weighted-domain output readiness error: {error}")
        return 1
    print(
        "NHANES public LMF weighted-domain output readiness ok: "
        f"ready={output['summary']['readyGateCount']} "
        f"blocked={output['summary']['blockedGateCount']} "
        "boundary=no-weighted-domain-output"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
