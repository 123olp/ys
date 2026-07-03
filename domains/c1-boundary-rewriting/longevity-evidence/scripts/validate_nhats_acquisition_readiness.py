#!/usr/bin/env python3
"""Validate the NHATS acquisition-readiness gate register."""

from __future__ import annotations

import argparse
import hashlib
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
DEFAULT_REGISTER = MANUAL_DIR / "life_path_nhats_acquisition_readiness.json"
DEFAULT_OUT = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhats-acquisition-readiness-validation.json"
)

REQUIRED_SOURCE_IDS = {
    "data-access",
    "cross-year-search",
    "conditions-of-use",
    "welcome-ai-notice",
    "nhats-files",
    "round-14-files",
    "round-13-files",
}
REQUIRED_GATE_IDS = {
    "official-source-refresh",
    "registration-status",
    "file-access-tier",
    "colectica-variable-confirmation",
    "round-window",
    "survey-design-plan",
    "endpoint-definition",
    "disclosure-control",
    "ai-boundary",
    "storage-destruction-plan",
}
REQUIRED_PROHIBITED_ACTIONS = {
    "download NHATS data before acquisition-ready",
    "write extraction scripts before exact variables and file tiers are complete",
    "place raw NHATS or NSOC data in this repository",
    "upload raw or row-level NHATS or NSOC data to public LLMs or AI platforms",
    "produce individual death-date prediction",
    "claim calibration or validation before governed cohort diagnostics exist",
}
REQUIRED_ALLOWED_AI_INPUTS = {
    "public NHATS documentation URLs",
    "synthetic examples created without row-level NHATS or NSOC data",
    "aggregate non-disclosive outputs that pass disclosure review",
}
PROHIBITED_KEYS = {
    "password",
    "sessionCookie",
    "sessionCookies",
    "authToken",
    "rawNhatsData",
    "rawNsocData",
    "rowLevelData",
    "individualIdentifier",
    "deathDate",
    "individualDeathDate",
}


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
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


def row_ids(rows: Any, key: str = "id") -> set[str]:
    if not isinstance(rows, list):
        return set()
    return {
        str(row[key])
        for row in rows
        if isinstance(row, dict) and isinstance(row.get(key), str)
    }


def as_set(value: Any) -> set[str]:
    if not isinstance(value, list):
        return set()
    return {str(item) for item in value}


def collect_keys(value: Any) -> set[str]:
    keys: set[str] = set()
    if isinstance(value, dict):
        for key, child in value.items():
            keys.add(str(key))
            keys.update(collect_keys(child))
    elif isinstance(value, list):
        for child in value:
            keys.update(collect_keys(child))
    return keys


def add_check(checks: list[dict[str, Any]], check_id: str, passed: bool, detail: str) -> None:
    checks.append({"id": check_id, "status": "PASS" if passed else "FAIL", "detail": detail})


def summarize(checks: list[dict[str, Any]]) -> dict[str, int]:
    return {
        "pass": sum(1 for check in checks if check["status"] == "PASS"),
        "fail": sum(1 for check in checks if check["status"] == "FAIL"),
    }


