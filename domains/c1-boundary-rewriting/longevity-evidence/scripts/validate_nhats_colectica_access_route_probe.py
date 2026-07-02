#!/usr/bin/env python3
"""Validate the NHATS Colectica access-route probe register."""

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
DEFAULT_REGISTER = MANUAL_DIR / "life_path_nhats_colectica_access_route_probe_register.json"
DEFAULT_EXECUTION_REGISTER = (
    MANUAL_DIR / "life_path_nhats_colectica_value_label_review_execution_register.json"
)
DEFAULT_OUT = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhats-colectica-access-route-probe-validation.json"
)

REQUIRED_EVIDENCE_IDS = {
    "nhats-cross-year-search-official-entry",
    "nhats-colectica-root-anonymous-probe",
    "nhats-colectica-search-anonymous-probe",
    "nhats-colectica-technical-guide",
}
REQUIRED_ROUTE_FIELDS = {
    "identity_join_key",
    "round13_baseline_eligibility",
    "round14_interview_status",
    "proxy_status",
    "facility_residential_status",
    "death_decedent_indicator",
    "nonresponse_missing_code",
    "design_weight_linkage",
    "disclosure_cell_count",
}
REQUIRED_CAPTURE_STEPS = {"CXP-01", "CXP-02", "CXP-03", "CXP-04"}
REQUIRED_TRUE_DECISIONS = {
    "officialAccessRouteProbed",
    "technicalGuideCaptured",
    "anonymousPortalProbeCompleted",
}
REQUIRED_FALSE_DECISIONS = {
    "colecticaAccountCreated",
    "colecticaLoginCompleted",
    "colecticaVariablePagesCaptured",
    "valueLabelsConfirmed",
    "questionTextConfirmed",
    "universeSkipLogicConfirmed",
    "routeValueCrosswalkReady",
    "publicExportAllowed",
    "calibrationAllowed",
    "individualPredictionAllowed",
}
PROHIBITED_KEYS = {
    "password",
    "sessionCookie",
    "sessionCookies",
    "authToken",
    "rawMetadataDump",
    "rawValueLabels",
    "colecticaExportRows",
    "rowLevelData",
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


def has_text(value: Any, needle: str) -> bool:
    return needle.lower() in json.dumps(value, ensure_ascii=False).lower()


def add_check(checks: list[dict[str, Any]], check_id: str, passed: bool, detail: str) -> None:
    checks.append({"id": check_id, "status": "PASS" if passed else "FAIL", "detail": detail})


def summarize(checks: list[dict[str, Any]]) -> dict[str, int]:
    return {
        "pass": sum(1 for check in checks if check["status"] == "PASS"),
        "fail": sum(1 for check in checks if check["status"] == "FAIL"),
    }


def validate_register(register: dict[str, Any], execution_register: dict[str, Any]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []

    add_check(
        checks,
        "schema-version",
        register.get("schemaVersion")
        == "human-infra.life-path-nhats-colectica-access-route-probe-register.v1",
        f"schemaVersion={register.get('schemaVersion')!r}",
    )

    identity_ok = (
        register.get("sourceId") == "nhats"
        and register.get("executionRegisterId") == execution_register.get("executionRegisterId")
        and register.get("status") == "public-entry-and-technical-guide-probed-login-required"
    )
    add_check(
        checks,
        "probe-register-identity",
        identity_ok,
        "probe must bind NHATS, current execution register and login-required probe status",
    )

    decision = register.get("currentDecision")
    decision_ok = isinstance(decision, dict)
    if isinstance(decision, dict):
        for key in REQUIRED_TRUE_DECISIONS:
            decision_ok = decision_ok and decision.get(key) is True
        for key in REQUIRED_FALSE_DECISIONS:
            decision_ok = decision_ok and decision.get(key) is False
    add_check(
        checks,
        "decision-boundary",
        decision_ok,
        "access route may be probed, but account, login, variable pages, labels, export, calibration and individual prediction must remain blocked",
    )

    evidence = register.get("sourceEvidence")
    evidence_ids = row_ids(evidence)
    evidence_ok = isinstance(evidence, list) and all(
        isinstance(row, dict)
        and isinstance(row.get("url"), str)
        and row["url"].startswith("https://")
        and isinstance(row.get("supports"), list)
        and isinstance(row.get("doesNotSupport"), list)
        for row in evidence
    )
    add_check(
        checks,
        "source-evidence",
        evidence_ok and REQUIRED_EVIDENCE_IDS.issubset(evidence_ids),
        f"missing={sorted(REQUIRED_EVIDENCE_IDS - evidence_ids)}",
    )

    probe = register.get("anonymousAccessProbe")
    probe_ok = (
        isinstance(probe, dict)
        and has_text(probe, "No account credentials")
        and probe.get("rootHeadNoFollow", {}).get("observedStatus") == "HTTP/2 302"
        and probe.get("rootHeadNoFollow", {}).get("location") == "/Account/Login?returnUrl=%2F"
        and probe.get("rootGetFollow", {}).get("htmlTitle") == "Log in - NHATS"
        and probe.get("searchGetFollow", {}).get("htmlTitle") == "Log in - NHATS"
    )
    add_check(
        checks,
        "anonymous-access-probe",
        probe_ok,
        "anonymous root and search probes must resolve to login boundary without metadata capture",
    )

    guide = register.get("technicalGuideRoute")
    guide_ok = (
        isinstance(guide, dict)
        and guide.get("requiresAccount") is True
        and has_text(guide, "Details page")
        and has_text(guide, "value labels")
        and has_text(guide, "Basket")
    )
    add_check(
        checks,
        "technical-guide-route",
        guide_ok,
        "technical guide route must require account and describe Details/Basket capture path",
    )

    capture_steps = row_ids(register.get("captureSequence"), key="stepId")
    add_check(
        checks,
        "capture-sequence",
        REQUIRED_CAPTURE_STEPS.issubset(capture_steps),
        f"missing={sorted(REQUIRED_CAPTURE_STEPS - capture_steps)}",
    )

    route_queue = set(register.get("routeFieldCaptureQueue") or [])
    add_check(
        checks,
        "route-field-capture-queue",
        REQUIRED_ROUTE_FIELDS.issubset(route_queue),
        f"missing={sorted(REQUIRED_ROUTE_FIELDS - route_queue)}",
    )

    blocked_until = register.get("blockedUntil")
    blocked_ok = isinstance(blocked_until, list) and all(
        has_text(blocked_until, phrase)
        for phrase in [
            "controlled Colectica account",
            "source hashes",
            "value labels",
            "question text",
            "second reviewer",
        ]
    )
    add_check(
        checks,
        "blocked-until",
        blocked_ok,
        "register must keep account, source hashes, value labels, question text and second review as blockers",
    )

    prohibited_uses = register.get("prohibitedUses")
    prohibited_ok = isinstance(prohibited_uses, list) and all(
        has_text(prohibited_uses, phrase)
        for phrase in [
            "Do not infer value labels",
            "Do not treat anonymous login-page probes as variable metadata",
            "Do not upload NHATS or NSOC raw data",
            "Do not publish individual death dates",
            "Do not enable calibration",
        ]
    )
    add_check(
        checks,
        "prohibited-uses",
        prohibited_ok,
        "probe must block inferred labels, anonymous metadata substitution, public AI upload, death dates and calibration",
    )

    key_hits = sorted(collect_keys(register) & PROHIBITED_KEYS)
    add_check(
        checks,
        "no-credential-or-raw-data-keys",
        not key_hits,
        f"prohibited_keys={key_hits}",
    )

    return checks


def write_validation(
    out_path: Path,
    register_path: Path,
    execution_register_path: Path,
    register: dict[str, Any],
    execution_register: dict[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    summary = summarize(checks)
    report = {
        "schemaVersion": "human-infra.life-path-nhats-colectica-access-route-probe-validation.v1",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "probeRegisterPath": repo_rel(register_path),
        "probeRegisterSha256": sha256_file(register_path),
        "executionRegisterPath": repo_rel(execution_register_path),
        "executionRegisterSha256": sha256_file(execution_register_path),
        "probeRegisterId": register.get("probeRegisterId"),
        "executionRegisterId": execution_register.get("executionRegisterId"),
        "overallStatus": "PASS" if summary["fail"] == 0 else "FAIL",
        "summary": summary,
        "checks": checks,
        "boundary": {
            "officialAccessRouteProbed": register.get("currentDecision", {}).get("officialAccessRouteProbed"),
            "technicalGuideCaptured": register.get("currentDecision", {}).get("technicalGuideCaptured"),
            "anonymousPortalProbeCompleted": register.get("currentDecision", {}).get("anonymousPortalProbeCompleted"),
            "colecticaAccountCreated": register.get("currentDecision", {}).get("colecticaAccountCreated"),
            "colecticaLoginCompleted": register.get("currentDecision", {}).get("colecticaLoginCompleted"),
            "colecticaVariablePagesCaptured": register.get("currentDecision", {}).get("colecticaVariablePagesCaptured"),
            "valueLabelsConfirmed": register.get("currentDecision", {}).get("valueLabelsConfirmed"),
            "publicExportAllowed": register.get("currentDecision", {}).get("publicExportAllowed"),
            "calibrationAllowed": register.get("currentDecision", {}).get("calibrationAllowed"),
            "individualPredictionAllowed": register.get("currentDecision", {}).get("individualPredictionAllowed"),
        },
        "note": "This validation proves only the public access route and login boundary. It does not prove authenticated Colectica access, variable details, value labels, question text, route classifiers, exports, calibration or individual prediction.",
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--register", type=Path, default=DEFAULT_REGISTER)
    parser.add_argument("--execution-register", type=Path, default=DEFAULT_EXECUTION_REGISTER)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    register = load_json(args.register)
    execution_register = load_json(args.execution_register)
    checks = validate_register(register, execution_register)
    write_validation(args.out, args.register, args.execution_register, register, execution_register, checks)
    summary = summarize(checks)
    if summary["fail"]:
        print(f"NHATS Colectica access route probe validation failed: {summary}")
        return 1
    print(f"wrote {repo_rel(args.out)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
