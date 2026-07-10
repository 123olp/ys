# Human Infra Maturity Roadmap

本文档定义 Human Infra 从“讲清楚价值”走向“严肃研究框架”和“可运行定量模型”的 100% 状态。它不是宣传稿，而是验收契约：任何阶段都必须能说明目标、对象、边界、证据、模型和不能外推的部分。

机器可读缺口账本见 [`human-infra-maturity-gap-register.json`](human-infra-maturity-gap-register.json)。路线图负责解释 100% 状态，缺口账本负责把当前未完成项拆成 gate、证据路径、缺失证据和下一步动作，并由 `make maturity-gap-audit` 检查。

模型准入契约见 [`human-infra-model-admission-contract.json`](human-infra-model-admission-contract.json)，由 `make model-admission-contract-audit` 检查 L0-L5 准入层级、MAC gates、hard abort gates、方法锚点和当前 B1-B9 reviewed artifacts 的 L1/L2-only 边界。该契约只打开“如何拒绝错误准入”和“如何进入下一步候选注册表”，不打开校准预测、干预效果或个体用途。

模型准入候选注册表见 [`human-infra-model-admission-candidate-registry.json`](human-infra-model-admission-candidate-registry.json)，由 `make model-admission-candidate-registry-audit` 检查 11 个 reviewed artifact registers、1386 个 reviewed artifacts、66 个 blocked rows、现有 L3 synthetic / public aggregate baseline、public NHANES-LMF aggregate pilot 和 blocked L4 candidates 的准入边界。该注册表只证明“当前哪些材料被拒绝升格”，不证明任何 calibrated model 已成立。

定量能力分层见 [`human-infra-quantitative-capability-ladder.json`](human-infra-quantitative-capability-ladder.json)，由 `make quantitative-capability-ladder-audit` 检查 Q0-Q5 输出能力、Q3 当前最高能力、Q4/Q5 阻塞状态、公共 Web 可消费输出和个人死亡日期/医学建议/干预排序禁用边界，并生成 [`../../web/src/data/human-infra-quantitative-capability-ladder-validation.json`](../../web/src/data/human-infra-quantitative-capability-ladder-validation.json)。该分层只说明“当前能展示什么、不能展示什么、晋级需要什么证据”，不打开 Q4 aggregate calibrated research model、Q5 individual decision support 或任何个人预测。

域到模型桥接契约见 [`human-infra-domain-to-model-bridge-contract.json`](human-infra-domain-to-model-bridge-contract.json)，代表性注册表见 [`human-infra-domain-to-model-bridge-register.json`](human-infra-domain-to-model-bridge-register.json)，由 `make domain-to-model-bridge-audit` 检查 C1-C6 研究域是否只进入 B2/L2/Q2 候选变量、候选机制和模型位置说明，并生成 [`../../web/src/data/human-infra-domain-to-model-bridge-validation.json`](../../web/src/data/human-infra-domain-to-model-bridge-validation.json)。该桥接层只说明“研究域如何进入模型语言”，不打开系数、因果效应、校准聚合预测、个体用途、医学建议、干预排序或个人死亡日期输出。

L4 模型准入阻塞矩阵见 [`human-infra-l4-model-readiness-blocker-matrix.json`](human-infra-l4-model-readiness-blocker-matrix.json)，由 `make l4-model-readiness-blocker-matrix-audit` 检查 NHANES public-use LMF 本地加权域输出、NHANES 披露审查执行状态、NHATS R13/R14 L4 runway、模型准入契约和 public Web no-real-values 门之间的阻塞关系。该矩阵只把 L4 仍缺的 governed access、exact field/value confirmation、real extraction、survey design/public output review、validation/calibration 证据列成可执行 work orders，不打开 public weighted output、calibrated prediction 或个体用途。

L4 解阻执行计划见 [`human-infra-l4-unblock-execution-plan.json`](human-infra-l4-unblock-execution-plan.json)，由 `make l4-unblock-execution-plan-audit` 检查从阻塞矩阵到真实执行的 work orders：NHATS governed access、Colectica exact field/value confirmation、NHATS real extraction/cohort flow、NHANES human disclosure review 和 validation/calibration diagnostics。该计划只定义直接证据、依赖顺序、不可替代证据和禁止用途，不能用来替代人工审查、外部受控访问或校准诊断。

L4 证据 intake 寄存器见 [`human-infra-l4-evidence-intake-register.json`](human-infra-l4-evidence-intake-register.json)，人工审查流程见 [`human-infra-l4-evidence-packet-review-playbook.md`](human-infra-l4-evidence-packet-review-playbook.md)。`make l4-evidence-intake-register-audit` 检查 5 个 work orders 的 24 个待填证据槽位是否仍为 pending，是否定义零 packet 的 `human-infra.l4-evidence-packet.v1` 契约，是否拒绝 raw rows、identifier-bearing files、restricted data copies、public AI upload、AI-only signoff 和无 hash 的自然语言主张，并确认 playbook 仍要求 redacted SHA-256、人工 reviewer、second reviewer、bounded L4 evidence review 和 `l4-still-blocked`。该寄存器和 playbook 只定义“证据如何安全进入审查、以后每个证据包必须长什么样、审查时如何拒绝或保持 blocked”，不代表已有直接证据。

L4 证据包 validator 测试契约见 [`human-infra-l4-evidence-packet-validator-test-cases.json`](human-infra-l4-evidence-packet-validator-test-cases.json)，由 `make l4-evidence-packet-validator-audit` 检查 synthetic future packet 是否只能进入 `reviewable-but-still-blocked`、`cannot-evaluate` 或 `rejected`，并生成 [`../../web/src/data/life-path-l4-evidence-packet-validator-validation.json`](../../web/src/data/life-path-l4-evidence-packet-validator-validation.json)。该 gate 只证明未来证据包预检规则可运行，不代表真实 evidence packet、人审完成、slot closure、L4 admission、公开加权输出或个体预测。

NHATS Colectica capture packet validator 测试契约见 [`life_path_nhats_colectica_capture_packet_validator_test_cases.json`](../../domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_colectica_capture_packet_validator_test_cases.json)，由 `make nhats-colectica-capture-packet-validator-audit` 检查未来 Colectica 捕获包只能进入 `reviewable-but-still-blocked`、`cannot-evaluate` 或 `rejected`，并生成 [`../../web/src/data/life-path-nhats-colectica-capture-packet-validator-validation.json`](../../web/src/data/life-path-nhats-colectica-capture-packet-validator-validation.json)。该 gate 只证明 G4 字段/值标签补证的预检规则可运行，不代表 controlled login、真实变量页捕获、slot closure、route classifier、真实提取、公开导出、校准或个体预测。

NHATS Colectica capture packet draft / handoff 本地准备器见 [`build_nhats_colectica_capture_packet_draft.py`](../../domains/c1-boundary-rewriting/longevity-evidence/scripts/build_nhats_colectica_capture_packet_draft.py) 和 [`build_nhats_colectica_capture_packet_review_handoff.py`](../../domains/c1-boundary-rewriting/longevity-evidence/scripts/build_nhats_colectica_capture_packet_review_handoff.py)，由 `make nhats-colectica-capture-packet-draft-audit` 与 `make nhats-colectica-capture-packet-review-handoff-audit` 在 ignored `build/reports/` 下为 39 个 capture tasks 批量生成 fail-closed draft packets、逐项 validation、batch validation 和 review handoff 报告。该准备层只降低未来受控人工捕获、复核和交接的操作摩擦，不写 tracked review execution register，不关闭任何 slot，不证明 controlled login、真实字段确认、route-value rows、真实提取、公开导出、校准或个体预测。

NHATS Colectica capture-packet review execution 寄存器见 [`life_path_nhats_colectica_capture_packet_review_execution_register.json`](../../domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_colectica_capture_packet_review_execution_register.json)，由 `make nhats-colectica-capture-packet-review-execution-audit` 检查 39 个捕获包审查槽位是否全部仍为 pending，是否保持 0 个真实包、0 个人审完成、0 个二审完成、0 个 slot closure、0 个 route classifier admission，并生成 [`../../web/src/data/life-path-nhats-colectica-capture-packet-review-execution-validation.json`](../../web/src/data/life-path-nhats-colectica-capture-packet-review-execution-validation.json)。该 gate 只把“未来人工捕获证据如何进入审查执行账本”机器化，不代表 controlled login、真实字段确认、slot closure、真实提取、校准或个体预测。

NHATS route-value crosswalk entry validator 测试契约见 [`life_path_nhats_route_value_crosswalk_entry_validator_test_cases.json`](../../domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_route_value_crosswalk_entry_validator_test_cases.json)，由 `make nhats-route-value-crosswalk-entry-validator-audit` 检查未来 route-value / missing-code crosswalk 条目只能进入 `reviewable-but-still-blocked`、`cannot-evaluate` 或 `rejected`，并生成 [`../../web/src/data/life-path-nhats-route-value-crosswalk-entry-validator-validation.json`](../../web/src/data/life-path-nhats-route-value-crosswalk-entry-validator-validation.json)。该 gate 只证明未来条目预检语义可运行，不代表真实 Colectica 登录、真实字段确认、route-value rows、变量级 missing-code maps、slot closure、route classifier、真实提取、公开导出、校准或个体预测。

L4 验证/校准报告契约见 [`human-infra-l4-validation-calibration-reporting-contract.json`](human-infra-l4-validation-calibration-reporting-contract.json)，由 `make l4-validation-calibration-reporting-contract-audit` 检查 L4WO-05 是否绑定 12 个报告段落、5 个证据槽、TRIPOD+AI / PROBAST+AI 风格报告边界、校准诊断、真实参数敏感性、偏倚适用性审查和零报告包阻塞状态。该契约只说明“未来合格报告包必须长什么样”，不代表已经有真实验证报告、校准诊断、外部验证、public weighted-domain output、calibrated prediction 或个体用途。

外部科研标准锚点注册表见 [`human-infra-research-standards-source-anchor-register.json`](human-infra-research-standards-source-anchor-register.json)，由 `make research-standards-source-anchor-audit` 检查 TRIPOD+AI、PROBAST+AI、STROBE、RECORD、CONSORT、SPIRIT、CONSORT-AI、SPIRIT-AI、PRISMA、GRADE、RoB 2、ROBINS-I、target trial emulation、STaRT-RWE 和 ISPOR-SMDM 路线是否进入报告、偏倚、证据等级、因果设计、RWE 和模型透明度门禁，并生成 [`../../web/src/data/human-infra-research-standards-source-anchor-validation.json`](../../web/src/data/human-infra-research-standards-source-anchor-validation.json)。该注册表只说明“我们用哪些外部标准约束证据和模型报告”，不证明外部文献真实性、干预效果、模型校准、个体预测、医学建议或长寿逃逸速度。

L4 验证/校准报告执行寄存器见 [`human-infra-l4-validation-calibration-report-execution-register.json`](human-infra-l4-validation-calibration-report-execution-register.json)，由 `make l4-validation-calibration-report-execution-register-audit` 检查 12 个报告段落和 5 个 L4WO-05 槽位是否全部仍为 pending real report packet，是否仅连接合成 dry-run 而不把它误升格为真实验证/校准证据，并生成 [`../../web/src/data/life-path-l4-validation-calibration-report-execution-validation.json`](../../web/src/data/life-path-l4-validation-calibration-report-execution-validation.json)。该寄存器只把“真实报告包尚未进入”的执行状态变成机器可审计对象，不打开 L4 admission、公开加权输出、calibrated prediction 或个体用途。

NHATS official source refresh 寄存器见 [`life_path_nhats_official_source_refresh_register.json`](../../domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_official_source_refresh_register.json)，由 `make nhats-official-source-refresh-audit` 检查 8 个官方公开来源的 HTTP 状态、内容长度、SHA-256、2026-07-04 live reprobe、gate impact 和 no-download / no-extraction / no-calibration / no-individual-prediction 边界。该寄存器只把 official-source-refresh 门升为 ready，不打开真实下载、提取、校准或个体预测；HTML hash 波动只作为动态页面重探证据，不能被解释为语义稳定或字段确认。

NHATS registration evidence 模板见 [`life_path_nhats_registration_evidence_template.json`](../../domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_registration_evidence_template.json)，由 `make nhats-registration-evidence-template-audit` 检查 8 个注册/访问证据槽、redacted-only 仓库边界和 no-registration-proof / no-download / no-extraction / no-calibration / no-individual-prediction 边界。该模板只把 registration-status 推进为 partial-template-only，不证明 NHATS 注册、访问授权、受控工作区或数据准入完成。

NHATS registration evidence packet validator 测试契约见 [`life_path_nhats_registration_evidence_packet_validator_test_cases.json`](../../domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_registration_evidence_packet_validator_test_cases.json)，由 `make nhats-registration-evidence-packet-validator-audit` 检查未来 redacted 注册证据包只能进入 `reviewable-but-still-blocked`、`cannot-evaluate` 或 `rejected`，并生成 [`../../web/src/data/life-path-nhats-registration-evidence-packet-validator-validation.json`](../../web/src/data/life-path-nhats-registration-evidence-packet-validator-validation.json)。该 gate 只证明注册证据包预检语义可运行，不代表 NHATS 注册完成、访问授权、受控工作区执行、下载、抽取、校准或个体预测。

NHATS L4 readiness runway 见 [`life_path_nhats_l4_readiness_runway.json`](../../domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_l4_readiness_runway.json)，由 `make nhats-l4-readiness-runway-audit` 检查 12 个 readiness gates、上游 source hash 和 no-real-extraction / no-calibration / no-individual-prediction 边界。该 runway 只把从 L2 设计资产进入 L4 前的阻塞门串起来，不打开 L4 calibrated admission。

NHANES public-use LMF aggregate pilot 见 [`life_path_nhanes_public_lmf_aggregate_pilot.json`](../../domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhanes_public_lmf_aggregate_pilot.json)，由 `make nhanes-public-lmf-aggregate-pilot-audit` 检查 CDC/NCHS 公开 NHANES 2017-2018 Linked Mortality File 与 DEMO_J 的 SEQN join、固定宽度字段契约、sex × ageBand 聚合、source hash、no-raw-rows / no-individual-prediction / no-calibration / no-survey-population-inference 边界。该试运行只把 MODEL-G3 从完全 blocked 推进为 partial，不打开 NHATS L4、加权估计、外部验证、校准或个体用途。

NHANES public-use LMF positive-weight eligible-base readiness 见 [`life_path_nhanes_public_lmf_eligible_base_readiness.json`](../../domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhanes_public_lmf_eligible_base_readiness.json)，由 `make nhanes-public-lmf-eligible-base-readiness-audit` 检查 `WTMEC2YR > 0` eligible-base 诊断、5809 名 positive-weight eligible adults、145 个 eligible adult deaths、15 个 positive-weight strata、minimum PSU per stratum = 2、no lonely positive-weight strata、no-row-persistence 和 no-weighted-domain-inference 边界。该门只把 NHANES public-use LMF 从 domain-rule readiness 推进到 eligible-base diagnostic readiness，不打开加权域死亡率、design-based confidence interval、校准或个体用途。

NHANES public-use LMF weighted-estimator readiness 见 [`life_path_nhanes_public_lmf_weighted_estimator_readiness.json`](../../domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhanes_public_lmf_weighted_estimator_readiness.json)，由 `make nhanes-public-lmf-weighted-estimator-readiness-audit` 检查 R `survey` / `svydesign` 后端选择、`WTMEC2YR` / `SDMVPSU` / `SDMVSTRA` / `nest=true` design-object 合约、domain indicator 合约、5 个 ready gates、4 个 blocked gates 和 no-weighted-domain-output 边界。该门只把 NHANES public-use LMF 从 eligible-base diagnostic readiness 推进到 estimator-backend-selected readiness，不打开 R runtime smoke、weighted domain output、design-based confidence interval、校准或个体用途。

NHANES public-use LMF R survey runtime smoke readiness 见 [`life_path_nhanes_public_lmf_r_survey_runtime_smoke_readiness.json`](../../domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhanes_public_lmf_r_survey_runtime_smoke_readiness.json)，由 `make nhanes-public-lmf-r-survey-runtime-smoke-audit` 检查当前环境是否具备 `Rscript`、R `survey` 包、synthetic `svydesign` 和 domain `subset` smoke 能力。默认当前环境门只记录本机依赖状态，不安装依赖；它可以记录 `blocked-no-rscript` 并仍然通过边界契约，因为它的职责是探测和阻塞输出，不是提供可复现运行时。controlled runtime 见 [`nhanes-public-lmf-r-survey-conda.yml`](../../domains/c1-boundary-rewriting/longevity-evidence/runtime/nhanes-public-lmf-r-survey-conda.yml)，由 `make nhanes-public-lmf-r-survey-controlled-runtime-smoke-audit` 创建或复用 `.runtime/nhanes-r-survey/`，并已生成 `life-path-nhanes-public-lmf-r-survey-controlled-runtime-smoke-validation.json`。该 controlled smoke 才是 R `survey` synthetic 运行时可复现证据，不打开 weighted domain output、design-based confidence interval、校准或个体用途。

NHANES public-use LMF domain indicator metadata diagnostic 见 [`life_path_nhanes_public_lmf_domain_indicator_diagnostic.json`](../../domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhanes_public_lmf_domain_indicator_diagnostic.json)，由 `make nhanes-public-lmf-domain-indicator-diagnostic-audit` 检查 8 个 sex × ageBand 公开聚合域组合、上游 aggregate pilot / weighted-estimator / controlled runtime validation hash、no-row-persistence、no-count-repeat、no-weighted-sum-repeat 和 no-weighted-domain-output 边界。该门只把 domain indicator metadata diagnostic 升为 ready，不打开 DOF/sparse-domain review、disclosure-reviewed output、weighted rates、design-based intervals、校准或个体用途。

