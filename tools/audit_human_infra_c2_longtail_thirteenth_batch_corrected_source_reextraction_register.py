#!/usr/bin/env python3
"""审计 C2-LT-B13 corrected source re-extraction 完成寄存器。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = ROOT / "docs/reference/human-infra-c2-longtail-thirteenth-batch-corrected-source-reextraction-register.json"
QUEUE_PATH = ROOT / "docs/reference/human-infra-c2-longtail-thirteenth-batch-corrected-source-reextraction-queue.json"

SCHEMA = "human-infra.c2ltb13-corrected-source-reextraction-register.v1"
STATUS = "active-c2ltb13-corrected-source-reextracted-model-blocked"
BATCH_ID = "C2-LT-B13"
TASK_ID = "C2LTB13-CREXT-001"
ORIGIN_TASK_ID = "C2LTB13-EXT-021"
CANDIDATE_ID = "C2LTB13-SRR-003-CAND-02"
CORRECTED_URL = "https://pubmed.ncbi.nlm.nih.gov/22193141/"
BLOCKED_PRIOR_URL = "https://pubmed.ncbi.nlm.nih.gov/26428404/"
REGISTER_LINK = "human-infra-c2-longtail-thirteenth-batch-corrected-source-reextraction-register.json"
SCRIPT_LINK = "audit_human_infra_c2_longtail_thirteenth_batch_corrected_source_reextraction_register.py"

SOURCE_OF_TRUTH_KEYS = {
    "correctedSourceReextractionQueue",
    "sourceResolutionRegister",
    "sourceExtractionRegister",
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
    "clinical-advice",
    "skin-care-advice",
    "dermatology-care-advice",
    "wound-care-advice",
    "incontinence-care-advice",
    "product-advice",
}
REQUIRED_ROW_FIELDS = {
    "reextractionTaskId",
    "originTaskId",
    "sourceResolutionId",
    "domainId",
    "localDomainPath",
    "candidateId",
    "sourceTitle",
    "sourceUrl",
    "pmid",
    "doi",
    "publicationDate",
    "sourceType",
    "extractionStatus",
    "sourceAccessStatus",
    "sourceIdentityCorrection",
    "currentnessBoundary",
    "exactClaimUse",
    "endpointDefinition",
    "populationOrSetting",
    "effectOrMechanismSignal",
    "uncertaintyOrBias",
    "transferBoundary",
    "downgradeTriggers",
    "modelPosition",
    "artifactPromotionReadiness",
    "modelAdmissionDecision",
    "blockedUses",
    "sourceEvidenceTrace",
    "nextAction",
}
REQUIRED_INDEX_FILES = [
    "docs/AGENTS.md",
    "docs/reference/README.md",
    "docs/reference/human-infra-maturity-roadmap.md",
    "docs/reference/human-infra-maturity-gap-register.json",
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


def queue_task(errors: list[str]) -> dict[str, Any]:
    queue = load_json(QUEUE_PATH, errors, "C2-LT-B13 corrected source re-extraction queue")
    tasks = queue.get("reextractionTasks")
    if not isinstance(tasks, list) or len(tasks) != 1:
        fail(errors, "queue.reextractionTasks must contain exactly one task")
        return {}
    task = tasks[0]
    if not isinstance(task, dict):
        fail(errors, "queue.reextractionTasks[0] must be an object")
        return {}
    if task.get("taskId") != TASK_ID:
        fail(errors, f"queue task must be {TASK_ID}")
    return task


def validate_source_of_truth(register: dict[str, Any], errors: list[str]) -> None:
    source = register.get("sourceOfTruth")
    if not isinstance(source, dict):
        fail(errors, "sourceOfTruth must be an object")
        return
    if set(source) != SOURCE_OF_TRUTH_KEYS:
        fail(errors, "sourceOfTruth must contain exactly the required keys")
    for key in SOURCE_OF_TRUTH_KEYS:
        if key in source:
            repo_path(source[key], f"sourceOfTruth.{key}", errors)


def validate_scope(register: dict[str, Any], errors: list[str]) -> None:
    scope = register.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return
    expected = {
        "queueTaskCount": 1,
        "reextractedRowCount": 1,
        "boundedFreshReviewCandidateCount": 1,
        "routeOrIndexOnlyCount": 0,
        "directArtifactFillCount": 0,
        "modelAdmissionOpenedCount": 0,
    }
    if scope.get("batchId") != BATCH_ID:
        fail(errors, f"scope.batchId must be {BATCH_ID}")
    for key, expected_value in expected.items():
        actual = require_int(scope.get(key), f"scope.{key}", errors)
        if actual is not None and actual != expected_value:
            fail(errors, f"scope.{key} must equal {expected_value}")
    require_string(scope.get("extractionLimit"), "scope.extractionLimit", errors)


def validate_model_position(value: Any, context: str, errors: list[str]) -> None:
    if not isinstance(value, dict):
        fail(errors, f"{context} must be an object")
        return
    require_string(value.get("primaryLocation"), f"{context}.primaryLocation", errors)
    require_string_list(value.get("variables"), f"{context}.variables", errors, min_len=4)
    require_string(value.get("admissibleUse"), f"{context}.admissibleUse", errors)


def validate_evidence_trace(value: Any, context: str, errors: list[str]) -> None:
    if not isinstance(value, list) or len(value) < 3:
        fail(errors, f"{context} must contain PubMed, ESummary and EFetch evidence")
        return
    urls = []
    for index, item in enumerate(value):
        if not isinstance(item, dict):
            fail(errors, f"{context}[{index}] must be an object")
            continue
        url = require_string(item.get("url"), f"{context}[{index}].url", errors)
        urls.append(url)
        if url and not url.startswith("https://"):
            fail(errors, f"{context}[{index}].url must be https")
        require_string(item.get("evidenceType"), f"{context}[{index}].evidenceType", errors)
        require_string(item.get("finding"), f"{context}[{index}].finding", errors)
    joined = "\n".join(urls)
    for required in [CORRECTED_URL, "esummary.fcgi", "efetch.fcgi"]:
        if required not in joined:
            fail(errors, f"{context} must include evidence route: {required}")


def validate_row(register: dict[str, Any], task: dict[str, Any], errors: list[str]) -> None:
    rows = register.get("extractedRows")
    if not isinstance(rows, list) or len(rows) != 1:
        fail(errors, "extractedRows must contain exactly one row")
        return
    row = rows[0]
    if not isinstance(row, dict):
        fail(errors, "extractedRows[0] must be an object")
        return
    missing = REQUIRED_ROW_FIELDS - set(row)
    if missing:
        fail(errors, f"extracted row missing fields: {sorted(missing)}")
    expected = {
        "reextractionTaskId": TASK_ID,
        "originTaskId": ORIGIN_TASK_ID,
        "candidateId": CANDIDATE_ID,
        "sourceUrl": CORRECTED_URL,
        "pmid": "22193141",
        "doi": "10.1097/WON.0b013e31823fe246",
        "extractionStatus": "completed-corrected-source-reextraction-bounded",
        "artifactPromotionReadiness": "eligible-for-independent-fresh-review-before-bounded-artifact-promotion",
        "modelAdmissionDecision": "blocked-pending-corrected-extraction-independent-review-and-artifact-gates",
    }
    for key, value in expected.items():
        if row.get(key) != value:
            fail(errors, f"{TASK_ID}.{key} must be {value}")
    if task:
        for row_key, task_key in {
            "originTaskId": "originTaskId",
            "sourceResolutionId": "sourceResolutionId",
            "domainId": "domainId",
            "localDomainPath": "localDomainPath",
            "candidateId": "candidateId",
            "sourceTitle": "sourceTitle",
            "sourceUrl": "sourceUrl",
        }.items():
            if row.get(row_key) != task.get(task_key):
                fail(errors, f"{TASK_ID}.{row_key} must match queue task")
    repo_path(row.get("localDomainPath", ""), f"{TASK_ID}.localDomainPath", errors)
    for key in REQUIRED_ROW_FIELDS:
        if key in {"downgradeTriggers", "modelPosition", "blockedUses", "sourceEvidenceTrace"}:
            continue
        require_string(row.get(key), f"{TASK_ID}.{key}", errors)
    if set(require_string_list(row.get("blockedUses"), f"{TASK_ID}.blockedUses", errors)) != REQUIRED_BLOCKED_USES:
        fail(errors, f"{TASK_ID}.blockedUses must match required blocked uses")
    if set(require_string_list(register.get("blockedUses"), "blockedUses", errors)) != REQUIRED_BLOCKED_USES:
        fail(errors, "register.blockedUses must match row blocked uses")
    triggers = require_string_list(row.get("downgradeTriggers"), f"{TASK_ID}.downgradeTriggers", errors, min_len=4)
    if not any("Block" in trigger or "block" in trigger for trigger in triggers):
        fail(errors, f"{TASK_ID}.downgradeTriggers must include a blocking condition")
    text = " ".join(
        str(row.get(key, ""))
        for key in [
            "sourceIdentityCorrection",
            "currentnessBoundary",
            "exactClaimUse",
            "uncertaintyOrBias",
            "transferBoundary",
            "nextAction",
        ]
    )
    for phrase in ["26428404", "22193141", "2012", "research remained limited", "Do not reuse"]:
        if phrase not in text:
            fail(errors, f"{TASK_ID} text must preserve phrase: {phrase}")
    validate_model_position(row.get("modelPosition"), f"{TASK_ID}.modelPosition", errors)
    validate_evidence_trace(row.get("sourceEvidenceTrace"), f"{TASK_ID}.sourceEvidenceTrace", errors)


def validate_summary(register: dict[str, Any], errors: list[str]) -> None:
    summary = register.get("summary")
    if not isinstance(summary, dict):
        fail(errors, "summary must be an object")
        return
    if summary.get("reextractedRowCount") != 1:
        fail(errors, "summary.reextractedRowCount must equal 1")
    if summary.get("freshReviewCandidateTaskIds") != [TASK_ID]:
        fail(errors, "summary.freshReviewCandidateTaskIds must contain only C2LTB13-CREXT-001")
    if summary.get("routeOrIndexOnlyTaskIds") != []:
        fail(errors, "summary.routeOrIndexOnlyTaskIds must be empty")
    if summary.get("blockedPriorSourceUrls") != [BLOCKED_PRIOR_URL]:
        fail(errors, "summary.blockedPriorSourceUrls must preserve invalid PMID route")
    if summary.get("correctedSourceUrls") != [CORRECTED_URL]:
        fail(errors, "summary.correctedSourceUrls must preserve corrected PMID route")
    require_string_list(summary.get("remainingWork"), "summary.remainingWork", errors, min_len=4)


def validate_index_links(register: dict[str, Any], errors: list[str]) -> None:
    if register.get("indexRequirements") != REQUIRED_INDEX_FILES:
        fail(errors, "indexRequirements must match required index file list")
    for relative_path in REQUIRED_INDEX_FILES:
        path = ROOT / relative_path
        if not path.exists():
            fail(errors, f"missing index file: {relative_path}")
            continue
        text = path.read_text(encoding="utf-8")
        if REGISTER_LINK not in text:
            fail(errors, f"index file does not reference corrected re-extraction register: {relative_path}")
    for relative_path in ["Makefile", "tools/README.md", "tools/AGENTS.md"]:
        text = (ROOT / relative_path).read_text(encoding="utf-8")
        if SCRIPT_LINK not in text:
            fail(errors, f"{relative_path} does not reference audit script")


def main() -> int:
    errors: list[str] = []
    register = load_json(REGISTER_PATH, errors, "C2-LT-B13 corrected source re-extraction register")
    task = queue_task(errors)
    if register:
        if register.get("schemaVersion") != SCHEMA:
            fail(errors, f"schemaVersion must be {SCHEMA}")
        if register.get("status") != STATUS:
            fail(errors, f"status must be {STATUS}")
        require_string(register.get("registerId"), "registerId", errors)
        require_string(register.get("purpose"), "purpose", errors)
        validate_source_of_truth(register, errors)
        validate_scope(register, errors)
        validate_row(register, task, errors)
        require_string_list(register.get("nonClaims"), "nonClaims", errors, min_len=4)
        validate_summary(register, errors)
        validate_index_links(register, errors)

    if errors:
        print("C2-LT-B13 corrected source re-extraction register audit failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("C2-LT-B13 corrected source re-extraction register audit ok: rows=1 fresh-review-candidates=1 model=blocked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
