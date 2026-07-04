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
    "nchsDataPresentationStandardsForProportions": "https://www.cdc.gov/nchs/data/series/sr_02/sr02_175.pdf",
    "nhanesReliabilityTutorial": "https://wwwn.cdc.gov/nchs/nhanes/tutorials/reliabilityofestimates.aspx",
    "nchsDataPresentationStandardsForRatesAndCounts": "https://www.cdc.gov/nchs/data/series/sr_02/sr02-200.pdf",
    "linkedMortalityPage": "https://www.cdc.gov/nchs/linked-data/mortality-files/index.html",
}
REQUIRED_GATE_IDS = {
    "upstream-weighted-estimator-readiness-validated",
    "controlled-r-survey-runtime-smoke-passed",
    "domain-indicator-contract-registered",
    "dof-sparse-domain-contract-registered",
    "disclosure-contract-registered",
    "public-domain-indicator-diagnostic-complete",
    "public-data-dof-sparse-review-complete",
    "public-disclosure-output-envelope-validated",
    "public-effective-sample-ci-publication-validated",
    "public-weighted-output-implementation-preflight-validated",
    "public-disclosure-review-template-validated",
    "public-disclosure-review-execution-registered",
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


def validate_dof_sparse_domain_diagnostic_upstream(data: dict[str, Any], errors: list[str]) -> None:
    upstream = data.get("upstreamDofSparseDomainDiagnostic")
    if not isinstance(upstream, dict):
        fail(errors, "upstreamDofSparseDomainDiagnostic must be an object")
        return

    diagnostic_path_text = upstream.get("path")
    validation_path_text = upstream.get("validationPath")
    diagnostic_sha256: str | None = None
    if not isinstance(diagnostic_path_text, str):
        fail(errors, "upstreamDofSparseDomainDiagnostic.path must be set")
    else:
        diagnostic_path = REPO_ROOT / diagnostic_path_text
        if not diagnostic_path.exists():
            fail(errors, "upstream DOF/sparse-domain diagnostic path does not exist")
        else:
            diagnostic_sha256 = sha256_file(diagnostic_path)
            if upstream.get("sha256") != diagnostic_sha256:
                fail(errors, "upstream DOF/sparse-domain diagnostic sha256 is stale")
            diagnostic = load_json(diagnostic_path)
            if diagnostic.get("schemaVersion") != (
                "human-infra.nhanes-public-lmf-dof-sparse-domain-diagnostic.v1"
            ):
                fail(errors, "upstream DOF/sparse-domain diagnostic schemaVersion mismatch")
            if diagnostic.get("status") != (
                "public-real-data-dof-sparse-domain-diagnostic-no-weighted-output"
            ):
                fail(errors, "upstream DOF/sparse-domain diagnostic status mismatch")
            summary = diagnostic.get("gateSummary", {})
            if summary.get("publicDataDofSparseReviewComplete") is not True:
                fail(errors, "upstream DOF/sparse-domain diagnostic must be complete")
            if summary.get("weightedDomainOutputAllowed") is not False:
                fail(errors, "upstream DOF/sparse-domain diagnostic must still block weighted output")

    if not isinstance(validation_path_text, str):
        fail(errors, "upstreamDofSparseDomainDiagnostic.validationPath must be set")
    else:
        validation_path = REPO_ROOT / validation_path_text
        if not validation_path.exists():
            fail(errors, "upstream DOF/sparse-domain diagnostic validation path does not exist")
        else:
            validation = load_json(validation_path)
            if validation.get("schemaVersion") != (
                "human-infra.nhanes-public-lmf-dof-sparse-domain-diagnostic-validation.v1"
            ):
                fail(errors, "upstream DOF/sparse-domain diagnostic validation schemaVersion mismatch")
            if validation.get("status") != "pass":
                fail(errors, "upstream DOF/sparse-domain diagnostic validation must pass")
            if validation.get("diagnosticPath") != diagnostic_path_text:
                fail(errors, "upstream DOF/sparse-domain diagnostic validation path mismatch")
            if diagnostic_sha256 and validation.get("diagnosticSha256") != diagnostic_sha256:
                fail(errors, "upstream DOF/sparse-domain diagnostic validation diagnosticSha256 is stale")
            summary = validation.get("summary", {})
            if summary.get("publicDataDofSparseReviewComplete") is not True:
                fail(errors, "upstream DOF/sparse-domain diagnostic validation must be complete")
            if summary.get("weightedDomainOutputAllowed") is not False:
                fail(errors, "upstream DOF/sparse-domain diagnostic validation must block weighted output")
            if summary.get("perDomainRecordCountsPersisted") is not False:
                fail(errors, "DOF/sparse-domain diagnostic must not persist per-domain record counts")
            if summary.get("perDomainWeightedSumsPersisted") is not False:
                fail(errors, "DOF/sparse-domain diagnostic must not persist per-domain weighted sums")
            if summary.get("minimumDomainDegreesOfFreedomObserved") != 15:
                fail(errors, "DOF/sparse-domain diagnostic minimum df must be 15")
            if summary.get("domainsWithLonelyRepresentedStrata") != 0:
                fail(errors, "DOF/sparse-domain diagnostic must report zero lonely represented strata")


def validate_disclosure_output_envelope_upstream(data: dict[str, Any], errors: list[str]) -> None:
    upstream = data.get("upstreamDisclosureOutputEnvelope")
    if not isinstance(upstream, dict):
        fail(errors, "upstreamDisclosureOutputEnvelope must be an object")
        return

    policy_path_text = upstream.get("policyPath")
    test_cases_path_text = upstream.get("testCasesPath")
    validation_path_text = upstream.get("validationPath")
    policy_sha256: str | None = None
    test_cases_sha256: str | None = None

    if not isinstance(policy_path_text, str):
        fail(errors, "upstreamDisclosureOutputEnvelope.policyPath must be set")
    else:
        policy_path = REPO_ROOT / policy_path_text
        if not policy_path.exists():
            fail(errors, "upstream disclosure envelope policy path does not exist")
        else:
            policy_sha256 = sha256_file(policy_path)
            if upstream.get("policySha256") != policy_sha256:
                fail(errors, "upstream disclosure envelope policy sha256 is stale")
            policy = load_json(policy_path)
            if policy.get("schemaVersion") != (
                "human-infra.nhanes-public-lmf-disclosure-output-envelope-policy.v1"
            ):
                fail(errors, "upstream disclosure envelope policy schemaVersion mismatch")
            if policy.get("status") != "synthetic-envelope-policy-ready-no-real-output":
                fail(errors, "upstream disclosure envelope policy status mismatch")
            decision = policy.get("currentDecision", {})
            if decision.get("realWeightedOutputPresent") is not False:
                fail(errors, "upstream disclosure envelope policy must not claim real weighted output")
            if decision.get("publicRealOutputExportAllowed") is not False:
                fail(errors, "upstream disclosure envelope policy must block real public export")

    if not isinstance(test_cases_path_text, str):
        fail(errors, "upstreamDisclosureOutputEnvelope.testCasesPath must be set")
    else:
        test_cases_path = REPO_ROOT / test_cases_path_text
        if not test_cases_path.exists():
            fail(errors, "upstream disclosure envelope test cases path does not exist")
        else:
            test_cases_sha256 = sha256_file(test_cases_path)
            if upstream.get("testCasesSha256") != test_cases_sha256:
                fail(errors, "upstream disclosure envelope test cases sha256 is stale")
            test_cases = load_json(test_cases_path)
            if test_cases.get("schemaVersion") != (
                "human-infra.nhanes-public-lmf-disclosure-output-envelope-test-cases.v1"
            ):
                fail(errors, "upstream disclosure envelope test cases schemaVersion mismatch")
            boundary = test_cases.get("currentBoundary", {})
            if boundary.get("containsRealNhanesData") is not False:
                fail(errors, "upstream disclosure envelope test cases must be synthetic-only")
            if boundary.get("weightedDomainOutputImplemented") is not False:
                fail(errors, "upstream disclosure envelope test cases must not implement weighted output")

    if not isinstance(validation_path_text, str):
        fail(errors, "upstreamDisclosureOutputEnvelope.validationPath must be set")
    else:
        validation_path = REPO_ROOT / validation_path_text
        if not validation_path.exists():
            fail(errors, "upstream disclosure envelope validation path does not exist")
        else:
            validation = load_json(validation_path)
            if validation.get("schemaVersion") != (
                "human-infra.nhanes-public-lmf-disclosure-output-envelope-validation.v1"
            ):
                fail(errors, "upstream disclosure envelope validation schemaVersion mismatch")
            if validation.get("overallStatus") != "PASS":
                fail(errors, "upstream disclosure envelope validation must pass")
            if validation.get("policyPath") != policy_path_text:
                fail(errors, "upstream disclosure envelope validation policy path mismatch")
            if validation.get("testCasesPath") != test_cases_path_text:
                fail(errors, "upstream disclosure envelope validation test cases path mismatch")
            if policy_sha256 and validation.get("policySha256") != policy_sha256:
                fail(errors, "upstream disclosure envelope validation policySha256 is stale")
            if test_cases_sha256 and validation.get("testCasesSha256") != test_cases_sha256:
                fail(errors, "upstream disclosure envelope validation testCasesSha256 is stale")
            boundary = validation.get("boundary", {})
            if boundary.get("containsRealNhanesData") is not False:
                fail(errors, "upstream disclosure envelope validation must be synthetic-only")
            if boundary.get("weightedDomainOutputImplemented") is not False:
                fail(errors, "upstream disclosure envelope validation must not implement weighted output")
            if boundary.get("publicWeightedDomainOutputAllowed") is not False:
                fail(errors, "upstream disclosure envelope validation must block weighted output")
            summary = validation.get("summary", {})
            if summary.get("caseCount") != 8:
                fail(errors, "upstream disclosure envelope validation must include 8 cases")
            if summary.get("fail") != 0:
                fail(errors, "upstream disclosure envelope validation must have zero failing cases")
            if summary.get("allowedCount") != 2 or summary.get("blockedCount") != 6:
                fail(errors, "upstream disclosure envelope validation allow/block counts mismatch")


def validate_effective_sample_ci_publication_upstream(data: dict[str, Any], errors: list[str]) -> None:
    upstream = data.get("upstreamEffectiveSampleCiPublicationReview")
    if not isinstance(upstream, dict):
        fail(errors, "upstreamEffectiveSampleCiPublicationReview must be an object")
        return

    policy_path_text = upstream.get("policyPath")
    test_cases_path_text = upstream.get("testCasesPath")
    validation_path_text = upstream.get("validationPath")
    policy_sha256: str | None = None
    test_cases_sha256: str | None = None

    if not isinstance(policy_path_text, str):
        fail(errors, "upstreamEffectiveSampleCiPublicationReview.policyPath must be set")
    else:
        policy_path = REPO_ROOT / policy_path_text
        if not policy_path.exists():
            fail(errors, "upstream effective sample / CI publication policy path does not exist")
        else:
            policy_sha256 = sha256_file(policy_path)
            if upstream.get("policySha256") != policy_sha256:
                fail(errors, "upstream effective sample / CI publication policy sha256 is stale")
            policy = load_json(policy_path)
            if policy.get("schemaVersion") != (
                "human-infra.nhanes-public-lmf-effective-sample-ci-publication-policy.v1"
            ):
                fail(errors, "upstream effective sample / CI publication policy schemaVersion mismatch")
            if policy.get("status") != "synthetic-publication-criteria-policy-ready-no-real-output":
                fail(errors, "upstream effective sample / CI publication policy status mismatch")
            decision = policy.get("currentDecision", {})
            if decision.get("realWeightedOutputPresent") is not False:
                fail(errors, "upstream publication policy must not claim real weighted output")
            if decision.get("realConfidenceIntervalsPresent") is not False:
                fail(errors, "upstream publication policy must not claim real confidence intervals")
            if decision.get("publicRealOutputExportAllowed") is not False:
                fail(errors, "upstream publication policy must block real public export")

    if not isinstance(test_cases_path_text, str):
        fail(errors, "upstreamEffectiveSampleCiPublicationReview.testCasesPath must be set")
    else:
        test_cases_path = REPO_ROOT / test_cases_path_text
        if not test_cases_path.exists():
            fail(errors, "upstream effective sample / CI publication test cases path does not exist")
        else:
            test_cases_sha256 = sha256_file(test_cases_path)
            if upstream.get("testCasesSha256") != test_cases_sha256:
                fail(errors, "upstream effective sample / CI publication test cases sha256 is stale")
            test_cases = load_json(test_cases_path)
            if test_cases.get("schemaVersion") != (
                "human-infra.nhanes-public-lmf-effective-sample-ci-publication-test-cases.v1"
            ):
                fail(errors, "upstream effective sample / CI publication test cases schemaVersion mismatch")
            boundary = test_cases.get("currentBoundary", {})
            if boundary.get("containsRealNhanesData") is not False:
                fail(errors, "upstream publication test cases must be synthetic-only")
            if boundary.get("weightedDomainOutputImplemented") is not False:
                fail(errors, "upstream publication test cases must not implement weighted output")
            if boundary.get("realConfidenceIntervalsComputed") is not False:
                fail(errors, "upstream publication test cases must not compute real confidence intervals")

    if not isinstance(validation_path_text, str):
        fail(errors, "upstreamEffectiveSampleCiPublicationReview.validationPath must be set")
    else:
        validation_path = REPO_ROOT / validation_path_text
        if not validation_path.exists():
            fail(errors, "upstream effective sample / CI publication validation path does not exist")
        else:
            validation = load_json(validation_path)
            if validation.get("schemaVersion") != (
                "human-infra.nhanes-public-lmf-effective-sample-ci-publication-validation.v1"
            ):
                fail(errors, "upstream effective sample / CI publication validation schemaVersion mismatch")
            if validation.get("overallStatus") != "PASS":
                fail(errors, "upstream effective sample / CI publication validation must pass")
            if validation.get("policyPath") != policy_path_text:
                fail(errors, "upstream effective sample / CI publication validation policy path mismatch")
            if validation.get("testCasesPath") != test_cases_path_text:
                fail(errors, "upstream effective sample / CI publication validation test cases path mismatch")
            if policy_sha256 and validation.get("policySha256") != policy_sha256:
                fail(errors, "upstream effective sample / CI publication validation policySha256 is stale")
            if test_cases_sha256 and validation.get("testCasesSha256") != test_cases_sha256:
                fail(
                    errors,
                    "upstream effective sample / CI publication validation testCasesSha256 is stale",
                )
            boundary = validation.get("boundary", {})
            if boundary.get("containsRealNhanesData") is not False:
                fail(errors, "upstream publication validation must be synthetic-only")
            if boundary.get("weightedDomainOutputImplemented") is not False:
                fail(errors, "upstream publication validation must not implement weighted output")
            if boundary.get("realConfidenceIntervalsComputed") is not False:
                fail(errors, "upstream publication validation must not compute real confidence intervals")
            if boundary.get("publicWeightedDomainOutputAllowed") is not False:
                fail(errors, "upstream publication validation must block weighted output")
            summary = validation.get("summary", {})
            if summary.get("caseCount") != 9:
                fail(errors, "upstream effective sample / CI publication validation must include 9 cases")
            if summary.get("fail") != 0:
                fail(errors, "upstream effective sample / CI publication validation must have zero failures")
            if summary.get("allowedCount") != 2 or summary.get("blockedCount") != 7:
                fail(errors, "upstream effective sample / CI publication validation allow/block mismatch")


def validate_weighted_output_implementation_preflight_upstream(
    data: dict[str, Any],
    errors: list[str],
) -> None:
    upstream = data.get("upstreamWeightedOutputImplementationPreflight")
    if not isinstance(upstream, dict):
        fail(errors, "upstreamWeightedOutputImplementationPreflight must be an object")
        return

    policy_path_text = upstream.get("policyPath")
    test_cases_path_text = upstream.get("testCasesPath")
    validation_path_text = upstream.get("validationPath")
    policy_sha256: str | None = None
    test_cases_sha256: str | None = None

    if not isinstance(policy_path_text, str):
        fail(errors, "upstreamWeightedOutputImplementationPreflight.policyPath must be set")
    else:
        policy_path = REPO_ROOT / policy_path_text
        if not policy_path.exists():
            fail(errors, "upstream weighted-output implementation preflight policy path does not exist")
        else:
            policy_sha256 = sha256_file(policy_path)
            if upstream.get("policySha256") != policy_sha256:
                fail(errors, "upstream weighted-output implementation preflight policy sha256 is stale")
            policy = load_json(policy_path)
            if policy.get("schemaVersion") != (
                "human-infra.nhanes-public-lmf-weighted-output-implementation-preflight-policy.v1"
            ):
                fail(errors, "upstream weighted-output implementation preflight policy schemaVersion mismatch")
            if policy.get("status") != "synthetic-implementation-preflight-ready-no-real-weighted-output":
                fail(errors, "upstream weighted-output implementation preflight policy status mismatch")
            decision = policy.get("currentDecision", {})
            if decision.get("realWeightedOutputImplemented") is not False:
                fail(errors, "upstream implementation preflight must not claim real weighted output")
            if decision.get("realDesignBasedIntervalsPresent") is not False:
                fail(errors, "upstream implementation preflight must not claim real intervals")
            if decision.get("publicRealOutputExportAllowed") is not False:
                fail(errors, "upstream implementation preflight must block real public export")

    if not isinstance(test_cases_path_text, str):
        fail(errors, "upstreamWeightedOutputImplementationPreflight.testCasesPath must be set")
    else:
        test_cases_path = REPO_ROOT / test_cases_path_text
        if not test_cases_path.exists():
            fail(errors, "upstream weighted-output implementation preflight test cases path does not exist")
        else:
            test_cases_sha256 = sha256_file(test_cases_path)
            if upstream.get("testCasesSha256") != test_cases_sha256:
                fail(errors, "upstream weighted-output implementation preflight test cases sha256 is stale")
            test_cases = load_json(test_cases_path)
            if test_cases.get("schemaVersion") != (
                "human-infra.nhanes-public-lmf-weighted-output-implementation-preflight-test-cases.v1"
            ):
                fail(errors, "upstream weighted-output implementation preflight test cases schemaVersion mismatch")
            boundary = test_cases.get("currentBoundary", {})
            if boundary.get("containsRealNhanesData") is not False:
                fail(errors, "upstream implementation preflight test cases must be synthetic-only")
            if boundary.get("weightedDomainOutputImplemented") is not False:
                fail(errors, "upstream implementation preflight test cases must not implement weighted output")
            if boundary.get("realWeightedRatesComputed") is not False:
                fail(errors, "upstream implementation preflight test cases must not compute real weighted rates")

    if not isinstance(validation_path_text, str):
        fail(errors, "upstreamWeightedOutputImplementationPreflight.validationPath must be set")
    else:
        validation_path = REPO_ROOT / validation_path_text
        if not validation_path.exists():
            fail(errors, "upstream weighted-output implementation preflight validation path does not exist")
        else:
            validation = load_json(validation_path)
            if validation.get("schemaVersion") != (
                "human-infra.nhanes-public-lmf-weighted-output-implementation-preflight-validation.v1"
            ):
                fail(errors, "upstream weighted-output implementation preflight validation schemaVersion mismatch")
            if validation.get("overallStatus") != "PASS":
                fail(errors, "upstream weighted-output implementation preflight validation must pass")
            if validation.get("policyPath") != policy_path_text:
                fail(errors, "upstream implementation preflight validation policy path mismatch")
            if validation.get("testCasesPath") != test_cases_path_text:
                fail(errors, "upstream implementation preflight validation test cases path mismatch")
            if policy_sha256 and validation.get("policySha256") != policy_sha256:
                fail(errors, "upstream implementation preflight validation policySha256 is stale")
            if test_cases_sha256 and validation.get("testCasesSha256") != test_cases_sha256:
                fail(errors, "upstream implementation preflight validation testCasesSha256 is stale")
            boundary = validation.get("boundary", {})
            if boundary.get("containsRealNhanesData") is not False:
                fail(errors, "upstream implementation preflight validation must be synthetic-only")
            if boundary.get("weightedDomainOutputImplemented") is not False:
                fail(errors, "upstream implementation preflight validation must not implement weighted output")
            if boundary.get("realWeightedRatesComputed") is not False:
                fail(errors, "upstream implementation preflight validation must not compute weighted rates")
            if boundary.get("realDesignBasedIntervalsComputed") is not False:
                fail(errors, "upstream implementation preflight validation must not compute real intervals")
            if boundary.get("publicWeightedDomainOutputAllowed") is not False:
                fail(errors, "upstream implementation preflight validation must block weighted output")
            summary = validation.get("summary", {})
            if summary.get("caseCount") != 8:
                fail(errors, "upstream weighted-output implementation preflight validation must include 8 cases")
            if summary.get("fail") != 0:
                fail(errors, "upstream weighted-output implementation preflight validation must have zero failures")
            if summary.get("allowedCount") != 2 or summary.get("blockedCount") != 6:
                fail(errors, "upstream weighted-output implementation preflight validation allow/block mismatch")


def validate_disclosure_review_template_upstream(data: dict[str, Any], errors: list[str]) -> None:
    upstream = data.get("upstreamDisclosureReviewTemplate")
    if not isinstance(upstream, dict):
        fail(errors, "upstreamDisclosureReviewTemplate must be an object")
        return

    template_path_text = upstream.get("path")
    validation_path_text = upstream.get("validationPath")
    template_sha256: str | None = None
    if not isinstance(template_path_text, str):
        fail(errors, "upstreamDisclosureReviewTemplate.path must be set")
    else:
        template_path = REPO_ROOT / template_path_text
        if not template_path.exists():
            fail(errors, "upstream disclosure review template path does not exist")
        else:
            template_sha256 = sha256_file(template_path)
            if upstream.get("sha256") != template_sha256:
                fail(errors, "upstream disclosure review template sha256 is stale")
            template = load_json(template_path)
            if template.get("schemaVersion") != (
                "human-infra.nhanes-public-lmf-disclosure-review-template.v1"
            ):
                fail(errors, "upstream disclosure review template schemaVersion mismatch")
            if template.get("status") != "template-ready-review-not-complete-no-real-output":
                fail(errors, "upstream disclosure review template status mismatch")
            decision = template.get("currentDecision", {})
            if decision.get("publicDisclosureReviewComplete") is not False:
                fail(errors, "upstream disclosure review template must not claim completed review")
            if decision.get("publicWeightedDomainOutputAllowed") is not False:
                fail(errors, "upstream disclosure review template must block public weighted output")
            slots = template.get("requiredReviewSlots")
            if not isinstance(slots, list) or len(slots) != 15:
                fail(errors, "upstream disclosure review template must contain 15 slots")
            elif any(not isinstance(slot, dict) or slot.get("status") != "pending" for slot in slots):
                fail(errors, "upstream disclosure review template slots must remain pending")

    if not isinstance(validation_path_text, str):
        fail(errors, "upstreamDisclosureReviewTemplate.validationPath must be set")
    else:
        validation_path = REPO_ROOT / validation_path_text
        if not validation_path.exists():
            fail(errors, "upstream disclosure review template validation path does not exist")
        else:
            validation = load_json(validation_path)
            if validation.get("schemaVersion") != (
                "human-infra.nhanes-public-lmf-disclosure-review-template-validation.v1"
            ):
                fail(errors, "upstream disclosure review template validation schemaVersion mismatch")
            if validation.get("overallStatus") != "PASS":
                fail(errors, "upstream disclosure review template validation must pass")
            if validation.get("templatePath") != template_path_text:
                fail(errors, "upstream disclosure review template validation path mismatch")
            if template_sha256 and validation.get("templateSha256") != template_sha256:
                fail(errors, "upstream disclosure review template validation templateSha256 is stale")
            summary = validation.get("summary", {})
            if summary.get("requiredSlotCount") != 15 or summary.get("pendingSlotCount") != 15:
                fail(errors, "upstream disclosure review template validation slot counts mismatch")
            if summary.get("publicDisclosureReviewComplete") is not False:
                fail(errors, "upstream disclosure review template validation must keep review incomplete")
            if summary.get("publicWeightedDomainOutputAllowed") is not False:
                fail(errors, "upstream disclosure review template validation must block public output")
            boundary = validation.get("boundary", {})
            if boundary.get("realWeightedOutputReviewed") is not False:
                fail(errors, "upstream disclosure review template validation must not review real output")
            if boundary.get("publicWeightedDomainOutputAllowed") is not False:
                fail(errors, "upstream disclosure review template validation must block weighted output")


def validate_disclosure_review_execution_upstream(data: dict[str, Any], errors: list[str]) -> None:
    upstream = data.get("upstreamDisclosureReviewExecutionRegister")
    if not isinstance(upstream, dict):
        fail(errors, "upstreamDisclosureReviewExecutionRegister must be an object")
        return

    register_path_text = upstream.get("path")
    validation_path_text = upstream.get("validationPath")
    register_sha256: str | None = None
    if not isinstance(register_path_text, str):
        fail(errors, "upstreamDisclosureReviewExecutionRegister.path must be set")
    else:
        register_path = REPO_ROOT / register_path_text
        if not register_path.exists():
            fail(errors, "upstream disclosure review execution register path does not exist")
        else:
            register_sha256 = sha256_file(register_path)
            if upstream.get("sha256") != register_sha256:
                fail(errors, "upstream disclosure review execution register sha256 is stale")
            register = load_json(register_path)
            if register.get("schemaVersion") != (
                "human-infra.nhanes-public-lmf-disclosure-review-execution-register.v1"
            ):
                fail(errors, "upstream disclosure review execution register schemaVersion mismatch")
            if register.get("status") != "execution-register-ready-public-review-not-complete-release-blocked":
                fail(errors, "upstream disclosure review execution register status mismatch")
            decision = register.get("currentDecision", {})
            if decision.get("publicDisclosureReviewComplete") is not False:
                fail(errors, "upstream disclosure review execution register must not claim completed review")
            if decision.get("publicWeightedDomainOutputAllowed") is not False:
                fail(errors, "upstream disclosure review execution register must block public weighted output")
            if decision.get("releaseDecision") != "blocked-pending-human-disclosure-review":
                fail(errors, "upstream disclosure review execution register releaseDecision mismatch")
            completion = register.get("completionState", {})
            if completion.get("completedSlotCount") != 0 or completion.get("humanReviewedSlotCount") != 0:
                fail(errors, "upstream disclosure review execution register must keep human review incomplete")
            if completion.get("reviewedOutputArtifactHash") is not None:
                fail(errors, "upstream disclosure review execution register must not contain a reviewed output hash")

    if not isinstance(validation_path_text, str):
        fail(errors, "upstreamDisclosureReviewExecutionRegister.validationPath must be set")
    else:
        validation_path = REPO_ROOT / validation_path_text
        if not validation_path.exists():
            fail(errors, "upstream disclosure review execution validation path does not exist")
        else:
            validation = load_json(validation_path)
            if validation.get("schemaVersion") != (
                "human-infra.nhanes-public-lmf-disclosure-review-execution-validation.v1"
            ):
                fail(errors, "upstream disclosure review execution validation schemaVersion mismatch")
            if validation.get("status") != "pass":
                fail(errors, "upstream disclosure review execution validation must pass")
            if validation.get("registerPath") != register_path_text:
                fail(errors, "upstream disclosure review execution validation path mismatch")
            if register_sha256 and validation.get("registerSha256") != register_sha256:
                fail(errors, "upstream disclosure review execution validation registerSha256 is stale")
            summary = validation.get("summary", {})
            if summary.get("requiredSlotCount") != 15 or summary.get("observedSlotCount") != 15:
                fail(errors, "upstream disclosure review execution validation slot counts mismatch")
            if summary.get("machinePrefillAllowedSlotCount") != 8:
                fail(errors, "upstream disclosure review execution validation machine-prefill count mismatch")
            if summary.get("completedSlotCount") != 0 or summary.get("humanReviewedSlotCount") != 0:
                fail(errors, "upstream disclosure review execution validation must keep review incomplete")
            if summary.get("releaseDecision") != "blocked-pending-human-disclosure-review":
                fail(errors, "upstream disclosure review execution validation releaseDecision mismatch")
            boundary = validation.get("boundary", {})
            if boundary.get("publicDisclosureReviewComplete") is not False:
                fail(errors, "upstream disclosure review execution validation must keep review incomplete")
            if boundary.get("publicWeightedDomainOutputAllowed") is not False:
                fail(errors, "upstream disclosure review execution validation must block weighted output")
            if boundary.get("publicOutputImplementationAllowed") is not False:
                fail(errors, "upstream disclosure review execution validation must block implementation")


def validate_local_only_weighted_domain_output_runway(data: dict[str, Any], errors: list[str]) -> None:
    runway = data.get("localOnlyWeightedDomainOutputRunway")
    if not isinstance(runway, dict):
        fail(errors, "localOnlyWeightedDomainOutputRunway must be an object")
        return

    if runway.get("status") != "local-runway-ready-public-output-still-blocked":
        fail(errors, "localOnlyWeightedDomainOutputRunway.status mismatch")
    if runway.get("makeTarget") != "nhanes-public-lmf-weighted-domain-output-local-run-audit":
        fail(errors, "localOnlyWeightedDomainOutputRunway.makeTarget mismatch")

    for key in ("runScriptPath", "validationScriptPath"):
        value = runway.get(key)
        if not isinstance(value, str) or not value:
            fail(errors, f"localOnlyWeightedDomainOutputRunway.{key} must be set")
            continue
        path = REPO_ROOT / value
        if not path.exists():
            fail(errors, f"localOnlyWeightedDomainOutputRunway.{key} does not exist")

    report_path = runway.get("defaultIgnoredReportPath")
    if not isinstance(report_path, str) or not report_path.startswith("build/reports/"):
        fail(errors, "localOnlyWeightedDomainOutputRunway.defaultIgnoredReportPath must stay under build/reports/")

    for key in (
        "requiredForDefaultCheck",
        "defaultCheckIncludesLocalRun",
        "defaultCheckReadsIgnoredReport",
        "ignoredReportMustExistForDefaultCheck",
        "trackedOutputAllowed",
        "webOutputAllowed",
        "rawRowsPersistedAfterRun",
        "publicDisclosureReviewComplete",
        "publicWeightedDomainOutputAllowed",
        "calibrationAllowed",
        "individualPredictionAllowed",
    ):
        require_bool(runway, key, False, errors, "localOnlyWeightedDomainOutputRunway")
    for key in (
        "generatesRealWeightedRatesLocally",
        "generatesRealDesignBasedIntervalsLocally",
        "localRunMayBeAbsentInCleanCheckout",
        "cleanCheckoutDefaultCheckIndependent",
    ):
        require_bool(runway, key, True, errors, "localOnlyWeightedDomainOutputRunway")


def validate_local_disclosure_review_packet_runway(data: dict[str, Any], errors: list[str]) -> None:
    runway = data.get("localDisclosureReviewPacketRunway")
    if not isinstance(runway, dict):
        fail(errors, "localDisclosureReviewPacketRunway must be an object")
        return

    if runway.get("status") != "local-packet-ready-public-release-still-blocked":
        fail(errors, "localDisclosureReviewPacketRunway.status mismatch")
    if runway.get("makeTarget") != "nhanes-public-lmf-local-disclosure-review-packet-audit":
        fail(errors, "localDisclosureReviewPacketRunway.makeTarget mismatch")

    for key in ("buildScriptPath", "validationScriptPath"):
        value = runway.get(key)
        if not isinstance(value, str) or not value:
            fail(errors, f"localDisclosureReviewPacketRunway.{key} must be set")
            continue
        path = REPO_ROOT / value
        if not path.exists():
            fail(errors, f"localDisclosureReviewPacketRunway.{key} does not exist")

    for key in ("defaultIgnoredPacketPath", "defaultIgnoredPacketValidationPath"):
        packet_path = runway.get(key)
        if not isinstance(packet_path, str) or not packet_path.startswith("build/reports/"):
            fail(errors, f"localDisclosureReviewPacketRunway.{key} must stay under build/reports/")

    for key in (
        "requiredForDefaultCheck",
        "defaultCheckIncludesLocalPacket",
        "defaultCheckReadsIgnoredPacket",
        "ignoredPacketMustExistForDefaultCheck",
        "ignoredPacketValidationMustExistForDefaultCheck",
        "packetContainsRealWeightedValues",
        "packetContainsRealDesignBasedIntervals",
        "trackedOutputAllowed",
        "webOutputAllowed",
        "publicDisclosureReviewComplete",
        "publicWeightedDomainOutputAllowed",
        "calibrationAllowed",
        "individualPredictionAllowed",
    ):
        require_bool(runway, key, False, errors, "localDisclosureReviewPacketRunway")
    for key in (
        "bindsLocalWeightedOutputHash",
        "localPacketMayBeAbsentInCleanCheckout",
        "cleanCheckoutDefaultCheckIndependent",
        "packetValidationGeneratedByLocalAudit",
    ):
        require_bool(runway, key, True, errors, "localDisclosureReviewPacketRunway")


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
    require_bool(dof, "publicDataDofSparseReviewComplete", True, errors, "dofSparseDomainContract")
    if dof.get("dofSparseDomainDiagnosticPath") != (
        "domains/c1-boundary-rewriting/longevity-evidence/data/manual/"
        "life_path_nhanes_public_lmf_dof_sparse_domain_diagnostic.json"
    ):
        fail(errors, "dofSparseDomainContract.dofSparseDomainDiagnosticPath mismatch")
    expected_dof_values = {
        "minimumDomainDegreesOfFreedomObserved": 15,
        "dfReviewThreshold": 8,
        "domainsBelowDfReviewThreshold": 0,
        "domainsWithLonelyRepresentedStrata": 0,
        "emptyDomainCombinationCount": 0,
        "domainsBelowLocalMinimumUnweightedRecords": 0,
        "effectiveSampleSizeComputed": False,
        "confidenceIntervalsComputed": False,
    }
    for key, expected in expected_dof_values.items():
        if dof.get(key) != expected:
            fail(errors, f"dofSparseDomainContract.{key} mismatch")

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
    if disclosure.get("disclosureOutputEnvelopePolicyPath") != (
        "domains/c1-boundary-rewriting/longevity-evidence/data/manual/"
        "life_path_nhanes_public_lmf_disclosure_output_envelope_policy.json"
    ):
        fail(errors, "disclosureContract.disclosureOutputEnvelopePolicyPath mismatch")
    if disclosure.get("disclosureOutputEnvelopeTestCasesPath") != (
        "domains/c1-boundary-rewriting/longevity-evidence/data/manual/"
        "life_path_nhanes_public_lmf_disclosure_output_envelope_test_cases.json"
    ):
        fail(errors, "disclosureContract.disclosureOutputEnvelopeTestCasesPath mismatch")
    if disclosure.get("disclosureOutputEnvelopeValidationPath") != (
        "web/src/data/life-path-nhanes-public-lmf-disclosure-output-envelope-validation.json"
    ):
        fail(errors, "disclosureContract.disclosureOutputEnvelopeValidationPath mismatch")
    require_bool(disclosure, "disclosureOutputEnvelopeValidated", True, errors, "disclosureContract")
    require_bool(disclosure, "syntheticOnlyEnvelopeValidation", True, errors, "disclosureContract")
    require_bool(disclosure, "disclosureReviewTemplateRequired", True, errors, "disclosureContract")
    if disclosure.get("disclosureReviewTemplatePath") != (
        "domains/c1-boundary-rewriting/longevity-evidence/data/manual/"
        "life_path_nhanes_public_lmf_disclosure_review_template.json"
    ):
        fail(errors, "disclosureContract.disclosureReviewTemplatePath mismatch")
    if disclosure.get("disclosureReviewTemplateValidationPath") != (
        "web/src/data/life-path-nhanes-public-lmf-disclosure-review-template-validation.json"
    ):
        fail(errors, "disclosureContract.disclosureReviewTemplateValidationPath mismatch")
    require_bool(disclosure, "disclosureReviewTemplateValidated", True, errors, "disclosureContract")
    require_bool(disclosure, "templateOnlyDisclosureReview", True, errors, "disclosureContract")
    require_bool(disclosure, "disclosureReviewExecutionRegisterRequired", True, errors, "disclosureContract")
    if disclosure.get("disclosureReviewExecutionRegisterPath") != (
        "domains/c1-boundary-rewriting/longevity-evidence/data/manual/"
        "life_path_nhanes_public_lmf_disclosure_review_execution_register.json"
    ):
        fail(errors, "disclosureContract.disclosureReviewExecutionRegisterPath mismatch")
    if disclosure.get("disclosureReviewExecutionValidationPath") != (
        "web/src/data/life-path-nhanes-public-lmf-disclosure-review-execution-validation.json"
    ):
        fail(errors, "disclosureContract.disclosureReviewExecutionValidationPath mismatch")
    require_bool(disclosure, "disclosureReviewExecutionRegistered", True, errors, "disclosureContract")
    if disclosure.get("disclosureReviewExecutionCompletedSlotCount") != 0:
        fail(errors, "disclosureContract.disclosureReviewExecutionCompletedSlotCount must be 0")
    if disclosure.get("disclosureReviewExecutionReleaseDecision") != "blocked-pending-human-disclosure-review":
        fail(errors, "disclosureContract.disclosureReviewExecutionReleaseDecision mismatch")
    require_bool(disclosure, "publicDisclosureReviewComplete", False, errors, "disclosureContract")
    require_bool(disclosure, "realWeightedOutputDisclosureReviewComplete", False, errors, "disclosureContract")

    publication = contract.get("publicationReliabilityContract")
    if not isinstance(publication, dict):
        fail(errors, "publicationReliabilityContract must be an object")
        publication = {}
    for key in (
        "effectiveSampleSizeReviewRequired",
        "confidenceIntervalWidthReviewRequired",
        "relativeStandardErrorReviewRequired",
        "domainDofReviewRequired",
    ):
        require_bool(publication, key, True, errors, "publicationReliabilityContract")
    if publication.get("effectiveSampleCiPublicationPolicyPath") != (
        "domains/c1-boundary-rewriting/longevity-evidence/data/manual/"
        "life_path_nhanes_public_lmf_effective_sample_ci_publication_policy.json"
    ):
        fail(errors, "publicationReliabilityContract.effectiveSampleCiPublicationPolicyPath mismatch")
    if publication.get("effectiveSampleCiPublicationTestCasesPath") != (
        "domains/c1-boundary-rewriting/longevity-evidence/data/manual/"
        "life_path_nhanes_public_lmf_effective_sample_ci_publication_test_cases.json"
    ):
        fail(errors, "publicationReliabilityContract.effectiveSampleCiPublicationTestCasesPath mismatch")
    if publication.get("effectiveSampleCiPublicationValidationPath") != (
        "web/src/data/life-path-nhanes-public-lmf-effective-sample-ci-publication-validation.json"
    ):
        fail(errors, "publicationReliabilityContract.effectiveSampleCiPublicationValidationPath mismatch")
    require_bool(
        publication,
        "effectiveSampleCiPublicationCriteriaValidated",
        True,
        errors,
        "publicationReliabilityContract",
    )
    require_bool(
        publication,
        "syntheticOnlyPublicationCriteriaValidation",
        True,
        errors,
        "publicationReliabilityContract",
    )
    require_bool(publication, "realEffectiveSampleSizeComputed", False, errors, "publicationReliabilityContract")
    require_bool(publication, "realConfidenceIntervalsComputed", False, errors, "publicationReliabilityContract")
    require_bool(publication, "realPublicationReviewComplete", False, errors, "publicationReliabilityContract")

    implementation = contract.get("implementationPreflightContract")
    if not isinstance(implementation, dict):
        fail(errors, "implementationPreflightContract must be an object")
        implementation = {}
    require_bool(
        implementation,
        "weightedOutputImplementationPreflightRequired",
        True,
        errors,
        "implementationPreflightContract",
    )
    if implementation.get("weightedOutputImplementationPreflightPolicyPath") != (
        "domains/c1-boundary-rewriting/longevity-evidence/data/manual/"
        "life_path_nhanes_public_lmf_weighted_output_implementation_preflight_policy.json"
    ):
        fail(errors, "implementationPreflightContract.weightedOutputImplementationPreflightPolicyPath mismatch")
    if implementation.get("weightedOutputImplementationPreflightTestCasesPath") != (
        "domains/c1-boundary-rewriting/longevity-evidence/data/manual/"
        "life_path_nhanes_public_lmf_weighted_output_implementation_preflight_test_cases.json"
    ):
        fail(errors, "implementationPreflightContract.weightedOutputImplementationPreflightTestCasesPath mismatch")
    if implementation.get("weightedOutputImplementationPreflightValidationPath") != (
        "web/src/data/life-path-nhanes-public-lmf-weighted-output-implementation-preflight-validation.json"
    ):
        fail(errors, "implementationPreflightContract.weightedOutputImplementationPreflightValidationPath mismatch")
    require_bool(
        implementation,
        "weightedOutputImplementationPreflightValidated",
        True,
        errors,
        "implementationPreflightContract",
    )
    require_bool(
        implementation,
        "syntheticOnlyImplementationPreflight",
        True,
        errors,
        "implementationPreflightContract",
    )
    for key in (
        "realWeightedOutputImplemented",
        "realDesignBasedIntervalsImplemented",
        "rowDropBeforeDesignAllowed",
        "rawRowPersistenceAllowed",
    ):
        require_bool(implementation, key, False, errors, "implementationPreflightContract")

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
        "publicDataDofSparseReviewComplete": True,
        "publicDisclosureOutputEnvelopeValidated": True,
        "publicEffectiveSampleCiPublicationCriteriaValidated": True,
        "publicWeightedOutputImplementationPreflightValidated": True,
        "publicDisclosureReviewTemplateValidated": True,
        "publicDisclosureReviewExecutionRegistered": True,
        "publicDisclosureReviewComplete": False,
        "weightedDomainOutputAllowed": False,
    }
    if data.get("gateSummary") != expected_summary:
        fail(errors, f"gateSummary mismatch: expected {expected_summary}, found {data.get('gateSummary')}")
    if ready != 12 or partial != 0 or blocked != 2:
        fail(errors, "weighted-domain output readiness must remain 12 ready, 0 partial, 2 blocked")


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
    validate_dof_sparse_domain_diagnostic_upstream(data, errors)
    validate_disclosure_output_envelope_upstream(data, errors)
    validate_effective_sample_ci_publication_upstream(data, errors)
    validate_weighted_output_implementation_preflight_upstream(data, errors)
    validate_disclosure_review_template_upstream(data, errors)
    validate_disclosure_review_execution_upstream(data, errors)
    validate_local_only_weighted_domain_output_runway(data, errors)
    validate_local_disclosure_review_packet_runway(data, errors)

    findings = data.get("sourceFindings")
    if not isinstance(findings, list) or len(findings) < 3:
        fail(errors, "sourceFindings must include at least three source-backed findings")
    else:
        findings_text = json.dumps(findings, ensure_ascii=False)
        for token in (
            "domain",
            "full",
            "subset",
            "degrees of freedom",
            "effective sample",
            "confidence interval",
            "implementation preflight",
            "review template",
            "execution register",
            "local disclosure packet",
        ):
            if token not in findings_text:
                fail(errors, f"sourceFindings missing token: {token}")
        for token in ("disclosure", "publication"):
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
        fail(errors, "nextWork must list disclosure, output implementation and publication-review work")
    else:
        next_work_text = " ".join(str(item) for item in data["nextWork"])
        for token in ("disclosure", "weighted-domain output", "effective sample", "confidence interval"):
            if token not in next_work_text:
                fail(errors, f"nextWork missing token: {token}")
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
            "publicDisclosureOutputEnvelopeValidated": data.get("gateSummary", {}).get("publicDisclosureOutputEnvelopeValidated"),
            "publicEffectiveSampleCiPublicationCriteriaValidated": data.get("gateSummary", {}).get(
                "publicEffectiveSampleCiPublicationCriteriaValidated"
            ),
            "publicWeightedOutputImplementationPreflightValidated": data.get("gateSummary", {}).get(
                "publicWeightedOutputImplementationPreflightValidated"
            ),
            "publicDisclosureReviewTemplateValidated": data.get("gateSummary", {}).get(
                "publicDisclosureReviewTemplateValidated"
            ),
            "publicDisclosureReviewExecutionRegistered": data.get("gateSummary", {}).get(
                "publicDisclosureReviewExecutionRegistered"
            ),
            "localOnlyWeightedDomainOutputRunwayReady": (
                data.get("localOnlyWeightedDomainOutputRunway", {}).get("status")
                == "local-runway-ready-public-output-still-blocked"
            ),
            "localOnlyWeightedDomainRunRequiredForDefaultCheck": data.get(
                "localOnlyWeightedDomainOutputRunway", {}
            ).get("requiredForDefaultCheck"),
            "localOnlyWeightedDomainIgnoredReportRequiredForDefaultCheck": data.get(
                "localOnlyWeightedDomainOutputRunway", {}
            ).get("ignoredReportMustExistForDefaultCheck"),
            "localDisclosureReviewPacketRunwayReady": (
                data.get("localDisclosureReviewPacketRunway", {}).get("status")
                == "local-packet-ready-public-release-still-blocked"
            ),
            "localDisclosureReviewPacketRequiredForDefaultCheck": data.get(
                "localDisclosureReviewPacketRunway", {}
            ).get("requiredForDefaultCheck"),
            "localDisclosureReviewPacketIgnoredOutputsRequiredForDefaultCheck": (
                data.get("localDisclosureReviewPacketRunway", {}).get("ignoredPacketMustExistForDefaultCheck")
                or data.get("localDisclosureReviewPacketRunway", {}).get(
                    "ignoredPacketValidationMustExistForDefaultCheck"
                )
            ),
            "cleanCheckoutDefaultCheckIndependent": (
                data.get("localOnlyWeightedDomainOutputRunway", {}).get("cleanCheckoutDefaultCheckIndependent")
                is True
                and data.get("localDisclosureReviewPacketRunway", {}).get(
                    "cleanCheckoutDefaultCheckIndependent"
                )
                is True
            ),
            "publicDisclosureReviewComplete": data.get("gateSummary", {}).get("publicDisclosureReviewComplete"),
            "weightedDomainOutputAllowed": data.get("gateSummary", {}).get("weightedDomainOutputAllowed"),
        },
        "nonProofBoundary": {
            "confirms": [
                "controlled synthetic R survey domain subset smoke is available",
                "public aggregate domain indicator metadata diagnostic is complete without repeating counts or weighted sums",
                "public aggregate DOF/sparse-domain metadata diagnostic is complete without persisting rows, counts or weighted sums",
                "synthetic disclosure output envelope blocks unsafe output shapes",
                "synthetic effective sample / confidence interval publication criteria blocks unsafe publication shapes",
                "synthetic weighted-output implementation preflight blocks unsafe implementation shapes",
                "public disclosure review template is ready but not completed",
                "public disclosure review execution register is ready but has zero completed human-review slots",
                "local-only real weighted-domain run can be generated into ignored build/reports",
                "local disclosure review packet can bind the ignored local output hash without copying real weighted values",
                "default weighted-domain readiness checks are independent of ignored local run and packet outputs",
                "domain indicator, DOF/sparse-domain, synthetic disclosure envelope, synthetic publication criteria, synthetic implementation preflight, disclosure execution and remaining real disclosure gates are registered",
                "public weighted-domain output remains blocked",
            ],
            "doesNotConfirm": [
                "public NHANES weighted domain output",
                "real effective sample size adequacy for publication",
                "disclosure-reviewed real public design-based confidence intervals",
                "disclosure-reviewed real public output",
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
