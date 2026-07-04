# Longevity Evidence

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c1-boundary-rewriting/longevity-evidence` |
| 分级 | `C1` - 可能性边界改写层 |
| 控制轴 | 寿命边界 |
| 分级理由 | 直接承载延长寿命和长寿逃逸相关证据账本。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何直接改写主体持续性边界，例如寿命、死亡、时间差分、身份连续性或未来抵达能力？

```text
研究域对象
  -> 影响变量 / 中间机制
  -> 改变主体状态或外部条件
  -> 改变风险、能力、时间成本或可达性
  -> 改变有效寿命、有效时间或未来选择权
```

### 使用边界

- 本域是研究与建模单元，不是个体医疗、法律、金融、工程、教育或安全操作建议。
- 新增内容必须标明来源、适用对象、证据等级和不确定性；AI 总结不能作为事实源。
- 若内容会改变分级、目录位置或上下游关系，先更新 `domains/_possibility-space-control/classification.tsv`。
<!-- domain-standard:end -->

<!-- domain-research-skeleton:start -->
## 研究推进骨架

### 最小问题集

- 界定本域直接改写的主体持续性边界：寿命、死亡、身份连续性、时间差分或未来抵达能力。
- 说明主体连续性条件：身体、记忆、人格、行动能力或法律身份中哪些必须保持。
- 列出不可越过的中止门槛：退出失败、连续性失败、尾部风险、不可逆损伤或治理失效。
- 说明它如何改变有效寿命、有效时间、未来选择权或可能性空间。
- 明确本域不能被宣传成现实永生、工程可行性或个体行动方案。

### 变量接口

- 输入变量：本域直接处理的对象、资源、技术、环境、制度或状态。
- 中间机制：变量通过什么因果路径改变主体状态、系统状态或外部条件。
- 状态改变：身体、认知、能力、资源、风险暴露、可及性、时间成本或协作条件如何变化。
- 风险 / 成本函数：死亡风险、失能风险、工程风险、尾部风险、机会成本、维护成本或治理成本如何变化。
- 输出指标：有效寿命、健康寿命、有效时间、主观时间、相对时间、行动能力、恢复能力或未来选择权。

### 证据入口

- 官方 / 原始资料：监管文件、数据库、临床登记、标准、论文原文、项目白皮书或一手报告。
- 综述 / 指南 / 标准：系统综述、领域指南、技术标准、伦理规范和权威机构材料。
- 数据集 / 登记系统：可复核的数据表、代码、实验记录、登记号、版本和采集边界。
- 反例 / 失败案例：负结果、副作用、安全事故、不可复现结果、伦理争议和误用案例。

### 最小产出

- Source Signals：记录候选资料、来源、日期、主张和待核验点。
- Source Cards：提取 claim、变量、机制、证据类型、边界、反证条件和可迁移位置。
- Claim-Evidence Matrix：把每个稳定主张绑定到来源、证据等级、适用范围和不确定性。
- 变量表：列出输入变量、中间变量、状态变量、风险变量、输出指标和可观测代理指标。
- 上下游关系：说明本域依赖哪些更根本域，并向哪些转化、应用或基础设施域输出。
<!-- domain-research-skeleton:end -->

Longevity Evidence 承接原 Biocat，是 Human Infra 中负责健康寿命、长寿干预、公开证据、临床试验和安全风险的子域。

一句话定位：

> 用可追溯证据判断每一种长寿方法有没有证据、效果多大、风险在哪里。

## 项目边界

本子域做证据整理、数据结构化和信息服务，不做医疗诊断、个性化用药建议或治疗方案推荐。

首批对象聚焦：

- 干预方法：药物、补剂、运动、饮食、睡眠、检测与疗法。
- 证据材料：论文、综述、人体研究、动物实验、临床试验和公开数据库。
- 评估维度：证据等级、效果大小、适用对象、风险、不确定性和更新频率。

## 与 Human Infra 的关系

Longevity Evidence 属于 Human Infra 的 L0/L1 生存、安全与生理基础设施部分。它回答“哪些健康寿命干预有证据”，但不负责全部人类运行问题。

远期“去具身中枢生命系统”和“记忆编辑”不放在本子域内，因为它们不是普通健康干预证据页，而是独立高风险研究域。

## 目录

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
│   │   ├── life_path_nhanes_public_lmf_weighted_domain_output_readiness.json
│   │   ├── life_path_public_mortality_anchor.json
│   │   ├── life_path_nhats_acquisition_readiness.json
│   │   ├── life_path_nhats_official_source_refresh_register.json
│   │   ├── life_path_nhats_registration_evidence_template.json
│   │   ├── life_path_nhats_registration_evidence_packet_validator_test_cases.json
│   │   ├── life_path_nhats_controlled_storage_destruction_plan.json
│   │   ├── life_path_nhats_synthetic_storage_destruction_drill.json
│   │   ├── life_path_nhats_colectica_access_route_probe_register.json
│   │   ├── life_path_nhats_colectica_authenticated_capture_template.json
│   │   ├── life_path_nhats_colectica_capture_task_register.json
│   │   ├── life_path_nhats_colectica_value_label_review_execution_register.json
│   │   ├── life_path_nhats_colectica_value_label_review_protocol.json
│   │   ├── life_path_nhats_route_classifier_readiness.json
│   │   ├── life_path_nhats_cohort_flow_endpoint_protocol.json
│   │   ├── life_path_nhats_disclosure_control_policy.json
│   │   ├── life_path_nhats_disclosure_control_test_cases.json
│   │   ├── life_path_nhats_file_tier_table.json
│   │   ├── life_path_nhats_first_estimand_protocol.json
│   │   ├── life_path_nhats_l2_variable_family_admission_register.json
│   │   ├── life_path_nhats_preoutcome_aggregation_protocol.json
│   │   ├── life_path_nhats_l4_readiness_runway.json
│   │   ├── life_path_nhats_missingness_route_protocol.json
│   │   ├── life_path_nhats_missingness_route_test_cases.json
│   │   ├── life_path_nhats_route_field_discovery_register.json
│   │   ├── life_path_nhats_survey_design_protocol.json
│   │   ├── life_path_nhats_survey_design_test_cases.json
│   │   ├── life_path_nhats_variable_confirmation_matrix.json
│   │   └── life_path_toy_model_scenarios.json
│   └── processed/
├── docs/
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
    ├── run_life_path_sensitivity_analysis.py
    ├── run_life_path_toy_model.py
    ├── validate_public_mortality_anchor.py
    ├── validate_nhats_acquisition_readiness.py
    ├── validate_nhats_official_source_refresh.py
    ├── validate_nhats_controlled_storage_destruction_plan.py
    ├── validate_nhats_synthetic_storage_destruction_drill.py
    ├── validate_nhats_colectica_value_label_review_execution.py
    ├── validate_nhats_colectica_value_label_protocol.py
    ├── validate_nhats_colectica_capture_task_register.py
    ├── validate_nhats_disclosure_outputs.py
    ├── build_nhats_route_classifier_synthetic_dry_run.py
    ├── validate_nhats_route_classifier_readiness.py
    ├── validate_nhats_missingness_route_map.py
    ├── validate_nhats_route_field_discovery.py
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
    ├── validate_nhanes_public_lmf_weighted_domain_output_readiness.py
    ├── run_nhanes_public_lmf_r_survey_controlled_runtime_smoke.sh
    └── validate_nhats_survey_design_plan.py
```

