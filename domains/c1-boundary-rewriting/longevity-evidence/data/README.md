# 数据目录

这里存放 Longevity Evidence 子域的公开数据源样例、原始快照和清洗后数据。

## 规则

- `raw/` 用于原始 API 响应或下载文件。
- `processed/` 用于清洗后的结构化数据。
- `manual/` 用于人工整理的首批 MVP 数据。
- `manual/higher_order_effects.tsv` 用于维护 LEV 二阶 / 多阶效应模型输入。
- `manual/lev_route_cards.tsv` 用于维护 LEV 主流路线卡模型输入。
- `manual/life_path_toy_model_scenarios.json` 用于维护生命路径 toy model 的合成队列场景输入。
- `manual/life_path_calibration_readiness.json` 用于维护生命路径模型从 toy model 进入校准模型前必须满足的研究设计、报告、验证和禁止用途字段。
- `manual/life_path_data_source_candidates.json` 用于维护生命路径模型后续可能使用的官方队列、死亡链接、老龄化面板和外部验证候选源；该文件只登记候选和治理边界，不表示已经下载、访问或校准。
- `manual/life_path_nhats_acquisition_readiness.json` 用于维护 NHATS 从候选数据源进入真实提取前的机器可读准入门；该文件只记录官方来源刷新、注册、文件层级、Colectica 变量确认、survey design、endpoint、披露控制、AI 边界和存储销毁要求，不表示已经 acquisition-ready。
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
- `web/src/data/life-path-sensitivity-analysis.json` 是从 `manual/life_path_toy_model_scenarios.json` 派生的合成 sensitivity 输出；它不放在本目录内，但由本域脚本生成并由本域审计器检查。
- `web/src/data/life-path-nhats-disclosure-control-validation.json` 是从披露控制 policy 和 synthetic test cases 派生的验证报告；它不放在本目录内，但由本域脚本生成并由本域审计器检查。
- `web/src/data/life-path-nhats-survey-design-validation.json` 是从 survey-design protocol 和 synthetic test cases 派生的验证报告；它不放在本目录内，但由本域脚本生成并由本域审计器检查。
- `web/src/data/life-path-nhats-missingness-route-validation.json` 是从 missingness-route protocol 和 synthetic test cases 派生的验证报告；它不放在本目录内，但由本域脚本生成并由本域审计器检查。
- `web/src/data/life-path-nhats-route-field-discovery-validation.json` 是从 route-field discovery register 派生的验证报告；它不放在本目录内，但由本域脚本生成并由本域审计器检查。
- 每份数据必须记录来源、抓取时间和处理脚本。

`raw/` 和 `processed/` 是可再生成的数据产物，已在根 `.gitignore` 中按多子域路径忽略；需要保留样例或发布快照时，应先写清来源、版本和体积边界。

## 当前文件

- `manual/interventions.json`：首批 20 个干预对象、类别、别名和检索词。
- `manual/higher_order_effects.tsv`：二阶 / 多阶效应、概率门、正负链路、研究域和来源引用。
- `manual/lev_route_cards.tsv`：R1-R9 主流路线卡、直接效应、一阶 / 二阶 / 多阶效应、概率门和禁止外推边界。
- `manual/life_path_toy_model_scenarios.json`：合成场景、基线风险、健康质量、控制变量和 LEV 阈值压力测试输入。
- `manual/life_path_calibration_readiness.json`：校准预备契约，记录 target population、time zero、outcome、estimand、predictor、censoring、validation、calibration、sensitivity、bias/applicability、reporting、prohibited use 和当前 cannot-calibrate-yet 边界。
- `manual/life_path_data_source_candidates.json`：候选数据源注册表，记录 HRS、NCHS linked mortality、UK Biobank、All of Us、NHATS、ELSA、SHARE 和 Framingham 等官方入口、覆盖标签、访问治理状态、限制和禁止外推边界。
- `manual/life_path_nhats_acquisition_readiness.json`：NHATS acquisition readiness 机器契约，记录官方入口、来源事实、提取前阻塞门、禁止动作和下一步证据，当前状态为 `cannot-extract-yet`。
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
- `../../../../web/src/data/life-path-sensitivity-analysis.json`：由 `run_life_path_sensitivity_analysis.py` 生成的合成敏感性分析输出，记录 48 个一因素扰动结果、场景稳定性摘要、最敏感参数和禁止个体用途边界。
- `../../../../web/src/data/life-path-nhats-disclosure-control-validation.json`：由 `validate_nhats_disclosure_outputs.py` 生成的 disclosure-control validation 输出，记录 6 个合成用例、policy/test-case hash、allow/block 决策和 synthetic-only 边界。
- `../../../../web/src/data/life-path-nhats-survey-design-validation.json`：由 `validate_nhats_survey_design_plan.py` 生成的 survey-design validation 输出，记录 6 个合成用例、protocol/test-case hash、allow/block 决策和 synthetic-only 边界。
- `../../../../web/src/data/life-path-nhats-missingness-route-validation.json`：由 `validate_nhats_missingness_route_map.py` 生成的 missingness-route validation 输出，记录 8 个合成用例、protocol/test-case hash、allow/block 决策、route class 覆盖和 synthetic-only 边界。
- `../../../../web/src/data/life-path-nhats-route-field-discovery-validation.json`：由 `validate_nhats_route_field_discovery.py` 生成的 route-field discovery validation 输出，记录 register hash、source evidence、field family、blocking gate 和禁止用途检查结果。
- `raw/`：采集脚本保存的原始响应。
- `processed/`：采集脚本生成的 JSONL 索引和汇总。
- `processed/hagr/`：HAGR 官方 zip 快照解压后的 CSV 文件。
