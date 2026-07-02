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
- `run_life_path_toy_model.py`：读取 `data/manual/life_path_toy_model_scenarios.json`，导出 `web/src/data/life-path-toy-model.json` 供 `/model/` 展示。
- `run_life_path_sensitivity_analysis.py`：读取同一组合成场景和已生成 toy model，导出 `web/src/data/life-path-sensitivity-analysis.json`，用于检查风险倍率、健康质量位移、能力倍率、主观时间、LEV 进度和尾部风险扰动下的场景稳定性。
- `validate_nhats_disclosure_outputs.py`：读取 `data/manual/life_path_nhats_disclosure_control_policy.json` 和 `data/manual/life_path_nhats_disclosure_control_test_cases.json`，导出 `web/src/data/life-path-nhats-disclosure-control-validation.json`，验证 NHATS synthetic output envelope 是否满足 aggregate-only、n < 5 suppression、row-level block、public AI block 和 forbidden-output rules。
- `validate_nhats_survey_design_plan.py`：读取 `data/manual/life_path_nhats_survey_design_protocol.json` 和 `data/manual/life_path_nhats_survey_design_test_cases.json`，导出 `web/src/data/life-path-nhats-survey-design-validation.json`，验证 NHATS synthetic design-plan envelope 是否满足 analysis weight、strata、PSU/variance unit、variance method、domain rule、missingness route、round linkage 和 disclosure prerequisites。
- `validate_nhats_missingness_route_map.py`：读取 `data/manual/life_path_nhats_missingness_route_protocol.json` 和 `data/manual/life_path_nhats_missingness_route_test_cases.json`，导出 `web/src/data/life-path-nhats-missingness-route-validation.json`，验证 NHATS synthetic route envelope 是否区分 alive self、alive proxy、alive facility、death boundary、missing/nonresponse、not-classifiable 和 small-cell suppression。
- `validate_nhats_route_field_discovery.py`：读取 `data/manual/life_path_nhats_route_field_discovery_register.json`，导出 `web/src/data/life-path-nhats-route-field-discovery-validation.json`，验证官方 crosswalk 字段发现是否仍保持 Colectica、数据访问、分类器、加权统计、公开导出、校准和个体预测阻塞。
- `validate_nhats_colectica_value_label_protocol.py`：读取 `data/manual/life_path_nhats_colectica_value_label_review_protocol.json`，导出 `web/src/data/life-path-nhats-colectica-value-label-validation.json`，验证 NHATS Colectica value-label review protocol 是否仍保持 value-label、question-text、skip-logic、route crosswalk、classifier、weighted counts、public export、calibration 和 individual prediction 阻塞。
- `audit_life_path_toy_model.py`：审计 `web/src/data/life-path-toy-model.json`、`web/src/data/life-path-sensitivity-analysis.json`、`web/src/data/life-path-nhats-disclosure-control-validation.json`、`web/src/data/life-path-nhats-survey-design-validation.json`、`web/src/data/life-path-nhats-missingness-route-validation.json`、`web/src/data/life-path-nhats-route-field-discovery-validation.json`、`web/src/data/life-path-nhats-colectica-value-label-validation.json`、`data/manual/life_path_calibration_readiness.json`、`data/manual/life_path_data_source_candidates.json`、`data/manual/life_path_nhats_acquisition_readiness.json`、`data/manual/life_path_nhats_file_tier_table.json`、`data/manual/life_path_nhats_first_estimand_protocol.json`、`data/manual/life_path_nhats_variable_confirmation_matrix.json`、`data/manual/life_path_nhats_cohort_flow_endpoint_protocol.json`、`data/manual/life_path_nhats_disclosure_control_policy.json`、`data/manual/life_path_nhats_disclosure_control_test_cases.json`、`data/manual/life_path_nhats_survey_design_protocol.json`、`data/manual/life_path_nhats_survey_design_test_cases.json`、`data/manual/life_path_nhats_missingness_route_protocol.json`、`data/manual/life_path_nhats_missingness_route_test_cases.json`、`data/manual/life_path_nhats_route_field_discovery_register.json`、`data/manual/life_path_nhats_colectica_value_label_review_protocol.json`、`docs/life-path-data-source-cards.md`、`docs/life-path-data-card-template.md`、`docs/life-path-data-card-nhats.md`、`docs/life-path-variable-dictionary-nhats.md` 和 `docs/life-path-extraction-manifest-nhats-draft.md`，并导出 `web/src/data/life-path-toy-model-audit.json` / `.md`。

运行示例：

```bash
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/collect_mvp_data.py --limit 10
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/collect_core_data.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/build_public_mortality_anchor.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_public_mortality_anchor.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/run_life_path_toy_model.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/run_life_path_sensitivity_analysis.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_disclosure_outputs.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_survey_design_plan.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_missingness_route_map.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_route_field_discovery.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_colectica_value_label_protocol.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/audit_life_path_toy_model.py
```