NHANES public-use LMF DOF / sparse-domain metadata diagnostic 见 [`life_path_nhanes_public_lmf_dof_sparse_domain_diagnostic.json`](../../domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhanes_public_lmf_dof_sparse_domain_diagnostic.json)，由 `make nhanes-public-lmf-dof-sparse-domain-diagnostic-audit` 检查官方 NHANES subgroup DOF 规则、NCHS df < 8 review flag、8 个 sex × ageBand 公开聚合域、minimum observed domain df = 15、0 个 lonely represented strata、0 个 empty domains、0 个 configured sparse-domain flags、no-row-persistence、no-per-domain-count 和 no-weighted-output 边界。该门只把 DOF/sparse metadata diagnostic 升为 ready，不打开 disclosure-reviewed output、weighted rates、design-based intervals、有效样本量发布审查、校准或个体用途。

NHANES public-use LMF disclosure output envelope 见 [`life_path_nhanes_public_lmf_disclosure_output_envelope_policy.json`](../../domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhanes_public_lmf_disclosure_output_envelope_policy.json) 和 [`life_path_nhanes_public_lmf_disclosure_output_envelope_test_cases.json`](../../domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhanes_public_lmf_disclosure_output_envelope_test_cases.json)，由 `make nhanes-public-lmf-disclosure-output-envelope-audit` 检查 8 个 synthetic allow/block 用例、small-cell suppression、low-DOF suppression、forbidden keys、forbidden output types、no-row-level、no-public-AI 和 no-real-output 边界。该门只把 disclosure output shape 的合成审查升为 ready，不打开真实 public weighted-domain output。

NHANES public-use LMF effective sample / CI publication gate 见 [`life_path_nhanes_public_lmf_effective_sample_ci_publication_policy.json`](../../domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhanes_public_lmf_effective_sample_ci_publication_policy.json) 和 [`life_path_nhanes_public_lmf_effective_sample_ci_publication_test_cases.json`](../../domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhanes_public_lmf_effective_sample_ci_publication_test_cases.json)，由 `make nhanes-public-lmf-effective-sample-ci-publication-audit` 检查 9 个 synthetic allow/block 用例、effective sample class、CI width class、RSE class、DOF、forbidden real-output type、no-public-AI 和 no-real-output 边界。该门只把 publication reliability shape 的合成审查升为 ready，不打开真实 effective sample size、真实 design-based confidence interval 或发布许可。

NHANES public-use LMF weighted-output implementation preflight 见 [`life_path_nhanes_public_lmf_weighted_output_implementation_preflight_policy.json`](../../domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhanes_public_lmf_weighted_output_implementation_preflight_policy.json) 和 [`life_path_nhanes_public_lmf_weighted_output_implementation_preflight_test_cases.json`](../../domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhanes_public_lmf_weighted_output_implementation_preflight_test_cases.json)，由 `make nhanes-public-lmf-weighted-output-implementation-preflight-audit` 检查 8 个 synthetic allow/block 用例、R `survey` / `svydesign` / post-design `survey::subset` 计划、no row-drop-before-design、no row persistence、forbidden count keys、forbidden real-output type、no-public-AI、no-individual-output 和 no-real-output 边界。该门只把 implementation-shape 的合成审查升为 ready，不执行真实 weighted-domain output。

NHANES public-use LMF disclosure review template 见 [`life_path_nhanes_public_lmf_disclosure_review_template.json`](../../domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhanes_public_lmf_disclosure_review_template.json)，由 `make nhanes-public-lmf-disclosure-review-template-audit` 检查 15 个 pending review slots、second-reviewer、output hash、suppression review、effective sample / CI review、forbidden-field scan、retention plan 和 release decision 槽位。该门只把真实输出披露审查的 packet 结构升为 ready，不完成真实 disclosure review，也不授权 public weighted-domain output。

NHANES public-use LMF disclosure review execution register 见 [`life_path_nhanes_public_lmf_disclosure_review_execution_register.json`](../../domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhanes_public_lmf_disclosure_review_execution_register.json)，由 `make nhanes-public-lmf-disclosure-review-execution-audit` 检查 15 个 review slots、8 个 machine-prefill-eligible slots、0 个 completed human-review slots、无 reviewed output hash、无 second reviewer signoff、release blocked 和 no-real-output 边界。该门只把人工披露审查执行状态机升为 ready，不完成真实 disclosure review。

NHANES public-use LMF weighted-domain output readiness 见 [`life_path_nhanes_public_lmf_weighted_domain_output_readiness.json`](../../domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhanes_public_lmf_weighted_domain_output_readiness.json)，由 `make nhanes-public-lmf-weighted-domain-output-readiness-audit` 检查上游 weighted-estimator readiness、default / controlled runtime smoke validation、domain indicator metadata diagnostic、DOF/sparse-domain metadata diagnostic、synthetic disclosure output envelope、synthetic effective sample / CI publication gate、synthetic weighted-output implementation preflight、disclosure review template、disclosure review execution register、local-only ignored run、local disclosure review packet、real disclosure review 和 no-public-weighted-domain-output 边界。该门登记 12 个 ready gates、2 个 blocked gates；DOF/sparse metadata、synthetic disclosure envelope、synthetic publication criteria、synthetic implementation preflight、disclosure review template 与 disclosure review execution register 已完成；本地受控真实 weighted-domain 运行已可由 `make nhanes-public-lmf-weighted-domain-output-local-run-audit` 写入已忽略的 `build/reports/nhanes-public-lmf-weighted-domain-output-local/validation.json`，生成 8 个 sex × ageBand 本地审计 cells、真实 weighted mortality rates 和 design-based confidence intervals；本地 disclosure review packet 已可由 `make nhanes-public-lmf-local-disclosure-review-packet-audit` 写入已忽略的 `build/reports/nhanes-public-lmf-local-disclosure-review-packet/validation.json`，并把 redacted packet 审计结果写入同一 ignored 目录下的 `packet-validation.json`，只绑定 output hash、来源、runtime、redacted summary 和 review slots，不复制真实 rates / intervals；默认 readiness 审计与 `make check` 不读取这些 ignored local outputs，干净 checkout 可以没有 `build/reports/`；但人工 disclosure review 和公开 output implementation 仍阻塞，不写入 `web/src/data`，不生成版本化公开 weighted rates / design-based intervals、校准输入或个体用途。

NHANES public-use LMF local run evidence manifest 见 [`life_path_nhanes_public_lmf_local_run_evidence_manifest.json`](../../domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhanes_public_lmf_local_run_evidence_manifest.json)，由 `make nhanes-public-lmf-local-run-evidence-manifest-audit` 检查 ignored 本地 weighted-domain report、local disclosure packet 和 packet-validation 的哈希、运行环境、8 个审计 cells、minimum DOF 15、0 个 human-reviewed slots、tracked values omitted 和 public output blocked 边界。该 manifest 是版本化 redacted 证明层：它证明本地真实 public-use weighted-domain run 已执行且可被 hash 追踪，但不复制真实 weighted rates、standard errors、design-based intervals 或行级数据，也不授权公开输出、校准输入或个体用途。

NHANES public-use LMF public-output implementation review template 见 [`life_path_nhanes_public_lmf_public_output_implementation_review_template.json`](../../domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhanes_public_lmf_public_output_implementation_review_template.json)，由 `make nhanes-public-lmf-public-output-implementation-review-template-audit` 检查 12 个 pending implementation review slots、前端 JSON source binding、fresh no-real-values scan、static build review、page rendering boundary review、rollback plan、boundary copy review 和 second reviewer signoff。该门只把公开前端实现审查 packet 结构升为 ready，不完成 public implementation review，也不授权 public weighted-domain output、calibration 或 individual prediction。

NHANES public-use LMF public-output implementation review execution register 见 [`life_path_nhanes_public_lmf_public_output_implementation_review_execution_register.json`](../../domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhanes_public_lmf_public_output_implementation_review_execution_register.json)，由 `make nhanes-public-lmf-public-output-implementation-review-execution-audit` 检查 12 个 implementation review execution slots、0 个 human-reviewed slots、无 reviewed artifact hash、无 front-end artifact review、无 second reviewer signoff、无 final implementation decision 和 release blocked 边界。该门只把公开前端实现审查执行状态升为可审计，不完成 public implementation review，也不授权 public weighted-domain output、calibration 或 individual prediction。

NHANES public-use LMF public release gate 见 [`life-path-nhanes-public-lmf-public-release-gate-validation.json`](../../web/src/data/life-path-nhanes-public-lmf-public-release-gate-validation.json)，由 `make nhanes-public-lmf-public-release-gate-audit` 汇合 disclosure review execution、public Web no-real-values scan、local-run evidence manifest、weighted-domain readiness、public-output implementation review template 和 public-output implementation review execution register，输出 `blocked-pending-human-disclosure-review` 的公开发布决策。该门是发布决策控制面：它不读取 ignored real output，不公开真实 weighted rates、standard errors、design-based intervals，不授权 public weighted-domain output、calibration 或 individual prediction。

NHANES public-use LMF public Web data no-real-values gate 见 [`life-path-nhanes-public-lmf-public-web-data-no-real-values-validation.json`](../../web/src/data/life-path-nhanes-public-lmf-public-web-data-no-real-values-validation.json)，由 `make nhanes-public-lmf-public-web-data-no-real-values-audit` 扫描 `web/src/data/life-path-nhanes-public-lmf-*.json`，阻止真实 weighted rates、standard errors、confidence intervals、行级字段、个体预测字段和越界 release/calibration flags 进入公开前端数据层。该门是发布层回归护栏，不替代人工 disclosure review、public output implementation review 或 suppression / reliability review。

页面级主张一致性账本见 [`human-infra-page-claim-consistency.json`](human-infra-page-claim-consistency.json)，由 `make page-claim-audit` 检查 README、Web 首页、论文页和关键 reference 页面是否都保留同一组 Claim ID 与禁止用途边界。

受众-主张映射账本见 [`human-infra-audience-claim-map.json`](human-infra-audience-claim-map.json)，由 `make audience-claim-map-audit` 检查研究者、构建者、长寿读者、基础设施读者、治理审查者和模型开发者是否都通过同一 Claim spine 理解项目，并保留邻近项目边界与禁止误读。

论文页强主张账本见 [`human-infra-paper-claim-register.json`](human-infra-paper-claim-register.json)，由 `make paper-claim-audit` 检查每个 arXiv-style 论文页是否注册了论文级强主张、核心 Claim ID、反证条件、降级动作和禁止用途边界。

域级反证覆盖账本见 [`human-infra-domain-falsifier-coverage.json`](human-infra-domain-falsifier-coverage.json)，由 `make domain-falsifier-audit` 检查 C1 全域和优先 C2 域是否具备强主张、变量接口、反证条件、降级动作和禁止用途脚手架。

反证 Source Card 锚点回填账本见 [`human-infra-falsifier-source-card-backfill.json`](human-infra-falsifier-source-card-backfill.json)，由 `make falsifier-source-audit` 检查当前论文强主张和 C1/C2 优先域反证是否具备来源锚点、证据角色、可用范围、迁移边界和后续 Source Card 动作。

反证 Source Card 字段级抽取账本见 [`human-infra-falsifier-source-card-extraction.json`](human-infra-falsifier-source-card-extraction.json)，由 `make falsifier-source-extraction-audit` 检查当前全部来源锚点是否进入来源身份、域、论文 claim、模型位置、反证用途、迁移边界和人工可读包。

域级 Claim-Evidence Matrix 见 [`human-infra-domain-claim-evidence-matrix.json`](human-infra-domain-claim-evidence-matrix.json)，由 `make domain-claim-matrix-audit` 检查当前 30 个优先研究域是否 join 到域强主张来源、变量契约来源、反证来源、字段级 Source Card ID、禁止用途和下一步抽取动作。

域 Source Card 字段抽取账本见 [`human-infra-domain-source-card-field-extraction.json`](human-infra-domain-source-card-field-extraction.json)，由 `make domain-field-extraction-audit` 检查当前 30 个优先研究域是否具备 endpoint 候选、population 槽位、uncertainty 槽位、transfer-boundary 槽位、禁止用途和 source-specific 深读动作。

域-来源深读队列见 [`human-infra-domain-source-specific-extraction-queue.json`](human-infra-domain-source-specific-extraction-queue.json)，由 `make domain-source-queue-audit` 检查 30 个域字段行是否派生为 93 个 domain-source 精读任务，并确认 exact claim、endpoint、population、uncertainty 和 transfer-boundary 精读完成前仍禁止校准预测、个体建议和域主张升级。

域-来源精读完成寄存器见 [`human-infra-domain-source-specific-extraction-register.json`](human-infra-domain-source-specific-extraction-register.json)，由 `make domain-source-extraction-audit` 检查原始 81/93 个 domain-source 精读字段行是否已经绑定到 exact claim、endpoint、population、uncertainty、transfer-boundary 和模型准入阻塞语义，并保留 12 个奇点域 source-specific 深读任务待完成。当前已完成方法锚点、生物机制、价值框架、认知扩展、脑保存、数字孪生、未来等待、AI 治理和筛查偏倚边界的字段级抽取；这些行仍必须经过外部文献 fresh review、变量卡晋升和模型校准门禁，才能进入更高等级证据。

域-来源卡片晋升队列见 [`human-infra-domain-source-card-promotion-queue.json`](human-infra-domain-source-card-promotion-queue.json)，由 `make domain-source-promotion-audit` 检查 81 个完成字段行是否一一派生为 source-context fresh review、Source Card、变量卡、endpoint 卡、uncertainty 卡、transfer-boundary 卡和 downgrade check 任务。该队列只是下一步执行队列，不证明任何晋升任务已经完成，也不打开校准预测、个体建议或干预排序。

来源语境本地复核账本见 [`human-infra-source-context-local-review-register.json`](human-infra-source-context-local-review-register.json)，由 `make source-context-local-review-audit` 检查当前 20 个来源锚点是否反查到原始 81 个晋升任务、26 个已完成 source-specific 域、来源证据、阻塞用途和索引入口。该账本只是本地 source-context 复核，不等于独立 fresh review、Source Card 晋升完成或模型准入。

卡片晋升预注册账本见 [`human-infra-card-promotion-prep-register.json`](human-infra-card-promotion-prep-register.json)，由 `make card-promotion-prep-audit` 检查当前 81 个本地复核晋升任务是否已经预分配 486 个 Source/变量/endpoint/uncertainty/transfer/downgrade 待产物 ID、评审问题、阻塞用途和索引入口。该账本只是卡片晋升执行前的准备包，不等于独立 fresh review 或卡片完成。

独立 fresh review 协议见 [`human-infra-independent-fresh-review-protocol.json`](human-infra-independent-fresh-review-protocol.json)，由 `make independent-fresh-review-protocol-audit` 检查 81 个准备包如何按四个批次进入独立审查。该协议只定义审查批次、字段和晋升规则，不保存任何 fresh review verdict。

独立 fresh review verdict 账本见 [`human-infra-independent-fresh-review-verdict-register.json`](human-infra-independent-fresh-review-verdict-register.json)，由 `make independent-fresh-review-verdict-audit` 检查 FRB-01 到 FRB-04 的 20 个来源锚点、81 个准备包是否全部完成独立 fresh review verdict，并确认这些 verdict 只允许 bounded artifact filling，不打开校准预测、个体建议、个体死亡日期、干预排序、域主张升级或临床有效性声明。

Reviewed card artifact 账本见 [`human-infra-reviewed-card-artifact-register.json`](human-infra-reviewed-card-artifact-register.json)，由 `make reviewed-card-artifact-audit` 检查 81 个已审查晋升包是否落成 486 个 reviewed Source/variable/endpoint/uncertainty/transfer-boundary/downgrade artifact 实体，并确认它们仍不打开模型准入、个体建议、个体死亡日期、干预排序、域主张升级或临床有效性声明。

Future-boundary route card 账本见 [`human-infra-future-boundary-route-card-register.json`](human-infra-future-boundary-route-card-register.json)，由 `make future-boundary-route-card-audit` 检查未来等待、生物停滞、神经身份连续性和 AI 加速四条高优先路线是否统一暴露技术窗口、接入、采用、持续期、可组合性、尾部风险和机会成本门，并确认路线可行性、校准预测和个体用途仍被阻塞。

C2 长尾覆盖账本见 [`human-infra-c2-longtail-coverage-register.json`](human-infra-c2-longtail-coverage-register.json)，由 `make c2-longtail-coverage-audit` 检查 `classification.tsv` 中全部 204 个 C2 源体维护域是否进入覆盖账本，并明确当前 20 个 priority reviewed-artifact covered 域与 184 个仍缺 Claim-Evidence/source/fresh-review/card artifact 的长尾域。

C2 长尾第一批晋升队列见 [`human-infra-c2-longtail-first-batch-promotion-queue.json`](human-infra-c2-longtail-first-batch-promotion-queue.json)，由 `make c2-longtail-first-batch-promotion-audit` 检查 24 个高影响未覆盖 C2 域是否绑定覆盖账本、候选来源、claim seed、variable seed、晋升步骤和禁止用途边界。该队列只是执行入口，不证明 Source Card、fresh review、变量卡、endpoint 卡、downgrade check 或模型准入已经完成。

C2 长尾第一批来源深读队列见 [`human-infra-c2-longtail-first-batch-source-extraction-queue.json`](human-infra-c2-longtail-first-batch-source-extraction-queue.json)，由 `make c2-longtail-first-batch-source-extraction-audit` 检查 C2-LT-B1 是否已经派生为 48 个 domain-source 深读任务，并要求后续逐源抽取 exact claim、endpoint、population/setting、mechanism/effect、uncertainty、transfer boundary、downgrade trigger 和 model position。该队列不证明来源已读完，不打开模型准入。

C2 长尾第一批来源抽取试运行见 [`human-infra-c2-longtail-first-batch-source-extraction-register.json`](human-infra-c2-longtail-first-batch-source-extraction-register.json)，由 `make c2-longtail-first-batch-source-extraction-register-audit` 检查 48/48 个来源是否已经进入字段级抽取。当前覆盖第一批 24 个高影响 C2 长尾域；它不等于 fresh review、Source Card 晋升或模型准入完成。

C2 长尾第一批本地来源语境复核见 [`human-infra-c2-longtail-first-batch-local-review-register.json`](human-infra-c2-longtail-first-batch-local-review-register.json)，由 `make c2-longtail-first-batch-local-review-audit` 检查 48/48 个来源抽取行是否完成本地结构复核、反查队列与抽取账本、保持禁止用途，并且只允许进入 independent fresh review。它不等于 reviewed artifacts、Source Card 晋升或模型准入完成。