## MVP

第一版目标仍是可信的长寿证据账本：

1. 整理 20 个高关注长寿干预。
2. 为每个干预建立证据页。
3. 标注人体证据、动物证据、临床试验、安全风险和证据缺口。
4. 输出可复用的数据结构，后续接入展示页、订阅产品或研究报告。

## 主流路线索引

`docs/lev-mainstream-routes.md` 记录当前全球围绕长寿逃逸速度的主流路线：组合疗法、健康寿命竞赛、Geroscience 临床转化、细胞重编程、AI 生物设计、衰老标志靶向、生物年龄与功能指标、动物临床捷径、资金与基础设施。

该文档的职责是把路线映射回现有研究域，而不是新增重复域或证明任何路线已经实现长寿逃逸速度。

`docs/lev-enabling-resources.md` 记录间接提升长寿逃逸速度概率的资源层：时间、注意力、认知、能力、记忆、AI、资金、社会支持和环境，并区分一阶、二阶和多阶效应。

`docs/lev-higher-order-effects-discovery.md` 记录二阶和多阶效应调研发现，把系统思维、fundamental cause theory、intervention-generated inequalities、diffusion of innovations、社会关系死亡风险、认知储备、睡眠恢复和数字鸿沟等理论迁移到 LEV 概率门。

