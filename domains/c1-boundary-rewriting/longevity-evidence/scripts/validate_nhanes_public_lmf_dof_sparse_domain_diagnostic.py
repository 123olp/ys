#!/usr/bin/env python3
"""验证 NHANES public-use LMF DOF/sparse-domain diagnostic 契约。"""

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
    / "life_path_nhanes_public_lmf_dof_sparse_domain_diagnostic.json"
)
DEFAULT_OUTPUT = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhanes-public-lmf-dof-sparse-domain-diagnostic-validation.json"
)

REQUIRED_STATUS = "public-real-data-dof-sparse-domain-diagnostic-no-weighted-output"
REQUIRED_SOURCE_URLS = {
    "varianceEstimationTutorial": "https://wwwn.cdc.gov/nchs/nhanes/tutorials/varianceestimation.aspx",
    "nchsDataPresentationStandardsForProportions": "https://www.cdc.gov/nchs/data/series/sr_02/sr02_175.pdf",
    "linkedMortalityPage": "https://www.cdc.gov/nchs/linked-data/mortality-files/index.html",
}
REQUIRED_SOURCE_HASHES = {
    "nhanesPublicLmf2017_2018Sha256": (
        "42989d4fe35754d696b770f26553b0a309c110a9e26ab0ee504be3eae5987523"
    ),
    "nhanesDemo2017_2018Sha256": (
        "c0b46e0345ea19404928656277c8b0d10b0cca348a9b2fe4fc3c67e8b7ee73ec"
    ),
    "cdcRReadInProgramSha256": (
        "04c514fd6b798ceb7eeed1afea61f42c6cdd270734c1483e1803027ff9066ac3"
    ),
}
REQUIRED_GATE_IDS = {
    "upstream-aggregate-validation-passed",
    "upstream-domain-indicator-diagnostic-validated",
    "nhanes-subgroup-dof-formula-registered",
    "nchs-df-under-eight-review-rule-registered",
    "public-domain-dof-summary-reviewed",
    "public-domain-lonely-psu-summary-reviewed",
    "public-domain-sparse-summary-reviewed",
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
FORBIDDEN_DIAGNOSTIC_KEYS = {
    "records",
    "deaths",
    "assumedAlive",
    "personMonthsExamTotal",
    "meanFollowupYearsExam",
    "unweightedMortalityFraction",
    "mecWeightSumDiagnostic",
    "mecWeightedDeathCountDiagnostic",
    "SEQN",
    "RIDAGEYR",
    "RIAGENDR",
    "RIDRETH3",
    "WTMEC2YR",
    "SDMVSTRA",
    "SDMVPSU",
}
REQUIRED_FALSE_TRACE_FLAGS = {
    "rawRowsPersisted",
    "individualRowsInOutput",
    "domainRowsPersisted",
    "perDomainRecordCountsPersisted",
    "perDomainDeathsPersisted",
    "perDomainWeightedSumsPersisted",
    "weightedEstimatorExecuted",
    "designBasedVarianceEstimated",
    "publicWeightedDomainRatesAllowed",
    "publicDesignBasedIntervalsAllowed",
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


def find_forbidden_key(value: Any) -> str | None:
    if isinstance(value, dict):
        for key, child in value.items():
            if key in FORBIDDEN_DIAGNOSTIC_KEYS:
                return key
            nested = find_forbidden_key(child)
            if nested:
                return nested
    elif isinstance(value, list):
        for child in value:
            nested = find_forbidden_key(child)
            if nested:
                return nested
    return None


def validate_upstream(
    data: dict[str, Any],
    key: str,
    expected_schema: str,
    expected_status: str,
    expected_validation_schema: str,
    errors: list[str],
) -> dict[str, Any]:
    upstream = data.get(key)
    if not isinstance(upstream, dict):
        fail(errors, f"{key} must be an object")
        return {}

    path_text = upstream.get("path")
    validation_path_text = upstream.get("validationPath")
    upstream_data: dict[str, Any] = {}
    upstream_sha: str | None = None
    if not isinstance(path_text, str):
        fail(errors, f"{key}.path must be set")
    else:
        path = REPO_ROOT / path_text
        if not path.exists():
            fail(errors, f"{key}.path does not exist")
        else:
            upstream_sha = sha256_file(path)
            if upstream.get("sha256") != upstream_sha:
                fail(errors, f"{key}.sha256 is stale")
            upstream_data = load_json(path)
            if upstream_data.get("schemaVersion") != expected_schema:
                fail(errors, f"{key} schemaVersion mismatch")
            if upstream_data.get("status") != expected_status:
                fail(errors, f"{key} status mismatch")

    if not isinstance(validation_path_text, str):
        fail(errors, f"{key}.validationPath must be set")
    else:
        validation_path = REPO_ROOT / validation_path_text
        if not validation_path.exists():
            fail(errors, f"{key}.validationPath does not exist")
        else:
            validation = load_json(validation_path)
            if validation.get("schemaVersion") != expected_validation_schema:
                fail(errors, f"{key} validation schemaVersion mismatch")
            if validation.get("status") != "pass":
                fail(errors, f"{key} validation must pass")
            for validation_key in ("aggregatePath", "diagnosticPath", "readinessPath"):
                if validation.get(validation_key) and validation.get(validation_key) != path_text:
                    fail(errors, f"{key} validation path mismatch")
            if upstream_sha:
                observed_sha = (
                    validation.get("aggregateSha256")
                    or validation.get("diagnosticSha256")
                    or validation.get("readinessSha256")
                )
                if observed_sha != upstream_sha:
                    fail(errors, f"{key} validation source hash is stale")
    return upstream_data


def validate_source_findings(data: dict[str, Any], errors: list[str]) -> None:
    findings = data.get("sourceFindings")
    if not isinstance(findings, list) or len(findings) < 5:
        fail(errors, "sourceFindings must include at least five source-backed findings")
        return

    findings_text = json.dumps(findings, ensure_ascii=False)
    for token in ("degrees of freedom", "subgroup", "8", "denominator"):
        if token not in findings_text:
            fail(errors, f"sourceFindings missing token: {token}")
    full_text = json.dumps(data, ensure_ascii=False)
    if "no-row-persistence" not in full_text and "without persisting rows" not in full_text:
        fail(errors, "diagnostic must preserve no-row-persistence source context")
    for finding in findings:
        if not isinstance(finding, dict):
            fail(errors, "sourceFindings entries must be objects")
            continue
        source_url = str(finding.get("sourceUrl", ""))
        if not (source_url.startswith("https://") or source_url.startswith("domains/")):
            fail(errors, "sourceFindings sourceUrl must be HTTPS or a local repository path")
        if not str(finding.get("observedFact", "")).strip():
            fail(errors, "sourceFindings observedFact must be non-empty")
        if not str(finding.get("modelConsequence", "")).strip():
            fail(errors, "sourceFindings modelConsequence must be non-empty")


def validate_calculation_trace(data: dict[str, Any], errors: list[str]) -> None:
    trace = data.get("calculationTrace")
    if not isinstance(trace, dict):
        fail(errors, "calculationTrace must be an object")
        return
    forbidden = find_forbidden_key(trace)
    if forbidden:
        fail(errors, f"calculationTrace leaked forbidden output key: {forbidden}")
    if trace.get("calculationMode") != "temporary-public-data-summary-no-row-persistence":
        fail(errors, "calculationTrace.calculationMode mismatch")
    if trace.get("sourceHashesFromAggregatePilot") != REQUIRED_SOURCE_HASHES:
        fail(errors, "calculationTrace.sourceHashesFromAggregatePilot mismatch")
    for flag in REQUIRED_FALSE_TRACE_FLAGS:
        require_bool(trace, flag, False, errors, "calculationTrace")


def validate_dof_sparse_diagnostic(data: dict[str, Any], errors: list[str]) -> None:
    diagnostic = data.get("dofSparseDomainDiagnostic")
    if not isinstance(diagnostic, dict):
        fail(errors, "dofSparseDomainDiagnostic must be an object")
        return
    forbidden = find_forbidden_key(diagnostic)
    if forbidden:
        fail(errors, f"dofSparseDomainDiagnostic leaked forbidden output key: {forbidden}")

    expected_values: dict[str, Any] = {
        "diagnosticMode": "domain-dof-sparse-summary-only",
        "domainAxes": ["sex", "ageBand"],
        "expectedDomainCombinationCount": 8,
        "domainCombinationCountReviewed": 8,
        "allExpectedDomainCombinationsPresent": True,
        "allDomainsNonEmpty": True,
        "domainDofFormula": "represented_psu_count - represented_strata_count",
        "overallPositiveWeightDesignStrataInTemp": 15,
        "overallPositiveWeightDesignPsuPairsInTemp": 30,
        "overallDesignDegreesOfFreedomInTemp": 15,
        "minimumDomainDegreesOfFreedomObserved": 15,
        "dfReviewThreshold": 8,
        "domainsBelowDfReviewThreshold": 0,
        "minimumPsuPerRepresentedDomainStratumObserved": 2,
        "domainsWithLonelyRepresentedStrata": 0,
        "emptyDomainCombinationCount": 0,
        "publicDataDofSparseReviewComplete": True,
        "publicOutputDisclosureReviewComplete": False,
        "weightedDomainOutputImplemented": False,
        "weightedDomainOutputAllowed": False,
        "calibrationAllowed": False,
        "individualPredictionAllowed": False,
        "medicalAdviceAllowed": False,
    }
    for key, expected in expected_values.items():
        if diagnostic.get(key) != expected:
            fail(errors, f"dofSparseDomainDiagnostic.{key} mismatch")

    sparse = diagnostic.get("sparseDomainPolicy")
    if not isinstance(sparse, dict):
        fail(errors, "sparseDomainPolicy must be an object")
        sparse = {}
    expected_sparse = {
        "localMinimumUnweightedRecordsPerDomain": 20,
        "nchsMinimumDenominatorSampleSizeForProportions": 30,
        "nchsEffectiveDenominatorSampleSizeReviewRequiredBeforePublication": True,
        "domainsBelowLocalMinimumUnweightedRecords": 0,
        "effectiveSampleSizeComputed": False,
        "confidenceIntervalsComputed": False,
    }
    for key, expected in expected_sparse.items():
        if sparse.get(key) != expected:
            fail(errors, f"sparseDomainPolicy.{key} mismatch")


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
        "readyGateCount": 7,
        "partialGateCount": 0,
        "blockedGateCount": 2,
        "publicDataDofSparseReviewComplete": True,
        "publicDisclosureReviewComplete": False,
        "weightedDomainOutputAllowed": False,
    }
    if data.get("gateSummary") != expected_summary:
        fail(errors, f"gateSummary mismatch: expected {expected_summary}, found {data.get('gateSummary')}")
    if ready != 7 or partial != 0 or blocked != 2:
        fail(errors, "DOF/sparse-domain diagnostic must remain 7 ready, 0 partial, 2 blocked")


def validate_payload(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if data.get("schemaVersion") != "human-infra.nhanes-public-lmf-dof-sparse-domain-diagnostic.v1":
        fail(errors, "schemaVersion mismatch")
    if data.get("diagnosticId") != "nhanes-public-lmf-2017-2018-dof-sparse-domain-diagnostic":
        fail(errors, "diagnosticId mismatch")
    if data.get("status") != REQUIRED_STATUS:
        fail(errors, "status must keep diagnostic-only no-weighted-output boundary")
    if data.get("sourceId") != "nhanes-public-lmf-2017-2018":
        fail(errors, "sourceId must bind NHANES public LMF 2017-2018")
    if data.get("officialSourceTrace") != REQUIRED_SOURCE_URLS:
        fail(errors, "officialSourceTrace must match required public sources")

    validate_upstream(
        data,
        "upstreamAggregate",
        "human-infra.nhanes-public-lmf-aggregate-pilot.v1",
        "public-real-data-aggregate-pilot-not-weighted-not-calibrated",
        "human-infra.nhanes-public-lmf-aggregate-pilot-validation.v1",
        errors,
    )
    validate_upstream(
        data,
        "upstreamDomainIndicatorDiagnostic",
        "human-infra.nhanes-public-lmf-domain-indicator-diagnostic.v1",
        "public-real-data-domain-indicator-metadata-diagnostic-no-weighted-output",
        "human-infra.nhanes-public-lmf-domain-indicator-diagnostic-validation.v1",
        errors,
    )
    validate_source_findings(data, errors)
    validate_calculation_trace(data, errors)
    validate_dof_sparse_diagnostic(data, errors)
    validate_gates(data, errors)

    if set(data.get("blockedUses", [])) != REQUIRED_BLOCKED_USES:
        fail(errors, "blockedUses must preserve all prohibited inference and individual-use actions")
    if not isinstance(data.get("allowedUses"), list) or len(data["allowedUses"]) < 3:
        fail(errors, "allowedUses must list diagnostic-only uses")
    if not isinstance(data.get("nextWork"), list) or len(data["nextWork"]) < 3:
        fail(errors, "nextWork must preserve disclosure, output and effective-sample-size work")
    return errors


def build_validation(diagnostic_path: Path, output_path: Path, errors: list[str], data: dict[str, Any]) -> dict[str, Any]:
    summary = data.get("gateSummary", {})
    diagnostic = data.get("dofSparseDomainDiagnostic", {})
    sparse = diagnostic.get("sparseDomainPolicy", {})
    return {
        "schemaVersion": "human-infra.nhanes-public-lmf-dof-sparse-domain-diagnostic-validation.v1",
        "status": "pass" if not errors else "fail",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "diagnosticPath": rel(diagnostic_path),
        "diagnosticSha256": sha256_file(diagnostic_path),
        "validationPath": rel(output_path),
        "summary": {
            "sourceId": data.get("sourceId"),
            "expectedDomainCombinationCount": diagnostic.get("expectedDomainCombinationCount"),
            "domainCombinationCountReviewed": diagnostic.get("domainCombinationCountReviewed"),
            "minimumDomainDegreesOfFreedomObserved": diagnostic.get(
                "minimumDomainDegreesOfFreedomObserved"
            ),
            "dfReviewThreshold": diagnostic.get("dfReviewThreshold"),
            "domainsBelowDfReviewThreshold": diagnostic.get("domainsBelowDfReviewThreshold"),
            "domainsWithLonelyRepresentedStrata": diagnostic.get(
                "domainsWithLonelyRepresentedStrata"
            ),
            "emptyDomainCombinationCount": diagnostic.get("emptyDomainCombinationCount"),
            "domainsBelowLocalMinimumUnweightedRecords": sparse.get(
                "domainsBelowLocalMinimumUnweightedRecords"
            ),
            "publicDataDofSparseReviewComplete": diagnostic.get("publicDataDofSparseReviewComplete"),
            "publicDisclosureReviewComplete": diagnostic.get("publicOutputDisclosureReviewComplete"),
            "weightedDomainOutputAllowed": diagnostic.get("weightedDomainOutputAllowed"),
            "perDomainRecordCountsPersisted": data.get("calculationTrace", {}).get(
                "perDomainRecordCountsPersisted"
            ),
            "perDomainWeightedSumsPersisted": data.get("calculationTrace", {}).get(
                "perDomainWeightedSumsPersisted"
            ),
            "readyGateCount": summary.get("readyGateCount"),
            "blockedGateCount": summary.get("blockedGateCount"),
        },
        "nonProofBoundary": {
            "confirms": [
                "public aggregate domain DOF/sparse metadata summary is complete for sex × ageBand",
                "the diagnostic persists no rows, per-domain counts, per-domain weighted sums, rates or intervals",
                "public weighted-domain output remains blocked until disclosure and output implementation gates pass",
            ],
            "doesNotConfirm": [
                "public NHANES weighted domain output",
                "effective sample size adequacy for publication",
                "design-based confidence intervals",
                "disclosure-reviewed public weighted cells",
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
    diagnostic_path = args.input.resolve()
    output_path = args.out.resolve()
    data = load_json(diagnostic_path)
    errors = validate_payload(data)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output = build_validation(diagnostic_path, output_path, errors, data)
    output_path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if errors:
        for error in errors:
            print(f"NHANES public LMF DOF/sparse-domain diagnostic error: {error}")
        return 1
    print(
        "NHANES public LMF DOF/sparse-domain diagnostic ok: "
        f"domains={output['summary']['expectedDomainCombinationCount']} "
        f"min_dof={output['summary']['minimumDomainDegreesOfFreedomObserved']} "
        f"ready={output['summary']['readyGateCount']} "
        f"blocked={output['summary']['blockedGateCount']} "
        "boundary=no-weighted-domain-output"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