C2 长尾第一批独立 fresh review 协议见 [`human-infra-c2-longtail-first-batch-independent-fresh-review-protocol.json`](human-infra-c2-longtail-first-batch-independent-fresh-review-protocol.json)，由 `make c2-longtail-first-batch-independent-fresh-review-protocol-audit` 检查 48 个本地复核行是否拆成 4 个 fresh-review 批次，并把 verdict 字段、降级动作和禁止用途写入协议。

C2 长尾第一批独立 fresh review 判定见 [`human-infra-c2-longtail-first-batch-independent-fresh-review-verdict-register.json`](human-infra-c2-longtail-first-batch-independent-fresh-review-verdict-register.json)，由 `make c2-longtail-first-batch-independent-fresh-review-verdict-audit` 检查当前 48/48 个来源是否已有外部核验证据、reviewer verdict、artifact promotion decision 和阻塞边界。该账本当前已经完成四批 verdict 收口；下一步只允许把 eligible rows 晋升为 reviewed artifacts，仍不打开模型准入。

C2 长尾第一批 reviewed artifact 账本见 [`human-infra-c2-longtail-first-batch-reviewed-card-artifact-register.json`](human-infra-c2-longtail-first-batch-reviewed-card-artifact-register.json)，由 `make c2-longtail-first-batch-reviewed-card-artifact-audit` 检查 42 个 eligible verdict rows 是否晋升为 252 个 reviewed Source/variable/endpoint/uncertainty/transfer-boundary/downgrade artifact，并确认 5 个 downgrade-before-fill 与 1 个 cannot-evaluate 行仍保持 blocked。该账本仍不打开模型准入，也不代表剩余 184 个 C2 长尾域闭合。

C2 长尾第一批 blocked source resolution 账本见 [`human-infra-c2-longtail-first-batch-blocked-source-resolution-register.json`](human-infra-c2-longtail-first-batch-blocked-source-resolution-register.json)，由 `make c2-longtail-first-batch-blocked-source-resolution-audit` 检查 6 个非 eligible rows 是否已经准备来源校正、时效核验和替代候选。该账本只解除下一轮重审的输入阻塞；它不改变原 verdict，不创建 reviewed artifacts，也不打开模型准入。

C2 长尾第一批 source-resolution fresh review 判定账本见 [`human-infra-c2-longtail-first-batch-source-resolution-fresh-review-verdict-register.json`](human-infra-c2-longtail-first-batch-source-resolution-fresh-review-verdict-register.json)，由 `make c2-longtail-first-batch-source-resolution-fresh-review-verdict-audit` 检查 6 个非 eligible rows 的来源纠偏候选是否已经完成 fresh review、16 个候选是否都有用途判定、哪些行只能 route/split，以及所有行是否仍禁止 direct artifact fill 和模型准入。该账本只允许 corrected source re-extraction，不创建 reviewed artifacts。

C2 长尾第一批 corrected source re-extraction 队列见 [`human-infra-c2-longtail-first-batch-corrected-source-reextraction-queue.json`](human-infra-c2-longtail-first-batch-corrected-source-reextraction-queue.json)，由 `make c2-longtail-first-batch-corrected-source-reextraction-queue-audit` 检查 6 个来源纠偏行中的 10 个 selected corrected candidates 是否被派生成重新抽取任务，并确认 6 个 route-only/context 候选只保留为拆分边界。该队列仍不等于 corrected extraction 完成、reviewed artifact 晋升或模型准入。

C2 长尾第一批 corrected source re-extraction 完成寄存器见 [`human-infra-c2-longtail-first-batch-corrected-source-reextraction-register.json`](human-infra-c2-longtail-first-batch-corrected-source-reextraction-register.json)，由 `make c2-longtail-first-batch-corrected-source-reextraction-register-audit` 检查 10/10 个 corrected candidates 是否已经完成 bounded source re-extraction，并确认 6 行只可进入下一轮 independent fresh review 候选、4 行仍保持 route/index/fulltext 阻塞。该寄存器仍不等于 fresh review 通过、reviewed artifact 晋升或模型准入。

C2 长尾第一批 corrected source fresh review 判定账本见 [`human-infra-c2-longtail-first-batch-corrected-source-fresh-review-verdict-register.json`](human-infra-c2-longtail-first-batch-corrected-source-fresh-review-verdict-register.json)，由 `make c2-longtail-first-batch-corrected-source-fresh-review-verdict-audit` 检查 10/10 个 corrected extraction outputs 是否已完成 independent fresh review、5 行是否只允许进入 bounded reviewed artifact prep、5 行是否继续保持 lineage/route/index/fulltext 阻塞。该账本仍不等于 reviewed artifact 已创建或模型准入。

C2 长尾第一批 corrected source reviewed artifact 账本见 [`human-infra-c2-longtail-first-batch-corrected-source-reviewed-card-artifact-register.json`](human-infra-c2-longtail-first-batch-corrected-source-reviewed-card-artifact-register.json)，由 `make c2-longtail-first-batch-corrected-source-reviewed-card-artifact-audit` 检查 5 个 eligible corrected rows 是否晋升为 30 个 bounded reviewed artifacts、5 个 blocked rows 是否仍保持 lineage/route/index/fulltext 边界。该账本仍不打开模型准入，也不代表剩余 184 个 C2 长尾域闭合。

C2 长尾第二批晋升队列见 [`human-infra-c2-longtail-second-batch-promotion-queue.json`](human-infra-c2-longtail-second-batch-promotion-queue.json)，由 `make c2-longtail-second-batch-promotion-audit` 检查 12 个非 B1 的剩余 C2 长尾域是否已绑定 24 个 web-checked 候选来源、晋升步骤和模型阻塞边界。该队列只扩展下一轮 source-specific 深读入口，不等于 Source Card、fresh review、reviewed artifact 或模型准入。

C2 长尾第二批来源深读队列见 [`human-infra-c2-longtail-second-batch-source-extraction-queue.json`](human-infra-c2-longtail-second-batch-source-extraction-queue.json)，由 `make c2-longtail-second-batch-source-extraction-audit` 检查 24 个第二批 domain-source 任务是否具备 exact claim、endpoint、population/setting、mechanism/effect、uncertainty、transfer boundary、downgrade trigger 和 model position 抽取槽位。该队列不证明来源已读完，不打开 fresh review、reviewed artifact 或模型准入。

C2 长尾第二批来源抽取寄存器见 [`human-infra-c2-longtail-second-batch-source-extraction-register.json`](human-infra-c2-longtail-second-batch-source-extraction-register.json)，由 `make c2-longtail-second-batch-source-extraction-register-audit` 检查 24/24 个第二批来源是否已经完成本地字段级抽取，并确认它们只可进入本地来源语境复核。该寄存器不等于 independent fresh review、reviewed artifact 或模型准入完成。

C2 长尾第二批本地来源语境复核见 [`human-infra-c2-longtail-second-batch-local-review-register.json`](human-infra-c2-longtail-second-batch-local-review-register.json)，由 `make c2-longtail-second-batch-local-review-audit` 检查 24/24 个第二批抽取行是否完成本地结构复核、反查队列与抽取寄存器、保持禁止用途，并且只允许进入 independent fresh review。它不等于 reviewed artifacts、Source Card 晋升或模型准入完成。

C2 长尾第二批 independent fresh review 协议见 [`human-infra-c2-longtail-second-batch-independent-fresh-review-protocol.json`](human-infra-c2-longtail-second-batch-independent-fresh-review-protocol.json)，由 `make c2-longtail-second-batch-independent-fresh-review-protocol-audit` 检查 24 个本地复核行是否拆成 2 个 fresh-review 批次，并把 required verdict fields、verdict taxonomy、artifact promotion decisions 和 blocked uses 写入协议。该协议不存放 reviewer verdict，不创建 reviewed artifacts，也不打开模型准入。

C2 长尾第二批 independent fresh review 判定见 [`human-infra-c2-longtail-second-batch-independent-fresh-review-verdict-register.json`](human-infra-c2-longtail-second-batch-independent-fresh-review-verdict-register.json)，由 `make c2-longtail-second-batch-independent-fresh-review-verdict-audit` 检查 24/24 个来源是否已有 fresh-review evidence、reviewer verdict、artifact promotion decision 和阻塞边界。当前 18 行 support-with-boundary、5 行 bounded-support、1 行 downgrade-required；下一步只允许 23 个 eligible rows 晋升为 bounded reviewed artifacts，仍不打开模型准入。

C2 长尾第二批 reviewed artifact 账本见 [`human-infra-c2-longtail-second-batch-reviewed-card-artifact-register.json`](human-infra-c2-longtail-second-batch-reviewed-card-artifact-register.json)，由 `make c2-longtail-second-batch-reviewed-card-artifact-audit` 检查 23 个 eligible verdict rows 是否晋升为 138 个 reviewed Source/variable/endpoint/uncertainty/transfer-boundary/downgrade artifacts，并确认 1 个 downgrade-before-fill row 仍保持 blocked。该账本仍不打开模型准入，也不代表剩余 C2 长尾域闭合。

C2 长尾第三批晋升队列见 [`human-infra-c2-longtail-third-batch-promotion-queue.json`](human-infra-c2-longtail-third-batch-promotion-queue.json)，由 `make c2-longtail-third-batch-promotion-audit` 检查 12 个非 B1/B2 的神经-感知-认知连续性域是否已绑定 24 个 web-checked 候选来源、晋升步骤和模型阻塞边界。该队列只扩展下一轮 source-specific 深读入口，不等于 Source Card、fresh review、reviewed artifact 或模型准入。

C2 长尾第三批来源深读队列见 [`human-infra-c2-longtail-third-batch-source-extraction-queue.json`](human-infra-c2-longtail-third-batch-source-extraction-queue.json)，由 `make c2-longtail-third-batch-source-extraction-audit` 检查 24 个第三批 domain-source 任务是否具备 exact claim、endpoint、population/setting、mechanism/effect、uncertainty、transfer boundary、downgrade trigger 和 model position 抽取槽位。该队列不证明来源已读完，不打开 fresh review、reviewed artifact 或模型准入。

C2 长尾第三批来源抽取寄存器见 [`human-infra-c2-longtail-third-batch-source-extraction-register.json`](human-infra-c2-longtail-third-batch-source-extraction-register.json)，由 `make c2-longtail-third-batch-source-extraction-register-audit` 检查 24/24 个第三批来源是否已经完成本地字段级来源语境抽取，并确认错源、标题/分卷错配、访问受限、降级触发和模型阻塞边界被保留。该寄存器不等于本地复核、independent fresh review、reviewed artifacts 或模型准入完成。

C2 长尾第三批本地来源语境复核见 [`human-infra-c2-longtail-third-batch-local-review-register.json`](human-infra-c2-longtail-third-batch-local-review-register.json)，由 `make c2-longtail-third-batch-local-review-audit` 检查 24/24 个第三批来源抽取行是否完成本地结构复核、反查队列与抽取寄存器、保持禁止用途，并保留 5 个错源/错配/访问受限问题行。该账本只允许进入 independent fresh review 或 source-resolution，不等于 reviewed artifacts、Source Card 晋升或模型准入完成。

C2 长尾第三批 source-resolution 账本见 [`human-infra-c2-longtail-third-batch-source-resolution-register.json`](human-infra-c2-longtail-third-batch-source-resolution-register.json)，由 `make c2-longtail-third-batch-source-resolution-audit` 检查 5 个本地复核问题行是否已准备 7 个 corrected、split 或 route-normalized 候选，并确认它们仍必须进入 independent fresh review、corrected re-extraction 和 reviewed artifact 门禁。该账本不创建 reviewed artifacts，也不打开模型准入。

C2 长尾第三批 independent fresh review 协议见 [`human-infra-c2-longtail-third-batch-independent-fresh-review-protocol.json`](human-infra-c2-longtail-third-batch-independent-fresh-review-protocol.json)，由 `make c2-longtail-third-batch-independent-fresh-review-protocol-audit` 检查 24 个本地复核行是否拆成 2 个 fresh-review 批次，并把 5 个 source-resolution issue rows 纳入纠偏来源检查。该协议不存放 reviewer verdict，不创建 reviewed artifacts，也不打开模型准入。

C2 长尾第三批 independent fresh review 判定见 [`human-infra-c2-longtail-third-batch-independent-fresh-review-verdict-register.json`](human-infra-c2-longtail-third-batch-independent-fresh-review-verdict-register.json)，由 `make c2-longtail-third-batch-independent-fresh-review-verdict-audit` 检查 24/24 个第三批来源是否已有 reviewer verdict、fresh-review evidence、artifact promotion decision、source-resolution routing 和阻塞边界。当前 18 行只允许 bounded artifact fill，5 行只允许 corrected-source re-extraction，1 行必须 downgrade-before-fill；该账本仍不创建 reviewed artifacts，也不打开模型准入。

C2 长尾第三批 corrected source re-extraction 队列见 [`human-infra-c2-longtail-third-batch-corrected-source-reextraction-queue.json`](human-infra-c2-longtail-third-batch-corrected-source-reextraction-queue.json)，由 `make c2-longtail-third-batch-corrected-source-reextraction-queue-audit` 检查 5 个 source-resolution-supported 问题行中的 7 个 corrected/split/route-normalized 候选是否被派生成 source-specific re-extraction 任务。该队列仍不等于 corrected extraction 完成、reviewed artifact 晋升或模型准入。

C2 长尾第三批 corrected source re-extraction 完成寄存器见 [`human-infra-c2-longtail-third-batch-corrected-source-reextraction-register.json`](human-infra-c2-longtail-third-batch-corrected-source-reextraction-register.json)，由 `make c2-longtail-third-batch-corrected-source-reextraction-register-audit` 检查 7/7 个 corrected candidates 是否已经完成 bounded source re-extraction，并确认 5 行只可进入下一轮 independent fresh review 候选、2 行仍保持 route/split 阻塞。该寄存器仍不等于 fresh review 通过、reviewed artifact 晋升或模型准入。

C2 长尾第三批 corrected source fresh review 判定账本见 [`human-infra-c2-longtail-third-batch-corrected-source-fresh-review-verdict-register.json`](human-infra-c2-longtail-third-batch-corrected-source-fresh-review-verdict-register.json)，由 `make c2-longtail-third-batch-corrected-source-fresh-review-verdict-audit` 检查 7/7 个 corrected extraction outputs 是否已完成 independent fresh review、6 行是否只允许进入 bounded reviewed artifact prep、1 行是否继续保持 duplicate/split route 阻塞，并确认 AAO-HNS publisher route 可读事实只进入有界 artifact 准备。该账本仍不等于模型准入。

C2 长尾第三批 reviewed artifact 账本见 [`human-infra-c2-longtail-third-batch-reviewed-card-artifact-register.json`](human-infra-c2-longtail-third-batch-reviewed-card-artifact-register.json)，由 `make c2-longtail-third-batch-reviewed-card-artifact-audit` 检查 18 个原始 eligible 行和 6 个 corrected eligible 行是否生成 144 个 bounded reviewed artifacts，并确认 EXT-022 downgrade-before-fill 与 C2LTB3-CREXT-004 duplicate/split route blocked row 被显式保留。该账本仍不等于剩余 C2 长尾域闭合或模型准入。

C2 长尾第十三批 corrected source re-extraction 队列见 [`human-infra-c2-longtail-thirteenth-batch-corrected-source-reextraction-queue.json`](human-infra-c2-longtail-thirteenth-batch-corrected-source-reextraction-queue.json)，由 `make c2-longtail-thirteenth-batch-corrected-source-reextraction-queue-audit` 检查 C2LTB13-EXT-021 是否把错配 PMID 26428404 保持阻塞，并把 corrected IAD review PMID 22193141 派生成唯一重新抽取任务。该队列仍不等于重新抽取完成、fresh review、reviewed artifact 或模型准入。

C2 长尾第十三批 corrected source re-extraction 完成寄存器见 [`human-infra-c2-longtail-thirteenth-batch-corrected-source-reextraction-register.json`](human-infra-c2-longtail-thirteenth-batch-corrected-source-reextraction-register.json)，由 `make c2-longtail-thirteenth-batch-corrected-source-reextraction-register-audit` 检查 C2LTB13-CREXT-001 是否已经完成 bounded IAD source-context re-extraction，并确认它只可进入下一轮 independent fresh review 候选。该寄存器仍不等于 fresh review 通过、reviewed artifact 晋升、临床建议或模型准入。

C2 长尾第十三批 corrected source fresh review 判定见 [`human-infra-c2-longtail-thirteenth-batch-corrected-source-fresh-review-verdict-register.json`](human-infra-c2-longtail-thirteenth-batch-corrected-source-fresh-review-verdict-register.json)，由 `make c2-longtail-thirteenth-batch-corrected-source-fresh-review-verdict-audit` 检查 corrected IAD PMID 22193141 是否只被判定为 bounded artifact-prep eligible，并继续阻塞临床、产品、护理建议、校准模型和个体用途。该判定仍不等于 reviewed artifact 已创建或模型准入。

C2 长尾第四批晋升队列见 [`human-infra-c2-longtail-fourth-batch-promotion-queue.json`](human-infra-c2-longtail-fourth-batch-promotion-queue.json)，由 `make c2-longtail-fourth-batch-promotion-audit` 检查 12 个非 B1/B2/B3 的代谢、内分泌、肾肝、电解质和携氧稳态连续性域是否已绑定 24 个 web-checked 候选来源、晋升步骤和模型阻塞边界。该队列只扩展下一轮 source-specific 深读入口，不等于 Source Card、fresh review、reviewed artifact 或模型准入。

C2 长尾第四批来源深读队列见 [`human-infra-c2-longtail-fourth-batch-source-extraction-queue.json`](human-infra-c2-longtail-fourth-batch-source-extraction-queue.json)，由 `make c2-longtail-fourth-batch-source-extraction-audit` 检查 24 个第四批 domain-source 任务是否具备 exact claim、endpoint、population/setting、mechanism/effect、uncertainty、transfer boundary、downgrade trigger 和 model position 抽取槽位。该队列不证明来源已读完，不打开 local review、fresh review、reviewed artifact 或模型准入。

