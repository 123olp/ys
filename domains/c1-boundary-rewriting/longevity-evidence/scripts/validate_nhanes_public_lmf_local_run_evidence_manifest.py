#!/usr/bin/env python3
"""验证 NHANES public-use LMF 本地运行证据清单不泄露真实数值。"""

from __future__ import annotations

import argparse
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
DEFAULT_MANIFEST = MANUAL_DIR / "life_path_nhanes_public_lmf_local_run_evidence_manifest.json"
DEFAULT_OUT = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhanes-public-lmf-local-run-evidence-manifest-validation.json"
)

FORBIDDEN_TRACKED_KEYS = {
    "SEQN",
    "RIDAGEYR",
    "RIAGENDR",
    "recordCount",
    "deathCount",
    "unweightedCount",
    "unweightedRecords",
    "unweightedDeaths",
    "weightSum",
    "weightedDeaths",
    "weightedMortalityRate",
    "standardError",
    "confidenceInterval95",
    "ciLower",
    "ciUpper",
    "relativeStandardError",
    "individualRiskScore",
    "deathDate",
    "rawRows",
    "publicAiPrompt",
    "publicAiResponse",
}

REQUIRED_FALSE_SUMMARY = {
    "rowLevelDataPresentInTrackedManifest",
    "identifierPresentInTrackedManifest",
    "webDataWritten",
    "publicDisclosureReviewComplete",
    "publicWeightedDomainOutputAllowed",
    "calibrationAllowed",
    "individualPredictionAllowed",
    "medicalAdviceAllowed",
}

REQUIRED_TRUE_SUMMARY = {
    "containsRealNhanesPublicUseData",
    "containsRealWeightedRatesInIgnoredReport",
    "containsRealDesignBasedIntervalsInIgnoredReport",
    "realWeightedValuesOmittedFromTrackedManifest",
    "realIntervalValuesOmittedFromTrackedManifest",
}


def load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def repo_rel(path: Path) -> str:
    return str(path.resolve().relative_to(REPO_ROOT))


def collect_keys(value: Any) -> set[str]:
    keys: set[str] = set()
    if isinstance(value, dict):
        for key, nested in value.items():
            keys.add(str(key))
            keys.update(collect_keys(nested))
    elif isinstance(value, list):
        for item in value:
            keys.update(collect_keys(item))
    return keys


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def require_bool(data: dict[str, Any], key: str, expected: bool, errors: list[str], prefix: str) -> None:
    if data.get(key) is not expected:
        fail(errors, f"{prefix}.{key} must be {expected}")


def require_sha(data: dict[str, Any], key: str, errors: list[str], prefix: str) -> None:
    value = data.get(key)
    if not isinstance(value, str) or len(value) != 64 or any(ch not in "0123456789abcdef" for ch in value):
        fail(errors, f"{prefix}.{key} must be a sha256 hex string")


def validate_last_run(manifest: dict[str, Any], errors: list[str]) -> None:
    last_run = manifest.get("lastLocalRunEvidence")
    if not isinstance(last_run, dict):
        fail(errors, "lastLocalRunEvidence must be an object")
        return

    expected_paths = {
        "weightedDomainReportPath": "build/reports/nhanes-public-lmf-weighted-domain-output-local/validation.json",
        "localDisclosurePacketPath": "build/reports/nhanes-public-lmf-local-disclosure-review-packet/validation.json",
        "localDisclosurePacketValidationPath": "build/reports/nhanes-public-lmf-local-disclosure-review-packet/packet-validation.json",
    }
    for key, expected in expected_paths.items():
        if last_run.get(key) != expected:
            fail(errors, f"lastLocalRunEvidence.{key} mismatch")
        if not str(last_run.get(key, "")).startswith("build/reports/"):
            fail(errors, f"lastLocalRunEvidence.{key} must stay under build/reports/")

    expected_status = {
        "weightedDomainReportStatus": "local-real-weighted-domain-output-generated-not-public-not-reviewed",
        "localDisclosurePacketStatus": "local-disclosure-packet-generated-public-release-blocked",
        "localDisclosurePacketValidationStatus": "pass",
    }
    for key, expected in expected_status.items():
        if last_run.get(key) != expected:
            fail(errors, f"lastLocalRunEvidence.{key} mismatch")

    for key in (
        "weightedDomainReportSha256",
        "localDisclosurePacketSha256",
        "localDisclosurePacketValidationSha256",
    ):
        require_sha(last_run, key, errors, "lastLocalRunEvidence")


def validate_summary(manifest: dict[str, Any], errors: list[str]) -> dict[str, Any]:
    summary = manifest.get("redactedSummary")
    if not isinstance(summary, dict):
        fail(errors, "redactedSummary must be an object")
        return {}

    expected_ints = {
        "cellCount": 8,
        "minimumDomainDof": 15,
        "qualityPassCellCount": 8,
        "machinePrefilledReviewSlotCount": 8,
        "requiredReviewSlotCount": 15,
        "humanReviewedSlotCount": 0,
    }
    for key, expected in expected_ints.items():
        if summary.get(key) != expected:
            fail(errors, f"redactedSummary.{key} must be {expected}")

    if summary.get("grouping") != ["sex", "ageBand"]:
        fail(errors, "redactedSummary.grouping mismatch")

    for key in REQUIRED_TRUE_SUMMARY:
        require_bool(summary, key, True, errors, "redactedSummary")
    for key in REQUIRED_FALSE_SUMMARY:
        require_bool(summary, key, False, errors, "redactedSummary")
    return summary


