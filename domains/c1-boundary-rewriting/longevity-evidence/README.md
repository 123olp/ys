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
│   │   ├── life_path_public_mortality_anchor.json
│   │   ├── life_path_nhats_acquisition_readiness.json
│   │   ├── life_path_nhats_controlled_storage_destruction_plan.json
│   │   ├── life_path_nhats_synthetic_storage_destruction_drill.json
│   │   ├── life_path_nhats_colectica_access_route_probe_register.json
│   │   ├── life_path_nhats_colectica_authenticated_capture_template.json
│   │   ├── life_path_nhats_colectica_value_label_review_execution_register.json
│   │   ├── life_path_nhats_colectica_value_label_review_protocol.json
│   │   ├── life_path_nhats_cohort_flow_endpoint_protocol.json
│   │   ├── life_path_nhats_disclosure_control_policy.json
│   │   ├── life_path_nhats_disclosure_control_test_cases.json
│   │   ├── life_path_nhats_file_tier_table.json
│   │   ├── life_path_nhats_first_estimand_protocol.json
│   │   ├── life_path_nhats_l2_variable_family_admission_register.json
│   │   ├── life_path_nhats_preoutcome_aggregation_protocol.json
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
    ├── validate_nhats_controlled_storage_destruction_plan.py
    ├── validate_nhats_synthetic_storage_destruction_drill.py
    ├── validate_nhats_colectica_value_label_review_execution.py
    ├── validate_nhats_colectica_value_label_protocol.py
    ├── validate_nhats_disclosure_outputs.py
    ├── validate_nhats_missingness_route_map.py
    ├── validate_nhats_route_field_discovery.py
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

