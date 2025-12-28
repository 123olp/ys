# AGENTS.md

> AI Agent 操作手册 - Wetware Engineering 项目

## 1. Mission & Scope（目标与边界）

### 允许的操作
- 编辑/新增 `i18n/` 目录下的文档文件 (`.md`)
- 更新 README.md、AGENTS.md、CONTRIBUTING.md
- 添加新的 Bio-DSL 示例
- 修复文档中的错误链接和格式问题

### 禁止的操作
- 删除任何现有文档（除非明确要求）
- 修改 LICENSE 文件
- 修改 `.github/workflows/` 中的 CI 配置（除非明确要求）
- 在文档中编造技术细节或引用

### 敏感区域（修改需谨慎）
- `i18n/zh/湿件工程技术规范.md` - Bio-Component Spec 核心定义
- `i18n/*/src/immortality/` - 永生计划子项目

## 2. Golden Path（推荐执行路径）

```bash
# 1. 克隆仓库
git clone https://github.com/tukuaiai/wetware-engineering.git
cd wetware-engineering

# 2. 查看文档结构
ls -la i18n/zh/
ls -la i18n/en/

# 3. 编辑文档
# ... 进行修改 ...

# 4. 检查 Markdown 格式（本地可选）
# npx markdownlint-cli2 "**/*.md"

# 5. 提交更改
git add .
git commit -m "docs: <描述变更>"
git push
```

## 3. Must-Run Commands（必须执行的命令）

本项目为纯文档项目，无构建/测试命令。

| 场景 | 命令 | 说明 |
|-----|------|------|
| 查看结构 | `find i18n -name "*.md" \| head -20` | 列出文档文件 |
| 格式检查 | `npx markdownlint-cli2 "**/*.md"` | 可选，CI 会自动运行 |

## 4. Code Change Rules（修改约束）

### 文档编写原则
- 中文文档放 `i18n/zh/`，英文文档放 `i18n/en/`
- 永生计划文档放 `i18n/*/src/immortality/`
- 文件名使用中文（中文文档）或英文小写下划线（英文文档）

### 链接规则
- 使用相对路径链接
- 链接到其他文档时确保路径正确（注意 `src/` 层级）

### 禁止行为
- 不得随意重构目录结构
- 不得删除 `_academic.md` 后缀的学术版文档
- 不得修改 Bio-DSL 语法定义（除非明确要求）

## 5. Style & Quality（风格与质量标准）

### Markdown 规范
- 配置文件：`.markdownlint.json`
- 已禁用规则：MD013（行长度）、MD033（HTML）、MD041（首行标题）

### 命名约定
- 中文文档：`湿件工程*.md`
- 英文文档：`snake_case.md`
- 学术版后缀：`*_academic.md`

### 文档结构
- 每个文档必须有一级标题
- 使用适当的标题层级（不跳级）
- 代码块标注语言类型

## 6. Project Map（项目结构速览）

```
wetware-engineering/
├── README.md                    # 项目主页（双语）
├── AGENTS.md                    # 本文件 - AI Agent 指南
├── CONTRIBUTING.md              # 贡献指南
├── CODE_OF_CONDUCT.md           # 行为准则
├── LICENSE                      # CC BY-SA 4.0
│
├── i18n/zh/                     # 中文文档
│   ├── README.md                # 中文索引
│   ├── 湿件工程.md              # 核心概念
│   ├── 湿件工程宣言.md          # 宣言
│   ├── 湿件工程技术规范.md      # 技术规范（Bio-Component Spec + Bio-DSL）
│   ├── 湿件工程快速入门指南.md  # 快速入门
│   └── src/immortality/         # 永生计划（中文）
│       ├── README.md            # 项目概述
│       ├── AGENTS.md            # 子项目 Agent 指南
│       ├── docs/core/           # 核心文档
│       │   ├── human_3.0_architecture.md
│       │   ├── human_3.0_technical_blueprint.md
│       │   └── immortality_27_elements.md
│       ├── docs/philosophy/     # 哲学探讨
│       │   ├── emotion_modeling.md
│       │   └── ontology_experience_machine.md
│       ├── docs/guides/         # 指南
│       │   └── human_3.0_social_media.md
│       └── data/                # 数据模板
│           ├── health_tracking_template.yaml
│           └── refs/核心论文清单.md
│
├── i18n/en/                     # English docs
│   ├── README.md                # English index
│   └── src/immortality/         # Immortality Project (EN)
│       ├── README.md
│       ├── README_academic.md
│       ├── AGENTS.md
│       ├── human_3.0_technical_blueprint.md
│       ├── human_3.0_technical_blueprint_academic.md
│       └── immortality_roadmap.md
│
└── .github/
    ├── workflows/lint.yml       # Markdown lint CI
    ├── ISSUE_TEMPLATE/          # Issue 模板
    └── PULL_REQUEST_TEMPLATE.md # PR 模板
```

## 7. Common Pitfalls（常见坑）

| 问题 | 原因 | 解决方案 |
|-----|------|---------|
| 链接 404 | 路径缺少 `src/` | 检查实际文件位置 |
| CI lint 失败 | Markdown 格式问题 | 本地运行 `npx markdownlint-cli2` 检查 |
| 中文文件名乱码 | Git 配置问题 | 确保 `git config core.quotepath false` |

## 8. PR / Commit Rules（提交规则）

### Commit Message 格式
```
<type>: <description>

type: docs / fix / chore / refactor
```

示例：
- `docs: add Bio-DSL example for neural controller`
- `fix: correct link to immortality roadmap`
- `chore: update .gitignore`

### 分支策略
- 主分支：`main`
- 功能分支：`feature/<topic>` 或 `docs/<topic>`

### CI 触发
- Push 到任意分支的 `.md` 文件变更会触发 Markdown lint

## 9. Documentation Sync Rule（文档同步规则）

### 强制同步要求
任何以下变更必须同步更新 README.md 和 AGENTS.md：
- 目录结构变化
- 新增/删除文档文件
- 链接路径变更
- 工作流/CI 配置变更

### 不确定时
- 使用 `TODO: <需要确认的内容>` 标注
- 不允许猜测或编造

---

## Key Concepts（核心概念速查）

- **Bio-Component**: 可独立功能的生物模块单元（执行器/传感器/处理器/代谢单元）
- **Bio-Interface**: 标准化连接（供能/信号/隔离/机械）
- **Bio-DSL**: 描述组件组合的领域特定语言
- **Bio-Runtime**: 负责调度、资源管理、监控的编排系统

## Current Status（当前状态）

| 模块 | 状态 |
|-----|------|
| 核心概念 | ✅ 已定义 |
| Bio-Component Spec | ✅ v0.1 草案 |
| Bio-DSL 语法 | ✅ 草案完成 |
| 中文文档 | ✅ 完成 |
| 英文文档 | 🚧 部分完成（仅永生计划） |
| 参考实现 | 📋 计划中 |
