#!/usr/bin/env python3
"""验证 NHANES public-use LMF R survey runtime smoke readiness 契约。"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
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
    / "life_path_nhanes_public_lmf_r_survey_runtime_smoke_readiness.json"
)
DEFAULT_OUTPUT = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhanes-public-lmf-r-survey-runtime-smoke-validation.json"
)

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
REQUIRED_GATE_IDS = {
    "upstream-weighted-estimator-readiness-validated",
    "runtime-smoke-validator-defined",
    "rscript-runtime-probed-by-validator",
    "survey-package-load-probed-by-validator",
    "synthetic-svydesign-domain-subset-probed-by-validator",
    "public-weighted-output-still-blocked",
}
SMOKE_R_CODE = r"""
suppressPackageStartupMessages(library(survey))
df <- data.frame(
  psu = c(1, 2, 3, 4, 1, 2, 3, 4),
  strata = c(1, 1, 2, 2, 1, 1, 2, 2),
  weight = c(1.2, 0.8, 1.1, 0.9, 1.0, 1.3, 0.7, 1.4),
  domain = c(1, 1, 1, 1, 0, 0, 0, 0),
  y = c(1, 0, 1, 0, 0, 1, 0, 1)
)
design <- svydesign(ids = ~psu, strata = ~strata, weights = ~weight, data = df, nest = TRUE)
domain_design <- subset(design, domain == 1)
estimate <- as.numeric(coef(svymean(~y, domain_design)))
cat(sprintf("human-infra-r-survey-smoke-ok:%0.6f\n", estimate))
"""


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


def run_command(command: list[str], timeout: int) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=timeout,
    )


def validate_upstream(data: dict[str, Any], errors: list[str]) -> None:
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
                fail(errors, "upstream weighted-estimator readiness schemaVersion mismatch")
            if readiness.get("status") != (
                "public-real-data-estimator-backend-selected-not-weighted-domain-output"
            ):
                fail(errors, "upstream weighted-estimator readiness must keep output blocked")

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
                fail(errors, "upstream weighted-estimator validation path must match readiness path")
            if readiness_sha256 and validation.get("readinessSha256") != readiness_sha256:
                fail(errors, "upstream weighted-estimator validation readinessSha256 is stale")


def validate_payload(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if data.get("schemaVersion") != (
        "human-infra.nhanes-public-lmf-r-survey-runtime-smoke-readiness.v1"
    ):
        fail(errors, "schemaVersion mismatch")
    if data.get("readinessId") != "nhanes-public-lmf-2017-2018-r-survey-runtime-smoke-readiness":
        fail(errors, "readinessId mismatch")
    if data.get("status") != "runtime-smoke-gate-defined-no-weighted-domain-output":
        fail(errors, "status must keep runtime-smoke gate in no-output mode")
    if data.get("sourceId") != "nhanes-public-lmf-2017-2018":
        fail(errors, "sourceId must bind NHANES public LMF 2017-2018")

    validate_upstream(data, errors)

    contract = data.get("runtimeSmokeContract")
    if not isinstance(contract, dict):
        fail(errors, "runtimeSmokeContract must be an object")
        contract = {}
    expected = {
        "runtimeExecutable": "Rscript",
        "requiredPackage": "survey",
        "primaryDesignFunction": "svydesign",
        "domainMechanism": "subset.survey.design",
        "timeoutSeconds": 20,
    }
    for key, value in expected.items():
        if contract.get(key) != value:
            fail(errors, f"runtimeSmokeContract.{key} mismatch")
    for flag in (
        "syntheticDataOnly",
        "publicNhanesRowsAllowed",
        "rowPersistenceAllowed",
        "packageInstallAllowed",
        "networkAccessAllowed",
        "weightedDomainOutputAllowed",
        "designBasedIntervalOutputAllowed",
        "calibrationAllowed",
        "individualPredictionAllowed",
    ):
        expected_value = flag == "syntheticDataOnly"
        if contract.get(flag) is not expected_value:
            fail(errors, f"runtimeSmokeContract.{flag} must be {expected_value}")

    cases = data.get("syntheticSmokeCases")
    case_ids = {case.get("id") for case in cases if isinstance(case, dict)} if isinstance(cases, list) else set()
    for case_id in (
        "rscript-runtime-discovery",
        "survey-package-load",
        "synthetic-svydesign-domain-subset",
    ):
        if case_id not in case_ids:
            fail(errors, f"syntheticSmokeCases missing {case_id}")

    gates = data.get("readinessGates")
    if not isinstance(gates, list):
        fail(errors, "readinessGates must be a list")
    else:
        gate_ids = {gate.get("id") for gate in gates if isinstance(gate, dict)}
        if gate_ids != REQUIRED_GATE_IDS:
            fail(errors, "readinessGates must contain the required runtime smoke gates")
        for gate in gates:
            if not isinstance(gate, dict):
                fail(errors, "readinessGates entries must be objects")
                continue
            if gate.get("id") == "public-weighted-output-still-blocked":
                if gate.get("status") != "blocked":
                    fail(errors, "public-weighted-output-still-blocked must remain blocked")
            if not isinstance(gate.get("blocksWeightedDomainOutput"), bool):
                fail(errors, f"{gate.get('id')}.blocksWeightedDomainOutput must be boolean")

    summary = data.get("gateSummary")
    if not isinstance(summary, dict):
        fail(errors, "gateSummary must be an object")
    else:
        expected_summary = {
            "requiredGateCount": 6,
            "readyGateCount": 2,
            "validationEvaluatedGateCount": 3,
            "blockedGateCount": 1,
            "runtimeProbeDefined": True,
            "runtimeSmokeExecutedByReadinessFile": False,
            "weightedDomainOutputAllowed": False,
        }
        for key, value in expected_summary.items():
            if summary.get(key) != value:
                fail(errors, f"gateSummary.{key} mismatch")

    blocked_uses = data.get("blockedUses")
    if not isinstance(blocked_uses, list) or set(blocked_uses) != REQUIRED_BLOCKED_USES:
        fail(errors, "blockedUses must preserve all forbidden output and use boundaries")

    return errors


def probe_runtime(timeout_seconds: int) -> dict[str, Any]:
    rscript_path = shutil.which("Rscript")
    probe: dict[str, Any] = {
        "rscriptPath": rscript_path,
        "rscriptVersion": None,
        "rscriptAvailable": bool(rscript_path),
        "surveyPackageAvailable": False,
        "syntheticSmokeExecuted": False,
        "syntheticSmokePassed": False,
        "smokeStatus": "blocked-no-rscript",
        "stdoutPreview": "",
        "stderrPreview": "",
        "returnCode": None,
    }
    if not rscript_path:
        return probe

    try:
        version = run_command([rscript_path, "--version"], timeout_seconds)
        probe["rscriptVersion"] = (version.stdout or version.stderr).strip()
    except (OSError, subprocess.TimeoutExpired) as exc:
        probe["smokeStatus"] = "blocked-rscript-version-probe-failed"
        probe["stderrPreview"] = str(exc)
        return probe

    try:
        result = run_command([rscript_path, "-e", SMOKE_R_CODE], timeout_seconds)
    except subprocess.TimeoutExpired as exc:
        probe["smokeStatus"] = "blocked-synthetic-smoke-timeout"
        probe["stderrPreview"] = str(exc)
        return probe
    except OSError as exc:
        probe["smokeStatus"] = "blocked-synthetic-smoke-oserror"
        probe["stderrPreview"] = str(exc)
        return probe

    stdout = result.stdout.strip()
    stderr = result.stderr.strip()
    probe["returnCode"] = result.returncode
    probe["stdoutPreview"] = stdout[:500]
    probe["stderrPreview"] = stderr[:500]
    if "there is no package called" in stderr and "survey" in stderr:
        probe["smokeStatus"] = "blocked-survey-package-missing"
        return probe
    if "library(survey)" in stderr or "package" in stderr.lower():
        probe["smokeStatus"] = "blocked-survey-package-load-failed"
        return probe

    probe["surveyPackageAvailable"] = result.returncode == 0
    probe["syntheticSmokeExecuted"] = result.returncode == 0
    probe["syntheticSmokePassed"] = (
        result.returncode == 0 and "human-infra-r-survey-smoke-ok:" in stdout
    )
    probe["smokeStatus"] = (
        "ready-synthetic-r-survey-smoke-passed"
        if probe["syntheticSmokePassed"]
        else "blocked-synthetic-smoke-failed"
    )
    return probe


def build_validation(data: dict[str, Any], input_path: Path, probe: dict[str, Any]) -> dict[str, Any]:
    smoke_ready = probe.get("smokeStatus") == "ready-synthetic-r-survey-smoke-passed"
    return {
        "schemaVersion": "human-infra.nhanes-public-lmf-r-survey-runtime-smoke-validation.v1",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "status": "pass",
        "readinessPath": rel(input_path),
        "readinessSha256": sha256_file(input_path),
        "summary": {
            "runtimeExecutable": data["runtimeSmokeContract"]["runtimeExecutable"],
            "requiredPackage": data["runtimeSmokeContract"]["requiredPackage"],
            "runtimeProbeExecuted": True,
            "rscriptAvailable": probe["rscriptAvailable"],
            "surveyPackageAvailable": probe["surveyPackageAvailable"],
            "syntheticSmokeExecuted": probe["syntheticSmokeExecuted"],
            "syntheticSmokePassed": probe["syntheticSmokePassed"],
            "smokeStatus": probe["smokeStatus"],
            "weightedDomainOutputAllowed": False,
            "individualPredictionAllowed": False,
        },
        "runtimeProbe": probe,
        "nonProofBoundary": {
            "confirms": [
                "runtime probe contract validity",
                "current environment Rscript/survey smoke status",
                "no public NHANES rows touched by smoke test",
                "weighted output remains blocked",
            ],
            "doesNotConfirm": [
                "public NHANES weighted domain output",
                "design-based confidence intervals",
                "domain degrees-of-freedom or sparse-domain policy",
                "disclosure-reviewed public output",
                "calibration",
                "individual prediction",
                "medical advice",
            ],
        },
        "nextAction": (
            "Add domain indicator, DOF/sparse-domain and disclosure gates before public weighted output."
            if smoke_ready
            else "Install/provide Rscript with the R survey package in a controlled runtime, then rerun this smoke gate."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    data = load_json(args.input)
    errors = validate_payload(data)
    timeout_seconds = int(data["runtimeSmokeContract"]["timeoutSeconds"])
    probe = probe_runtime(timeout_seconds)
    validation = build_validation(data, args.input, probe)

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(validation, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        "NHANES public LMF R survey runtime smoke gate ok: "
        f"smoke={probe['smokeStatus']} weighted_output=blocked"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
