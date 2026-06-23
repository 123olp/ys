#!/usr/bin/env python3
"""采集 Longevity Evidence 的核心基础数据源。

覆盖范围：
- HAGR / GenAge / LongevityMap / DrugAge 官方快照。
- PubChem 化合物实体信息。
- openFDA 药品标签、不良事件聚合和 Drugs@FDA 信息。
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import time
import zipfile
from datetime import UTC, datetime
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
INTERVENTIONS_PATH = ROOT / "data" / "manual" / "interventions.json"
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"
USER_AGENT = "HumanInfra-LongevityEvidence/0.1 (public evidence research; contact: local)"

HAGR_SOURCES = [
    {
        "id": "drugage",
        "url": "https://hagr.ageing-map.org/drugs/dataset.zip",
        "description": "DrugAge 药物和寿命实验数据",
    },
    {
        "id": "genage_human",
        "url": "https://hagr.ageing-map.org/genes/human_genes.zip",
        "description": "GenAge human aging genes",
    },
    {
        "id": "genage_models",
        "url": "https://hagr.ageing-map.org/genes/models_genes.zip",
        "description": "GenAge model organism aging genes",
    },
    {
        "id": "longevitymap",
        "url": "https://hagr.ageing-map.org/longevity/longevity_genes.zip",
        "description": "LongevityMap longevity-associated genes",
    },
]


def utc_now() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat()


def ensure_dirs() -> None:
    for path in [
        RAW_DIR / "hagr",
        RAW_DIR / "pubchem",
        RAW_DIR / "openfda_event",
        RAW_DIR / "drugsfda",
        PROCESSED_DIR / "hagr",
    ]:
        path.mkdir(parents=True, exist_ok=True)


def load_interventions() -> list[dict[str, Any]]:
    with INTERVENTIONS_PATH.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def request_bytes(url: str, timeout: int = 60, retries: int = 2, accept: str = "application/json") -> tuple[bytes | None, dict[str, Any]]:
    started = time.time()
    last_meta: dict[str, Any] = {}
    for attempt in range(retries + 1):
        request = Request(
            url,
            headers={
                "User-Agent": USER_AGENT,
                "Accept": accept,
            },
        )
        try:
            with urlopen(request, timeout=timeout) as response:
                body = response.read()
                return body, {
                    "url": url,
                    "status": response.status,
                    "content_type": response.headers.get("content-type"),
                    "retrieved_at": utc_now(),
                    "elapsed_ms": round((time.time() - started) * 1000),
                    "attempts": attempt + 1,
                    "size": len(body),
                    "raw_hash": hashlib.sha256(body).hexdigest(),
                }
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


def request_json(url: str, timeout: int = 60, retries: int = 2) -> tuple[dict[str, Any] | None, dict[str, Any]]:
    body, meta = request_bytes(url, timeout=timeout, retries=retries, accept="application/json")
    if body is None:
        return None, meta
    try:
        return json.loads(body.decode("utf-8")), meta
    except json.JSONDecodeError as exc:
        meta["status"] = "json_decode_error"
        meta["error"] = str(exc)
        return None, meta


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")


def write_jsonl(path: Path, records: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")


def count_csv_rows(path: Path) -> int:
    with path.open("r", encoding="utf-8", errors="replace", newline="") as handle:
        reader = csv.reader(handle)
        next(reader, None)
        return sum(1 for _ in reader)


def collect_hagr() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    records: list[dict[str, Any]] = []
    runs: list[dict[str, Any]] = []
    for source in HAGR_SOURCES:
        body, meta = request_bytes(
            source["url"],
            timeout=120,
            accept="application/zip,application/octet-stream,*/*",
        )
        run = {"source": "hagr", "source_id": source["id"], **meta}
        runs.append(run)
        if body is None:
            continue

        zip_path = RAW_DIR / "hagr" / f"{source['id']}.zip"
        zip_path.write_bytes(body)
        extract_dir = PROCESSED_DIR / "hagr" / source["id"]
        extract_dir.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(zip_path) as archive:
            archive.extractall(extract_dir)
            members = archive.namelist()

        csv_files = [path for path in extract_dir.rglob("*.csv")]
        row_count = sum(count_csv_rows(path) for path in csv_files)
        records.append(
            {
                "source": "hagr",
                "source_id": source["id"],
                "description": source["description"],
                "url": source["url"],
                "zip_path": str(zip_path.relative_to(ROOT)),
                "extracted_files": [str((extract_dir / member).relative_to(ROOT)) for member in members],
                "csv_files": [str(path.relative_to(ROOT)) for path in csv_files],
                "row_count": row_count,
                "retrieved_at": meta.get("retrieved_at"),
                "raw_hash": meta.get("raw_hash"),
            }
        )
        time.sleep(0.5)
    return records, runs


def pubchem_name(intervention: dict[str, Any]) -> str | None:
    if intervention.get("fda_query"):
        return intervention["fda_query"]
    if intervention["category"] in {"drug", "supplement", "metabolite"}:
        return intervention["search_terms"][0]
    return None


def collect_pubchem(interventions: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    records: list[dict[str, Any]] = []
    runs: list[dict[str, Any]] = []
    props = "MolecularFormula,MolecularWeight,CanonicalSMILES,IsomericSMILES,InChIKey,IUPACName"
    for intervention in interventions:
        name = pubchem_name(intervention)
        if not name:
            continue
        url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{quote(name)}/property/{props}/JSON"
        payload, meta = request_json(url)
        runs.append({"source": "pubchem", "intervention_id": intervention["id"], **meta})
        write_json(RAW_DIR / "pubchem" / f"{intervention['id']}.json", {"meta": meta, "data": payload})
        for item in (payload or {}).get("PropertyTable", {}).get("Properties", []):
            records.append(
                {
                    "source": "pubchem",
                    "intervention_id": intervention["id"],
                    "query_name": name,
                    "cid": item.get("CID"),
                    "molecular_formula": item.get("MolecularFormula"),
                    "molecular_weight": item.get("MolecularWeight"),
                    "canonical_smiles": item.get("CanonicalSMILES") or item.get("ConnectivitySMILES"),
                    "isomeric_smiles": item.get("IsomericSMILES"),
                    "inchi_key": item.get("InChIKey"),
                    "iupac_name": item.get("IUPACName"),
                    "url": f"https://pubchem.ncbi.nlm.nih.gov/compound/{item.get('CID')}" if item.get("CID") else None,
                    "retrieved_at": meta.get("retrieved_at"),
                }
            )
        time.sleep(0.25)
    return records, runs


def collect_openfda_events(interventions: list[dict[str, Any]], limit: int) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    records: list[dict[str, Any]] = []
    runs: list[dict[str, Any]] = []
    for intervention in interventions:
        query = intervention.get("fda_query")
        if not query:
            continue
        params = {
            "search": f'patient.drug.openfda.substance_name:"{query}"',
            "count": "patient.reaction.reactionmeddrapt.exact",
            "limit": str(limit),
        }
        url = "https://api.fda.gov/drug/event.json?" + urlencode(params)
        payload, meta = request_json(url)
        runs.append({"source": "openfda_event", "intervention_id": intervention["id"], **meta})
        write_json(RAW_DIR / "openfda_event" / f"{intervention['id']}.json", {"meta": meta, "data": payload})
        for item in (payload or {}).get("results", []):
            records.append(
                {
                    "source": "openfda_event",
                    "intervention_id": intervention["id"],
                    "reaction": item.get("term"),
                    "count": item.get("count"),
                    "retrieved_at": meta.get("retrieved_at"),
                }
            )
        time.sleep(0.25)
    return records, runs


def collect_drugsfda(interventions: list[dict[str, Any]], limit: int) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    records: list[dict[str, Any]] = []
    runs: list[dict[str, Any]] = []
    for intervention in interventions:
        query = intervention.get("fda_query")
        if not query:
            continue
        params = {
            "search": f'products.active_ingredients.name:"{query}"',
            "limit": str(limit),
        }
        url = "https://api.fda.gov/drug/drugsfda.json?" + urlencode(params)
        payload, meta = request_json(url)
        runs.append({"source": "drugsfda", "intervention_id": intervention["id"], **meta})
        write_json(RAW_DIR / "drugsfda" / f"{intervention['id']}.json", {"meta": meta, "data": payload})
        for item in (payload or {}).get("results", []):
            records.append(
                {
                    "source": "drugsfda",
                    "intervention_id": intervention["id"],
                    "application_number": item.get("application_number"),
                    "sponsor_name": item.get("sponsor_name"),
                    "products": [
                        {
                            "brand_name": product.get("brand_name"),
                            "dosage_form": product.get("dosage_form"),
                            "route": product.get("route"),
                            "marketing_status": product.get("marketing_status"),
                            "active_ingredients": product.get("active_ingredients", []),
                        }
                        for product in item.get("products", [])
                    ],
                    "submissions": [
                        {
                            "submission_type": submission.get("submission_type"),
                            "submission_status": submission.get("submission_status"),
                            "submission_status_date": submission.get("submission_status_date"),
                        }
                        for submission in item.get("submissions", [])[:5]
                    ],
                    "retrieved_at": meta.get("retrieved_at"),
                }
            )
        time.sleep(0.25)
    return records, runs


def main() -> int:
    parser = argparse.ArgumentParser(description="采集 Longevity Evidence 核心基础数据源")
    parser.add_argument("--event-limit", type=int, default=20)
    parser.add_argument("--drugsfda-limit", type=int, default=10)
    args = parser.parse_args()

    ensure_dirs()
    interventions = load_interventions()

    hagr_records, hagr_runs = collect_hagr()
    pubchem_records, pubchem_runs = collect_pubchem(interventions)
    event_records, event_runs = collect_openfda_events(interventions, args.event_limit)
    drugsfda_records, drugsfda_runs = collect_drugsfda(interventions, args.drugsfda_limit)
    runs = hagr_runs + pubchem_runs + event_runs + drugsfda_runs

    write_jsonl(PROCESSED_DIR / "hagr_snapshots.jsonl", hagr_records)
    write_jsonl(PROCESSED_DIR / "pubchem_compounds.jsonl", pubchem_records)
    write_jsonl(PROCESSED_DIR / "openfda_event_counts.jsonl", event_records)
    write_jsonl(PROCESSED_DIR / "drugsfda_applications.jsonl", drugsfda_records)
    write_jsonl(PROCESSED_DIR / "core_source_runs.jsonl", runs)

    summary = {
        "started_and_finished_at": utc_now(),
        "sources": {
            "hagr_snapshots": len(hagr_records),
            "pubchem_compounds": len(pubchem_records),
            "openfda_event_counts": len(event_records),
            "drugsfda_applications": len(drugsfda_records),
        },
        "errors": [run for run in runs if run.get("status") not in (200, "200")],
    }
    write_json(PROCESSED_DIR / "core_collection_summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
