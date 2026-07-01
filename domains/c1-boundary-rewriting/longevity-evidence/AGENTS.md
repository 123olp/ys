# Longevity Evidence 架构说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c1-boundary-rewriting/longevity-evidence` |
| 所属层级 | `C1` - 可能性边界改写层 |
| 父级容器 | `domains/c1-boundary-rewriting` |
| 路径真相源 | `domains/_possibility-space-control/classification.tsv` |
| 复核状态 | `heuristic-v0.1` |

### 文件职责

- `README.md` 面向读者，说明研究对象、Human Infra 价值链路、证据边界、非目标和下一步资料入口。
- `AGENTS.md` 面向维护者和代理，说明目录结构、上下游依赖、禁止事项、更新规则和验证要求。

### 更新规则

- 修改本域对象、边界或上下游关系时，必须同步检查 README、AGENTS 和分类表中的 `physical_path`。
- 新增资料优先沉淀为 Source Signals、Source Cards、Claim-Evidence Matrix 或明确的证据段落，不把未经核验的摘要写成稳定结论。
- 若发现当前层级不符合“可能性空间控制力”标尺，先修改 `_possibility-space-control/rubric.md` 或 `classification.tsv`，再移动目录。

### 禁止事项

- 不把研究域写成个体行动处方、临床建议、法律建议、投资建议、工程操作手册或规避规则指南。
- 不在本目录保存无来源、无边界、无证据等级的断言。
- 不绕过父级 C1-C6 物理目录直接在 `domains/` 根目录新增正式研究域。
<!-- domain-agent-contract:end -->

<!-- domain-agent-workflow:start -->
## 代理执行流程

1. 先读本目录 `README.md`，确认研究对象、分级理由、Human Infra 追问和使用边界。
2. 再读父级层目录的 `README.md` 与 `AGENTS.md`，确认 `C1` 层的根本性标尺和同层相邻域。
3. 需要移动、拆分、合并或重命名本域时，先更新 `domains/_possibility-space-control/classification.tsv`，再运行 `python3 tools/update_domain_doc_contracts.py`。
4. 新增资料时先落到 Source Signals 或 Source Cards；只有完成证据边界复核后，才沉淀为稳定叙述。
5. 输出结论时必须同时写清：它影响什么变量、通过什么机制、证据等级是什么、不能推出什么。

## 补齐优先级

- P1 Source trail：补来源、日期、版本、作者、原始链接和本地路径。
- P2 Variable map：补输入变量、中间机制、状态变量、风险变量和输出指标。
- P3 Claim-Evidence Matrix：补主张、证据、适用范围、不确定性、反例和禁用外推。
- P4 Relation links：补上游依赖、下游输出、同层相邻域和可能的迁移路径。
- P5 Reader path：补新手入口、术语、最小阅读顺序和下一步研究任务。

## 验证要求

- 批量更新域文档后，必须运行 `python3 tools/update_domain_doc_contracts.py` 并确认第二次运行更新数为 0。
- 结构或链接变化后，必须运行 `make check`。
- 提交前必须运行 `git diff --check`，避免 Markdown 空白和格式错误。
- 不得把 `web/`、临时下载、个人资料或未核验论文缓存混入域文档提交。
<!-- domain-agent-workflow:end -->

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