def validate_runtime(manifest: dict[str, Any], errors: list[str]) -> None:
    runtime = manifest.get("runtimeTrace")
    if not isinstance(runtime, dict):
        fail(errors, "runtimeTrace must be an object")
        return
    expected = {
        "estimatorBackend": "R survey",
        "designFunction": "svydesign",
        "domainSubsettingFunction": "survey::subset",
        "varianceMethod": "Taylor linearization",
        "domainIndicatorTiming": "post-design subset via survey::subset",
        "controlledRuntimePath": ".runtime/nhanes-r-survey/bin/Rscript",
        "rVersion": "R version 4.3.3 (2024-02-29)",
        "surveyVersion": "4.4.8",
    }
    for key, value in expected.items():
        if runtime.get(key) != value:
            fail(errors, f"runtimeTrace.{key} mismatch")
    require_bool(runtime, "rowDropBeforeDesign", False, errors, "runtimeTrace")


def validate_targets(manifest: dict[str, Any], errors: list[str]) -> None:
    targets = manifest.get("reproductionTargets")
    if not isinstance(targets, dict):
        fail(errors, "reproductionTargets must be an object")
        return
    expected = {
        "localWeightedRunTarget": "nhanes-public-lmf-weighted-domain-output-local-run-audit",
        "localDisclosurePacketTarget": "nhanes-public-lmf-local-disclosure-review-packet-audit",
        "trackedManifestAuditTarget": "nhanes-public-lmf-local-run-evidence-manifest-audit",
    }
    for key, value in expected.items():
        if targets.get(key) != value:
            fail(errors, f"reproductionTargets.{key} mismatch")


def validate_boundary(manifest: dict[str, Any], errors: list[str]) -> None:
    boundary = manifest.get("trackedArtifactBoundary")
    if not isinstance(boundary, dict):
        fail(errors, "trackedArtifactBoundary must be an object")
        return
    if boundary.get("modelAdmissionDecision") != "blocked":
        fail(errors, "trackedArtifactBoundary.modelAdmissionDecision must remain blocked")
    forbidden = set(boundary.get("forbiddenUse", []))
    for item in (
        "public weighted-domain mortality publication",
        "public design-based confidence interval release",
        "calibrated Human Infra prediction",
        "individual prediction",
        "individual death-date output",
        "medical advice",
    ):
        if item not in forbidden:
            fail(errors, f"trackedArtifactBoundary.forbiddenUse missing {item!r}")
    dependency = str(boundary.get("defaultCheckDependency", ""))
    if "must not require build/reports" not in dependency:
        fail(errors, "trackedArtifactBoundary.defaultCheckDependency must preserve clean checkout independence")


def validate_manifest(path: Path, manifest: dict[str, Any]) -> tuple[list[str], dict[str, Any]]:
    errors: list[str] = []
    if manifest.get("schemaVersion") != "human-infra.nhanes-public-lmf-local-run-evidence-manifest.v1":
        fail(errors, "schemaVersion mismatch")
    if manifest.get("status") != "tracked-redacted-evidence-for-local-run-public-release-blocked":
        fail(errors, "status mismatch")
    if manifest.get("sourceId") != "nhanes-public-lmf-2017-2018":
        fail(errors, "sourceId mismatch")

    validate_last_run(manifest, errors)
    summary = validate_summary(manifest, errors)
    validate_runtime(manifest, errors)
    validate_targets(manifest, errors)
    validate_boundary(manifest, errors)

    leaked_keys = sorted(collect_keys(manifest) & FORBIDDEN_TRACKED_KEYS)
    if leaked_keys:
        fail(errors, f"forbidden tracked keys present: {leaked_keys}")

    return errors, {
        "manifestPath": repo_rel(path),
        "cellCount": summary.get("cellCount"),
        "minimumDomainDof": summary.get("minimumDomainDof"),
        "qualityPassCellCount": summary.get("qualityPassCellCount"),
        "humanReviewedSlotCount": summary.get("humanReviewedSlotCount"),
        "containsRealWeightedRatesInIgnoredReport": summary.get("containsRealWeightedRatesInIgnoredReport"),
        "containsRealDesignBasedIntervalsInIgnoredReport": summary.get("containsRealDesignBasedIntervalsInIgnoredReport"),
        "trackedValuesOmitted": (
            summary.get("realWeightedValuesOmittedFromTrackedManifest") is True
            and summary.get("realIntervalValuesOmittedFromTrackedManifest") is True
        ),
        "publicWeightedDomainOutputAllowed": summary.get("publicWeightedDomainOutputAllowed"),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    manifest = load_json(args.manifest)
    errors, summary = validate_manifest(args.manifest, manifest)
    output = {
        "schemaVersion": "human-infra.nhanes-public-lmf-local-run-evidence-manifest-validation.v1",
        "status": "PASS" if not errors else "FAIL",
        "validatedAt": datetime.now(timezone.utc).isoformat(),
        "summary": summary,
        "errors": errors,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {repo_rel(args.out)}")
    print(f"status={output['status']} summary={summary}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
