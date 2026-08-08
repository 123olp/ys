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
    └── check.yml             # 隐私、仓库结构与研究契约门禁
```

## 职责边界

- `ISSUE_TEMPLATE/` 只定义协作入口，不承载长期知识结论。
- `PULL_REQUEST_TEMPLATE.md` 负责让变更说明包含范围、验证和风险。
- `workflows/check.yml` 运行 `make check`，由同一入口执行隐私泄露、历史年表和仓库研究契约门禁；同时阻止已退役的 Research Narrative 页面、Astro 配置、Wrangler 配置和 Pages 工作流返回活动路径。
- Research Narrative 的历史 Pages 工作流已移入 `archive/retired-research-narrative-site/pages.yml`，禁止恢复或执行。
- 新增远程自动化时，优先复用 `Makefile` 或 `tools/` 中的本地命令，避免本地和 CI 出现两套真相。
