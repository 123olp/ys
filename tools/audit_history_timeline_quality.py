#!/usr/bin/env python3
"""Audit structural quality of the history timeline data."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "docs" / "reference" / "history-timeline"


def load_json(name: str):
    return json.loads((PACKAGE / name).read_text(encoding="utf-8"))


def main() -> None:
    timeline = load_json("timeline.json")["events"]
    source_ids = {source["source_id"] for source in load_json("sources.json")["sources"]}

    issues: dict[str, list[str]] = defaultdict(list)
    title_counts: Counter[str] = Counter()
    for event in timeline:
        event_id = event.get("event_id", "")
        title = event.get("title", "")
        title_counts[title] += 1
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

    duplicate_titles = [title for title, count in title_counts.items() if count > 1]
    hard_error_keys = ("empty_title", "empty_summary", "empty_claim", "no_sources", "missing_source_ref")
    hard_errors = sum(len(issues[key]) for key in hard_error_keys)
    warnings = len(issues["exact_without_day"]) + len(duplicate_titles)

    print(
        "status=OK history_timeline_quality=pass "
        f"events={len(timeline)} hard_errors={hard_errors} warnings={warnings} "
        f"duplicate_titles={len(duplicate_titles)} exact_without_day={len(issues['exact_without_day'])}"
    )
    if hard_errors:
        for key in hard_error_keys:
            for item in issues[key][:10]:
                print(f"issue={key} event={item}")
        print(f"status=FAIL reason=hard_quality_errors count={hard_errors}")
        raise SystemExit(1)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as exc:  # pragma: no cover
        print(f"status=FAIL reason=unexpected_error detail={type(exc).__name__}: {exc}")
        raise SystemExit(1) from exc
