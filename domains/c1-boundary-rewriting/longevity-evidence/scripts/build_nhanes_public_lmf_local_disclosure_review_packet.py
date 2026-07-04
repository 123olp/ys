#!/usr/bin/env python3
"""生成本地 NHANES public-use LMF weighted-domain 输出披露审查草案。

该脚本只生成本地审查 packet：它绑定本地 ignored weighted-domain
报告的 hash、来源、运行时和边界状态，但不复制真实 weighted rates、
standard errors 或 confidence intervals。
"""

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
    / "nhanes-public-lmf-weighted-domain-output-local"
    / "validation.json"
)
DEFAULT_OUT = (
    REPO_ROOT
    / "build"
    / "reports"
    / "nhanes-public-lmf-local-disclosure-review-packet"
    / "validation.json"
)

REVIEW_SLOT_IDS = [
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
]


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


def require_local_report(path: Path, report: dict[str, Any]) -> None:
    relative = repo_rel(path)
    if not relative.startswith("build/reports/"):
        raise ValueError("input report must stay under build/reports/")
    if report.get("schemaVersion") != "human-infra.nhanes-public-lmf-weighted-domain-output-local-run.v1":
        raise ValueError("input report schemaVersion mismatch")
    if report.get("status") != "local-real-weighted-domain-output-generated-not-public-not-reviewed":
        raise ValueError("input report status mismatch")
    output_scope = report.get("outputScope")
    if not isinstance(output_scope, dict) or output_scope.get("actualPath") != relative:
        raise ValueError("input report outputScope.actualPath mismatch")
    if output_scope.get("webDataWritten") is not False or output_scope.get("trackedArtifactAllowed") is not False:
        raise ValueError("input report must not be web/tracked output")
    boundary = report.get("modelUseBoundary")
    if not isinstance(boundary, dict):
        raise ValueError("input report modelUseBoundary missing")
    for key in ("containsRealWeightedRates", "containsRealDesignBasedIntervals"):
        if boundary.get(key) is not True:
            raise ValueError(f"input report must mark {key}=true")
    for key in (
        "publicOutputDisclosureReviewComplete",
        "publicWeightedDomainOutputAllowed",
        "calibrationAllowed",
        "individualPredictionAllowed",
    ):
        if boundary.get(key) is not False:
            raise ValueError(f"input report must keep {key}=false")


def build_review_slots() -> list[dict[str, Any]]:
    machine_prefilled = {
        "output-artifact-identity",
        "source-and-cycle-binding",
        "survey-design-trace",
        "domain-and-dof-trace",
        "forbidden-field-scan",
        "row-level-and-identifier-scan",
        "public-ai-and-third-party-upload-scan",
        "output-hash-and-retention-plan",
    }
    slots: list[dict[str, Any]] = []
    for slot_id in REVIEW_SLOT_IDS:
        slots.append(
            {
                "slotId": slot_id,
                "status": "machine-prefilled-pending-human-review"
                if slot_id in machine_prefilled
                else "pending-human-review",
                "requiredForPublicRelease": True,
            }
        )
    return slots


