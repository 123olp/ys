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
│   │   ├── life_path_nhanes_public_lmf_aggregate_pilot.json
│   │   ├── life_path_nhanes_public_lmf_domain_subpopulation_rule_readiness.json
│   │   ├── life_path_nhanes_public_lmf_eligible_base_readiness.json
│   │   ├── life_path_nhanes_public_lmf_survey_design_readiness.json
│   │   ├── life_path_nhanes_public_lmf_weighted_estimator_readiness.json
│   │   ├── life_path_nhanes_public_lmf_r_survey_runtime_smoke_readiness.json
│   │   ├── life_path_nhanes_public_lmf_domain_indicator_diagnostic.json
│   │   ├── life_path_nhanes_public_lmf_dof_sparse_domain_diagnostic.json
│   │   ├── life_path_nhanes_public_lmf_disclosure_output_envelope_policy.json
│   │   ├── life_path_nhanes_public_lmf_disclosure_output_envelope_test_cases.json
│   │   ├── life_path_nhanes_public_lmf_effective_sample_ci_publication_policy.json
│   │   ├── life_path_nhanes_public_lmf_effective_sample_ci_publication_test_cases.json
│   │   ├── life_path_nhanes_public_lmf_weighted_output_implementation_preflight_policy.json
│   │   ├── life_path_nhanes_public_lmf_weighted_output_implementation_preflight_test_cases.json
│   │   ├── life_path_nhanes_public_lmf_disclosure_review_template.json
│   │   ├── life_path_nhanes_public_lmf_disclosure_review_execution_register.json
│   │   ├── life_path_nhanes_public_lmf_local_run_evidence_manifest.json
│   │   ├── life_path_nhanes_public_lmf_weighted_domain_output_readiness.json
│   │   ├── life_path_nhats_acquisition_readiness.json
│   │   ├── life_path_nhats_official_source_refresh_register.json
│   │   ├── life_path_nhats_registration_evidence_template.json
│   │   ├── life_path_nhats_registration_evidence_packet_validator_test_cases.json
│   │   ├── life_path_nhats_controlled_storage_destruction_plan.json
│   │   ├── life_path_nhats_synthetic_storage_destruction_drill.json
│   │   ├── life_path_nhats_colectica_access_route_probe_register.json
│   │   ├── life_path_nhats_colectica_authenticated_capture_template.json
│   │   ├── life_path_nhats_colectica_capture_packet_validator_test_cases.json
│   │   ├── life_path_nhats_colectica_capture_packet_review_execution_register.json
│   │   ├── life_path_nhats_colectica_capture_task_register.json
│   │   ├── life_path_nhats_colectica_value_label_review_execution_register.json
│   │   ├── life_path_nhats_colectica_value_label_review_protocol.json
│   │   ├── life_path_nhats_route_value_crosswalk_assembly_protocol.json
│   │   ├── life_path_nhats_route_value_crosswalk_entry_validator_test_cases.json
│   │   ├── life_path_nhats_route_classifier_readiness.json
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
│   ├── ai-automated-science-technology-window-compression.md
│   ├── ai-automated-science-source-cards.md
│   ├── ai-automated-science-research-results.md
│   ├── life-path-data-card-template.md
│   ├── life-path-data-card-nhats.md
│   ├── life-path-extraction-manifest-nhats-draft.md
│   ├── life-path-data-source-cards.md
│   ├── life-path-variable-dictionary-nhats.md
│   ├── nhats-colectica-capture-packet-runbook.md
│   ├── mvp-roadmap.md
│   └── product-brief.md
├── runtime/
│   ├── README.md
│   └── nhanes-public-lmf-r-survey-conda.yml
└── scripts/
    ├── README.md
    ├── audit_life_path_toy_model.py
    ├── build_nhanes_public_lmf_aggregate_pilot.py
    ├── build_public_mortality_anchor.py
    ├── collect_core_data.py
    ├── collect_mvp_data.py
    ├── run_life_path_toy_model.py
    ├── run_life_path_sensitivity_analysis.py
    ├── build_life_path_synthetic_validation_calibration_report.py
    ├── validate_public_mortality_anchor.py
    ├── validate_nhats_acquisition_readiness.py
    ├── validate_nhats_official_source_refresh.py
    ├── validate_nhats_registration_evidence_template.py
    ├── validate_nhats_registration_evidence_packet_validator.py
    ├── validate_nhats_controlled_storage_destruction_plan.py
    ├── validate_nhats_synthetic_storage_destruction_drill.py
    ├── validate_nhats_colectica_access_route_probe.py
	    ├── validate_nhats_colectica_authenticated_capture_template.py
	    ├── validate_nhats_colectica_capture_packet_validator.py
	    ├── build_nhats_colectica_capture_packet_draft.py
	    ├── build_nhats_colectica_capture_packet_review_handoff.py
	    ├── validate_nhats_colectica_capture_packet_review_execution.py
	    ├── validate_nhats_colectica_capture_task_register.py
    ├── validate_nhats_colectica_value_label_review_execution.py
    ├── validate_nhats_colectica_value_label_protocol.py
    ├── validate_nhats_disclosure_outputs.py
    ├── validate_nhats_route_value_crosswalk_assembly.py
    ├── validate_nhats_route_value_crosswalk_entry_validator.py
    ├── build_nhats_route_value_crosswalk_entry_draft.py
    ├── build_nhats_route_value_crosswalk_entry_review_handoff.py
    ├── build_nhats_route_classifier_synthetic_dry_run.py
    ├── validate_nhats_route_classifier_readiness.py
    ├── validate_nhats_l2_variable_family_admission.py
    ├── validate_nhats_preoutcome_aggregation_protocol.py
    ├── validate_nhats_l4_readiness_runway.py
    ├── validate_nhanes_public_lmf_aggregate_pilot.py
    ├── validate_nhanes_public_lmf_domain_subpopulation_rule_readiness.py
    ├── validate_nhanes_public_lmf_eligible_base_readiness.py
    ├── validate_nhanes_public_lmf_survey_design_readiness.py
    ├── validate_nhanes_public_lmf_weighted_estimator_readiness.py
    ├── validate_nhanes_public_lmf_r_survey_runtime_smoke.py
    ├── validate_nhanes_public_lmf_domain_indicator_diagnostic.py
    ├── validate_nhanes_public_lmf_dof_sparse_domain_diagnostic.py
    ├── validate_nhanes_public_lmf_disclosure_output_envelope.py
    ├── validate_nhanes_public_lmf_effective_sample_ci_publication.py
    ├── validate_nhanes_public_lmf_weighted_output_implementation_preflight.py
    ├── validate_nhanes_public_lmf_disclosure_review_template.py
    ├── validate_nhanes_public_lmf_disclosure_review_execution.py
    ├── run_nhanes_public_lmf_weighted_domain_output_local.py
    ├── validate_nhanes_public_lmf_weighted_domain_output_local_run.py
    ├── build_nhanes_public_lmf_local_disclosure_review_packet.py
    ├── validate_nhanes_public_lmf_local_disclosure_review_packet.py
    ├── validate_nhanes_public_lmf_local_run_evidence_manifest.py
    ├── validate_nhanes_public_lmf_public_web_data_no_real_values.py
    ├── validate_nhanes_public_lmf_weighted_domain_output_readiness.py
    ├── run_nhanes_public_lmf_r_survey_controlled_runtime_smoke.sh
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
- `docs/ai-automated-science-technology-window-compression.md`：AI 自动科研与技术窗口压缩路线说明，把 AlphaFold、AlphaMissense、GNoME、A-Lab、RoboChem 等信号转成 C1 的 LEV 外部条件模型，而不把奇点或永生写成事实结论。
- `docs/ai-automated-science-source-cards.md`：AI 自动科研路线 Source Cards，记录已拉取文献、E-utilities hash、A-Lab correction 约束、可支持主张、禁止外推和模型准入边界。
- `docs/ai-automated-science-research-results.md`：AI 自动科研路线研究成果稿，把来源卡片综合为 C1 技术窗口压缩结论、变量模型、正负链路、LEV 解释和下一步协议。
- `docs/life-path-data-source-cards.md`：生命路径候选数据源 Source Cards，保存每个官方数据源可能支持的变量、不能支持的结论、接入前缺口和下一步 Data Card 要求。
- `docs/life-path-data-card-template.md`：真实队列进入模型前必须填写的数据卡模板，约束治理、研究设计、结局、预测变量、数据质量、模型用途、决策和来源追踪。
- `docs/life-path-data-card-nhats.md`：NHATS 数据准入卡草案，约束晚年功能/有效时间模型使用 NHATS 前必须满足的治理、设计、结局、变量、质量和中止条件。
- `docs/life-path-variable-dictionary-nhats.md`：NHATS 变量家族字典草案，把设计变量、死亡边界、功能、认知、资源支持、环境和有效时间代理指标映射到生命路径模型角色。
- `docs/life-path-extraction-manifest-nhats-draft.md`：NHATS 提取清单草案，把文件名、变量名、权重、缺失码、访问层级、endpoint、允许输出和中止条件作为写抽取脚本前的准入门。
- `docs/nhats-colectica-capture-packet-runbook.md`：NHATS Colectica 捕获包人工执行 runbook，把 capture task register、authenticated template 和 validator 串成第一个 redacted `reviewable-but-still-blocked` packet 工作流；它不保存凭据、原始标签、行级数据、公开输出、校准证据或个体预测材料。
- `data/manual/life_path_nhats_survey_design_protocol.json`：NHATS survey-design 协议，要求权重、分层、PSU/variance unit、方差方法、domain rule、missingness route、round linkage 和披露验证全部就绪后才允许加权估计。
- `data/manual/life_path_nhats_survey_design_test_cases.json`：NHATS survey-design 合成测试集，只验证 synthetic design-plan envelope 的 allow/block 行为，不包含真实 NHATS 权重、路由或参与者数据。
- `scripts/validate_nhats_survey_design_plan.py`：NHATS survey-design 验证器，生成 `web/src/data/life-path-nhats-survey-design-validation.json`，证明缺权重、缺分层、缺 PSU、缺方差方法或提前公共推断时必须阻断。
- `docs/collection-run-*.md`：历史采集记录和质量风险。
- `data/manual/interventions.json`：首批 20 个干预对象、类别、别名和检索词。
- `data/manual/higher_order_effects.tsv`：LEV 二阶 / 多阶效应模型输入，供 Web 导出脚本生成多阶飞轮图。
- `data/manual/lev_route_cards.tsv`：R1-R9 主流路线卡模型输入，供 Web 导出脚本生成路线矩阵和概率门图。
- `data/manual/life_path_toy_model_scenarios.json`：生命路径 toy model 的合成场景输入，定义基线风险、健康质量、场景控制值和 LEV 阈值压力测试。
- `data/manual/life_path_public_mortality_anchor.json`：NCHS 2021 U.S. Life Tables 的公开聚合死亡率锚点，用于 baseline hazard plausibility comparison；它不包含个人数据，不授权校准预测、干预效果估计或个体死亡日期输出。
- `data/manual/life_path_nhanes_public_lmf_aggregate_pilot.json`：CDC/NCHS NHANES 2017-2018 DEMO 与 2019 public-use Linked Mortality File 的 sex × age band 粗聚合试运行输出；它只证明公开真实数据聚合管线可运行，不证明 survey-weighted inference、校准预测、因果效应、医学建议或个体死亡日期输出。
- `data/manual/life_path_nhanes_public_lmf_survey_design_readiness.json`：NHANES public-use LMF survey-design readiness 契约；它只证明 WTMEC2YR、SDMVPSU、SDMVSTRA 官方字段和诊断边界已登记，不证明加权人口推断、design-based confidence interval、校准或个体预测。
- `data/manual/life_path_nhanes_public_lmf_domain_subpopulation_rule_readiness.json`：NHANES public-use LMF domain/subpopulation rule readiness 契约；它只证明官方 domain/subpopulation 机制和禁止 row-drop subgroup filtering 的边界已登记，不证明 weighted domain inference、design-based confidence interval、校准或个体预测。
- `data/manual/life_path_nhanes_public_lmf_eligible_base_readiness.json`：NHANES public-use LMF positive-weight eligible-base readiness 契约；它只证明 `WTMEC2YR > 0` eligible-base 诊断、no-row-persistence 和 no-row-drop 边界已登记，不证明 weighted domain inference、design-based confidence interval、校准或个体预测。
- `data/manual/life_path_nhanes_public_lmf_weighted_estimator_readiness.json`：NHANES public-use LMF weighted-estimator readiness 契约；它只选择 R `survey` / `svydesign` 后端并绑定 design-object / domain indicator 合约，不证明 R runtime smoke、weighted domain output、design-based interval、校准或个体预测。
- `data/manual/life_path_nhanes_public_lmf_r_survey_runtime_smoke_readiness.json`：NHANES public-use LMF R `survey` runtime smoke readiness 契约；它只允许探测当前环境是否具备 `Rscript`、`survey` 包和 synthetic `svydesign` / domain `subset` smoke 能力，不证明 weighted domain output、design-based interval、校准或个体预测。
- `data/manual/life_path_nhanes_public_lmf_domain_indicator_diagnostic.json`：NHANES public-use LMF domain indicator metadata diagnostic 契约；它只验证 8 个 sex × ageBand 聚合域组合覆盖和 no-row / no-count / no-weighted-output 边界，不证明 DOF、披露、weighted domain output、校准或个体预测。
- `data/manual/life_path_nhanes_public_lmf_dof_sparse_domain_diagnostic.json`：NHANES public-use LMF DOF / sparse-domain metadata diagnostic 契约；它只验证 8 个 sex × ageBand 公开聚合域的 represented DOF、lonely represented strata、empty domain、sparse-domain flags 和 no-row/no-count/no-weighted-output 边界，不证明披露、weighted domain output、校准或个体预测。
- `data/manual/life_path_nhanes_public_lmf_disclosure_output_envelope_policy.json`：NHANES public-use LMF synthetic disclosure output envelope policy；它只定义合成输出形状的 allow/block、small-cell suppression、low-DOF suppression、禁止行级/标识符/public AI/真实加权输出边界，不授权真实公开输出。
- `data/manual/life_path_nhanes_public_lmf_disclosure_output_envelope_test_cases.json`：NHANES public-use LMF disclosure envelope 合成测试集；它只验证安全输出形状和阻断 unsafe shapes，不包含真实 NHANES 输出或个体数据。
- `data/manual/life_path_nhanes_public_lmf_effective_sample_ci_publication_policy.json`：NHANES public-use LMF synthetic effective sample / CI publication policy；它只定义合成发布可靠性形状的 allow/block、effective sample class、CI width class、RSE、DOF 和真实输出禁止边界，不授权真实发布许可。
- `data/manual/life_path_nhanes_public_lmf_effective_sample_ci_publication_test_cases.json`：NHANES public-use LMF effective sample / CI publication 合成测试集；它只验证 publication reliability shape，不包含真实 NHANES 输出、真实置信区间或个体数据。
- `data/manual/life_path_nhanes_public_lmf_weighted_output_implementation_preflight_policy.json`：NHANES public-use LMF synthetic weighted-output implementation preflight policy；它只定义 future implementation shape、R `survey` / `svydesign` / post-design `survey::subset`、forbidden keys、forbidden output types、no row persistence 和 no-real-output 边界，不授权真实加权输出。
- `data/manual/life_path_nhanes_public_lmf_weighted_output_implementation_preflight_test_cases.json`：NHANES public-use LMF weighted-output implementation preflight 合成测试集；它只验证 estimator-plan shape，不包含真实 NHANES 输出、真实置信区间或个体数据。
- `data/manual/life_path_nhanes_public_lmf_disclosure_review_template.json`：NHANES public-use LMF disclosure review template；它只登记真实公开输出前必须填写的 15 个 pending review slots、second-reviewer、output hash、suppression review、effective sample / CI review、forbidden-field scan、retention plan 和 release decision，不完成真实 disclosure review。
- `data/manual/life_path_nhanes_public_lmf_disclosure_review_execution_register.json`：NHANES public-use LMF disclosure review execution register；它只登记真实公开输出前的人工 review 状态机、15 个 slot 执行状态、reviewed output hash、second-reviewer signoff、release decision 和 no-real-output 边界，当前 0 个 completed human-review slots，继续阻塞公开输出。
- `data/manual/life_path_nhanes_public_lmf_local_run_evidence_manifest.json`：NHANES public-use LMF 本地运行证据清单；它把 ignored 本地真实 weighted-domain run、local disclosure packet 和 packet-validation 的哈希、运行环境、redacted summary、8 个审计 cells、minimum DOF 15、0 个 human-reviewed slots 和 public-output blocked 边界带入版本库，但不保存真实 rates、standard errors、confidence intervals 或行级数据。
- `data/manual/life_path_nhanes_public_lmf_weighted_domain_output_readiness.json`：NHANES public-use LMF weighted-domain output safety gate；它只登记 domain indicator、DOF / sparse-domain metadata diagnostic、synthetic disclosure envelope、synthetic effective sample / CI publication criteria、synthetic implementation preflight、disclosure review template、disclosure review execution register、local-only ignored run 和 real disclosure / output implementation 前置门，其中 disclosure review template、execution register 与 local-only run runway 已 ready，真实 disclosure review 仍阻塞 public weighted domain output、design-based interval、校准和个体预测；默认 readiness 审计必须独立于 ignored local run / packet outputs，干净 checkout 可以没有 `build/reports/`。
- `runtime/README.md`：说明本域可复现 runtime 配置的职责、默认本地环境位置、禁止保存真实环境和禁止处理行级数据的边界。
- `runtime/nhanes-public-lmf-r-survey-conda.yml`：NHANES public-use LMF R `survey` synthetic smoke 的 conda 环境契约，固定 R `4.3.3` 与 `r-survey` 依赖；实际环境创建在仓库根目录 `.runtime/nhanes-r-survey/`，不进入版本库。
- `data/manual/life_path_calibration_readiness.json`：生命路径模型的校准预备契约，记录 target population、time zero、outcome、estimand、data requirement、validation、calibration、sensitivity、bias/applicability、reporting 和 prohibited use 字段；它证明下一阶段要补什么，不证明当前模型已校准。
- `data/manual/life_path_data_source_candidates.json`：生命路径模型的候选数据源注册表，记录官方队列入口、可能模型角色、覆盖标签、访问治理状态和禁止外推边界；它只证明后续数据源搜索空间已被登记，不证明数据已访问、模型已校准或因果效应成立。
- `data/manual/life_path_nhats_acquisition_readiness.json`：NHATS acquisition readiness 机器契约，记录官方来源刷新、注册状态、文件层级、Colectica 变量确认、round window、survey design、endpoint、披露控制、AI 边界、存储销毁和禁止动作；它只证明提取前准入条件被机器化审计，当前仍是 `cannot-extract-yet`。
- `data/manual/life_path_nhats_official_source_refresh_register.json`：NHATS official source refresh 寄存器，记录官方 Data Access、Cross-Year Search、Conditions of Use、R13/R14 文件页、Colectica 技术指南和 2026-07-04 live reprobe 的 HTTP 状态、内容长度、SHA-256、标题与 PDF HEAD 元数据；它只把 official-source-refresh 门升为 ready，不授权下载、抽取、校准或个体预测。
- `data/manual/life_path_nhats_registration_evidence_template.json`：NHATS registration evidence 模板，固定 redacted 账号状态、允许用户边界、使用条款确认、public-use file access tier、restricted approval boundary、controlled workspace linkage、no-public-secret-storage 和二次复核槽；它只把 registration-status 推进为 template-only partial，不证明注册完成。
- `data/manual/life_path_nhats_registration_evidence_packet_validator_test_cases.json`：NHATS registration evidence packet validator 合成测试集，固定 6 个 future packet 预检用例，确保格式正确的注册证据包也只能进入 `reviewable-but-still-blocked`、`cannot-evaluate` 或 `rejected`。
- `scripts/validate_nhats_registration_evidence_template.py`：读取 NHATS registration evidence 模板，生成 `web/src/data/life-path-nhats-registration-evidence-template-validation.json`，验证 8 个证据槽和 no-registration-proof / no-download / no-extraction / no-calibration / no-individual-prediction 边界。
- `scripts/validate_nhats_registration_evidence_packet_validator.py`：读取 NHATS registration evidence packet validator 合成测试集和注册证据模板，生成 `web/src/data/life-path-nhats-registration-evidence-packet-validator-validation.json`，验证未来注册证据包不会绕过真实注册、下载、抽取、raw data、public AI、校准或个体预测阻塞门。
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
- `data/manual/life_path_nhats_colectica_access_route_probe_register.json`：NHATS Colectica access-route probe 登记，记录官方 Cross-Year Search 入口、匿名访问登录边界、2026-07-04 anonymous live reprobe、technical guide freshness probe、技术指南 SHA-256、Details/Basket capture workflow 和后续受控登录捕获步骤；它只证明访问路线已探测，不证明账号、登录、变量页、value labels、question text、导出、校准或个体预测已完成。
- `data/manual/life_path_nhats_colectica_authenticated_capture_template.json`：NHATS Colectica 受控登录后变量页捕获模板，记录 route field 进入 value-label 复核前必须补齐的 item id、变量名、文件名、Details URL、source hash、question text、universe/skip logic、变量级缺失码和二次复核槽位；它只证明捕获证据结构已固定，不证明登录、捕获、标签确认、route classifier、公开导出、校准或个体预测已完成。
- `data/manual/life_path_nhats_colectica_capture_task_register.json`：NHATS Colectica capture task register，把 authenticated capture template 展开为 9 个 route-field 组和 39 个 pending 变量 / 输出任务，仍阻塞登录、变量页捕获、值标签确认、真实分类器、提取、校准和个体预测。
- `data/manual/life_path_nhats_colectica_capture_packet_validator_test_cases.json`：NHATS Colectica capture packet validator 合成测试集，验证未来捕获包只能进入 `reviewable-but-still-blocked`、`cannot-evaluate` 或 `rejected`；它只证明预检拒绝规则可运行，不代表真实登录、捕获、人审、slot closure 或模型准入完成。
- `data/manual/life_path_nhats_colectica_capture_packet_review_execution_register.json`：NHATS Colectica capture-packet review execution register，登记 39 个 pending 捕获包审查槽位、0 个真实包、0 个二审、0 个关闭槽和 0 个模型准入；它只提供未来人工证据进入审查的执行账本，不代表真实登录、字段确认、slot closure、route classifier、提取、校准或个体预测完成。
- `data/manual/life_path_nhats_route_value_crosswalk_assembly_protocol.json`：NHATS route-value crosswalk assembly 协议，绑定 capture task、capture-packet review execution、value-label execution 和 route-classifier readiness，定义 9 个 assembly units 与 0 准入状态；它只证明 crosswalk 装配门可审计，不代表 route-value rows、变量级 missing-code map、二次复核、真实分类器、提取、校准或个体预测完成。
- `data/manual/life_path_nhats_route_value_crosswalk_entry_validator_test_cases.json`：NHATS route-value crosswalk entry validator 合成测试集，验证未来 route-value / missing-code entry 只能进入 `reviewable-but-still-blocked`、`cannot-evaluate` 或 `rejected`；它只证明未来条目预检可审计，不代表真实 crosswalk 行、assembly unit closure、route classifier、提取、校准或个体预测完成。
- `data/manual/life_path_nhats_route_classifier_readiness.json`：NHATS route-classifier readiness 契约，记录 9 个分类器输入族、12 个晋升门、上游 route-field / Colectica / missingness / pre-outcome 绑定和禁止动作；它只证明真实 route classifier 前的阻塞门已机器化，不授权分类器代码、真实提取、聚合、加权估计、校准或个体预测。
- `data/manual/life_path_nhats_l2_variable_family_admission_register.json`：NHATS L2 变量族准入前映射，绑定第一版窄 estimand、变量确认矩阵、模型准入契约和候选注册表，把 6 个候选变量族固定为 L2-only；它不确认精确字段、不授权真实提取、校准或个体预测。
- `data/manual/life_path_nhats_preoutcome_aggregation_protocol.json`：NHATS 预结果聚合协议，冻结 8 条 L2-only 聚合规则、7 个合成用例和真实聚合前置证据要求；它不授权真实 NHATS 聚合、加权估计、公开导出、L4 准入、校准或个体预测。
- `data/manual/life_path_nhats_l4_readiness_runway.json`：NHATS L4 readiness runway，把 R13/R14 从 L2 设计资产推进到 L4 aggregate-calibrated research model 前必须通过的 12 个 readiness gates 串成一条可审计路线；当前状态仍是 `runway-only-l4-blocked`。
- `data/raw/`：采集脚本保存的原始 API 响应和下载快照。
- `data/processed/`：采集脚本生成的 JSONL 索引和汇总。
- `scripts/collect_mvp_data.py`：采集 PubMed、OpenAlex、ClinicalTrials.gov 和 openFDA 标签数据。
- `scripts/collect_core_data.py`：采集 HAGR、PubChem、openFDA event 和 Drugs@FDA 数据。
- `scripts/build_public_mortality_anchor.py`：从 NCHS 官方 xlsx 生命表生成公开聚合死亡率锚点。
- `scripts/validate_public_mortality_anchor.py`：离线审计公开聚合死亡率锚点的 schema、来源、年龄范围、列值和禁止用途边界。
- `scripts/build_nhanes_public_lmf_aggregate_pilot.py`：从 CDC/NCHS 官方 public-use NHANES LMF 和 DEMO XPT 临时下载、内存连接并只导出粗聚合单元；不得持久化行级数据。
- `scripts/validate_nhanes_public_lmf_aggregate_pilot.py`：验证 NHANES public-use LMF 聚合输出和验证报告，保证 source hash、聚合计数和禁止用途边界未漂移。
- `scripts/validate_nhanes_public_lmf_survey_design_readiness.py`：验证 NHANES public-use LMF survey-design readiness 契约和 Web 验证报告，保证 design-field readiness 不被误写成 survey-weighted inference。
- `scripts/validate_nhanes_public_lmf_domain_subpopulation_rule_readiness.py`：验证 NHANES public-use LMF domain/subpopulation rule readiness 契约和 Web 验证报告，保证官方 domain 规则不会被误写成 weighted domain inference。
- `scripts/validate_nhanes_public_lmf_eligible_base_readiness.py`：验证 NHANES public-use LMF positive-weight eligible-base readiness 契约和 Web 验证报告，保证 `WTMEC2YR > 0` eligible-base 诊断不会被误写成 weighted domain inference 或个体预测。
- `scripts/validate_nhanes_public_lmf_weighted_estimator_readiness.py`：验证 NHANES public-use LMF weighted-estimator readiness 契约和 Web 验证报告，保证 R `survey` / `svydesign` 后端选择不会被误写成真实 weighted domain output 或模型校准。
- `scripts/validate_nhanes_public_lmf_r_survey_runtime_smoke.py`：探测并验证 NHANES public-use LMF R `survey` runtime smoke readiness，当前只在 synthetic data 上检查 `Rscript` / `survey` / `svydesign` 可用性，并继续阻塞真实 NHANES weighted domain output、校准和个体预测。
- `scripts/run_nhanes_public_lmf_r_survey_controlled_runtime_smoke.sh`：使用 `runtime/nhanes-public-lmf-r-survey-conda.yml` 创建或修复本地 controlled conda prefix，再运行 synthetic-only runtime smoke 并导出 controlled validation JSON；它不得加入默认 `make check`，避免默认审计下载或安装 R 依赖。
- `scripts/validate_nhanes_public_lmf_domain_indicator_diagnostic.py`：验证 NHANES public-use LMF domain indicator metadata diagnostic 契约和 Web 验证报告，保证 domain 覆盖检查不重复公开计数、加权和、区间、原始行或个体行。
- `scripts/validate_nhanes_public_lmf_dof_sparse_domain_diagnostic.py`：验证 NHANES public-use LMF DOF / sparse-domain metadata diagnostic 契约和 Web 验证报告，保证 DOF、lonely represented strata、empty domain 和 sparse-domain 检查不持久化行、逐域计数、逐域加权和、rates 或 intervals。
- `scripts/validate_nhanes_public_lmf_disclosure_output_envelope.py`：验证 NHANES public-use LMF disclosure output envelope policy、合成测试集和 Web 验证报告，保证 safe synthetic aggregate shape 可通过、small-cell / low-DOF / row-level / identifier / public-AI / real-output 形状被阻断。
- `scripts/validate_nhanes_public_lmf_effective_sample_ci_publication.py`：验证 NHANES public-use LMF effective sample / CI publication policy、合成测试集和 Web 验证报告，保证 publication-ready synthetic shape 可通过，低 effective sample class、unacceptable RSE、unacceptable CI width、低 DOF、真实 CI、public-AI 和 real-output 形状被阻断。
- `scripts/validate_nhanes_public_lmf_weighted_output_implementation_preflight.py`：验证 NHANES public-use LMF weighted-output implementation preflight policy、合成测试集和 Web 验证报告，保证安全 synthetic estimator-plan shape 可通过，row-level、row-drop-before-design、真实 weighted rate、public-AI、count key 和 individual-output 形状被阻断。
- `scripts/validate_nhanes_public_lmf_disclosure_review_template.py`：验证 NHANES public-use LMF disclosure review template 和 Web 验证报告，保证 15 个 disclosure review slots 仍全部 pending，并继续阻塞真实 public weighted-domain output、design-based interval、校准和个体预测。
- `scripts/validate_nhanes_public_lmf_disclosure_review_execution.py`：验证 NHANES public-use LMF disclosure review execution register 和 Web 验证报告，保证 15 个 review slots 存在、8 个 machine-prefill-eligible slots、0 个 completed human-review slots、无 reviewed output hash、无 second-reviewer signoff，且 release 继续 blocked。
- `scripts/validate_nhanes_public_lmf_weighted_domain_output_readiness.py`：验证 NHANES public-use LMF weighted-domain output readiness 契约和 Web 验证报告，保证 controlled runtime smoke 不会被误写成 public NHANES weighted domain output，且 domain indicator、DOF / sparse-domain metadata、synthetic disclosure envelope、synthetic publication criteria、synthetic implementation preflight、disclosure review template、disclosure review execution register 和 real disclosure / output implementation gates 仍按边界阻塞输出；它还强制默认检查不要求 ignored local run / packet / packet-validation 存在。
- `scripts/run_nhanes_public_lmf_weighted_domain_output_local.py`：显式本地运行 NHANES public-use LMF weighted-domain analysis，输出只允许进入 ignored `build/reports/`，禁止进入 `web/src/data` 或版本库。
- `scripts/validate_nhanes_public_lmf_weighted_domain_output_local_run.py`：验证 local-only report 的路径、schema、8 个域、minimum domain DOF、禁止 row/count-like key、禁止 public export / calibration / individual prediction 边界。
- `scripts/build_nhanes_public_lmf_local_disclosure_review_packet.py`：从 ignored local-only weighted-domain report 生成本地 disclosure review packet，只绑定输入 hash、来源 hash、runtime trace、redacted summary 和 15 个 review slots，不复制真实 rates、standard errors 或 intervals。
- `scripts/validate_nhanes_public_lmf_local_disclosure_review_packet.py`：验证本地 disclosure review packet 和 ignored packet-validation，确保 packet 仍在 `build/reports/`、不写 `web/src/data`、不完成 human review、不授权公开输出、校准或个体预测。
- `scripts/validate_nhanes_public_lmf_local_run_evidence_manifest.py`：验证版本化 local run evidence manifest 和 Web validation，确保仓库只保存 hash / runtime / redacted summary / blocked release 边界，不保存真实 weighted rates、standard errors、confidence intervals 或行级数据；该审计进入默认 `make check`。
- `scripts/validate_nhanes_public_lmf_public_web_data_no_real_values.py`：扫描 `web/src/data/life-path-nhanes-public-lmf-*.json` 公开前端数据，确保真实 weighted rates、standard errors、confidence intervals、行级字段、个体预测字段和越界 release/calibration flags 不会进入 Web 数据层；该审计进入默认 `make check`。
- `scripts/validate_nhats_registration_evidence_template.py`：读取 NHATS registration evidence 模板，生成 `web/src/data/life-path-nhats-registration-evidence-template-validation.json`，把注册/访问证据槽、redacted-only 仓库边界和禁止真实下载/抽取/校准/个体预测边界纳入默认审计。
- `scripts/validate_nhats_registration_evidence_packet_validator.py`：读取 registration evidence packet validator 合成测试集，生成 `web/src/data/life-path-nhats-registration-evidence-packet-validator-validation.json`，把未来注册证据包的 rejected / cannot-evaluate / reviewable-but-still-blocked 预检语义纳入默认审计。
- `scripts/validate_nhats_acquisition_readiness.py`：读取 NHATS acquisition readiness 机器契约，生成 `web/src/data/life-path-nhats-acquisition-readiness-validation.json`，把注册模板、文件层级、Colectica、survey design、endpoint、披露控制、AI 边界和存储销毁缺口纳入默认审计。
- `scripts/validate_nhats_official_source_refresh.py`：读取 NHATS official source refresh 寄存器，生成 `web/src/data/life-path-nhats-official-source-refresh-validation.json`，验证 8 个官方公开来源的状态、hash、2026-07-04 live reprobe、支持范围和禁止用途边界。
- `scripts/run_life_path_toy_model.py`：读取合成场景并导出 `web/src/data/life-path-toy-model.json`，用于 `/model/` 的最小可运行定量展示。
- `scripts/run_life_path_sensitivity_analysis.py`：读取合成场景和已导出的 toy model，生成 `web/src/data/life-path-sensitivity-analysis.json`，用于一因素扰动检查场景排序、开放边界和最敏感参数。
- `scripts/build_life_path_synthetic_validation_calibration_report.py`：读取生命路径 toy model、合成敏感性分析和 L4 验证/校准报告契约，生成 `web/src/data/life-path-synthetic-validation-calibration-report.json` / `.md`，演练 12 个报告章节和 5 个 L4 槽位的机器可审计形状；它不授权真实验证、真实校准、L4 准入、公开加权输出或个体预测。
- `scripts/build_life_path_l4_synthetic_evidence_packet_dry_run.py`：读取 L4 evidence intake register、packet review playbook 和合成验证/校准报告 dry-run，生成 `web/src/data/life-path-l4-synthetic-evidence-packet-dry-run.json` / `.md`，演练 24 个 pending slot 的 hash-only draft packet 形状；它不授权 direct evidence、人审完成、slot closure、L4 准入、公开加权输出或个体预测。
- `scripts/validate_nhats_disclosure_outputs.py`：读取 NHATS 披露控制策略和合成测试用例，生成 `web/src/data/life-path-nhats-disclosure-control-validation.json`，验证 aggregate-only、small-cell suppression、row-level block、public AI block 和 forbidden output type 规则。
- `scripts/validate_nhats_route_field_discovery.py`：读取 NHATS route-field discovery register，生成 `web/src/data/life-path-nhats-route-field-discovery-validation.json`，验证官方字段发现仍然保持 Colectica、数据访问、分类器、加权统计、公开导出、校准和个体预测阻塞。
- `scripts/validate_nhats_colectica_value_label_protocol.py`：读取 NHATS Colectica value-label review protocol，生成 `web/src/data/life-path-nhats-colectica-value-label-validation.json`，验证 value labels、question text、skip logic、route crosswalk、classifier、weighted counts、public export、calibration 和 individual prediction 仍被阻塞。
- `scripts/validate_nhats_colectica_value_label_review_execution.py`：读取 NHATS Colectica value-label review execution register，生成 `web/src/data/life-path-nhats-colectica-value-label-review-execution-validation.json`，验证第一轮执行登记只打开 source trace / negative-code family 证据，不打开 value labels、route map、classifier、weighted counts、public export、calibration 或 individual prediction。
- `scripts/validate_nhats_colectica_access_route_probe.py`：读取 NHATS Colectica access-route probe register，生成 `web/src/data/life-path-nhats-colectica-access-route-probe-validation.json`，验证公开入口、匿名登录边界、2026-07-04 anonymous live reprobe、technical guide freshness probe、技术指南 workflow 和受控 capture sequence，同时继续阻塞 authenticated capture、value labels、exports、calibration 和 individual prediction。
- `scripts/validate_nhats_colectica_authenticated_capture_template.py`：读取 NHATS Colectica authenticated capture template，生成 `web/src/data/life-path-nhats-colectica-authenticated-capture-template-validation.json`，验证受控登录后变量页捕获槽、敏感死亡字段排除、source hash 证据要求和二次复核门，同时继续阻塞账号状态、登录、变量页实捕获、value labels、route classifier、公开导出、校准和 individual prediction。
- `scripts/validate_nhats_colectica_capture_task_register.py`：读取 NHATS Colectica capture task register，生成 `web/src/data/life-path-nhats-colectica-capture-task-register-validation.json`，验证 9 个 route-field 组和 39 个 pending 任务覆盖 capture template，同时继续阻塞登录、实捕获、真实分类器、提取、校准和 individual prediction。
- `scripts/validate_nhats_colectica_capture_packet_validator.py`：读取 NHATS Colectica capture packet validator 合成测试集、capture template、capture task register 和 route-classifier readiness，生成 `web/src/data/life-path-nhats-colectica-capture-packet-validator-validation.json`，验证未来捕获包预检只输出 `reviewable-but-still-blocked`、`cannot-evaluate` 或 `rejected`，并继续阻塞 slot closure、真实分类器、提取、公开导出、校准和 individual prediction。
- `scripts/build_nhats_colectica_capture_packet_draft.py`：默认为 39 个 NHATS Colectica capture task 批量生成 ignored fail-closed 草稿、逐项 draft validation 和批量 summary；复用 packet validator 证明草稿不会打开真实捕获、slot closure、route classifier、提取、校准或个体预测。
- `scripts/build_nhats_colectica_capture_packet_review_handoff.py`：读取 ignored draft 目录和 validator 依赖，默认为所有 draft 批量生成 ignored review handoff 报告；只有 `reviewable-but-still-blocked` 包才可进入 handoff-ready 状态，但仍不写 tracked review execution register、不关闭 slot、不打开 route classifier、提取、校准或个体预测。
- `scripts/validate_nhats_colectica_capture_packet_review_execution.py`：读取 NHATS Colectica capture-packet review execution register，生成 `web/src/data/life-path-nhats-colectica-capture-packet-review-execution-validation.json`，验证 39 个 review slots 仍为 pending 且 0 个真实包、0 个二审、0 个 slot closure、0 个 route classifier/extraction/calibration admission。
- `scripts/validate_nhats_route_value_crosswalk_assembly.py`：读取 NHATS route-value crosswalk assembly 协议，生成 `web/src/data/life-path-nhats-route-value-crosswalk-assembly-validation.json`，验证 9 个 assembly units、capture task 覆盖、上游 hash、敏感 death-date 排除和全部 0 准入状态，同时继续阻塞 route-value rows、missing-code maps、slot closure、route classifier、extraction、calibration 和 individual prediction。
- `scripts/validate_nhats_route_value_crosswalk_entry_validator.py`：读取 NHATS route-value crosswalk entry validator 合成测试集、assembly 协议、capture-packet review execution、capture task register 和 route-classifier readiness，生成 `web/src/data/life-path-nhats-route-value-crosswalk-entry-validator-validation.json`，验证未来 crosswalk 条目预检只输出 `reviewable-but-still-blocked`、`cannot-evaluate` 或 `rejected`，并继续阻塞 assembly unit closure、真实分类器、提取、公开导出、校准和 individual prediction。
- `scripts/build_nhats_route_value_crosswalk_entry_draft.py`：生成 ignored NHATS route-value crosswalk entry fail-closed 草稿和 draft validation，默认针对 `identity_join_key`，复用 entry validator 证明草稿不会打开 assembly unit closure、route classifier、提取、公开导出、校准或 individual prediction。
- `scripts/build_nhats_route_value_crosswalk_entry_review_handoff.py`：读取一个 NHATS route-value crosswalk entry 和 validator 依赖，生成 ignored review handoff 报告；只有 `reviewable-but-still-blocked` entry 才可进入 handoff-ready 状态，但仍不写 tracked assembly / route-classifier register、不关闭模型准入。
- `scripts/build_nhats_route_classifier_synthetic_dry_run.py`：读取 missingness-route 合成用例、route-classifier readiness 和 route-value crosswalk handoff，生成 ignored synthetic dry-run 报告和 tracked `web/src/data/life-path-nhats-route-classifier-synthetic-dry-run-validation.json`；它只证明 route envelope 逻辑可以用合成用例 fail-closed 运行，仍不打开真实 route classifier、extraction、weighted counts、public export、calibration、individual prediction 或 `modelG4`，并由总 toy model audit 消费 tracked validation。
- `scripts/validate_nhats_route_classifier_readiness.py`：读取 NHATS route-classifier readiness 契约，生成 `web/src/data/life-path-nhats-route-classifier-readiness-validation.json`，验证真实 route classifier 仍被 Colectica value labels、route-value crosswalk、变量级 missing-code map、真实数据访问、survey design、披露审查和二次复核门阻塞。
- `scripts/validate_nhats_l2_variable_family_admission.py`：读取 NHATS L2 变量族准入前映射，生成 `web/src/data/life-path-nhats-l2-variable-family-admission-validation.json`，验证窄 estimand、6 个 L2 候选变量族、来源 hash、L4/L5 阻塞门和禁止抽取 / 校准 / 个体预测边界。
- `scripts/validate_nhats_preoutcome_aggregation_protocol.py`：读取 NHATS 预结果聚合协议，生成 `web/src/data/life-path-nhats-preoutcome-aggregation-validation.json`，验证 8 条 L2-only 聚合规则、7 个合成用例、上游 source hash 和真实聚合 / 加权估计 / L4 准入 / 校准 / 个体预测阻塞边界。
- `scripts/validate_nhats_l4_readiness_runway.py`：读取 NHATS L4 readiness runway，生成 `web/src/data/life-path-nhats-l4-readiness-runway-validation.json`，验证 12 个 runway gates、上游 source hash、L4 阻塞状态和禁止真实提取 / 校准 / 个体预测边界。
- `scripts/audit_life_path_toy_model.py`：审计生成后的生命路径 toy model、合成敏感性分析、校准预备契约、候选数据源注册表、数据源 Source Cards、Data Card 模板、NHATS Data Card、NHATS 变量字典、NHATS extraction manifest、NHATS registration evidence 模板与 validation、NHATS acquisition readiness 机器契约、NHATS acquisition-readiness validation、NHATS controlled storage/destruction validation、NHATS synthetic storage/destruction drill validation、NHATS file-tier table 与 file-tier validation、NHATS first estimand protocol、NHATS variable confirmation matrix、NHATS cohort-flow endpoint protocol、NHATS disclosure-control validation、NHATS survey-design validation、NHATS missingness-route validation、NHATS route-field discovery validation、NHATS Colectica value-label validation、NHATS Colectica value-label execution validation、NHATS Colectica access-route probe validation、NHATS Colectica authenticated capture template validation、NHATS route-value crosswalk assembly validation、NHATS route-value crosswalk entry validator validation、NHATS route-classifier readiness validation、NHATS L2 variable-family admission validation 和 NHATS pre-outcome aggregation validation，输出机器可读 JSON 和人可读 Markdown，检查模型卡、来源 hash、生存曲线、概率范围、LEV 开放边界、敏感性参数覆盖、校准预备字段、候选数据源治理边界、数据卡准入文档、提取前治理门禁、注册证据模板边界、准入门机器化状态、acquisition-readiness validator、受控存储/销毁 validator、合成销毁演练 validator、文件层级覆盖与 file-tier validation、第一版 estimand 研究设计门、变量确认门、队列流转/终点路由/披露控制门、合成 disclosure/survey/missingness validator 结果、官方字段发现边界、Colectica 复核协议门、Colectica 第一轮执行登记边界、Colectica 访问路线边界、Colectica authenticated capture 模板边界、route-value assembly 阻塞门、route-value entry validator 阻塞门、route-classifier readiness 阻塞门、L2 变量族准入前映射边界、预结果聚合规则边界和禁止个体死亡日期字段。

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
- 2026-07-04：新增 `life_path_nhats_registration_evidence_packet_validator_test_cases.json`、`validate_nhats_registration_evidence_packet_validator.py` 和 `life-path-nhats-registration-evidence-packet-validator-validation.json`，把 NHATS 注册证据包预检语义纳入默认审计；该门只验证未来包形状和拒绝规则，仍阻塞真实注册证明、下载、抽取、校准和个体预测。
- 2026-07-03：新增 `life_path_nhats_controlled_storage_destruction_plan.json`、`validate_nhats_controlled_storage_destruction_plan.py` 和 `life-path-nhats-controlled-storage-destruction-validation.json`，把 NHATS 受控存储/销毁计划接入默认审计；该 gate 仍只允许 partial，继续阻塞真实下载和抽取。
- 2026-07-03：新增 `life_path_nhats_synthetic_storage_destruction_drill.json`、`validate_nhats_synthetic_storage_destruction_drill.py` 和 `life-path-nhats-synthetic-storage-destruction-drill-validation.json`，把 NHATS 合成存储/销毁演练接入默认审计；它只证明 dry-run 机制，仍不打开真实下载、抽取或校准。
- 2026-07-03：新增 `life_path_nhats_l4_readiness_runway.json`、`validate_nhats_l4_readiness_runway.py` 和 `life-path-nhats-l4-readiness-runway-validation.json`，把 NHATS L4 readiness runway 接入默认审计；它只证明 12 个阻塞门可审计，不打开真实提取、校准或个体预测。
- 2026-07-03：新增 `life_path_nhats_official_source_refresh_register.json`、`validate_nhats_official_source_refresh.py` 和 `life-path-nhats-official-source-refresh-validation.json`，把 NHATS 官方公开来源刷新接入默认审计；它只把 official-source-refresh 门升为 ready，其他 acquisition/L4 门继续阻塞。
- 2026-07-04：更新 `life_path_nhats_official_source_refresh_register.json`、`validate_nhats_official_source_refresh.py` 和 `life-path-nhats-official-source-refresh-validation.json`，补入 8 个官方公开入口的 live reprobe；该证据只证明入口可达，不证明 HTML 内容语义稳定、注册完成、下载许可、抽取许可、校准或个体预测。
- 2026-07-03：新增 `life_path_nhats_route_classifier_readiness.json`、`validate_nhats_route_classifier_readiness.py` 和 `life-path-nhats-route-classifier-readiness-validation.json`，把 NHATS route-classifier readiness 阻塞门接入默认审计；它只证明分类器前置证据缺口可机器审查，不打开真实分类器、提取、聚合、校准或个体预测。
- 2026-07-03：新增 `life_path_nhats_colectica_capture_task_register.json`、`validate_nhats_colectica_capture_task_register.py` 和 `life-path-nhats-colectica-capture-task-register-validation.json`，把 Colectica 变量页捕获任务清单接入默认审计；它只证明任务级捕获清单已准备，不打开登录、实捕获、分类器、提取、校准或个体预测。
- 2026-07-04：新增 `life_path_nhats_colectica_capture_packet_validator_test_cases.json`、`validate_nhats_colectica_capture_packet_validator.py` 和 `life-path-nhats-colectica-capture-packet-validator-validation.json`，把 Colectica 捕获包预检接入默认审计；它只证明未来捕获包拒绝规则可机器审查，不打开真实捕获、slot closure、分类器、提取、校准或个体预测。
- 2026-07-04：新增 `life_path_nhats_colectica_capture_packet_review_execution_register.json`、`validate_nhats_colectica_capture_packet_review_execution.py` 和 `life-path-nhats-colectica-capture-packet-review-execution-validation.json`，把 Colectica 捕获包审查执行账本接入默认审计；它只证明 39 个审查槽位可接收未来人工证据，不打开真实捕获、slot closure、分类器、提取、校准或个体预测。
- 2026-07-04：新增 `docs/nhats-colectica-capture-packet-runbook.md`，把 Colectica capture task register、authenticated template 和 packet validator 串成第一个 redacted capture packet 的人工执行流程；该 runbook 只支持生成 `reviewable-but-still-blocked` 形状证据，不打开真实捕获、slot closure、route classifier、提取、公开输出、校准或个体预测。
- 2026-07-04：新增并扩展 `build_nhats_colectica_capture_packet_draft.py` 和 `make nhats-colectica-capture-packet-draft-audit`，把 39 个 Colectica capture task 从人工 skeleton 推进到 ignored fail-closed 草稿批量生成；这些草稿仍不是真实捕获证据，不进入 tracked Web 数据层，也不打开 slot closure、route classifier、提取、公开输出、校准或个体预测。
- 2026-07-04：新增并扩展 `build_nhats_colectica_capture_packet_review_handoff.py` 和 `make nhats-colectica-capture-packet-review-handoff-audit`，把 39 个 Colectica packet validator 结果推进到 ignored review handoff 状态机；默认草稿仍为 `blocked-not-reviewable`，真实包即使 handoff-ready 也不能关闭 slot、改写 register、打开 route classifier、提取、校准或个体预测。
- 2026-07-04：新增 `life_path_nhats_route_value_crosswalk_entry_validator_test_cases.json`、`validate_nhats_route_value_crosswalk_entry_validator.py` 和 `life-path-nhats-route-value-crosswalk-entry-validator-validation.json`，把 route-value crosswalk 条目预检接入默认审计；它只证明未来条目可机器审查，不打开 assembly unit closure、真实 crosswalk、分类器、提取、校准或个体预测。
- 2026-07-04：新增 `build_nhats_route_value_crosswalk_entry_draft.py`、`build_nhats_route_value_crosswalk_entry_review_handoff.py`、`make nhats-route-value-crosswalk-entry-draft-audit` 和 `make nhats-route-value-crosswalk-entry-review-handoff-audit`，把 route-value crosswalk 条目从 validator 推进到 ignored fail-closed 草稿与 handoff 状态机；默认草稿仍为 `cannot-evaluate`，不会关闭 assembly unit、改写 tracked register、打开 route classifier、提取、校准或个体预测。
- 2026-07-04：新增并强化 `build_nhats_route_classifier_synthetic_dry_run.py` 和 `make nhats-route-classifier-synthetic-dry-run-audit`，把 route classifier 从纯 readiness 阻塞推进到合成 dry-run 执行门；该门生成 ignored 详细报告和 tracked public validation summary，只验证 synthetic route envelope 逻辑可运行，并继续阻塞真实分类器、真实提取、加权统计、公开导出、校准和个体预测。
- 2026-07-03：新增 `life_path_nhanes_public_lmf_domain_indicator_diagnostic.json`、`validate_nhanes_public_lmf_domain_indicator_diagnostic.py` 和 `life-path-nhanes-public-lmf-domain-indicator-diagnostic-validation.json`，把 NHANES domain indicator metadata gate 推进为 ready；它只验证聚合域覆盖和 no-row/no-count/no-weighted-output 边界，DOF、披露和 weighted-domain output 继续阻塞。
- 2026-07-03：新增 `life_path_nhanes_public_lmf_dof_sparse_domain_diagnostic.json`、`validate_nhanes_public_lmf_dof_sparse_domain_diagnostic.py` 和 `life-path-nhanes-public-lmf-dof-sparse-domain-diagnostic-validation.json`，把 NHANES DOF/sparse-domain metadata gate 推进为 ready；当时 weighted-domain output readiness 同步为 7 ready / 2 blocked，披露审查和输出实现继续阻塞。
- 2026-07-03：新增 NHANES public-use LMF disclosure output envelope policy、合成测试集、验证器和 Web validation，把 synthetic disclosure envelope gate 推进为 ready；weighted-domain output readiness 同步为 8 ready / 2 blocked，真实 disclosure review、有效样本量 / CI 发布审查和输出实现继续阻塞。
- 2026-07-03：新增 NHANES public-use LMF effective sample / CI publication policy、合成测试集、验证器和 Web validation，把 synthetic publication criteria gate 推进为 ready；weighted-domain output readiness 同步为 9 ready / 2 blocked，真实 disclosure review 和真实输出实现继续阻塞。
- 2026-07-03：新增 NHANES public-use LMF weighted-output implementation preflight policy、合成测试集、验证器和 Web validation，把 synthetic implementation preflight gate 推进为 ready；weighted-domain output readiness 同步为 10 ready / 2 blocked，真实 disclosure review 和真实输出实现继续阻塞。
- 2026-07-03：新增 NHANES public-use LMF disclosure review template、验证器和 Web validation，把 review-packet shape gate 推进为 ready；weighted-domain output readiness 同步为 11 ready / 2 blocked，真实 disclosure review 和真实输出实现继续阻塞。
- 2026-07-03：新增 NHANES public-use LMF local-only weighted-domain 运行器、验证器和 `make nhanes-public-lmf-weighted-domain-output-local-run-audit`，把真实 public-use weighted-domain 计算推进到 ignored 本地报告；默认 `make check` 不联网运行该 target，公开输出、disclosure review、校准和个体预测继续阻塞。
- 2026-07-03：新增 NHANES public-use LMF local disclosure review packet 生成器、验证器和 `make nhanes-public-lmf-local-disclosure-review-packet-audit`，把 ignored 本地 weighted-domain 报告推进到 hash-bound 审查包；packet 不复制真实 rates / intervals，不进入 `web/src/data`，人工 disclosure review、公开输出、校准和个体预测继续阻塞。验证器现在会把 redacted packet 审计结果写入 ignored `build/reports/nhanes-public-lmf-local-disclosure-review-packet/packet-validation.json`，保留可复核证据但仍不进入版本库。
- 2026-07-03：新增 NHANES public-use LMF disclosure review execution register、验证器、Web validation 和 `make nhanes-public-lmf-disclosure-review-execution-audit`，把人工审查执行状态机纳入默认门禁；weighted-domain output readiness 同步为 12 ready / 2 blocked，真实 disclosure review、公开输出、校准和个体预测继续阻塞。
- 2026-07-03：补强 NHANES weighted-domain output readiness 的 clean-checkout independence 契约；默认 readiness 审计和 `make check` 不读取 ignored local weighted run、disclosure packet 或 packet-validation，干净 checkout 缺少 `build/reports/` 仍应通过默认门禁。
- 2026-07-03：新增 NHANES public-use LMF local run evidence manifest、验证器、Web validation 和 `make nhanes-public-lmf-local-run-evidence-manifest-audit`，把 ignored 本地真实 weighted-domain run 与 disclosure packet 的哈希证明带入默认门禁；版本库仍不保存真实 rates / intervals，公开输出、校准和个体预测继续阻塞。
- 2026-07-03：新增 NHANES public-use LMF public Web data no-real-values 验证器、Web validation 和 `make nhanes-public-lmf-public-web-data-no-real-values-audit`，把公开前端 JSON 防泄漏扫描接入默认门禁；真实 rates、standard errors、confidence intervals、行级字段、个体预测字段和越界 release/calibration flags 继续禁止进入 `web/src/data`。
