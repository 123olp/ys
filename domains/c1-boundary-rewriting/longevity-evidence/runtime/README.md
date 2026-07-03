# Longevity Evidence Runtime

本目录只保存可复现运行环境的轻量配置，不保存实际环境、下载包或行级数据。

## NHANES Public LMF R Survey Runtime

`nhanes-public-lmf-r-survey-conda.yml` 固定 NHANES public-use LMF R `survey` synthetic smoke 所需的最小运行时：

- R `4.3.3`
- R package `survey` `4.4`
- channel: `conda-forge`

默认本地环境路径由脚本创建在仓库根目录 `.runtime/nhanes-r-survey/`，该目录已被 `.gitignore` 排除。该 runtime 只用于 synthetic `svydesign` / domain `subset` smoke，不下载、不保存、不处理 NHANES public-use 行级数据，不授权 weighted domain output、design-based interval、校准或个体预测。

运行入口：

```bash
domains/c1-boundary-rewriting/longevity-evidence/scripts/run_nhanes_public_lmf_r_survey_controlled_runtime_smoke.sh
```

可用 `HUMAN_INFRA_R_SURVEY_ENV_PREFIX` 指向其他 conda prefix，用 `HUMAN_INFRA_R_SURVEY_SMOKE_OUT` 指向输出 JSON。
