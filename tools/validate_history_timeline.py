#!/usr/bin/env python3
"""Validate the Human Infra history timeline machine contract."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from build_history_timeline_preview import build_timelinejs, render_preview


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "docs" / "reference" / "history-timeline"
CONTRACT = ROOT / "governance" / "control-plane" / "history-timeline-contract.v1.yaml"

REQUIRED_FILES = [
    "docs/reference/history-timeline/README.md",
    "docs/reference/history-timeline/CONTRACT.md",
    "docs/reference/history-timeline/GOVERNANCE.md",
    "docs/reference/history-timeline/TOOLS.md",
    "docs/reference/history-timeline/timeline.schema.json",
    "docs/reference/history-timeline/sources.schema.json",
    "docs/reference/history-timeline/periods.schema.json",
    "docs/reference/history-timeline/timeline.json",
    "docs/reference/history-timeline/sources.json",
    "docs/reference/history-timeline/periods.json",
    "docs/reference/history-timeline/example-events.json",
    "docs/reference/history-timeline/works-subset.schema.json",
    "docs/reference/history-timeline/works-subset.v1.json",
    "docs/reference/history-timeline/works-review-register.schema.json",
    "docs/reference/history-timeline/works-review-register.v1.json",
    "docs/reference/history-timeline/timelinejs.json",
    "docs/reference/history-timeline/preview.html",
    "docs/templates/history-event.md",
]

DATE_TYPES = {"exact", "approx", "range", "long_process", "era", "undated"}
PATH_FAMILIES = {
    "maintenance",
    "reconstruction",
    "suspension",
    "digital_migration",
    "cognitive_extension",
    "social_composite",
    "philosophical",
    "cross_path",
}
EVENT_TYPES = {
    "myth",
    "religious",
    "thought",
    "practice",
    "technology",
    "institution",
    "literature",
    "failure",
    "demographic",
    "policy",
}
EVIDENCE_GRADES = {"S", "M", "I", "T", "L"}
VERIFICATION_STATUSES = {
    "unreviewed",
    "locally_reviewed",
    "fresh_reviewed",
    "blocked",
    "superseded",
}
STATUSES = {"draft", "needs_revision", "published", "archived"}
SOURCE_TYPES = {"primary", "secondary", "tertiary", "expert_narrative"}
MAPPING_STATUSES = {"matched", "pending"}
TOP_REQUIRED = {"timeline_id", "version", "events"}
REGISTRY_REQUIRED = {"timeline_id", "version"}
SOURCE_REQUIRED = {"source_id", "source_type", "label", "url"}
PERIOD_REQUIRED = {"period_id", "label_zh", "label_en", "mapping_status"}
EVENT_REQUIRED = {
    "event_id",
    "title",
    "date_start",
    "date_type",
    "civilization",
    "region",
    "path_family",
    "event_type",
    "claim",
    "summary",
    "sources",
    "evidence_grade",
    "verification_status",
    "status",
}


def fail(message: str) -> None:
    print(f"status=FAIL reason={message}")
    raise SystemExit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load_json(relative_path: str):
    path = ROOT / relative_path
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"json_error path={relative_path} detail={exc}")
    except OSError as exc:
        fail(f"read_error path={relative_path} detail={exc}")


def validate_sources(sources: list) -> dict[str, dict]:
    registry: dict[str, dict] = {}
    for index, source in enumerate(sources):
        prefix = f"sources[{index}]"
        require(isinstance(source, dict), f"invalid_source {prefix}")
        missing = SOURCE_REQUIRED - set(source)
        require(not missing, f"missing_source_field {prefix} fields={','.join(sorted(missing))}")
        source_id = source.get("source_id", "")
        require(
            re.fullmatch(r"SRC-[0-9]{3,}", source_id) is not None,
            f"invalid_source_id {prefix} value={source_id}",
        )
        require(source.get("source_type") in SOURCE_TYPES, f"invalid_source_type {prefix}")
        require(source.get("label", "").strip(), f"empty_source_label {prefix}")
        require(source.get("url", "").strip(), f"empty_source_url {prefix}")
        require(source_id not in registry, f"duplicate_source_id source_id={source_id}")
        registry[source_id] = source
    return registry


def validate_periods(periods: list) -> dict[str, dict]:
    registry: dict[str, dict] = {}
    for index, period in enumerate(periods):
        prefix = f"periods[{index}]"
        require(isinstance(period, dict), f"invalid_period {prefix}")
        missing = PERIOD_REQUIRED - set(period)
        require(not missing, f"missing_period_field {prefix} fields={','.join(sorted(missing))}")
        period_id = period.get("period_id", "")
        require(
            re.fullmatch(r"period-[a-z0-9-]+", period_id) is not None,
            f"invalid_period_id {prefix} value={period_id}",
        )
        require(period.get("label_zh", "").strip(), f"empty_period_label_zh {prefix}")
        require(period.get("label_en", "").strip(), f"empty_period_label_en {prefix}")
        require(period.get("mapping_status") in MAPPING_STATUSES, f"invalid_mapping_status {prefix}")
        require(period_id not in registry, f"duplicate_period_id period_id={period_id}")
        registry[period_id] = period
    return registry


def validate_event(
    event: dict,
    index: int,
    source_registry: dict[str, dict],
    period_registry: dict[str, dict],
) -> None:
    prefix = f"event[{index}]"
    missing = EVENT_REQUIRED - set(event)
    require(not missing, f"missing_event_field {prefix} fields={','.join(sorted(missing))}")

    event_id = event.get("event_id", "")
    require(
        re.fullmatch(r"HIT-[A-Z]{3}-[0-9]{3,}", event_id) is not None,
        f"invalid_event_id {prefix} value={event_id}",
    )
    require(event.get("title", "").strip(), f"empty_title {prefix}")
    require(event.get("date_start", "").strip(), f"empty_date_start {prefix}")
    require(event.get("date_type") in DATE_TYPES, f"invalid_date_type {prefix}")
    require(event.get("civilization", "").strip(), f"empty_civilization {prefix}")
    require(event.get("region", "").strip(), f"empty_region {prefix}")
    require(event.get("path_family") in PATH_FAMILIES, f"invalid_path_family {prefix}")
    require(event.get("event_type") in EVENT_TYPES, f"invalid_event_type {prefix}")
    require(event.get("claim", "").strip(), f"empty_claim {prefix}")
    require(event.get("summary", "").strip(), f"empty_summary {prefix}")
    require(event.get("evidence_grade") in EVIDENCE_GRADES, f"invalid_evidence_grade {prefix}")
    require(
        event.get("verification_status") in VERIFICATION_STATUSES,
        f"invalid_verification_status {prefix}",
    )
    require(event.get("status") in STATUSES, f"invalid_status {prefix}")

    period_id = event.get("period_id")
    if period_id:
        require(period_id in period_registry, f"unknown_period_id {prefix} period_id={period_id}")

    sources = event.get("sources")
    require(isinstance(sources, list) and sources, f"missing_sources {prefix}")
    seen_sources: set[str] = set()
    for source_index, source_ref in enumerate(sources):
        require(isinstance(source_ref, str), f"invalid_source_ref {prefix} source_index={source_index}")
        require(
            re.fullmatch(r"SRC-[0-9]{3,}", source_ref) is not None,
            f"invalid_source_ref {prefix} value={source_ref}",
        )
        require(source_ref in source_registry, f"unknown_source_ref {prefix} source_id={source_ref}")
        require(source_ref not in seen_sources, f"duplicate_source_in_event {prefix} source_id={source_ref}")
        seen_sources.add(source_ref)


def validate_registry_file(relative_path: str, kind: str) -> dict[str, dict]:
    data = load_json(relative_path)
    require(isinstance(data, dict), f"registry_not_object path={relative_path}")
    missing = REGISTRY_REQUIRED - set(data)
    require(not missing, f"missing_registry_field path={relative_path} fields={','.join(sorted(missing))}")
    require(
        re.fullmatch(r"HITL-[A-Z0-9-]+", data.get("timeline_id", "")),
        f"invalid_timeline_id path={relative_path}",
    )
    require(
        re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", data.get("version", "")),
        f"invalid_timeline_version path={relative_path}",
    )
    items = data.get("sources" if kind == "sources" else "periods")
    require(isinstance(items, list), f"{kind}_not_list path={relative_path}")
    if kind == "sources":
        return validate_sources(items)
    return validate_periods(items)


def validate_timeline_file(
    relative_path: str,
    source_registry: dict[str, dict],
    period_registry: dict[str, dict],
) -> list[str]:
    data = load_json(relative_path)
    missing = TOP_REQUIRED - set(data)
    require(not missing, f"missing_top_level_field fields={','.join(sorted(missing))}")
    require(
        re.fullmatch(r"HITL-[A-Z0-9-]+", data.get("timeline_id", "")),
        "invalid_timeline_id",
    )
    require(
        re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", data.get("version", "")),
        "invalid_timeline_version",
    )
    require(isinstance(data.get("events"), list), "events_not_list")

    event_ids: set[str] = set()
    for index, event in enumerate(data["events"]):
        validate_event(event, index, source_registry, period_registry)
        event_id = event["event_id"]
        require(event_id not in event_ids, f"duplicate_event_id event_id={event_id}")
        event_ids.add(event_id)

    for index, event in enumerate(data["events"]):
        for cross_link in event.get("cross_links", []):
            require(cross_link in event_ids, f"unknown_cross_link event_index={index} cross_link={cross_link}")

    return sorted(event_ids)


def validate_works_subset(relative_path: str, event_ids: set[str]) -> None:
    data = load_json(relative_path)
    require(isinstance(data, dict), f"invalid_works_subset path={relative_path}")
    subset_id = data.get("subset_id", "")
    require(
        re.fullmatch(r"HITL-WS-V[0-9]+", subset_id),
        f"invalid_subset_id path={relative_path} value={subset_id}",
    )
    require(
        re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", data.get("version", "")),
        f"invalid_subset_version path={relative_path}",
    )
    ids = data.get("event_ids")
    require(isinstance(ids, list) and len(set(ids)) == len(ids), f"invalid_subset_ids {relative_path}")
    require(len(ids) > 0, f"empty_subset {relative_path}")
    for event_id in ids:
        require(event_id in event_ids, f"unknown_subset_event {relative_path} event_id={event_id}")
    require(data.get("reviewed_event_count", 0) >= 0, f"invalid_reviewed_count {relative_path}")
    require(data.get("fresh_reviewed_event_count", 0) >= 0, f"invalid_fresh_reviewed_count {relative_path}")


def validate_works_review_register(
    relative_path: str,
    event_ids: set[str],
    subset_ids: set[str],
    source_registry: dict[str, dict],
    timeline_by_id: dict[str, dict],
    works_subset: dict,
) -> None:
    data = load_json(relative_path)
    require(isinstance(data, dict), f"invalid_works_review_register {relative_path}")
    require(
        re.fullmatch(r"HITL-WSR-V[0-9]+", data.get("register_id", "")),
        f"invalid_register_id {relative_path}",
    )
    require(
        re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", data.get("version", "")),
        f"invalid_register_version {relative_path}",
    )
    entries = data.get("entries")
    require(isinstance(entries, list) and entries, f"invalid_register_entries {relative_path}")

    reviewed_ids: set[str] = set()
    for index, entry in enumerate(entries):
        prefix = f"register[{index}]"
        require(isinstance(entry, dict), f"invalid_register_entry {prefix}")
        event_id = entry.get("event_id", "")
        require(event_id in event_ids, f"unknown_review_event {prefix} event_id={event_id}")
        require(event_id in subset_ids, f"review_event_not_in_subset {prefix} event_id={event_id}")
        verdict = entry.get("verdict")
        require(verdict in {"locally_reviewed", "needs_revision", "blocked"}, f"invalid_verdict {prefix}")
        require(event_id not in reviewed_ids, f"duplicate_review_event {prefix} event_id={event_id}")
        reviewed_ids.add(event_id)
        source_status = entry.get("source_status", {})
        require(isinstance(source_status, dict), f"invalid_source_status {prefix}")
        for source_ref in source_status:
            require(source_ref in source_registry, f"unknown_review_source {prefix} source_id={source_ref}")

        if verdict == "locally_reviewed":
            require(
                timeline_by_id[event_id].get("verification_status") == "locally_reviewed",
                f"verdict_not_synced {prefix} event_id={event_id}",
            )

    timeline_reviewed = sum(
        1 for event in timeline_by_id.values() if event.get("verification_status") == "locally_reviewed"
    )
    require(
        timeline_reviewed == works_subset.get("reviewed_event_count", 0),
        "reviewed_count_mismatch",
    )


def main() -> None:
    for relative_path in REQUIRED_FILES:
        require((ROOT / relative_path).is_file(), f"missing_required_file path={relative_path}")

    schema = load_json("docs/reference/history-timeline/timeline.schema.json")
    require(schema.get("$schema", "").startswith("https://json-schema.org/"), "invalid_schema_dialect")

    source_registry = validate_registry_file(
        "docs/reference/history-timeline/sources.json",
        "sources",
    )
    period_registry = validate_registry_file(
        "docs/reference/history-timeline/periods.json",
        "periods",
    )
    event_ids = validate_timeline_file(
        "docs/reference/history-timeline/timeline.json",
        source_registry,
        period_registry,
    )
    validate_works_subset(
        "docs/reference/history-timeline/works-subset.v1.json",
        set(event_ids),
    )
    works_subset = load_json("docs/reference/history-timeline/works-subset.v1.json")
    timeline_by_id = {event["event_id"]: event for event in load_json("docs/reference/history-timeline/timeline.json")["events"]}
    validate_works_review_register(
        "docs/reference/history-timeline/works-review-register.v1.json",
        set(event_ids),
        set(works_subset["event_ids"]),
        source_registry,
        timeline_by_id,
        works_subset,
    )

    # The example file remains a compact, reviewable illustration and must use the same reference model.
    example = load_json("docs/reference/history-timeline/example-events.json")
    require(isinstance(example, dict) and isinstance(example.get("events"), list), "invalid_example_file")
    for index, event in enumerate(example["events"]):
        validate_event(event, index, source_registry, period_registry)
        example_id = event["event_id"]
        require(example_id in event_ids, f"example_event_not_in_timeline event_id={example_id}")

    expected_timelinejs = build_timelinejs()
    actual_timelinejs = load_json("docs/reference/history-timeline/timelinejs.json")
    require(actual_timelinejs == expected_timelinejs, "stale_timelinejs_preview")
    expected_preview = render_preview(expected_timelinejs)
    actual_preview = (ROOT / "docs/reference/history-timeline/preview.html").read_text(encoding="utf-8")
    require(actual_preview == expected_preview, "stale_preview_html")

    contract_text = CONTRACT.read_text(encoding="utf-8")
    for relative_path in REQUIRED_FILES:
        require(relative_path in contract_text, f"contract_mismatch path={relative_path}")

    print(f"status=OK history_timeline=pass events={len(event_ids)} sources={len(source_registry)} periods={len(period_registry)}")


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as exc:  # pragma: no cover
        print(f"status=FAIL reason=unexpected_error detail={type(exc).__name__}: {exc}")
        raise SystemExit(1) from exc
