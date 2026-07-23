# GitHub 协作入口说明

`.github/` 承载远程协作入口和自动质量门禁。它不保存项目知识正文，只保存 GitHub 平台读取的模板与工作流。

## 目录结构

```text
.github/
├── AGENTS.md                 # 说明 GitHub 协作入口的职责边界
├── ISSUE_TEMPLATE/           # 结构化 issue 模板
│   ├── config.yml            # Issue 模板选择页配置
│   ├── data-pipeline.yml     # 数据采集与处理问题模板
│   ├── documentation.yml     # 文档修正模板
│   └── research-note.yml     # 研究资料补充模板
├── PULL_REQUEST_TEMPLATE.md  # PR 描述、验证和风险模板
└── workflows/
    ├── check.yml             # 仓库结构、Web 构建与 GEO 门禁
    └── pages.yml             # GitHub Pages 构建、审计与部署
```

## 职责边界

- `ISSUE_TEMPLATE/` 只定义协作入口，不承载长期知识结论。
- `PULL_REQUEST_TEMPLATE.md` 负责让变更说明包含范围、验证和风险。
- `workflows/check.yml` 并行运行 `make check` 与 `web/npm run audit:geo`，同时守住仓库结构和 Web 发布契约。
- `workflows/pages.yml` 只在 Web、分级真相源、成熟度账本或证据图消费的四个来源注册表变化时构建；部署前必须通过 GEO 审计，发布产物只来自 `web/dist/`。
- 新增远程自动化时，优先复用 `Makefile` 或 `tools/` 中的本地命令，避免本地和 CI 出现两套真相。
