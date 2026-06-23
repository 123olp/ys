# Human Infra

Human Infra 是一个以“人类作为任务执行系统”为中心的基础设施研究与产品化项目。

它把人类表现从“意志、自律、天赋”的单点解释，重构为一套可诊断、可设计、可维护、可恢复的运行系统：生理、认知、情绪、环境、工具、资源、时间、反馈和恢复共同决定人能否长期稳定地完成复杂任务。

一句话定位：

> Human Infra 研究和构建支持人类长期执行、创造、判断与生活的运行基础设施。

## 核心边界

Human Infra 不是效率鸡汤，也不是把人压榨成机器的管理系统。它的首要目标是保护人的长期能动性、健康、创造力、自由度和尊严。

项目当前分成四类材料：

- `docs/`：Human Infra 的总理论、域地图、伦理边界和原始资料归档。
- `domains/longevity-evidence/`：原 Biocat 长寿证据账本，负责公开证据、临床试验、安全风险和数据采集。
- `domains/future-waiting/`：未来等待路径，负责黑洞等待室等“压缩等待 / 去未来”思想实验和边界。
- `domains/disembodied-cns/`：去具身外部维持型中枢生命系统研究域，负责“脑/中枢神经系统脱离自然身体后的生命支持与接口架构”概念建模。
- `domains/memory-editing/`：记忆编辑研究域，负责记忆读写、人格连续性、安全验证和伦理边界的高层建模。

## 当前重组原则

- 总项目叫 Human Infra；Biocat 不再占据根目录，而是作为“生理与长寿证据基础设施”的子域存在。
- “永生”和“记忆编辑”不直接混进长寿干预证据页，而是拆成两个远期研究域：`disembodied-cns` 和 `memory-editing`。
- 数据和采集脚本只属于 `longevity-evidence` 子域；它们不代表 Human Infra 的全部范围。
- 原始资料保留在 `docs/source-notes/`，综合后的稳定表述放在 `docs/` 和各 `domains/*/README.md`。

## 非目标

- 不提供医疗诊断、个性化用药建议或治疗方案推荐。
- 不宣称任何干预、系统或技术可以实现永生。
- 不提供侵入式神经操作、记忆操控或人体实验的可执行步骤。
- 不把人的状态监控变成组织压榨、控制或规训工具。
- 不用 AI 摘要替代原始证据、临床事实和人工审核。

## 目录

```text
human_infra/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
├── .editorconfig
├── .gitattributes
├── .gitignore
├── AGENTS.md
├── CHANGELOG.md
├── CITATION.cff
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── GOVERNANCE.md
├── LICENSE.md
├── Makefile
├── README.md
├── SECURITY.md
├── SUPPORT.md
├── docs/
│   ├── AGENTS.md
│   ├── README.md
│   ├── decisions/
│   ├── explanations/
│   ├── how-to/
│   ├── reference/
│   ├── source-notes/
│   └── tutorials/
├── domains/
    ├── AGENTS.md
    ├── disembodied-cns/
    │   ├── AGENTS.md
    │   └── README.md
    ├── future-waiting/
    │   ├── AGENTS.md
    │   ├── README.md
    │   └── paths/
    ├── longevity-evidence/
    │   ├── AGENTS.md
    │   ├── README.md
    │   ├── data/
    │   ├── docs/
    │   └── scripts/
    └── memory-editing/
        ├── AGENTS.md
        └── README.md
└── tools/
    ├── README.md
    └── check_repository.py
```

## 变更日志

- 2026-06-20：从 Biocat 单项目重组为 Human Infra 总项目；Biocat 迁入 `domains/longevity-evidence/`；新增去具身中枢生命系统与记忆编辑两个研究域；补齐 Docs-as-Code 知识仓库根文件、文档分层、协作模板和结构检查脚本。
- 2026-06-22：新增 `future-waiting` 子域和“黑洞等待室”未来等待路径。
