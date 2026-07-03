#!/usr/bin/env python3
"""生成 NHANES public-use LMF 聚合试运行数据。

该脚本只把 CDC/NCHS 公开 NHANES 2017-2018 DEMO 文件和 2019
public-use Linked Mortality File 下载到临时目录，按 SEQN 做内存内连接，
然后写出 sex × age band 粗聚合单元。仓库不得持久化任何行级数据。
"""

from __future__ import annotations

import argparse
import hashlib
import json
import tempfile
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_OUTPUT = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
    / "life_path_nhanes_public_lmf_aggregate_pilot.json"
)

CDC_LMF_PAGE_URL = "https://www.cdc.gov/nchs/linked-data/mortality-files/index.html"
CDC_LMF_DESCRIPTION_URL = (
    "https://www.cdc.gov/nchs/data/datalinkage/"
    "public-use-linked-mortality-file-description.pdf"
)
CDC_LMF_DICTIONARY_URL = (
    "https://www.cdc.gov/nchs/data/datalinkage/"
    "public-use-linked-mortality-files-data-dictionary.pdf"
)
CDC_LMF_READIN_R_URL = (
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/datalinkage/"
    "linked_mortality/R_ReadInProgramAllSurveys.R"
)
NHANES_2017_2018_LMF_URL = (
    "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/datalinkage/"
    "linked_mortality/NHANES_2017_2018_MORT_2019_PUBLIC.dat"
)
NHANES_2017_2018_DEMO_URL = (
    "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/DEMO_J.XPT"
)
NHANES_2017_2018_DEMO_DOC_URL = (
    "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/DEMO_J.htm"
)

MIN_CELL_COUNT = 20
AGE_BANDS = [
    ("18-39", 18, 39),
    ("40-59", 40, 59),
    ("60-79", 60, 79),
    ("80+", 80, 150),
]
SEX_LABELS = {1: "male", 2: "female"}


def download(url: str, destination: Path) -> None:
    request = urllib.request.Request(url, headers={"User-Agent": "HumanInfraResearch/0.1"})
    with urllib.request.urlopen(request, timeout=60) as response:  # noqa: S310 - public CDC URL.
        destination.write_bytes(response.read())


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_int(text: str) -> int | None:
    value = text.strip()
    if value in {"", ".", ".."}:
        return None
    return int(value)