def validate_register(register: dict[str, Any]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []

    add_check(
        checks,
        "schema-version",
        register.get("schemaVersion") == "human-infra.life-path-nhats-acquisition-readiness.v1",
        f"schemaVersion={register.get('schemaVersion')!r}",
    )

    identity_ok = (
        register.get("sourceId") == "nhats"
        and register.get("acquisitionReadinessId") == "nhats-acquisition-readiness-2026-07-02"
        and register.get("status") == "cannot-extract-yet"
    )
    add_check(
        checks,
        "register-identity",
        identity_ok,
        "register must bind NHATS acquisition readiness and keep cannot-extract-yet status",
    )

    decision = register.get("currentDecision")
    decision_ok = isinstance(decision, dict)
    if isinstance(decision, dict):
        for field in (
            "acquisitionReady",
            "extractionScriptAllowed",
            "rawDataAllowedInRepository",
            "calibrationAllowed",
            "individualPredictionAllowed",
        ):
            decision_ok = decision_ok and decision.get(field) is False
    add_check(
        checks,
        "current-decision-boundary",
        decision_ok,
        "acquisition, extraction, raw repository data, calibration and individual prediction must remain false",
    )

    source_rows = register.get("officialSourceRefresh")
    source_ids = row_ids(source_rows)
    source_rows_ok = isinstance(source_rows, list) and all(
        isinstance(row, dict)
        and isinstance(row.get("url"), str)
        and row["url"].startswith("https://")
        and isinstance(row.get("observedFact"), str)
        and isinstance(row.get("modelConsequence"), str)
        for row in source_rows
    )
    add_check(
        checks,
        "official-source-refresh",
        source_rows_ok and REQUIRED_SOURCE_IDS.issubset(source_ids),
        f"missing={sorted(REQUIRED_SOURCE_IDS - source_ids)}",
    )

    gates = register.get("gates")
    gate_ids = row_ids(gates)
    gates_ok = isinstance(gates, list) and REQUIRED_GATE_IDS.issubset(gate_ids)
    add_check(
        checks,
        "gate-coverage",
        gates_ok,
        f"missing={sorted(REQUIRED_GATE_IDS - gate_ids)}",
    )

    gate_status_ok = True
    blocking_ok = True
    ready_count = 0
    partial_count = 0
    missing_count = 0
    if isinstance(gates, list):
        for gate in gates:
            if not isinstance(gate, dict):
                gate_status_ok = False
                blocking_ok = False
                continue
            status = gate.get("status")
            if status == "ready":
                ready_count += 1
            elif status == "partial":
                partial_count += 1
            elif status == "missing":
                missing_count += 1
            else:
                gate_status_ok = False
            if gate.get("blocksExtraction") is not True:
                blocking_ok = False
    else:
        gate_status_ok = False
        blocking_ok = False
    add_check(
        checks,
        "gate-statuses",
        gate_status_ok and ready_count == 0 and partial_count == 3 and missing_count == 7,
        f"ready={ready_count} partial={partial_count} missing={missing_count}",
    )
    add_check(
        checks,
        "all-gates-block-extraction",
        blocking_ok,
        "every acquisition-readiness gate must block extraction until ready evidence exists",
    )

    summary = register.get("gateSummary")
    summary_ok = (
        isinstance(summary, dict)
        and summary.get("requiredGateCount") == 10
        and summary.get("readyGateCount") == 0
        and summary.get("partialGateCount") == 3
        and summary.get("missingGateCount") == 7
        and summary.get("blockingGateCount") == 10
    )
    add_check(
        checks,
        "gate-summary",
        summary_ok,
        "gate summary must report 10 blocking gates, 0 ready, 3 partial and 7 missing",
    )

    allowed_ai_inputs = as_set(register.get("allowedAiInputs"))
    add_check(
        checks,
        "allowed-ai-input-boundary",
        REQUIRED_ALLOWED_AI_INPUTS.issubset(allowed_ai_inputs),
        f"missing={sorted(REQUIRED_ALLOWED_AI_INPUTS - allowed_ai_inputs)}",
    )

    prohibited_actions = as_set(register.get("prohibitedActions"))
    add_check(
        checks,
        "prohibited-actions",
        REQUIRED_PROHIBITED_ACTIONS.issubset(prohibited_actions),
        f"missing={sorted(REQUIRED_PROHIBITED_ACTIONS - prohibited_actions)}",
    )

    source_trace = as_set(register.get("sourceTrace"))
    source_urls = {
        str(row.get("url"))
        for row in source_rows
        if isinstance(source_rows, list) and isinstance(row, dict)
    }
    add_check(
        checks,
        "source-trace",
        bool(source_urls) and source_urls.issubset(source_trace),
        f"missing={sorted(source_urls - source_trace)}",
    )

    prohibited_keys = sorted(collect_keys(register) & PROHIBITED_KEYS)
    add_check(
        checks,
        "no-credential-or-raw-data-keys",
        not prohibited_keys,
        f"prohibited_keys={prohibited_keys}",
    )

    return checks


def build_report(register_path: Path, register: dict[str, Any]) -> dict[str, Any]:
    checks = validate_register(register)
    decision = register.get("currentDecision") if isinstance(register.get("currentDecision"), dict) else {}
    summary = register.get("gateSummary") if isinstance(register.get("gateSummary"), dict) else {}
    return {
        "schemaVersion": "human-infra.life-path-nhats-acquisition-readiness-validation.v1",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "registerPath": repo_rel(register_path),
        "registerSha256": sha256_file(register_path),
        "acquisitionReadinessId": register.get("acquisitionReadinessId"),
        "overallStatus": "PASS" if summarize(checks)["fail"] == 0 else "FAIL",
        "summary": summarize(checks),
        "gateSummary": summary,
        "boundary": {
            "acquisitionReady": decision.get("acquisitionReady"),
            "extractionScriptAllowed": decision.get("extractionScriptAllowed"),
            "rawDataAllowedInRepository": decision.get("rawDataAllowedInRepository"),
            "calibrationAllowed": decision.get("calibrationAllowed"),
            "individualPredictionAllowed": decision.get("individualPredictionAllowed"),
            "requiredGateCount": summary.get("requiredGateCount"),
            "readyGateCount": summary.get("readyGateCount"),
            "blockingGateCount": summary.get("blockingGateCount"),
        },
        "checks": checks,
        "note": "This validation proves only that NHATS acquisition-readiness gates are explicit and still block extraction. It does not prove registration, governed storage, file downloads, exact variables, real extraction, calibration or individual prediction.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--register", type=Path, default=DEFAULT_REGISTER)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    register_path = args.register.resolve()
    out_path = args.out.resolve()
    register = load_json(register_path)
    report = build_report(register_path, register)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as handle:
        json.dump(report, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(f"wrote {repo_rel(out_path)}")
    print(f"status={report['overallStatus']} checks={report['summary']}")
    return 0 if report["overallStatus"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
