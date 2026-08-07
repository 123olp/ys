#!/usr/bin/env python3
"""Fetch Crossref candidates for history timeline batches.

The config file defines one round per object with a targeted query. The script
applies journal allowlists, publication-year bounds, keyword checks, and DOI
deduplication before emitting a batch JSON for human review.
"""

from __future__ import annotations

import argparse
import json
import time
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "docs" / "reference" / "history-timeline"

JOURNAL_ALLOWLIST = {
    "nature aging",
    "nature medicine",
    "nature communications",
    "nature biotechnology",
    "nature reviews drug discovery",
    "nature reviews genetics",
    "nature reviews molecular cell biology",
    "nature neuroscience",
    "nature metabolism",
    "nature methods",
    "nature biomedical engineering",
    "nature electronics",
    "nature computational science",
    "nature",
    "npj aging",
    "npj regenerative medicine",
    "npj digital medicine",
    "npj mental health research",
    "lancet healthy longevity",
    "science translational medicine",
    "science",
    "science advances",
    "cell",
    "cell stem cell",
    "cell reports medicine",
    "cell reports",
    "cell reports methods",
    "cell metabolism",
    "developmental cell",
    "neuron",
    "molecular cell",
    "cell discovery",
    "protein & cell",
    "jama",
    "jama network open",
    "geroscience",
    "aging cell",
    "aging and disease",
    "frontiers in aging",
    "frontiers in aging neuroscience",
    "frontiers in immunology",
    "elife",
    "plos medicine",
    "the journals of gerontology series a",
    "journals of gerontology series a",
    "journal of the american geriatrics society",
    "ageing research reviews",
    "mechanisms of ageing and development",
    "experimental gerontology",
    "gerontology",
    "biogerontology",
    "rejuvenation research",
    "healthy longevity and clinical medicine",
    "human reproduction",
    "human reproduction update",
    "fertility and sterility",
    "cryobiology",
    "biopreservation and biobanking",
    "stem cell reports",
    "stem cells translational medicine",
    "stem cells",
    "biomaterials",
    "advanced science",
    "advanced materials",
    "advanced healthcare materials",
    "acs nano",
    "nano letters",
    "journal of controlled release",
    "iscience",
    "molecular neurodegeneration",
    "alzheimer's & dementia",
    "neurobiology of aging",
    "brain stimulation",
    "journal of neural engineering",
    "ieee transactions on neural systems and rehabilitation engineering",
    "ieee transactions on biomedical engineering",
    "journal of neuroengineering and rehabilitation",
    "artificial organs",
    "american journal of transplantation",
    "xenotransplantation",
    "journal of assisted reproduction and genetics",
    "reproductive biomedicine online",
    "pnas",
    "pnas nexus",
    "embo molecular medicine",
    "signal transduction and targeted therapy",
    "trends in molecular medicine",
    "trends in cell biology",
    "annual review of biomedical engineering",
    "nature reviews bioengineering",
    "lancet",
    "the lancet",
    "lancet public health",
    "the lancet public health",
    "lancet neurology",
    "the lancet neurology",
    "lancet diabetes & endocrinology",
    "the lancet diabetes & endocrinology",
    "lancet respiratory medicine",
    "the lancet respiratory medicine",
    "bmj",
    "bmj open",
    "british medical journal",
    "jama internal medicine",
    "jama neurology",
    "jama cardiology",
    "jama psychiatry",
    "jama pediatrics",
    "jama surgery",
    "annals of internal medicine",
    "new england journal of medicine",
    "nature reviews neuroscience",
    "nature reviews neurology",
    "nature reviews immunology",
    "nature reviews endocrinology",
    "nature reviews cardiology",
    "nature reviews nephrology",
    "nature reviews gastroenterology & hepatology",
    "nature reviews cancer",
    "nature reviews microbiology",
    "nature reviews aging",
    "nature immunology",
    "immunity",
    "journal of experimental medicine",
    "journal of immunology",
    "clinical immunology",
    "brain",
    "brain communications",
    "brain research",
    "journal of neuroscience",
    "neuroscience",
    "neurobiology of disease",
    "movement disorders",
    "journal of neurology",
    "journal of neurology, neurosurgery & psychiatry",
    "journal of neurotrauma",
    "neurorehabilitation and neural repair",
    "restorative neurology and neuroscience",
    "journal of cerebral blood flow & metabolism",
    "fluids and barriers of the cns",
    "sleep",
    "sleep medicine",
    "journal of sleep research",
    "npj biological timing and sleep",
    "chronic obstructive pulmonary diseases",
    "journal of applied physiology",
    "american journal of respiratory and critical care medicine",
    "thorax",
    "chest",
    "circulation",
    "circulation research",
    "european heart journal",
    "journal of the american college of cardiology",
    "hypertension",
    "arteriosclerosis, thrombosis, and vascular biology",
    "journal of thrombosis and haemostasis",
    "kidney international",
    "journal of the american society of nephrology",
    "nephrology dialysis transplantation",
    "hepatology",
    "journal of hepatology",
    "gastroenterology",
    "gut",
    "cell host & microbe",
    "mucosal immunology",
    "diabetes",
    "diabetologia",
    "metabolism",
    "molecular metabolism",
    "endocrinology",
    "journal of clinical endocrinology & metabolism",
    "thyroid",
    "blood",
    "leukemia",
    "haematologica",
    "vaccine",
    "npj vaccines",
    "bone",
    "journal of bone and mineral research",
    "calcified tissue international",
    "osteoarthritis and cartilage",
    "connective tissue research",
    "journal of orthopaedic research",
    "journal of dental research",
    "oral diseases",
    "clinical oral investigations",
    "journal of clinical periodontology",
    "periodontology 2000",
    "american journal of clinical nutrition",
    "journal of nutrition",
    "nutrients",
    "obesity",
    "international journal of epidemiology",
    "american journal of epidemiology",
    "social science & medicine",
    "psychosomatic medicine",
    "health psychology",
    "journals of gerontology series b",
    "the gerontologist",
    "innovation in aging",
    "age and ageing",
    "archives of physical medicine and rehabilitation",
    "journal of rehabilitation medicine",
    "physical therapy",
    "journal of biomechanics",
    "clinical biomechanics",
    "reproductive sciences",
    "menopause",
    "aging",
    "aging (albany ny)",
    "international journal of molecular sciences",
    "biomedicines",
    "cells",
    "biology",
    "frontiers in physiology",
    "frontiers in neuroscience",
    "frontiers in neurology",
    "frontiers in cellular neuroscience",
    "frontiers in human neuroscience",
    "frontiers in endocrinology",
    "frontiers in nutrition",
    "frontiers in medicine",
    "frontiers in public health",
    "frontiers in cell and developmental biology",
    "frontiers in molecular neuroscience",
    "frontiers in pharmacology",
    "frontiers in aging neuroscience",
    "npj healthy longevity",
    "healthy longevity",
    "longevity & healthspan",
}

