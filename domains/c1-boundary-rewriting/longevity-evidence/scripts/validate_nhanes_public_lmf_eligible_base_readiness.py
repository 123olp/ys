#!/usr/bin/env python3
"""验证 NHANES public-use LMF positive-weight eligible-base readiness 契约。"""

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
    / "life_path_nhanes_public_lmf_eligible_base_readiness.json"
)
DEFAULT_OUTPUT = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhanes-public-lmf-eligible-base-readiness-validation.json"
)

REQUIRED_STATUS = "public-real-data-eligible-base-diagnostic-not-weighted-domain-inference"
REQUIRED_SOURCE_URLS = {
    "demoDocumentation": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/DEMO_J.htm",
    "varianceEstimationTutorial": "https://wwwn.cdc.gov/nchs/nhanes/tutorials/varianceestimation.aspx",
    "weightingTutorial": "https://wwwn.cdc.gov/nchs/nhanes/tutorials/weighting.aspx",
    "linkedMortalityPage": "https://www.cdc.gov/nchs/linked-data/mortality-files/index.html",
}
REQUIRED_GATE_IDS = {
    "official-positive-weight-distribution-documented",
    "nonzero-weight-design-input-rule-documented",
    "aggregate-positive-weight-diagnostic-built",
    "no-row-persistence-boundary-validated",
    "software-estimator-not-selected",
    "domain-indicator-not-evaluated-on-design-object",
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
EXPECTED_DIAGNOSTICS = {
    "eligibleAdultRecordsInTemp": 5809,
    "eligibleAdultDeaths": 145,
    "positiveMecWeightEligibleAdultRecordsInTemp": 5809,
    "zeroMecWeightEligibleAdultRecordsInTemp": 0,
    "missingMecWeightEligibleAdultRecordsInTemp": 0,
    "positiveMecWeightEligibleAdultDeaths": 145,
    "zeroMecWeightEligibleAdultDeaths": 0,
    "missingPseudoPsuAmongPositiveWeightEligibleAdultsInTemp": 0,
    "missingPseudoStratumAmongPositiveWeightEligibleAdultsInTemp": 0,
    "positiveWeightStrataInTemp": 15,
    "minimumPsuPerPositiveWeightStratumInTemp": 2,
    "lonelyPositiveWeightStrataInTemp": 0,
}
REQUIRED_FALSE_RULE_FLAGS = {
    "rowDropBeforeDesignAllowed",
    "eligibleBaseRowsPersisted",
    "rawRowsPersisted",
    "aggregateCellsAreEstimator",
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


def validate_upstream_link(
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
                source_hash = validation.get("aggregateSha256") or validation.get("readinessSha256")
                if source_hash != upstream_sha:
                    fail(errors, f"{key} validation source hash is stale")
    return upstream_data


def validate_payload(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if data.get("schemaVersion") != "human-infra.nhanes-public-lmf-eligible-base-readiness.v1":
        fail(errors, "schemaVersion mismatch")
    if data.get("readinessId") != (
        "nhanes-public-lmf-2017-2018-positive-weight-eligible-base-readiness"
    ):
        fail(errors, "readinessId mismatch")
    if data.get("status") != REQUIRED_STATUS:
        fail(errors, "status must keep eligible-base diagnostic-only non-inference boundary")
    if data.get("sourceId") != "nhanes-public-lmf-2017-2018":
        fail(errors, "sourceId must bind NHANES public LMF 2017-2018")

    aggregate = validate_upstream_link(
        data,
        "upstreamAggregate",
        "human-infra.nhanes-public-lmf-aggregate-pilot.v1",
        "public-real-data-aggregate-pilot-not-weighted-not-calibrated",
        "human-infra.nhanes-public-lmf-aggregate-pilot-validation.v1",
        errors,
    )
    survey = validate_upstream_link(
        data,
        "upstreamSurveyDesignReadiness",
        "human-infra.nhanes-public-lmf-survey-design-readiness.v1",
        "public-real-data-survey-design-diagnostic-not-weighted-inference",
        "human-infra.nhanes-public-lmf-survey-design-readiness-validation.v1",
        errors,
    )
    domain = validate_upstream_link(
        data,
        "upstreamDomainRuleReadiness",
        "human-infra.nhanes-public-lmf-domain-subpopulation-rule-readiness.v1",
        "public-real-data-domain-rule-diagnostic-not-weighted-inference",
        "human-infra.nhanes-public-lmf-domain-subpopulation-rule-readiness-validation.v1",
        errors,
    )

    if data.get("officialSourceTrace") != REQUIRED_SOURCE_URLS:
        fail(errors, "officialSourceTrace must match official CDC/NCHS URLs")

    findings = data.get("sourceFindings")
    if not isinstance(findings, list) or len(findings) < 4:
        fail(errors, "sourceFindings must contain at least four source-backed facts")
    else:
        findings_text = json.dumps(findings, ensure_ascii=False)
        for token in ("WTMEC2YR", "8704", "550", "non-zero", "never", "5809"):
            if token not in findings_text:
                fail(errors, f"sourceFindings missing {token}")
        for finding in findings:
            if not isinstance(finding, dict):
                fail(errors, "sourceFindings entries must be objects")
                continue
            source_url = str(finding.get("sourceUrl", ""))
            if not (source_url.startswith("https://") or source_url.startswith("domains/")):
                fail(errors, "sourceFindings sourceUrl must be HTTPS or local governed artifact")
            if not str(finding.get("observedFact", "")).strip():
                fail(errors, "sourceFindings observedFact must be non-empty")
            if not str(finding.get("modelConsequence", "")).strip():
                fail(errors, "sourceFindings modelConsequence must be non-empty")

    rule = data.get("eligibleBaseRule")
    if not isinstance(rule, dict):
        fail(errors, "eligibleBaseRule must be an object")
        rule = {}
    if rule.get("analysisWeight") != "WTMEC2YR":
        fail(errors, "eligibleBaseRule.analysisWeight must be WTMEC2YR")
    if rule.get("positiveWeightCondition") != "WTMEC2YR > 0":
        fail(errors, "eligibleBaseRule.positiveWeightCondition must be WTMEC2YR > 0")
    if rule.get("fullDesignInputBeforeDomainRequired") is not True:
        fail(errors, "fullDesignInputBeforeDomainRequired must be true")
    if rule.get("subpopulationIndicatorRequiredAfterEligibleBase") is not True:
        fail(errors, "subpopulationIndicatorRequiredAfterEligibleBase must be true")
    for flag in REQUIRED_FALSE_RULE_FLAGS:
        if rule.get(flag) is not False:
            fail(errors, f"eligibleBaseRule.{flag} must be false")

    diagnostics = data.get("aggregateDiagnostics")
    if diagnostics != EXPECTED_DIAGNOSTICS:
        fail(errors, "aggregateDiagnostics must match expected positive-weight diagnostics")
    upstream_diagnostics = aggregate.get("aggregate", {}).get("eligibleBaseDiagnostics", {})
    if upstream_diagnostics:
        for key, expected in EXPECTED_DIAGNOSTICS.items():
            upstream_key = key
            if key in {"eligibleAdultRecordsInTemp", "eligibleAdultDeaths"}:
                upstream_value = aggregate.get("aggregate", {}).get(key)
            else:
                upstream_value = upstream_diagnostics.get(upstream_key)
            if upstream_value != expected:
                fail(errors, f"upstream aggregate diagnostic mismatch for {key}")

    if survey.get("gateSummary", {}).get("weightedInferenceAllowed") is not False:
        fail(errors, "upstream survey-design readiness must keep weighted inference blocked")
    if domain.get("gateSummary", {}).get("weightedDomainInferenceAllowed") is not False:
        fail(errors, "upstream domain-rule readiness must keep weighted domain inference blocked")

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
        "weightedDomainInferenceAllowed": False,
    }
    if data.get("gateSummary") != expected_summary:
        fail(errors, f"gateSummary mismatch: expected {expected_summary}, found {data.get('gateSummary')}")
    if ready != 4 or partial != 0 or blocked != 4:
        fail(errors, "eligible-base gate mix must remain 4 ready, 0 partial, 4 blocked")

    if set(data.get("blockedUses", [])) != REQUIRED_BLOCKED_USES:
        fail(errors, "blockedUses must preserve all prohibited inference and individual-use actions")
    if not isinstance(data.get("allowedUses"), list) or len(data["allowedUses"]) < 3:
        fail(errors, "allowedUses must list diagnostic-only uses")
    if not isinstance(data.get("nextWork"), list) or len(data["nextWork"]) < 4:
        fail(errors, "nextWork must list estimator, design object, sparse-domain and disclosure work")

    return errors


def build_validation(
    readiness_path: Path,
    output_path: Path,
    errors: list[str],
    data: dict[str, Any],
) -> dict[str, Any]:
    status = "pass" if not errors else "fail"
    return {
        "schemaVersion": "human-infra.nhanes-public-lmf-eligible-base-readiness-validation.v1",
        "status": status,
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "readinessPath": rel(readiness_path),
        "readinessSha256": sha256_file(readiness_path),
        "validationPath": rel(output_path),
        "summary": {
            "sourceId": data.get("sourceId"),
            "readyGateCount": data.get("gateSummary", {}).get("readyGateCount"),
            "partialGateCount": data.get("gateSummary", {}).get("partialGateCount"),
            "blockedGateCount": data.get("gateSummary", {}).get("blockedGateCount"),
            "positiveMecWeightEligibleAdultRecords": data.get(
                "aggregateDiagnostics", {}
            ).get("positiveMecWeightEligibleAdultRecordsInTemp"),
            "zeroMecWeightEligibleAdultRecords": data.get("aggregateDiagnostics", {}).get(
                "zeroMecWeightEligibleAdultRecordsInTemp"
            ),
            "weightedDomainInferenceAllowed": data.get("gateSummary", {}).get(
                "weightedDomainInferenceAllowed"
            ),
        },
        "nonProofBoundary": {
            "confirms": (
                "positive-weight eligible-base diagnostic readiness and no-row-persistence boundary"
            ),
            "doesNotConfirm": [
                "survey-weighted population inference",
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
            print(f"NHANES public LMF eligible-base readiness error: {error}")
        return 1
    print(
        "NHANES public LMF eligible-base readiness ok: "
        f"positive_weight={output['summary']['positiveMecWeightEligibleAdultRecords']} "
        f"blocked={output['summary']['blockedGateCount']} "
        "boundary=no-weighted-domain-inference"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