`data/manual/life_path_toy_model_scenarios.json`、`data/manual/life_path_public_mortality_anchor.json`、`data/manual/life_path_calibration_readiness.json`、`data/manual/life_path_data_source_candidates.json`、`data/manual/life_path_nhats_acquisition_readiness.json`、`data/manual/life_path_nhats_controlled_storage_destruction_plan.json`、`data/manual/life_path_nhats_synthetic_storage_destruction_drill.json`、`data/manual/life_path_nhats_colectica_value_label_review_protocol.json`、`data/manual/life_path_nhats_colectica_value_label_review_execution_register.json`、`data/manual/life_path_nhats_colectica_access_route_probe_register.json`、`data/manual/life_path_nhats_colectica_authenticated_capture_template.json`、`data/manual/life_path_nhats_file_tier_table.json`、`data/manual/life_path_nhats_first_estimand_protocol.json`、`data/manual/life_path_nhats_l2_variable_family_admission_register.json`、`data/manual/life_path_nhats_preoutcome_aggregation_protocol.json`、`data/manual/life_path_nhats_variable_confirmation_matrix.json`、`data/manual/life_path_nhats_cohort_flow_endpoint_protocol.json`、`data/manual/life_path_nhats_disclosure_control_policy.json`、`data/manual/life_path_nhats_disclosure_control_test_cases.json`、`data/manual/life_path_nhats_survey_design_protocol.json`、`data/manual/life_path_nhats_survey_design_test_cases.json`、`data/manual/life_path_nhats_missingness_route_protocol.json`、`data/manual/life_path_nhats_missingness_route_test_cases.json`、`data/manual/life_path_nhats_route_field_discovery_register.json`、`docs/life-path-data-source-cards.md`、`docs/life-path-data-card-template.md`、`docs/life-path-data-card-nhats.md`、`docs/life-path-variable-dictionary-nhats.md`、`docs/life-path-extraction-manifest-nhats-draft.md`、`scripts/build_public_mortality_anchor.py`、`scripts/validate_public_mortality_anchor.py`、`scripts/validate_nhats_acquisition_readiness.py`、`scripts/validate_nhats_controlled_storage_destruction_plan.py`、`scripts/validate_nhats_synthetic_storage_destruction_drill.py`、`scripts/run_life_path_toy_model.py`、`scripts/run_life_path_sensitivity_analysis.py`、`scripts/validate_nhats_disclosure_outputs.py`、`scripts/validate_nhats_survey_design_plan.py`、`scripts/validate_nhats_missingness_route_map.py`、`scripts/validate_nhats_route_field_discovery.py`、`scripts/validate_nhats_colectica_value_label_protocol.py`、`scripts/validate_nhats_colectica_value_label_review_execution.py`、`scripts/validate_nhats_colectica_access_route_probe.py`、`scripts/validate_nhats_colectica_authenticated_capture_template.py`、`scripts/validate_nhats_l2_variable_family_admission.py`、`scripts/validate_nhats_preoutcome_aggregation_protocol.py` 和 `scripts/audit_life_path_toy_model.py` 是最小定量管线：输入保存合成场景，公开聚合死亡率锚点从 NCHS 2021 U.S. Life Tables 的男性/女性生命表抽取 age 40-100 的 `qx/lx/dx/Lx/Tx/ex`，只用于 baseline hazard plausibility comparison，不用于个体预测、干预效果估计或校准模型；校准预备契约记录 target population、time zero、outcome、estimand、validation、calibration、sensitivity 和 prohibited use 等下一阶段字段，候选数据源注册表记录 HRS、NCHS linked mortality、UK Biobank、All of Us、NHATS、ELSA、SHARE 和 Framingham 等可能用于后续校准或外部验证的官方入口与治理边界，Source Cards 把每个候选源的支持范围和禁止外推边界落成可审查文本，Data Card 模板规定真实数据进入模型前必须补齐的治理、设计、变量、质量、验证和禁止输出字段，NHATS Data Card、变量字典草案、extraction manifest 草案、机器可读 acquisition readiness、acquisition-readiness validator、受控存储/销毁计划、受控存储/销毁 validator、合成存储/销毁演练 validator、R13/R14 file-tier table、第一版 estimand protocol、L2 变量族准入前映射、pre-outcome aggregation protocol、variable confirmation matrix、cohort-flow endpoint-routing protocol、disclosure-control validator、survey-design validator、missingness-route validator、route-field discovery validator、Colectica value-label review validator、Colectica 第一轮执行登记 validator、Colectica access-route probe validator、Colectica authenticated capture template validator、L2 variable-family admission validator 和 pre-outcome aggregation validator 提供第一份晚年功能/有效时间模型准入、受控存储、合成销毁演练、公开导出、加权估计、字段发现、值标签复核、字段级来源追踪、公开入口/登录边界、受控登录后变量页捕获槽位、L2 变量族预映射、预结果聚合规则和终点/缺失路由门禁样板，并明确未补齐文件名、变量名、权重、分层、PSU/variance unit、方差方法、缺失码、访问层级、endpoint、cohort flow、pre-outcome aggregation evidence、真实受控工作区执行记录、访问日志、清单日志、Colectica 登录、Colectica authenticated capture hashes、Colectica value labels、question text、skip logic、route fields、survey design、披露控制和输出规则前不能写抽取脚本、下载数据、报告加权人群估计、做 endpoint route classification、做真实聚合或做模型校准，导出器生成 `web/src/data/life-path-toy-model.json`，敏感性导出器生成 `web/src/data/life-path-sensitivity-analysis.json`，acquisition-readiness 验证器生成 `web/src/data/life-path-nhats-acquisition-readiness-validation.json`，受控存储/销毁验证器生成 `web/src/data/life-path-nhats-controlled-storage-destruction-validation.json`，合成销毁演练验证器生成 `web/src/data/life-path-nhats-synthetic-storage-destruction-drill-validation.json`，披露验证器生成 `web/src/data/life-path-nhats-disclosure-control-validation.json`，survey-design 验证器生成 `web/src/data/life-path-nhats-survey-design-validation.json`，missingness-route 验证器生成 `web/src/data/life-path-nhats-missingness-route-validation.json`，route-field discovery 验证器生成 `web/src/data/life-path-nhats-route-field-discovery-validation.json`，Colectica value-label 验证器生成 `web/src/data/life-path-nhats-colectica-value-label-validation.json`，Colectica 执行登记验证器生成 `web/src/data/life-path-nhats-colectica-value-label-review-execution-validation.json`，Colectica access-route probe 验证器生成 `web/src/data/life-path-nhats-colectica-access-route-probe-validation.json`，Colectica authenticated capture template 验证器生成 `web/src/data/life-path-nhats-colectica-authenticated-capture-template-validation.json`，L2 variable-family admission 验证器生成 `web/src/data/life-path-nhats-l2-variable-family-admission-validation.json`，pre-outcome aggregation 验证器生成 `web/src/data/life-path-nhats-preoutcome-aggregation-validation.json`，审计器生成 `web/src/data/life-path-toy-model-audit.json` / `.md`。该模型只验证生命路径建模契约、公开聚合基线锚点、校准预备边界、候选数据源边界、数据卡准入脚手架、提取前治理门禁、acquisition-readiness 门禁、受控存储/销毁计划门、合成存储/销毁演练门、第一版 estimand 预注册门、合成敏感性分析、合成披露控制门、合成调查设计门、合成缺失/终点路由门、NHATS 官方字段发现门、Colectica 值标签复核协议门、Colectica 第一轮执行登记边界、Colectica 公开入口 / 登录边界、Colectica authenticated capture 模板边界、L2 变量族准入前映射边界和 pre-outcome aggregation 规则边界，不作为真实医学预测。

## 运行示例

从仓库根目录运行：

```bash
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/collect_mvp_data.py --limit 10
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/collect_core_data.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/build_public_mortality_anchor.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_public_mortality_anchor.py
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
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_l2_variable_family_admission.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_preoutcome_aggregation_protocol.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/audit_life_path_toy_model.py
```
