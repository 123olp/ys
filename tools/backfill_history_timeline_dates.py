#!/usr/bin/env python3
"""Backfill publication dates from Crossref for history timeline events."""

from __future__ import annotations

import argparse
import json
import re
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "docs" / "reference" / "history-timeline"
CACHE = PACKAGE / "date-backfill-cache.json"
MAILTO = "human-infra@tradecatlabs.com"
FULL_DATE_RE = re.compile(r"^-?\d{4}-\d{2}-\d{2}$")
MONTH_DATE_RE = re.compile(r"^-?\d{4}-\d{2}$")
YEAR_DATE_RE = re.compile(r"^-?\d{4}$")
PUBLICATION_DATE_FIELDS = ("published-online", "published-print", "issued", "published")
CACHE_PROVENANCE = "crossref-publication-date-v3"
CACHE_VERSION_LABEL = CACHE_PROVENANCE.rsplit("-", 1)[-1]
LEGACY_NOTE_MARKER = "日期补齐：Crossref"
DATE_PRECISIONS = {"year", "month", "day"}


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def bump_patch(version: str) -> str:
    major, minor, patch = (int(part) for part in version.split("."))
    return f"{major}.{minor}.{patch + 1}"


def choose_date_record(work: dict) -> dict[str, str] | None:
    candidates: list[dict[str, str]] = []
    for field in PUBLICATION_DATE_FIELDS:
        date_parts = (work.get(field) or {}).get("date-parts") or []
        if not date_parts:
            continue
        parts = date_parts[0]
        if not parts or not parts[0]:
            continue
        date = f"{int(parts[0]):04d}"
        precision = "year"
        if len(parts) >= 2 and parts[1]:
            date += f"-{int(parts[1]):02d}"
            precision = "month"
        if len(parts) >= 3 and parts[2]:
            date += f"-{int(parts[2]):02d}"
            precision = "day"
        candidates.append(
            {
                "date": date,
                "precision": precision,
                "field": field,
                "provenance": CACHE_PROVENANCE,
            }
        )
    if not candidates:
        return None
    return candidates[0]


def choose_date(work: dict) -> str | None:
    record = choose_date_record(work)
    if not record or record["precision"] != "day":
        return None
    return record["date"]


def trusted_cache_record(entry: object) -> dict[str, str] | None:
    if not isinstance(entry, dict):
        return None
    if entry.get("provenance") != CACHE_PROVENANCE:
        return None
    field = entry.get("field")
    precision = entry.get("precision")
    date = entry.get("date")
    if field not in PUBLICATION_DATE_FIELDS or precision not in DATE_PRECISIONS:
        return None
    if not isinstance(date, str):
        return None
    validators = {"year": YEAR_DATE_RE, "month": MONTH_DATE_RE, "day": FULL_DATE_RE}
    if not validators[precision].match(date):
        return None
    return {
        "date": date,
        "precision": precision,
        "field": field,
        "provenance": CACHE_PROVENANCE,
    }


def trusted_cache_date(entry: object) -> str | None:
    record = trusted_cache_record(entry)
    if not record or record["precision"] != "day":
        return None
    return record["date"]


def event_needs_refresh(
    event: dict,
    doi: str,
    cache: dict,
    refresh_legacy: bool,
) -> bool:
    """Return whether an event needs a fetch or a provenance-aware rewrite."""
    record = trusted_cache_record(cache.get(doi))
    notes = str(event.get("notes", ""))
    expected_date_type = None
    if record:
        expected_date_type = "exact" if record["precision"] == "day" else "approx"

    if refresh_legacy and doi in cache and not record:
        return True
    if refresh_legacy and LEGACY_NOTE_MARKER in notes:
        if not record or f", {CACHE_VERSION_LABEL})" not in notes:
            return True

    if FULL_DATE_RE.match(str(event.get("date_start", ""))):
        return False
    if not record:
        return True
    return any(
        (
            event.get("date_start") != record["date"],
            event.get("date_type") != expected_date_type,
            LEGACY_NOTE_MARKER not in notes,
            f", {CACHE_VERSION_LABEL})" not in notes,
        )
    )