EXCLUDE_WORDS = {
    "editorial",
    "correction",
    "erratum",
    "comment",
    "news",
    "retraction",
    "letter to the editor",
    "fossil",
    "webcast",
}


def matches_journal(container: str) -> bool:
    normalized = container.lower().strip()
    return normalized in JOURNAL_ALLOWLIST


def crossref(query: str, min_year: int = 1990, rows: int = 40) -> list[dict]:
    params = {
        "query.title": query,
        "rows": str(rows),
        "filter": f"type:journal-article,from-pub-date:{min_year}-01-01",
        "select": "DOI,title,container-title,issued,type,score",
        "mailto": "human-infra@tradecatlabs.com",
    }
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode(params)
    request = urllib.request.Request(url, headers={"User-Agent": "HumanInfraTimeline/1.0 (mailto:human-infra@tradecatlabs.com)"})
    last_error: Exception | None = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=45) as response:
                return json.loads(response.read().decode("utf-8"))["message"]["items"]
        except Exception as exc:  # network or Crossref transient failure
            last_error = exc
            if attempt < 2:
                time.sleep(2 * (attempt + 1))
    raise last_error


def clean_label(title: str) -> str:
    return " ".join(title.split())


def matches_keywords(title: str, keywords: list[str], required_terms: list[str]) -> bool:
    lowered = title.lower()
    hits = sum(1 for keyword in keywords if keyword.lower() in lowered)
    required_hits = sum(1 for term in required_terms if term.lower() in lowered)
    return required_hits >= 1 and hits >= 2


