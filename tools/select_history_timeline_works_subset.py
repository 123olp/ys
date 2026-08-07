#!/usr/bin/env python3
"""Select a balanced first-edition works subset from the history timeline."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "docs" / "reference" / "history-timeline"
OUTPUT = PACKAGE / "works-subset.v1.json"

KNOWN_WRONG_SOURCE_HINTS = (
    "未绑定事件正文",
    "blocked",
    "404",
    "无法访问",
)


def load(name: str) -> dict:
    return json.loads((PACKAGE / name).read_text(encoding="utf-8"))


def has_exact_date(event: dict) -> bool:
    return bool(
        event.get("date_type") == "exact"
        and re.search(r"-\d{1,2}-\d{1,2}$", str(event.get("date_start", "")))
    )


def score_event(event: dict, path_counts: Counter, type_counts: Counter) -> float:
    score = 0.0
    significance = event.get("significance", "major")
    score += {"turning_point": 100.0, "major": 60.0, "medium": 20.0}.get(significance, 10.0)
    if has_exact_date(event):
        score += 20.0
    if len(event.get("sources", [])) >= 2:
        score += 5.0

    under_path = {
        "maintenance": 20.0,
        "reconstruction": 30.0,
        "social_composite": 35.0,
        "cognitive_extension": 35.0,
        "suspension": 40.0,
        "philosophical": 45.0,
        "digital_migration": 45.0,
        "cross_path": 45.0,
    }
    under_type = {
        "technology": 20.0,
        "literature": 35.0,
        "thought": 30.0,
        "policy": 45.0,
        "institution": 45.0,
        "practice": 45.0,
        "failure": 50.0,
        "demographic": 50.0,
    }
    under_evidence = {
        "S": 10.0,
        "I": 25.0,
        "T": 40.0,
        "M": 40.0,
        "L": 50.0,
    }
    path = event.get("path_family", "")
    score += under_path.get(path, 0.0) / max(1, path_counts.get(path, 1))
    event_type = event.get("event_type", "")
    score += under_type.get(event_type, 0.0) / max(1, type_counts.get(event_type, 1))
    score += under_evidence.get(event.get("evidence_grade", ""), 0.0)
    return score


def is_usable(event: dict, source_registry: dict[str, dict]) -> bool:
    for ref in event.get("sources", []):
        source = source_registry.get(ref, {})
        note = source.get("note", "")
        if any(hint in note for hint in KNOWN_WRONG_SOURCE_HINTS):
            return False
    return True


def main() -> int:
    timeline = load("timeline.json")
    sources = load("sources.json")
    source_registry = {s["source_id"]: s for s in sources["sources"]}

    events = timeline["events"]
    pre_modern = [e for e in events if e.get("period_id") != "period-21st-century"]
    modern = [e for e in events if e.get("period_id") == "period-21st-century"]

    path_counts = Counter(e.get("path_family") for e in modern)
    type_counts = Counter(e.get("event_type") for e in modern)
    usable_modern = [e for e in modern if is_usable(e, source_registry)]
    ranked = sorted(
        usable_modern,
        key=lambda e: (score_event(e, path_counts, type_counts), e["event_id"]),
        reverse=True,
    )

    target_total = 400
    modern_quota = target_total - len(pre_modern)
    selected_modern = ranked[:modern_quota]
    selected_ids = [e["event_id"] for e in pre_modern] + [
        e["event_id"] for e in selected_modern
    ]
    selected_ids.sort()

    by_id = {e["event_id"]: e for e in events}
    selected_events = [by_id[i] for i in selected_ids]
    stats = {
        "total_selected": len(selected_ids),
        "pre_modern_selected": len(pre_modern),
        "modern_selected": len(selected_modern),
        "by_period": dict(Counter(e.get("period_id") for e in selected_events)),
        "by_path_family": dict(Counter(e.get("path_family") for e in selected_events)),
        "by_event_type": dict(Counter(e.get("event_type") for e in selected_events)),
        "by_evidence_grade": dict(Counter(e.get("evidence_grade") for e in selected_events)),
        "by_significance": dict(Counter(e.get("significance") for e in selected_events)),
    }

    payload = {
        "subset_id": "HITL-WS-V1",
        "version": "1.0.0",
        "title": "永生史第一版作品子集",
        "created_at": "2026-08-07T12:00:00Z",
        "description": "从 2592 条 draft 事件中选择 400 条作为第一版作品子集，覆盖全部本地时期、路径族、事件类型与证据等级，并优先收录转折点和日期精确事件。",
        "selection_criteria": [
            "覆盖全部本地时期，不把作品正文局限于 21 世纪技术事件。",
            "覆盖 8 个路径族和主要事件类型，保留神话、思想、失败与制度线索。",
            "优先收录 significance=turning_point、日期精确、来源数量较多的可复核事件。",
            "排除已知未绑定正文、不可访问或 blocked 来源。",
            "当前只表示入选，不表示复核；verification_status 必须单独推进。",
        ],
        "reviewed_event_count": 0,
        "fresh_reviewed_event_count": 0,
        "event_ids": selected_ids,
        "stats": stats,
    }

    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        "status=OK subset=HITL-WS-V1 "
        f"selected={len(selected_ids)} modern={len(selected_modern)} "
        f"usable_modern={len(usable_modern)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
