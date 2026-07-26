# web 目录说明

`web/` 是研究发布中间资产目录，不是 Web 应用。它只保存结构化研究数据。

## 职责

- `src/data/`：保存论文、模型和验证流程消费的结构化中间产物。
- `src/data/human-infra-quantitative-capability-ladder-validation.json`：保存定量能力分层审计结果，由仓库审计器维护。
- `src/data/human-infra-domain-to-model-bridge-validation.json`：保存研究域到模型桥接审计结果。
- `src/data/human-infra-research-standards-source-anchor-validation.json`：保存科研标准来源锚点审计结果。
- `src/data/life-path-l4-validation-calibration-report-execution-validation.json`：保存 L4 校准报告执行审计结果。

## 禁止边界

- 禁止创建页面、布局、样式、静态站点资源或路由。
- 禁止引入运行脚本、包管理配置、Astro、Wrangler、Pages 发布配置或静态构建产物。
- 禁止部署本目录。
- 任何公开展示必须进入科技树或 Wiki 的正式产品边界。