`docs/lev-route-card-template.md` 规定任何新 LEV 路线进入模型前必须填写的路线卡字段、概率门、正负链路和禁止外推边界。

`docs/lev-source-cards.md` 保存第一批 Source Cards，限定二阶 / 多阶效应理论来源能支持什么、不能支持什么。

`data/manual/life_path_toy_model_scenarios.json`、`data/manual/life_path_public_mortality_anchor.json`、`data/manual/life_path_calibration_readiness.json`、`data/manual/life_path_data_source_candidates.json`、`data/manual/life_path_nhats_acquisition_readiness.json`、`data/manual/life_path_nhats_controlled_storage_destruction_plan.json`、`data/manual/life_path_nhats_synthetic_storage_destruction_drill.json`、`data/manual/life_path_nhats_colectica_value_label_review_protocol.json`、`data/manual/life_path_nhats_colectica_value_label_review_execution_register.json`、`data/manual/life_path_nhats_colectica_access_route_probe_register.json`、`data/manual/life_path_nhats_colectica_authenticated_capture_template.json`、`data/manual/life_path_nhats_route_value_crosswalk_assembly_protocol.json`、`data/manual/life_path_nhats_route_value_crosswalk_entry_validator_test_cases.json`、`data/manual/life_path_nhats_route_classifier_readiness.json`、`data/manual/life_path_nhats_file_tier_table.json`、`data/manual/life_path_nhats_first_estimand_protocol.json`、`data/manual/life_path_nhats_l2_variable_family_admission_register.json`、`data/manual/life_path_nhats_preoutcome_aggregation_protocol.json`、`data/manual/life_path_nhats_variable_confirmation_matrix.json`、`data/manual/life_path_nhats_cohort_flow_endpoint_protocol.json`、`data/manual/life_path_nhats_disclosure_control_policy.json`、`data/manual/life_path_nhats_disclosure_control_test_cases.json`、`data/manual/life_path_nhats_survey_design_protocol.json`、`data/manual/life_path_nhats_survey_design_test_cases.json`、`data/manual/life_path_nhats_missingness_route_protocol.json`、`data/manual/life_path_nhats_missingness_route_test_cases.json`、`data/manual/life_path_nhats_route_field_discovery_register.json`、`docs/life-path-data-source-cards.md`、`docs/life-path-data-card-template.md`、`docs/life-path-data-card-nhats.md`、`docs/life-path-variable-dictionary-nhats.md`、`docs/life-path-extraction-manifest-nhats-draft.md`、`scripts/build_public_mortality_anchor.py`、`scripts/validate_public_mortality_anchor.py`、`scripts/validate_nhats_file_tier_table.py`、`scripts/validate_nhats_acquisition_readiness.py`、`scripts/validate_nhats_controlled_storage_destruction_plan.py`、`scripts/validate_nhats_synthetic_storage_destruction_drill.py`、`scripts/run_life_path_toy_model.py`、`scripts/run_life_path_sensitivity_analysis.py`、`scripts/validate_nhats_disclosure_outputs.py`、`scripts/validate_nhats_survey_design_plan.py`、`scripts/validate_nhats_missingness_route_map.py`、`scripts/validate_nhats_route_field_discovery.py`、`scripts/validate_nhats_colectica_value_label_protocol.py`、`scripts/validate_nhats_colectica_value_label_review_execution.py`、`scripts/validate_nhats_colectica_access_route_probe.py`、`scripts/validate_nhats_colectica_authenticated_capture_template.py`、`scripts/validate_nhats_route_value_crosswalk_assembly.py`、`scripts/validate_nhats_route_value_crosswalk_entry_validator.py`、`scripts/validate_nhats_route_classifier_readiness.py`、`scripts/validate_nhats_l2_variable_family_admission.py`、`scripts/validate_nhats_preoutcome_aggregation_protocol.py` 和 `scripts/audit_life_path_toy_model.py` 是最小定量管线：输入保存合成场景，公开聚合死亡率锚点从 NCHS 2021 U.S. Life Tables 的男性/女性生命表抽取 age 40-100 的 `qx/lx/dx/Lx/Tx/ex`，只用于 baseline hazard plausibility comparison，不用于个体预测、干预效果估计或校准模型；校准预备契约记录 target population、time zero、outcome、estimand、validation、calibration、sensitivity 和 prohibited use 等下一阶段字段，候选数据源注册表记录 HRS、NCHS linked mortality、UK Biobank、All of Us、NHATS、ELSA、SHARE 和 Framingham 等可能用于后续校准或外部验证的官方入口与治理边界，Source Cards 把每个候选源的支持范围和禁止外推边界落成可审查文本，Data Card 模板规定真实数据进入模型前必须补齐的治理、设计、变量、质量、验证和禁止输出字段，NHATS Data Card、变量字典草案、extraction manifest 草案、机器可读 acquisition readiness、acquisition-readiness validator、受控存储/销毁计划、受控存储/销毁 validator、合成存储/销毁演练 validator、R13/R14 file-tier table、file-tier validator、第一版 estimand protocol、L2 变量族准入前映射、pre-outcome aggregation protocol、variable confirmation matrix、cohort-flow endpoint-routing protocol、disclosure-control validator、survey-design validator、missingness-route validator、route-field discovery validator、Colectica value-label review validator、Colectica 第一轮执行登记 validator、Colectica access-route probe validator、Colectica authenticated capture template validator、route-value crosswalk assembly validator、route-value crosswalk entry validator、route-classifier readiness validator、L2 variable-family admission validator 和 pre-outcome aggregation validator 提供第一份晚年功能/有效时间模型准入、受控存储、合成销毁演练、文件层级候选表审计、公开导出、加权估计、字段发现、值标签复核、字段级来源追踪、公开入口/登录边界、受控登录后变量页捕获槽位、真实分类器前置阻塞门、route-value 装配门、future crosswalk-entry 预检门、L2 变量族预映射、预结果聚合规则和终点/缺失路由门禁样板，并明确未补齐文件名、变量名、权重、分层、PSU/variance unit、方差方法、缺失码、访问层级、endpoint、cohort flow、pre-outcome aggregation evidence、真实受控工作区执行记录、访问日志、清单日志、Colectica 登录、Colectica authenticated capture hashes、Colectica value labels、question text、skip logic、route fields、route-value crosswalk、variable-specific missing-code map、second-reviewer signoff、survey design、披露控制和输出规则前不能写抽取脚本、下载数据、报告加权人群估计、做 endpoint route classification、做真实聚合或做模型校准，导出器生成 `web/src/data/life-path-toy-model.json`，敏感性导出器生成 `web/src/data/life-path-sensitivity-analysis.json`，file-tier 验证器生成 `web/src/data/life-path-nhats-file-tier-table-validation.json`，acquisition-readiness 验证器生成 `web/src/data/life-path-nhats-acquisition-readiness-validation.json`，受控存储/销毁验证器生成 `web/src/data/life-path-nhats-controlled-storage-destruction-validation.json`，合成销毁演练验证器生成 `web/src/data/life-path-nhats-synthetic-storage-destruction-drill-validation.json`，披露验证器生成 `web/src/data/life-path-nhats-disclosure-control-validation.json`，survey-design 验证器生成 `web/src/data/life-path-nhats-survey-design-validation.json`，missingness-route 验证器生成 `web/src/data/life-path-nhats-missingness-route-validation.json`，route-field discovery 验证器生成 `web/src/data/life-path-nhats-route-field-discovery-validation.json`，Colectica value-label 验证器生成 `web/src/data/life-path-nhats-colectica-value-label-validation.json`，Colectica 执行登记验证器生成 `web/src/data/life-path-nhats-colectica-value-label-review-execution-validation.json`，Colectica access-route probe 验证器生成 `web/src/data/life-path-nhats-colectica-access-route-probe-validation.json`，Colectica authenticated capture template 验证器生成 `web/src/data/life-path-nhats-colectica-authenticated-capture-template-validation.json`，route-value assembly 验证器生成 `web/src/data/life-path-nhats-route-value-crosswalk-assembly-validation.json`，route-value entry validator 生成 `web/src/data/life-path-nhats-route-value-crosswalk-entry-validator-validation.json`，route-classifier readiness 验证器生成 `web/src/data/life-path-nhats-route-classifier-readiness-validation.json`，L2 variable-family admission 验证器生成 `web/src/data/life-path-nhats-l2-variable-family-admission-validation.json`，pre-outcome aggregation 验证器生成 `web/src/data/life-path-nhats-preoutcome-aggregation-validation.json`，审计器生成 `web/src/data/life-path-toy-model-audit.json` / `.md`。该模型只验证生命路径建模契约、公开聚合基线锚点、校准预备边界、候选数据源边界、数据卡准入脚手架、提取前治理门禁、acquisition-readiness 门禁、受控存储/销毁计划门、合成存储/销毁演练门、file-tier 表一致性门、第一版 estimand 预注册门、合成敏感性分析、合成披露控制门、合成调查设计门、合成缺失/终点路由门、NHATS 官方字段发现门、Colectica 值标签复核协议门、Colectica 第一轮执行登记边界、Colectica 公开入口 / 登录边界、Colectica authenticated capture 模板边界、route-value assembly 阻塞门、route-value entry validator 阻塞门、route-classifier readiness 阻塞门、L2 变量族准入前映射边界和 pre-outcome aggregation 规则边界，不作为真实医学预测。

