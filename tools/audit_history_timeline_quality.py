#!/usr/bin/env python3
"""Audit structural quality of the history timeline data."""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "docs" / "reference" / "history-timeline"


def load_json(name: str):
    return json.loads((PACKAGE / name).read_text(encoding="utf-8"))


def main() -> None:
    timeline = load_json("timeline.json")["events"]
    sources = load_json("sources.json")["sources"]
    source_ids = {source["source_id"] for source in sources}
    source_by_id = {source["source_id"]: source for source in sources}

    issues: dict[str, list[str]] = defaultdict(list)
    for event in timeline:
        event_id = event.get("event_id", "")
        title = event.get("title", "")
        if not title.strip():
            issues["empty_title"].append(event_id)
        if not event.get("summary", "").strip():
            issues["empty_summary"].append(event_id)
        if not event.get("claim", "").strip():
            issues["empty_claim"].append(event_id)
        refs = event.get("sources", [])
        if not refs:
            issues["no_sources"].append(event_id)
        missing = [ref for ref in refs if ref not in source_ids]
        if missing:
            issues["missing_source_ref"].append(f"{event_id}:{','.join(missing)}")
        if event.get("date_type") == "exact" and not re.search(
            r"-\d{1,2}-\d{1,2}$", str(event.get("date_start", ""))
        ):
            issues["exact_without_day"].append(event_id)

    def canonical_source_key(source: dict) -> str | None:
        return source.get("doi") or source.get("url")

    def event_source_keys(event: dict) -> set[str]:
        keys: set[str] = set()
        for ref in event.get("sources", []):
            source = source_by_id.get(ref, {})
            key = canonical_source_key(source)
            if key:
                keys.add(key)
        return keys

    title_groups: dict[str, list[dict]] = defaultdict(list)
    for event in timeline:
        title_groups[event.get("title", "")].append(event)

    duplicate_title_same_source: list[str] = []
    same_title_different_source = 0
    for title, group in title_groups.items():
        if len(group) < 2:
            continue
        key_sets = [event_source_keys(event) for event in group]
        if any(
            key_sets[i] & key_sets[j]
            for i in range(len(key_sets))
            for j in range(i + 1, len(key_sets))
        ):
            duplicate_title_same_source.append(title)
        else:
            same_title_different_source += 1

    source_key_groups: dict[str, list[str]] = defaultdict(list)
    for source in sources:
        key = canonical_source_key(source)
        if key:
            source_key_groups[key].append(source["source_id"])
    duplicate_source_identity = [
        key for key, source_ids_in_group in source_key_groups.items()
        if len(source_ids_in_group) > 1
    ]
    hard_error_keys = ("empty_title", "empty_summary", "empty_claim", "no_sources", "missing_source_ref")
    hard_errors = sum(len(issues[key]) for key in hard_error_keys)
    warnings = (
        len(issues["exact_without_day"])
        + len(duplicate_title_same_source)
        + len(duplicate_source_identity)
    )

    print(
        "status=OK history_timeline_quality=pass "
        f"events={len(timeline)} hard_errors={hard_errors} warnings={warnings} "
        f"duplicate_title_same_source={len(duplicate_title_same_source)} "
        f"same_title_different_source={same_title_different_source} "
        f"duplicate_source_identity={len(duplicate_source_identity)} "
        f"exact_without_day={len(issues['exact_without_day'])}"
    )
    if hard_errors:
        for key in hard_error_keys:
            for item in issues[key][:10]:
                print(f"issue={key} event={item}")
        print(f"status=FAIL reason=hard_quality_errors count={hard_errors}")
        raise SystemExit(1)
    for key in duplicate_source_identity[:10]:
        ids = ",".join(source_key_groups[key])
        print(f"warning=duplicate_source_identity key={key} sources={ids}")


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as exc:  # pragma: no cover
        print(f"status=FAIL reason=unexpected_error detail={type(exc).__name__}: {exc}")
        raise SystemExit(1) from exc
