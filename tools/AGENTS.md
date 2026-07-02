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
├── audit_human_infra_audience_claim_map.py # 受众-主张映射与邻近项目边界审计器
├── audit_human_infra_paper_claim_register.py # arXiv-style 论文页强主张注册表审计器
├── audit_human_infra_domain_falsifier_coverage.py # C1/C2 优先域反证覆盖审计器
├── audit_human_infra_domain_claim_evidence_matrix.py # 域级主张-证据矩阵审计器
├── audit_human_infra_domain_source_card_field_extraction.py # 域 Source Card 字段抽取审计器
├── audit_human_infra_c2_longtail_first_batch_source_extraction_register.py # C2-LT-B1 48/48 来源抽取试运行审计器
├── audit_human_infra_c2_longtail_first_batch_local_review_register.py # C2-LT-B1 本地来源语境复核审计器
├── audit_human_infra_c2_longtail_first_batch_independent_fresh_review_protocol.py # C2-LT-B1 独立 fresh review 协议审计器
├── audit_human_infra_c2_longtail_first_batch_independent_fresh_review_verdict_register.py # C2-LT-B1 独立 fresh review 判定审计器
├── audit_human_infra_c2_longtail_first_batch_reviewed_card_artifact_register.py # C2-LT-B1 reviewed artifact 审计器
├── audit_human_infra_domain_source_specific_extraction_queue.py # 域-来源深读队列审计器
├── audit_human_infra_domain_source_specific_extraction_register.py # 域-来源精读完成寄存器审计器
├── audit_human_infra_domain_source_card_promotion_queue.py # 域-来源卡片晋升队列审计器
├── audit_human_infra_source_context_local_review_register.py # 来源语境本地复核账本审计器
├── audit_human_infra_card_promotion_prep_register.py # 卡片晋升预注册账本审计器
├── audit_human_infra_independent_fresh_review_protocol.py # 独立 fresh review 协议审计器
├── audit_human_infra_independent_fresh_review_verdict_register.py # 独立 fresh review verdict 账本审计器
├── audit_human_infra_falsifier_source_card_backfill.py # 反证 Source Card 锚点回填审计器
├── audit_human_infra_falsifier_source_card_extraction.py # 反证 Source Card 字段级抽取审计器
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
- `audit_human_infra_audience_claim_map.py` 只检查受众-主张映射账本是否覆盖研究者、构建者、长寿读者、基础设施读者、治理审查者和模型开发者，并保留邻近项目边界、入口索引和禁止误读；它不证明传播效果或外部科学主张。
- `audit_human_infra_paper_claim_register.py` 只检查 arXiv-style 论文页是否全部进入论文强主张注册表，并具备强主张、核心 Claim ID、反证条件、降级动作、source data path 和禁止用途边界；它不证明论文主张为真，也不验证外部文献真实性。
- `audit_human_infra_domain_falsifier_coverage.py` 只检查 C1 和当前 20 个优先 C2 研究域是否具备强主张、变量接口、反证条件、降级动作和禁止用途脚手架，不证明所有 C2 域、论文页或外部文献已经完成证据闭环。
- `audit_human_infra_domain_claim_evidence_matrix.py` 只检查当前 26 个优先研究域是否通过域级矩阵连接到强主张、变量契约来源、反证来源和已抽取 Source Card ID；它不证明外部文献正确，也不等于完成逐条 endpoint / population / uncertainty Source Card 精读。
- `audit_human_infra_domain_source_card_field_extraction.py` 只检查当前 26 个优先研究域是否具备 endpoint 候选、population 槽位、uncertainty 槽位、transfer-boundary 槽位和下一步抽取动作；它不证明 source-specific endpoint、样本、人群、效应量或不确定性已经完成精读。
- `audit_human_infra_c2_longtail_coverage_register.py` 只检查 C2 长尾覆盖账本是否覆盖 `classification.tsv` 中全部 C2 域，并明确 20 个已覆盖优先域与 184 个长尾缺口；它不补足长尾证据。
- `audit_human_infra_c2_longtail_first_batch_source_extraction_register.py` 只检查 C2-LT-B1 来源抽取试运行账本是否完成 48/48 个来源语境字段、阻塞用途、索引和队列映射；它不证明 full Source Cards、fresh review 或模型准入已经完成。
- `audit_human_infra_c2_longtail_first_batch_local_review_register.py` 只检查 C2-LT-B1 48/48 个来源抽取行是否完成本地来源语境复核、反查队列和抽取账本、保持阻塞用途并只路由到 independent fresh review；它不证明 reviewed artifacts、Source Card 晋升或模型准入已经完成。
- `audit_human_infra_c2_longtail_first_batch_independent_fresh_review_protocol.py` 只检查 C2-LT-B1 独立 fresh review 协议是否覆盖 48 个本地复核行、四个批次、判定字段和禁止用途边界；它不存放或证明 verdict。
- `audit_human_infra_c2_longtail_first_batch_independent_fresh_review_verdict_register.py` 只检查 C2-LT-B1 fresh-review 判定账本的 48/48 覆盖、外部核验证据字段、降级判定和模型阻塞边界；它不证明 reviewed artifacts 或模型准入完成。
- `audit_human_infra_c2_longtail_first_batch_reviewed_card_artifact_register.py` 只检查 `docs/reference/human-infra-c2-longtail-first-batch-reviewed-card-artifact-register.json` 是否把 42 个 eligible verdict 行落成 252 个 Source/变量/endpoint/uncertainty/transfer/downgrade artifact，并保留 6 个 blocked 行；它不证明剩余 C2 长尾域闭合或模型准入完成。
- `audit_human_infra_domain_source_specific_extraction_queue.py` 只检查当前 26 个域字段行是否派生为 81 个 domain-source 深读任务，并确认模型准入仍被 exact claim、endpoint、population、uncertainty 和 transfer-boundary 精读阻塞；它不证明任何来源已经支持对应域主张。
- `audit_human_infra_domain_source_specific_extraction_register.py` 只检查当前 81/81 个 domain-source 精读完成行是否来自队列、字段匹配、阻塞用途完整、索引到位；它不证明外部文献已完成 fresh review，也不打开校准预测、个体建议或干预排序。
- `audit_human_infra_domain_source_card_promotion_queue.py` 只检查当前 81 个 completed field rows 是否一一派生为 fresh review、Source Card、变量卡、endpoint 卡、uncertainty 卡、transfer-boundary 卡和 downgrade check 晋升任务；它不证明任何晋升任务已经完成，也不打开模型准入。
- `audit_human_infra_source_context_local_review_register.py` 只检查当前 20 个本地复核来源锚点是否反查到 promotion queue、来源证据、受影响任务、阻塞用途和入口索引；它不证明独立 fresh review 已完成，也不允许个体预测、干预排序或临床有效性声明。
- `audit_human_infra_card_promotion_prep_register.py` 只检查当前 81 个本地复核晋升任务是否预注册 Source/变量/endpoint/uncertainty/transfer/downgrade 待产物 ID、评审问题、阻塞用途和入口索引；它不证明独立 fresh review 或卡片晋升已经完成。
- `audit_human_infra_independent_fresh_review_protocol.py` 只检查独立 fresh review 协议是否把 81 个准备包按批次绑定到真实 source counts、verdict taxonomy、blocked uses 和入口索引；它不证明任何 fresh review verdict 已完成。
- `audit_human_infra_independent_fresh_review_verdict_register.py` 只检查独立 fresh review verdict 账本是否把已复核批次的来源锚点和晋升包绑定到 protocol、prep register、本地来源复核、source-specific extraction、阻塞用途和入口索引；它不证明卡片已经填充，也不打开模型准入。
- `audit_human_infra_reviewed_card_artifact_register.py` 只检查 reviewed card artifact 账本是否把 81 个 fresh-reviewed 晋升包落成 486 个 Source/变量/endpoint/uncertainty/transfer/downgrade artifact 实体，并确认模型准入、个体建议和临床有效性声明仍被阻塞。
- `audit_human_infra_future_boundary_route_card_register.py` 只检查 future-boundary route card 账本是否覆盖未来等待、生物停滞、神经身份连续性和 AI 加速四类高优先路线，并暴露技术窗口、接入、采用、持续期、可组合性、尾部风险和机会成本门；它不证明路线可行。
- `audit_human_infra_falsifier_source_card_backfill.py` 只检查当前论文强主张和 C1/C2 优先域反证是否具备 Source Card 锚点、证据角色、可用范围和外推边界；它不证明外部文献正确，也不等于完成逐篇 Source Card 精读。
- `audit_human_infra_falsifier_source_card_extraction.py` 只检查当前 21 个来源锚点是否全部完成字段级 Source Card 抽取，并绑定来源身份、域、论文 claim、模型位置、边界和人工可读包；它不证明外部文献正确，也不等于完成域级 Claim-Evidence Matrix。
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
