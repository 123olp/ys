# 脚本目录

这里放置 Longevity Evidence 子域的数据采集、清洗、校验和导出脚本。

## 规则

- 脚本必须可重复执行。
- 外部 API 调用必须设置超时、分页和速率限制。
- 原始数据保存到本子域的 `data/raw/`，清洗结果保存到本子域的 `data/processed/`。
- 医学判断和证据评分规则放在文档或配置中，不硬编码在采集脚本里。

## 当前脚本

- `collect_mvp_data.py`：采集首批干预的 PubMed、OpenAlex、ClinicalTrials.gov 和 openFDA 数据。
- `collect_core_data.py`：采集 HAGR、PubChem、openFDA 不良事件聚合和 Drugs@FDA 数据。
- `build_public_mortality_anchor.py`：从 NCHS 2021 U.S. Life Tables 官方 xlsx 表生成 `data/manual/life_path_public_mortality_anchor.json`，作为公开聚合死亡率基线锚点；它不接触个人数据，不证明校准预测。
- `validate_public_mortality_anchor.py`：离线审计 `data/manual/life_path_public_mortality_anchor.json` 的 schema、官方来源、年龄范围、sex-specific 表、qx/lx/ex 合理性和禁止个体预测边界。
- `validate_nhats_acquisition_readiness.py`：读取 `data/manual/life_path_nhats_acquisition_readiness.json`，导出 `web/src/data/life-path-nhats-acquisition-readiness-validation.json`，验证 10 个 acquisition-readiness gates 仍全部阻塞 extraction，并确认没有凭据、raw NHATS/NSOC 数据或个体死亡日期字段进入仓库。
- `validate_nhats_controlled_storage_destruction_plan.py`：读取 `data/manual/life_path_nhats_controlled_storage_destruction_plan.json`，导出 `web/src/data/life-path-nhats-controlled-storage-destruction-validation.json`，验证受控存储/销毁计划只处于 plan-only，继续阻塞 download、extraction、raw data 入库、public AI 上传、calibration 和 individual prediction。
- `validate_nhats_synthetic_storage_destruction_drill.py`：读取 `data/manual/life_path_nhats_synthetic_storage_destruction_drill.json`，导出 `web/src/data/life-path-nhats-synthetic-storage-destruction-drill-validation.json`，验证合成 create-hash-delete 演练已完成且仍不证明注册、受控工作区、下载、抽取、校准或个体预测。
- `run_life_path_toy_model.py`：读取 `data/manual/life_path_toy_model_scenarios.json`，导出 `web/src/data/life-path-toy-model.json` 供 `/model/` 展示。
- `run_life_path_sensitivity_analysis.py`：读取同一组合成场景和已生成 toy model，导出 `web/src/data/life-path-sensitivity-analysis.json`，用于检查风险倍率、健康质量位移、能力倍率、主观时间、LEV 进度和尾部风险扰动下的场景稳定性。
- `validate_nhats_disclosure_outputs.py`：读取 `data/manual/life_path_nhats_disclosure_control_policy.json` 和 `data/manual/life_path_nhats_disclosure_control_test_cases.json`，导出 `web/src/data/life-path-nhats-disclosure-control-validation.json`，验证 NHATS synthetic output envelope 是否满足 aggregate-only、n < 5 suppression、row-level block、public AI block 和 forbidden-output rules。
- `validate_nhats_survey_design_plan.py`：读取 `data/manual/life_path_nhats_survey_design_protocol.json` 和 `data/manual/life_path_nhats_survey_design_test_cases.json`，导出 `web/src/data/life-path-nhats-survey-design-validation.json`，验证 NHATS synthetic design-plan envelope 是否满足 analysis weight、strata、PSU/variance unit、variance method、domain rule、missingness route、round linkage 和 disclosure prerequisites。
- `validate_nhats_missingness_route_map.py`：读取 `data/manual/life_path_nhats_missingness_route_protocol.json` 和 `data/manual/life_path_nhats_missingness_route_test_cases.json`，导出 `web/src/data/life-path-nhats-missingness-route-validation.json`，验证 NHATS synthetic route envelope 是否区分 alive self、alive proxy、alive facility、death boundary、missing/nonresponse、not-classifiable 和 small-cell suppression。
- `validate_nhats_route_field_discovery.py`：读取 `data/manual/life_path_nhats_route_field_discovery_register.json`，导出 `web/src/data/life-path-nhats-route-field-discovery-validation.json`，验证官方 crosswalk 字段发现是否仍保持 Colectica、数据访问、分类器、加权统计、公开导出、校准和个体预测阻塞。
- `validate_nhats_colectica_value_label_protocol.py`：读取 `data/manual/life_path_nhats_colectica_value_label_review_protocol.json`，导出 `web/src/data/life-path-nhats-colectica-value-label-validation.json`，验证 NHATS Colectica value-label review protocol 是否仍保持 value-label、question-text、skip-logic、route crosswalk、classifier、weighted counts、public export、calibration 和 individual prediction 阻塞。
- `validate_nhats_colectica_value_label_review_execution.py`：读取 `data/manual/life_path_nhats_colectica_value_label_review_execution_register.json`，导出 `web/src/data/life-path-nhats-colectica-value-label-review-execution-validation.json`，验证第一轮执行登记只准备了官方来源追踪、字段级 source-trace 骨架和标准 negative missing-code family，仍阻塞 Colectica 登录、value labels、question text、skip logic、route-value map、classifier、weighted counts、public export、calibration 和 individual prediction。
- `validate_nhats_colectica_access_route_probe.py`：读取 `data/manual/life_path_nhats_colectica_access_route_probe_register.json`，导出 `web/src/data/life-path-nhats-colectica-access-route-probe-validation.json`，验证公开入口、匿名登录边界、技术指南 workflow 和受控 capture sequence 是否存在，同时保持账号、登录、变量页、value labels、导出、校准和 individual prediction 阻塞。
- `validate_nhats_colectica_authenticated_capture_template.py`：读取 `data/manual/life_path_nhats_colectica_authenticated_capture_template.json`，导出 `web/src/data/life-path-nhats-colectica-authenticated-capture-template-validation.json`，验证受控登录后变量页捕获模板是否包含 route-field 证据槽、敏感死亡字段排除、source hash、二次复核和模型准入阻塞边界；它不执行登录、不抓取变量页、不确认 value labels。
- `validate_nhats_l2_variable_family_admission.py`：读取 `data/manual/life_path_nhats_l2_variable_family_admission_register.json`，导出 `web/src/data/life-path-nhats-l2-variable-family-admission-validation.json`，验证 first estimand、变量确认矩阵、模型准入契约、候选注册表和 capture template 的 source hash，并确认 6 个变量族仍是 L2-only、L4/L5 blocked。
- `validate_nhats_preoutcome_aggregation_protocol.py`：读取 `data/manual/life_path_nhats_preoutcome_aggregation_protocol.json`，导出 `web/src/data/life-path-nhats-preoutcome-aggregation-validation.json`，验证 8 条 L2-only 预结果聚合规则、7 个合成用例、上游 source hash 和真实聚合 / 加权估计 / L4 准入 / 校准 / 个体预测阻塞边界。
- `audit_life_path_toy_model.py`：审计 `web/src/data/life-path-toy-model.json`、`web/src/data/life-path-sensitivity-analysis.json`、`web/src/data/life-path-nhats-acquisition-readiness-validation.json`、`web/src/data/life-path-nhats-controlled-storage-destruction-validation.json`、`web/src/data/life-path-nhats-synthetic-storage-destruction-drill-validation.json`、`web/src/data/life-path-nhats-disclosure-control-validation.json`、`web/src/data/life-path-nhats-survey-design-validation.json`、`web/src/data/life-path-nhats-missingness-route-validation.json`、`web/src/data/life-path-nhats-route-field-discovery-validation.json`、`web/src/data/life-path-nhats-colectica-value-label-validation.json`、`web/src/data/life-path-nhats-colectica-value-label-review-execution-validation.json`、`web/src/data/life-path-nhats-colectica-access-route-probe-validation.json`、`web/src/data/life-path-nhats-colectica-authenticated-capture-template-validation.json`、`web/src/data/life-path-nhats-l2-variable-family-admission-validation.json`、`web/src/data/life-path-nhats-preoutcome-aggregation-validation.json`、`data/manual/life_path_calibration_readiness.json`、`data/manual/life_path_data_source_candidates.json`、`data/manual/life_path_nhats_acquisition_readiness.json`、`data/manual/life_path_nhats_controlled_storage_destruction_plan.json`、`data/manual/life_path_nhats_synthetic_storage_destruction_drill.json`、`data/manual/life_path_nhats_file_tier_table.json`、`data/manual/life_path_nhats_first_estimand_protocol.json`、`data/manual/life_path_nhats_variable_confirmation_matrix.json`、`data/manual/life_path_nhats_cohort_flow_endpoint_protocol.json`、`data/manual/life_path_nhats_disclosure_control_policy.json`、`data/manual/life_path_nhats_disclosure_control_test_cases.json`、`data/manual/life_path_nhats_survey_design_protocol.json`、`data/manual/life_path_nhats_survey_design_test_cases.json`、`data/manual/life_path_nhats_missingness_route_protocol.json`、`data/manual/life_path_nhats_missingness_route_test_cases.json`、`data/manual/life_path_nhats_route_field_discovery_register.json`、`data/manual/life_path_nhats_colectica_value_label_review_protocol.json`、`data/manual/life_path_nhats_colectica_value_label_review_execution_register.json`、`data/manual/life_path_nhats_colectica_access_route_probe_register.json`、`data/manual/life_path_nhats_colectica_authenticated_capture_template.json`、`data/manual/life_path_nhats_l2_variable_family_admission_register.json`、`data/manual/life_path_nhats_preoutcome_aggregation_protocol.json`、`docs/life-path-data-source-cards.md`、`docs/life-path-data-card-template.md`、`docs/life-path-data-card-nhats.md`、`docs/life-path-variable-dictionary-nhats.md` 和 `docs/life-path-extraction-manifest-nhats-draft.md`，并导出 `web/src/data/life-path-toy-model-audit.json` / `.md`。

运行示例：

```bash
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/collect_mvp_data.py --limit 10
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/collect_core_data.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/build_public_mortality_anchor.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_public_mortality_anchor.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_acquisition_readiness.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_controlled_storage_destruction_plan.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_synthetic_storage_destruction_drill.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/run_life_path_toy_model.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/run_life_path_sensitivity_analysis.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_disclosure_outputs.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_survey_design_plan.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_missingness_route_map.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_route_field_discovery.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_colectica_value_label_protocol.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_colectica_value_label_review_execution.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_colectica_access_route_probe.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_colectica_authenticated_capture_template.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_l2_variable_family_admission.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_preoutcome_aggregation_protocol.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/audit_life_path_toy_model.py
```
