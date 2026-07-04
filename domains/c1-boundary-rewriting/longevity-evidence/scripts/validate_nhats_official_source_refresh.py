#!/usr/bin/env python3
"""Validate the NHATS official-source refresh register.

This audit is intentionally offline. It validates recorded public-source
reachability evidence without re-fetching official pages during `make check`.
"""

from __future__ import annotations

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
DEFAULT_REGISTER = MANUAL_DIR / "life_path_nhats_official_source_refresh_register.json"
DEFAULT_OUT = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhats-official-source-refresh-validation.json"
)

REQUIRED_SCHEMA = "human-infra.life-path-nhats-official-source-refresh.v1"
REQUIRED_STATUS = "official-source-refresh-only-acquisition-still-blocked"
REQUIRED_SOURCE_IDS = {
    "data-access",
    "cross-year-search",
    "conditions-of-use",
    "welcome-ai-notice",
    "nhats-files-index",
    "round-13-files",
    "round-14-files",
    "colectica-technical-guide",
}
REQUIRED_LIVE_REPROBE_ID = "nhats-official-source-live-reprobe-2026-07-04"
REQUIRED_FALSE_DECISIONS = {
    "registrationStatusReady",
    "downloadAllowed",
    "extractionAllowed",
    "rawDataAllowedInRepository",
    "calibrationAllowed",
    "individualPredictionAllowed",
}
REQUIRED_HARD_BOUNDARIES = {
    "no NHATS data file download",
    "no credentials in repository",
    "no raw NHATS or NSOC data in repository",
    "no row-level output",
    "no public AI upload of NHATS or NSOC data",
    "no calibration claim",
    "no individual prediction",
}
REQUIRED_LIVE_REPROBE_FALSE_SUMMARY = {
    "downloadAllowed",
    "extractionAllowed",
    "calibrationAllowed",
    "individualPredictionAllowed",
}
PROHIBITED_KEYS = {
    "password",
    "sessionCookie",
    "sessionCookies",
    "authToken",
    "rawNhatsData",
    "rawNsocData",
    "rowLevelData",
    "deathDate",
    "individualDeathDate",
    "predictedDeathDate",
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
        register.get("schemaVersion") == REQUIRED_SCHEMA,
        f"schemaVersion={register.get('schemaVersion')!r}",
    )
    add_check(
        checks,
        "identity-and-status",
        register.get("sourceId") == "nhats"
        and register.get("status") == REQUIRED_STATUS
        and register.get("refreshRegisterId") == "nhats-official-source-refresh-2026-07-03",
        "register must bind the NHATS 2026-07-03 official-source refresh and keep acquisition blocked",
    )

    decision = register.get("currentDecision")
    decision_ok = isinstance(decision, dict) and decision.get("officialSourceRefreshReady") is True
    if isinstance(decision, dict):
        for field in REQUIRED_FALSE_DECISIONS:
            decision_ok = decision_ok and decision.get(field) is False
    add_check(
        checks,
        "current-decision-boundary",
        decision_ok,
        "official source refresh may be ready, but registration, download, extraction, raw storage, calibration and individual prediction must remain false",
    )

    rows = register.get("sourceRows")
    observed_ids: set[str] = set()
    source_rows_ok = isinstance(rows, list) and len(rows) == len(REQUIRED_SOURCE_IDS)
    if isinstance(rows, list):
        for row in rows:
            if not isinstance(row, dict):
                source_rows_ok = False
                continue
            row_id = row.get("id")
            if isinstance(row_id, str):
                observed_ids.add(row_id)
            source_rows_ok = source_rows_ok and row.get("httpStatus") == 200
            source_rows_ok = source_rows_ok and isinstance(row.get("url"), str)
            source_rows_ok = source_rows_ok and row["url"].startswith("https://")
            source_rows_ok = source_rows_ok and isinstance(row.get("contentLengthBytes"), int)
            source_rows_ok = source_rows_ok and row["contentLengthBytes"] > 10000
            source_rows_ok = source_rows_ok and isinstance(row.get("sha256"), str)
            source_rows_ok = source_rows_ok and len(row["sha256"]) == 64
            source_rows_ok = source_rows_ok and isinstance(row.get("observedFact"), str)
            source_rows_ok = source_rows_ok and isinstance(row.get("modelConsequence"), str)
            source_rows_ok = source_rows_ok and isinstance(row.get("supports"), list)
            source_rows_ok = source_rows_ok and isinstance(row.get("doesNotSupport"), list)
            source_rows_ok = source_rows_ok and any(
                "confirmed" in str(item) or "approved" in str(item) or "complete" in str(item)
                for item in row.get("doesNotSupport", [])
            )
    add_check(
        checks,
        "source-row-coverage",
        source_rows_ok and observed_ids == REQUIRED_SOURCE_IDS,
        f"observed={len(observed_ids)} missing={sorted(REQUIRED_SOURCE_IDS - observed_ids)}",
    )

    live_reprobe = register.get("latestOfficialPublicLiveReprobe")
    live_reprobe_ok = (
        isinstance(live_reprobe, dict)
        and live_reprobe.get("probeId") == REQUIRED_LIVE_REPROBE_ID
        and live_reprobe.get("observedDateLocal") == "2026-07-04"
        and "reachability only" in str(live_reprobe.get("methodBoundary", ""))
    )
    live_summary = live_reprobe.get("summary") if isinstance(live_reprobe, dict) else None
    if isinstance(live_summary, dict):
        live_reprobe_ok = (
            live_reprobe_ok
            and live_summary.get("rows") == len(REQUIRED_SOURCE_IDS)
            and live_summary.get("httpStatus200Rows") == len(REQUIRED_SOURCE_IDS)
            and live_summary.get("htmlGetRows") == len(REQUIRED_SOURCE_IDS) - 1
            and live_summary.get("pdfHeadRows") == 1
        )
        for field in REQUIRED_LIVE_REPROBE_FALSE_SUMMARY:
            live_reprobe_ok = live_reprobe_ok and live_summary.get(field) is False
    live_rows = live_reprobe.get("rows") if isinstance(live_reprobe, dict) else None
    live_ids: set[str] = set()
    live_rows_ok = isinstance(live_rows, list) and len(live_rows) == len(REQUIRED_SOURCE_IDS)
    if isinstance(live_rows, list):
        for row in live_rows:
            if not isinstance(row, dict):
                live_rows_ok = False
                continue
            row_id = row.get("id")
            if isinstance(row_id, str):
                live_ids.add(row_id)
            method = row.get("method")
            live_rows_ok = live_rows_ok and row.get("httpStatus") == 200
            live_rows_ok = live_rows_ok and method in {"GET", "HEAD"}
            live_rows_ok = live_rows_ok and isinstance(row.get("url"), str)
            live_rows_ok = live_rows_ok and row["url"].startswith("https://")
            live_rows_ok = live_rows_ok and isinstance(row.get("finalUrl"), str)
            live_rows_ok = live_rows_ok and row["finalUrl"].startswith("https://")
            live_rows_ok = live_rows_ok and isinstance(row.get("contentType"), str)
            live_rows_ok = live_rows_ok and isinstance(row.get("contentLengthBytes"), int)
            live_rows_ok = live_rows_ok and row["contentLengthBytes"] > 10000
            live_rows_ok = live_rows_ok and isinstance(row.get("doesNotSupport"), list)
            live_rows_ok = live_rows_ok and any(
                "confirmed" in str(item) or "approved" in str(item) or "complete" in str(item)
                for item in row.get("doesNotSupport", [])
            )
            if method == "GET":
                live_rows_ok = live_rows_ok and isinstance(row.get("title"), str)
                live_rows_ok = live_rows_ok and bool(row.get("title", "").strip())
                live_rows_ok = live_rows_ok and isinstance(row.get("sha256"), str)
                live_rows_ok = live_rows_ok and len(row["sha256"]) == 64
            if method == "HEAD":
                live_rows_ok = live_rows_ok and row.get("id") == "colectica-technical-guide"
                live_rows_ok = live_rows_ok and row.get("contentType") == "application/pdf"
                live_rows_ok = live_rows_ok and isinstance(row.get("lastModified"), str)
                live_rows_ok = live_rows_ok and isinstance(row.get("etag"), str)
    add_check(
        checks,
        "latest-official-public-live-reprobe",
        live_reprobe_ok and live_rows_ok and live_ids == REQUIRED_SOURCE_IDS,
        f"observed={len(live_ids)} missing={sorted(REQUIRED_SOURCE_IDS - live_ids)}",
    )

    gate_impact = register.get("gateImpact")
    gate_ok = (
        isinstance(gate_impact, dict)
        and gate_impact.get("acquisitionGateId") == "official-source-refresh"
        and gate_impact.get("newGateStatus") == "ready"
        and isinstance(gate_impact.get("extractionStillBlockedBy"), list)
        and len(gate_impact["extractionStillBlockedBy"]) >= 8
    )
    add_check(
        checks,
        "gate-impact",
        gate_ok,
        "official-source-refresh may become ready, but extraction must remain blocked by downstream gates",
    )

    hard_boundaries = set(register.get("hardBoundaries", []))
    add_check(
        checks,
        "hard-boundaries",
        REQUIRED_HARD_BOUNDARIES.issubset(hard_boundaries),
        f"missing={sorted(REQUIRED_HARD_BOUNDARIES - hard_boundaries)}",
    )

    summary = register.get("summary")
    summary_ok = (
        isinstance(summary, dict)
        and summary.get("sourceRows") == len(REQUIRED_SOURCE_IDS)
        and summary.get("httpStatus200Rows") == len(REQUIRED_SOURCE_IDS)
        and summary.get("officialSourceRefreshReady") is True
        and summary.get("downloadAllowed") is False
        and summary.get("extractionAllowed") is False
        and summary.get("calibrationAllowed") is False
        and summary.get("individualPredictionAllowed") is False
    )
    add_check(
        checks,
        "summary-boundary",
        summary_ok,
        "summary must keep only official-source refresh ready and all model/data actions blocked",
    )

    forbidden_present = sorted(PROHIBITED_KEYS & collect_keys(register))
    add_check(
        checks,
        "no-prohibited-keys",
        not forbidden_present,
        f"forbidden_present={forbidden_present}",
    )

    return checks


