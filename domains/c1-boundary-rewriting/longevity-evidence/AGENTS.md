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
│   │   ├── higher_order_effects.tsv
│   │   ├── interventions.json
│   │   ├── lev_route_cards.tsv
│   │   ├── life_path_calibration_readiness.json
│   │   ├── life_path_data_source_candidates.json
│   │   ├── life_path_nhats_file_tier_table.json
│   │   ├── life_path_nhats_acquisition_readiness.json
│   │   ├── life_path_nhats_first_estimand_protocol.json
│   │   ├── life_path_nhats_variable_confirmation_matrix.json
│   │   ├── life_path_nhats_cohort_flow_endpoint_protocol.json
│   │   ├── life_path_nhats_disclosure_control_policy.json
│   │   ├── life_path_nhats_disclosure_control_test_cases.json
│   │   └── life_path_toy_model_scenarios.json
│   ├── processed/
│   └── raw/
├── docs/
│   ├── README.md
│   ├── collection-run-2026-05-29-expanded.md
│   ├── collection-run-2026-05-29.md
│   ├── data-inventory.md
│   ├── data-sources.md
│   ├── evidence-model.md
│   ├── lev-enabling-resources.md
│   ├── lev-higher-order-effects-discovery.md
│   ├── lev-route-card-template.md
│   ├── lev-source-cards.md
│   ├── lev-mainstream-routes.md
│   ├── life-path-data-card-template.md
│   ├── life-path-data-card-nhats.md
│   ├── life-path-extraction-manifest-nhats-draft.md
│   ├── life-path-data-source-cards.md
│   ├── life-path-variable-dictionary-nhats.md
│   ├── mvp-roadmap.md
│   └── product-brief.md
└── scripts/
    ├── README.md
    ├── audit_life_path_toy_model.py
    ├── collect_core_data.py
    ├── collect_mvp_data.py
    ├── run_life_path_sensitivity_analysis.py
    ├── validate_nhats_disclosure_outputs.py
    └── run_life_path_toy_model.py
