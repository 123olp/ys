#!/usr/bin/env python3
"""验证 NHANES public-use LMF domain indicator metadata diagnostic 契约。"""

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
    / "life_path_nhanes_public_lmf_domain_indicator_diagnostic.json"
)
DEFAULT_OUTPUT = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhanes-public-lmf-domain-indicator-diagnostic-validation.json"
)

REQUIRED_STATUS = "public-real-data-domain-indicator-metadata-diagnostic-no-weighted-output"
REQUIRED_SOURCE_URLS = {
    "varianceEstimationTutorial": "https://wwwn.cdc.gov/nchs/nhanes/tutorials/varianceestimation.aspx",
    "weightingTutorial": "https://wwwn.cdc.gov/nchs/nhanes/tutorials/weighting.aspx",
    "surveySubsetDocumentation": "https://r-survey.r-forge.r-project.org/survey/html/subset.survey.design.html",
    "linkedMortalityPage": "https://www.cdc.gov/nchs/linked-data/mortality-files/index.html",
}
EXPECTED_DOMAIN_LABELS = {
    ("female", "18-39"),
    ("female", "40-59"),
    ("female", "60-79"),
    ("female", "80+"),
    ("male", "18-39"),
    ("male", "40-59"),
    ("male", "60-79"),
    ("male", "80+"),
}
REQUIRED_GATE_IDS = {
    "upstream-aggregate-validation-passed",
    "upstream-weighted-estimator-readiness-validated",
    "domain-axis-contract-registered",
    "expected-domain-combinations-present",
    "no-row-persistence-boundary-validated",
    "no-estimator-output-boundary-validated",
    "domain-dof-sparse-review-not-complete",
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
REQUIRED_FALSE_DIAGNOSTIC_FLAGS = {
    "rowDropBeforeDesignAllowed",
    "rawRowsPersisted",
    "individualRowsInOutput",
    "domainIndicatorRowsPersisted",
    "publicRecordCountsRepeatedByThisDiagnostic",
    "publicDeathCountsRepeatedByThisDiagnostic",
    "publicWeightedSumsRepeatedByThisDiagnostic",
    "weightedEstimatorExecuted",
    "designBasedVarianceEstimated",
    "publicWeightedDomainCellsAllowed",
    "publicWeightedDomainRatesAllowed",
    "publicDesignBasedIntervalsAllowed",
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
            if validation.get("aggregatePath") and validation.get("aggregatePath") != path_text:
                fail(errors, f"{key} validation path mismatch")
            if validation.get("readinessPath") and validation.get("readinessPath") != path_text:
                fail(errors, f"{key} validation path mismatch")
            if upstream_sha:
                observed_sha = validation.get("aggregateSha256") or validation.get("readinessSha256")
                if observed_sha != upstream_sha:
                    fail(errors, f"{key} validation source hash is stale")
    return upstream_data


def validate_aggregate_domain_coverage(aggregate: dict[str, Any], errors: list[str]) -> None:
    cells = aggregate.get("aggregate", {}).get("aggregateCells")
    if not isinstance(cells, list):
        fail(errors, "upstream aggregateCells must be a list")
        return

    labels: set[tuple[str, str]] = set()
    suppressed = 0
    for cell in cells:
        if not isinstance(cell, dict):
            fail(errors, "upstream aggregate cell must be an object")
            continue
        labels.add((str(cell.get("sex")), str(cell.get("ageBand"))))
        if cell.get("suppressed") is True:
            suppressed += 1
    if labels != EXPECTED_DOMAIN_LABELS:
        fail(errors, "upstream aggregate must cover all expected sex × ageBand domain labels")
    if suppressed != 0:
        fail(errors, "current upstream aggregate domain labels must have no suppressed combinations")


def validate_payload(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if data.get("schemaVersion") != "human-infra.nhanes-public-lmf-domain-indicator-diagnostic.v1":
        fail(errors, "schemaVersion mismatch")
    if data.get("diagnosticId") != "nhanes-public-lmf-2017-2018-domain-indicator-diagnostic":
        fail(errors, "diagnosticId mismatch")
    if data.get("status") != REQUIRED_STATUS:
        fail(errors, "status must keep metadata-only no-weighted-output boundary")
    if data.get("sourceId") != "nhanes-public-lmf-2017-2018":
        fail(errors, "sourceId must bind NHANES public LMF 2017-2018")
    if data.get("officialSourceTrace") != REQUIRED_SOURCE_URLS:
        fail(errors, "officialSourceTrace must match required public sources")

    aggregate = validate_upstream(
        data,
        "upstreamAggregate",
        "human-infra.nhanes-public-lmf-aggregate-pilot.v1",
        "public-real-data-aggregate-pilot-not-weighted-not-calibrated",
        "human-infra.nhanes-public-lmf-aggregate-pilot-validation.v1",
        errors,
    )
    validate_upstream(
        data,
        "upstreamWeightedEstimatorReadiness",
        "human-infra.nhanes-public-lmf-weighted-estimator-readiness.v1",
        "public-real-data-estimator-backend-selected-not-weighted-domain-output",
        "human-infra.nhanes-public-lmf-weighted-estimator-readiness-validation.v1",
        errors,
    )
    validate_aggregate_domain_coverage(aggregate, errors)

    findings = data.get("sourceFindings")
    if not isinstance(findings, list) or len(findings) < 3:
        fail(errors, "sourceFindings must include at least three source-backed findings")
    else:
        findings_text = json.dumps(findings, ensure_ascii=False)
        for token in ("subpopulation", "subset", "sex", "ageBand", "no-row-persistence"):
            if token not in findings_text:
                fail(errors, f"sourceFindings missing token: {token}")
        for finding in findings:
            if not isinstance(finding, dict):
                fail(errors, "sourceFindings entries must be objects")
                continue
            source_url = str(finding.get("sourceUrl", ""))
            if not (source_url.startswith("https://") or source_url.startswith("domains/")):
                fail(errors, "sourceFindings sourceUrl must be HTTPS or local repository path")
            if not str(finding.get("observedFact", "")).strip():
                fail(errors, "sourceFindings observedFact must be non-empty")
            if not str(finding.get("modelConsequence", "")).strip():
                fail(errors, "sourceFindings modelConsequence must be non-empty")

    diagnostic = data.get("domainIndicatorDiagnostic")
    if not isinstance(diagnostic, dict):
        fail(errors, "domainIndicatorDiagnostic must be an object")
        diagnostic = {}
    forbidden = find_forbidden_key(diagnostic)
    if forbidden:
        fail(errors, f"domainIndicatorDiagnostic leaked forbidden output key: {forbidden}")
    if diagnostic.get("diagnosticMode") != "aggregate-domain-metadata-only":
        fail(errors, "domainIndicatorDiagnostic.diagnosticMode mismatch")
    if diagnostic.get("domainAxes") != ["sex", "ageBand"]:
        fail(errors, "domainIndicatorDiagnostic.domainAxes must be sex and ageBand")
    if diagnostic.get("expectedSexLevels") != ["female", "male"]:
        fail(errors, "domainIndicatorDiagnostic.expectedSexLevels mismatch")
    if diagnostic.get("expectedAgeBandLevels") != ["18-39", "40-59", "60-79", "80+"]:
        fail(errors, "domainIndicatorDiagnostic.expectedAgeBandLevels mismatch")
    if diagnostic.get("expectedDomainCombinationCount") != 8:
        fail(errors, "expectedDomainCombinationCount must be 8")
    if diagnostic.get("allExpectedDomainCombinationsPresent") is not True:
        fail(errors, "allExpectedDomainCombinationsPresent must be true")
    if diagnostic.get("suppressedDomainCombinationCount") != 0:
        fail(errors, "suppressedDomainCombinationCount must be 0")
    if diagnostic.get("minimumCellCountPolicy") != 20:
        fail(errors, "minimumCellCountPolicy must be 20")
    if diagnostic.get("domainIndicatorRequiredForFutureEstimator") is not True:
        fail(errors, "domainIndicatorRequiredForFutureEstimator must be true")
    if diagnostic.get("domainIndicatorTimingForFutureEstimator") != "after design object creation":
        fail(errors, "domainIndicatorTimingForFutureEstimator mismatch")
    if diagnostic.get("requiresFullDesignInputBeforeDomain") is not True:
        fail(errors, "requiresFullDesignInputBeforeDomain must be true")
    for flag in REQUIRED_FALSE_DIAGNOSTIC_FLAGS:
        if diagnostic.get(flag) is not False:
            fail(errors, f"domainIndicatorDiagnostic.{flag} must be false")

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
            if gate.get("blocksWeightedDomainOutput") is not False:
                fail(errors, f"ready gate {gate_id} must not block weighted output")
        elif status == "partial":
            partial += 1
            if gate.get("blocksWeightedDomainOutput") is not True:
                fail(errors, f"partial gate {gate_id} must block weighted output")
        elif status == "blocked":
            blocked += 1
            if gate.get("blocksWeightedDomainOutput") is not True:
                fail(errors, f"blocked gate {gate_id} must block weighted output")
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
        "domainIndicatorMetadataDiagnosticComplete": True,
        "weightedDomainOutputAllowed": False,
    }
    if data.get("gateSummary") != expected_summary:
        fail(errors, f"gateSummary mismatch: expected {expected_summary}, found {data.get('gateSummary')}")
    if ready != 6 or partial != 0 or blocked != 3:
        fail(errors, "domain indicator diagnostic must remain 6 ready, 0 partial, 3 blocked")
    if set(data.get("blockedUses", [])) != REQUIRED_BLOCKED_USES:
        fail(errors, "blockedUses must preserve all prohibited inference and individual-use actions")
    if not isinstance(data.get("allowedUses"), list) or len(data["allowedUses"]) < 3:
        fail(errors, "allowedUses must list metadata-only uses")
    if not isinstance(data.get("nextWork"), list) or len(data["nextWork"]) < 3:
        fail(errors, "nextWork must list DOF/sparse-domain, disclosure and output implementation work")
    return errors


def build_validation(diagnostic_path: Path, output_path: Path, errors: list[str], data: dict[str, Any]) -> dict[str, Any]:
    summary = data.get("gateSummary", {})
    diagnostic = data.get("domainIndicatorDiagnostic", {})
    return {
        "schemaVersion": "human-infra.nhanes-public-lmf-domain-indicator-diagnostic-validation.v1",
        "status": "pass" if not errors else "fail",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "diagnosticPath": rel(diagnostic_path),
        "diagnosticSha256": sha256_file(diagnostic_path),
        "validationPath": rel(output_path),
        "summary": {
            "sourceId": data.get("sourceId"),
            "domainAxes": diagnostic.get("domainAxes"),
            "expectedDomainCombinationCount": diagnostic.get("expectedDomainCombinationCount"),
            "allExpectedDomainCombinationsPresent": diagnostic.get("allExpectedDomainCombinationsPresent"),
            "readyGateCount": summary.get("readyGateCount"),
            "blockedGateCount": summary.get("blockedGateCount"),
            "domainIndicatorMetadataDiagnosticComplete": summary.get(
                "domainIndicatorMetadataDiagnosticComplete"
            ),
            "weightedDomainOutputAllowed": summary.get("weightedDomainOutputAllowed"),
            "recordCountsRepeatedByThisDiagnostic": diagnostic.get(
                "publicRecordCountsRepeatedByThisDiagnostic"
            ),
            "deathCountsRepeatedByThisDiagnostic": diagnostic.get(
                "publicDeathCountsRepeatedByThisDiagnostic"
            ),
            "weightedSumsRepeatedByThisDiagnostic": diagnostic.get(
                "publicWeightedSumsRepeatedByThisDiagnostic"
            ),
        },
        "nonProofBoundary": {
            "confirms": [
                "public aggregate domain metadata coverage is complete for sex × ageBand",
                "the diagnostic repeats no public record counts, death counts, weighted sums, rates or intervals",
                "public weighted-domain output remains blocked",
            ],
            "doesNotConfirm": [
                "public NHANES weighted domain output",
                "domain degrees-of-freedom or sparse-domain adequacy",
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
            print(f"NHANES public LMF domain indicator diagnostic error: {error}")
        return 1
    print(
        "NHANES public LMF domain indicator diagnostic ok: "
        f"domains={output['summary']['expectedDomainCombinationCount']} "
        f"ready={output['summary']['readyGateCount']} "
        f"blocked={output['summary']['blockedGateCount']} "
        "boundary=no-weighted-domain-output"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