C2 长尾第四批来源抽取寄存器见 [`human-infra-c2-longtail-fourth-batch-source-extraction-register.json`](human-infra-c2-longtail-fourth-batch-source-extraction-register.json)，由 `make c2-longtail-fourth-batch-source-extraction-register-audit` 检查 24/24 个第四批来源是否已经完成本地字段级来源语境抽取，并确认无摘要全文复核、重复共识路线、降级触发和模型阻塞边界被保留。该寄存器不等于本地复核、independent fresh review、reviewed artifacts 或模型准入完成。

C2 长尾第四批本地来源语境复核见 [`human-infra-c2-longtail-fourth-batch-local-review-register.json`](human-infra-c2-longtail-fourth-batch-local-review-register.json)，由 `make c2-longtail-fourth-batch-local-review-audit` 检查 24/24 个第四批来源抽取行是否完成本地结构复核、是否反查队列与抽取账本、是否保留 1 个重复共识路线行和 3 个无摘要需全文行，以及是否继续阻塞 reviewed artifacts、Source Card 晋升和模型准入。该账本只打开 independent fresh review / source-resolution 的下一步路由，不等于 fresh review 判定或 artifact 晋升完成。

C2 长尾第四批 source-resolution 账本见 [`human-infra-c2-longtail-fourth-batch-source-resolution-register.json`](human-infra-c2-longtail-fourth-batch-source-resolution-register.json)，由 `make c2-longtail-fourth-batch-source-resolution-audit` 检查 4 个第四批问题行是否已经准备 8 个重复路线、官方指南页、DOI 或全文路线候选，并确认所有候选继续阻塞 fresh review、manual fulltext extraction、reviewed artifacts 和模型准入。该账本不等于全文复核完成，不等于 fresh-review verdict，也不打开 artifact 晋升。

C2 长尾第四批 manual/fulltext extraction 账本见 [`human-infra-c2-longtail-fourth-batch-manual-fulltext-extraction-register.json`](human-infra-c2-longtail-fourth-batch-manual-fulltext-extraction-register.json)，由 `make c2-longtail-fourth-batch-manual-fulltext-extraction-audit` 检查 8 个 source-resolution 候选是否已完成有界全文/官方页路线抽取，并确认 3 个 bounded fresh-review 候选与 5 个 duplicate、route-only 或 manual-access 阻塞行被分开保留。该账本不是 independent fresh-review verdict，不创建 reviewed artifacts，也不打开模型准入。

C2 长尾第四批 manual/fulltext fresh review 判定账本见 [`human-infra-c2-longtail-fourth-batch-manual-fulltext-fresh-review-verdict-register.json`](human-infra-c2-longtail-fourth-batch-manual-fulltext-fresh-review-verdict-register.json)，由 `make c2-longtail-fourth-batch-manual-fulltext-fresh-review-verdict-audit` 检查 8/8 个 manual/fulltext extraction 行是否完成 independent fresh review、3 行是否只允许进入 bounded reviewed artifact prep、5 行是否继续保持 duplicate、route-only、manual-access 或 context-only 阻塞。该账本仍不创建 reviewed artifacts，也不打开模型准入。

C2 长尾第四批 manual/fulltext reviewed artifact 账本见 [`human-infra-c2-longtail-fourth-batch-manual-fulltext-reviewed-card-artifact-register.json`](human-infra-c2-longtail-fourth-batch-manual-fulltext-reviewed-card-artifact-register.json)，由 `make c2-longtail-fourth-batch-manual-fulltext-reviewed-card-artifact-audit` 检查 3 个 eligible manual/fulltext fresh-review rows 是否生成 18 个 bounded reviewed artifacts，并确认 5 个 duplicate、route-only、manual-access 或 context-only blockedRows 被显式保留。该账本只完成有界研究卡片晋升，不等于校准模型准入、个体建议、干预排序、临床有效性主张或死亡日期输出。

C2 长尾第五批晋升队列见 [`human-infra-c2-longtail-fifth-batch-promotion-queue.json`](human-infra-c2-longtail-fifth-batch-promotion-queue.json)，由 `make c2-longtail-fifth-batch-promotion-audit` 检查 12 个第五批细胞质量控制、细胞器通信、分子运输、膜脂韧性、清除和屏障底座 C2 长尾域是否已绑定 24 个 web/API-checked 候选来源、晋升步骤和模型阻塞边界。第五批来源深读队列见 [`human-infra-c2-longtail-fifth-batch-source-extraction-queue.json`](human-infra-c2-longtail-fifth-batch-source-extraction-queue.json)，由 `make c2-longtail-fifth-batch-source-extraction-audit` 检查 24 个候选来源是否已派生成 exact claim、endpoint、population、uncertainty、transfer-boundary、downgrade 和 model-position 抽取任务。第五批来源抽取寄存器见 [`human-infra-c2-longtail-fifth-batch-source-extraction-register.json`](human-infra-c2-longtail-fifth-batch-source-extraction-register.json)，由 `make c2-longtail-fifth-batch-source-extraction-register-audit` 检查 24/24 个来源语境字段抽取是否完成，并确认无开放全文、跨域复用来源、模型生物/综述边界和模型准入阻塞仍被显式保留。第五批本地来源语境复核见 [`human-infra-c2-longtail-fifth-batch-local-review-register.json`](human-infra-c2-longtail-fifth-batch-local-review-register.json)，由 `make c2-longtail-fifth-batch-local-review-audit` 检查 24/24 个抽取行是否完成本地结构复核，并确认 8 个无开放全文或跨域复用问题行仍需 source-resolution/manual fulltext 后才能进入 bounded fresh review。第五批 source-resolution 账本见 [`human-infra-c2-longtail-fifth-batch-source-resolution-register.json`](human-infra-c2-longtail-fifth-batch-source-resolution-register.json)，由 `make c2-longtail-fifth-batch-source-resolution-audit` 检查 8 个问题行是否整理为 14 个 PubMed、Europe PMC、DOI 或 PMC route 候选，并确认 manual/fulltext extraction、fresh review、reviewed artifacts 和模型准入仍被阻塞。第五批 manual/fulltext extraction 账本见 [`human-infra-c2-longtail-fifth-batch-manual-fulltext-extraction-register.json`](human-infra-c2-longtail-fifth-batch-manual-fulltext-extraction-register.json)，由 `make c2-longtail-fifth-batch-manual-fulltext-extraction-audit` 检查 14 个候选是否已完成有界路线/全文上下文抽取，并确认只有 2 个 PMC 主路线进入 bounded fresh-review 候选、12 个 route-only/manual-access/duplicate 行继续阻塞。第五批 independent fresh review 判定账本见 [`human-infra-c2-longtail-fifth-batch-independent-fresh-review-verdict-register.json`](human-infra-c2-longtail-fifth-batch-independent-fresh-review-verdict-register.json)，由 `make c2-longtail-fifth-batch-independent-fresh-review-verdict-audit` 检查 16 个非问题来源抽取行和 14 个 manual/fulltext 行是否已完成 independent fresh review、17 行是否只允许进入 bounded reviewed artifact prep、13 个 manual route-only、manual-access、duplicate 或 context-only 行是否继续阻塞，并确认模型准入仍为 0。第五批 reviewed artifact 账本见 [`human-infra-c2-longtail-fifth-batch-reviewed-card-artifact-register.json`](human-infra-c2-longtail-fifth-batch-reviewed-card-artifact-register.json)，由 `make c2-longtail-fifth-batch-reviewed-card-artifact-audit` 检查 17 个 eligible fresh-review rows 是否生成 102 个有界 reviewed artifacts、13 个 blocked manual rows 是否显式保留，并确认模型准入仍阻塞。

C2 长尾第六批晋升队列见 [`human-infra-c2-longtail-sixth-batch-promotion-queue.json`](human-infra-c2-longtail-sixth-batch-promotion-queue.json)，由 `make c2-longtail-sixth-batch-promotion-audit` 检查 12 个第六批跨代连续性、生殖力、孕产新生儿、儿童免疫、儿童铅暴露、儿童喂养吞咽、哺乳和儿童口腔健康 C2 长尾域是否已绑定 24 个 web-checked 候选来源、晋升步骤和模型阻塞边界。第六批来源深读队列见 [`human-infra-c2-longtail-sixth-batch-source-extraction-queue.json`](human-infra-c2-longtail-sixth-batch-source-extraction-queue.json)，由 `make c2-longtail-sixth-batch-source-extraction-audit` 检查 24 个候选来源是否已派生成 exact claim、endpoint、population、uncertainty、transfer-boundary、downgrade 和 model-position 抽取任务。第六批来源抽取寄存器见 [`human-infra-c2-longtail-sixth-batch-source-extraction-register.json`](human-infra-c2-longtail-sixth-batch-source-extraction-register.json)，由 `make c2-longtail-sixth-batch-source-extraction-register-audit` 检查 24/24 个来源语境字段抽取是否完成，并确认 guideline route、publisher/manual review、source-lineage、降级触发和模型准入阻塞仍被显式保留。第六批本地来源语境复核见 [`human-infra-c2-longtail-sixth-batch-local-review-register.json`](human-infra-c2-longtail-sixth-batch-local-review-register.json)，由 `make c2-longtail-sixth-batch-local-review-audit` 检查 24/24 个抽取行是否完成本地结构复核，并确认 7 个 guideline route、publisher/manual review 或 source-lineage 问题行仍需 source-resolution/manual fulltext 后才能进入 bounded fresh review。第六批 source-resolution 账本见 [`human-infra-c2-longtail-sixth-batch-source-resolution-register.json`](human-infra-c2-longtail-sixth-batch-source-resolution-register.json)，由 `make c2-longtail-sixth-batch-source-resolution-audit` 检查 7 个问题行是否整理为 19 个官方页、PubMed/PMC、OUP/LWW/AAP 或 CDC 路线候选，并确认它只准备 manual/fulltext extraction 与 independent fresh review，不完成 reviewed artifacts 或模型准入。第六批 manual/fulltext extraction 账本见 [`human-infra-c2-longtail-sixth-batch-manual-fulltext-extraction-register.json`](human-infra-c2-longtail-sixth-batch-manual-fulltext-extraction-register.json)，由 `make c2-longtail-sixth-batch-manual-fulltext-extraction-audit` 检查 19 个候选是否已完成有界路线/全文上下文抽取，并确认只有 7 行进入 bounded fresh-review 候选、12 行继续 route-only、bibliographic、summary、companion-lineage 或 policy-resource context 阻塞。第六批 independent fresh review 判定账本见 [`human-infra-c2-longtail-sixth-batch-independent-fresh-review-verdict-register.json`](human-infra-c2-longtail-sixth-batch-independent-fresh-review-verdict-register.json)，由 `make c2-longtail-sixth-batch-independent-fresh-review-verdict-audit` 检查 17 个非问题来源抽取行和 19 个 manual/fulltext 行是否已完成独立复核、24 行是否只允许进入 bounded reviewed artifact prep、12 个 manual route-only、bibliographic、summary、companion-lineage 或 policy-resource context 行是否继续阻塞。第六批 reviewed artifact 账本见 [`human-infra-c2-longtail-sixth-batch-reviewed-card-artifact-register.json`](human-infra-c2-longtail-sixth-batch-reviewed-card-artifact-register.json)，由 `make c2-longtail-sixth-batch-reviewed-card-artifact-audit` 检查 24 个 eligible fresh-review rows 是否生成 144 个有界 reviewed artifacts、12 个 manual blocked/context rows 是否显式保留，并确认模型准入仍阻塞。

C2 长尾第七批晋升队列见 [`human-infra-c2-longtail-seventh-batch-promotion-queue.json`](human-infra-c2-longtail-seventh-batch-promotion-queue.json)，由 `make c2-longtail-seventh-batch-promotion-audit` 检查 12 个第七批癌症控制、幸存者连续性、移植安全、器官捐献和工程器官替换 C2 长尾域是否已绑定 24 个 web-checked 候选来源、晋升步骤和模型阻塞边界。第七批来源深读队列见 [`human-infra-c2-longtail-seventh-batch-source-extraction-queue.json`](human-infra-c2-longtail-seventh-batch-source-extraction-queue.json)，由 `make c2-longtail-seventh-batch-source-extraction-audit` 检查 24 个候选来源是否已派生成 exact claim、endpoint、population、uncertainty、transfer-boundary、downgrade 和 model-position 抽取任务。第七批来源抽取寄存器见 [`human-infra-c2-longtail-seventh-batch-source-extraction-register.json`](human-infra-c2-longtail-seventh-batch-source-extraction-register.json)，由 `make c2-longtail-seventh-batch-source-extraction-register-audit` 检查 24/24 个来源语境字段抽取是否完成，并确认 FDA 404 路线、动态注册页、重复 CDC 来源、筛查边界、降级触发和模型准入阻塞仍被显式保留。第七批本地来源语境复核见 [`human-infra-c2-longtail-seventh-batch-local-review-register.json`](human-infra-c2-longtail-seventh-batch-local-review-register.json)，由 `make c2-longtail-seventh-batch-local-review-audit` 检查 24/24 个抽取行是否完成本地结构复核，并确认 6 个 FDA 404、Donate Life 动态注册或 CDC 重复来源问题行仍需 source-resolution/manual route 后才能进入 bounded fresh review。第七批 source-resolution 账本见 [`human-infra-c2-longtail-seventh-batch-source-resolution-register.json`](human-infra-c2-longtail-seventh-batch-source-resolution-register.json)，由 `make c2-longtail-seventh-batch-source-resolution-audit` 检查 6 个问题行是否整理为 7 个官方 FDA、CDC、Donate Life 或 RegisterMe 路线候选，并确认它只准备 manual/fulltext extraction 与 independent fresh review，不完成 reviewed artifacts 或模型准入。第七批 manual/fulltext extraction 账本见 [`human-infra-c2-longtail-seventh-batch-manual-fulltext-extraction-register.json`](human-infra-c2-longtail-seventh-batch-manual-fulltext-extraction-register.json)，由 `make c2-longtail-seventh-batch-manual-fulltext-extraction-audit` 检查 7 个候选是否已完成有界路线/全文上下文抽取，并确认只有 3 个官方 CDC/FDA 指南路线进入 bounded fresh-review 候选、4 个动态注册、访问受限、重复 CDC 或 FDA index 路线继续阻塞。第七批 manual/fulltext fresh review 判定账本见 [`human-infra-c2-longtail-seventh-batch-manual-fulltext-fresh-review-verdict-register.json`](human-infra-c2-longtail-seventh-batch-manual-fulltext-fresh-review-verdict-register.json)，由 `make c2-longtail-seventh-batch-manual-fulltext-fresh-review-verdict-audit` 检查 7/7 个 manual/fulltext 行是否完成独立复核、3 行是否只允许进入 bounded reviewed artifact prep、4 个 dynamic-registration/access-restricted/duplicate/index 行是否继续阻塞。第七批 manual/fulltext reviewed artifact 账本见 [`human-infra-c2-longtail-seventh-batch-manual-fulltext-reviewed-card-artifact-register.json`](human-infra-c2-longtail-seventh-batch-manual-fulltext-reviewed-card-artifact-register.json)，由 `make c2-longtail-seventh-batch-manual-fulltext-reviewed-card-artifact-audit` 检查 3 个 eligible rows 是否生成 18 个有界 reviewed artifacts、4 个 blocked rows 是否显式保留，并确认模型准入仍阻塞。该第七批链路仍不完成模型准入、临床建议或癌症筛查建议；新 artifacts 只进入 L1/L2-only 候选层。

C2 长尾第八批晋升队列见 [`human-infra-c2-longtail-eighth-batch-promotion-queue.json`](human-infra-c2-longtail-eighth-batch-promotion-queue.json)，由 `make c2-longtail-eighth-batch-promotion-audit` 检查 12 个第八批疼痛、创伤恢复、神经发育、感觉通信、自主神经、BCI 和活性算力 C2 长尾域是否已绑定 24 个 web-checked 候选来源、晋升步骤和模型阻塞边界。第八批来源深读队列见 [`human-infra-c2-longtail-eighth-batch-source-extraction-queue.json`](human-infra-c2-longtail-eighth-batch-source-extraction-queue.json)，由 `make c2-longtail-eighth-batch-source-extraction-audit` 检查 24 个候选来源是否已派生成 exact claim、endpoint、population、uncertainty、transfer-boundary、downgrade 和 model-position 抽取任务。第八批来源抽取寄存器见 [`human-infra-c2-longtail-eighth-batch-source-extraction-register.json`](human-infra-c2-longtail-eighth-batch-source-extraction-register.json)，由 `make c2-longtail-eighth-batch-source-extraction-register-audit` 检查 24/24 个来源语境字段抽取是否完成，并确认 PubMed/fulltext、practice portal、policy instrument、BCI 治理、活性算力外推边界、降级触发和模型准入阻塞仍被显式保留。第八批本地来源语境复核见 [`human-infra-c2-longtail-eighth-batch-local-review-register.json`](human-infra-c2-longtail-eighth-batch-local-review-register.json)，由 `make c2-longtail-eighth-batch-local-review-audit` 检查 24/24 个抽取行是否完成本地结构复核，并确认 7 个 PubMed/fulltext 或活性算力外推高风险问题行仍需 source-resolution/manual fulltext 后才能进入 bounded fresh review。第八批 source-resolution 账本见 [`human-infra-c2-longtail-eighth-batch-source-resolution-register.json`](human-infra-c2-longtail-eighth-batch-source-resolution-register.json)，由 `make c2-longtail-eighth-batch-source-resolution-audit` 检查 7 个问题行是否整理为 19 个 PubMed、PMC、DOI 或纠偏 PMID 候选，并确认 3 个原始 PMID 与标题错配行仍被显式保留。第八批 manual/fulltext extraction 账本见 [`human-infra-c2-longtail-eighth-batch-manual-fulltext-extraction-register.json`](human-infra-c2-longtail-eighth-batch-manual-fulltext-extraction-register.json)，由 `make c2-longtail-eighth-batch-manual-fulltext-extraction-audit` 检查 19 个候选是否已完成有界路线/全文上下文抽取，并确认只有 5 个 PMC 开放全文路线进入 bounded fresh-review 候选、14 个 PubMed、纠偏 PubMed、DOI 或 route-only 行继续阻塞。第八批 manual/fulltext fresh review 判定账本见 [`human-infra-c2-longtail-eighth-batch-manual-fulltext-fresh-review-verdict-register.json`](human-infra-c2-longtail-eighth-batch-manual-fulltext-fresh-review-verdict-register.json)，由 `make c2-longtail-eighth-batch-manual-fulltext-fresh-review-verdict-audit` 检查 19/19 个 manual/fulltext 行是否完成独立复核、5 个 PMC 可读全文行是否只允许进入 bounded reviewed artifact prep、14 个 route-only 或 publisher-route 行是否继续阻塞。第八批 manual/fulltext reviewed artifact 账本见 [`human-infra-c2-longtail-eighth-batch-manual-fulltext-reviewed-card-artifact-register.json`](human-infra-c2-longtail-eighth-batch-manual-fulltext-reviewed-card-artifact-register.json)，由 `make c2-longtail-eighth-batch-manual-fulltext-reviewed-card-artifact-audit` 检查 5 个 eligible rows 是否生成 30 个有界 reviewed artifacts、14 个 blocked rows 是否显式保留，并确认模型准入仍阻塞。该批次把活性算力放入 `synthetic-biological-intelligence-organoid-computing-continuity` 的候选来源审查，只允许提取 living neural computation、organoid intelligence、规模化/网络效应假设和伦理边界，不允许直接声称超越人类、临床可用或模型准入完成。

