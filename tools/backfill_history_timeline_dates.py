#!/usr/bin/env python3
"""Backfill full publication dates from Crossref for history timeline events."""

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
PUBLICATION_DATE_FIELDS = ("published-print", "published-online", "issued", "published")
CACHE_PROVENANCE = "crossref-publication-date-v2"


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


def choose_date(work: dict) -> str | None:
    for key in PUBLICATION_DATE_FIELDS:
        date_parts = (work.get(key) or {}).get("date-parts") or []
        if not date_parts:
            continue
        parts = date_parts[0]
        if len(parts) >= 3 and parts[0] and parts[1] and parts[2]:
            return f"{int(parts[0]):04d}-{int(parts[1]):02d}-{int(parts[2]):02d}"
    return None


def trusted_cache_date(entry: object) -> str | None:
    if not isinstance(entry, dict):
        return None
    if entry.get("provenance") != CACHE_PROVENANCE:
        return None
    date = entry.get("date")
    if not isinstance(date, str) or not FULL_DATE_RE.match(date):
        return None
    return date


def fetch_doi(doi: str, timeout: int = 45) -> str | None:
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
                return choose_date(work)
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
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--cache", type=Path, default=CACHE)
    args = parser.parse_args()

    timeline = load_json(PACKAGE / "timeline.json")
    sources_file = load_json(PACKAGE / "sources.json")
    sources = {source["source_id"]: source for source in sources_file["sources"]}
    cache: dict = {}
    if args.cache.is_file():
        cache = load_json(args.cache)

    missing_dois: dict[str, list[str]] = {}
    for event in timeline["events"]:
        if FULL_DATE_RE.match(str(event.get("date_start", ""))):
            continue
        doi = None
        for source_id in event.get("sources", []):
            candidate = sources.get(source_id, {}).get("doi")
            if candidate:
                doi = candidate
                break
        if not doi:
            continue
        missing_dois.setdefault(doi, []).append(event["event_id"])

    trusted_cached = sum(1 for doi in missing_dois if trusted_cache_date(cache.get(doi)))
    print(
        f"status=scope missing_events={sum(len(v) for v in missing_dois.values())} "
        f"unique_dois={len(missing_dois)} trusted_cached={trusted_cached} "
        f"legacy_or_invalid_cached={len(cache) - trusted_cached}"
    )
    if args.dry_run:
        return

    todos = [doi for doi in missing_dois if not trusted_cache_date(cache.get(doi))]
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
                date = future.result()
                if date:
                    cache[doi] = {"date": date, "provenance": CACHE_PROVENANCE}
                fetched += 1
                if fetched % 50 == 0:
                    dump_json(args.cache, cache)
                    print(f"progress fetched={fetched} cached={len(cache)}", flush=True)
        dump_json(args.cache, cache)
        print(f"status=fetch_done fetched={fetched} cached={len(cache)}", flush=True)

    updated_events = 0
    updated_at = now_iso()
    for event in timeline["events"]:
        if FULL_DATE_RE.match(str(event.get("date_start", ""))):
            continue
        doi = None
        for source_id in event.get("sources", []):
            candidate = sources.get(source_id, {}).get("doi")
            if candidate:
                doi = candidate
                break
        if not doi:
            continue
        date = trusted_cache_date(cache.get(doi))
        if not date or not FULL_DATE_RE.match(date):
            continue
        event["date_start"] = date
        event["date_type"] = "exact"
        event["updated_at"] = updated_at
        note = str(event.get("notes", ""))
        if "日期补齐：Crossref" not in note:
            event["notes"] = f"{note}；日期补齐：Crossref {date}".strip("；")
        updated_events += 1

    if updated_events:
        timeline["version"] = bump_patch(timeline["version"])
        sources_file["version"] = bump_patch(sources_file["version"])
        dump_json(PACKAGE / "timeline.json", timeline)
        dump_json(PACKAGE / "sources.json", sources_file)
    print(f"status=OK updated_events={updated_events} version={timeline['version']} cache={args.cache}")


if __name__ == "__main__":
    main()
