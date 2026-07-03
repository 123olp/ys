#!/usr/bin/env python3
"""验证 NHANES public-use LMF domain/subpopulation rule readiness 契约。"""

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
    / "life_path_nhanes_public_lmf_domain_subpopulation_rule_readiness.json"
)
DEFAULT_OUTPUT = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhanes-public-lmf-domain-subpopulation-rule-readiness-validation.json"
)

REQUIRED_STATUS = "public-real-data-domain-rule-diagnostic-not-weighted-inference"
REQUIRED_SOURCE_URLS = {
    "varianceEstimationTutorial": "https://wwwn.cdc.gov/nchs/nhanes/tutorials/varianceestimation.aspx",
    "weightingTutorial": "https://wwwn.cdc.gov/nchs/nhanes/tutorials/weighting.aspx",
    "demoDocumentation": "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/DEMO_J.htm",
    "linkedMortalityPage": "https://www.cdc.gov/nchs/linked-data/mortality-files/index.html",
}
REQUIRED_GATE_IDS = {
    "official-domain-mechanisms-documented",
    "full-design-before-domain-documented",
    "domain-indicator-not-implemented",
    "software-estimator-not-selected",
    "positive-weight-eligible-base-not-implemented",
    "domain-dof-review-not-implemented",
    "public-output-disclosure-not-reviewed",
    "calibration-validation-not-started",
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
REQUIRED_TRUE_RULE_FLAGS = {
    "domainIndicatorRequired",
    "fullDesignInputRequired",
    "positiveWeightEligibleBaseRequired",
}
REQUIRED_FALSE_RULE_FLAGS = {
    "rowDropBeforeDesignAllowed",
    "postJoinGroupedCellsAreEstimator",
    "softwareSpecificEstimatorSelected",
    "softwareSpecificEstimatorTested",
    "domainDofReviewed",
    "publicAggregateCellOutputAllowed",
    "weightedDomainInferenceAllowed",
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
    upstream = data.get("upstreamSurveyDesignReadiness")
    if not isinstance(upstream, dict):
        fail(errors, "upstreamSurveyDesignReadiness must be an object")
        return

    readiness_path_text = upstream.get("path")
    validation_path_text = upstream.get("validationPath")
    readiness_sha256: str | None = None
    if not isinstance(readiness_path_text, str):
        fail(errors, "upstreamSurveyDesignReadiness.path must be set")
    else:
        readiness_path = REPO_ROOT / readiness_path_text
        if not readiness_path.exists():
            fail(errors, "upstream survey-design readiness path does not exist")
        else:
            readiness_sha256 = sha256_file(readiness_path)
            if upstream.get("sha256") != readiness_sha256:
                fail(errors, "upstream survey-design readiness sha256 is stale")
            readiness = load_json(readiness_path)
            if (
                readiness.get("schemaVersion")
                != "human-infra.nhanes-public-lmf-survey-design-readiness.v1"
            ):
                fail(errors, "upstream survey-design readiness schemaVersion mismatch")
            if readiness.get("status") != "public-real-data-survey-design-diagnostic-not-weighted-inference":
                fail(errors, "upstream survey-design readiness must remain diagnostic-only")
            if readiness.get("gateSummary", {}).get("weightedInferenceAllowed") is not False:
                fail(errors, "upstream survey-design readiness must still block weighted inference")

    if not isinstance(validation_path_text, str):
        fail(errors, "upstreamSurveyDesignReadiness.validationPath must be set")
    else:
        validation_path = REPO_ROOT / validation_path_text
        if not validation_path.exists():
            fail(errors, "upstream survey-design readiness validation path does not exist")
        else:
            validation = load_json(validation_path)
            if (
                validation.get("schemaVersion")
                != "human-infra.nhanes-public-lmf-survey-design-readiness-validation.v1"
            ):
                fail(errors, "upstream survey-design validation schemaVersion mismatch")
            if validation.get("status") != "pass":
                fail(errors, "upstream survey-design validation must pass")
            if validation.get("readinessPath") != readiness_path_text:
                fail(errors, "upstream survey-design validation path must match readiness path")
            if readiness_sha256 and validation.get("readinessSha256") != readiness_sha256:
                fail(errors, "upstream survey-design validation readinessSha256 is stale")


def validate_payload(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if data.get("schemaVersion") != (
        "human-infra.nhanes-public-lmf-domain-subpopulation-rule-readiness.v1"
    ):
        fail(errors, "schemaVersion mismatch")
    if data.get("readinessId") != (
        "nhanes-public-lmf-2017-2018-domain-subpopulation-rule-readiness"
    ):
        fail(errors, "readinessId mismatch")
    if data.get("status") != REQUIRED_STATUS:
        fail(errors, "status must keep domain-rule diagnostic-only non-inference boundary")
    if data.get("sourceId") != "nhanes-public-lmf-2017-2018":
        fail(errors, "sourceId must bind NHANES public LMF 2017-2018")

    validate_upstream(data, errors)

    if data.get("officialSourceTrace") != REQUIRED_SOURCE_URLS:
        fail(errors, "officialSourceTrace must match official CDC/NCHS URLs")

    findings = data.get("sourceFindings")
    if not isinstance(findings, list) or len(findings) < 4:
        fail(errors, "sourceFindings must contain at least four source-backed facts")
    else:
        findings_text = json.dumps(findings, ensure_ascii=False)
        for token in ("DOMAIN", "SUBPOPX", "subpop", "subset", "WTMEC2YR"):
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

    rule = data.get("domainRule")
    if not isinstance(rule, dict):
        fail(errors, "domainRule must be an object")
        rule = {}
    for flag in REQUIRED_TRUE_RULE_FLAGS:
        if rule.get(flag) is not True:
            fail(errors, f"domainRule.{flag} must be true")
    for flag in REQUIRED_FALSE_RULE_FLAGS:
        if rule.get(flag) is not False:
            fail(errors, f"domainRule.{flag} must be false")

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

    summary = data.get("gateSummary")
    if not isinstance(summary, dict):
        fail(errors, "gateSummary must be an object")
        summary = {}
    expected_summary = {
        "requiredGateCount": len(REQUIRED_GATE_IDS),
        "readyGateCount": ready,
        "partialGateCount": partial,
        "blockedGateCount": blocked,
        "weightedDomainInferenceAllowed": False,
    }
    if summary != expected_summary:
        fail(errors, f"gateSummary mismatch: expected {expected_summary}, found {summary}")
    if ready != 2 or partial != 0 or blocked != 6:
        fail(errors, "domain-rule gate mix must remain 2 ready, 0 partial, 6 blocked")

    if set(data.get("blockedUses", [])) != REQUIRED_BLOCKED_USES:
        fail(errors, "blockedUses must preserve all prohibited inference and individual-use actions")
    if not isinstance(data.get("allowedUses"), list) or len(data["allowedUses"]) < 3:
        fail(errors, "allowedUses must list diagnostic-only uses")
    if not isinstance(data.get("nextWork"), list) or len(data["nextWork"]) < 4:
        fail(errors, "nextWork must list estimator, eligible-base, domain and disclosure work")

    return errors


def build_validation(
    readiness_path: Path,
    output_path: Path,
    errors: list[str],
    data: dict[str, Any],
) -> dict[str, Any]:
    status = "pass" if not errors else "fail"
    return {
        "schemaVersion": (
            "human-infra.nhanes-public-lmf-domain-subpopulation-rule-readiness-validation.v1"
        ),
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
            "weightedDomainInferenceAllowed": data.get("gateSummary", {}).get(
                "weightedDomainInferenceAllowed"
            ),
            "rowDropBeforeDesignAllowed": data.get("domainRule", {}).get(
                "rowDropBeforeDesignAllowed"
            ),
            "softwareSpecificEstimatorSelected": data.get("domainRule", {}).get(
                "softwareSpecificEstimatorSelected"
            ),
        },
        "nonProofBoundary": {
            "confirms": (
                "official NHANES domain/subpopulation rule readiness boundary "
                "and blocked estimator status"
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
            print(f"NHANES public LMF domain/subpopulation readiness error: {error}")
        return 1
    print(
        "NHANES public LMF domain/subpopulation readiness ok: "
        f"ready={output['summary']['readyGateCount']} "
        f"blocked={output['summary']['blockedGateCount']} "
        "boundary=no-weighted-domain-inference"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
