# 研究发布中间资产

`web/` 现只保留结构化研究中间数据，名称是历史遗留路径。它不是网站，不包含脚本或页面路由，不可构建、不可预览、不可部署。

## 目录结构

```text
web/
├── AGENTS.md
├── README.md
└── src/data/  # 研究发布中间数据与验证结果
```

## 使用边界

- 数据只能由仓库 `tools/` 与各研究域的正式审计器生成和验证。
- `src/data/human-infra-quantitative-capability-ladder-validation.json` 保存定量能力分层审计结果，不是页面发布数据源。
- `src/data/human-infra-domain-to-model-bridge-validation.json` 保存研究域到模型桥接审计结果。
- `src/data/human-infra-research-standards-source-anchor-validation.json` 保存科研标准来源锚点审计结果。
- `src/data/life-path-l4-validation-calibration-report-execution-validation.json` 保存 L4 校准报告执行审计结果。
- 禁止新增 `src/pages/`、`astro.config.*`、`wrangler.*`、`dist/` 或任何部署工作流。
- 公开产品只允许来自科技树与 Wiki 的独立正式源码。
- 已退役网站位于 `archive/retired-research-narrative-site/`，禁止恢复。