`data/manual/life_path_nhats_l4_readiness_runway.json` 与 `scripts/validate_nhats_l4_readiness_runway.py` 维护 NHATS 从 L2 设计资产进入 L4 aggregate-calibrated research model 前的 readiness runway；它只把 12 个 pass / partial / blocked gates 和上游 source hash 接入审计，导出 `web/src/data/life-path-nhats-l4-readiness-runway-validation.json`，不授权真实提取、校准预测、干预排序、个体死亡日期或个体决策支持。

`scripts/build_nhats_route_classifier_synthetic_dry_run.py` 维护 NHATS route-classifier 的合成执行门；它读取 missingness-route 合成用例、route-classifier readiness 和 route-value crosswalk handoff，生成 ignored `build/reports/nhats-route-classifier-synthetic-dry-run/route-classifier-synthetic-dry-run.json` 和 tracked `web/src/data/life-path-nhats-route-classifier-synthetic-dry-run-validation.json`，证明 route envelope 逻辑可 fail-closed 运行，但不读取真实 NHATS rows、不打开 weighted route counts、public export、校准、L4 admission 或 individual prediction；tracked validation 会被总 toy model audit 消费。

`data/manual/life_path_nhanes_public_lmf_survey_design_readiness.json` 与 `scripts/validate_nhanes_public_lmf_survey_design_readiness.py` 维护 NHANES public-use LMF 试运行的 survey-design readiness；它把 WTMEC2YR、SDMVPSU、SDMVSTRA 官方字段、Taylor linearization 文档线索和 estimator/domain/disclosure/calibration 阻塞门接入审计，导出 `web/src/data/life-path-nhanes-public-lmf-survey-design-readiness-validation.json`，不授权 survey-weighted inference、design-based confidence interval、校准预测或个体预测。