```

## 文件职责

- `README.md`：说明本子域在 Human Infra 中的位置、边界、MVP 和运行入口。
- `docs/README.md`：说明本子域文档入口和每份文档职责。
- `docs/product-brief.md`：Longevity Evidence 产品定位、用户、价值和非目标。
- `docs/evidence-model.md`：干预、主张、证据、临床试验和证据等级模型。
- `docs/data-sources.md`：首批公开数据源和接入优先级。
- `docs/data-inventory.md`：数据域、字段、持续维护源和更新节奏。
- `docs/lev-enabling-resources.md`：LEV 间接资源层，维护时间、注意力、认知、能力、记忆、AI、资金、社会支持、环境及多阶效应链路。
- `docs/lev-higher-order-effects-discovery.md`：二阶 / 多阶效应调研发现，维护新增概率门、正负链路、研究传统和可迁移标签。
- `docs/lev-route-card-template.md`：LEV 路线卡契约，规定新路线必须填写的变量、概率门、证据和禁止外推边界。
- `docs/lev-source-cards.md`：LEV Source Cards，保存来源能支持和不能支持的主张边界。
- `docs/lev-mainstream-routes.md`：长寿逃逸速度主流路线、官方/论文来源信号、现有研究域映射和证据边界。
- `docs/life-path-data-source-cards.md`：生命路径候选数据源 Source Cards，保存每个官方数据源可能支持的变量、不能支持的结论、接入前缺口和下一步 Data Card 要求。
- `docs/life-path-data-card-template.md`：真实队列进入模型前必须填写的数据卡模板，约束治理、研究设计、结局、预测变量、数据质量、模型用途、决策和来源追踪。
- `docs/life-path-data-card-nhats.md`：NHATS 数据准入卡草案，约束晚年功能/有效时间模型使用 NHATS 前必须满足的治理、设计、结局、变量、质量和中止条件。
- `docs/life-path-variable-dictionary-nhats.md`：NHATS 变量家族字典草案，把设计变量、死亡边界、功能、认知、资源支持、环境和有效时间代理指标映射到生命路径模型角色。
- `docs/life-path-extraction-manifest-nhats-draft.md`：NHATS 提取清单草案，把文件名、变量名、权重、缺失码、访问层级、endpoint、允许输出和中止条件作为写抽取脚本前的准入门。
- `docs/collection-run-*.md`：历史采集记录和质量风险。
- `data/manual/interventions.json`：首批 20 个干预对象、类别、别名和检索词。
- `data/manual/higher_order_effects.tsv`：LEV 二阶 / 多阶效应模型输入，供 Web 导出脚本生成多阶飞轮图。
- `data/manual/lev_route_cards.tsv`：R1-R9 主流路线卡模型输入，供 Web 导出脚本生成路线矩阵和概率门图。
- `data/manual/life_path_toy_model_scenarios.json`：生命路径 toy model 的合成场景输入，定义基线风险、健康质量、场景控制值和 LEV 阈值压力测试。
- `data/manual/life_path_calibration_readiness.json`：生命路径模型的校准预备契约，记录 target population、time zero、outcome、estimand、data requirement、validation、calibration、sensitivity、bias/applicability、reporting 和 prohibited use 字段；它证明下一阶段要补什么，不证明当前模型已校准。
- `data/manual/life_path_data_source_candidates.json`：生命路径模型的候选数据源注册表，记录官方队列入口、可能模型角色、覆盖标签、访问治理状态和禁止外推边界；它只证明后续数据源搜索空间已被登记，不证明数据已访问、模型已校准或因果效应成立。
- `data/manual/life_path_nhats_acquisition_readiness.json`：NHATS acquisition readiness 机器契约，记录官方来源刷新、注册状态、文件层级、Colectica 变量确认、round window、survey design、endpoint、披露控制、AI 边界、存储销毁和禁止动作；它只证明提取前准入条件被机器化审计，当前仍是 `cannot-extract-yet`。
- `data/manual/life_path_nhats_file_tier_table.json`：NHATS R13/R14 文件层级表，记录 annual public files、clock drawing images、sensitive SP/OP、R13 seasonality weights、官方文件路径、访问层级、候选用途、阻塞门、方法文档依赖和禁止动作；它只证明文件层级已登记，不授权下载或抽取。
- `data/manual/life_path_nhats_first_estimand_protocol.json`：NHATS 第一版 estimand 协议，预注册 R13/R14 cohort-level functional-survival 研究问题、target population、time zero、outcome、predictor family、censoring/missingness、survey design 和 aggregate-only 输出边界；它只证明研究设计门已固定，不授权下载、抽取、校准、验证或个体预测。
- `data/manual/life_path_nhats_variable_confirmation_matrix.json`：NHATS 变量确认矩阵，记录官方来源事实、R13/R14 候选字段模式、变量组、cohort-flow 模板、readiness gates 和禁止动作；它只证明字段确认搜索空间已固定，不授权把候选字段当作已确认变量。
- `data/manual/life_path_nhats_cohort_flow_endpoint_protocol.json`：NHATS 队列流转与终点路由协议，记录 R13/R14 cohort-flow rows、R14 endpoint route classes、aggregate-only output contracts、n < 5 披露控制、readiness gates 和禁止动作；它只证明路由门禁已预注册，不授权下载、抽取、公开导出、校准或个体预测。
- `data/manual/life_path_nhats_disclosure_control_policy.json`：NHATS 披露控制策略，记录 aggregate-only、n < 5 suppression、row-level export block、public AI upload block、允许/禁止输出类型和 validator 契约；它只证明公开导出门禁已机器化，不授权真实 NHATS 输出离开受控环境。
- `data/manual/life_path_nhats_disclosure_control_test_cases.json`：NHATS 披露控制合成测试用例，覆盖安全聚合、小单元未抑制、小单元已抑制、行级泄漏、public AI upload 和禁止输出类型；它只保存 synthetic envelopes，不保存真实 NHATS 数据。
- `data/raw/`：采集脚本保存的原始 API 响应和下载快照。
- `data/processed/`：采集脚本生成的 JSONL 索引和汇总。
- `scripts/collect_mvp_data.py`：采集 PubMed、OpenAlex、ClinicalTrials.gov 和 openFDA 标签数据。
- `scripts/collect_core_data.py`：采集 HAGR、PubChem、openFDA event 和 Drugs@FDA 数据。
- `scripts/run_life_path_toy_model.py`：读取合成场景并导出 `web/src/data/life-path-toy-model.json`，用于 `/model/` 的最小可运行定量展示。
- `scripts/run_life_path_sensitivity_analysis.py`：读取合成场景和已导出的 toy model，生成 `web/src/data/life-path-sensitivity-analysis.json`，用于一因素扰动检查场景排序、开放边界和最敏感参数。
- `scripts/validate_nhats_disclosure_outputs.py`：读取 NHATS 披露控制策略和合成测试用例，生成 `web/src/data/life-path-nhats-disclosure-control-validation.json`，验证 aggregate-only、small-cell suppression、row-level block、public AI block 和 forbidden output type 规则。
- `scripts/audit_life_path_toy_model.py`：审计生成后的生命路径 toy model、合成敏感性分析、校准预备契约、候选数据源注册表、数据源 Source Cards、Data Card 模板、NHATS Data Card、NHATS 变量字典、NHATS extraction manifest、NHATS acquisition readiness 机器契约、NHATS file-tier table、NHATS first estimand protocol、NHATS variable confirmation matrix、NHATS cohort-flow endpoint protocol 和 NHATS disclosure-control validation，输出机器可读 JSON 和人可读 Markdown，检查模型卡、来源 hash、生存曲线、概率范围、LEV 开放边界、敏感性参数覆盖、校准预备字段、候选数据源治理边界、数据卡准入文档、提取前治理门禁、准入门机器化状态、文件层级覆盖、第一版 estimand 研究设计门、变量确认门、队列流转/终点路由/披露控制门、合成 disclosure validator 结果和禁止个体死亡日期字段。

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
