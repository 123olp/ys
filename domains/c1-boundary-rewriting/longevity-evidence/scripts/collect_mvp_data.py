#!/usr/bin/env python3
"""采集 Longevity Evidence MVP 的公开数据源。

脚本只使用官方 API 或公开数据库入口，保留原始响应，再生成轻量 JSONL 索引。
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
from datetime import UTC, datetime
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INTERVENTIONS = ROOT / "data" / "manual" / "interventions.json"
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"
USER_AGENT = "HumanInfra-LongevityEvidence/0.1 (public evidence research; contact: local)"
AGING_TERMS = "(aging OR ageing OR longevity OR lifespan OR healthspan)"


def utc_now() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat()


def ensure_dirs() -> None:
    for path in [
        RAW_DIR / "pubmed",
        RAW_DIR / "openalex",
        RAW_DIR / "clinicaltrials",
        RAW_DIR / "openfda",
        PROCESSED_DIR,
    ]:
        path.mkdir(parents=True, exist_ok=True)


def load_interventions(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, list):
        raise ValueError("interventions.json 必须是数组")
    return data


def request_json(url: str, timeout: int = 30, retries: int = 2) -> tuple[dict[str, Any] | None, dict[str, Any]]:
    started = time.time()
    last_meta: dict[str, Any] = {}
    for attempt in range(retries + 1):
        request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
        try:
            with urlopen(request, timeout=timeout) as response:
                body = response.read()
                meta = {
                    "url": url,
                    "status": response.status,
                    "retrieved_at": utc_now(),
                    "elapsed_ms": round((time.time() - started) * 1000),
                    "attempts": attempt + 1,
                    "raw_hash": hashlib.sha256(body).hexdigest(),
                }
                return json.loads(body.decode("utf-8")), meta
        except HTTPError as exc:
            body = exc.read()
            last_meta = {
                "url": url,
                "status": exc.code,
                "retrieved_at": utc_now(),
                "elapsed_ms": round((time.time() - started) * 1000),
                "attempts": attempt + 1,
                "error": body.decode("utf-8", errors="replace")[:1000],
            }
            if exc.code not in {429, 500, 502, 503, 504} or attempt >= retries:
                return None, last_meta
        except (URLError, TimeoutError) as exc:
            last_meta = {
                "url": url,
                "status": "network_error",
                "retrieved_at": utc_now(),
                "elapsed_ms": round((time.time() - started) * 1000),
                "attempts": attempt + 1,
                "error": str(exc),
            }
            if attempt >= retries:
                return None, last_meta
        time.sleep(1.5 * (attempt + 1))
    return None, last_meta


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")


def append_jsonl(path: Path, records: list[dict[str, Any]]) -> None:
    with path.open("a", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")


def pubmed_query(term: str, limit: int) -> str:
    query = f"({term}) AND {AGING_TERMS}"
    return "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?" + urlencode(
        {
            "db": "pubmed",
            "term": query,
            "retmode": "json",
            "retmax": str(limit),
            "sort": "relevance",
        }
    )


def pubmed_summary_url(ids: list[str]) -> str:
    return "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?" + urlencode(
        {"db": "pubmed", "id": ",".join(ids), "retmode": "json"}
    )


def collect_pubmed(intervention: dict[str, Any], limit: int, delay: float) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    term = intervention["search_terms"][0]
    search_payload, search_meta = request_json(pubmed_query(term, limit))
    run_records = [{"source": "pubmed_search", "intervention_id": intervention["id"], **search_meta}]
    write_json(RAW_DIR / "pubmed" / f"{intervention['id']}_search.json", {"meta": search_meta, "data": search_payload})
    time.sleep(delay)

    ids = []
    if search_payload:
        ids = search_payload.get("esearchresult", {}).get("idlist", [])
    if not ids:
        return [], run_records

    summary_payload, summary_meta = request_json(pubmed_summary_url(ids))
    run_records.append({"source": "pubmed_summary", "intervention_id": intervention["id"], **summary_meta})
    write_json(RAW_DIR / "pubmed" / f"{intervention['id']}_summary.json", {"meta": summary_meta, "data": summary_payload})
    time.sleep(delay)

    records: list[dict[str, Any]] = []
    result = (summary_payload or {}).get("result", {})
    for pmid in result.get("uids", []):
        item = result.get(pmid, {})
        records.append(
            {
                "source": "pubmed",
                "intervention_id": intervention["id"],
                "source_record_id": pmid,
                "title": item.get("title"),
                "journal": item.get("fulljournalname") or item.get("source"),
                "pubdate": item.get("pubdate"),
                "authors": [author.get("name") for author in item.get("authors", []) if author.get("name")],
                "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
                "retrieved_at": summary_meta.get("retrieved_at"),
            }
        )
    return records, run_records


def collect_openalex(intervention: dict[str, Any], limit: int, delay: float) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    term = f"{intervention['search_terms'][0]} aging longevity healthspan"
    url = "https://api.openalex.org/works?" + urlencode(
        {
            "search": term,
            "per-page": str(limit),
            "sort": "relevance_score:desc",
        }
    )
    payload, meta = request_json(url)
    write_json(RAW_DIR / "openalex" / f"{intervention['id']}.json", {"meta": meta, "data": payload})
    time.sleep(delay)

    records: list[dict[str, Any]] = []
    for item in (payload or {}).get("results", []):
        records.append(
            {
                "source": "openalex",
                "intervention_id": intervention["id"],
                "source_record_id": item.get("id"),
                "doi": item.get("doi"),
                "title": item.get("title") or item.get("display_name"),
                "publication_year": item.get("publication_year"),
                "cited_by_count": item.get("cited_by_count"),
                "type": item.get("type"),
                "url": item.get("id"),
                "retrieved_at": meta.get("retrieved_at"),
            }
        )
    return records, [{"source": "openalex", "intervention_id": intervention["id"], **meta}]


def collect_clinicaltrials(intervention: dict[str, Any], limit: int, delay: float) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    term = f"{intervention['search_terms'][0]} aging longevity healthspan"
    url = "https://clinicaltrials.gov/api/v2/studies?" + urlencode(
        {
            "format": "json",
            "query.term": term,
            "pageSize": str(limit),
        }
    )
    payload, meta = request_json(url)
    write_json(RAW_DIR / "clinicaltrials" / f"{intervention['id']}.json", {"meta": meta, "data": payload})
    time.sleep(delay)

    records: list[dict[str, Any]] = []
    for study in (payload or {}).get("studies", []):
        protocol = study.get("protocolSection", {})
        ident = protocol.get("identificationModule", {})
        status = protocol.get("statusModule", {})
        design = protocol.get("designModule", {})
        conditions = protocol.get("conditionsModule", {})
        arms = protocol.get("armsInterventionsModule", {})
        outcomes = protocol.get("outcomesModule", {})
        nct_id = ident.get("nctId")
        records.append(
            {
                "source": "clinicaltrials",
                "intervention_id": intervention["id"],
                "source_record_id": nct_id,
                "title": ident.get("briefTitle") or ident.get("officialTitle"),
                "status": status.get("overallStatus"),
                "phase": design.get("phases"),
                "conditions": conditions.get("conditions", []),
                "interventions": [
                    item.get("name") for item in arms.get("interventions", []) if item.get("name")
                ],
                "primary_outcomes": [
                    item.get("measure") for item in outcomes.get("primaryOutcomes", []) if item.get("measure")
                ],
                "last_update_submit_date": status.get("lastUpdateSubmitDate"),
                "url": f"https://clinicaltrials.gov/study/{nct_id}" if nct_id else None,
                "retrieved_at": meta.get("retrieved_at"),
            }
        )
    return records, [{"source": "clinicaltrials", "intervention_id": intervention["id"], **meta}]


def collect_openfda(intervention: dict[str, Any], limit: int, delay: float) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    query = intervention.get("fda_query")
    if not query:
        return [], []
    url = "https://api.fda.gov/drug/label.json?" + urlencode(
        {
            "search": f'openfda.substance_name:"{query}"',
            "limit": str(limit),
        }
    )
    payload, meta = request_json(url)
    write_json(RAW_DIR / "openfda" / f"{intervention['id']}.json", {"meta": meta, "data": payload})
    time.sleep(delay)

    records: list[dict[str, Any]] = []
    for item in (payload or {}).get("results", []):
        openfda = item.get("openfda", {})
        record_id = item.get("id") or item.get("set_id")
        records.append(
            {
                "source": "openfda_label",
                "intervention_id": intervention["id"],
                "source_record_id": record_id,
                "brand_name": openfda.get("brand_name", []),
                "generic_name": openfda.get("generic_name", []),
                "substance_name": openfda.get("substance_name", []),
                "warnings": item.get("warnings", [])[:2],
                "contraindications": item.get("contraindications", [])[:2],
                "adverse_reactions": item.get("adverse_reactions", [])[:2],
                "effective_time": item.get("effective_time"),
                "url": f"https://api.fda.gov/drug/label.json?search=id:{record_id}" if record_id else None,
                "retrieved_at": meta.get("retrieved_at"),
            }
        )
    return records, [{"source": "openfda_label", "intervention_id": intervention["id"], **meta}]


def reset_outputs() -> None:
    for name in [
        "pubmed_evidence.jsonl",
        "openalex_works.jsonl",
        "clinical_trials.jsonl",
        "safety_labels.jsonl",
        "source_runs.jsonl",
        "collection_summary.json",
    ]:
        path = PROCESSED_DIR / name
        if path.exists():
            path.unlink()


def main() -> int:
    parser = argparse.ArgumentParser(description="采集 Longevity Evidence MVP 公开数据")
    parser.add_argument("--interventions", type=Path, default=DEFAULT_INTERVENTIONS)
    parser.add_argument("--limit", type=int, default=10, help="每个源、每个干预最多拉取的记录数")
    parser.add_argument("--delay", type=float, default=0.34, help="请求间隔秒数")
    parser.add_argument("--only", nargs="*", help="只采集指定 intervention id")
    args = parser.parse_args()

    ensure_dirs()
    reset_outputs()
    interventions = load_interventions(args.interventions)
    if args.only:
        selected = set(args.only)
        interventions = [item for item in interventions if item["id"] in selected]

    summary = {
        "started_at": utc_now(),
        "intervention_count": len(interventions),
        "limit": args.limit,
        "sources": {
            "pubmed": 0,
            "openalex": 0,
            "clinicaltrials": 0,
            "openfda_label": 0,
        },
        "errors": [],
    }

    for intervention in interventions:
        pubmed_records, pubmed_runs = collect_pubmed(intervention, args.limit, args.delay)
        openalex_records, openalex_runs = collect_openalex(intervention, args.limit, args.delay)
        trial_records, trial_runs = collect_clinicaltrials(intervention, args.limit, args.delay)
        safety_records, safety_runs = collect_openfda(intervention, min(args.limit, 25), args.delay)

        append_jsonl(PROCESSED_DIR / "pubmed_evidence.jsonl", pubmed_records)
        append_jsonl(PROCESSED_DIR / "openalex_works.jsonl", openalex_records)
        append_jsonl(PROCESSED_DIR / "clinical_trials.jsonl", trial_records)
        append_jsonl(PROCESSED_DIR / "safety_labels.jsonl", safety_records)
        runs = pubmed_runs + openalex_runs + trial_runs + safety_runs
        append_jsonl(PROCESSED_DIR / "source_runs.jsonl", runs)

        summary["sources"]["pubmed"] += len(pubmed_records)
        summary["sources"]["openalex"] += len(openalex_records)
        summary["sources"]["clinicaltrials"] += len(trial_records)
        summary["sources"]["openfda_label"] += len(safety_records)
        for run in runs:
            if run.get("status") not in (200, "200"):
                summary["errors"].append(run)

    summary["finished_at"] = utc_now()
    write_json(PROCESSED_DIR / "collection_summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
