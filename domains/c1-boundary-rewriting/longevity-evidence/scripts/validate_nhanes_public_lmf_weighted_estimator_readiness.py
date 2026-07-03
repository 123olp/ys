#!/usr/bin/env python3
"""验证 NHANES public-use LMF weighted-estimator readiness 契约。"""

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
    / "life_path_nhanes_public_lmf_weighted_estimator_readiness.json"
)
DEFAULT_OUTPUT = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhanes-public-lmf-weighted-estimator-readiness-validation.json"
)

REQUIRED_STATUS = "public-real-data-estimator-backend-selected-not-weighted-domain-output"
REQUIRED_SOURCE_URLS = {
    "varianceEstimationTutorial": "https://wwwn.cdc.gov/nchs/nhanes/tutorials/varianceestimation.aspx",
    "weightingTutorial": "https://wwwn.cdc.gov/nchs/nhanes/tutorials/weighting.aspx",
    "surveyPackageCran": "https://cran.r-project.org/package=survey",
    "surveyPackageManual": "https://cran.r-project.org/web/packages/survey/survey.pdf",
    "surveySubsetDocumentation": "https://r-survey.r-forge.r-project.org/survey/html/subset.survey.design.html",
}
REQUIRED_GATE_IDS = {
    "nhanes-r-software-path-documented",
    "r-survey-backend-selected",
    "no-custom-estimator-boundary-documented",
    "design-object-contract-bound",
    "eligible-base-upstream-validated",
    "r-runtime-smoke-not-executed",
    "domain-indicator-design-object-test-not-implemented",
    "domain-dof-sparse-review-not-implemented",
    "public-output-disclosure-not-reviewed",
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
REQUIRED_TRUE_DESIGN_FLAGS = {
    "nest",
    "requiresFullDesignInputBeforeDomain",
    "requiresDomainIndicatorInsideDesignObject",
    "requiresDomainDofSparseReviewBeforeOutput",
    "requiresDisclosureReviewBeforePublicOutput",
}
REQUIRED_FALSE_BACKEND_FLAGS = {
    "runtimeProbeExecuted",
    "customTaylorLinearizationAllowed",
    "pythonAdHocWeightedEstimatorAllowed",
    "postJoinGroupedCellsAsEstimatorAllowed",
    "weightedEstimatorImplemented",
    "weightedDomainInferenceAllowed",
    "designBasedIntervalAllowed",
    "calibrationAllowed",
    "individualPredictionAllowed",
    "medicalAdviceAllowed",
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


def validate_upstream(data: dict[str, Any], errors: list[str]) -> None:
    upstream = data.get("upstreamEligibleBaseReadiness")
    if not isinstance(upstream, dict):
        fail(errors, "upstreamEligibleBaseReadiness must be an object")
        return

    readiness_path_text = upstream.get("path")
    validation_path_text = upstream.get("validationPath")
    readiness_sha256: str | None = None
    if not isinstance(readiness_path_text, str):
        fail(errors, "upstreamEligibleBaseReadiness.path must be set")
    else:
        readiness_path = REPO_ROOT / readiness_path_text
        if not readiness_path.exists():
            fail(errors, "upstream eligible-base readiness path does not exist")
        else:
            readiness_sha256 = sha256_file(readiness_path)
            if upstream.get("sha256") != readiness_sha256:
                fail(errors, "upstream eligible-base readiness sha256 is stale")
            readiness = load_json(readiness_path)
            if readiness.get("schemaVersion") != (
                "human-infra.nhanes-public-lmf-eligible-base-readiness.v1"
            ):
                fail(errors, "upstream eligible-base readiness schemaVersion mismatch")
            if readiness.get("status") != (
                "public-real-data-eligible-base-diagnostic-not-weighted-domain-inference"
            ):
                fail(errors, "upstream eligible-base readiness must remain diagnostic-only")
            if readiness.get("gateSummary", {}).get("weightedDomainInferenceAllowed") is not False:
                fail(errors, "upstream eligible-base readiness must still block weighted inference")

    if not isinstance(validation_path_text, str):
        fail(errors, "upstreamEligibleBaseReadiness.validationPath must be set")
    else:
        validation_path = REPO_ROOT / validation_path_text
        if not validation_path.exists():
            fail(errors, "upstream eligible-base validation path does not exist")
        else:
            validation = load_json(validation_path)
            if validation.get("schemaVersion") != (
                "human-infra.nhanes-public-lmf-eligible-base-readiness-validation.v1"
            ):
                fail(errors, "upstream eligible-base validation schemaVersion mismatch")
            if validation.get("status") != "pass":
                fail(errors, "upstream eligible-base validation must pass")
            if validation.get("readinessPath") != readiness_path_text:
                fail(errors, "upstream eligible-base validation path must match readiness path")
            if readiness_sha256 and validation.get("readinessSha256") != readiness_sha256:
                fail(errors, "upstream eligible-base validation readinessSha256 is stale")


def validate_payload(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if data.get("schemaVersion") != "human-infra.nhanes-public-lmf-weighted-estimator-readiness.v1":
        fail(errors, "schemaVersion mismatch")
    if data.get("readinessId") != "nhanes-public-lmf-2017-2018-weighted-estimator-readiness":
        fail(errors, "readinessId mismatch")
    if data.get("status") != REQUIRED_STATUS:
        fail(errors, "status must keep estimator-selection-only non-output boundary")
    if data.get("sourceId") != "nhanes-public-lmf-2017-2018":
        fail(errors, "sourceId must bind NHANES public LMF 2017-2018")

    validate_upstream(data, errors)

    if data.get("officialSourceTrace") != REQUIRED_SOURCE_URLS:
        fail(errors, "officialSourceTrace must match CDC/NCHS and R survey URLs")

    findings = data.get("sourceFindings")
    if not isinstance(findings, list) or len(findings) < 5:
        fail(errors, "sourceFindings must contain at least five source-backed facts")
    else:
        findings_text = json.dumps(findings, ensure_ascii=False)
        for token in (
            "Taylor",
            "R",
            "svydesign",
            "SDMVPSU",
            "SDMVSTRA",
            "WTMEC2YR",
            "subset",
            "degrees of freedom",
        ):
            if token not in findings_text:
                fail(errors, f"sourceFindings missing {token}")
        for finding in findings:
            if not isinstance(finding, dict):
                fail(errors, "sourceFindings entries must be objects")
                continue
            if not str(finding.get("sourceUrl", "")).startswith("https://"):
                fail(errors, "sourceFindings sourceUrl must use HTTPS")
            if not str(finding.get("observedFact", "")).strip():
                fail(errors, "sourceFindings observedFact must be non-empty")
            if not str(finding.get("modelConsequence", "")).strip():
                fail(errors, "sourceFindings modelConsequence must be non-empty")

    backend = data.get("estimatorBackend")
    if not isinstance(backend, dict):
        fail(errors, "estimatorBackend must be an object")
        backend = {}
    if backend.get("selectedBackend") != "R survey package":
        fail(errors, "selectedBackend must be R survey package")
    if backend.get("packageName") != "survey":
        fail(errors, "packageName must be survey")
    if backend.get("primaryDesignFunction") != "svydesign":
        fail(errors, "primaryDesignFunction must be svydesign")
    if "subset.survey.design" not in backend.get("domainMechanisms", []):
        fail(errors, "domainMechanisms must include subset.survey.design")
    if backend.get("backendSelectionStatus") != "selected-from-primary-documentation-not-runtime-smoked":
        fail(errors, "backendSelectionStatus must remain selected but not runtime-smoked")
    if backend.get("runtimeAvailableInCurrentEnvironment") is not None:
        fail(errors, "runtimeAvailableInCurrentEnvironment must remain null until probed")
    if backend.get("packageInstalledInCurrentEnvironment") is not None:
        fail(errors, "packageInstalledInCurrentEnvironment must remain null until probed")
    for flag in REQUIRED_FALSE_BACKEND_FLAGS:
        if backend.get(flag) is not False:
            fail(errors, f"estimatorBackend.{flag} must be false")

    design = data.get("designObjectContract")
    if not isinstance(design, dict):
        fail(errors, "designObjectContract must be an object")
        design = {}
    expected_design_values = {
        "joinKey": "SEQN",
        "analysisWeight": "WTMEC2YR",
        "positiveWeightCondition": "WTMEC2YR > 0",
        "primarySamplingUnit": "SDMVPSU",
        "strata": "SDMVSTRA",
        "domainIndicatorTiming": "after design object creation",
    }
    for key, expected in expected_design_values.items():
        if design.get(key) != expected:
            fail(errors, f"designObjectContract.{key} mismatch")
    for flag in REQUIRED_TRUE_DESIGN_FLAGS:
        if design.get(flag) is not True:
            fail(errors, f"designObjectContract.{flag} must be true")
    for flag in ("rowDropBeforeDesignAllowed", "eligibleBaseRowsPersisted", "rawRowsPersisted"):
        if design.get(flag) is not False:
            fail(errors, f"designObjectContract.{flag} must be false")

    domain_review = data.get("domainReviewContract")
    if not isinstance(domain_review, dict):
        fail(errors, "domainReviewContract must be an object")
        domain_review = {}
    for flag in (
        "domainDegreesOfFreedomReviewRequired",
        "sparseDomainReviewRequired",
        "lonelyPsuPolicyRequired",
        "emptyDomainPolicyRequired",
        "minimumPsuPerReportedStratumDiagnosticRequired",
        "publicOutputDisclosureReviewRequired",
    ):
        if domain_review.get(flag) is not True:
            fail(errors, f"domainReviewContract.{flag} must be true")
    for flag in (
        "publicWeightedDomainCellsAllowed",
        "publicWeightedDomainRatesAllowed",
        "publicDesignBasedIntervalsAllowed",
    ):
        if domain_review.get(flag) is not False:
            fail(errors, f"domainReviewContract.{flag} must be false")

    gates = data.get("readinessGates")
    observed_gate_ids: set[str] = set()
    ready = partial = blocked = 0
    if not isinstance(gates, list):
        fail(errors, "readinessGates must be a list")
        gates = []
    for gate in gates:
        if not isinstance(gate, dict):
            fail(errors, "each readiness gate must be an object")
            continue
        gate_id = gate.get("id")
        if isinstance(gate_id, str):
            observed_gate_ids.add(gate_id)
        status = gate.get("status")
        if status == "ready":
            ready += 1
            if gate.get("blocksWeightedDomainInference") is not False:
                fail(errors, f"ready gate {gate_id} must not block weighted domain inference")
        elif status == "partial":
            partial += 1
            if gate.get("blocksWeightedDomainInference") is not True:
                fail(errors, f"partial gate {gate_id} must block weighted domain inference")
        elif status == "blocked":
            blocked += 1
            if gate.get("blocksWeightedDomainInference") is not True:
                fail(errors, f"blocked gate {gate_id} must block weighted domain inference")
        else:
            fail(errors, f"unexpected gate status for {gate_id}: {status!r}")
        if not str(gate.get("evidence", "")).strip():
            fail(errors, f"readiness gate {gate_id} must include evidence")
    missing_gate_ids = sorted(REQUIRED_GATE_IDS - observed_gate_ids)
    if missing_gate_ids:
        fail(errors, f"missing readiness gates: {missing_gate_ids}")

    expected_summary = {
        "requiredGateCount": len(REQUIRED_GATE_IDS),
        "readyGateCount": ready,
        "partialGateCount": partial,
        "blockedGateCount": blocked,
        "estimatorBackendSelected": True,
        "runtimeSmokeExecuted": False,
        "weightedEstimatorImplemented": False,
        "weightedDomainInferenceAllowed": False,
    }
    if data.get("gateSummary") != expected_summary:
        fail(errors, f"gateSummary mismatch: expected {expected_summary}, found {data.get('gateSummary')}")
    if ready != 5 or partial != 0 or blocked != 4:
        fail(errors, "weighted-estimator gate mix must remain 5 ready, 0 partial, 4 blocked")

    if set(data.get("blockedUses", [])) != REQUIRED_BLOCKED_USES:
        fail(errors, "blockedUses must preserve all prohibited inference and individual-use actions")
    if not isinstance(data.get("allowedUses"), list) or len(data["allowedUses"]) < 3:
        fail(errors, "allowedUses must list contract-only uses")
    if not isinstance(data.get("nextWork"), list) or len(data["nextWork"]) < 4:
        fail(errors, "nextWork must list backend smoke, domain, sparse-domain and disclosure work")

    return errors


def build_validation(
    readiness_path: Path,
    output_path: Path,
    errors: list[str],
    data: dict[str, Any],
) -> dict[str, Any]:
    status = "pass" if not errors else "fail"
    return {
        "schemaVersion": "human-infra.nhanes-public-lmf-weighted-estimator-readiness-validation.v1",
        "status": status,
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "readinessPath": rel(readiness_path),
        "readinessSha256": sha256_file(readiness_path),
        "validationPath": rel(output_path),
        "summary": {
            "sourceId": data.get("sourceId"),
            "selectedBackend": data.get("estimatorBackend", {}).get("selectedBackend"),
            "primaryDesignFunction": data.get("estimatorBackend", {}).get("primaryDesignFunction"),
            "readyGateCount": data.get("gateSummary", {}).get("readyGateCount"),
            "blockedGateCount": data.get("gateSummary", {}).get("blockedGateCount"),
            "runtimeSmokeExecuted": data.get("gateSummary", {}).get("runtimeSmokeExecuted"),
            "weightedEstimatorImplemented": data.get("gateSummary", {}).get("weightedEstimatorImplemented"),
            "weightedDomainInferenceAllowed": data.get("gateSummary", {}).get("weightedDomainInferenceAllowed"),
        },
        "nonProofBoundary": {
            "confirms": "estimator backend selection and design-object contract readiness",
            "doesNotConfirm": [
                "R runtime availability",
                "survey package installation",
                "executed weighted estimator",
                "weighted domain mortality rates",
                "design-based confidence intervals",
                "calibrated prediction",
                "intervention or causal effect",
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
    output_path.write_text(
        json.dumps(output, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    if errors:
        for error in errors:
            print(f"NHANES public LMF weighted-estimator readiness error: {error}")
        return 1
    print(
        "NHANES public LMF weighted-estimator readiness ok: "
        f"backend={output['summary']['selectedBackend']} "
        f"blocked={output['summary']['blockedGateCount']} "
        "boundary=no-weighted-domain-output"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