def existing_dois() -> set[str]:
    sources = json.loads((PACKAGE / "sources.json").read_text(encoding="utf-8"))
    return {source.get("doi") for source in sources["sources"] if source.get("doi")}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()

    config = json.loads(args.config.read_text(encoding="utf-8"))
    seen = existing_dois()
    items: list[dict] = []

    for round_spec in config["rounds"]:
        queries = round_spec.get("queries", [round_spec["query"]])
        keyword_min_hits = round_spec.get("keyword_min_hits", 2)
        min_year = round_spec.get("min_year", 2023)
        results = []
        for query in queries:
            results.extend(crossref(query, min_year=min_year))
            time.sleep(0.4)
        selected = []
        candidate_pool: list[dict] = []
        for result in results:
            doi = result.get("DOI", "")
            title = clean_label((result.get("title") or [""])[0])
            container = clean_label((result.get("container-title") or [""])[0])
            year = result.get("issued", {}).get("date-parts", [[None]])[0][0]
            score = result.get("score", 0)
            if not doi or not title or not container or not year:
                continue
            if doi in seen:
                continue
            if any(word in title.lower() for word in EXCLUDE_WORDS):
                continue
            if not matches_journal(container):
                continue
            if year < min_year:
                continue
            if score < 1:
                continue
            if not matches_keywords(
                title,
                round_spec["keywords"],
                round_spec.get("required_terms", [round_spec["keywords"][0]]),
            ):
                continue
            candidate_pool.append(
                {
                    "round": round_spec["round"],
                    "topic": round_spec["topic"],
                    "chapter": round_spec["chapter"],
                    "path_family": round_spec["path_family"],
                    "event_type": round_spec["event_type"],
                    "evidence_grade": round_spec.get("evidence_grade", "S"),
                    "significance": round_spec.get("significance", "medium"),
                    "label": title,
                    "url": f"https://doi.org/{doi}",
                    "doi": doi,
                    "date_start": str(year),
                    "date_type": "approx",
                    "source_note": f"{container}；Crossref/DOI 元数据核验。",
                    "claim": round_spec["claim_template"].format(topic=round_spec["topic"], title=title),
                    "summary": round_spec["summary_template"].format(topic=round_spec["topic"], title=title),
                    "uncertainty": round_spec.get("uncertainty", "本记录基于期刊元数据和论文标题，尚未完成全文语境复核。"),
                    "title": f"《{title}》论文发表",
                }
            )

        # Deduplicate titles while preserving Crossref relevance order.
        seen_titles: set[str] = set()
        for candidate in candidate_pool:
            normalized = candidate["label"].lower()
            if normalized in seen_titles:
                continue
            seen_titles.add(normalized)
            seen.add(candidate["doi"])
            selected.append(candidate)
            if len(selected) >= 5:
                break

        if len(selected) < 5:
            print(
                f"warn round={round_spec['round']} selected={len(selected)} "
                f"query={queries[0]}"
            )
        items.extend(selected)
        time.sleep(0.5)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(
        json.dumps({"items": items}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        f"status=OK total={len(items)} rounds={len(config['rounds'])} "
        f"out={args.out}"
    )


if __name__ == "__main__":
    main()