def apply_date_record(event: dict, record: dict[str, str], updated_at: str) -> bool:
    """Apply one trusted date record and report whether the event changed."""
    date_type = "exact" if record["precision"] == "day" else "approx"
    note_parts = [
        part
        for part in str(event.get("notes", "")).split("；")
        if part and not part.startswith(LEGACY_NOTE_MARKER)
    ]
    note_parts.append(
        f"{LEGACY_NOTE_MARKER} {record['date']} "
        f"({record['field']}, {record['precision']}, {CACHE_VERSION_LABEL})"
    )
    notes = "；".join(note_parts)
    changed = any(
        (
            event.get("date_start") != record["date"],
            event.get("date_type") != date_type,
            event.get("notes", "") != notes,
        )
    )
    if not changed:
        return False
    event["date_start"] = record["date"]
    event["date_type"] = date_type
    event["notes"] = notes
    event["updated_at"] = updated_at
    return True


def fetch_doi(doi: str, timeout: int = 45) -> dict[str, str] | None:
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="")
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": f"HumanInfraTimeline/2.0 (mailto:{MAILTO})",
            "Accept": "application/json",
        },
    )
    last_error: Exception | None = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                work = json.loads(response.read().decode("utf-8"))["message"]
                return choose_date_record(work)
        except Exception as exc:
            last_error = exc
            if attempt < 2:
                time.sleep(2 * (attempt + 1))
    if last_error:
        print(f"warn doi={doi} error={last_error}", flush=True)
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=0, help="limit number of DOIs to fetch")
    parser.add_argument("--dry-run", action="store_true", help="report scope without changing files")
    parser.add_argument(
        "--refresh-legacy",
        action="store_true",
        help="re-fetch events previously filled from unversioned Crossref cache entries",
    )
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--cache", type=Path, default=CACHE)
    args = parser.parse_args()

    timeline = load_json(PACKAGE / "timeline.json")
    sources_file = load_json(PACKAGE / "sources.json")
    sources = {source["source_id"]: source for source in sources_file["sources"]}
    cache: dict = {}
    if args.cache.is_file():
        cache = load_json(args.cache)

    target_dois: dict[str, list[str]] = {}
    for event in timeline["events"]:
        doi = None
        for source_id in event.get("sources", []):
            candidate = sources.get(source_id, {}).get("doi")
            if candidate:
                doi = candidate
                break
        if not doi:
            continue
        if event_needs_refresh(event, doi, cache, args.refresh_legacy):
            target_dois.setdefault(doi, []).append(event["event_id"])

    trusted_cached = sum(1 for doi in target_dois if trusted_cache_record(cache.get(doi)))
    legacy_or_invalid_cached = sum(
        1 for doi in target_dois if doi in cache and not trusted_cache_record(cache.get(doi))
    )
    print(
        f"status=scope target_events={sum(len(v) for v in target_dois.values())} "
        f"unique_dois={len(target_dois)} trusted_cached={trusted_cached} "
        f"legacy_or_invalid_cached={legacy_or_invalid_cached}"
    )
    if args.dry_run:
        return

    todos = [doi for doi in target_dois if not trusted_cache_record(cache.get(doi))]
    if args.limit:
        todos = todos[: args.limit]
    if not todos:
        print("status=OK no_new_dois_to_fetch")
    else:
        fetched = 0
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = {executor.submit(fetch_doi, doi): doi for doi in todos}
            for future in as_completed(futures):
                doi = futures[future]
                record = future.result()
                if record:
                    cache[doi] = record
                fetched += 1
                if fetched % 50 == 0:
                    dump_json(args.cache, cache)
                    print(f"progress fetched={fetched} cached={len(cache)}", flush=True)
        dump_json(args.cache, cache)
        print(f"status=fetch_done fetched={fetched} cached={len(cache)}", flush=True)

    updated_events = 0
    updated_at = now_iso()
    target_event_ids = {
        event_id for event_ids in target_dois.values() for event_id in event_ids
    }
    for event in timeline["events"]:
        if event["event_id"] not in target_event_ids:
            continue
        doi = None
        for source_id in event.get("sources", []):
            candidate = sources.get(source_id, {}).get("doi")
            if candidate:
                doi = candidate
                break
        if not doi:
            continue
        record = trusted_cache_record(cache.get(doi))
        if not record:
            continue
        if apply_date_record(event, record, updated_at):
            updated_events += 1

    if updated_events:
        timeline["version"] = bump_patch(timeline["version"])
        timeline["updated_at"] = updated_at
        dump_json(PACKAGE / "timeline.json", timeline)
    print(f"status=OK updated_events={updated_events} version={timeline['version']} cache={args.cache}")


if __name__ == "__main__":
    main()