`data/manual/life_path_nhanes_public_lmf_domain_subpopulation_rule_readiness.json` 与 `scripts/validate_nhanes_public_lmf_domain_subpopulation_rule_readiness.py` 维护 NHANES public-use LMF 试运行的 domain/subpopulation rule readiness；它把 CDC/NCHS domain/subpopulation 机制、完整设计输入、禁止 row-drop subgroup filtering、eligible base、DOF、disclosure 和 calibration 阻塞门接入审计，导出 `web/src/data/life-path-nhanes-public-lmf-domain-subpopulation-rule-readiness-validation.json`，不授权 weighted domain inference、design-based confidence interval、校准预测或个体预测。

`data/manual/life_path_nhanes_public_lmf_eligible_base_readiness.json` 与 `scripts/validate_nhanes_public_lmf_eligible_base_readiness.py` 维护 NHANES public-use LMF 试运行的 positive-weight eligible-base readiness；它把 DEMO_J `WTMEC2YR > 0`、完整设计输入、禁止预先丢行、5809 名 positive-weight eligible adults、15 个 strata 和 no lonely positive-weight strata 接入审计，导出 `web/src/data/life-path-nhanes-public-lmf-eligible-base-readiness-validation.json`，不授权 weighted domain inference、design-based confidence interval、校准预测或个体预测。

`data/manual/life_path_nhanes_public_lmf_weighted_estimator_readiness.json` 与 `scripts/validate_nhanes_public_lmf_weighted_estimator_readiness.py` 维护 NHANES public-use LMF 试运行的 weighted-estimator readiness；它选择 R `survey` / `svydesign` 作为成熟复杂抽样后端，绑定 `WTMEC2YR`、`SDMVPSU`、`SDMVSTRA`、`nest=true`、design-object 和 domain indicator 合约，导出 `web/src/data/life-path-nhanes-public-lmf-weighted-estimator-readiness-validation.json`，不授权 R runtime smoke、weighted domain output、design-based confidence interval、校准预测或个体预测。

