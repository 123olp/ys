# 数据目录

这里存放 Longevity Evidence 子域的公开数据源样例、原始快照和清洗后数据。

## 规则

- `raw/` 用于原始 API 响应或下载文件。
- `processed/` 用于清洗后的结构化数据。
- `manual/` 用于人工整理的首批 MVP 数据。
- `manual/higher_order_effects.tsv` 用于维护 LEV 二阶 / 多阶效应模型输入。
- `manual/lev_route_cards.tsv` 用于维护 LEV 主流路线卡模型输入。
- `manual/life_path_toy_model_scenarios.json` 用于维护生命路径 toy model 的合成队列场景输入。
- `manual/life_path_public_mortality_anchor.json` 用于维护 NCHS 2021 U.S. Life Tables 的公开聚合死亡率锚点，支持 toy baseline plausibility comparison；该文件不包含个人数据，不授权校准预测、干预效果估计或个体死亡日期输出。
- `manual/life_path_calibration_readiness.json` 用于维护生命路径模型从 toy model 进入校准模型前必须满足的研究设计、报告、验证和禁止用途字段。
- `manual/life_path_data_source_candidates.json` 用于维护生命路径模型后续可能使用的官方队列、死亡链接、老龄化面板和外部验证候选源；该文件只登记候选和治理边界，不表示已经下载、访问或校准。
- `manual/life_path_nhats_acquisition_readiness.json` 用于维护 NHATS 从候选数据源进入真实提取前的机器可读准入门；该文件只记录官方来源刷新、注册、文件层级、Colectica 变量确认、survey design、endpoint、披露控制、AI 边界和存储销毁要求，不表示已经 acquisition-ready。
- `manual/life_path_nhats_controlled_storage_destruction_plan.json` 用于维护 NHATS 受控存储和销毁计划；该文件只定义非仓库受控工作区、访问日志、清单槽位、销毁触发和禁止位置，不表示已经 provisioned workspace、下载数据、执行抽取或完成销毁演练。
- `manual/life_path_nhats_file_tier_table.json` 用于维护 NHATS R13/R14 官方文件层级、访问层级、候选用途、阻塞门和禁止动作；该文件只证明文件层级已登记，不授权下载、抽取、校准或公共 AI 上传。
- `manual/life_path_nhats_first_estimand_protocol.json` 用于维护 NHATS R13/R14 第一版 aggregate functional-survival estimand 预注册协议；该文件只固定 target population、time zero、outcome、predictor family、censoring、survey design 和输出边界，不授权下载、抽取、校准、验证或个体预测。
- `manual/life_path_nhats_variable_confirmation_matrix.json` 用于维护 NHATS R13/R14 第一版 estimand 的变量确认矩阵、候选字段模式、cohort-flow 模板和阻塞门；该文件只记录字段搜索空间和缺口，不授权用候选字段写抽取脚本。
- `manual/life_path_nhats_cohort_flow_endpoint_protocol.json` 用于维护 NHATS R13/R14 队列流转、终点路由、输出契约、披露控制和 readiness gates；该文件只预注册路线与禁止动作，不授权下载、抽取、公开导出、校准或个体预测。
- `manual/life_path_nhats_disclosure_control_policy.json` 用于维护 NHATS 输出公开导出前的披露控制策略，固定 aggregate-only、n < 5 suppression、row-level export block、public AI upload block、允许输出类型和禁止输出类型。
- `manual/life_path_nhats_disclosure_control_test_cases.json` 用于维护 NHATS 披露控制 validator 的合成测试用例；该文件只包含 synthetic output envelopes，不包含真实 NHATS 数据或真实 route counts。
- `manual/life_path_nhats_survey_design_protocol.json` 用于维护 NHATS survey-design gate，固定权重、分层、PSU/variance unit、方差方法、domain rule、missingness route、round linkage、披露验证和 weighted-estimator review 这些加权估计前置条件。
- `manual/life_path_nhats_survey_design_test_cases.json` 用于维护 NHATS survey-design validator 的合成测试用例；该文件只包含 synthetic design-plan envelopes，不包含真实 NHATS 权重、route counts、cohort counts 或参与者数据。
- `manual/life_path_nhats_missingness_route_protocol.json` 用于维护 NHATS missingness / endpoint-route gate，固定死亡边界、self/proxy/facility 路由、known-alive noninterview、缺失/失访、not-classifiable、小单元抑制和 dominance rules。
- `manual/life_path_nhats_missingness_route_test_cases.json` 用于维护 NHATS missingness-route validator 的合成测试用例；该文件只包含 synthetic route envelopes，不包含真实 NHATS route counts、cohort counts、死亡记录或参与者数据。
- `manual/life_path_nhats_route_field_discovery_register.json` 用于维护 NHATS R13/R14 官方 crosswalk 和 User Guide 中已经发现的 route-field 候选；该文件只记录字段发现、来源边界和阻塞门，不表示 Colectica value labels 已确认、真实文件已访问、route classifier 已允许或 endpoint classification 已可执行。
- `manual/life_path_nhats_colectica_value_label_review_protocol.json` 用于维护 NHATS Colectica value-label 复核协议；该文件只定义登录记录、字段级 source trace、route-value crosswalk、missing-code map、二次复核和分类器晋升门，不表示任何 value labels、question text、skip logic 或 route classifier 已确认。
- `manual/life_path_nhats_colectica_value_label_review_execution_register.json` 用于维护 NHATS Colectica value-label 复核的第一轮执行登记；该文件只记录官方来源追踪、字段级 source-trace 骨架和标准 negative missing-code family，仍不表示 Colectica 登录完成、value labels 确认、question text 确认、route-value crosswalk 可用或 classifier 可晋升。
- `manual/life_path_nhats_colectica_access_route_probe_register.json` 用于维护 NHATS Colectica 公开入口、匿名登录边界和技术指南捕获路线的 probe 登记；该文件只证明官方访问路径和下一步 capture workflow，不表示账号、登录、变量页、value labels、question text、导出、校准或个体预测已完成。
- `manual/life_path_nhats_colectica_authenticated_capture_template.json` 用于维护 NHATS Colectica 受控登录后变量页捕获模板；该文件只定义每个 route field 必须补齐的 item id、变量名、轮次、文件名、Details URL、source hash、value labels、question text、universe/skip logic 和二次复核证据槽，不表示登录、捕获、标签确认、route classifier、导出、校准或个体预测已完成。
- `manual/life_path_nhats_l2_variable_family_admission_register.json` 用于维护 NHATS 第一版窄 estimand 的 L2 变量族准入前映射；该文件只把 6 个候选变量族绑定到模型位置和晋升阻塞门，不表示精确字段、Colectica value labels、真实提取、校准或个体预测已完成。
- `manual/life_path_nhats_preoutcome_aggregation_protocol.json` 用于维护 NHATS 预结果聚合规则；该文件只冻结 L2-only 聚合边界、合成测试用例和真实聚合前置证据，不表示真实 NHATS 数据、route classification、加权估计、公开导出、L4 准入、校准或个体预测已完成。
- `web/src/data/life-path-sensitivity-analysis.json` 是从 `manual/life_path_toy_model_scenarios.json` 派生的合成 sensitivity 输出；它不放在本目录内，但由本域脚本生成并由本域审计器检查。
- `web/src/data/life-path-nhats-controlled-storage-destruction-validation.json` 是从受控存储/销毁计划派生的验证报告；它不放在本目录内，但由本域脚本生成并由本域审计器检查，只证明 storage-destruction gate 为 partial 且仍阻塞下载、抽取、raw data 入库、public AI 上传、校准和个体预测。
- `web/src/data/life-path-nhats-disclosure-control-validation.json` 是从披露控制 policy 和 synthetic test cases 派生的验证报告；它不放在本目录内，但由本域脚本生成并由本域审计器检查。
- `web/src/data/life-path-nhats-survey-design-validation.json` 是从 survey-design protocol 和 synthetic test cases 派生的验证报告；它不放在本目录内，但由本域脚本生成并由本域审计器检查。
- `web/src/data/life-path-nhats-missingness-route-validation.json` 是从 missingness-route protocol 和 synthetic test cases 派生的验证报告；它不放在本目录内，但由本域脚本生成并由本域审计器检查。
- `web/src/data/life-path-nhats-route-field-discovery-validation.json` 是从 route-field discovery register 派生的验证报告；它不放在本目录内，但由本域脚本生成并由本域审计器检查。
- `web/src/data/life-path-nhats-colectica-value-label-validation.json` 是从 Colectica value-label review protocol 派生的验证报告；它不放在本目录内，但由本域脚本生成并由本域审计器检查。
- `web/src/data/life-path-nhats-colectica-value-label-review-execution-validation.json` 是从 Colectica value-label review execution register 派生的验证报告；它不放在本目录内，但由本域脚本生成并由本域审计器检查。
- `web/src/data/life-path-nhats-colectica-access-route-probe-validation.json` 是从 Colectica access-route probe register 派生的验证报告；它不放在本目录内，但由本域脚本生成并由本域审计器检查。
- `web/src/data/life-path-nhats-colectica-authenticated-capture-template-validation.json` 是从 Colectica authenticated capture template 派生的验证报告；它不放在本目录内，但由本域脚本生成并由本域审计器检查。
- `web/src/data/life-path-nhats-l2-variable-family-admission-validation.json` 是从 L2 variable-family admission register 派生的验证报告；它不放在本目录内，但由本域脚本生成并由本域审计器检查。
- `web/src/data/life-path-nhats-preoutcome-aggregation-validation.json` 是从 pre-outcome aggregation protocol 派生的验证报告；它不放在本目录内，但由本域脚本生成并由本域审计器检查。
- 每份数据必须记录来源、抓取时间和处理脚本。

