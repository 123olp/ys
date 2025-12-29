# 湿件工程 (Wetware Engineering)

> 把生命能力从个体中解耦为可复用模块，用软件工程范式重构生命系统。

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![Markdown Lint](https://github.com/tukuaiai/wetware-engineering/actions/workflows/lint.yml/badge.svg)](https://github.com/tukuaiai/wetware-engineering/actions/workflows/lint.yml)

## 📖 项目概览

**湿件工程**（Wetware Engineering）是一个跨学科方法论框架，旨在将软件工程的核心抽象——模块化、接口标准化、依赖管理、运行时编排——系统性地迁移到生物系统构建领域。

### 核心理念

这不是"用软件运行生物"，而是**用编程范式重构生命系统**：

- 将器官、组织、执行器、传感器视为可组合的"生物组件"（Bio-Component）
- 定义标准化接口（Bio-Interface）实现组件间的即插即用
- 使用领域特定语言（Bio-DSL）声明式描述系统组合
- 通过运行时系统（Bio-Runtime）进行资源调度和监控

### 适用场景

- 组织工程与器官芯片研究
- 生物混合机器人开发
- 合成生物学系统设计
- 再生医学与器官替代
- 跨学科生物系统教育

## ✨ 功能特性

| 特性 | 说明 |
|-----|------|
| **Bio-Component Spec** | 标准化生物模块描述规范（v0.1） |
| **Bio-DSL** | 声明式系统组合语言 |
| **Component-Interface-Runtime 三元组** | 模块化生物系统的基础抽象 |
| **中英双语文档** | 完整的概念、宣言、技术规范文档 |
| **学术论文** | 13页 arXiv 格式预印本 |

## 🚀 快速开始

### 环境要求

- Git
- Markdown 阅读器（VS Code、Typora 等）
- （可选）Node.js 18+（用于 Markdown lint）
- （可选）TeX Live（用于编译论文）

### 获取项目

```bash
# 克隆仓库
git clone https://github.com/tukuaiai/wetware-engineering.git
cd wetware-engineering

# 查看文档结构
ls -la i18n/zh/
ls -la i18n/en/
```

### 阅读文档

**推荐阅读顺序：**

1. [快速入门指南](i18n/zh/湿件工程快速入门指南.md) - 5分钟理解核心概念
2. [湿件工程](i18n/zh/湿件工程.md) - 完整概念介绍
3. [技术规范](i18n/zh/湿件工程技术规范.md) - Bio-Component Spec & Bio-DSL 详解
4. [宣言](i18n/zh/湿件工程宣言.md) - 愿景与原则

### Bio-DSL 示例

```biodsl
// 定义组件
COMPONENT muscle FROM "muscle-actuator-human-skeletal@^2.3"
COMPONENT sensor FROM "piezo-force-sensor@~1.1"
COMPONENT controller FROM "neural-organoid-spinal@>=0.8"

// 连接组件
CONNECT sensor.output TO controller.input
CONNECT controller.output TO muscle.stimulation

// 运行时配置
RUNTIME {
  perfusion: { temperature: 37 C, flow_rate: 0.5 mL/min },
  control: { mode: "closed_loop" }
}
```

## 📚 文档索引

### 湿件工程核心文档

| 中文 | English | 说明 |
|-----|---------|------|
| [快速入门指南](i18n/zh/湿件工程快速入门指南.md) | [Quick Start](i18n/en/wetware_engineering_quick_start.md) | 5分钟理解核心概念 |
| [傻子博士解读版本](i18n/zh/傻子博士解读版本.md) | - | 大白话版本，零门槛理解 |
| [湿件工程](i18n/zh/湿件工程.md) | [Wetware Engineering](i18n/en/wetware_engineering.md) | 完整概念介绍 |
| [湿件工程宣言](i18n/zh/湿件工程宣言.md) | [Manifesto](i18n/en/wetware_engineering_manifesto.md) | 愿景与原则 |
| [技术规范](i18n/zh/湿件工程技术规范.md) | [Technical Spec](i18n/en/wetware_engineering_technical_spec.md) | Bio-Component Spec & Bio-DSL |

### 永生计划 (Immortality Project)

| 中文 | English | 说明 |
|-----|---------|------|
| [项目概述](i18n/zh/src/immortality/README.md) | [Overview](i18n/en/src/immortality/README.md) | 项目介绍 |
| [Human 3.0 架构](i18n/zh/src/immortality/docs/core/human_3.0_architecture.md) | [Architecture](i18n/en/src/immortality/docs/core/human_3.0_architecture.md) | 技术架构 |
| [27要素](i18n/zh/src/immortality/docs/core/immortality_27_elements.md) | [27 Elements](i18n/en/src/immortality/docs/core/immortality_27_elements.md) | 永生27要素 |
| [技术蓝图](i18n/zh/src/immortality/docs/core/human_3.0_technical_blueprint.md) | [Blueprint](i18n/en/src/immortality/human_3.0_technical_blueprint.md) | 实施路线 |

### 📄 学术论文

| 文档 | 说明 |
|------|------|
| [预印本 PDF](paper/arxiv/wetware_engineering.pdf) | 完整论文（13页，arXiv 格式） |
| [LaTeX 源码](paper/arxiv/wetware_engineering.tex) | 用于 arXiv 投稿 |
| [Markdown 草稿](paper/wetware_engineering_full_paper.md) | 完整草稿（约9000词） |

## 🎯 核心概念

### Component-Interface-Runtime 三元组

```
┌─────────────────────────────────────────────────────────┐
│                   Wetware Engineering                    │
├─────────────────────────────────────────────────────────┤
│  Component        │  Interface      │  Runtime          │
│  (生物模块)        │  (生物接口)      │  (编排系统)        │
├───────────────────┼─────────────────┼───────────────────┤
│  • Actuator 执行器 │  • Power 供能    │  • Scheduling     │
│  • Sensor 传感器   │  • Signal 信号   │  • Resource Mgmt  │
│  • Processor 处理器│  • Isolation 隔离│  • Monitoring     │
│  • Metabolic 代谢  │  • Mechanical 机械│  • Fault Isolation│
└───────────────────┴─────────────────┴───────────────────┘
```

### 软件工程概念映射

| 软件工程 | 湿件工程 | 说明 |
|---------|---------|------|
| Package Manager | Bio-Registry | 组件注册与发现 |
| Semantic Versioning | Bio-Versioning | `muscle@2.3.1` |
| API Contract | Bio-Interface | 输入/输出规范 |
| Unit Test | Viability Test | 组件功能验证 |
| Container | Perfusion System | 生命支持环境 |

## 📁 目录结构

```
wetware-engineering/
├── README.md                        # 本文件 - 项目主页
├── AGENTS.md                        # AI Agent 操作手册
├── Makefile                         # 常用命令（lint/paper/clean/backup）
├── metadata.yaml                    # 项目元数据
├── LICENSE                          # CC BY-SA 4.0 许可证
├── CONTRIBUTING.md                  # 贡献指南
├── CODE_OF_CONDUCT.md               # 行为准则
│
├── i18n/                            # 国际化文档
│   ├── zh/                          # 中文文档
│   │   ├── README.md                # 中文索引
│   │   ├── 湿件工程.md              # 核心概念
│   │   ├── 湿件工程宣言.md          # 宣言
│   │   ├── 湿件工程技术规范.md      # 技术规范
│   │   ├── 湿件工程快速入门指南.md  # 快速入门
│   │   └── src/immortality/         # 永生计划（中文）
│   │       ├── README.md
│   │       ├── docs/core/           # 核心文档
│   │       ├── docs/philosophy/     # 哲学探讨
│   │       └── docs/guides/         # 指南
│   │
│   └── en/                          # English docs
│       ├── README.md
│       ├── wetware_engineering.md
│       ├── wetware_engineering_manifesto.md
│       ├── wetware_engineering_technical_spec.md
│       ├── wetware_engineering_quick_start.md
│       └── src/immortality/         # Immortality Project
│
├── paper/                           # 学术论文
│   ├── arxiv/                       # arXiv 投稿版本
│   │   ├── wetware_engineering.tex  # LaTeX 源码
│   │   ├── wetware_engineering.pdf  # 编译后 PDF（13页）
│   │   ├── arxiv.sty                # arXiv 样式文件
│   │   └── orcid.pdf                # ORCID 图标
│   ├── sections/                    # 论文章节（Markdown）
│   └── wetware_engineering_full_paper.md  # 完整草稿
│
└── .github/
    ├── workflows/lint.yml           # Markdown lint CI
    ├── ISSUE_TEMPLATE/              # Issue 模板
    │   ├── bug_report.md
    │   └── feature_request.md
    └── PULL_REQUEST_TEMPLATE.md     # PR 模板
```

## ⚙️ 常用命令

| 命令 | 说明 |
|------|------|
| `find i18n -name "*.md"` | 列出所有文档文件 |
| `npx markdownlint-cli2 "**/*.md"` | 检查 Markdown 格式 |
| `cd paper/arxiv && xelatex wetware_engineering.tex` | 编译 LaTeX 论文 |
| `python backups/快速备份.py` | 执行项目备份 |

## 🗺️ 项目路线图

### 已完成 ✅

- [x] 核心概念定义
- [x] Bio-Component Spec v0.1 草案
- [x] Bio-DSL 语法草案
- [x] 中文文档（完整）
- [x] 英文文档（完整）
- [x] 永生计划文档（中英双语）
- [x] 学术论文预印本（13页）

### 进行中 🚧

- [ ] arXiv 投稿

### 计划中 📋

- [ ] 参考实现（Python/TypeScript）
- [ ] Bio-DSL 解析器
- [ ] 组件注册中心原型
- [ ] 可视化编辑器

## 🤝 参与贡献

我们欢迎各种形式的贡献！

### 贡献方式

1. **文档改进**：修复错误、改进表述、添加示例
2. **翻译**：帮助翻译到其他语言
3. **概念讨论**：在 Issues 中提出想法和建议
4. **技术实现**：参与参考实现开发

### 贡献流程

```bash
# 1. Fork 仓库
# 2. 创建分支
git checkout -b docs/your-improvement

# 3. 进行修改并提交
git commit -m "docs: your description"

# 4. 推送并创建 PR
git push origin docs/your-improvement
```

详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## ❓ 常见问题

### Q: 湿件工程和合成生物学有什么区别？

**A**: 合成生物学主要在基因/分子层面操作（如 BioBricks），湿件工程在器官/系统层面操作。两者是互补的：合成生物学定义组件内部，湿件工程定义组件如何组合。

### Q: Bio-DSL 可以实际运行吗？

**A**: 目前 Bio-DSL 是概念性规范，尚无运行时实现。它的价值在于提供标准化的系统描述语言，为未来的工具链奠定基础。

### Q: 这个项目的实际应用是什么？

**A**: 短期目标是建立概念框架和标准规范；中期目标是开发工具链；长期目标是实现可复用、可组合的生物系统工程。

## 📄 许可证

本项目采用 [CC BY-SA 4.0](LICENSE) 许可证。

- ✅ 可自由分享和改编
- ✅ 需注明出处
- ✅ 需以相同许可证分享

## 🔗 相关链接

- **GitHub**: https://github.com/tukuaiai/wetware-engineering
- **作者 ORCID**: [0009-0009-6523-1823](https://orcid.org/0009-0009-6523-1823)

### 🤖 AI 解读

- **ZRead AI**: [zread.ai/tukuaiai/wetware-engineering](https://zread.ai/tukuaiai/wetware-engineering) - AI 驱动的仓库解读
- **NotebookLM**: [Google NotebookLM 笔记本](https://notebooklm.google.com/notebook/11e804ff-ae6f-4b27-b2f0-e94c2e98ce3a) - AI 辅助学习笔记

---

<p align="center">
  <strong>湿件工程：编程生命系统的未来</strong> 🧬💻
</p>