C2 长尾第九批晋升队列见 [`human-infra-c2-longtail-ninth-batch-promotion-queue.json`](human-infra-c2-longtail-ninth-batch-promotion-queue.json)，由 `make c2-longtail-ninth-batch-promotion-audit` 检查 12 个低背痛、肌肉力量/肌少症、骨折预防、慢性伤口、口腔健康、牙科可及、口干、哮喘/COPD 控制、家庭氧疗、免疫老化/疫苗反应和野火烟雾/清洁空气 C2 长尾域是否已绑定 24 个 web-checked 候选来源、晋升步骤和模型阻塞边界。第九批来源深读队列见 [`human-infra-c2-longtail-ninth-batch-source-extraction-queue.json`](human-infra-c2-longtail-ninth-batch-source-extraction-queue.json)，由 `make c2-longtail-ninth-batch-source-extraction-audit` 检查 24 个候选来源是否已派生成 exact claim、endpoint、population、uncertainty、transfer-boundary、downgrade 和 model-position 抽取任务。第九批来源抽取寄存器见 [`human-infra-c2-longtail-ninth-batch-source-extraction-register.json`](human-infra-c2-longtail-ninth-batch-source-extraction-register.json)，由 `make c2-longtail-ninth-batch-source-extraction-register-audit` 检查 24/24 个来源语境字段抽取是否完成，并确认 IDSA 525、Medicaid 403、GOLD 重定向、临床建议、牙科建议、康复建议、设备建议、疫苗建议、环境健康建议和模型准入阻塞仍被显式保留。第九批本地来源语境复核见 [`human-infra-c2-longtail-ninth-batch-local-review-register.json`](human-infra-c2-longtail-ninth-batch-local-review-register.json)，由 `make c2-longtail-ninth-batch-local-review-audit` 检查 24/24 个抽取行是否完成本地结构复核，并确认 IDSA 525 与 Medicaid 403 两个 manual-route 问题行仍需 source-resolution/manual-route 处理。第九批 source-resolution 账本见 [`human-infra-c2-longtail-ninth-batch-source-resolution-register.json`](human-infra-c2-longtail-ninth-batch-source-resolution-register.json)，由 `make c2-longtail-ninth-batch-source-resolution-audit` 检查 2 个问题行是否已整理为 8 个 IDSA、PubMed、DOI、Medicaid canonical、redirect provenance、官方 PDF 和 EPSDT 候选路线。第九批 manual/fulltext extraction 账本见 [`human-infra-c2-longtail-ninth-batch-manual-fulltext-extraction-register.json`](human-infra-c2-longtail-ninth-batch-manual-fulltext-extraction-register.json)，由 `make c2-longtail-ninth-batch-manual-fulltext-extraction-audit` 检查 8 个候选是否已完成有界路线/全文语境抽取，并确认只有 4 个官方页、官方 PDF 或相关政策路线进入 bounded fresh-review 候选、4 个 PubMed、DOI 或 redirect-provenance 行继续阻塞。第九批 manual/fulltext fresh review 判定见 [`human-infra-c2-longtail-ninth-batch-manual-fulltext-fresh-review-verdict-register.json`](human-infra-c2-longtail-ninth-batch-manual-fulltext-fresh-review-verdict-register.json)，由 `make c2-longtail-ninth-batch-manual-fulltext-fresh-review-verdict-audit` 检查 8/8 个 manual/fulltext 行是否完成 independent fresh review，确认 4 个官方页、官方 PDF 或相关政策行只可进入 bounded reviewed artifact prep，4 个 PubMed、DOI 或 redirect-provenance 行继续阻塞。第九批 manual/fulltext reviewed artifacts 见 [`human-infra-c2-longtail-ninth-batch-manual-fulltext-reviewed-card-artifact-register.json`](human-infra-c2-longtail-ninth-batch-manual-fulltext-reviewed-card-artifact-register.json)，由 `make c2-longtail-ninth-batch-manual-fulltext-reviewed-card-artifact-audit` 检查 4 个 eligible manual/fulltext fresh-review rows 是否晋升为 24 个 bounded Source/变量/endpoint/uncertainty/transfer/downgrade artifacts，并确认 4 个 blocked rows 和全部模型准入、临床/牙科/设备/疫苗/环境健康建议仍被阻塞。

C2 长尾第十批晋升队列见 [`human-infra-c2-longtail-tenth-batch-promotion-queue.json`](human-infra-c2-longtail-tenth-batch-promotion-queue.json)，由 `make c2-longtail-tenth-batch-promotion-audit` 检查 12 个设备感染、居家透析、外周神经病变、低视力康复、助听设备维护、手术伤口/SSI、温度稳态、烧伤、糖尿病视网膜病变、照护者健康、窒息和神经退行性吞咽障碍 C2 长尾域是否已绑定 24 个 web-checked 候选来源、晋升步骤和模型阻塞边界。第十批来源深读队列见 [`human-infra-c2-longtail-tenth-batch-source-extraction-queue.json`](human-infra-c2-longtail-tenth-batch-source-extraction-queue.json)，由 `make c2-longtail-tenth-batch-source-extraction-audit` 检查 24 个候选来源是否已派生成 exact claim、endpoint、population、uncertainty、transfer-boundary、downgrade 和 model-position 抽取任务。第十批来源抽取寄存器见 [`human-infra-c2-longtail-tenth-batch-source-extraction-register.json`](human-infra-c2-longtail-tenth-batch-source-extraction-register.json)，由 `make c2-longtail-tenth-batch-source-extraction-register-audit` 检查 24/24 个来源语境字段抽取是否完成，并确认临床/设备/透析/视听/康复/伤口/烧伤/急救/照护/营养/吞咽建议、reviewed artifacts 和模型准入阻塞仍被显式保留。第十批本地来源语境复核见 [`human-infra-c2-longtail-tenth-batch-local-review-register.json`](human-infra-c2-longtail-tenth-batch-local-review-register.json)，由 `make c2-longtail-tenth-batch-local-review-audit` 检查 24/24 个抽取行是否完成本地结构复核、0 个本地 source-resolution issue 是否被保持、以及全部行是否只进入 independent fresh review。第十批 independent fresh review 协议见 [`human-infra-c2-longtail-tenth-batch-independent-fresh-review-protocol.json`](human-infra-c2-longtail-tenth-batch-independent-fresh-review-protocol.json)，由 `make c2-longtail-tenth-batch-independent-fresh-review-protocol-audit` 检查 24 个本地复核行是否被拆成 2 个复核批次，并确认 review fields、verdict taxonomy、promotion decisions、B10 专属建议用途阻塞和模型准入边界已经定义。第十批 independent fresh review 判定见 [`human-infra-c2-longtail-tenth-batch-independent-fresh-review-verdict-register.json`](human-infra-c2-longtail-tenth-batch-independent-fresh-review-verdict-register.json)，由 `make c2-longtail-tenth-batch-independent-fresh-review-verdict-audit` 检查 24/24 个来源抽取行是否只允许进入 bounded reviewed artifact prep，并继续阻塞个体建议、干预排序和模型准入。第十批 reviewed artifacts 见 [`human-infra-c2-longtail-tenth-batch-reviewed-card-artifact-register.json`](human-infra-c2-longtail-tenth-batch-reviewed-card-artifact-register.json)，由 `make c2-longtail-tenth-batch-reviewed-card-artifact-audit` 检查 24 个 eligible fresh-review rows 是否晋升为 144 个 bounded Source/变量/endpoint/uncertainty/transfer/downgrade artifacts，并确认全部临床/设备/透析/视听/康复/伤口/烧伤/急救/照护/营养/吞咽建议和模型准入仍被阻塞。

C2 长尾第十一批晋升队列见 [`human-infra-c2-longtail-eleventh-batch-promotion-queue.json`](human-infra-c2-longtail-eleventh-batch-promotion-queue.json)，由 `make c2-longtail-eleventh-batch-promotion-audit` 检查 12 个吞咽/误吸、牙科感染、隐形眼镜相关角膜感染、糖尿病足卸载、眼外伤、听觉辅助、噪声性听损、儿童视觉筛查、嗅味觉、颞下颌/口面痛、双侧前庭功能低下和前庭耳毒性 C2 长尾域是否已绑定 24 个 web-checked 候选来源、晋升步骤和模型阻塞边界。第十一批来源深读队列见 [`human-infra-c2-longtail-eleventh-batch-source-extraction-queue.json`](human-infra-c2-longtail-eleventh-batch-source-extraction-queue.json)，由 `make c2-longtail-eleventh-batch-source-extraction-audit` 检查 24 个候选来源是否已派生成 exact claim、endpoint、population、uncertainty、transfer-boundary、downgrade 和 model-position 抽取任务。第十一批来源抽取寄存器见 [`human-infra-c2-longtail-eleventh-batch-source-extraction-register.json`](human-infra-c2-longtail-eleventh-batch-source-extraction-register.json)，由 `make c2-longtail-eleventh-batch-source-extraction-register-audit` 检查 24/24 个来源语境字段抽取是否完成，并确认临床/牙科/视听/前庭/吞咽/营养/感染/疼痛/行动建议、reviewed artifacts 和模型准入阻塞仍被显式保留。第十一批本地来源语境复核见 [`human-infra-c2-longtail-eleventh-batch-local-review-register.json`](human-infra-c2-longtail-eleventh-batch-local-review-register.json)，由 `make c2-longtail-eleventh-batch-local-review-audit` 检查 24/24 个抽取行是否完成本地结构复核、0 个本地 source-resolution issue 是否被保持、以及全部行是否只进入 independent fresh review。第十一批 independent fresh review 协议见 [`human-infra-c2-longtail-eleventh-batch-independent-fresh-review-protocol.json`](human-infra-c2-longtail-eleventh-batch-independent-fresh-review-protocol.json)，由 `make c2-longtail-eleventh-batch-independent-fresh-review-protocol-audit` 检查 24 个本地复核行是否被拆成 2 个复核批次，并确认 review fields、verdict taxonomy、promotion decisions、B11 专属建议用途阻塞和模型准入边界已经定义。第十一批 independent fresh review 判定见 [`human-infra-c2-longtail-eleventh-batch-independent-fresh-review-verdict-register.json`](human-infra-c2-longtail-eleventh-batch-independent-fresh-review-verdict-register.json)，由 `make c2-longtail-eleventh-batch-independent-fresh-review-verdict-audit` 检查 24/24 个来源抽取行是否完成判定，确认 21 行只可进入 bounded reviewed artifact prep，3 个 PubMed-only 行继续 blocked-cannot-evaluate，且全部建议用途、干预排序、个体预测和模型准入仍被阻塞。第十一批 reviewed artifacts 见 [`human-infra-c2-longtail-eleventh-batch-reviewed-card-artifact-register.json`](human-infra-c2-longtail-eleventh-batch-reviewed-card-artifact-register.json)，由 `make c2-longtail-eleventh-batch-reviewed-card-artifact-audit` 检查 21 个 eligible fresh-review rows 是否晋升为 126 个 bounded Source/变量/endpoint/uncertainty/transfer/downgrade artifacts，并确认 3 个 PubMed-only blocked rows、全部建议用途、干预排序、个体预测和模型准入仍被阻塞。该批次当前不完成模型准入、个体建议、干预排序或校准预测。

C2 长尾第十二批晋升队列见 [`human-infra-c2-longtail-twelfth-batch-promotion-queue.json`](human-infra-c2-longtail-twelfth-batch-promotion-queue.json)，由 `make c2-longtail-twelfth-batch-promotion-audit` 检查 12 个工程化细胞疗法、类器官/器官芯片、合成生物学生物安全、辐射核安全、消毒灭菌、血源暴露、泌尿生殖、过敏特应、干眼、听觉处理、构音障碍和言语失用 C2 长尾域是否已绑定 24 个 web-checked 候选来源、晋升步骤和模型阻塞边界。第十二批来源深读队列见 [`human-infra-c2-longtail-twelfth-batch-source-extraction-queue.json`](human-infra-c2-longtail-twelfth-batch-source-extraction-queue.json)，由 `make c2-longtail-twelfth-batch-source-extraction-audit` 检查 24 个候选来源是否已派生成 exact claim、endpoint、population、uncertainty、transfer-boundary、downgrade 和 model-position 抽取任务。第十二批来源抽取寄存器见 [`human-infra-c2-longtail-twelfth-batch-source-extraction-register.json`](human-infra-c2-longtail-twelfth-batch-source-extraction-register.json)，由 `make c2-longtail-twelfth-batch-source-extraction-register-audit` 检查 24/24 个来源语境字段抽取是否完成，并确认临床/筛查/药物/生物制品/细胞疗法/生物安全/辐射/感染控制/职业暴露/泌尿生殖/过敏/眼科/听觉/言语/康复建议、reviewed artifacts 和模型准入阻塞仍被显式保留。第十二批本地来源语境复核见 [`human-infra-c2-longtail-twelfth-batch-local-review-register.json`](human-infra-c2-longtail-twelfth-batch-local-review-register.json)，由 `make c2-longtail-twelfth-batch-local-review-audit` 检查 24/24 个抽取行是否完成本地结构复核、0 个本地 source-resolution issue 是否被保持、以及全部行是否只进入 independent fresh review。第十二批 independent fresh review 协议见 [`human-infra-c2-longtail-twelfth-batch-independent-fresh-review-protocol.json`](human-infra-c2-longtail-twelfth-batch-independent-fresh-review-protocol.json)，由 `make c2-longtail-twelfth-batch-independent-fresh-review-protocol-audit` 检查 24 个本地复核行是否被拆成 2 个复核批次，并确认 review fields、verdict taxonomy、promotion decisions、B12 专属建议用途阻塞和模型准入边界已经定义。第十二批 independent fresh review 判定见 [`human-infra-c2-longtail-twelfth-batch-independent-fresh-review-verdict-register.json`](human-infra-c2-longtail-twelfth-batch-independent-fresh-review-verdict-register.json)，由 `make c2-longtail-twelfth-batch-independent-fresh-review-verdict-audit` 检查 24/24 个来源抽取行是否完成判定，确认 20 行只可进入 bounded reviewed artifact prep，4 个 PubMed-only 行继续 blocked-cannot-evaluate，且全部建议用途、干预排序、个体预测和模型准入仍被阻塞。第十二批 reviewed artifacts 见 [`human-infra-c2-longtail-twelfth-batch-reviewed-card-artifact-register.json`](human-infra-c2-longtail-twelfth-batch-reviewed-card-artifact-register.json)，由 `make c2-longtail-twelfth-batch-reviewed-card-artifact-audit` 检查 20 个 eligible fresh-review rows 是否晋升为 120 个 bounded Source/变量/endpoint/uncertainty/transfer/downgrade artifacts，并确认 4 个 PubMed-only blocked rows、全部建议用途、干预排序、个体预测和模型准入仍被阻塞。该批次当前不完成模型准入、个体建议、干预排序或校准预测。

C2 长尾第十三批晋升队列见 [`human-infra-c2-longtail-thirteenth-batch-promotion-queue.json`](human-infra-c2-longtail-thirteenth-batch-promotion-queue.json)，由 `make c2-longtail-thirteenth-batch-promotion-audit` 检查 12 个肢端肥大症、性腺功能低下、ED/血管性性功能、肾结石/梗阻、子宫肌瘤、外阴阴道疼痛/感染、儿童中耳炎、语音音系障碍、前庭性偏头痛、前庭炎/迷路炎、失禁相关皮炎和银屑病 C2 长尾域是否已绑定 24 个 web-checked 候选来源、晋升步骤和模型阻塞边界。第十三批来源深读队列见 [`human-infra-c2-longtail-thirteenth-batch-source-extraction-queue.json`](human-infra-c2-longtail-thirteenth-batch-source-extraction-queue.json)，由 `make c2-longtail-thirteenth-batch-source-extraction-audit` 检查 24 个候选来源是否已派生成 exact claim、endpoint、population、uncertainty、transfer-boundary、downgrade 和 model-position 抽取任务。第十三批来源抽取寄存器见 [`human-infra-c2-longtail-thirteenth-batch-source-extraction-register.json`](human-infra-c2-longtail-thirteenth-batch-source-extraction-register.json)，由 `make c2-longtail-thirteenth-batch-source-extraction-register-audit` 检查 24/24 个来源语境字段、3 个 PubMed/manual-review 路由阻塞、B13 专属建议用途、降级触发和索引。第十三批本地来源语境复核见 [`human-infra-c2-longtail-thirteenth-batch-local-review-register.json`](human-infra-c2-longtail-thirteenth-batch-local-review-register.json)，由 `make c2-longtail-thirteenth-batch-local-review-audit` 检查 24/24 个抽取行是否完成本地结构复核、21 个非问题行是否只进入 independent fresh review、3 个 PubMed/manual-review 路由行是否继续 source-resolution/manual-route 阻塞。第十三批来源解析见 [`human-infra-c2-longtail-thirteenth-batch-source-resolution-register.json`](human-infra-c2-longtail-thirteenth-batch-source-resolution-register.json)，由 `make c2-longtail-thirteenth-batch-source-resolution-audit` 检查 3 个 PubMed/manual-route 问题行是否已解析为 2 个 PMID 身份匹配、1 个失禁相关皮炎 title/domain mismatch 和 1 个 corrected PMID 候选。该批次当前仍不完成 corrected-source re-extraction、fresh review、reviewed artifacts、内分泌/泌尿/生殖/妇科/儿科/听力/言语/前庭/皮肤/康复建议或模型准入。