`data/manual/life_path_nhanes_public_lmf_r_survey_runtime_smoke_readiness.json`、`runtime/nhanes-public-lmf-r-survey-conda.yml`、`scripts/validate_nhanes_public_lmf_r_survey_runtime_smoke.py` 与 `scripts/run_nhanes_public_lmf_r_survey_controlled_runtime_smoke.sh` 维护 NHANES public-use LMF R `survey` runtime smoke；默认探测当前环境，controlled 脚本会在仓库根目录 `.runtime/nhanes-r-survey/` 创建可重建 conda prefix，并导出 `web/src/data/life-path-nhanes-public-lmf-r-survey-controlled-runtime-smoke-validation.json`。该门只证明 R `4.3.3`、R `survey` 和 synthetic `svydesign` / domain `subset` smoke 能跑通，不下载、不保存、不处理 NHANES 行级数据，不授权 weighted domain output、design-based confidence interval、校准预测或个体预测。

`data/manual/life_path_nhanes_public_lmf_domain_indicator_diagnostic.json` 与 `scripts/validate_nhanes_public_lmf_domain_indicator_diagnostic.py` 维护 NHANES public-use LMF domain indicator metadata diagnostic；它只验证上游聚合试运行覆盖 8 个 sex × ageBand 公开聚合域组合，并确认 diagnostic 自身不重复公开 record counts、death counts、weighted sums、rates、intervals、原始行或个体行，导出 `web/src/data/life-path-nhanes-public-lmf-domain-indicator-diagnostic-validation.json`。该门把 domain indicator metadata gate 推进到 ready，但仍不授权 weighted domain output、design-based confidence interval、校准预测或个体预测。

`data/manual/life_path_nhanes_public_lmf_dof_sparse_domain_diagnostic.json` 与 `scripts/validate_nhanes_public_lmf_dof_sparse_domain_diagnostic.py` 维护 NHANES public-use LMF DOF / sparse-domain metadata diagnostic；它只验证 8 个 sex × ageBand 公开聚合域的 represented PSU/strata DOF、lonely represented strata、empty domain 和 sparse-domain flags，并确认不持久化行、逐域计数、逐域加权和、rates 或 intervals，导出 `web/src/data/life-path-nhanes-public-lmf-dof-sparse-domain-diagnostic-validation.json`。该门把 DOF/sparse metadata gate 推进到 ready，但仍不授权 weighted domain output、design-based confidence interval、校准预测或个体预测。

`data/manual/life_path_nhanes_public_lmf_disclosure_output_envelope_policy.json`、`data/manual/life_path_nhanes_public_lmf_disclosure_output_envelope_test_cases.json` 与 `scripts/validate_nhanes_public_lmf_disclosure_output_envelope.py` 维护 NHANES public-use LMF synthetic disclosure output envelope；它只验证合成输出形状的 allow/block 规则，禁止 row-level leak、identifier key、public AI upload、真实 weighted output 类型和未抑制 small cell / low DOF 公开输出，导出 `web/src/data/life-path-nhanes-public-lmf-disclosure-output-envelope-validation.json`。该门把 disclosure output envelope 的合成审查推进到 ready，但不授权真实 public weighted-domain output。

`data/manual/life_path_nhanes_public_lmf_effective_sample_ci_publication_policy.json`、`data/manual/life_path_nhanes_public_lmf_effective_sample_ci_publication_test_cases.json` 与 `scripts/validate_nhanes_public_lmf_effective_sample_ci_publication.py` 维护 NHANES public-use LMF synthetic effective sample / confidence interval publication gate；它只验证合成发布可靠性形状的 allow/block 规则，禁止低 effective sample class、unacceptable RSE、unacceptable CI width、低 DOF、真实 CI 声明、public AI upload 和真实 output type，导出 `web/src/data/life-path-nhanes-public-lmf-effective-sample-ci-publication-validation.json`。该门把 publication criteria 的合成审查推进到 ready，但不授权真实 public weighted-domain output、真实 design-based interval 或发布许可。

`data/manual/life_path_nhanes_public_lmf_weighted_output_implementation_preflight_policy.json`、`data/manual/life_path_nhanes_public_lmf_weighted_output_implementation_preflight_test_cases.json` 与 `scripts/validate_nhanes_public_lmf_weighted_output_implementation_preflight.py` 维护 NHANES public-use LMF synthetic weighted-output implementation preflight；它只验证未来实现计划是否采用 R `survey` / `svydesign` / post-design `survey::subset` 形状，并阻断 row-drop-before-design、row persistence、真实 weighted rate / interval、public AI upload、count key 和 individual-output 形状，导出 `web/src/data/life-path-nhanes-public-lmf-weighted-output-implementation-preflight-validation.json`。该门把 implementation-shape 的合成审查推进到 ready，但不执行真实 weighted-domain output。

