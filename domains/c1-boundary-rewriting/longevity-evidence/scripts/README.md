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
- `run_life_path_toy_model.py`：读取 `data/manual/life_path_toy_model_scenarios.json`，导出 `web/src/data/life-path-toy-model.json` 供 `/model/` 展示。
- `run_life_path_sensitivity_analysis.py`：读取同一组合成场景和已生成 toy model，导出 `web/src/data/life-path-sensitivity-analysis.json`，用于检查风险倍率、健康质量位移、能力倍率、主观时间、LEV 进度和尾部风险扰动下的场景稳定性。
- `audit_life_path_toy_model.py`：审计 `web/src/data/life-path-toy-model.json`、`web/src/data/life-path-sensitivity-analysis.json`、`data/manual/life_path_calibration_readiness.json`、`data/manual/life_path_data_source_candidates.json`、`data/manual/life_path_nhats_acquisition_readiness.json`、`data/manual/life_path_nhats_file_tier_table.json`、`data/manual/life_path_nhats_first_estimand_protocol.json`、`data/manual/life_path_nhats_variable_confirmation_matrix.json`、`docs/life-path-data-source-cards.md`、`docs/life-path-data-card-template.md`、`docs/life-path-data-card-nhats.md`、`docs/life-path-variable-dictionary-nhats.md` 和 `docs/life-path-extraction-manifest-nhats-draft.md`，并导出 `web/src/data/life-path-toy-model-audit.json` / `.md`。

运行示例：

```bash
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/collect_mvp_data.py --limit 10
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/collect_core_data.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/run_life_path_toy_model.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/run_life_path_sensitivity_analysis.py
python3 domains/c1-boundary-rewriting/longevity-evidence/scripts/audit_life_path_toy_model.py
```