C2 长尾第十四批晋升队列见 [`human-infra-c2-longtail-fourteenth-batch-promotion-queue.json`](human-infra-c2-longtail-fourteenth-batch-promotion-queue.json)，由 `make c2-longtail-fourteenth-batch-promotion-audit` 检查当前仍未排队的最后 16 个 C2 长尾域是否已绑定 32 个 web-checked 候选来源、晋升步骤和模型阻塞边界。第十四批来源深读队列见 [`human-infra-c2-longtail-fourteenth-batch-source-extraction-queue.json`](human-infra-c2-longtail-fourteenth-batch-source-extraction-queue.json)，由 `make c2-longtail-fourteenth-batch-source-extraction-audit` 检查 32 个候选来源是否已派生成 exact claim、endpoint、population、uncertainty、transfer-boundary、downgrade 和 model-position 抽取任务。第十四批来源抽取寄存器见 [`human-infra-c2-longtail-fourteenth-batch-source-extraction-register.json`](human-infra-c2-longtail-fourteenth-batch-source-extraction-register.json)，由 `make c2-longtail-fourteenth-batch-source-extraction-register-audit` 检查 32/32 个来源语境字段、7 个 403/manual-review 路由阻塞、1 个 FDA 404/source-resolution 路由阻塞、B14 专属建议用途、降级触发和索引。第十四批本地来源语境复核见 [`human-infra-c2-longtail-fourteenth-batch-local-review-register.json`](human-infra-c2-longtail-fourteenth-batch-local-review-register.json)，由 `make c2-longtail-fourteenth-batch-local-review-audit` 检查 32/32 个抽取行是否完成本地结构复核、24 个非问题行是否只进入 independent fresh review、7 个 403/manual-review 和 1 个 FDA 404/source-resolution 路由行是否继续 source-resolution/manual-route 阻塞。该批次将当前 unqueued selection gap 降为 0，并完成 source-specific 字段抽取和本地复核，但仍不完成 fresh review、reviewed artifacts、能源/医疗/法律/环境/数据治理/营养福利/暴露建议或模型准入。

## Claim Spine

本路线图对齐 `HI-CL1`、`HI-CL2`、`HI-CL3`、`HI-CL4`、`HI-CL6` 和 `HI-CL7`：主体持续性是价值成立条件，Human Infra 的对象是主体持续性的基础条件集合，定量模型必须区分寿命、健康寿命、有效时间和未来选择权，并把技术放入变量、状态、风险函数和证据链中审查。边界：不是医疗建议；不输出个体死亡日期；不证明具体技术已经实现有效永生。

## 总判断

截至 2026-07-04，项目已经完成了价值追问、域地图、主流 LEV 路线和 Web 叙事的主体搭建，但尚未达到完整研究工程系统。

| 轴线 | 当前成熟度 | 100% 状态 | 当前最大缺口 |
| --- | ---: | --- | --- |
| 项目价值 | 100% | 不同受众能用同一核心命题理解 Human Infra 的必要性 | 已有核心命题、多视角价值解析、页面级 Claim ID 一致性门禁、受众-主张映射和邻近项目边界对照；后续只需防止页面漂移 |
| 研究框架 | 99% | 每条主张都进入 Source Card、Claim-Evidence Matrix、变量表和反证条件 | 已有核心主张矩阵、页面级 Claim ID 门禁、arXiv-style 论文页强主张门禁、C1/20 个优先 C2 反证覆盖门禁、v0.1 反证 Source Card 锚点回填、当前 21 个来源锚点字段级 Source Card 抽取、30 个优先域的域级 Claim-Evidence Matrix seed、30 个优先域的 endpoint 候选和 source-specific 深读槽位、93 个 domain-source 深读任务队列、81/93 个 domain-source 精读完成行并保留 12 个奇点域待完成任务、81 项卡片晋升队列、20 个来源锚点本地来源语境复核账本、81 项卡片晋升预注册包、独立 fresh review 协议、FRB-01 到 FRB-04 合计 81/81 个 fresh-review verdict、486 个 reviewed card artifacts、4 条 future-boundary route cards、204 个 C2 域长尾覆盖账本、本地审计门禁、第一批 24 个高影响 C2 长尾域晋升队列、48 个 C2-LT-B1 逐源深读任务、48/48 个 C2-LT-B1 来源抽取试运行行、48/48 个 C2-LT-B1 本地来源语境复核门禁、C2-LT-B1 48 行独立 fresh-review 协议、48/48 个 C2-LT-B1 独立 fresh-review verdict、42 个 eligible C2-LT-B1 来源行晋升出的 252 个 reviewed artifacts、6 个非 eligible 行的 blocked source resolution 候选、6 个来源纠偏行的 source-resolution fresh review verdict、10 个 corrected source re-extraction 任务、10/10 个 corrected source re-extraction 输出、10/10 个 corrected source fresh review verdict、5 个 eligible corrected rows 晋升出的 30 个 corrected reviewed artifacts，以及第二批 12 个剩余 C2 长尾域的晋升队列、24 个 web-checked 候选来源、24/24 个本地抽取行、24/24 个本地来源语境复核行、2 批 independent fresh review 协议和 24/24 个 fresh-review verdict，其中 23 行可进入 bounded artifact fill、1 行 downgrade-before-fill，并已把 23 个 eligible rows 晋升为 138 个 bounded reviewed artifacts；第三批又选择 12 个神经-感知-认知连续性 C2 长尾域，绑定 24 个 web-checked 候选来源，派生 24 个深读任务，完成 24/24 个本地来源语境字段抽取、24/24 个本地来源语境复核、5 个问题行的 7 个 corrected/split/route-normalized source-resolution candidates、2 批 independent fresh-review 协议和 24/24 个 fresh-review verdict，其中 18 行可进入 bounded artifact fill、5 行只允许 corrected-source re-extraction、1 行 downgrade-before-fill，并已把 7 个 corrected/split/route-normalized 候选完成 bounded source re-extraction 和 7/7 corrected source fresh-review verdict，其中 6 行可进入 bounded artifact prep、1 行保持 duplicate/split route 阻塞；现在又把 18 个原始 eligible 行和 6 个 corrected eligible 行晋升为 144 个 bounded reviewed artifacts，并保留 EXT-022 downgrade-before-fill 与 C2LTB3-CREXT-004 duplicate/split route blocked row；第四批又选择 12 个代谢、内分泌、肾肝、电解质和携氧稳态连续性 C2 长尾域，绑定 24 个 web-checked 候选来源，派生 24 个 source-specific 深读任务，并完成 24/24 个本地来源语境字段抽取、24/24 个本地来源语境复核、4 个问题行的 source-resolution 候选准备、8 个候选的 manual/fulltext extraction、8/8 个 manual/fulltext fresh-review verdict，并把 3 个 eligible manual/fulltext fresh-review rows 晋升为 18 个 bounded reviewed artifacts，显式保留 5 个 duplicate/route-only/manual-access/context-only 阻塞行、3 个无摘要需全文复核行、1 个重复共识路线行和 8 个来源路线候选；第五批又选择 12 个细胞质量控制、细胞器通信、分子运输、膜脂韧性、清除和屏障底座 C2 长尾域，绑定 24 个 web/API-checked 候选来源，派生 24 个 source-specific 深读任务，完成 24/24 个本地来源语境字段抽取、24/24 个本地来源语境复核，并把 8 个无开放全文或跨域复用问题行整理为 14 个 PubMed、Europe PMC、DOI 或 PMC route 候选；第六批、第七批、第八批、第九批与第十批已经继续扩展到跨代/儿科、癌症/移植、疼痛/创伤/感知通信/神经技术/活性算力、肌骨/口腔/呼吸/免疫老化/环境暴露，以及设备感染、居家透析、感觉输入、伤口边界、温度稳态、烧伤、糖尿病视网膜病变、照护者健康、窒息和吞咽障碍入口；B8/B9/B10 已分别进入 bounded reviewed artifacts 或保留显式阻塞行；剩余缺口是后续未覆盖 C2 批次、跨批次强主张闭合和校准模型准入 |
| 定量模型 | 95% | 有可运行、可复现、可审查的场景级模型管线 | 已有 toy model、合成敏感性分析、合成验证/校准报告 dry-run、L4 合成证据包 dry-run、审计器、NCHS 2021 U.S. Life Tables 公开聚合死亡率锚点、NHANES public-use LMF aggregate pilot、survey-design / domain-rule / positive-weight eligible-base / weighted-estimator / R survey runtime probe / controlled runtime smoke / domain indicator metadata / DOF-sparse metadata / synthetic disclosure envelope / synthetic effective sample-CI publication / synthetic weighted-output implementation preflight / disclosure review template / disclosure review execution register / public-output implementation review template / public-output implementation review execution register / weighted-domain output safety validators、local-only ignored weighted-domain run、local disclosure review packet、tracked local-run evidence manifest、public release gate、public Web data no-real-values scan、校准预备契约、真实队列候选注册表、NHATS 数据准入草案、变量字典草案、extraction manifest 草案、official source refresh / registration template / file-tier / acquisition-readiness / storage-destruction / synthetic drill / estimand / variable-confirmation / cohort-flow / disclosure / survey-design / missingness / route-field / Colectica capture packet validator / capture-packet review execution / route-value crosswalk assembly / route-value crosswalk entry-validator / L2 variable-family / pre-outcome / L4 readiness runway validators、模型准入契约、模型准入候选注册表、L4 evidence intake、L4 evidence packet review playbook 和 L4 validation/calibration reporting contract；默认 R survey runtime probe 已明确为诊断型 pass，可记录本机 `blocked-no-rscript` 而不提供可复现运行时；controlled runtime smoke 才是 R `survey` synthetic 运行时可复现证据。合成验证/校准报告 dry-run 只演练 12 个报告章节和 5 个 L4 槽位如何被填充并继续阻塞，不能替代真实验证、真实校准、TRIPOD+AI / PROBAST+AI 报告包或 L4 admission。L4 合成证据包 dry-run 只演练 24 个 pending slot 的 hash-only draft packet 形状，不能替代真实 evidence packet、人审完成、slot closure 或 L4 admission。NHANES 已从公开聚合烟测和 metadata / safety gates 推进到本地受控真实 weighted-domain 运行，能在 ignored `build/reports` 中生成 8 个 sex × ageBand cells、真实 weighted rates 和 design-based intervals，并通过 tracked redacted manifest 在版本库中保留 hash/runtime/summary 级证据，再通过 public-output implementation review template/execution register 和 public release gate 固定 `blocked-pending-human-disclosure-review` 决策，并通过 public Web data no-real-values scan 阻止真实数值进入前端 JSON；但公开发布层仍 blocked，weighted-domain output readiness 是 12 个 ready gates、2 个 blocked gates，真实 disclosure review、公开 weighted-domain output implementation、真实 NHATS 注册证明、Colectica 登录、变量页实捕获、value labels 精确确认、question text / universe / skip logic 确认、真实提取、真实 NHATS route classification、真实 NHATS 输出披露审查、公开 survey-design 加权估计、外部验证、校准诊断、TRIPOD+AI / PROBAST+AI 报告包、校准后的敏感性分析和任何 L4 calibrated admission 仍未完成 |

## 价值层 100%

价值层的 100% 不是写更多宏大叙事，而是让项目在不同入口都指向同一个第一原理：

```text
一切目标、价值和创造都预设一个能够持续行动的主体
  -> 主体持续性不是普通目标之一，而是所有目标成立的边界条件
  -> Human Infra 的对象是维持、延展、增强主体持续性所需的生命、认知、时间、资源、工具、环境和协作系统
  -> 项目价值不是单点延寿，而是扩大主体未来仍能存在、行动、学习、修正和选择的可能性空间
```

验收条件：

- 有一个 100 字内总定义，能解释目标、对象和约束。
- 有至少三种价值视角：主体持续性、通用资源增量、反稀缺工程。
- 每种视角都能说明它改变的稀缺资源：寿命、健康寿命、有效时间、注意力、认知、恢复、资金、社会支持、环境和未来选择权。
- 能区分 Human Infra 与健康管理、长寿知识库、AI 工具箱、社会政策百科和医学建议系统。
- 能把价值语言连接到外部理论脊柱：能力方法、健康作为身体/心理/社会福祉、福祉测量、复杂干预和预测模型报告规范。

## 研究框架 100%

研究框架的 100% 是让每个研究域和每条主张都能被审查。

最低结构：

```text
研究问题
  -> 研究域对象
  -> 变量表
  -> 机制链路
  -> Source Cards
  -> Claim-Evidence Matrix
  -> 反证条件
  -> 模型位置
  -> 治理边界
```

验收条件：

- 研究域必须进入 C1-C6 物理分级目录，并在 README / AGENTS 中说明对象、非目标和上下游。
- 每个进入主论文或 Web 页的强主张必须绑定来源、证据等级、适用范围和禁止外推边界。
- 每个定量相关主张必须区分相关性、因果效应、预测能力、机制合理性和治理判断。
- 每条路线必须拆出概率门：技术窗口、可及性、采用概率、持续时间、组合性、尾部风险、机会成本。
- 模型必须区分 `screening model`、`toy model`、`calibrated predictive model` 和 `decision model`。
- 高风险领域必须写明中止条件，而不是只写“未来可能”。

## 定量模型 100%

定量模型的 100% 不是预测个人死亡日期，而是建立可复现的场景级生命路径模型。

目标形态：

```text
versioned inputs
  -> executable model
  -> generated scenario outputs
  -> Web visualization
  -> model card
  -> sanity checks
  -> governance boundary
```

最小可运行模型必须做到：

- 从版本化 JSON / TSV 输入读取场景，而不是把参数只写在前端脚本里。
- 命令行能生成 Web 数据文件。
- 输出群体/合成队列的风险函数、生存曲线、健康质量积分、有效时间和 LEV 阈值状态。
- 不输出个体死亡日期，不给个体医疗建议，不声明真实疗效。
- 包含模型卡：用途、非用途、输入来源、证据等级、主要假设、已知限制和升级条件。
- 包含 sanity checks：生存曲线单调、概率范围合法、无个人预测字段、场景 ID 唯一。
- 包含审计产物：机器可读 JSON 和人可读 Markdown，证明模型输出满足本地报告契约。
- 包含校准预备契约：target population、time zero、outcome、estimand、predictor、censoring、validation、calibration、sensitivity、bias/applicability 和 prohibited use 的最低字段。

## 外部方法锚点

这些锚点只提供方法约束，不直接证明 Human Infra 的任何具体主张。

| 来源 | Human Infra 使用位置 | 边界 |
| --- | --- | --- |
| Stanford Encyclopedia of Philosophy: Capability Approach | 把项目价值从资源占有转向真实能力、功能和选择空间 | 不把能力方法直接等同于永生伦理 |
| WHO Constitution | 把健康理解为身体、心理和社会福祉，而非仅无病 | 不把 WHO 定义当作具体干预证据 |
| MRC complex interventions framework | 复杂干预需要开发、评估、实施和语境分析 | 不替代具体临床试验 |
| TRIPOD+AI | 预测模型需要透明报告、开发/验证/更新边界 | 不表示当前 toy model 已达临床预测标准 |
| PROBAST / PROBAST+AI | 预测模型偏倚和适用性需要系统评估 | 不表示当前模型已具备低偏倚 |
| ISPOR Modeling Good Research Practices | 模型需要结构、参数、验证、报告和决策语境 | 不表示当前模型可用于真实资源分配 |
| DYNAMO-HIA / Future Elderly Model / OHDSI PLP | 可参考群体健康模拟、老龄化微观仿真和患者级预测工程 | 不直接复用为 Human Infra 校准模型 |

## 阶段路线

### Stage 1: 价值和边界冻结

完成条件：

- README、Web 首页、论文页和 reference 文档都使用同一套目标、对象、约束语言。
- 价值视角不再互相竞争，而是作为同一第一原理的不同投影。
- 每个传播性概念都有正式研究名和禁止误读说明。

### Stage 2: 研究域证据闭环

完成条件：

- C1 / C2 核心域优先完成 Source Cards 和 Claim-Evidence Matrix。
- 每个主流 LEV 路线都有路线卡、概率门、负向链路和证据边界。
- 所有强主张都能回到本地文档、来源链接和审查状态。

### Stage 3: Toy model 可运行

完成条件：

- 存在独立脚本可从版本化输入导出 Web 模型数据。
- Web 页面消费导出数据，而不是只用内嵌示意参数。
- CI / make check 能至少编译模型脚本。

### Stage 4: 校准模型预备

完成条件：

- 明确 target population、estimand、time zero、outcome、predictors、censoring 和 validation plan。
- 明确可用数据源、数据质量、缺失、代表性和伦理边界。
- 引入 TRIPOD+AI、PROBAST+AI、MRC 和 ISPOR 的最低报告字段。
- 机器审计必须证明当前仍然不能校准：没有真实队列、没有外部验证、没有个人用途许可。

### Stage 5: 严肃研究系统

完成条件：

- 模型、文档、Source Cards、Web 可视化和审计账本可一起复现。
- 能清楚说明某个技术或资源如何改变变量、状态、风险函数、生存曲线、有效时间和未来选择权。
- 能清楚说明当前不能算什么、为什么不能算、缺什么数据才能算。

## 当前下一步

当前已经完成最小 toy model 管线和校准预备契约：

