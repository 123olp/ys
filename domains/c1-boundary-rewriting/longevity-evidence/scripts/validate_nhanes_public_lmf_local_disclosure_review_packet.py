#!/usr/bin/env python3
"""验证本地 NHANES public-use LMF disclosure review packet 边界。"""

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
    / "build"
    / "reports"
    / "nhanes-public-lmf-local-disclosure-review-packet"
    / "validation.json"
)
DEFAULT_OUT = (
    REPO_ROOT
    / "build"
    / "reports"
    / "nhanes-public-lmf-local-disclosure-review-packet"
    / "packet-validation.json"
)

REQUIRED_SLOT_IDS = {
    "output-artifact-identity",
    "source-and-cycle-binding",
    "survey-design-trace",
    "domain-and-dof-trace",
    "effective-sample-ci-trace",
    "disclosure-envelope-trace",
    "small-cell-suppression-review",
    "low-dof-suppression-review",
    "rse-ci-width-review",
    "forbidden-field-scan",
    "row-level-and-identifier-scan",
    "public-ai-and-third-party-upload-scan",
    "output-hash-and-retention-plan",
    "second-reviewer-signoff",
    "release-decision-record",
}

FORBIDDEN_PACKET_KEYS = {
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


def load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
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


def validate_storage(path: Path, packet: dict[str, Any], errors: list[str]) -> None:
    relative = repo_rel(path)
    if not relative.startswith("build/reports/"):
        fail(errors, "review packet must stay under build/reports/")
    if relative.startswith("web/src/data/"):
        fail(errors, "review packet must never be written under web/src/data/")
    storage = packet.get("storage")
    if not isinstance(storage, dict):
        fail(errors, "storage must be an object")
        return
    if storage.get("storageClass") != "ignored-local-build-report":
        fail(errors, "storage.storageClass mismatch")
    if storage.get("packetPath") != relative:
        fail(errors, "storage.packetPath must match input path")
    if not str(storage.get("inputReportPath", "")).startswith("build/reports/"):
        fail(errors, "storage.inputReportPath must stay under build/reports/")
    for key in ("webDataWritten", "trackedArtifactAllowed", "publicExportAllowed"):
        require_bool(storage, key, False, errors, "storage")


def validate_packet(packet: dict[str, Any]) -> tuple[list[str], dict[str, Any]]:
    errors: list[str] = []
    if packet.get("schemaVersion") != "human-infra.nhanes-public-lmf-local-disclosure-review-packet.v1":
        fail(errors, "schemaVersion mismatch")
    if packet.get("status") != "local-disclosure-packet-generated-public-release-blocked":
        fail(errors, "status mismatch")
    if packet.get("sourceId") != "nhanes-public-lmf-2017-2018":
        fail(errors, "sourceId mismatch")
    if packet.get("reviewScope") != "local-only-ignored-weighted-domain-output-disclosure-review-packet":
        fail(errors, "reviewScope mismatch")

    input_identity = packet.get("inputReportIdentity")
    if not isinstance(input_identity, dict):
        fail(errors, "inputReportIdentity must be an object")
    else:
        if input_identity.get("schemaVersion") != "human-infra.nhanes-public-lmf-weighted-domain-output-local-run.v1":
            fail(errors, "inputReportIdentity.schemaVersion mismatch")
        if input_identity.get("status") != "local-real-weighted-domain-output-generated-not-public-not-reviewed":
            fail(errors, "inputReportIdentity.status mismatch")
        if not isinstance(input_identity.get("sha256"), str) or len(input_identity["sha256"]) != 64:
            fail(errors, "inputReportIdentity.sha256 must be a sha256 hex string")

    source_binding = packet.get("sourceBinding")
    if not isinstance(source_binding, dict):
        fail(errors, "sourceBinding must be an object")
    else:
        for key in (
            "nhanesPublicLmf2017_2018Sha256",
            "nhanesDemo2017_2018Sha256",
            "cdcRReadInProgramSha256",
            "localRAnalysisProgramSha256",
        ):
            if not isinstance(source_binding.get(key), str) or len(source_binding[key]) != 64:
                fail(errors, f"sourceBinding.{key} must be a sha256 hex string")

    runtime = packet.get("runtimeTrace")
    if not isinstance(runtime, dict):
        fail(errors, "runtimeTrace must be an object")
    else:
        expected = {
            "estimatorBackend": "R survey",
            "designFunction": "svydesign",
            "domainSubsettingFunction": "survey::subset",
            "varianceMethod": "Taylor linearization",
        }
        for key, value in expected.items():
            if runtime.get(key) != value:
                fail(errors, f"runtimeTrace.{key} mismatch")
        require_bool(runtime, "rowDropBeforeDesign", False, errors, "runtimeTrace")

    summary = packet.get("redactedOutputSummary")
    if not isinstance(summary, dict):
        fail(errors, "redactedOutputSummary must be an object")
    else:
        if summary.get("cellCount") != 8:
            fail(errors, "redactedOutputSummary.cellCount must be 8")
        if not isinstance(summary.get("minimumDomainDof"), int) or summary["minimumDomainDof"] < 8:
            fail(errors, "redactedOutputSummary.minimumDomainDof must be >= 8")
        if summary.get("qualityPassCellCount") != 8:
            fail(errors, "redactedOutputSummary.qualityPassCellCount must be 8")
        for key in (
            "allCellsLocalReleaseBlocked",
            "realWeightedValuesOmittedFromPacket",
            "realIntervalValuesOmittedFromPacket",
        ):
            require_bool(summary, key, True, errors, "redactedOutputSummary")

    machine = packet.get("machineReview")
    if not isinstance(machine, dict):
        fail(errors, "machineReview must be an object")
    else:
        require_bool(machine, "forbiddenValueFieldScanPassed", True, errors, "machineReview")
        for key in (
            "rowLevelDataPresentInPacket",
            "identifierPresentInPacket",
            "publicAiUploadDetected",
            "rawRowsPersistedAfterRun",
            "temporaryAnalysisCsvPersistedAfterRun",
        ):
            require_bool(machine, key, False, errors, "machineReview")

    slots = packet.get("reviewSlots")
    if not isinstance(slots, list):
        fail(errors, "reviewSlots must be a list")
    else:
        observed = {slot.get("slotId") for slot in slots if isinstance(slot, dict)}
        if observed != REQUIRED_SLOT_IDS:
            fail(errors, f"reviewSlots mismatch: {sorted(REQUIRED_SLOT_IDS ^ observed)}")
        for slot in slots:
            if not isinstance(slot, dict):
                fail(errors, "reviewSlots entries must be objects")
                continue
            if slot.get("requiredForPublicRelease") is not True:
                fail(errors, f"slot {slot.get('slotId')} must be requiredForPublicRelease")
            if slot.get("status") not in {"machine-prefilled-pending-human-review", "pending-human-review"}:
                fail(errors, f"slot {slot.get('slotId')} has invalid status")

    completion = packet.get("completionState")
    if not isinstance(completion, dict):
        fail(errors, "completionState must be an object")
    else:
        if completion.get("machinePrefilledSlotCount") != 8:
            fail(errors, "completionState.machinePrefilledSlotCount must be 8")
        if completion.get("requiredSlotCount") != len(REQUIRED_SLOT_IDS):
            fail(errors, "completionState.requiredSlotCount mismatch")
        if completion.get("humanReviewedSlotCount") != 0:
            fail(errors, "completionState.humanReviewedSlotCount must remain 0")
        if completion.get("releaseDecision") != "blocked-pending-human-disclosure-review":
            fail(errors, "completionState.releaseDecision mismatch")
        for key in (
            "secondReviewerSignoffPresent",
            "publicDisclosureReviewComplete",
            "publicWeightedDomainOutputAllowed",
            "calibrationAllowed",
            "individualPredictionAllowed",
        ):
            require_bool(completion, key, False, errors, "completionState")

    leaked_keys = sorted(collect_keys(packet) & FORBIDDEN_PACKET_KEYS)
    if leaked_keys:
        fail(errors, f"forbidden value or row keys present in packet: {leaked_keys}")

    boundary = packet.get("nonProofBoundary")
    if not isinstance(boundary, dict):
        fail(errors, "nonProofBoundary must be an object")
    else:
        confirms = " ".join(str(item) for item in boundary.get("confirms", []))
        does_not = " ".join(str(item) for item in boundary.get("doesNotConfirm", []))
        for token in ("local ignored", "output artifact hash", "omits real weighted values", "public release remains blocked"):
            if token not in confirms:
                fail(errors, f"nonProofBoundary.confirms missing token: {token}")
        for token in ("public disclosure review completion", "public weighted-domain output permission", "calibration", "individual prediction"):
            if token not in does_not:
                fail(errors, f"nonProofBoundary.doesNotConfirm missing token: {token}")

    summary_out = {
        "requiredSlotCount": len(REQUIRED_SLOT_IDS),
        "machinePrefilledSlotCount": packet.get("completionState", {}).get("machinePrefilledSlotCount"),
        "humanReviewedSlotCount": packet.get("completionState", {}).get("humanReviewedSlotCount"),
        "cellCount": packet.get("redactedOutputSummary", {}).get("cellCount"),
        "minimumDomainDof": packet.get("redactedOutputSummary", {}).get("minimumDomainDof"),
        "publicDisclosureReviewComplete": packet.get("completionState", {}).get("publicDisclosureReviewComplete"),
        "publicWeightedDomainOutputAllowed": packet.get("completionState", {}).get("publicWeightedDomainOutputAllowed"),
    }
    return errors, summary_out


def build_validation(path: Path, packet: dict[str, Any], errors: list[str], summary: dict[str, Any]) -> dict[str, Any]:
    return {
        "schemaVersion": "human-infra.nhanes-public-lmf-local-disclosure-review-packet-validation.v1",
        "status": "pass" if not errors else "fail",
        "validatedAt": datetime.now(timezone.utc).isoformat(),
        "inputPath": repo_rel(path),
        "inputSha256": sha256_file(path),
        "summary": summary,
        "boundary": {
            "packetValidated": not errors,
            "packetContainsRealWeightedValues": False,
            "packetContainsRealIntervalValues": False,
            "webDataWritten": False,
            "trackedArtifactAllowed": False,
            "publicDisclosureReviewComplete": False,
            "publicWeightedDomainOutputAllowed": False,
            "calibrationAllowed": False,
            "individualPredictionAllowed": False,
        },
        "errors": errors,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    path = args.input.resolve()
    output_path = args.out.resolve()
    packet = load_json(path)
    errors: list[str] = []
    validate_storage(path, packet, errors)
    packet_errors, summary = validate_packet(packet)
    errors.extend(packet_errors)
    validation = build_validation(path, packet, errors, summary)
    if not repo_rel(output_path).startswith("build/reports/"):
        raise ValueError("local packet validation output must stay under build/reports/")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(validation, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if errors:
        for error in errors:
            print(f"NHANES public LMF local disclosure review packet error: {error}")
        return 1
    print(
        "NHANES public LMF local disclosure review packet ok: "
        f"slots={summary['requiredSlotCount']} "
        f"machine_prefilled={summary['machinePrefilledSlotCount']} "
        f"human_reviewed={summary['humanReviewedSlotCount']} "
        f"wrote={repo_rel(output_path)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