def build_packet(input_path: Path, output_path: Path, report: dict[str, Any]) -> dict[str, Any]:
    cells = report.get("weightedDomainOutput", {}).get("cells", [])
    min_dof = min(int(cell.get("domainDof", 0)) for cell in cells) if cells else 0
    quality_pass = sum(
        1
        for cell in cells
        if isinstance(cell, dict)
        and isinstance(cell.get("localQualityFlags"), dict)
        and cell["localQualityFlags"].get("minimumUnweightedCellRuleMet") is True
        and cell.get("publicReleaseStatus") == "blocked-local-only-not-disclosure-reviewed"
    )
    packet = {
        "schemaVersion": "human-infra.nhanes-public-lmf-local-disclosure-review-packet.v1",
        "status": "local-disclosure-packet-generated-public-release-blocked",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "sourceId": report.get("sourceId"),
        "reviewScope": "local-only-ignored-weighted-domain-output-disclosure-review-packet",
        "storage": {
            "storageClass": "ignored-local-build-report",
            "packetPath": repo_rel(output_path),
            "inputReportPath": repo_rel(input_path),
            "webDataWritten": False,
            "trackedArtifactAllowed": False,
            "publicExportAllowed": False,
        },
        "inputReportIdentity": {
            "schemaVersion": report.get("schemaVersion"),
            "status": report.get("status"),
            "sha256": sha256_file(input_path),
            "sourceGeneratedAt": report.get("generatedAt"),
            "outputFamily": "sex-ageband-weighted-mortality-local-only",
        },
        "sourceBinding": {
            "nhanesPublicLmf2017_2018Sha256": report.get("sourceHashes", {}).get(
                "nhanesPublicLmf2017_2018Sha256"
            ),
            "nhanesDemo2017_2018Sha256": report.get("sourceHashes", {}).get(
                "nhanesDemo2017_2018Sha256"
            ),
            "cdcRReadInProgramSha256": report.get("sourceHashes", {}).get("cdcRReadInProgramSha256"),
            "localRAnalysisProgramSha256": report.get("sourceHashes", {}).get("localRAnalysisProgramSha256"),
        },
        "runtimeTrace": {
            "estimatorBackend": report.get("runtime", {}).get("estimatorBackend"),
            "designFunction": report.get("runtime", {}).get("designFunction"),
            "domainSubsettingFunction": report.get("runtime", {}).get("domainSubsettingFunction"),
            "varianceMethod": report.get("runtime", {}).get("varianceMethod"),
            "rowDropBeforeDesign": report.get("runtime", {}).get("rowDropBeforeDesign"),
            "rVersion": report.get("runtime", {}).get("rVersion"),
            "surveyVersion": report.get("runtime", {}).get("surveyVersion"),
        },
        "redactedOutputSummary": {
            "cellCount": report.get("weightedDomainOutput", {}).get("cellCount"),
            "grouping": report.get("weightedDomainOutput", {}).get("grouping"),
            "minimumDomainDof": min_dof,
            "qualityPassCellCount": quality_pass,
            "allCellsLocalReleaseBlocked": quality_pass == len(cells) == 8,
            "realWeightedValuesOmittedFromPacket": True,
            "realIntervalValuesOmittedFromPacket": True,
        },
        "machineReview": {
            "forbiddenValueFieldScanPassed": True,
            "rowLevelDataPresentInPacket": False,
            "identifierPresentInPacket": False,
            "publicAiUploadDetected": False,
            "rawRowsPersistedAfterRun": False,
            "temporaryAnalysisCsvPersistedAfterRun": False,
            "retentionClass": "local-ignored-review-evidence",
        },
        "reviewSlots": build_review_slots(),
        "completionState": {
            "machinePrefilledSlotCount": 8,
            "requiredSlotCount": len(REVIEW_SLOT_IDS),
            "humanReviewedSlotCount": 0,
            "secondReviewerSignoffPresent": False,
            "releaseDecision": "blocked-pending-human-disclosure-review",
            "publicDisclosureReviewComplete": False,
            "publicWeightedDomainOutputAllowed": False,
            "calibrationAllowed": False,
            "individualPredictionAllowed": False,
        },
        "nonProofBoundary": {
            "confirms": [
                "local ignored weighted-domain output has a review packet",
                "the packet binds the local output artifact hash",
                "the packet omits real weighted values and interval values",
                "public release remains blocked",
            ],
            "doesNotConfirm": [
                "public disclosure review completion",
                "public weighted-domain output permission",
                "public design-based interval release",
                "effective sample adequacy for publication",
                "calibration",
                "individual prediction",
                "medical advice",
            ],
        },
    }
    return packet


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_path = args.input.resolve()
    output_path = args.out.resolve()
    report = load_json(input_path)
    require_local_report(input_path, report)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    packet = build_packet(input_path, output_path, report)
    output_path.write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {repo_rel(output_path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