```text
life_path_toy_model_scenarios.json
  -> run_life_path_toy_model.py
  -> life-path-toy-model.json
  -> run_life_path_sensitivity_analysis.py
  -> life-path-sensitivity-analysis.json
  -> build_life_path_synthetic_validation_calibration_report.py
  -> life-path-synthetic-validation-calibration-report.json / .md
  -> audit_life_path_toy_model.py
  -> life-path-toy-model-audit.json / .md
  -> life_path_calibration_readiness.json
  -> human-infra-model-admission-contract.json
  -> human-infra-model-admission-candidate-registry.json
  -> human-infra-domain-to-model-bridge-contract.json
  -> human-infra-domain-to-model-bridge-register.json
  -> human-infra-domain-to-model-bridge-validation.json
  -> life_path_data_source_candidates.json
  -> life-path-data-source-cards.md
  -> life-path-data-card-template.md
  -> life-path-data-card-nhats.md
  -> life-path-variable-dictionary-nhats.md
  -> life-path-extraction-manifest-nhats-draft.md
  -> life_path_nhats_official_source_refresh_register.json
  -> validate_nhats_official_source_refresh.py
  -> life-path-nhats-official-source-refresh-validation.json
  -> life_path_nhats_registration_evidence_template.json
  -> validate_nhats_registration_evidence_template.py
  -> life-path-nhats-registration-evidence-template-validation.json
  -> life_path_nhats_registration_evidence_packet_validator_test_cases.json
  -> validate_nhats_registration_evidence_packet_validator.py
  -> life-path-nhats-registration-evidence-packet-validator-validation.json
  -> life_path_nhats_acquisition_readiness.json
  -> validate_nhats_acquisition_readiness.py
  -> life-path-nhats-acquisition-readiness-validation.json
  -> life_path_nhats_controlled_storage_destruction_plan.json
  -> validate_nhats_controlled_storage_destruction_plan.py
  -> life-path-nhats-controlled-storage-destruction-validation.json
  -> life_path_nhats_synthetic_storage_destruction_drill.json
  -> validate_nhats_synthetic_storage_destruction_drill.py
  -> life-path-nhats-synthetic-storage-destruction-drill-validation.json
  -> life_path_nhats_file_tier_table.json
  -> validate_nhats_file_tier_table.py
  -> life-path-nhats-file-tier-table-validation.json
  -> life_path_nhats_first_estimand_protocol.json
  -> life_path_nhats_variable_confirmation_matrix.json
  -> life_path_nhats_cohort_flow_endpoint_protocol.json
  -> life_path_nhats_disclosure_control_policy.json
  -> life_path_nhats_disclosure_control_test_cases.json
  -> validate_nhats_disclosure_outputs.py
  -> life-path-nhats-disclosure-control-validation.json
  -> life_path_nhats_survey_design_protocol.json
  -> life_path_nhats_survey_design_test_cases.json
  -> validate_nhats_survey_design_plan.py
  -> life-path-nhats-survey-design-validation.json
  -> life_path_nhats_missingness_route_protocol.json
  -> life_path_nhats_missingness_route_test_cases.json
  -> validate_nhats_missingness_route_map.py
  -> life-path-nhats-missingness-route-validation.json
  -> life_path_nhats_route_field_discovery_register.json
  -> validate_nhats_route_field_discovery.py
  -> life-path-nhats-route-field-discovery-validation.json
  -> life_path_nhats_colectica_value_label_review_protocol.json
  -> validate_nhats_colectica_value_label_protocol.py
  -> life-path-nhats-colectica-value-label-validation.json
  -> life_path_nhats_colectica_value_label_review_execution_register.json
  -> validate_nhats_colectica_value_label_review_execution.py
  -> life-path-nhats-colectica-value-label-review-execution-validation.json
  -> life_path_nhats_colectica_access_route_probe_register.json
  -> validate_nhats_colectica_access_route_probe.py
  -> life-path-nhats-colectica-access-route-probe-validation.json
  -> life_path_nhats_colectica_authenticated_capture_template.json
  -> validate_nhats_colectica_authenticated_capture_template.py
  -> life-path-nhats-colectica-authenticated-capture-template-validation.json
  -> life_path_nhats_colectica_capture_task_register.json
  -> validate_nhats_colectica_capture_task_register.py
  -> life-path-nhats-colectica-capture-task-register-validation.json
  -> life_path_nhats_colectica_capture_packet_validator_test_cases.json
  -> validate_nhats_colectica_capture_packet_validator.py
  -> life-path-nhats-colectica-capture-packet-validator-validation.json
  -> life_path_nhats_l2_variable_family_admission_register.json
  -> validate_nhats_l2_variable_family_admission.py
  -> life-path-nhats-l2-variable-family-admission-validation.json
  -> life_path_nhats_preoutcome_aggregation_protocol.json
  -> validate_nhats_preoutcome_aggregation_protocol.py
  -> life-path-nhats-preoutcome-aggregation-validation.json
  -> life_path_nhats_l4_readiness_runway.json
  -> validate_nhats_l4_readiness_runway.py
  -> life-path-nhats-l4-readiness-runway-validation.json
  -> /model/ Web 图表
  -> model card + sanity checks + synthetic sensitivity checks + calibration-readiness audit checks + data-source candidate audit checks + source-card/data-card readiness checks + NHATS data-admission checks + pre-extraction manifest checks + official source refresh checks + machine-readable acquisition-readiness checks + acquisition-readiness validator checks + controlled storage/destruction validator checks + synthetic storage/destruction drill checks + file-tier table checks + file-tier table validation checks + first-estimand protocol checks + variable-confirmation matrix checks + cohort-flow endpoint-routing protocol checks + synthetic disclosure-control checks + synthetic survey-design checks + synthetic missingness-route checks + official route-field discovery checks + Colectica value-label review protocol checks + Colectica value-label review execution checks + Colectica access-route probe checks + Colectica authenticated capture template checks + Colectica capture task register checks + NHATS route-value crosswalk assembly checks + NHATS route-value crosswalk entry-validator checks + NHATS L2 variable-family admission checks + NHATS pre-outcome aggregation checks + NHATS L4 readiness runway checks + NHANES public-use LMF aggregate pilot checks + NHANES public-use LMF domain/subpopulation rule readiness checks + NHANES public-use LMF positive-weight eligible-base readiness checks + NHANES public-use LMF weighted-estimator readiness checks + NHANES public-use LMF R survey runtime smoke checks + NHANES controlled R survey runtime smoke proof + NHANES public-use LMF domain indicator metadata diagnostic checks + NHANES public-use LMF DOF/sparse-domain metadata diagnostic checks + NHANES public-use LMF synthetic disclosure output envelope checks + NHANES public-use LMF synthetic effective sample-CI publication checks + NHANES public-use LMF synthetic weighted-output implementation preflight checks + NHANES public-use LMF disclosure review template checks + NHANES public-use LMF disclosure review execution register checks + NHANES public-use LMF weighted-domain output safety checks + NHANES public-use LMF local-only weighted-domain run checks + NHANES public-use LMF local disclosure review packet checks + NHANES public-use LMF local packet-validation checks + NHANES public-use LMF tracked local-run evidence manifest checks + NHANES public-use LMF public Web data no-real-values checks
```

这一步已经把项目从“有定量想法的研究叙事”推进到“有最小可执行、可审计模型管线的研究系统”，并且开始把合成敏感性分析、真实队列候选、治理边界、第一份 NHATS 数据准入草案、NHANES public-use LMF survey-design readiness validator、NHANES public-use LMF domain/subpopulation rule readiness validator、NHANES public-use LMF positive-weight eligible-base readiness validator、NHANES public-use LMF weighted-estimator readiness validator、NHANES public-use LMF R survey runtime smoke validator、NHANES controlled R survey runtime smoke proof、NHANES public-use LMF domain indicator metadata diagnostic validator、NHANES public-use LMF DOF/sparse-domain metadata diagnostic validator、NHANES public-use LMF synthetic disclosure output envelope validator、NHANES public-use LMF synthetic effective sample-CI publication validator、NHANES public-use LMF synthetic weighted-output implementation preflight validator、NHANES public-use LMF disclosure review template validator、NHANES public-use LMF disclosure review execution register validator、NHANES public-use LMF weighted-domain output safety gate、NHANES public-use LMF local-only weighted-domain run validator、NHANES public-use LMF local disclosure review packet validator、NHANES public-use LMF ignored packet-validation validator、NHANES public-use LMF tracked local-run evidence manifest validator、NHATS official source refresh register / validator、NHATS 机器可读 acquisition-readiness gates、NHATS acquisition-readiness validator、NHATS controlled storage/destruction validator、NHATS synthetic storage/destruction drill validator、R13/R14 file-tier table / validator、第一版 NHATS estimand protocol、NHATS variable confirmation matrix、NHATS cohort-flow endpoint-routing protocol、synthetic disclosure-control validator、synthetic survey-design validator、synthetic missingness-route validator、NHATS route-field discovery validator、NHATS Colectica value-label review protocol validator、NHATS Colectica value-label review execution validator、NHATS Colectica access-route probe validator、NHATS Colectica authenticated capture template validator、NHATS Colectica capture task register validator、NHATS route-value crosswalk assembly validator、NHATS route-value crosswalk entry validator、NHATS L2 variable-family admission validator、NHATS pre-outcome aggregation validator、NHATS L4 readiness runway validator、模型准入契约、模型准入候选注册表、L4 模型准入阻塞矩阵、L4 解阻执行计划、L4 证据 intake 寄存器、L4 证据包审查 playbook、L4 验证/校准报告契约和核心主张证据矩阵纳入机器审计。下一步不是继续膨胀新域，而是补四件硬东西：

- 继续用 `human-infra-core-claim-evidence-matrix.md` 作为核心主张入口，把 README、论文页和 Web 页的强叙事都回连到同一组 Claim ID、来源角色和禁止外推边界。
- C2 长尾深读已经形成六批推进线：B1 完成 48/48 fresh-review verdict、252 个原始 reviewed artifacts、10 个 corrected source re-extraction、10/10 corrected source fresh-review verdict 和 30 个 corrected reviewed artifacts；B2 完成 24/24 fresh-review verdict，并把 23 个 eligible rows 晋升为 138 个 bounded reviewed artifacts；B3 已完成 24/24 字段抽取、24/24 本地来源语境复核、24/24 independent fresh-review verdict、5 个问题行的 7 个 corrected/split/route-normalized 候选、7/7 corrected source re-extraction、7/7 corrected source fresh-review verdict，以及 144 个 bounded reviewed artifacts；EXT-022 downgrade-before-fill 与 C2LTB3-CREXT-004 duplicate/split route 均已显式保留为 blocked row；B4 已选定 12 个代谢、内分泌、肾肝、电解质和携氧稳态连续性域，绑定 24 个 web-checked 候选来源，派生 24 个 source-specific 深读任务，并完成 24/24 个本地来源语境字段抽取、24/24 个本地来源语境复核、4 个问题行的 source-resolution 候选准备、8 个候选的 manual/fulltext extraction、8/8 个 manual/fulltext fresh-review verdict，以及 3 个 eligible manual/fulltext fresh-review rows 对应的 18 个 bounded reviewed artifacts；5 个 duplicate/route-only/manual-access/context-only blockedRows 被显式保留。B5 已完成 24/24 字段抽取、24/24 本地复核、8 个问题行的 source-resolution、14 个 manual/fulltext extraction、30 行 independent fresh review 判定，并把 17 个 eligible rows 晋升为 102 个 bounded reviewed artifacts。B6 已选定 12 个跨代连续性、生殖力、孕产新生儿、儿童免疫、儿童铅暴露、儿童喂养吞咽、哺乳和儿童口腔健康 C2 长尾域，完成 24/24 字段抽取、24/24 本地复核、7 个问题行的 source-resolution、19 个 manual/fulltext extraction、36 行 independent fresh review 判定，并把 24 个 eligible rows 晋升为 144 个 bounded reviewed artifacts；12 个 manual blocked/context rows 被显式保留，模型准入继续禁止。
- 把 NHATS manifest、controlled storage/destruction plan、route-field discovery register、Colectica value-label review protocol、Colectica value-label review execution register、Colectica access-route probe register、Colectica authenticated capture template、L2 variable-family admission register、pre-outcome aggregation protocol、L4 readiness runway 和 first estimand protocol 从 draft / partial-executed / login-required / template-only / L2-only / protocol-only / runway-only 推进到 governed acquisition-ready，补真实受控工作区执行记录、access/inventory log、受控工作区内销毁证据、Colectica 登录复核、variable page capture hash、value labels、question text、universe/skip logic、精确字段名、轮次、变量级缺失码、公开/敏感/受限状态、权重、endpoint 定义、cohort flow、survey design、代码本来源、真实聚合前置证据和输出抑制规则。
- 把 sensitivity analysis 从合成一因素扰动推进到基于真实队列、预注册范围和校准诊断的敏感性分析。

## 当前已具备的定量门禁

`npm run export:life-path-toy` 生成场景级模型输出。

`npm run export:life-path-validation-calibration-report` 生成 `web/src/data/life-path-synthetic-validation-calibration-report.json` 和 `.md`，当前只演练 L4 报告契约的 12 个章节、5 个槽位和阻塞规则，不生成真实验证、真实校准、公开加权输出、L4 admission 或个体预测。

`npm run export:life-path-l4-validation-calibration-report-execution-validation` 生成 `web/src/data/life-path-l4-validation-calibration-report-execution-validation.json`，当前只验证 L4 验证/校准报告执行寄存器中 12 个报告段落和 5 个 L4WO-05 槽位仍缺真实报告包、人审和二审签名；它不生成真实验证、真实校准、公开加权输出、L4 admission 或个体预测。

`npm run export:life-path-l4-evidence-packet-dry-run` 生成 `web/src/data/life-path-l4-synthetic-evidence-packet-dry-run.json` 和 `.md`，当前只演练 L4 evidence intake 的 24 个 pending slot、hash-only draft packet、零真实 evidence packet、零人审、零 slot closure 和阻塞规则，不生成直接证据、公开加权输出、L4 admission 或个体预测。

`npm run export:life-path-l4-evidence-packet-validator-validation` 生成 `web/src/data/life-path-l4-evidence-packet-validator-validation.json`，当前只验证 synthetic future packet cases 的 `rejected`、`cannot-evaluate` 和 `reviewable-but-still-blocked` 预检语义，不生成真实 evidence packet、人审签名、slot closure、公开加权输出、L4 admission 或个体预测。

`npm run export:nhats-colectica-capture-packet-validator-validation` 生成 `web/src/data/life-path-nhats-colectica-capture-packet-validator-validation.json`，当前只验证 NHATS Colectica future capture packet cases 的 `rejected`、`cannot-evaluate` 和 `reviewable-but-still-blocked` 预检语义，不生成真实 Colectica capture、人审签名、slot closure、route classifier、真实提取、公开加权输出、校准或个体预测。

`npm run export:nhats-colectica-capture-packet-review-execution-validation` 生成 `web/src/data/life-path-nhats-colectica-capture-packet-review-execution-validation.json`，当前只验证 39 个 Colectica capture-packet review slots 仍为 pending，且 0 个真实包、0 个人审完成、0 个二审完成、0 个 slot closure、0 个 route classifier admission，不生成真实字段确认、真实提取、公开加权输出、校准或个体预测。

`npm run export:nhats-route-value-crosswalk-assembly-validation` 生成 `web/src/data/life-path-nhats-route-value-crosswalk-assembly-validation.json`，当前只验证 9 个 route-field assembly units、上游 hash 绑定、敏感 death-date 排除和全部 0 准入状态，不生成真实 route-value rows、变量级 missing-code maps、route classifier、真实提取、公开加权输出、校准或个体预测。

`npm run export:nhats-route-value-crosswalk-entry-validator-validation` 生成 `web/src/data/life-path-nhats-route-value-crosswalk-entry-validator-validation.json`，当前只验证 synthetic future route-value / missing-code crosswalk 条目的 `reviewable-but-still-blocked`、`cannot-evaluate` 和 `rejected` 预检语义，不生成真实 route-value rows、变量级 missing-code maps、slot closure、route classifier、真实提取、公开加权输出、校准或个体预测。

`make nhats-route-classifier-synthetic-dry-run-audit` 生成 ignored `build/reports/nhats-route-classifier-synthetic-dry-run/route-classifier-synthetic-dry-run.json` 和 tracked [`../../web/src/data/life-path-nhats-route-classifier-synthetic-dry-run-validation.json`](../../web/src/data/life-path-nhats-route-classifier-synthetic-dry-run-validation.json)，当前只用 8 个 synthetic route envelope cases 验证 route classifier 逻辑可以 fail-closed 运行；它不读取真实 NHATS rows、不生成 weighted route counts、不打开 public export、校准、L4 admission 或 individual prediction。总 toy model audit 会消费该 tracked validation，确保 synthetic dry-run 不停留在孤立 build artifact。

`make life-path-toy-model-audit` 或 `npm run audit:life-path-toy` 生成 `web/src/data/life-path-toy-model-audit.json` 和 `web/src/data/life-path-toy-model-audit.md`；npm 路径会先生成 route-classifier synthetic dry-run validation，Make 路径在默认 `make check` 中位于 NHATS route classifier / L4 readiness gates 之后。当前检查包括：

