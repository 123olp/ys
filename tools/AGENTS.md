# tools 目录说明

`tools/` 保存仓库维护脚本和可迁移工程工具。这里的脚本不是产品运行时代码，默认从仓库根目录执行，也应尽量保持可复制到其他仓库使用。

## 目录结构

```text
tools/
├── AGENTS.md                         # 本目录架构说明
├── README.md                         # 工具入口和常用命令
├── audit_core_claim_evidence_matrix.py # 核心主张证据矩阵审计器
├── audit_human_infra_maturity_gap_register.py # 100% 成熟度缺口账本审计器
├── audit_human_infra_page_claim_consistency.py # 页面级 Claim ID 一致性审计器
├── audit_human_infra_paper_claim_register.py # arXiv-style 论文页强主张注册表审计器
├── audit_human_infra_domain_falsifier_coverage.py # C1/C2 优先域反证覆盖审计器
├── audit_human_infra_falsifier_source_card_backfill.py # 反证 Source Card 锚点回填审计器
├── arxiv_html_paper_tool.py          # arXiv HTML papers 复用 CLI
├── check_repository.py               # 仓库结构和 Markdown 链接检查
├── update_domain_doc_contracts.py     # 研究域 README/AGENTS 标准块、研究骨架和代理流程生成器
└── arxiv-html-paper/
    ├── AGENTS.md                     # arXiv 复用工具包说明
    ├── CHANGELOG.md                  # 工具包版本变更记录
    ├── CONSUMER_GUIDE.md             # 外部项目消费指南
    ├── CONTRACT.md                   # 人读稳定消费契约
    ├── GOVERNANCE.md                 # 维护治理与兼容规则
    ├── MAINTENANCE.md                # 镜像、资产、模板维护运行手册
    ├── README.md                     # 安装、校验、脚手架和文档入口
    ├── VERSION                       # 工具包版本
    ├── arxiv-html-paper.contract.v1.json # 机器可读消费契约
    ├── assets/                       # 小型补丁静态资源
    └── templates/
        ├── PaperReaderLayout.astro   # 论文阅读器布局模板
        └── paper.astro               # 最小论文页面骨架
```

## 职责边界

- `check_repository.py` 只检查仓库结构、临时文件名、Python 缓存和本地 Markdown 链接。
- `audit_core_claim_evidence_matrix.py` 只检查核心 Claim-Evidence Matrix 的结构契约、Source Anchor、Claim ID、gate、方法锚点、禁止用途和入口索引，不验证外部文献真实性。
- `audit_human_infra_maturity_gap_register.py` 只检查 100% 成熟度缺口账本的结构契约、三条成熟度轴、gate 状态、证据路径、路线图百分比一致性和入口索引，不证明项目已经完成 100%。
- `audit_human_infra_page_claim_consistency.py` 只检查主要 README、Web、论文和 reference 页面是否包含账本要求的 Claim ID、Claim spine 标签和禁止用途边界，不验证外部文献真实性或域级证据闭环。
- `audit_human_infra_paper_claim_register.py` 只检查 arXiv-style 论文页是否全部进入论文强主张注册表，并具备强主张、核心 Claim ID、反证条件、降级动作、source data path 和禁止用途边界；它不证明论文主张为真，也不验证外部文献真实性。
- `audit_human_infra_domain_falsifier_coverage.py` 只检查 C1 和当前 20 个优先 C2 研究域是否具备强主张、变量接口、反证条件、降级动作和禁止用途脚手架，不证明所有 C2 域、论文页或外部文献已经完成证据闭环。
- `audit_human_infra_falsifier_source_card_backfill.py` 只检查当前论文强主张和 C1/C2 优先域反证是否具备 Source Card 锚点、证据角色、可用范围和外推边界；它不证明外部文献正确，也不等于完成逐篇 Source Card 精读。
- `update_domain_doc_contracts.py` 只根据 `domains/_possibility-space-control/classification.tsv` 为正式研究域 README/AGENTS 生成标准元信息、研究推进骨架、维护契约和代理执行流程块。
- `arxiv_html_paper_tool.py` 只负责 arXiv HTML papers 资源安装、资产校验、Astro 布局和页面骨架生成。
- `arxiv-html-paper/templates/` 保留可复制模板，不承载 Human Infra 正文理论。
- `arxiv-html-paper/CONTRACT.md` 和 `arxiv-html-paper/arxiv-html-paper.contract.v1.json` 是其他项目消费工具包的稳定契约。
- `arxiv-html-paper/CONSUMER_GUIDE.md`、`GOVERNANCE.md`、`MAINTENANCE.md` 分别服务外部消费、兼容治理和维护运行。
- 工具脚本应优先使用 Python 标准库；只有外部工具本身是任务对象时，才在文档中要求 `wget`、`monolith`、`LaTeXML` 等依赖。

## 维护规则

- 新增工具必须更新 `tools/README.md` 和本文件。
- 新增工具包目录必须有自己的 `AGENTS.md` 和 `README.md`。
- 工具默认不得写入个人数据、医疗数据或远程服务凭据。
- 面向全局复用的工具不得硬编码 Human Infra 正文内容；项目特有内容只能作为示例或调用参数存在。
- 修改可复用工具包的消费契约时，必须同步更新工具包 README、契约 JSON、CHANGELOG 和本文件。
