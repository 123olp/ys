#!/usr/bin/env python3
"""审计 Human Infra reviewed card artifact register 的实体化覆盖与阻塞边界。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = ROOT / "docs/reference/human-infra-reviewed-card-artifact-register.json"
PREP_PATH = ROOT / "docs/reference/human-infra-card-promotion-prep-register.json"
VERDICT_PATH = ROOT / "docs/reference/human-infra-independent-fresh-review-verdict-register.json"

SCHEMA = "human-infra.reviewed-card-artifact-register.v1"
STATUS = "active-reviewed-card-artifact-register-model-blocked"
REGISTER_LINK = "human-infra-reviewed-card-artifact-register.json"

SOURCE_OF_TRUTH_KEYS = {
    "cardPromotionPrepRegister",
    "independentFreshReviewVerdictRegister",
    "sourceCardSystem",
    "evidencePolicy",
    "maturityGapRegister",
}

ARTIFACT_TYPES = {
    "reviewed-source-card": "reviewedSourceCardId",
    "variable-card": "variableCardId",
    "endpoint-card": "endpointCardId",
    "uncertainty-card": "uncertaintyCardId",
    "transfer-boundary-card": "transferBoundaryCardId",
    "downgrade-check": "downgradeCheckId",
}

REQUIRED_ARTIFACT_FIELDS = [
    "artifactId",
    "artifactType",
    "artifactStatus",
    "promotionTaskId",
    "domainId",
    "domainClaimId",
    "fieldCardId",
    "sourceCardId",
    "sourceRole",
    "reviewerVerdict",
    "artifactPromotionDecision",
    "modelAdmissionDecision",
    "blockedUses",
    "freshReviewEvidenceUrls",
    "registeredExactClaimUses",
    "registeredTransferBoundaries",
    "content",
]

TYPE_CONTENT_FIELDS = {
    "reviewed-source-card": {
        "sourceIdentity",
        "sourceRole",
        "exactClaimUse",
        "transferBoundary",
        "freshReviewEvidence",
        "reviewerNote",
    },
    "variable-card": {
        "variableQuestion",
        "sourceRole",
        "exactClaimUse",
        "modelPosition",
        "promotionBoundary",
    },
    "endpoint-card": {
        "endpointQuestion",
        "endpointBoundary",
        "modelPosition",
        "blockedEndpointUses",
    },
    "uncertainty-card": {
        "uncertaintyQuestion",
        "uncertaintyBoundary",
        "evidenceLimit",
        "blockedUncertaintyUses",
    },
    "transfer-boundary-card": {
        "transferBoundaryQuestion",
        "domainTransferVerdict",
        "registeredTransferBoundaries",
        "blockedTransferUses",
    },
    "downgrade-check": {
        "downgradeQuestion",
        "downgradeVerdict",
        "reviewerVerdict",
        "downgradeRequiredWhen",
    },
}

REQUIRED_INDEX_FILES = [
    "docs/reference/README.md",
    "docs/reference/human-infra-maturity-roadmap.md",
    "tools/README.md",
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
    if not isinstance(relative_path, str) or not relative_path.strip():
        fail(errors, f"{context} must be a non-empty local path")
        return None
    if relative_path.startswith(("http://", "https://")):
        fail(errors, f"{context} must be a local path, not URL")
        return None
    target = (ROOT / relative_path).resolve()
    try:
        target.relative_to(ROOT)
    except ValueError:
        fail(errors, f"{context} escapes repository: {relative_path}")
        return None
    if not target.exists():
        fail(errors, f"{context} does not exist: {relative_path}")
        return None
    return target


def validate_source_of_truth(register: dict[str, Any], errors: list[str]) -> None:
    source = register.get("sourceOfTruth")
    if not isinstance(source, dict):
        fail(errors, "sourceOfTruth must be an object")
        return
    if set(source) != SOURCE_OF_TRUTH_KEYS:
        fail(errors, "sourceOfTruth must contain exactly the required keys")
    for key in SOURCE_OF_TRUTH_KEYS:
        value = require_string(source.get(key), f"sourceOfTruth.{key}", errors)
        if value:
            repo_path(value, f"sourceOfTruth.{key}", errors)


def validate_scope(
    register: dict[str, Any],
    prep: dict[str, Any],
    verdict: dict[str, Any],
    artifacts: list[dict[str, Any]],
    errors: list[str],
) -> None:
    scope = register.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return
    if scope.get("artifactLevel") != "fresh-review-verdict-to-reviewed-card-artifact":
        fail(errors, "scope.artifactLevel must be fresh-review-verdict-to-reviewed-card-artifact")

    prep_scope = prep.get("scope", {}) if isinstance(prep.get("scope"), dict) else {}
    verdict_scope = verdict.get("scope", {}) if isinstance(verdict.get("scope"), dict) else {}
    promotion_tasks = int(prep_scope.get("artifactPackCount", 0))
    artifact_count = promotion_tasks * len(ARTIFACT_TYPES)
    source_count = int(verdict_scope.get("reviewedSourceAnchorCount", 0))
    domain_count = int(verdict_scope.get("coveredDomainCount", 0))

    expected = {
        "promotionTaskCount": promotion_tasks,
        "sourceAnchorCount": source_count,
        "coveredDomainCount": domain_count,
        "artifactTypeCount": len(ARTIFACT_TYPES),
        "reviewedArtifactCount": artifact_count,
    }
    for key, value in expected.items():
        actual = require_int(scope.get(key), f"scope.{key}", errors)
        if actual is not None and actual != value:
            fail(errors, f"scope.{key} must equal {value}")

    artifact_types = set(require_string_list(scope.get("artifactTypes"), "scope.artifactTypes", errors, len(ARTIFACT_TYPES)))
    if artifact_types != set(ARTIFACT_TYPES):
        fail(errors, "scope.artifactTypes must contain every artifact type")
    if len(artifacts) != artifact_count:
        fail(errors, f"reviewedArtifacts must contain {artifact_count} artifacts")
    for field in ["selectionRule", "artifactStatusRule", "modelAdmissionRule"]:
        require_string(scope.get(field), f"scope.{field}", errors)
    non_claims = require_string_list(scope.get("nonClaims"), "scope.nonClaims", errors, 4)
    joined = " ".join(non_claims)
    for phrase in [
        "not model-ready",
        "does not authorize calibrated prediction",
        "does not replace Markdown Source Cards",
        "model gates remain blocked",
    ]:
        if phrase not in joined:
            fail(errors, f"scope.nonClaims must mention {phrase!r}")


def prep_lookup(prep: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        packet["promotionTaskId"]: packet
        for packet in prep.get("promotionPackets", [])
        if isinstance(packet, dict) and isinstance(packet.get("promotionTaskId"), str)
    }


def verdict_packet_lookup(verdict: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        row["promotionTaskId"]: row
        for row in verdict.get("packetCoverage", [])
        if isinstance(row, dict) and isinstance(row.get("promotionTaskId"), str)
    }


def verdict_source_lookup(verdict: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        row["sourceCardId"]: row
        for row in verdict.get("sourceAnchorFreshReviews", [])
        if isinstance(row, dict) and isinstance(row.get("sourceCardId"), str)
    }


def validate_artifact(
    artifact: Any,
    index: int,
    prep_by_task: dict[str, dict[str, Any]],
    verdict_by_task: dict[str, dict[str, Any]],
    source_reviews: dict[str, dict[str, Any]],
    seen_artifact_ids: set[str],
    seen_pairs: set[tuple[str, str]],
    errors: list[str],
) -> None:
    if not isinstance(artifact, dict):
        fail(errors, f"reviewedArtifacts[{index}] must be an object")
        return
    for field in REQUIRED_ARTIFACT_FIELDS:
        if field not in artifact:
            fail(errors, f"reviewedArtifacts[{index}] missing {field}")

    artifact_id = require_string(artifact.get("artifactId"), f"reviewedArtifacts[{index}].artifactId", errors)
    artifact_type = require_string(artifact.get("artifactType"), f"{artifact_id}.artifactType", errors)
    task_id = require_string(artifact.get("promotionTaskId"), f"{artifact_id}.promotionTaskId", errors)
    if not artifact_id or not artifact_type or not task_id:
        return
    if artifact_type not in ARTIFACT_TYPES:
        fail(errors, f"{artifact_id}.artifactType is invalid")
        return
    if artifact_id in seen_artifact_ids:
        fail(errors, f"duplicate artifactId: {artifact_id}")
    seen_artifact_ids.add(artifact_id)
    pair = (task_id, artifact_type)
    if pair in seen_pairs:
        fail(errors, f"duplicate artifact type for task: {task_id} {artifact_type}")
    seen_pairs.add(pair)

    prep_packet = prep_by_task.get(task_id)
    verdict_packet = verdict_by_task.get(task_id)
    if not prep_packet:
        fail(errors, f"{artifact_id} lacks prep packet: {task_id}")
        return
    if not verdict_packet:
        fail(errors, f"{artifact_id} lacks fresh-review verdict packet: {task_id}")
        return

    expected_artifact_id = prep_packet.get("artifactIds", {}).get(ARTIFACT_TYPES[artifact_type])
    if artifact_id != expected_artifact_id:
        fail(errors, f"{artifact_id} must match prep artifactIds.{ARTIFACT_TYPES[artifact_type]}")
    for field in ["domainId", "domainClaimId", "fieldCardId", "sourceCardId", "sourceRole"]:
        if artifact.get(field) != prep_packet.get(field):
            fail(errors, f"{artifact_id}.{field} must match prep packet")
    for field in ["reviewerVerdict", "artifactPromotionDecision"]:
        if artifact.get(field) != verdict_packet.get(field):
            fail(errors, f"{artifact_id}.{field} must match verdict packet")
    if "blocked" not in require_string(artifact.get("modelAdmissionDecision"), f"{artifact_id}.modelAdmissionDecision", errors):
        fail(errors, f"{artifact_id}.modelAdmissionDecision must remain blocked")

    source_id = artifact.get("sourceCardId")
    source_review = source_reviews.get(source_id)
    if not source_review:
        fail(errors, f"{artifact_id} lacks source review: {source_id}")
        return
    if set(artifact.get("blockedUses", [])) != set(source_review.get("blockedUses", [])):
        fail(errors, f"{artifact_id}.blockedUses must match source review")
    expected_urls = sorted(
        item.get("url")
        for item in source_review.get("freshReviewEvidence", [])
        if isinstance(item, dict) and isinstance(item.get("url"), str)
    )
    if sorted(artifact.get("freshReviewEvidenceUrls", [])) != expected_urls:
        fail(errors, f"{artifact_id}.freshReviewEvidenceUrls must match source review evidence URLs")
    if sorted(artifact.get("registeredExactClaimUses", [])) != sorted(source_review.get("registeredExactClaimUses", [])):
        fail(errors, f"{artifact_id}.registeredExactClaimUses must match source review")
    if sorted(artifact.get("registeredTransferBoundaries", [])) != sorted(source_review.get("registeredTransferBoundaries", [])):
        fail(errors, f"{artifact_id}.registeredTransferBoundaries must match source review")

    content = artifact.get("content")
    if not isinstance(content, dict):
        fail(errors, f"{artifact_id}.content must be an object")
        return
    expected_content_fields = TYPE_CONTENT_FIELDS[artifact_type]
    if set(content) != expected_content_fields:
        fail(errors, f"{artifact_id}.content must contain exact fields for {artifact_type}")
    for key in expected_content_fields:
        value = content.get(key)
        if isinstance(value, str):
            require_string(value, f"{artifact_id}.content.{key}", errors)
        elif isinstance(value, list):
            if not value:
                fail(errors, f"{artifact_id}.content.{key} must be a non-empty list")
            for item_index, item in enumerate(value):
                if isinstance(item, str):
                    require_string(item, f"{artifact_id}.content.{key}[{item_index}]", errors)
                elif isinstance(item, dict):
                    if not item:
                        fail(errors, f"{artifact_id}.content.{key}[{item_index}] must be a non-empty object")
                    for evidence_field in ["url", "evidenceType", "finding"]:
                        if evidence_field in item:
                            require_string(
                                item.get(evidence_field),
                                f"{artifact_id}.content.{key}[{item_index}].{evidence_field}",
                                errors,
                            )
                else:
                    fail(errors, f"{artifact_id}.content.{key}[{item_index}] must be a string or object")
        elif isinstance(value, dict):
            if not value:
                fail(errors, f"{artifact_id}.content.{key} must be a non-empty object")
        else:
            fail(errors, f"{artifact_id}.content.{key} must be string, list or object")


def validate_artifacts(register: dict[str, Any], prep: dict[str, Any], verdict: dict[str, Any], errors: list[str]) -> tuple[int, int]:
    artifacts = register.get("reviewedArtifacts")
    if not isinstance(artifacts, list) or not artifacts:
        fail(errors, "reviewedArtifacts must be a non-empty list")
        return 0, 0
    prep_by_task = prep_lookup(prep)
    verdict_by_task = verdict_packet_lookup(verdict)
    source_reviews = verdict_source_lookup(verdict)
    seen_artifact_ids: set[str] = set()
    seen_pairs: set[tuple[str, str]] = set()
    for index, artifact in enumerate(artifacts):
        validate_artifact(artifact, index, prep_by_task, verdict_by_task, source_reviews, seen_artifact_ids, seen_pairs, errors)
    expected_pairs = {(task_id, artifact_type) for task_id in prep_by_task for artifact_type in ARTIFACT_TYPES}
    if seen_pairs != expected_pairs:
        fail(errors, "reviewedArtifacts must contain exactly one artifact of each type for every promotion task")
    return len(seen_pairs), len(seen_artifact_ids)


def validate_index_requirements(register: dict[str, Any], errors: list[str]) -> None:
    index_requirements = require_string_list(register.get("indexRequirements"), "indexRequirements", errors, len(REQUIRED_INDEX_FILES))
    if sorted(index_requirements) != sorted(REQUIRED_INDEX_FILES):
        fail(errors, "indexRequirements must list the required index files")
    for relative_path in REQUIRED_INDEX_FILES:
        target = repo_path(relative_path, f"indexRequirements.{relative_path}", errors)
        if target and REGISTER_LINK not in target.read_text(encoding="utf-8"):
            fail(errors, f"{relative_path} must link {REGISTER_LINK}")


def validate_register(register: dict[str, Any], prep: dict[str, Any], verdict: dict[str, Any], errors: list[str]) -> tuple[int, int]:
    if register.get("schemaVersion") != SCHEMA:
        fail(errors, f"schemaVersion must be {SCHEMA}")
    if register.get("status") != STATUS:
        fail(errors, f"status must be {STATUS}")
    require_string(register.get("registerId"), "registerId", errors)
    require_string(register.get("purpose"), "purpose", errors)
    validate_source_of_truth(register, errors)
    artifacts = register.get("reviewedArtifacts")
    validate_scope(register, prep, verdict, artifacts if isinstance(artifacts, list) else [], errors)
    pair_count, artifact_count = validate_artifacts(register, prep, verdict, errors)
    validate_index_requirements(register, errors)
    return pair_count, artifact_count


def main() -> int:
    errors: list[str] = []
    register = load_json(REGISTER_PATH, errors, "reviewed card artifact register")
    prep = load_json(PREP_PATH, errors, "card-promotion prep register")
    verdict = load_json(VERDICT_PATH, errors, "independent fresh review verdict register")
    pair_count = artifact_count = 0
    if register and prep and verdict:
        pair_count, artifact_count = validate_register(register, prep, verdict, errors)

    if errors:
        print("reviewed card artifact register audit failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"reviewed card artifact register audit ok: artifacts={artifact_count} task_type_pairs={pair_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
