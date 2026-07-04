#!/usr/bin/env python3
"""审计 C2-LT-B8 source-resolution 账本。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = ROOT / "docs/reference/human-infra-c2-longtail-eighth-batch-source-resolution-register.json"
QUEUE_PATH = ROOT / "docs/reference/human-infra-c2-longtail-eighth-batch-source-extraction-queue.json"
EXTRACTION_PATH = ROOT / "docs/reference/human-infra-c2-longtail-eighth-batch-source-extraction-register.json"
LOCAL_REVIEW_PATH = ROOT / "docs/reference/human-infra-c2-longtail-eighth-batch-local-review-register.json"

SCHEMA = "human-infra.c2-longtail-eighth-batch-source-resolution-register.v1"
STATUS = "active-c2ltb8-source-resolution-register-independent-fresh-review-required"
REGISTER_LINK = "human-infra-c2-longtail-eighth-batch-source-resolution-register.json"
SCRIPT_LINK = "audit_human_infra_c2_longtail_eighth_batch_source_resolution_register.py"

EXPECTED_TASK_IDS = [
    "C2LTB8-EXT-006",
    "C2LTB8-EXT-008",
    "C2LTB8-EXT-011",
    "C2LTB8-EXT-014",
    "C2LTB8-EXT-021",
    "C2LTB8-EXT-022",
    "C2LTB8-EXT-024",
]
PUBMED_FULLTEXT_ROUTE_TASK_IDS = {
    "C2LTB8-EXT-006",
    "C2LTB8-EXT-008",
    "C2LTB8-EXT-021",
    "C2LTB8-EXT-022",
}
SOURCE_ID_MISMATCH_TASK_IDS = {
    "C2LTB8-EXT-011",
    "C2LTB8-EXT-014",
    "C2LTB8-EXT-024",
}
LIVING_NEURAL_COMPUTATION_TASK_IDS = {"C2LTB8-EXT-011"}
EXPECTED_CANDIDATE_COUNT = 19
EXPECTED_VERIFICATION_IDS = {
    "C2LTB8-SR-VERIFY-AAP-ADHD-GUIDELINE-20260703",
    "C2LTB8-SR-VERIFY-AAP-AUTISM-CLINICAL-REPORT-20260703",
    "C2LTB8-SR-VERIFY-LIVING-NEURAL-COMPUTATION-CORRECTED-PMID-20260703",
    "C2LTB8-SR-VERIFY-LONG-COVID-AUTONOMIC-CORRECTED-PMID-20260703",
    "C2LTB8-SR-VERIFY-VESTIBULAR-REHAB-GUIDELINE-20260703",
    "C2LTB8-SR-VERIFY-BPPV-GUIDELINE-20260703",
    "C2LTB8-SR-VERIFY-STROKE-DYSPHAGIA-CORRECTED-PMID-20260703",
}
SOURCE_OF_TRUTH_KEYS = {
    "sourceExtractionQueue",
    "sourceExtractionRegister",
    "localReviewRegister",
    "evidencePolicy",
    "maturityGapRegister",
}
REQUIRED_BLOCKED_USES = {
    "calibrated-prediction",
    "individual-advice",
    "individual-death-date-output",
    "intervention-ranking",
    "clinical-validity-claim",
    "domain-claim-upgrade",
}
REQUIRED_ROW_FIELDS = {
    "resolutionId",
    "taskId",
    "domainId",
    "localDomainPath",
    "sourceRefId",
    "originalRegisteredTitle",
    "originalRegisteredUrl",
    "localReviewIssueType",
    "currentSourceCheck",
    "sourceResolutionDecision",
    "sourceResolutionStatus",
    "sourceResolutionCandidates",
    "requiredFreshReviewActions",
    "artifactPromotionDecision",
    "modelAdmissionDecision",
    "blockedUses",
}
REQUIRED_CANDIDATE_FIELDS = {
    "candidateId",
    "candidateRole",
    "title",
    "url",
    "sourceType",
    "sourceIdentityStatus",
    "verificationEvidence",
    "resolutionFinding",
    "useBoundary",
}
REQUIRED_INDEX_FILES = [
    "README.md",
    "docs/AGENTS.md",
    "docs/reference/README.md",
    "docs/reference/human-infra-maturity-roadmap.md",
    "tools/README.md",
    "tools/AGENTS.md",
]


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def load_json(path: Path, errors: list[str], context: str) -> dict[str, Any]:
    if not path.exists():
        fail(errors, f"missing {context}: {path.relative_to(ROOT)}")
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(errors, f"invalid JSON in {context}: {exc}")
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


def require_int(value: Any, context: str, errors: list[str]) -> int | None:
    if not isinstance(value, int):
        fail(errors, f"{context} must be an integer")
        return None
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


def repo_path(relative_path: str, context: str, errors: list[str]) -> Path | None:
    value = require_string(relative_path, context, errors)
    if not value:
        return None
    if value.startswith(("http://", "https://")):
        fail(errors, f"{context} must be a local path, not URL")
        return None
    target = (ROOT / value).resolve()
    try:
        target.relative_to(ROOT)
    except ValueError:
        fail(errors, f"{context} escapes repository: {value}")
        return None
    if not target.exists():
        fail(errors, f"{context} does not exist: {value}")
        return None
    return target


def task_rows(path: Path, key: str, errors: list[str], context: str) -> dict[str, dict[str, Any]]:
    data = load_json(path, errors, context)
    rows = data.get(key) if data else None
    if not isinstance(rows, list):
        fail(errors, f"{context}.{key} must be a list")
        return {}
    result: dict[str, dict[str, Any]] = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"{context}.{key}[{index}] must be an object")
            continue
        task_id = require_string(row.get("taskId"), f"{context}.{key}[{index}].taskId", errors)
        if task_id:
            result[task_id] = row
    return result


def validate_source_of_truth(data: dict[str, Any], errors: list[str]) -> None:
    source = data.get("sourceOfTruth")
    if not isinstance(source, dict):
        fail(errors, "sourceOfTruth must be an object")
        return
    if set(source) != SOURCE_OF_TRUTH_KEYS:
        fail(errors, "sourceOfTruth must contain exactly the required keys")
    for key in SOURCE_OF_TRUTH_KEYS:
        if key in source:
            repo_path(source[key], f"sourceOfTruth.{key}", errors)


def validate_scope(data: dict[str, Any], rows: list[dict[str, Any]], errors: list[str]) -> None:
    scope = data.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return
    expected = {
        "totalLocalReviewRowCount": 24,
        "issueRowCount": len(EXPECTED_TASK_IDS),
        "pubmedFulltextRouteIssueCount": len(PUBMED_FULLTEXT_ROUTE_TASK_IDS),
        "sourceIdMismatchIssueCount": len(SOURCE_ID_MISMATCH_TASK_IDS),
        "livingNeuralComputationOverclaimIssueCount": len(LIVING_NEURAL_COMPUTATION_TASK_IDS),
        "resolutionCandidateCount": EXPECTED_CANDIDATE_COUNT,
    }
    if scope.get("batchId") != "C2-LT-B8":
        fail(errors, "scope.batchId must be C2-LT-B8")
    if scope.get("resolutionLevel") != "c2ltb8-local-review-issue-row-source-resolution-v0.1":
        fail(errors, "scope.resolutionLevel is invalid")
    for key, expected_value in expected.items():
        actual = require_int(scope.get(key), f"scope.{key}", errors)
        if actual is not None and actual != expected_value:
            fail(errors, f"scope.{key} must equal {expected_value}")
    candidate_count = sum(len(row.get("sourceResolutionCandidates", [])) for row in rows)
    if candidate_count != EXPECTED_CANDIDATE_COUNT:
        fail(errors, f"resolution candidate count must equal {EXPECTED_CANDIDATE_COUNT}")
    non_claims = require_string_list(scope.get("nonClaims"), "scope.nonClaims", errors, 4)
    for phrase in ["does not change", "does not create reviewed artifacts", "does not authorize"]:
        if not any(phrase in item for item in non_claims):
            fail(errors, f"scope.nonClaims must include phrase: {phrase}")


def validate_verification_sources(data: dict[str, Any], errors: list[str]) -> set[str]:
    sources = data.get("verificationSources")
    if not isinstance(sources, list):
        fail(errors, "verificationSources must be a list")
        return set()
    seen: set[str] = set()
    for index, source in enumerate(sources):
        if not isinstance(source, dict):
            fail(errors, f"verificationSources[{index}] must be an object")
            continue
        verification_id = require_string(source.get("verificationId"), f"verificationSources[{index}].verificationId", errors)
        if verification_id:
            seen.add(verification_id)
        for field in ["title", "url", "sourceType", "useBoundary"]:
            require_string(source.get(field), f"verificationSources[{index}].{field}", errors)
        url = source.get("url")
        if isinstance(url, str) and not url.startswith("https://"):
            fail(errors, f"verificationSources[{index}].url must be https")
    if seen != EXPECTED_VERIFICATION_IDS:
        fail(errors, "verificationSources must match expected verification IDs")
    return seen


def validate_current_source_check(row: dict[str, Any], index: int, verification_ids: set[str], errors: list[str]) -> None:
    check = row.get("currentSourceCheck")
    if not isinstance(check, dict):
        fail(errors, f"resolutionRows[{index}].currentSourceCheck must be an object")
        return
    for field in ["observedTitle", "verificationEvidence", "result"]:
        require_string(check.get(field), f"resolutionRows[{index}].currentSourceCheck.{field}", errors)
    evidence = check.get("verificationEvidence")
    if isinstance(evidence, str) and evidence not in verification_ids:
        fail(errors, f"resolutionRows[{index}].currentSourceCheck.verificationEvidence unknown: {evidence}")


def validate_candidates(row: dict[str, Any], index: int, verification_ids: set[str], errors: list[str]) -> None:
    candidates = row.get("sourceResolutionCandidates")
    if not isinstance(candidates, list) or not candidates:
        fail(errors, f"resolutionRows[{index}].sourceResolutionCandidates must be non-empty list")
        return
    for cand_index, candidate in enumerate(candidates):
        if not isinstance(candidate, dict):
            fail(errors, f"resolutionRows[{index}].sourceResolutionCandidates[{cand_index}] must be an object")
            continue
        missing = REQUIRED_CANDIDATE_FIELDS - set(candidate)
        if missing:
            fail(
                errors,
                f"resolutionRows[{index}].sourceResolutionCandidates[{cand_index}] missing fields: {sorted(missing)}",
            )
        for field in REQUIRED_CANDIDATE_FIELDS:
            if field in candidate:
                require_string(candidate.get(field), f"resolutionRows[{index}].sourceResolutionCandidates[{cand_index}].{field}", errors)
        url = candidate.get("url")
        if isinstance(url, str) and not url.startswith("https://"):
            fail(errors, f"resolutionRows[{index}].sourceResolutionCandidates[{cand_index}].url must be https")
        evidence = candidate.get("verificationEvidence")
        if isinstance(evidence, str) and evidence not in verification_ids:
            fail(errors, f"resolutionRows[{index}].sourceResolutionCandidates[{cand_index}].verificationEvidence unknown: {evidence}")
        boundary = candidate.get("useBoundary")
        if isinstance(boundary, str) and not any(
            phrase in boundary for phrase in ["no artifact fill", "no individual", "Use only", "manual/fulltext"]
        ):
            fail(errors, f"resolutionRows[{index}].sourceResolutionCandidates[{cand_index}].useBoundary must preserve blocked-use boundary")


def validate_resolution_rows(data: dict[str, Any], verification_ids: set[str], errors: list[str]) -> None:
    rows = data.get("resolutionRows")
    if not isinstance(rows, list):
        fail(errors, "resolutionRows must be a list")
        return
    if [row.get("taskId") for row in rows if isinstance(row, dict)] != EXPECTED_TASK_IDS:
        fail(errors, "resolutionRows task order must match expected C2-LT-B8 issue rows")

    extraction_rows = task_rows(EXTRACTION_PATH, "extractedRows", errors, "sourceExtractionRegister")
    local_findings = task_rows(LOCAL_REVIEW_PATH, "sourceResolutionFindings", errors, "localReviewRegister")

    seen_resolution_ids: set[str] = set()
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"resolutionRows[{index}] must be an object")
            continue
        missing = REQUIRED_ROW_FIELDS - set(row)
        if missing:
            fail(errors, f"resolutionRows[{index}] missing fields: {sorted(missing)}")
        task_id = require_string(row.get("taskId"), f"resolutionRows[{index}].taskId", errors)
        if task_id and task_id not in EXPECTED_TASK_IDS:
            fail(errors, f"unexpected taskId in resolutionRows[{index}]: {task_id}")
        resolution_id = require_string(row.get("resolutionId"), f"resolutionRows[{index}].resolutionId", errors)
        if resolution_id in seen_resolution_ids:
            fail(errors, f"duplicate resolutionId: {resolution_id}")
        seen_resolution_ids.add(resolution_id)
        if task_id in extraction_rows:
            for field, row_field in [
                ("domainId", "domainId"),
                ("localDomainPath", "localDomainPath"),
                ("sourceRefId", "sourceRefId"),
                ("sourceTitle", "originalRegisteredTitle"),
                ("sourceUrl", "originalRegisteredUrl"),
            ]:
                if row.get(row_field) != extraction_rows[task_id].get(field):
                    fail(errors, f"{task_id}.{row_field} must match extraction register {field}")
        if task_id in local_findings and row.get("localReviewIssueType") != local_findings[task_id].get("issueType"):
            fail(errors, f"{task_id}.localReviewIssueType must match local review finding")
        for field in [
            "domainId",
            "localDomainPath",
            "sourceRefId",
            "originalRegisteredTitle",
            "originalRegisteredUrl",
            "localReviewIssueType",
            "sourceResolutionDecision",
            "sourceResolutionStatus",
            "artifactPromotionDecision",
            "modelAdmissionDecision",
        ]:
            require_string(row.get(field), f"resolutionRows[{index}].{field}", errors)
        if row.get("sourceResolutionStatus") != "candidate-resolution-prepared-not-fresh-reviewed":
            fail(errors, f"{task_id}.sourceResolutionStatus must remain candidate-resolution-prepared-not-fresh-reviewed")
        if "blocked" not in str(row.get("artifactPromotionDecision")):
            fail(errors, f"{task_id}.artifactPromotionDecision must stay blocked")
        if "blocked" not in str(row.get("modelAdmissionDecision")):
            fail(errors, f"{task_id}.modelAdmissionDecision must stay blocked")
        if set(row.get("blockedUses", [])) != REQUIRED_BLOCKED_USES:
            fail(errors, f"{task_id}.blockedUses must match required blocked uses")
        actions = require_string_list(row.get("requiredFreshReviewActions"), f"resolutionRows[{index}].requiredFreshReviewActions", errors, 4)
        action_text = " ".join(actions)
        for phrase in ["independent fresh review", "model admission", "blocked"]:
            if phrase not in action_text:
                fail(errors, f"{task_id}.requiredFreshReviewActions must mention {phrase}")
        if task_id in SOURCE_ID_MISMATCH_TASK_IDS:
            text_blob = " ".join(str(row.get(field, "")) for field in ["currentSourceCheck", "sourceResolutionDecision"])
            if "source-ID mismatch" not in text_blob and "source-id-mismatch" not in text_blob:
                fail(errors, f"{task_id} must explicitly preserve source-ID mismatch context")
            if "original" not in text_blob or "corrected" not in text_blob:
                fail(errors, f"{task_id} must mention original and corrected PMID context")
        if task_id in LIVING_NEURAL_COMPUTATION_TASK_IDS:
            text_blob = " ".join(str(row.get(field, "")) for field in ["currentSourceCheck", "sourceResolutionDecision", "requiredFreshReviewActions"])
            for phrase in ["network", "sentience", "human-surpassing"]:
                if phrase not in text_blob:
                    fail(errors, f"{task_id} must preserve living neural computation overclaim blocker: {phrase}")
        validate_current_source_check(row, index, verification_ids, errors)
        validate_candidates(row, index, verification_ids, errors)


def validate_global_decisions(data: dict[str, Any], errors: list[str]) -> None:
    if set(data.get("blockedUses", [])) != REQUIRED_BLOCKED_USES:
        fail(errors, "blockedUses must match required blocked uses")
    required_next = require_string_list(data.get("requiredNextArtifacts"), "requiredNextArtifacts", errors, 4)
    joined = " ".join(required_next)
    for phrase in ["manual", "fresh-review", "model-admission"]:
        if phrase not in joined:
            fail(errors, f"requiredNextArtifacts must mention {phrase}")
    model_decision = require_string(data.get("modelAdmissionDecision"), "modelAdmissionDecision", errors)
    if "blocked" not in model_decision:
        fail(errors, "modelAdmissionDecision must remain blocked")


def validate_index_links(errors: list[str]) -> None:
    for relative_path in REQUIRED_INDEX_FILES:
        path = ROOT / relative_path
        if not path.exists():
            fail(errors, f"missing index file: {relative_path}")
            continue
        text = path.read_text(encoding="utf-8")
        if REGISTER_LINK not in text:
            fail(errors, f"index does not link source-resolution register: {relative_path}")
        if relative_path.startswith("tools/") and SCRIPT_LINK not in text:
            fail(errors, f"tools index does not link audit script: {relative_path}")


def validate_auxiliary_sources(errors: list[str]) -> None:
    task_rows(QUEUE_PATH, "extractionTasks", errors, "sourceExtractionQueue")
    task_rows(EXTRACTION_PATH, "extractedRows", errors, "sourceExtractionRegister")
    task_rows(LOCAL_REVIEW_PATH, "sourceResolutionFindings", errors, "localReviewRegister")


def main() -> int:
    errors: list[str] = []
    data = load_json(REGISTER_PATH, errors, "source-resolution register")
    validate_auxiliary_sources(errors)
    if data:
        if data.get("schemaVersion") != SCHEMA:
            fail(errors, f"schemaVersion must be {SCHEMA}")
        if data.get("status") != STATUS:
            fail(errors, f"status must be {STATUS}")
        require_string(data.get("registerId"), "registerId", errors)
        require_string(data.get("purpose"), "purpose", errors)
        validate_source_of_truth(data, errors)
        rows = data.get("resolutionRows") if isinstance(data.get("resolutionRows"), list) else []
        validate_scope(data, rows, errors)
        verification_ids = validate_verification_sources(data, errors)
        validate_resolution_rows(data, verification_ids, errors)
        validate_global_decisions(data, errors)
    validate_index_links(errors)

    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1

    rows = data["resolutionRows"]
    candidate_count = sum(len(row["sourceResolutionCandidates"]) for row in rows)
    print(
        "C2-LT-B8 source-resolution register audit ok: "
        f"rows={len(rows)} candidates={candidate_count} model=blocked"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