`data/manual/life_path_nhanes_public_lmf_disclosure_review_template.json` 与 `scripts/validate_nhanes_public_lmf_disclosure_review_template.py` 维护 NHANES public-use LMF disclosure review template；它只验证未来真实输出披露审查 packet 是否包含 15 个 pending review slots、second-reviewer、output hash、suppression review、effective sample / CI review、forbidden-field scan、retention plan 和 release decision，导出 `web/src/data/life-path-nhanes-public-lmf-disclosure-review-template-validation.json`。该门把 review-packet shape 推进到 ready，但不完成真实 disclosure review。

`data/manual/life_path_nhanes_public_lmf_disclosure_review_execution_register.json` 与 `scripts/validate_nhanes_public_lmf_disclosure_review_execution.py` 维护 NHANES public-use LMF disclosure review execution register；它把 15 个 review slots、8 个 machine-prefill-eligible slots、reviewed output hash、second-reviewer signoff、release decision 和 public output permission 状态变成机器可审计登记，导出 `web/src/data/life-path-nhanes-public-lmf-disclosure-review-execution-validation.json`。该门只证明人工审查执行状态可审计，当前 0 个 human-reviewed slots，release 仍 blocked。

`data/manual/life_path_nhanes_public_lmf_weighted_domain_output_readiness.json` 与 `scripts/validate_nhanes_public_lmf_weighted_domain_output_readiness.py` 维护 NHANES public-use LMF weighted-domain output safety gate；它把 controlled runtime smoke、post-design domain indicator、DOF / sparse-domain metadata diagnostic、synthetic disclosure output envelope、synthetic effective sample / confidence interval publication gate、synthetic weighted-output implementation preflight、disclosure review template、disclosure review execution register 和 real disclosure / output implementation review 绑定成公开输出前置门，导出 `web/src/data/life-path-nhanes-public-lmf-weighted-domain-output-readiness-validation.json`。该门现在只证明 domain indicator、DOF/sparse metadata、synthetic disclosure envelope、synthetic publication criteria、synthetic implementation preflight、disclosure review template 和 disclosure review execution register gates 已 ready，共 12 个 ready gates、2 个 blocked gates；它显式声明 ignored local run / packet 不是默认检查依赖，干净 checkout 即使没有 `build/reports/` 也必须能通过默认 readiness 审计。真实 disclosure review 与真实 output implementation 仍 blocked，不生成 weighted mortality rate、design-based interval、校准预测或个体预测。

`scripts/run_nhanes_public_lmf_weighted_domain_output_local.py`、`scripts/validate_nhanes_public_lmf_weighted_domain_output_local_run.py` 与 `make nhanes-public-lmf-weighted-domain-output-local-run-audit` 维护本地受控真实 weighted-domain 运行切片；它会下载 public-use NHANES LMF/DEMO 到临时目录，用 R `survey` 执行 `svydesign` 和 post-design `survey::subset`，只把 8 个 sex × ageBand 的本地审计报告写入已忽略的 `build/reports/nhanes-public-lmf-weighted-domain-output-local/validation.json`。该输出不进入 `web/src/data`，不进入版本库，不完成 disclosure review，不授权公开 weighted rates、design-based intervals、校准预测或个体预测；该 ignored report 可以在干净 checkout 中不存在，默认 `make check` 和 readiness audit 不读取它。

`scripts/build_nhanes_public_lmf_local_disclosure_review_packet.py`、`scripts/validate_nhanes_public_lmf_local_disclosure_review_packet.py` 与 `make nhanes-public-lmf-local-disclosure-review-packet-audit` 维护本地 disclosure review packet 跑道；它先生成本地真实 weighted-domain 报告，再把报告 hash、来源绑定、R `survey` runtime、8 个域、minimum DOF 和 15 个 review slots 写入已忽略的 `build/reports/nhanes-public-lmf-local-disclosure-review-packet/validation.json`，并把 redacted packet 审计结果写入同一 ignored 目录下的 `packet-validation.json`。该 packet 和 packet validation 都不复制真实 weighted rates、standard errors 或 design-based intervals，不进入 `web/src/data`，不完成人工 disclosure review，不授权公开输出、校准预测或个体预测；这些 ignored packet 产物可以在干净 checkout 中不存在，默认 `make check` 和 readiness audit 不读取它们。

