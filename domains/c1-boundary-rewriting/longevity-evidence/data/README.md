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
- `web/src/data/life-path-sensitivity-analysis.json` 是从 `manual/life_path_toy_model_scenarios.json` 派生的合成 sensitivity 输出；它不放在本目录内，但由本域脚本生成并由本域审计器检查。
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
- `../../../../web/src/data/life-path-sensitivity-analysis.json`：由 `run_life_path_sensitivity_analysis.py` 生成的合成敏感性分析输出，记录 48 个一因素扰动结果、场景稳定性摘要、最敏感参数和禁止个体用途边界。
- `raw/`：采集脚本保存的原始响应。
- `processed/`：采集脚本生成的 JSONL 索引和汇总。
- `processed/hagr/`：HAGR 官方 zip 快照解压后的 CSV 文件。
