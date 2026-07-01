# 2026-05-29 扩展核心数据采集记录

## 执行命令

```bash
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/collect_core_data.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/collect_mvp_data.py --limit 25 --delay 0.2
```

## 数据源范围

本轮覆盖 8 类核心源：

- PubMed / NCBI E-utilities
- OpenAlex Works
- ClinicalTrials.gov
- openFDA Drug Label
- openFDA Drug Event
- openFDA Drugs@FDA
- PubChem
- HAGR / GenAge / LongevityMap / DrugAge

## 处理后数据量

| 输出 | 条数 |
| --- | ---: |
| `domains/c1-boundary-rewriting/longevity-evidence/data/processed/pubmed_evidence.jsonl` | 500 |
| `domains/c1-boundary-rewriting/longevity-evidence/data/processed/openalex_works.jsonl` | 500 |
| `domains/c1-boundary-rewriting/longevity-evidence/data/processed/clinical_trials.jsonl` | 39 |
| `domains/c1-boundary-rewriting/longevity-evidence/data/processed/safety_labels.jsonl` | 103 |
| `domains/c1-boundary-rewriting/longevity-evidence/data/processed/openfda_event_counts.jsonl` | 120 |
| `domains/c1-boundary-rewriting/longevity-evidence/data/processed/drugsfda_applications.jsonl` | 55 |
| `domains/c1-boundary-rewriting/longevity-evidence/data/processed/pubchem_compounds.jsonl` | 15 |
| `domains/c1-boundary-rewriting/longevity-evidence/data/processed/hagr_snapshots.jsonl` | 4 |

去重后关键对象：

| 对象 | 去重数 |
| --- | ---: |
| PubMed PMID | 427 |
| OpenAlex work | 290 |
| ClinicalTrials.gov NCT | 15 |
| openFDA label | 103 |

HAGR 快照行数：

| 快照 | 行数 |
| --- | ---: |
| DrugAge | 3423 |
| GenAge human | 307 |
| GenAge models | 2205 |
| LongevityMap | 550 |

## 原始文件数

| 源 | 文件数 |
| --- | ---: |
| PubMed | 40 |
| OpenAlex | 20 |
| ClinicalTrials.gov | 20 |
| openFDA Drug Label | 6 |
| openFDA Drug Event | 6 |
| Drugs@FDA | 6 |
| PubChem | 12 |
| HAGR | 4 |

## 质量判断

- 两个采集脚本均无错误完成。
- HAGR 使用官方 zip 快照，已保留原始 zip 并解压 CSV。
- PubChem 只对药物、补剂和代谢物类干预采集；生活方式类干预没有化合物实体，这是预期行为。
- openFDA event 是自发报告聚合，只能作为风险信号，不代表因果关系或发生率。
- ClinicalTrials.gov 当前仍使用宽查询，后续需要实体相关性过滤。
- PubMed / OpenAlex 当前是候选证据池，仍需人工确认研究类型、物种、人群、终点和效果大小。

## 下一步

1. 建立统一去重表，把 PMID、DOI、OpenAlex ID 和 NCT ID 合并到同一证据对象。
2. 给 ClinicalTrials.gov 结果做干预相关性过滤，去掉宽查询噪音。
3. 对首批 20 个干预生成证据卡片草稿。
4. 把 HAGR DrugAge 与 `interventions` 做名称匹配，优先找出已经有寿命实验的干预。
