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
    └── check.yml             # 依赖安装前的历史隐私预检与仓库研究契约门禁
```

## 职责边界

- `ISSUE_TEMPLATE/` 只定义协作入口，不承载长期知识结论。
- `PULL_REQUEST_TEMPLATE.md` 负责让变更说明包含范围、验证和风险。
- `workflows/check.yml` 使用固定提交的官方 Action、只读权限、完整历史和非持久化 checkout 凭据；在安装项目依赖前以 CI 脱敏模式扫描当前树、可达历史、提交身份与工作流策略，再运行 `make check` 执行本地负例、历史年表和仓库研究契约门禁。
- 隐私失败日志只能输出规则名、数量和不可逆 `location_id`，不得回显命中值、作者身份、相对路径、提交消息或环境变量。
- Research Narrative 的历史 Pages 工作流已移入 `archive/retired-research-narrative-site/pages.yml`，禁止恢复或执行。
- 新增远程自动化时，优先复用 `Makefile` 或 `tools/` 中的本地命令，避免本地和 CI 出现两套真相。
