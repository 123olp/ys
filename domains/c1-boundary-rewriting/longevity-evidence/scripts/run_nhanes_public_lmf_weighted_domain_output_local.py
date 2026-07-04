#!/usr/bin/env python3
"""本地生成 NHANES public-use LMF weighted-domain 输出审计报告。

该脚本是定量模型管线的受控本地运行切片：它下载 CDC/NCHS 公开
NHANES 2017-2018 DEMO 与 public-use LMF 到临时目录，使用 R `survey`
在临时 CSV 上执行 `svydesign` 与 post-design `subset`，最后只把聚合
层面的本地审计报告写入 ignored `build/reports/`。仓库不得持久化行级
数据，也不得把本脚本输出复制进 `web/src/data` 或公开发布。
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import build_nhanes_public_lmf_aggregate_pilot as aggregate_pilot


REPO_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_OUTPUT = (
    REPO_ROOT
    / "build"
    / "reports"
    / "nhanes-public-lmf-weighted-domain-output-local"
    / "validation.json"
)
DEFAULT_RSCRIPT = REPO_ROOT / ".runtime" / "nhanes-r-survey" / "bin" / "Rscript"

ANALYSIS_COLUMNS = [
    "sexLabel",
    "ageBandLabel",
    "mortstat",
    "permthExm",
    "WTMEC2YR",
    "SDMVSTRA",
    "SDMVPSU",
]

R_ANALYSIS_SCRIPT = r"""
suppressPackageStartupMessages(library(survey))
args <- commandArgs(trailingOnly=TRUE)
df <- read.csv(args[1], stringsAsFactors=FALSE)
df$mortstat <- as.numeric(df$mortstat)
design <- svydesign(
  ids=~SDMVPSU,
  strata=~SDMVSTRA,
  weights=~WTMEC2YR,
  data=df,
  nest=TRUE
)
sexes <- c("female", "male")
bands <- c("18-39", "40-59", "60-79", "80+")
rows <- list()
idx <- 1
for (sex_name in sexes) {
  for (band_name in bands) {
    expr <- substitute(
      sexLabel == SEXVALUE & ageBandLabel == BANDVALUE,
      list(SEXVALUE=sex_name, BANDVALUE=band_name)
    )
    domain_design <- subset(design, eval(expr))
    estimate <- svymean(~mortstat, domain_design, na.rm=TRUE)
    interval <- confint(estimate)
    domain_rows <- df[df$sexLabel == sex_name & df$ageBandLabel == band_name,]
    rows[[idx]] <- data.frame(
      sex=sex_name,
      ageBand=band_name,
      weightedMortalityRate=as.numeric(coef(estimate)[1]),
      standardError=as.numeric(SE(estimate)[1]),
      ciLow=as.numeric(interval[1,1]),
      ciHigh=as.numeric(interval[1,2]),
      designDf=degf(domain_design),
      unweightedRecords=nrow(domain_rows),
      unweightedDeaths=sum(domain_rows$mortstat),
      weightSum=sum(domain_rows$WTMEC2YR),
      weightedDeaths=sum(domain_rows$WTMEC2YR * domain_rows$mortstat)
    )
    idx <- idx + 1
  }
}
write.csv(do.call(rbind, rows), args[2], row.names=FALSE, quote=TRUE)
cat(paste0("rVersion=", R.version.string, "\n"))
cat(paste0("surveyVersion=", as.character(packageVersion("survey")), "\n"))
"""


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def repo_rel(path: Path) -> str:
    return str(path.resolve().relative_to(REPO_ROOT))


def round_number(value: float, digits: int = 8) -> float:
    return round(float(value), digits)


def resolve_rscript(candidate: Path | None) -> Path:
    if candidate is not None:
        path = candidate.resolve()
        if not path.exists():
            raise FileNotFoundError(f"Rscript not found: {path}")
        return path
    if DEFAULT_RSCRIPT.exists():
        return DEFAULT_RSCRIPT.resolve()
    found = shutil.which("Rscript")
    if found:
        return Path(found).resolve()
    raise FileNotFoundError(
        "Rscript not found. Run "
        "domains/c1-boundary-rewriting/longevity-evidence/scripts/"
        "run_nhanes_public_lmf_r_survey_controlled_runtime_smoke.sh first."
    )


def build_analysis_csv(lmf_path: Path, demo_path: Path, csv_path: Path) -> dict[str, Any]:
    try:
        import pandas as pd
    except ImportError as exc:  # pragma: no cover - environment guard.
        raise RuntimeError("pandas is required to read NHANES XPT files") from exc

    lmf = pd.DataFrame(aggregate_pilot.parse_lmf(lmf_path))
    demo = pd.read_sas(demo_path, format="xport")
    demo = demo[
        [
            "SEQN",
            "RIDAGEYR",
            "RIAGENDR",
            "WTMEC2YR",
            "SDMVSTRA",
            "SDMVPSU",
        ]
    ].copy()
    demo["SEQN"] = demo["SEQN"].astype(int)

    merged = demo.merge(lmf, on="SEQN", how="inner")
    eligible = merged[
        (merged["eligstat"] == 1)
        & (merged["RIDAGEYR"] >= 18)
        & (merged["WTMEC2YR"] > 0)
    ].copy()
    eligible["sexLabel"] = eligible["RIAGENDR"].astype(int).map(aggregate_pilot.SEX_LABELS)
    eligible["ageBandLabel"] = eligible["RIDAGEYR"].astype(int).map(aggregate_pilot.age_band)
    eligible["mortstat"] = eligible["mortstat"].fillna(0).astype(int)
    eligible["permthExm"] = eligible["permthExm"].fillna(0).astype(float)

    eligible[ANALYSIS_COLUMNS].to_csv(csv_path, index=False)

    psu_per_stratum = eligible.groupby("SDMVSTRA")["SDMVPSU"].nunique()
    return {
        "rawLmfRecordsReadInTemp": int(len(lmf)),
        "rawDemoRecordsReadInTemp": int(len(demo)),
        "joinedRecordsInTemp": int(len(merged)),
        "eligiblePositiveWeightAdultRecordsInTemp": int(len(eligible)),
        "eligiblePositiveWeightAdultDeathsInTemp": int(eligible["mortstat"].sum()),
        "positiveWeightStrataInTemp": int(psu_per_stratum.size),
        "minimumPsuPerPositiveWeightStratumInTemp": int(psu_per_stratum.min()),
        "temporaryAnalysisCsvPersistedAfterRun": False,
    }


def parse_r_stdout(stdout: str) -> dict[str, str]:
    metadata: dict[str, str] = {}
    for line in stdout.splitlines():
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        metadata[key.strip()] = value.strip()
    return metadata


def load_r_rows(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            unweighted_records = int(float(row["unweightedRecords"]))
            unweighted_deaths = int(float(row["unweightedDeaths"]))
            rows.append(
                {
                    "sex": row["sex"],
                    "ageBand": row["ageBand"],
                    "weightedMortalityRate": round_number(float(row["weightedMortalityRate"])),
                    "standardError": round_number(float(row["standardError"])),
                    "confidenceInterval95": {
                        "method": "R survey svymean normal confint; interval is not bounded to [0, 1]",
                        "lower": round_number(float(row["ciLow"])),
                        "upper": round_number(float(row["ciHigh"])),
                    },
                    "domainDof": int(float(row["designDf"])),
                    "localQualityFlags": {
                        "minimumUnweightedCellRuleMet": unweighted_records
                        >= aggregate_pilot.MIN_CELL_COUNT,
                        "hasObservedDeaths": unweighted_deaths > 0,
                    },
                    "publicReleaseStatus": "blocked-local-only-not-disclosure-reviewed",
                }
            )
    return rows


def build_output(rscript: Path) -> dict[str, Any]:
    with tempfile.TemporaryDirectory() as temp_dir:
        temp = Path(temp_dir)
        lmf_path = temp / "NHANES_2017_2018_MORT_2019_PUBLIC.dat"
        demo_path = temp / "DEMO_J.XPT"
        readin_path = temp / "R_ReadInProgramAllSurveys.R"
        analysis_csv = temp / "analysis_input.csv"
        r_output_csv = temp / "weighted_domain_output.csv"
        r_program = temp / "weighted_domain_output.R"

        aggregate_pilot.download(aggregate_pilot.NHANES_2017_2018_LMF_URL, lmf_path)
        aggregate_pilot.download(aggregate_pilot.NHANES_2017_2018_DEMO_URL, demo_path)
        aggregate_pilot.download(aggregate_pilot.CDC_LMF_READIN_R_URL, readin_path)
        temp_diagnostics = build_analysis_csv(lmf_path, demo_path, analysis_csv)
        r_program.write_text(R_ANALYSIS_SCRIPT, encoding="utf-8")

        completed = subprocess.run(
            [str(rscript), str(r_program), str(analysis_csv), str(r_output_csv)],
            check=False,
            capture_output=True,
            text=True,
        )
        if completed.returncode != 0:
            raise RuntimeError(
                "R weighted-domain output failed with exit code "
                f"{completed.returncode}:\n{completed.stderr}"
            )

        source_hashes = {
            "nhanesPublicLmf2017_2018Sha256": aggregate_pilot.sha256_file(lmf_path),
            "nhanesDemo2017_2018Sha256": aggregate_pilot.sha256_file(demo_path),
            "cdcRReadInProgramSha256": aggregate_pilot.sha256_file(readin_path),
            "localRAnalysisProgramSha256": sha256_text(R_ANALYSIS_SCRIPT),
        }
        rows = load_r_rows(r_output_csv)
        r_metadata = parse_r_stdout(completed.stdout)

    return {
        "schemaVersion": "human-infra.nhanes-public-lmf-weighted-domain-output-local-run.v1",
        "status": "local-real-weighted-domain-output-generated-not-public-not-reviewed",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "sourceId": "nhanes-public-lmf-2017-2018",
        "sourceAuthority": "CDC/NCHS public-use NHANES Linked Mortality File",
        "outputScope": {
            "storageClass": "ignored-local-build-report",
            "defaultPath": repo_rel(DEFAULT_OUTPUT),
            "publicExportAllowed": False,
            "webDataWritten": False,
            "trackedArtifactAllowed": False,
            "rawRowsPersistedAfterRun": False,
            "temporaryAnalysisCsvPersistedAfterRun": False,
        },
        "sourceUrls": {
            "linkedMortalityPage": aggregate_pilot.CDC_LMF_PAGE_URL,
            "fileDescription": aggregate_pilot.CDC_LMF_DESCRIPTION_URL,
            "dataDictionary": aggregate_pilot.CDC_LMF_DICTIONARY_URL,
            "rReadInProgram": aggregate_pilot.CDC_LMF_READIN_R_URL,
            "nhanes2017_2018PublicLmf": aggregate_pilot.NHANES_2017_2018_LMF_URL,
            "nhanes2017_2018DemoXpt": aggregate_pilot.NHANES_2017_2018_DEMO_URL,
            "nhanes2017_2018DemoDocumentation": aggregate_pilot.NHANES_2017_2018_DEMO_DOC_URL,
        },
        "sourceHashes": source_hashes,
        "runtime": {
            "rscriptPath": str(rscript),
            "rVersion": r_metadata.get("rVersion"),
            "surveyVersion": r_metadata.get("surveyVersion"),
            "estimatorBackend": "R survey",
            "designFunction": "svydesign",
            "domainSubsettingFunction": "survey::subset",
            "varianceMethod": "Taylor linearization",
            "domainIndicatorTiming": "post-design subset via survey::subset",
            "rowDropBeforeDesign": False,
        },
        "temporaryInputDiagnostics": temp_diagnostics,
        "modelUseBoundary": {
            "containsRealNhanesPublicUseData": True,
            "containsRealWeightedRates": True,
            "containsRealDesignBasedIntervals": True,
            "containsRowLevelData": False,
            "containsIdentifiers": False,
            "containsExactDomainCountsInOutput": False,
            "publicOutputDisclosureReviewComplete": False,
            "realPublicationReliabilityReviewComplete": False,
            "publicWeightedDomainOutputAllowed": False,
            "calibrationAllowed": False,
            "individualPredictionAllowed": False,
            "medicalAdviceAllowed": False,
            "blockedUses": [
                "public weighted-domain mortality publication",
                "public design-based confidence interval release",
                "calibrated Human Infra prediction",
                "intervention effect estimation",
                "causal claim",
                "individual prediction",
                "individual death-date output",
                "medical advice",
            ],
        },
        "weightedDomainOutput": {
            "cellCount": len(rows),
            "grouping": ["sex", "ageBand"],
            "cells": rows,
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--rscript", type=Path, default=None)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output_path = args.out.resolve()
    rscript = resolve_rscript(args.rscript)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output = build_output(rscript)
    output["outputScope"]["actualPath"] = repo_rel(output_path)
    with output_path.open("w", encoding="utf-8") as handle:
        json.dump(output, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(f"wrote {repo_rel(output_path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
