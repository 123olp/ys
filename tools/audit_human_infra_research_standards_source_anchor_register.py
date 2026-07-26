#!/usr/bin/env python3
"""审计 Human Infra 外部科研标准锚点注册表。"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = ROOT / "docs/reference/human-infra-research-standards-source-anchor-register.json"
DEFAULT_JSON_OUT = ROOT / "web/src/data/human-infra-research-standards-source-anchor-validation.json"

SCHEMA = "human-infra.research-standards-source-anchor-register.v1"
STATUS = "active-standards-anchor-register-no-model-admission"
VALIDATION_SCHEMA = "human-infra.research-standards-source-anchor-validation.v1"
REGISTER_LINK = "human-infra-research-standards-source-anchor-register.json"
SCRIPT_LINK = "audit_human_infra_research_standards_source_anchor_register.py"
VALIDATION_LINK = "human-infra-research-standards-source-anchor-validation.json"

REQUIRED_SOURCE_KEYS = {
    "evidencePolicy",
    "sourceCardSystem",
    "modelAdmissionContract",
    "modelAdmissionCandidateRegistry",
    "l4ValidationCalibrationReportingContract",
    "l4ValidationCalibrationReportExecutionRegister",
    "maturityGapRegister",
}
REQUIRED_ANCHOR_IDS = {
    "RSA-TRIPOD-AI-2024",
    "RSA-PROBAST-AI-2024",
    "RSA-STROBE-OBSERVATIONAL",
    "RSA-RECORD-ROUTINE-DATA",
    "RSA-CONSORT-2025",
    "RSA-SPIRIT-2025",
    "RSA-CONSORT-AI-2020",
    "RSA-SPIRIT-AI-2020",
    "RSA-PRISMA-2020",
    "RSA-GRADE-CERTAINTY",
    "RSA-ROB2-RCT-BIAS",
    "RSA-ROBINS-I-V2",
    "RSA-TARGET-TRIAL-EMULATION",
    "RSA-START-RWE",
    "RSA-ISPOR-SMDM-MODELING",
}
REQUIRED_STANDARD_FAMILIES = {
    "prediction-model-reporting",
    "prediction-model-bias-applicability",
    "observational-reporting",
    "routinely-collected-data-reporting",
    "randomized-trial-reporting",
    "trial-protocol-reporting",
    "ai-trial-reporting",
    "ai-trial-protocol-reporting",
    "systematic-review-reporting",
    "evidence-certainty",
    "randomized-risk-of-bias",
    "nonrandomized-intervention-risk-of-bias",
    "causal-emulation-design",
    "real-world-evidence-planning-reporting",
    "model-transparency-validation",
}
REQUIRED_NEVER_EVIDENCE = {
    "individual-prediction",
    "medical-advice",
    "longevity-escape-velocity-proof",
}
REQUIRED_FALSE_DECISION_KEYS = {
    "standardsProveInterventionEffects",
    "standardsProveModelCalibration",
    "standardsPermitIndividualPrediction",
    "standardsPermitMedicalAdvice",
    "standardsPermitLongevityEscapeVelocityClaim",
    "l4AggregateCalibratedAdmissionAllowed",
    "publicWeightedDomainOutputAllowed",
}
REQUIRED_INDEX_LINKS = {
    "README.md": REGISTER_LINK,
    "docs/AGENTS.md": REGISTER_LINK,
    "docs/reference/README.md": REGISTER_LINK,
    "docs/reference/human-infra-maturity-roadmap.md": REGISTER_LINK,
    "docs/reference/human-infra-maturity-gap-register.json": REGISTER_LINK,
    "Makefile": "research-standards-source-anchor-audit",
    "tools/README.md": SCRIPT_LINK,
    "tools/AGENTS.md": SCRIPT_LINK,
    "web/README.md": VALIDATION_LINK,
    "web/AGENTS.md": VALIDATION_LINK,
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def load_json(path: Path, errors: list[str], context: str) -> dict[str, Any]:
    if not path.exists():
        fail(errors, f"missing {context}: {path.relative_to(ROOT)}")
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(errors, f"invalid {context} JSON: {exc}")
        return {}
    if not isinstance(data, dict):
        fail(errors, f"{context} must be a JSON object")
        return {}
    return data


def require_string(value: Any, context: str, errors: list[str]) -> str:
    if not isinstance(value, str) or not value.strip():
        fail(errors, f"{context} must be a non-empty string")
        return ""
    return value


def require_string_list(value: Any, context: str, errors: list[str], min_len: int = 1) -> list[str]:
    if not isinstance(value, list) or len(value) < min_len:
        fail(errors, f"{context} must be a list with at least {min_len} item(s)")
        return []
    result: list[str] = []
    for index, item in enumerate(value):
        if not isinstance(item, str) or not item.strip():
            fail(errors, f"{context}[{index}] must be a non-empty string")
            continue
        result.append(item)
    return result


def validate_local_path(relative_path: str, context: str, errors: list[str]) -> None:
    value = require_string(relative_path, context, errors)
    if not value:
        return
    if value.startswith(("http://", "https://")):
        fail(errors, f"{context} must be a local repository path, not URL")
        return
    target = (ROOT / value).resolve()
    try:
        target.relative_to(ROOT)
    except ValueError:
        fail(errors, f"{context} escapes repository: {value}")
        return
    if not target.exists():
        fail(errors, f"{context} does not exist: {value}")


def validate_source_of_truth(register: dict[str, Any], errors: list[str]) -> None:
    source = register.get("sourceOfTruth")
    if not isinstance(source, dict):
        fail(errors, "sourceOfTruth must be an object")
        return
    if set(source) != REQUIRED_SOURCE_KEYS:
        fail(errors, "sourceOfTruth must contain exactly the required keys")
    for key, value in source.items():
        validate_local_path(value, f"sourceOfTruth.{key}", errors)


def validate_anchor_policy(register: dict[str, Any], errors: list[str]) -> None:
    policy = register.get("anchorPolicy")
    if not isinstance(policy, dict):
        fail(errors, "anchorPolicy must be an object")
        return
    required = set(require_string_list(policy.get("neverEvidenceFor"), "anchorPolicy.neverEvidenceFor", errors, 5))
    missing = REQUIRED_NEVER_EVIDENCE - required
    if missing:
        fail(errors, f"anchorPolicy.neverEvidenceFor missing {sorted(missing)}")
    required_before = set(require_string_list(policy.get("requiredBeforeUse"), "anchorPolicy.requiredBeforeUse", errors, 4))
    for phrase in ["bias or applicability assessment", "calibration or validation report admission"]:
        if phrase not in required_before:
            fail(errors, f"anchorPolicy.requiredBeforeUse must include {phrase!r}")


def validate_standard_anchors(register: dict[str, Any], errors: list[str]) -> tuple[int, list[str]]:
    anchors = register.get("standardAnchors")
    if not isinstance(anchors, list) or len(anchors) != len(REQUIRED_ANCHOR_IDS):
        fail(errors, f"standardAnchors must contain {len(REQUIRED_ANCHOR_IDS)} anchors")
        return 0, []

    ids: set[str] = set()
    families: set[str] = set()
    urls: set[str] = set()
    for index, anchor in enumerate(anchors):
        if not isinstance(anchor, dict):
            fail(errors, f"standardAnchors[{index}] must be an object")
            continue
        anchor_id = require_string(anchor.get("anchorId"), f"standardAnchors[{index}].anchorId", errors)
        if anchor_id in ids:
            fail(errors, f"duplicate anchorId: {anchor_id}")
        ids.add(anchor_id)
        family = require_string(anchor.get("standardFamily"), f"{anchor_id}.standardFamily", errors)
        families.add(family)
        for key in ["title", "sourceType", "sourceStatus", "primaryUse", "humanInfraPlacement"]:
            require_string(anchor.get(key), f"{anchor_id}.{key}", errors)
        url = require_string(anchor.get("sourceUrl"), f"{anchor_id}.sourceUrl", errors)
        if not url.startswith("https://"):
            fail(errors, f"{anchor_id}.sourceUrl must be https")
        if url in urls:
            fail(errors, f"duplicate sourceUrl: {url}")
        urls.add(url)
        required_before = require_string_list(anchor.get("requiredBefore"), f"{anchor_id}.requiredBefore", errors, 2)
        not_evidence = set(require_string_list(anchor.get("notEvidenceFor"), f"{anchor_id}.notEvidenceFor", errors, 5))
        if len(required_before) < 2:
            fail(errors, f"{anchor_id}.requiredBefore must describe at least two gate uses")
        missing_never = REQUIRED_NEVER_EVIDENCE - not_evidence
        if missing_never:
            fail(errors, f"{anchor_id}.notEvidenceFor missing {sorted(missing_never)}")
    if ids != REQUIRED_ANCHOR_IDS:
        fail(errors, f"standardAnchors ids mismatch: missing={sorted(REQUIRED_ANCHOR_IDS - ids)} extra={sorted(ids - REQUIRED_ANCHOR_IDS)}")
    if families != REQUIRED_STANDARD_FAMILIES:
        fail(
            errors,
            f"standardFamilies mismatch: missing={sorted(REQUIRED_STANDARD_FAMILIES - families)} extra={sorted(families - REQUIRED_STANDARD_FAMILIES)}",
        )
    return len(anchors), sorted(families)


def validate_decisions(register: dict[str, Any], errors: list[str]) -> None:
    decisions = register.get("currentDecisions")
    if not isinstance(decisions, dict):
        fail(errors, "currentDecisions must be an object")
        return
    if set(decisions) != REQUIRED_FALSE_DECISION_KEYS:
        fail(errors, "currentDecisions must contain exactly the required keys")
    for key, value in decisions.items():
        if value is not False:
            fail(errors, f"currentDecisions.{key} must be false")


def validate_consumption_contract(register: dict[str, Any], errors: list[str]) -> None:
    contract = register.get("consumptionContract")
    if not isinstance(contract, dict):
        fail(errors, "consumptionContract must be an object")
        return
    allowed = set(require_string_list(contract.get("allowedUses"), "consumptionContract.allowedUses", errors, 4))
    blocked = set(require_string_list(contract.get("blockedUses"), "consumptionContract.blockedUses", errors, 4))
    if "bias/applicability gate selection" not in allowed:
        fail(errors, "consumptionContract.allowedUses must include bias/applicability gate selection")
    for phrase in ["individual death dates", "longevity escape velocity"]:
        if not any(phrase in item for item in blocked):
            fail(errors, f"consumptionContract.blockedUses must mention {phrase}")


def validate_index_links(register: dict[str, Any], errors: list[str]) -> None:
    links = set(require_string_list(register.get("indexLinks"), "indexLinks", errors, len(REQUIRED_INDEX_LINKS)))
    missing_links = set(REQUIRED_INDEX_LINKS) - links
    if missing_links:
        fail(errors, f"indexLinks missing {sorted(missing_links)}")
    for relative_path, phrase in REQUIRED_INDEX_LINKS.items():
        path = ROOT / relative_path
        if not path.exists():
            fail(errors, f"missing index path: {relative_path}")
            continue
        text = path.read_text(encoding="utf-8")
        if phrase not in text:
            fail(errors, f"{relative_path} must mention {phrase}")


def validate_register(register: dict[str, Any], errors: list[str]) -> tuple[int, list[str]]:
    if register.get("schemaVersion") != SCHEMA:
        fail(errors, f"schemaVersion must be {SCHEMA}")
    if register.get("status") != STATUS:
        fail(errors, f"status must be {STATUS}")
    require_string(register.get("registerId"), "registerId", errors)
    require_string(register.get("purpose"), "purpose", errors)
    require_string(register.get("currentAssessmentDate"), "currentAssessmentDate", errors)
    validate_source_of_truth(register, errors)
    validate_anchor_policy(register, errors)
    anchor_count, families = validate_standard_anchors(register, errors)
    validate_decisions(register, errors)
    validate_consumption_contract(register, errors)
    validate_index_links(register, errors)
    return anchor_count, families


def write_validation(output_path: Path, anchor_count: int, families: list[str]) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    validation = {
        "schemaVersion": VALIDATION_SCHEMA,
        "status": "pass-no-model-admission",
        "generatedAt": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "sourceRegister": "docs/reference/human-infra-research-standards-source-anchor-register.json",
        "anchorCount": anchor_count,
        "standardFamilies": families,
        "modelAdmission": "blocked",
        "publicWeightedDomainOutput": "blocked",
        "individualPrediction": "blocked",
        "medicalAdvice": "blocked",
        "longevityEscapeVelocityClaim": "blocked"
    }
    output_path.write_text(json.dumps(validation, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json-out", default=str(DEFAULT_JSON_OUT), help="Path for generated validation JSON.")
    args = parser.parse_args()

    errors: list[str] = []
    register = load_json(REGISTER_PATH, errors, "research standards source anchor register")
    anchor_count = 0
    families: list[str] = []
    if register:
        anchor_count, families = validate_register(register, errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    output_path = (ROOT / args.json_out).resolve() if not Path(args.json_out).is_absolute() else Path(args.json_out)
    try:
        output_path.relative_to(ROOT)
    except ValueError:
        print(f"ERROR: json-out escapes repository: {output_path}", file=sys.stderr)
        return 1
    write_validation(output_path, anchor_count, families)
    print(
        "research standards source anchor audit ok: "
        f"anchors={anchor_count} categories={len(families)} model_admission=blocked"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