def build_report(register_path: Path, output_path: Path) -> dict[str, Any]:
    register = load_json(register_path)
    checks = validate_register(register)
    summary = summarize(checks)
    source_rows = register.get("sourceRows", [])
    row_summaries = [
        {
            "id": row.get("id"),
            "url": row.get("url"),
            "httpStatus": row.get("httpStatus"),
            "contentLengthBytes": row.get("contentLengthBytes"),
            "sha256": row.get("sha256"),
        }
        for row in source_rows
        if isinstance(row, dict)
    ]
    report = {
        "schemaVersion": "human-infra.life-path-nhats-official-source-refresh-validation.v1",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "registerPath": repo_rel(register_path),
        "registerSha256": sha256_file(register_path),
        "refreshRegisterId": register.get("refreshRegisterId"),
        "status": "PASS" if summary["fail"] == 0 else "FAIL",
        "checks": checks,
        "summary": summary,
        "sourceRows": row_summaries,
        "latestOfficialPublicLiveReprobe": register.get("latestOfficialPublicLiveReprobe"),
        "gateImpact": register.get("gateImpact"),
        "boundary": "This validation proves only that public official-source reachability was recorded; it does not authorize data download, extraction, calibration or individual use.",
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return report


def main() -> int:
    report = build_report(DEFAULT_REGISTER, DEFAULT_OUT)
    print(f"wrote {repo_rel(DEFAULT_OUT)}")
    print(f"status={report['status']} checks={report['summary']}")
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