`raw/` 和 `processed/` 是可再生成的数据产物，已在根 `.gitignore` 中按多子域路径忽略；需要保留样例或发布快照时，应先写清来源、版本和体积边界。

## 当前文件

- `manual/interventions.json`：首批 20 个干预对象、类别、别名和检索词。
- `manual/higher_order_effects.tsv`：二阶 / 多阶效应、概率门、正负链路、研究域和来源引用。
- `manual/lev_route_cards.tsv`：R1-R9 主流路线卡、直接效应、一阶 / 二阶 / 多阶效应、概率门和禁止外推边界。
- `manual/life_path_toy_model_scenarios.json`：合成场景、基线风险、健康质量、控制变量和 LEV 阈值压力测试输入。
- `manual/life_path_public_mortality_anchor.json`：NCHS 2021 U.S. Life Tables 男性/女性年龄 40-100 的公开聚合 `qx/lx/dx/Lx/Tx/ex` 锚点，用于约束 baseline hazard 的现实尺度；它不是个人数据、不是校准结果、不是干预效果估计。
- `manual/life_path_calibration_readiness.json`：校准预备契约，记录 target population、time zero、outcome、estimand、predictor、censoring、validation、calibration、sensitivity、bias/applicability、reporting、prohibited use 和当前 cannot-calibrate-yet 边界。
- `manual/life_path_data_source_candidates.json`：候选数据源注册表，记录 HRS、NCHS linked mortality、UK Biobank、All of Us、NHATS、ELSA、SHARE 和 Framingham 等官方入口、覆盖标签、访问治理状态、限制和禁止外推边界。
- `manual/life_path_nhats_acquisition_readiness.json`：NHATS acquisition readiness 机器契约，记录官方入口、来源事实、提取前阻塞门、禁止动作和下一步证据，当前状态为 `cannot-extract-yet`。
- `manual/life_path_nhats_controlled_storage_destruction_plan.json`：NHATS controlled storage / destruction 计划，记录非仓库受控工作区、访问日志、清单槽位、销毁步骤、禁止位置和 readiness impact；当前状态为 `plan-only-not-executed-no-data-acquired`。
- `manual/life_path_nhats_file_tier_table.json`：NHATS R13/R14 文件层级表，记录 public-use registration-required 和 sensitive application-required 文件家族、官方路径、候选用途、阻塞项、方法文档依赖和禁止动作。
- `manual/life_path_nhats_first_estimand_protocol.json`：NHATS 第一版 estimand 协议，预注册 R13/R14 cohort-level functional-survival 问题、R13 time zero、R14 endpoint 边界、候选预测变量家族、缺失/删失路由、survey design 阻塞项和 aggregate-only 输出边界。
- `manual/life_path_nhats_variable_confirmation_matrix.json`：NHATS 变量确认矩阵，记录 Colectica/codebook 作为字段真相源、User Guide 命名/缺失码线索、Technical Paper 55 权重/方差方法线索、候选字段组、cohort-flow 模板、readiness gates 和禁止动作。
- `manual/life_path_nhats_cohort_flow_endpoint_protocol.json`：NHATS cohort-flow / endpoint-routing 协议，记录 R13/R14 队列流转行、R14 终点路由类、aggregate-only 输出契约、n < 5 披露控制、阻塞门和禁止动作，当前状态为 `protocol-only-cannot-extract`。
- `manual/life_path_nhats_disclosure_control_policy.json`：NHATS 披露控制策略，记录可公开输出的 aggregate-only 类型、小单元抑制阈值、row-level / public AI / individual prediction / calibration 禁止边界和 validator contract。
- `manual/life_path_nhats_disclosure_control_test_cases.json`：NHATS 披露控制合成测试集，覆盖 allow-export 与 block-export 两类结果，用于证明 validator 能阻断小单元未抑制、行级泄漏、public AI upload 和禁止输出类型。
- `manual/life_path_nhats_survey_design_protocol.json`：NHATS survey-design 协议，记录 R13/R14 加权估计前必须满足的 analysis weight、strata、PSU/variance unit、variance method、domain rule、missingness route、round linkage、disclosure validation 和 weighted-estimator review gate。
- `manual/life_path_nhats_survey_design_test_cases.json`：NHATS survey-design 合成测试集，覆盖 allow-weighted-diagnostics 与 block-weighted-estimate 两类结果，用于证明 validator 能阻断缺权重、缺分层、缺 PSU、缺方差方法和提前公共推断。
- `manual/life_path_nhats_missingness_route_protocol.json`：NHATS missingness / endpoint-route 协议，记录 alive self、alive proxy、alive facility/residential、known alive not interviewed、decedent/death boundary、missing/nonresponse、not classifiable、restricted-required 和 small-cell suppression 路由类及阻塞门。
- `manual/life_path_nhats_missingness_route_test_cases.json`：NHATS missingness-route 合成测试集，覆盖 allow-route-classification 与 block-route-classification 两类结果，用于证明 validator 能阻断 missingness-as-outcome、alive/death 冲突和小单元未抑制公开导出。
- `manual/life_path_nhats_route_field_discovery_register.json`：NHATS route-field discovery 登记表，记录 R13/R14 crosswalk 中的身份、状态、proxy、facility、death、missingness、design weight 和 disclosure cell count 候选字段，同时保留 Colectica、数据访问、分类器、披露和校准阻塞门。
- `manual/life_path_nhats_colectica_value_label_review_protocol.json`：NHATS Colectica value-label review 协议，记录字段级值标签复核、问题文本、universe/skip logic、route-value crosswalk、negative missing-code map、sensitive death-date exclusion、二次复核和 public-output disclosure 边界，当前状态为 `protocol-only-value-labels-not-reviewed`。
- `manual/life_path_nhats_colectica_value_label_review_execution_register.json`：NHATS Colectica value-label review 第一轮执行登记，记录官方来源追踪已准备、9 个 route-field source-trace 骨架、标准 `-1/-7/-8/-9` negative missing code family 和 10 个仍阻塞的晋升门，当前状态为 `partial-executed-official-source-trace-ready-colectica-login-required`。
- `manual/life_path_nhats_colectica_access_route_probe_register.json`：NHATS Colectica access-route probe 登记，记录官方 Cross-Year Search 入口、匿名访问登录边界、技术指南 SHA-256、Details/Basket capture workflow 和后续受控登录捕获步骤，当前状态为 `public-entry-and-technical-guide-probed-login-required`。
- `manual/life_path_nhats_colectica_authenticated_capture_template.json`：NHATS Colectica authenticated capture 模板，记录 9 个 route-field 进入真实变量页复核前必须补齐的证据槽，当前状态为 `template-only-authenticated-capture-not-started`。
- `manual/life_path_nhats_l2_variable_family_admission_register.json`：NHATS L2 variable-family admission 登记，记录 1 个窄 aggregate estimand 与 6 个 L2 候选变量族，当前状态为 `l2-variable-family-mapping-only-l4-blocked`。
- `manual/life_path_nhats_preoutcome_aggregation_protocol.json`：NHATS pre-outcome aggregation 协议，记录 8 条 L2-only 聚合规则、7 个合成用例、9 个真实聚合前置证据要求和禁止动作，当前状态为 `protocol-only-preoutcome-rules-frozen-l4-blocked`。
- `../../../../web/src/data/life-path-sensitivity-analysis.json`：由 `run_life_path_sensitivity_analysis.py` 生成的合成敏感性分析输出，记录 48 个一因素扰动结果、场景稳定性摘要、最敏感参数和禁止个体用途边界。
- `../../../../web/src/data/life-path-nhats-controlled-storage-destruction-validation.json`：由 `validate_nhats_controlled_storage_destruction_plan.py` 生成的 storage/destruction validation 输出，记录计划 hash、acquisition-readiness hash、15 个计划边界检查、partial readiness impact 和 no-download/no-extraction/no-calibration/no-individual-prediction 边界。
- `../../../../web/src/data/life-path-nhats-disclosure-control-validation.json`：由 `validate_nhats_disclosure_outputs.py` 生成的 disclosure-control validation 输出，记录 6 个合成用例、policy/test-case hash、allow/block 决策和 synthetic-only 边界。
- `../../../../web/src/data/life-path-nhats-survey-design-validation.json`：由 `validate_nhats_survey_design_plan.py` 生成的 survey-design validation 输出，记录 6 个合成用例、protocol/test-case hash、allow/block 决策和 synthetic-only 边界。
- `../../../../web/src/data/life-path-nhats-missingness-route-validation.json`：由 `validate_nhats_missingness_route_map.py` 生成的 missingness-route validation 输出，记录 8 个合成用例、protocol/test-case hash、allow/block 决策、route class 覆盖和 synthetic-only 边界。
- `../../../../web/src/data/life-path-nhats-route-field-discovery-validation.json`：由 `validate_nhats_route_field_discovery.py` 生成的 route-field discovery validation 输出，记录 register hash、source evidence、field family、blocking gate 和禁止用途检查结果。
- `../../../../web/src/data/life-path-nhats-colectica-value-label-validation.json`：由 `validate_nhats_colectica_value_label_protocol.py` 生成的 Colectica value-label validation 输出，记录 protocol hash、source evidence、artifact requirements、route-field review units、blocking gates 和 no-confirmed-value-label-map 边界。
- `../../../../web/src/data/life-path-nhats-colectica-value-label-review-execution-validation.json`：由 `validate_nhats_colectica_value_label_review_execution.py` 生成的 Colectica value-label execution validation 输出，记录 execution register hash、protocol hash、route-field discovery hash、source-trace-only 边界、standard negative-code family-only 边界和禁止 route classifier / public export / calibration / individual prediction 边界。
- `../../../../web/src/data/life-path-nhats-colectica-access-route-probe-validation.json`：由 `validate_nhats_colectica_access_route_probe.py` 生成的 Colectica access-route probe validation 输出，记录 probe register hash、execution register hash、匿名访问登录页边界、技术指南 workflow 和禁止 authenticated capture / export / calibration / individual prediction 边界。
- `../../../../web/src/data/life-path-nhats-colectica-authenticated-capture-template-validation.json`：由 `validate_nhats_colectica_authenticated_capture_template.py` 生成的 Colectica authenticated capture template validation 输出，记录 template hash、probe / execution / protocol / route-field register hash、9 个 route-field 捕获槽、敏感死亡字段排除和禁止 route classifier / public export / calibration / individual prediction 边界。
- `../../../../web/src/data/life-path-nhats-l2-variable-family-admission-validation.json`：由 `validate_nhats_l2_variable_family_admission.py` 生成的 L2 variable-family admission validation 输出，记录 first estimand、变量确认矩阵、模型准入契约、候选注册表和 capture template 的 source hash，并确认 6 个变量族仍只允许 L2 映射。
- `../../../../web/src/data/life-path-nhats-preoutcome-aggregation-validation.json`：由 `validate_nhats_preoutcome_aggregation_protocol.py` 生成的 pre-outcome aggregation validation 输出，记录协议和上游 source hash、8 条聚合规则、7 个合成用例、真实聚合前置证据和禁止真实聚合 / 加权估计 / L4 准入 / 校准 / 个体预测边界。
- `raw/`：采集脚本保存的原始响应。
- `processed/`：采集脚本生成的 JSONL 索引和汇总。
- `processed/hagr/`：HAGR 官方 zip 快照解压后的 CSV 文件。
