#!/usr/bin/env python3
"""Validate the NHATS R13/R14 file-tier candidate table."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from audit_life_path_toy_model import (  # noqa: E402
    DEFAULT_NHATS_ACQUISITION_READINESS,
    DEFAULT_NHATS_FILE_TIER_TABLE,
    REPO_ROOT,
    add_check,
    audit_nhats_file_tier_table,
    load_json,
    sha256_file,
    status_from_bool,
    summarize_checks,
)


MANUAL_DIR = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
)
DEFAULT_OFFICIAL_SOURCE_REFRESH = (
    MANUAL_DIR / "life_path_nhats_official_source_refresh_register.json"
)
DEFAULT_REGISTRATION_EVIDENCE_TEMPLATE = (
    MANUAL_DIR / "life_path_nhats_registration_evidence_template.json"
)
DEFAULT_OUT = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhats-file-tier-table-validation.json"
)


def repo_rel(path: Path) -> str:
    return str(path.resolve().relative_to(REPO_ROOT))


def count_rows(rows: Any, key: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    if not isinstance(rows, list):
        return counts
    for row in rows:
        if not isinstance(row, dict):
            continue
        value = str(row.get(key, ""))
        if not value:
            continue
        counts[value] = counts.get(value, 0) + 1
    return dict(sorted(counts.items()))


def build_extra_checks(
    table_path: Path,
    table: dict[str, Any],
    acquisition_readiness_path: Path,
    official_source_refresh_path: Path,
    registration_template_path: Path,
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    acquisition = load_json(acquisition_readiness_path)

    binding_ok = (
        acquisition.get("fileTierTableId") == table.get("tableId")
        and acquisition.get("fileTierTablePath") == repo_rel(table_path)
        and acquisition.get("officialSourceRefreshRegisterPath")
        == repo_rel(official_source_refresh_path)
        and acquisition.get("registrationEvidenceTemplatePath")
        == repo_rel(registration_template_path)
        and official_source_refresh_path.exists()
        and registration_template_path.exists()
    )
    add_check(
        checks,
        "upstream-register-bindings",
        status_from_bool(binding_ok),
        "file-tier table must be bound from acquisition readiness and its official-source / registration upstreams must exist",
    )

    tier_gate = None
    gates = acquisition.get("gates")
    if isinstance(gates, list):
        tier_gate = next(
            (
                gate
                for gate in gates
                if isinstance(gate, dict) and gate.get("id") == "file-access-tier"
            ),
            None,
        )
    gate_ok = (
        isinstance(tier_gate, dict)
        and tier_gate.get("status") == "partial"
        and tier_gate.get("blocksExtraction") is True
        and "registration state" in str(tier_gate.get("nextEvidence", "")).lower()
        and "governed storage path" in str(tier_gate.get("nextEvidence", "")).lower()
    )
    add_check(
        checks,
        "acquisition-file-access-tier-gate",
        status_from_bool(gate_ok),
        "acquisition readiness must keep file-access-tier partial and extraction-blocking until registration, approval, canonical format and governed storage are complete",
    )

    decision = table.get("currentDecision")
    hard_boundary_ok = (
        isinstance(decision, dict)
        and decision.get("fileTierTableReady") is False
        and decision.get("downloadAllowed") is False
        and decision.get("extractionScriptAllowed") is False
        and decision.get("rawDataAllowedInRepository") is False
        and decision.get("publicAiUploadAllowed") is False
        and decision.get("calibrationAllowed") is False
        and decision.get("individualPredictionAllowed") is False
        and acquisition.get("status") == "cannot-extract-yet"
    )
    add_check(
        checks,
        "hard-boundary-consistency",
        status_from_bool(hard_boundary_ok),
        "file-tier validation may not move NHATS beyond cannot-extract-yet or open download, extraction, repository storage, public AI upload, calibration or individual prediction",
    )

    return checks


def build_report(
    table_path: Path,
    acquisition_readiness_path: Path,
    official_source_refresh_path: Path,
    registration_template_path: Path,
) -> dict[str, Any]:
    table = load_json(table_path)
    base_audit = audit_nhats_file_tier_table(table_path)
    checks = list(base_audit["checks"])
    checks.extend(
        build_extra_checks(
            table_path,
            table,
            acquisition_readiness_path,
            official_source_refresh_path,
            registration_template_path,
        )
    )
    summary = summarize_checks(checks)
    decision = table.get("currentDecision") if isinstance(table.get("currentDecision"), dict) else {}
    rows = table.get("fileRows")

    return {
        "schemaVersion": "human-infra.life-path-nhats-file-tier-table-validation.v1",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "tablePath": repo_rel(table_path),
        "tableSha256": sha256_file(table_path),
        "acquisitionReadinessPath": repo_rel(acquisition_readiness_path),
        "acquisitionReadinessSha256": sha256_file(acquisition_readiness_path),
        "officialSourceRefreshRegisterPath": repo_rel(official_source_refresh_path),
        "officialSourceRefreshRegisterSha256": sha256_file(official_source_refresh_path),
        "registrationEvidenceTemplatePath": repo_rel(registration_template_path),
        "registrationEvidenceTemplateSha256": sha256_file(registration_template_path),
        "tableId": table.get("tableId"),
        "acquisitionReadinessId": table.get("acquisitionReadinessId"),
        "overallStatus": "PASS" if summary["fail"] == 0 else "FAIL",
        "summary": summary,
        "roundWindowCandidate": table.get("roundWindowCandidate"),
        "rowSummary": {
            "byRound": count_rows(rows, "round"),
            "byAccessTier": count_rows(rows, "accessTier"),
            "byCandidateUse": count_rows(rows, "candidateUse"),
            "byFormat": count_rows(rows, "format"),
            "tierSummary": table.get("tierSummary"),
        },
        "boundary": {
            "fileTierTableReady": decision.get("fileTierTableReady"),
            "downloadAllowed": decision.get("downloadAllowed"),
            "extractionScriptAllowed": decision.get("extractionScriptAllowed"),
            "rawDataAllowedInRepository": decision.get("rawDataAllowedInRepository"),
            "publicAiUploadAllowed": decision.get("publicAiUploadAllowed"),
            "calibrationAllowed": decision.get("calibrationAllowed"),
            "individualPredictionAllowed": decision.get("individualPredictionAllowed"),
        },
        "checks": checks,
        "note": "This validation proves only that the NHATS R13/R14 file-tier candidate table is internally consistent, bound to current upstream access records, and keeps all real download, extraction, raw repository storage, public AI upload, calibration and individual-use actions blocked. It does not prove NHATS registration, data access approval, governed storage execution, Colectica variable confirmation or model readiness.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--table", type=Path, default=DEFAULT_NHATS_FILE_TIER_TABLE)
    parser.add_argument(
        "--acquisition-readiness",
        type=Path,
        default=DEFAULT_NHATS_ACQUISITION_READINESS,
    )
    parser.add_argument(
        "--official-source-refresh",
        type=Path,
        default=DEFAULT_OFFICIAL_SOURCE_REFRESH,
    )
    parser.add_argument(
        "--registration-template",
        type=Path,
        default=DEFAULT_REGISTRATION_EVIDENCE_TEMPLATE,
    )
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    report = build_report(
        args.table.resolve(),
        args.acquisition_readiness.resolve(),
        args.official_source_refresh.resolve(),
        args.registration_template.resolve(),
    )
    out_path = args.out.resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as handle:
        json.dump(report, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(f"wrote {repo_rel(out_path)}")
    print(f"status={report['overallStatus']} checks={report['summary']}")
    return 0 if report["overallStatus"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