- schema version 是否正确；
- source path 和 sha256 是否回到输入场景；
- model card 是否包含必需字段；
- prohibited use 是否明确禁止个体死亡日期和个体预测；
- evidence boundary 是否明确为 synthetic；
- scenario ID 是否唯一且包含 baseline；
- 每个场景是否包含必需 metrics；
- 生存曲线是否单调非增；
- survival / health-quality 是否处于 `[0, 1]`；
- resource budget 是否处于 `[0, 100]`；
- `LEV >= 1` 是否显示开放边界；
- 是否不存在个体死亡日期字段。
- 合成敏感性分析是否存在；
- 合成敏感性分析是否回到当前 toy model 的 source hash；
- 合成敏感性分析是否覆盖风险倍率、健康质量位移、能力倍率、主观时间、LEV 进度和尾部风险；
- 合成敏感性分析是否生成 48 个一因素扰动结果、场景稳定性摘要和禁止个体死亡日期字段检查；
- 合成验证/校准报告 dry-run 是否存在，是否覆盖 L4 报告契约 12 个章节和 5 个槽位，并继续保持真实验证、真实校准、公开加权输出、L4 admission 和个体用途全部 blocked；
- L4 合成证据包 dry-run 是否存在，是否覆盖 L4 intake register 的 24 个 pending slot，并继续保持真实 evidence packet、人审、second review、slot closure、公开加权输出、L4 admission 和个体用途全部 blocked；
- 校准预备契约是否存在；
- 是否明确当前没有真实队列、校准、外部验证和个体用途；
- 是否包含 TRIPOD+AI、PROBAST/PROBAST+AI、ISPOR、MRC 和 OHDSI PLP 方法锚点；
- 是否包含 target population、time zero、outcome、estimand、predictor、data requirement、censoring、validation、calibration、sensitivity、bias/applicability、reporting 和 prohibited use 字段。
- 候选数据源注册表是否存在；
- 候选数据源是否明确 no data download、no access grant、no individual data、no calibration claim 和 no causal claim；
- 候选数据源是否覆盖 mortality、function、biomarkers、cognition、resource/social 和 external validation 的最低需求；
- NHANES public-use LMF aggregate pilot 是否存在，是否回到官方 CDC/NCHS LMF、DEMO_J 和 read-in script source hash，是否 `PASS`，是否只输出 sex × ageBand 聚合单元，并继续阻止 raw-row persistence、个体预测、死亡日期输出、加权总体推断、校准、因果和医学建议。
- 每个候选源是否使用官方 HTTPS URL、写明 access/governance status，并禁止个体预测、校准过度主张和因果过度主张。
- 数据源 Source Cards 是否存在、覆盖每个候选源 ID 和官方 URL，并保留 candidate-only、未下载真实数据、未建立校准、禁止个体死亡日期预测和未外部验证边界；
- Data Card 模板是否存在，是否包含 Header、Governance、Study Design、Outcomes、Predictors、Data Quality、Model Use、Decision 和 Source Trace，并禁止个体死亡日期预测、个人医疗建议、个人寿命排名和未验证的校准声明。
- NHATS Data Card 是否存在，是否包含 source_card_id、draft/cannot-evaluate-yet 状态、官方来源追踪、禁止个体预测、禁止个人医疗建议、禁止 raw data 上传到公共 AI 系统、有效时间代理、不可评估决策和中止条件。
- NHATS 变量字典草案是否存在，是否保持 candidate-only 边界，并覆盖 design/identity、outcome boundary、function/mobility、cognition/attention、resources/support、environment/access 和 effective_time_proxy 这些模型角色。
- NHATS extraction manifest 草案是否存在，是否绑定 source card、Data Card 和变量字典，是否保持 cannot-extract-yet 状态，是否记录官方访问条款、Colectica/codebook 依赖、候选变量组、禁止 raw data 入库 / public LLM 上传、允许/禁止输出和中止条件。
- NHATS acquisition readiness 机器契约是否存在，是否保持 `cannot-extract-yet`，是否覆盖官方来源刷新、注册状态、文件层级、Colectica 变量确认、round window、survey design、endpoint、披露控制、AI 边界、存储销毁、禁止动作和下一步证据。
- NHATS official source refresh register / validation 是否存在，是否回到当前 8 个官方公开来源 hash，是否 `PASS`，是否只把 official-source-refresh 门升为 ready，并继续禁止下载、抽取、raw data 入库、校准和个体预测。
- NHATS registration evidence template / validation 是否存在，是否回到当前 template hash，是否 `PASS`，是否证明 8 个注册/访问证据槽、redacted-only repository boundary 和 no-registration-proof / no-download / no-extraction / no-calibration / no-individual-prediction 边界。
- NHATS acquisition readiness validation 是否存在，是否回到当前机器契约 hash，是否 `PASS`，是否证明 1 个 official-source-refresh 门 ready、1 个 registration template 门 partial、8 个其他 readiness gates 仍阻塞 extraction，并继续禁止下载、抽取、raw data 入库、校准和个体预测。
- NHANES public-use LMF survey-design readiness validation 是否存在，是否回到当前 readiness 契约 hash，是否 `PASS`，是否只证明 WTMEC2YR、SDMVPSU、SDMVSTRA 官方字段和诊断边界，并继续禁止 survey-weighted inference、design-based confidence interval、校准和个体预测。
- NHANES public-use LMF domain/subpopulation rule readiness validation 是否存在，是否回到当前 readiness 契约 hash，是否 `PASS`，是否只证明官方 domain/subpopulation 机制、完整设计输入要求和禁止 row-drop subgroup filtering 的边界，并继续禁止 weighted domain inference、design-based confidence interval、校准和个体预测。
- NHANES public-use LMF positive-weight eligible-base readiness validation 是否存在，是否回到当前 readiness 契约 hash，是否 `PASS`，是否只证明 `WTMEC2YR > 0` eligible-base 诊断、5809 名 positive-weight eligible adults、no-row-persistence 和 no-weighted-domain-inference 边界，并继续禁止 weighted domain inference、design-based confidence interval、校准和个体预测。
- NHANES public-use LMF weighted-estimator readiness validation 是否存在，是否回到当前 readiness 契约 hash，是否 `PASS`，是否只证明 R `survey` / `svydesign` 后端选择、design-object / domain indicator 合约和 no-weighted-domain-output 边界，并继续禁止 R runtime smoke、weighted domain output、design-based confidence interval、校准和个体预测。
- NHANES public-use LMF R survey runtime smoke validation 是否存在，是否回到当前 readiness 契约 hash，是否 `PASS`，是否记录当前 smoke 状态；若为 `blocked-no-rscript`，必须继续禁止 weighted domain output、design-based confidence interval、校准和个体预测。
- NHANES public-use LMF domain indicator diagnostic validation 是否存在，是否回到当前 diagnostic 契约 hash，是否 `PASS`，是否只证明 sex × ageBand 公开聚合域组合覆盖、domain indicator metadata gate 和 no-row/no-count/no-weighted-output 边界，并继续禁止 weighted domain output、design-based confidence interval、校准和个体预测。
- NHANES public-use LMF DOF/sparse-domain diagnostic validation 是否存在，是否回到当前 diagnostic 契约 hash，是否 `PASS`，是否只证明 8 个 sex × ageBand 公开聚合域的 DOF/sparse metadata、minimum observed domain df = 15、0 个 lonely represented strata、0 个 empty domains、0 个 configured sparse-domain flags 和 no-row/no-count/no-weighted-output 边界，并继续禁止 public weighted-domain output、design-based confidence interval、校准和个体预测。
- NHANES public-use LMF disclosure output envelope validation 是否存在，是否回到当前 policy / test-case hash，是否 `PASS`，是否只证明 synthetic output envelope 2 allow / 6 block、small-cell / low-DOF / forbidden key / forbidden output type 阻断边界，并继续禁止真实 public weighted-domain output、design-based confidence interval、校准和个体预测。
- NHANES public-use LMF effective sample / CI publication validation 是否存在，是否回到当前 policy / test-case hash，是否 `PASS`，是否只证明 synthetic publication criteria 2 allow / 7 block、effective sample / CI width / RSE / DOF / real CI / forbidden output type 阻断边界，并继续禁止真实 public weighted-domain output、design-based confidence interval、校准和个体预测。
- NHANES public-use LMF weighted-output implementation preflight validation 是否存在，是否回到当前 policy / test-case hash，是否 `PASS`，是否只证明 synthetic implementation preflight 2 allow / 6 block、R `survey` / `svydesign` / `survey::subset` estimator-plan、row-drop-before-design / row persistence / real output / public AI / individual output 阻断边界，并继续禁止真实 public weighted-domain output、design-based confidence interval、校准和个体预测。
- NHANES public-use LMF disclosure review template validation 是否存在，是否回到当前 template hash，是否 `PASS`，是否只证明 15 个 disclosure review slots 已登记且全部 pending，并继续禁止真实 public weighted-domain output、design-based confidence interval、校准和个体预测。
- NHANES public-use LMF weighted-domain output readiness validation 是否存在，是否回到当前 readiness 契约 hash，是否 `PASS`，是否只证明 controlled runtime smoke、domain indicator metadata diagnostic、DOF/sparse metadata diagnostic、synthetic disclosure envelope、synthetic publication criteria、synthetic implementation preflight 和 disclosure review template gates 已登记，其中真实 disclosure review 与 output implementation 仍为 blocked，并继续禁止 public weighted-domain output、design-based confidence interval、校准和个体预测。
- NHANES public-use LMF local run evidence manifest validation 是否存在，是否回到当前 manifest hash，是否 `PASS`，是否只证明 ignored 本地 weighted-domain run / local disclosure packet / packet-validation 的哈希、运行环境、8 个审计 cells、minimum DOF 15、0 个 human-reviewed slots、tracked values omitted 和 public output blocked 边界，并继续禁止版本化真实 rates、standard errors、design-based intervals、公开输出、校准和个体预测。
- NHANES public-use LMF public-output implementation review template / execution validation 是否存在，是否 `PASS`，是否只证明 12 个 implementation review 槽位已登记且仍全部 pending、0 个 human-reviewed slots、无 reviewed artifact hash、无 second reviewer signoff、无 final implementation decision，并继续禁止 public weighted-domain output、calibration 和 individual prediction。
- NHANES public-use LMF public release gate validation 是否存在，是否 `PASS`，是否只汇合 disclosure review execution、public Web no-real-values scan、local-run evidence manifest、weighted-domain readiness、public-output implementation review template 和 public-output implementation review execution register，并保持 `blocked-pending-human-disclosure-review`、public weighted-domain output blocked、calibration blocked 和 individual prediction blocked。
- NHANES public-use LMF public Web data no-real-values validation 是否存在，是否 `PASS`，是否扫描 `web/src/data/life-path-nhanes-public-lmf-*.json` 并证明公开前端 JSON 不含真实 weighted rates、standard errors、confidence intervals、行级字段、个体预测字段或越界 release/calibration flags。
- NHATS controlled storage/destruction plan / validation 是否存在，是否回到当前 plan 和 acquisition-readiness hash，是否 `PASS`，是否只把 storage-destruction gate 升到 partial，并继续阻止工作区未执行状态下的下载、抽取、raw data 入库、public AI 上传、校准和个体预测。
- NHATS synthetic storage/destruction drill / validation 是否存在，是否回到当前 drill、plan 和 acquisition-readiness hash，是否 `PASS`，是否只证明 synthetic create-hash-delete 演练完成，并继续阻止下载、抽取、raw data 入库、public AI 上传、校准和个体预测。
- NHATS file-tier table / validation 是否存在，是否覆盖 R13/R14 annual public files、clock drawing images、sensitive SP/OP files 和 R13 seasonality weights，是否记录 access tier、官方路径、候选用途、方法文档依赖，是否回到当前 table/upstream hash 并 `PASS`，并继续禁止下载、抽取、raw data 入库、public AI 上传、校准和个体预测。
- NHATS first estimand protocol 是否存在，是否预注册 R13/R14 cohort-level functional-survival 研究问题、target population、time zero、outcome、predictor family、censoring/missingness、survey design、readiness gates、aggregate-only 输出边界，并继续禁止下载、抽取、校准、验证和个体预测。
- NHATS variable confirmation matrix 是否存在，是否记录 Colectica/codebook 字段真相源、User Guide 变量命名/缺失码线索、Technical Paper 55 权重/方差线索、R13/R14 候选字段模式、变量组、cohort-flow 模板、readiness gates、禁止动作和官方来源追踪，并继续阻止从候选字段直接写抽取脚本。
- NHATS cohort-flow endpoint-routing protocol 是否存在，是否记录 R13/R14 队列流转行、R14 终点路由类、aggregate-only 输出契约、n < 5 披露控制、readiness gates、禁止动作和官方来源追踪，并继续阻止下载、抽取、公开导出、校准和个体预测。
- NHATS disclosure-control policy 是否存在，是否记录 aggregate-only、n < 5 suppression、row-level block、public AI block、允许输出类型、禁止输出类型和官方来源追踪，并继续阻止真实 public export、校准和个体预测。
- NHATS disclosure-control synthetic test cases 是否存在，是否覆盖 allow-export 与 block-export、small-cell unsuppressed、small-cell suppressed、row-level leak、public AI upload 和 forbidden output type。
- NHATS disclosure-control validation 是否存在，是否回到当前 policy/test-case hash，是否 `PASS`，是否 6 个合成用例全通过，并保留 synthetic-only、no-real-data、no-calibration 和 no-individual-prediction 边界。
- NHATS survey-design protocol / test cases / validation 是否存在，是否回到当前 protocol/test-case hash，是否 `PASS`，是否覆盖权重、分层、PSU/variance unit、方差方法、domain rule、route-map、round linkage 和 disclosure prerequisites，并继续保留 synthetic-only、no-real-data、no-calibration 和 no-individual-prediction 边界。
- NHATS missingness-route protocol / test cases / validation 是否存在，是否回到当前 protocol/test-case hash，是否 `PASS`，是否覆盖 alive self、alive proxy、alive facility/residential、death boundary、missing/nonresponse、not-classifiable、small-cell suppression、alive/death 冲突和禁止 missingness-as-outcome 边界。
- NHATS route-field discovery register / validation 是否存在，是否回到当前 register hash，是否 `PASS`，是否记录官方 R13/R14 crosswalk 字段候选、Colectica value-labels-pending 状态、sensitive death-date exclusion、阻塞门、source evidence 和禁止真实 route classification / weighted route counts / public AI / individual prediction 边界。
- NHATS Colectica value-label review protocol / validation 是否存在，是否回到当前 protocol hash，是否 `PASS`，是否记录 source evidence、review artifact requirements、route-field review units、blocking gates、sensitive death-date exclusion、no confirmed value-label map，并继续阻止 route classifier、endpoint classification、weighted route counts、public export、calibration 和 individual prediction。
- NHATS Colectica value-label review execution register / validation 是否存在，是否回到当前 execution register、protocol 和 route-field discovery hash，是否 `PASS`，是否只打开官方来源追踪、字段级 source-trace 骨架和 standard negative-code family 边界，并继续阻止 Colectica 登录、value labels、question text、skip logic、route-value map、classifier、weighted counts、public export、calibration 和 individual prediction。
- NHATS Colectica access-route probe register / validation 是否存在，是否回到当前 probe register 和 execution register hash，是否 `PASS`，是否包含 2026-07-04 anonymous live reprobe 和 technical guide freshness probe，是否只证明官方 Cross-Year Search 入口、匿名访问登录页边界、技术指南 workflow 和受控 capture sequence，并继续阻止账号、登录、变量页捕获、value labels、question text、exports、calibration 和 individual prediction。
- NHATS Colectica authenticated capture template / validation 是否存在，是否回到当前 template、probe register、execution register、protocol 和 route-field discovery hash，是否 `PASS`，是否只证明受控登录后变量页捕获槽、敏感死亡字段排除、source hash 要求和二次复核门已固定，并继续阻止账号状态、登录、变量页实捕获、value labels、question text、universe/skip logic、route classifier、公开导出、校准和 individual prediction。
- NHATS route-value crosswalk assembly protocol / validation 是否存在，是否回到当前 protocol、capture task、capture-packet review execution、value-label execution 和 route-classifier readiness hash，是否 `PASS`，是否只证明 9 个 assembly units、敏感 death-date 排除和全部 0 准入状态，并继续阻止 route-value rows、变量级 missing-code maps、slot closure、真实 route classifier、真实提取、公开导出、校准和 individual prediction。
- NHATS route-value crosswalk entry validator / validation 是否存在，是否回到当前 test cases、assembly protocol、capture-packet review execution、capture task 和 route-classifier readiness hash，是否 `PASS`，是否只证明 1 个 reviewable-but-still-blocked、1 个 cannot-evaluate 和 4 个 rejected 的 future entry 预检语义，并继续阻止真实 route-value rows、变量级 missing-code maps、slot closure、route classifier、真实提取、公开导出、校准和 individual prediction。
- NHATS route-classifier synthetic dry-run 是否能由 `make nhats-route-classifier-synthetic-dry-run-audit` 同时生成 ignored 详细报告和 tracked Web validation summary，是否只验证 8 个 synthetic route envelope cases 的 allow/block 分类逻辑，是否被总 toy model audit 消费，并继续阻止真实 route classifier、真实提取、加权统计、公开导出、校准和 individual prediction。
- NHATS route-classifier readiness contract / validation 是否存在，是否回到当前 route-field discovery、Colectica execution、authenticated capture、missingness-route 和 pre-outcome aggregation hash，是否 `PASS`，是否只把 9 个分类器输入族和 12 个晋升门机器化，并继续阻止真实 route classifier、抽取、真实聚合、weighted counts、校准和 individual prediction。
- NHATS L2 variable-family admission register / validation 是否存在，是否回到当前 first estimand、变量确认矩阵、模型准入契约、候选注册表和 capture template hash，是否 `PASS`，是否只把 6 个候选变量族固定为 L2-only，并继续阻止精确字段确认、真实提取、route classification、校准、L4 admission 和 individual prediction。
- NHATS pre-outcome aggregation protocol / validation 是否存在，是否回到当前 L2 准入、变量确认、cohort-flow、survey-design 和 disclosure source hash，是否 `PASS`，是否只冻结 8 条 L2-only 聚合规则和 7 个 synthetic allow/block cases，并继续阻止真实聚合、weighted aggregation、L4 admission、calibration 和 individual prediction。

## 参考入口

- Stanford Encyclopedia of Philosophy, Capability Approach: https://plato.stanford.edu/entries/capability-approach/
- WHO Constitution: https://www.who.int/about/governance/constitution
- MRC framework for complex interventions: https://www.bmj.com/content/374/bmj.n2061
- TRIPOD statement: https://www.tripod-statement.org/
- PROBAST: https://www.probast.org/
- ISPOR Good Practices Reports: https://www.ispor.org/heor-resources/good-practices
- DYNAMO-HIA: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0033317
- Future Elderly Model: https://schaeffer.usc.edu/data/future-elderly-model/
- OHDSI Patient-Level Prediction: https://www.ohdsi.org/web/wiki/doku.php?id=projects:workgroups:patient-level_prediction
- WHO HALE metadata: https://www.who.int/data/gho/indicator-metadata-registry/imr-details/7752
