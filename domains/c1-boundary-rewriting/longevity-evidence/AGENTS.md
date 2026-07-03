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
│   │   ├── life_path_nhats_acquisition_readiness.json
│   │   ├── life_path_nhats_official_source_refresh_register.json
│   │   ├── life_path_nhats_registration_evidence_template.json
│   │   ├── life_path_nhats_controlled_storage_destruction_plan.json
│   │   ├── life_path_nhats_synthetic_storage_destruction_drill.json
│   │   ├── life_path_nhats_colectica_access_route_probe_register.json
│   │   ├── life_path_nhats_colectica_authenticated_capture_template.json
│   │   ├── life_path_nhats_colectica_value_label_review_execution_register.json
│   │   ├── life_path_nhats_colectica_value_label_review_protocol.json
│   │   ├── life_path_nhats_file_tier_table.json
│   │   ├── life_path_nhats_first_estimand_protocol.json
│   │   ├── life_path_nhats_l2_variable_family_admission_register.json
│   │   ├── life_path_nhats_preoutcome_aggregation_protocol.json
│   │   ├── life_path_nhats_l4_readiness_runway.json
│   │   ├── life_path_nhats_variable_confirmation_matrix.json
│   │   ├── life_path_nhats_cohort_flow_endpoint_protocol.json
│   │   ├── life_path_nhats_disclosure_control_policy.json
│   │   ├── life_path_nhats_disclosure_control_test_cases.json
│   │   ├── life_path_nhats_survey_design_protocol.json
│   │   ├── life_path_nhats_survey_design_test_cases.json
│   │   ├── life_path_nhats_missingness_route_protocol.json
│   │   ├── life_path_nhats_missingness_route_test_cases.json
│   │   ├── life_path_public_mortality_anchor.json
│   │   ├── life_path_nhats_route_field_discovery_register.json
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
    ├── build_public_mortality_anchor.py
    ├── collect_core_data.py
    ├── collect_mvp_data.py
    ├── run_life_path_sensitivity_analysis.py
    ├── run_life_path_toy_model.py
    ├── validate_public_mortality_anchor.py
    ├── validate_nhats_acquisition_readiness.py
    ├── validate_nhats_official_source_refresh.py
    ├── validate_nhats_registration_evidence_template.py
    ├── validate_nhats_controlled_storage_destruction_plan.py
    ├── validate_nhats_synthetic_storage_destruction_drill.py
    ├── validate_nhats_colectica_access_route_probe.py
    ├── validate_nhats_colectica_authenticated_capture_template.py
    ├── validate_nhats_colectica_value_label_review_execution.py
    ├── validate_nhats_colectica_value_label_protocol.py
    ├── validate_nhats_disclosure_outputs.py
    ├── validate_nhats_l2_variable_family_admission.py
    ├── validate_nhats_preoutcome_aggregation_protocol.py
    ├── validate_nhats_l4_readiness_runway.py
    ├── validate_nhats_missingness_route_map.py
    ├── validate_nhats_route_field_discovery.py
    └── validate_nhats_survey_design_plan.py
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
- `data/manual/life_path_nhats_survey_design_protocol.json`：NHATS survey-design 协议，要求权重、分层、PSU/variance unit、方差方法、domain rule、missingness route、round linkage 和披露验证全部就绪后才允许加权估计。
- `data/manual/life_path_nhats_survey_design_test_cases.json`：NHATS survey-design 合成测试集，只验证 synthetic design-plan envelope 的 allow/block 行为，不包含真实 NHATS 权重、路由或参与者数据。
- `scripts/validate_nhats_survey_design_plan.py`：NHATS survey-design 验证器，生成 `web/src/data/life-path-nhats-survey-design-validation.json`，证明缺权重、缺分层、缺 PSU、缺方差方法或提前公共推断时必须阻断。
- `docs/collection-run-*.md`：历史采集记录和质量风险。
- `data/manual/interventions.json`：首批 20 个干预对象、类别、别名和检索词。
- `data/manual/higher_order_effects.tsv`：LEV 二阶 / 多阶效应模型输入，供 Web 导出脚本生成多阶飞轮图。
- `data/manual/lev_route_cards.tsv`：R1-R9 主流路线卡模型输入，供 Web 导出脚本生成路线矩阵和概率门图。
- `data/manual/life_path_toy_model_scenarios.json`：生命路径 toy model 的合成场景输入，定义基线风险、健康质量、场景控制值和 LEV 阈值压力测试。
- `data/manual/life_path_public_mortality_anchor.json`：NCHS 2021 U.S. Life Tables 的公开聚合死亡率锚点，用于 baseline hazard plausibility comparison；它不包含个人数据，不授权校准预测、干预效果估计或个体死亡日期输出。
- `data/manual/life_path_calibration_readiness.json`：生命路径模型的校准预备契约，记录 target population、time zero、outcome、estimand、data requirement、validation、calibration、sensitivity、bias/applicability、reporting 和 prohibited use 字段；它证明下一阶段要补什么，不证明当前模型已校准。
- `data/manual/life_path_data_source_candidates.json`：生命路径模型的候选数据源注册表，记录官方队列入口、可能模型角色、覆盖标签、访问治理状态和禁止外推边界；它只证明后续数据源搜索空间已被登记，不证明数据已访问、模型已校准或因果效应成立。
- `data/manual/life_path_nhats_acquisition_readiness.json`：NHATS acquisition readiness 机器契约，记录官方来源刷新、注册状态、文件层级、Colectica 变量确认、round window、survey design、endpoint、披露控制、AI 边界、存储销毁和禁止动作；它只证明提取前准入条件被机器化审计，当前仍是 `cannot-extract-yet`。
- `data/manual/life_path_nhats_official_source_refresh_register.json`：NHATS official source refresh 寄存器，记录官方 Data Access、Cross-Year Search、Conditions of Use、R13/R14 文件页和 Colectica 技术指南的 HTTP 状态、内容长度和 SHA-256；它只把 official-source-refresh 门升为 ready，不授权下载、抽取、校准或个体预测。
- `data/manual/life_path_nhats_registration_evidence_template.json`：NHATS registration evidence 模板，固定 redacted 账号状态、允许用户边界、使用条款确认、public-use file access tier、restricted approval boundary、controlled workspace linkage、no-public-secret-storage 和二次复核槽；它只把 registration-status 推进为 template-only partial，不证明注册完成。
- `scripts/validate_nhats_registration_evidence_template.py`：读取 NHATS registration evidence 模板，生成 `web/src/data/life-path-nhats-registration-evidence-template-validation.json`，验证 8 个证据槽和 no-registration-proof / no-download / no-extraction / no-calibration / no-individual-prediction 边界。
- `scripts/validate_nhats_acquisition_readiness.py`：读取 NHATS acquisition readiness 机器契约，生成 `web/src/data/life-path-nhats-acquisition-readiness-validation.json`，验证 acquisition-readiness gates 中 1 个 official-source-refresh 门 ready、1 个 registration template 门 partial、8 个其他门仍阻塞 extraction，并确认仓库内没有 raw NHATS、凭据或个体死亡日期字段。
- `data/manual/life_path_nhats_controlled_storage_destruction_plan.json`：NHATS 受控存储/销毁计划，定义非仓库受控工作区、访问日志、清单槽位、销毁触发和禁止位置；它只把 storage-destruction gate 升到 partial，不授权下载、抽取、校准或个体预测。
- `scripts/validate_nhats_controlled_storage_destruction_plan.py`：读取 NHATS 受控存储/销毁计划，生成 `web/src/data/life-path-nhats-controlled-storage-destruction-validation.json`，验证计划存在但仍未执行，并继续阻塞 download、extraction、raw data 入库、public AI 上传、calibration 和 individual prediction。
- `data/manual/life_path_nhats_synthetic_storage_destruction_drill.json`：NHATS 合成存储/销毁演练记录，保存 `/tmp` create-hash-delete dry-run 的哈希和删除确认；它只证明 synthetic drill mechanics，不证明注册、正式受控工作区、下载、抽取、校准或个体预测。
- `scripts/validate_nhats_synthetic_storage_destruction_drill.py`：读取 NHATS 合成存储/销毁演练记录，生成 `web/src/data/life-path-nhats-synthetic-storage-destruction-drill-validation.json`，验证演练 synthetic-only、三类临时文件 destroyed、最终路径不存在，并继续阻塞真实数据与模型动作。
- `data/manual/life_path_nhats_file_tier_table.json`：NHATS R13/R14 文件层级表，记录 annual public files、clock drawing images、sensitive SP/OP、R13 seasonality weights、官方文件路径、访问层级、候选用途、阻塞门、方法文档依赖和禁止动作；它只证明文件层级已登记，不授权下载或抽取。
- `scripts/validate_nhats_file_tier_table.py`：读取 NHATS R13/R14 文件层级表，生成 `web/src/data/life-path-nhats-file-tier-table-validation.json`，验证 16 个文件行、上游 access/source/template hash、method docs、阻塞门和禁止下载/抽取/仓库存储/public AI/校准/个体预测边界。
- `data/manual/life_path_nhats_first_estimand_protocol.json`：NHATS 第一版 estimand 协议，预注册 R13/R14 cohort-level functional-survival 研究问题、target population、time zero、outcome、predictor family、censoring/missingness、survey design 和 aggregate-only 输出边界；它只证明研究设计门已固定，不授权下载、抽取、校准、验证或个体预测。
- `data/manual/life_path_nhats_variable_confirmation_matrix.json`：NHATS 变量确认矩阵，记录官方来源事实、R13/R14 候选字段模式、变量组、cohort-flow 模板、readiness gates 和禁止动作；它只证明字段确认搜索空间已固定，不授权把候选字段当作已确认变量。
- `data/manual/life_path_nhats_cohort_flow_endpoint_protocol.json`：NHATS 队列流转与终点路由协议，记录 R13/R14 cohort-flow rows、R14 endpoint route classes、aggregate-only output contracts、n < 5 披露控制、readiness gates 和禁止动作；它只证明路由门禁已预注册，不授权下载、抽取、公开导出、校准或个体预测。
- `data/manual/life_path_nhats_disclosure_control_policy.json`：NHATS 披露控制策略，记录 aggregate-only、n < 5 suppression、row-level export block、public AI upload block、允许/禁止输出类型和 validator 契约；它只证明公开导出门禁已机器化，不授权真实 NHATS 输出离开受控环境。
- `data/manual/life_path_nhats_disclosure_control_test_cases.json`：NHATS 披露控制合成测试用例，覆盖安全聚合、小单元未抑制、小单元已抑制、行级泄漏、public AI upload 和禁止输出类型；它只保存 synthetic envelopes，不保存真实 NHATS 数据。
- `data/manual/life_path_nhats_route_field_discovery_register.json`：NHATS R13/R14 路由字段发现登记表，记录官方 crosswalk 和 User Guide 中的身份、状态、proxy、facility、death、missingness、design weight 和 disclosure 候选字段；它只证明字段候选已登记，不替代 Colectica value labels、受控数据访问、分类器审查、披露审查或校准。
- `data/manual/life_path_nhats_colectica_value_label_review_protocol.json`：NHATS Colectica value-label 复核协议，记录登录、字段级来源追踪、值标签、问题文本、universe/skip logic、route-value crosswalk、negative missing-code map、敏感 death-date 排除、二次复核和输出披露边界；它只证明下一步复核门已机器化，不替代已确认 value labels 或真实 route classifier。
- `data/manual/life_path_nhats_colectica_value_label_review_execution_register.json`：NHATS Colectica value-label 复核第一轮执行登记，记录官方来源追踪、字段级 source-trace 骨架、standard negative-code family 和仍未通过的登录、值标签、问题文本、skip logic、route-value crosswalk、二次复核、公开输出和模型准入阻塞门。
- `data/manual/life_path_nhats_colectica_access_route_probe_register.json`：NHATS Colectica access-route probe 登记，记录官方 Cross-Year Search 入口、匿名访问登录边界、技术指南 SHA-256、Details/Basket capture workflow 和后续受控登录捕获步骤；它只证明访问路线已探测，不证明账号、登录、变量页、value labels、question text、导出、校准或个体预测已完成。
- `data/manual/life_path_nhats_colectica_authenticated_capture_template.json`：NHATS Colectica 受控登录后变量页捕获模板，记录 route field 进入 value-label 复核前必须补齐的 item id、变量名、文件名、Details URL、source hash、question text、universe/skip logic、变量级缺失码和二次复核槽位；它只证明捕获证据结构已固定，不证明登录、捕获、标签确认、route classifier、公开导出、校准或个体预测已完成。
- `data/manual/life_path_nhats_l2_variable_family_admission_register.json`：NHATS L2 变量族准入前映射，绑定第一版窄 estimand、变量确认矩阵、模型准入契约和候选注册表，把 6 个候选变量族固定为 L2-only；它不确认精确字段、不授权真实提取、校准或个体预测。
- `data/manual/life_path_nhats_preoutcome_aggregation_protocol.json`：NHATS 预结果聚合协议，冻结 8 条 L2-only 聚合规则、7 个合成用例和真实聚合前置证据要求；它不授权真实 NHATS 聚合、加权估计、公开导出、L4 准入、校准或个体预测。
- `data/manual/life_path_nhats_l4_readiness_runway.json`：NHATS L4 readiness runway，把 R13/R14 从 L2 设计资产推进到 L4 aggregate-calibrated research model 前必须通过的 12 个 readiness gates 串成一条可审计路线；当前状态仍是 `runway-only-l4-blocked`。
- `data/raw/`：采集脚本保存的原始 API 响应和下载快照。
- `data/processed/`：采集脚本生成的 JSONL 索引和汇总。
- `scripts/collect_mvp_data.py`：采集 PubMed、OpenAlex、ClinicalTrials.gov 和 openFDA 标签数据。
- `scripts/collect_core_data.py`：采集 HAGR、PubChem、openFDA event 和 Drugs@FDA 数据。
- `scripts/build_public_mortality_anchor.py`：从 NCHS 官方 xlsx 生命表生成公开聚合死亡率锚点。
- `scripts/validate_public_mortality_anchor.py`：离线审计公开聚合死亡率锚点的 schema、来源、年龄范围、列值和禁止用途边界。
- `scripts/validate_nhats_registration_evidence_template.py`：读取 NHATS registration evidence 模板，生成 `web/src/data/life-path-nhats-registration-evidence-template-validation.json`，把注册/访问证据槽、redacted-only 仓库边界和禁止真实下载/抽取/校准/个体预测边界纳入默认审计。
- `scripts/validate_nhats_acquisition_readiness.py`：读取 NHATS acquisition readiness 机器契约，生成 `web/src/data/life-path-nhats-acquisition-readiness-validation.json`，把注册模板、文件层级、Colectica、survey design、endpoint、披露控制、AI 边界和存储销毁缺口纳入默认审计。
- `scripts/validate_nhats_official_source_refresh.py`：读取 NHATS official source refresh 寄存器，生成 `web/src/data/life-path-nhats-official-source-refresh-validation.json`，验证 8 个官方公开来源的状态、hash、支持范围和禁止用途边界。
- `scripts/run_life_path_toy_model.py`：读取合成场景并导出 `web/src/data/life-path-toy-model.json`，用于 `/model/` 的最小可运行定量展示。
- `scripts/run_life_path_sensitivity_analysis.py`：读取合成场景和已导出的 toy model，生成 `web/src/data/life-path-sensitivity-analysis.json`，用于一因素扰动检查场景排序、开放边界和最敏感参数。
- `scripts/validate_nhats_disclosure_outputs.py`：读取 NHATS 披露控制策略和合成测试用例，生成 `web/src/data/life-path-nhats-disclosure-control-validation.json`，验证 aggregate-only、small-cell suppression、row-level block、public AI block 和 forbidden output type 规则。
- `scripts/validate_nhats_route_field_discovery.py`：读取 NHATS route-field discovery register，生成 `web/src/data/life-path-nhats-route-field-discovery-validation.json`，验证官方字段发现仍然保持 Colectica、数据访问、分类器、加权统计、公开导出、校准和个体预测阻塞。
- `scripts/validate_nhats_colectica_value_label_protocol.py`：读取 NHATS Colectica value-label review protocol，生成 `web/src/data/life-path-nhats-colectica-value-label-validation.json`，验证 value labels、question text、skip logic、route crosswalk、classifier、weighted counts、public export、calibration 和 individual prediction 仍被阻塞。
- `scripts/validate_nhats_colectica_value_label_review_execution.py`：读取 NHATS Colectica value-label review execution register，生成 `web/src/data/life-path-nhats-colectica-value-label-review-execution-validation.json`，验证第一轮执行登记只打开 source trace / negative-code family 证据，不打开 value labels、route map、classifier、weighted counts、public export、calibration 或 individual prediction。
- `scripts/validate_nhats_colectica_access_route_probe.py`：读取 NHATS Colectica access-route probe register，生成 `web/src/data/life-path-nhats-colectica-access-route-probe-validation.json`，验证公开入口、匿名登录边界、技术指南 workflow 和受控 capture sequence，同时继续阻塞 authenticated capture、value labels、exports、calibration 和 individual prediction。
- `scripts/validate_nhats_colectica_authenticated_capture_template.py`：读取 NHATS Colectica authenticated capture template，生成 `web/src/data/life-path-nhats-colectica-authenticated-capture-template-validation.json`，验证受控登录后变量页捕获槽、敏感死亡字段排除、source hash 证据要求和二次复核门，同时继续阻塞账号状态、登录、变量页实捕获、value labels、route classifier、公开导出、校准和 individual prediction。
- `scripts/validate_nhats_l2_variable_family_admission.py`：读取 NHATS L2 变量族准入前映射，生成 `web/src/data/life-path-nhats-l2-variable-family-admission-validation.json`，验证窄 estimand、6 个 L2 候选变量族、来源 hash、L4/L5 阻塞门和禁止抽取 / 校准 / 个体预测边界。
- `scripts/validate_nhats_preoutcome_aggregation_protocol.py`：读取 NHATS 预结果聚合协议，生成 `web/src/data/life-path-nhats-preoutcome-aggregation-validation.json`，验证 8 条 L2-only 聚合规则、7 个合成用例、上游 source hash 和真实聚合 / 加权估计 / L4 准入 / 校准 / 个体预测阻塞边界。
- `scripts/validate_nhats_l4_readiness_runway.py`：读取 NHATS L4 readiness runway，生成 `web/src/data/life-path-nhats-l4-readiness-runway-validation.json`，验证 12 个 runway gates、上游 source hash、L4 阻塞状态和禁止真实提取 / 校准 / 个体预测边界。
- `scripts/audit_life_path_toy_model.py`：审计生成后的生命路径 toy model、合成敏感性分析、校准预备契约、候选数据源注册表、数据源 Source Cards、Data Card 模板、NHATS Data Card、NHATS 变量字典、NHATS extraction manifest、NHATS registration evidence 模板与 validation、NHATS acquisition readiness 机器契约、NHATS acquisition-readiness validation、NHATS controlled storage/destruction validation、NHATS synthetic storage/destruction drill validation、NHATS file-tier table 与 file-tier validation、NHATS first estimand protocol、NHATS variable confirmation matrix、NHATS cohort-flow endpoint protocol、NHATS disclosure-control validation、NHATS survey-design validation、NHATS missingness-route validation、NHATS route-field discovery validation、NHATS Colectica value-label validation、NHATS Colectica value-label execution validation、NHATS Colectica access-route probe validation、NHATS Colectica authenticated capture template validation、NHATS L2 variable-family admission validation 和 NHATS pre-outcome aggregation validation，输出机器可读 JSON 和人可读 Markdown，检查模型卡、来源 hash、生存曲线、概率范围、LEV 开放边界、敏感性参数覆盖、校准预备字段、候选数据源治理边界、数据卡准入文档、提取前治理门禁、注册证据模板边界、准入门机器化状态、acquisition-readiness validator、受控存储/销毁 validator、合成销毁演练 validator、文件层级覆盖与 file-tier validation、第一版 estimand 研究设计门、变量确认门、队列流转/终点路由/披露控制门、合成 disclosure/survey/missingness validator 结果、官方字段发现边界、Colectica 复核协议门、Colectica 第一轮执行登记边界、Colectica 访问路线边界、Colectica authenticated capture 模板边界、L2 变量族准入前映射边界、预结果聚合规则边界和禁止个体死亡日期字段。

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
- 2026-07-03：更新 `validate_nhats_acquisition_readiness.py` 与 `life-path-nhats-acquisition-readiness-validation.json`，把 NHATS acquisition readiness 的 1 个 ready 门、1 个 registration template partial 门和 8 个其他阻塞门接入默认审计。
- 2026-07-03：新增 `life_path_nhats_registration_evidence_template.json`、`validate_nhats_registration_evidence_template.py` 和 `life-path-nhats-registration-evidence-template-validation.json`，把 NHATS 注册/访问证据槽纳入默认审计；该门只把 `registration-status` 推进为 template-only partial，仍阻塞真实注册证明、下载、抽取、校准和个体预测。
- 2026-07-03：新增 `life_path_nhats_controlled_storage_destruction_plan.json`、`validate_nhats_controlled_storage_destruction_plan.py` 和 `life-path-nhats-controlled-storage-destruction-validation.json`，把 NHATS 受控存储/销毁计划接入默认审计；该 gate 仍只允许 partial，继续阻塞真实下载和抽取。
- 2026-07-03：新增 `life_path_nhats_synthetic_storage_destruction_drill.json`、`validate_nhats_synthetic_storage_destruction_drill.py` 和 `life-path-nhats-synthetic-storage-destruction-drill-validation.json`，把 NHATS 合成存储/销毁演练接入默认审计；它只证明 dry-run 机制，仍不打开真实下载、抽取或校准。
- 2026-07-03：新增 `life_path_nhats_l4_readiness_runway.json`、`validate_nhats_l4_readiness_runway.py` 和 `life-path-nhats-l4-readiness-runway-validation.json`，把 NHATS L4 readiness runway 接入默认审计；它只证明 12 个阻塞门可审计，不打开真实提取、校准或个体预测。
- 2026-07-03：新增 `life_path_nhats_official_source_refresh_register.json`、`validate_nhats_official_source_refresh.py` 和 `life-path-nhats-official-source-refresh-validation.json`，把 NHATS 官方公开来源刷新接入默认审计；它只把 official-source-refresh 门升为 ready，其他 acquisition/L4 门继续阻塞。
