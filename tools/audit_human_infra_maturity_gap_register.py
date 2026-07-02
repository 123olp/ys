#!/usr/bin/env python3
"""审计 Human Infra 100% 成熟度缺口账本的本地契约。"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = ROOT / "docs/reference/human-infra-maturity-gap-register.json"
ROADMAP_PATH = ROOT / "docs/reference/human-infra-maturity-roadmap.md"

REQUIRED_AXIS_IDS = {
    "value_clarity": "项目价值",
    "research_framework": "研究框架",
    "quantitative_model": "定量模型",
}

REQUIRED_STATUS = {"pass", "partial", "blocked"}

REQUIRED_BOUNDARY_PHRASES = [
    "Do not mark value clarity complete",
    "Do not mark research framework complete",
    "Do not mark quantitative model complete",
    "Do not output individual death dates",
]

REQUIRED_INDEX_REFERENCES = [
    "README.md",
    "docs/reference/README.md",
    "docs/reference/human-infra-maturity-roadmap.md",
]

REGISTER_LINK = "human-infra-maturity-gap-register.json"


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def load_register(errors: list[str]) -> dict[str, Any]:
    if not REGISTER_PATH.exists():
        fail(errors, f"missing register: {REGISTER_PATH.relative_to(ROOT)}")
        return {}
    try:
        data = json.loads(REGISTER_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(errors, f"invalid JSON: {exc}")
        return {}
    if not isinstance(data, dict):
        fail(errors, "register must be a JSON object")
        return {}
    return data


def roadmap_percentages(errors: list[str]) -> dict[str, int]:
    if not ROADMAP_PATH.exists():
        fail(errors, f"missing roadmap: {ROADMAP_PATH.relative_to(ROOT)}")
        return {}
    text = ROADMAP_PATH.read_text(encoding="utf-8")
    percentages: dict[str, int] = {}
    for axis_name in REQUIRED_AXIS_IDS.values():
        match = re.search(rf"\| {re.escape(axis_name)} \| (\d+)% \|", text)
        if not match:
            fail(errors, f"roadmap missing percentage row: {axis_name}")
            continue
        percentages[axis_name] = int(match.group(1))
    return percentages


def require_string(value: Any, path: str, errors: list[str]) -> str:
    if not isinstance(value, str) or not value.strip():
        fail(errors, f"{path} must be a non-empty string")
        return ""
    return value


def require_bool(value: Any, path: str, errors: list[str]) -> bool | None:
    if not isinstance(value, bool):
        fail(errors, f"{path} must be boolean")
        return None
    return value


def require_int(value: Any, path: str, errors: list[str]) -> int | None:
    if not isinstance(value, int):
        fail(errors, f"{path} must be integer")
        return None
    return value


def validate_paths(paths: Any, path: str, errors: list[str]) -> list[str]:
    if not isinstance(paths, list) or not paths:
        fail(errors, f"{path} must be a non-empty list")
        return []
    valid_paths: list[str] = []
    for index, item in enumerate(paths):
        item_path = f"{path}[{index}]"
        rel = require_string(item, item_path, errors)
        if not rel:
            continue
        if rel.startswith("http://") or rel.startswith("https://"):
            fail(errors, f"{item_path} must be a local evidence path, not URL")
            continue
        target = (ROOT / rel).resolve()
        try:
            target.relative_to(ROOT)
        except ValueError:
            fail(errors, f"{item_path} escapes repository: {rel}")
            continue
        if not target.exists():
            fail(errors, f"{item_path} does not exist: {rel}")
            continue
        valid_paths.append(rel)
    return valid_paths


def validate_gate(
    gate: Any,
    axis_id: str,
    gate_ids: set[str],
    errors: list[str],
) -> None:
    if not isinstance(gate, dict):
        fail(errors, f"{axis_id}.gates[] must contain objects")
        return

    gate_id = require_string(gate.get("gateId"), f"{axis_id}.gateId", errors)
    if gate_id:
        if gate_id in gate_ids:
            fail(errors, f"duplicate gateId: {gate_id}")
        gate_ids.add(gate_id)

    status = require_string(gate.get("status"), f"{gate_id}.status", errors)
    if status and status not in REQUIRED_STATUS:
        fail(errors, f"{gate_id}.status must be one of {sorted(REQUIRED_STATUS)}")

    require_string(gate.get("requirement"), f"{gate_id}.requirement", errors)
    validate_paths(gate.get("evidence"), f"{gate_id}.evidence", errors)

    missing = gate.get("missingEvidence")
    if not isinstance(missing, list):
        fail(errors, f"{gate_id}.missingEvidence must be a list")
    elif status in {"partial", "blocked"} and not missing:
        fail(errors, f"{gate_id} is {status} but has no missingEvidence")
    elif status == "pass" and missing:
        fail(errors, f"{gate_id} is pass but still lists missingEvidence")

    require_string(gate.get("nextAction"), f"{gate_id}.nextAction", errors)
    blocks = require_bool(gate.get("blocks100Percent"), f"{gate_id}.blocks100Percent", errors)
    if status in {"partial", "blocked"} and blocks is not True:
        fail(errors, f"{gate_id} is incomplete but does not block 100%")


def validate_axis(
    axis: Any,
    expected_axis_ids: set[str],
    roadmap_percents: dict[str, int],
    gate_ids: set[str],
    errors: list[str],
) -> None:
    if not isinstance(axis, dict):
        fail(errors, "axes[] must contain objects")
        return

    axis_id = require_string(axis.get("axisId"), "axis.axisId", errors)
    if axis_id not in REQUIRED_AXIS_IDS:
        fail(errors, f"unexpected axisId: {axis_id}")
        return
    expected_axis_ids.discard(axis_id)

    axis_name = require_string(axis.get("axisName"), f"{axis_id}.axisName", errors)
    expected_name = REQUIRED_AXIS_IDS[axis_id]
    if axis_name != expected_name:
        fail(errors, f"{axis_id}.axisName must be {expected_name!r}")

    current = require_int(axis.get("currentPercent"), f"{axis_id}.currentPercent", errors)
    target = require_int(axis.get("targetPercent"), f"{axis_id}.targetPercent", errors)
    if target != 100:
        fail(errors, f"{axis_id}.targetPercent must be 100")
    if current is not None and not (0 <= current <= 100):
        fail(errors, f"{axis_id}.currentPercent must be within [0, 100]")
    if current is not None and axis_name in roadmap_percents and current != roadmap_percents[axis_name]:
        fail(
            errors,
            f"{axis_id}.currentPercent={current} does not match roadmap={roadmap_percents[axis_name]}",
        )

    require_string(axis.get("definitionOfDone"), f"{axis_id}.definitionOfDone", errors)
    validate_paths(axis.get("primaryEvidence"), f"{axis_id}.primaryEvidence", errors)

    gates = axis.get("gates")
    if not isinstance(gates, list) or len(gates) < 6:
        fail(errors, f"{axis_id}.gates must contain at least 6 gates")
        return

    incomplete_count = 0
    blocked_count = 0
    for gate in gates:
        if isinstance(gate, dict) and gate.get("status") in {"partial", "blocked"}:
            incomplete_count += 1
        if isinstance(gate, dict) and gate.get("status") == "blocked":
            blocked_count += 1
        validate_gate(gate, axis_id, gate_ids, errors)

    if current is not None and current < 100 and incomplete_count == 0:
        fail(errors, f"{axis_id} is below 100 but has no incomplete gates")
    if axis_id == "quantitative_model" and blocked_count < 4:
        fail(errors, "quantitative_model must expose at least 4 blocked gates")


def validate_index_links(errors: list[str]) -> None:
    for relative_path in REQUIRED_INDEX_REFERENCES:
        path = ROOT / relative_path
        if not path.exists():
            fail(errors, f"missing index: {relative_path}")
            continue
        text = path.read_text(encoding="utf-8")
        if REGISTER_LINK not in text:
            fail(errors, f"index does not link maturity gap register: {relative_path}")


def validate_next_work_order(data: dict[str, Any], gate_ids: set[str], errors: list[str]) -> None:
    items = data.get("nextWorkOrder")
    if not isinstance(items, list) or len(items) < 3:
        fail(errors, "nextWorkOrder must contain at least 3 items")
        return
    priorities: set[int] = set()
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            fail(errors, f"nextWorkOrder[{index}] must be an object")
            continue
        priority = require_int(item.get("priority"), f"nextWorkOrder[{index}].priority", errors)
        if priority is not None:
            if priority in priorities:
                fail(errors, f"duplicate nextWorkOrder priority: {priority}")
            priorities.add(priority)
        require_string(item.get("item"), f"nextWorkOrder[{index}].item", errors)
        unblocks = item.get("unblocks")
        if not isinstance(unblocks, list) or not unblocks:
            fail(errors, f"nextWorkOrder[{index}].unblocks must be non-empty list")
            continue
        for gate_id in unblocks:
            if not isinstance(gate_id, str):
                fail(errors, f"nextWorkOrder[{index}].unblocks contains non-string gate")
            elif gate_id not in gate_ids:
                fail(errors, f"nextWorkOrder references unknown gate: {gate_id}")


def main() -> int:
    errors: list[str] = []
    data = load_register(errors)
    roadmap_percents = roadmap_percentages(errors)

    if data:
        if data.get("schemaVersion") != "human-infra.maturity-gap-register.v1":
            fail(errors, "schemaVersion must be human-infra.maturity-gap-register.v1")
        if data.get("status") != "active-gap-register-not-complete":
            fail(errors, "status must remain active-gap-register-not-complete until all gates pass")
        if data.get("targetPercent") == 100:
            fail(errors, "register-level targetPercent is not used; targets live on axes")

        require_string(data.get("registerId"), "registerId", errors)
        require_string(data.get("purpose"), "purpose", errors)
        source_roadmap = require_string(data.get("sourceRoadmap"), "sourceRoadmap", errors)
        if source_roadmap and not (ROOT / source_roadmap).exists():
            fail(errors, f"sourceRoadmap does not exist: {source_roadmap}")

        global_boundaries = data.get("globalBoundaries")
        if not isinstance(global_boundaries, list):
            fail(errors, "globalBoundaries must be a list")
        else:
            boundary_text = "\n".join(str(item) for item in global_boundaries)
            for phrase in REQUIRED_BOUNDARY_PHRASES:
                if phrase not in boundary_text:
                    fail(errors, f"missing global boundary phrase: {phrase}")

        axes = data.get("axes")
        expected_axis_ids = set(REQUIRED_AXIS_IDS)
        gate_ids: set[str] = set()
        if not isinstance(axes, list) or len(axes) != len(REQUIRED_AXIS_IDS):
            fail(errors, f"axes must contain exactly {len(REQUIRED_AXIS_IDS)} entries")
        else:
            for axis in axes:
                validate_axis(axis, expected_axis_ids, roadmap_percents, gate_ids, errors)
        for axis_id in sorted(expected_axis_ids):
            fail(errors, f"missing axis: {axis_id}")

        validate_next_work_order(data, gate_ids, errors)

    validate_index_links(errors)

    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1

    total_gates = sum(len(axis["gates"]) for axis in data["axes"])
    blocked_gates = sum(
        1
        for axis in data["axes"]
        for gate in axis["gates"]
        if gate["status"] == "blocked"
    )
    partial_gates = sum(
        1
        for axis in data["axes"]
        for gate in axis["gates"]
        if gate["status"] == "partial"
    )
    print(
        "maturity gap register audit ok: "
        f"axes={len(data['axes'])} gates={total_gates} "
        f"partial={partial_gates} blocked={blocked_gates}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
