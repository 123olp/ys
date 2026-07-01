# Longevity Evidence 架构说明

`longevity-evidence/` 承接原 Biocat，是 Human Infra 中负责长寿干预证据、临床试验、安全风险和公开数据采集的子域。

## 目录结构

```text
longevity-evidence/
├── AGENTS.md
├── README.md
├── data/
│   ├── README.md
│   ├── manual/
│   │   └── interventions.json
│   ├── processed/
│   └── raw/
├── docs/
│   ├── README.md
│   ├── collection-run-2026-05-29-expanded.md
│   ├── collection-run-2026-05-29.md
│   ├── data-inventory.md
│   ├── data-sources.md
│   ├── evidence-model.md
│   ├── mvp-roadmap.md
│   └── product-brief.md
└── scripts/
    ├── README.md
    ├── collect_core_data.py
    └── collect_mvp_data.py
```

## 文件职责

- `README.md`：说明本子域在 Human Infra 中的位置、边界、MVP 和运行入口。
- `docs/README.md`：说明本子域文档入口和每份文档职责。
- `docs/product-brief.md`：Longevity Evidence 产品定位、用户、价值和非目标。
- `docs/evidence-model.md`：干预、主张、证据、临床试验和证据等级模型。
- `docs/data-sources.md`：首批公开数据源和接入优先级。
- `docs/data-inventory.md`：数据域、字段、持续维护源和更新节奏。
- `docs/collection-run-*.md`：历史采集记录和质量风险。
- `data/manual/interventions.json`：首批 20 个干预对象、类别、别名和检索词。
- `data/raw/`：采集脚本保存的原始 API 响应和下载快照。
- `data/processed/`：采集脚本生成的 JSONL 索引和汇总。
- `scripts/collect_mvp_data.py`：采集 PubMed、OpenAlex、ClinicalTrials.gov 和 openFDA 标签数据。
- `scripts/collect_core_data.py`：采集 HAGR、PubChem、openFDA event 和 Drugs@FDA 数据。

## 依赖关系

- `scripts/` 只依赖本子域内的 `data/`，不依赖仓库根目录的数据路径。
- `data/` 只保存可追溯公开数据、清洗结果和人工整理词表。
- `docs/` 先定义事实模型和数据边界，避免采集脚本反向决定产品判断。
- 根 `README.md` 只路由到本子域，不承载本子域的数据细节。

## 设计原则

- 优先复用公开数据库、官方 API、成熟文献索引和生物医学标准。
- 自研代码只做连接、清洗、归一化、评分编排和产品表达。
- 本子域是证据导航，不是医疗建议系统。
- 证据评分必须保留来源、适用对象、研究类型和不确定性。
- 新增采集脚本前，必须先确认字段归属、刷新节奏和数据质量门槛。

## 变更日志

- 2026-06-20：从根目录迁入 `domains/c1-boundary-rewriting/longevity-evidence/`，成为 Human Infra 的长寿证据子域；脚本和数据路径保持在子域内部。