`data/manual/life_path_nhanes_public_lmf_r_survey_runtime_smoke_readiness.json` 与 `scripts/validate_nhanes_public_lmf_r_survey_runtime_smoke.py` 维护 NHANES public-use LMF 试运行的 R `survey` runtime smoke readiness；它只探测当前环境是否具备 `Rscript`、`survey` 包和 synthetic `svydesign` / domain `subset` smoke 能力，当前可记录 `blocked-no-rscript` 这类运行时阻塞，不下载、不保存、不处理 NHANES 行级数据，也不授权 weighted domain output、design-based confidence interval、校准预测或个体预测。

`data/manual/life_path_nhanes_public_lmf_aggregate_pilot.json`、`web/src/data/life-path-nhanes-public-lmf-aggregate-pilot-validation.json`、`scripts/build_nhanes_public_lmf_aggregate_pilot.py` 与 `scripts/validate_nhanes_public_lmf_aggregate_pilot.py` 维护第一条公开真实死亡结局聚合试运行路径：从 CDC/NCHS public-use NHANES 2017-2018 LMF 和 DEMO XPT 下载到临时目录、按 SEQN 内存连接、按 sex × age band 导出 8 个粗聚合单元，并由验证器确认 source hash、聚合计数、禁止行级字段和禁止用途边界。该切片只证明公开数据管线 smoke test，不证明 survey-weighted population inference、校准预测、因果效应、医学建议或个体死亡日期输出。

`data/manual/life_path_nhats_colectica_capture_task_register.json` 与 `scripts/validate_nhats_colectica_capture_task_register.py` 维护 NHATS Colectica 变量页捕获任务清单；它把 authenticated capture template 展开为 9 个 route-field 组和 39 个 pending 变量 / 输出任务，导出 `web/src/data/life-path-nhats-colectica-capture-task-register-validation.json`，只证明任务清单已准备，不表示 Colectica 登录、变量页捕获、值标签确认、route classifier、真实提取、校准或个体预测已允许。

`data/manual/life_path_nhats_official_source_refresh_register.json` 与 `scripts/validate_nhats_official_source_refresh.py` 维护 NHATS 官方公开来源刷新证据；它记录 Data Access、Cross-Year Search、Conditions of Use、R13/R14 文件页和 Colectica 技术指南的 HTTP 状态、内容长度、SHA-256、2026-07-04 live reprobe、HTML 标题和 PDF HEAD 元数据，导出 `web/src/data/life-path-nhats-official-source-refresh-validation.json`，并把 acquisition readiness 中的 official-source-refresh 门升为 ready。该门不授权数据下载、抽取、校准、公开导出或个体预测。

## 运行示例

从仓库根目录运行：

```bash
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/collect_mvp_data.py --limit 10
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/collect_core_data.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/build_public_mortality_anchor.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_public_mortality_anchor.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/build_nhanes_public_lmf_aggregate_pilot.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhanes_public_lmf_aggregate_pilot.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhanes_public_lmf_survey_design_readiness.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhanes_public_lmf_domain_subpopulation_rule_readiness.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhanes_public_lmf_eligible_base_readiness.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhanes_public_lmf_weighted_estimator_readiness.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhanes_public_lmf_r_survey_runtime_smoke.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhanes_public_lmf_domain_indicator_diagnostic.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhanes_public_lmf_dof_sparse_domain_diagnostic.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhanes_public_lmf_disclosure_output_envelope.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhanes_public_lmf_effective_sample_ci_publication.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhanes_public_lmf_weighted_output_implementation_preflight.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhanes_public_lmf_disclosure_review_template.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhanes_public_lmf_weighted_domain_output_readiness.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_official_source_refresh.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_acquisition_readiness.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_controlled_storage_destruction_plan.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/run_life_path_toy_model.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/run_life_path_sensitivity_analysis.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_survey_design_plan.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_route_field_discovery.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_colectica_value_label_protocol.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_colectica_value_label_review_execution.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_colectica_access_route_probe.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_colectica_authenticated_capture_template.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_colectica_capture_task_register.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_route_classifier_readiness.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_l2_variable_family_admission.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_preoutcome_aggregation_protocol.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_l4_readiness_runway.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/audit_life_path_toy_model.py
```