def parse_lmf(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue

        def field(start: int, end: int) -> str:
            return line[start - 1 : end]

        rows.append(
            {
                "SEQN": parse_int(field(1, 6)),
                "eligstat": parse_int(field(15, 15)),
                "mortstat": parse_int(field(16, 16)),
                "ucodLeading": field(17, 19).strip() or None,
                "diabetes": parse_int(field(20, 20)),
                "hyperten": parse_int(field(21, 21)),
                "permthInt": parse_int(field(43, 45)),
                "permthExm": parse_int(field(46, 48)),
            }
        )
    return rows


def age_band(age: int) -> str:
    for label, lower, upper in AGE_BANDS:
        if lower <= age <= upper:
            return label
    raise ValueError(f"age out of configured bands: {age}")


def round_number(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def build_aggregate(lmf_path: Path, demo_path: Path) -> dict[str, Any]:
    try:
        import pandas as pd
    except ImportError as exc:  # pragma: no cover - environment guard.
        raise RuntimeError("pandas is required to read NHANES XPT files") from exc

    lmf = pd.DataFrame(parse_lmf(lmf_path))
    demo = pd.read_sas(demo_path, format="xport")
    demo = demo[
        [
            "SEQN",
            "RIDAGEYR",
            "RIAGENDR",
            "RIDRETH3",
            "WTMEC2YR",
            "SDMVSTRA",
            "SDMVPSU",
        ]
    ].copy()
    demo["SEQN"] = demo["SEQN"].astype(int)

    merged = demo.merge(lmf, on="SEQN", how="inner")
    eligible = merged[(merged["eligstat"] == 1) & (merged["RIDAGEYR"] >= 18)].copy()
    eligible["sex"] = eligible["RIAGENDR"].astype(int).map(SEX_LABELS)
    eligible["ageBand"] = eligible["RIDAGEYR"].astype(int).map(age_band)
    eligible["mortstat"] = eligible["mortstat"].fillna(0).astype(int)
    eligible["permthExm"] = eligible["permthExm"].fillna(0).astype(float)

    cells: list[dict[str, Any]] = []
    for (sex, band), group in eligible.groupby(["sex", "ageBand"], sort=True):
        records = int(len(group))
        deaths = int(group["mortstat"].sum())
        suppressed = records < MIN_CELL_COUNT
        cell: dict[str, Any] = {
            "sex": sex,
            "ageBand": band,
            "records": records,
            "suppressed": suppressed,
        }
        if not suppressed:
            person_months = float(group["permthExm"].sum())
            cell.update(
                {
                    "deaths": deaths,
                    "assumedAlive": records - deaths,
                    "personMonthsExamTotal": round_number(person_months, 3),
                    "meanFollowupYearsExam": round_number(person_months / records / 12),
                    "unweightedMortalityFraction": round_number(deaths / records),
                    "mecWeightSumDiagnostic": round_number(float(group["WTMEC2YR"].sum()), 3),
                    "mecWeightedDeathCountDiagnostic": round_number(
                        float((group["WTMEC2YR"] * group["mortstat"]).sum()),
                        3,
                    ),
                }
            )
        cells.append(cell)

    return {
        "rawLmfRecordsReadInTemp": int(len(lmf)),
        "rawDemoRecordsReadInTemp": int(len(demo)),
        "joinedRecordsInTemp": int(len(merged)),
        "eligibleAdultRecordsInTemp": int(len(eligible)),
        "eligibleAdultDeaths": int(eligible["mortstat"].sum()),
        "aggregateCells": cells,
    }


def build_output() -> dict[str, Any]:
    with tempfile.TemporaryDirectory() as temp_dir:
        temp = Path(temp_dir)
        lmf_path = temp / "NHANES_2017_2018_MORT_2019_PUBLIC.dat"
        demo_path = temp / "DEMO_J.XPT"
        readin_path = temp / "R_ReadInProgramAllSurveys.R"
        download(NHANES_2017_2018_LMF_URL, lmf_path)
        download(NHANES_2017_2018_DEMO_URL, demo_path)
        download(CDC_LMF_READIN_R_URL, readin_path)
        aggregate = build_aggregate(lmf_path, demo_path)
        source_hashes = {
            "nhanesPublicLmf2017_2018Sha256": sha256_file(lmf_path),
            "nhanesDemo2017_2018Sha256": sha256_file(demo_path),
            "cdcRReadInProgramSha256": sha256_file(readin_path),
        }

    return {
        "schemaVersion": "human-infra.nhanes-public-lmf-aggregate-pilot.v1",
        "status": "public-real-data-aggregate-pilot-not-weighted-not-calibrated",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "sourceAuthority": "CDC/NCHS public-use NHANES Linked Mortality File",
        "sourceUrls": {
            "linkedMortalityPage": CDC_LMF_PAGE_URL,
            "fileDescription": CDC_LMF_DESCRIPTION_URL,
            "dataDictionary": CDC_LMF_DICTIONARY_URL,
            "rReadInProgram": CDC_LMF_READIN_R_URL,
            "nhanes2017_2018PublicLmf": NHANES_2017_2018_LMF_URL,
            "nhanes2017_2018DemoXpt": NHANES_2017_2018_DEMO_URL,
            "nhanes2017_2018DemoDocumentation": NHANES_2017_2018_DEMO_DOC_URL,
        },
        "sourceHashes": source_hashes,
        "scope": {
            "survey": "NHANES",
            "cycle": "2017-2018",
            "mortalityFollowupRelease": "2019 public-use LMF",
            "population": "public-use eligible adults with DEMO and LMF join",
            "joinKey": "SEQN",
            "outcome": "all-cause final mortality status from public-use LMF",
            "timeAtRisk": "PERMTH_EXM public-use follow-up months from MEC exam",
            "grouping": ["sex", "ageBand"],
            "minimumCellCount": MIN_CELL_COUNT,
        },
        "lmfFixedWidthContract": {
            "seqn": "columns 1-6",
            "eligstat": "column 15",
            "mortstat": "column 16",
            "ucodLeading": "columns 17-19",
            "diabetes": "column 20",
            "hyperten": "column 21",
            "permthInt": "columns 43-45",
            "permthExm": "columns 46-48",
        },
        "modelUseBoundary": {
            "allowedUses": [
                "aggregate-only public real-data pilot",
                "pipeline join and aggregation smoke test",
                "model admission boundary testing",
                "baseline mortality endpoint feasibility check",
            ],
            "blockedUses": [
                "individual prediction",
                "individual death-date output",
                "medical advice",
                "calibrated Human Infra prediction",
                "intervention effect estimation",
                "causal claim",
                "survey-population inference",
                "small-cell public export",
            ],
            "rawRowsPersisted": False,
            "individualRowsInOutput": False,
            "surveyVarianceEstimated": False,
            "weightedPopulationEstimateClaimed": False,
            "calibrationClaimed": False,
        },
        "aggregate": aggregate,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output_path = args.out.resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output = build_output()
    with output_path.open("w", encoding="utf-8") as handle:
        json.dump(output, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(f"wrote {output_path.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
