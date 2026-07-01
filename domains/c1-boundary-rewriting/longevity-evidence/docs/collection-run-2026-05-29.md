# 2026-05-29 MVP 数据采集记录

## 执行命令

```bash
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/collect_mvp_data.py --limit 10 --delay 0.2
```

## 范围

- 干预数量：20
- 单源单干预上限：10 条
- 数据源：PubMed、OpenAlex、ClinicalTrials.gov、openFDA Drug Label
- 原始响应目录：`domains/c1-boundary-rewriting/longevity-evidence/data/raw/`
- 处理后索引目录：`domains/c1-boundary-rewriting/longevity-evidence/data/processed/`

## 结果

| 输出 | 条数 |
| --- | ---: |
| `domains/c1-boundary-rewriting/longevity-evidence/data/processed/pubmed_evidence.jsonl` | 200 |
| `domains/c1-boundary-rewriting/longevity-evidence/data/processed/openalex_works.jsonl` | 200 |
| `domains/c1-boundary-rewriting/longevity-evidence/data/processed/clinical_trials.jsonl` | 39 |
| `domains/c1-boundary-rewriting/longevity-evidence/data/processed/safety_labels.jsonl` | 30 |
| `domains/c1-boundary-rewriting/longevity-evidence/data/processed/source_runs.jsonl` | 86 |

去重后记录：

| 数据 | 去重条数 |
| --- | ---: |
| PubMed PMID | 171 |
| OpenAlex work | 129 |
| ClinicalTrials.gov NCT | 15 |
| openFDA label | 30 |

## 原始文件

| 源 | 文件数 |
| --- | ---: |
| PubMed | 40 |
| OpenAlex | 20 |
| ClinicalTrials.gov | 20 |
| openFDA | 6 |

## 临床试验覆盖

有 ClinicalTrials.gov 结果的干预：

- `blood-pressure-control`: 3
- `exercise`: 10
- `glp-1`: 1
- `metformin`: 3
- `nad-plus`: 2
- `nmn`: 1
- `quercetin`: 1
- `rapamycin`: 6
- `resistance-training`: 3
- `sleep-optimization`: 6
- `statins`: 1
- `vo2-max`: 2

## 安全标签覆盖

openFDA 首轮只覆盖药物类查询：

- `acarbose`: 5
- `dasatinib`: 5
- `glp-1`: 5
- `metformin`: 5
- `rapamycin`: 5
- `statins`: 5

## 质量备注

- 第二轮采集无错误。
- 第一轮曾遇到 NCBI 对 `nicotinamide-riboside` 的 500 错误，已为采集脚本加入 429/5xx/network error 重试机制。
- 当前结果是候选证据池，不是最终证据结论；后续必须人工审核研究类型、适用对象、效果大小和局限性。
- ClinicalTrials.gov 查询使用宽搜索词，后续需要按干预实体和同义词做更严格的相关性过滤。
