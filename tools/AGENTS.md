# tools 目录说明

`tools/` 保存仓库维护脚本和可迁移工程工具。这里的脚本不是产品运行时代码，默认从仓库根目录执行，也应尽量保持可复制到其他仓库使用。

## 目录结构

```text
tools/
├── AGENTS.md                         # 本目录架构说明
├── README.md                         # 工具入口和常用命令
├── audit_core_claim_evidence_matrix.py # 核心主张证据矩阵审计器
├── audit_human_infra_maturity_gap_register.py # 100% 成熟度缺口账本审计器
├── audit_human_infra_model_admission_contract.py # 模型准入契约审计器
├── audit_human_infra_model_admission_candidate_registry.py # 模型准入候选注册表审计器
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
├── audit_human_infra_c2_longtail_first_batch_blocked_source_resolution_register.py # C2-LT-B1 blocked source resolution 审计器
├── audit_human_infra_c2_longtail_first_batch_source_resolution_fresh_review_verdict_register.py # C2-LT-B1 source-resolution fresh review 判定审计器
├── audit_human_infra_c2_longtail_first_batch_corrected_source_reextraction_queue.py # C2-LT-B1 corrected source re-extraction 队列审计器
├── audit_human_infra_c2_longtail_first_batch_corrected_source_reextraction_register.py # C2-LT-B1 corrected source re-extraction 完成审计器
├── audit_human_infra_c2_longtail_first_batch_corrected_source_fresh_review_verdict_register.py # C2-LT-B1 corrected source fresh review 判定审计器
├── audit_human_infra_c2_longtail_first_batch_corrected_source_reviewed_card_artifact_register.py # C2-LT-B1 corrected source reviewed artifact 审计器
├── audit_human_infra_c2_longtail_second_batch_promotion_queue.py # C2-LT-B2 晋升队列审计器
├── audit_human_infra_c2_longtail_second_batch_source_extraction_queue.py # C2-LT-B2 来源深读队列审计器
├── audit_human_infra_c2_longtail_second_batch_source_extraction_register.py # C2-LT-B2 来源抽取完成寄存器审计器
├── audit_human_infra_c2_longtail_second_batch_local_review_register.py # C2-LT-B2 本地来源语境复核审计器
├── audit_human_infra_c2_longtail_second_batch_independent_fresh_review_protocol.py # C2-LT-B2 independent fresh review 协议审计器
├── audit_human_infra_c2_longtail_second_batch_independent_fresh_review_verdict_register.py # C2-LT-B2 independent fresh review 判定审计器
├── audit_human_infra_c2_longtail_second_batch_reviewed_card_artifact_register.py # C2-LT-B2 reviewed artifact 审计器
├── audit_human_infra_c2_longtail_third_batch_promotion_queue.py # C2-LT-B3 晋升队列审计器
├── audit_human_infra_c2_longtail_fourth_batch_promotion_queue.py # C2-LT-B4 晋升队列审计器
├── audit_human_infra_c2_longtail_third_batch_source_extraction_queue.py # C2-LT-B3 来源深读队列审计器
├── audit_human_infra_c2_longtail_fourth_batch_source_extraction_queue.py # C2-LT-B4 来源深读队列审计器
├── audit_human_infra_c2_longtail_fourth_batch_source_extraction_register.py # C2-LT-B4 来源抽取寄存器审计器
├── audit_human_infra_c2_longtail_fourth_batch_local_review_register.py # C2-LT-B4 本地来源语境复核审计器
├── audit_human_infra_c2_longtail_fourth_batch_source_resolution_register.py # C2-LT-B4 source-resolution 审计器
├── audit_human_infra_c2_longtail_fourth_batch_manual_fulltext_extraction_register.py # C2-LT-B4 manual/fulltext extraction 审计器
├── audit_human_infra_c2_longtail_fourth_batch_manual_fulltext_fresh_review_verdict_register.py # C2-LT-B4 manual/fulltext fresh-review 判定审计器
├── audit_human_infra_c2_longtail_seventh_batch_source_extraction_queue.py # C2-LT-B7 来源深读队列审计器
├── audit_human_infra_c2_longtail_seventh_batch_source_extraction_register.py # C2-LT-B7 来源抽取寄存器审计器
├── audit_human_infra_c2_longtail_seventh_batch_local_review_register.py # C2-LT-B7 本地来源语境复核审计器
├── audit_human_infra_c2_longtail_sixth_batch_independent_fresh_review_verdict_register.py # C2-LT-B6 independent fresh review 判定审计器
├── audit_human_infra_c2_longtail_sixth_batch_reviewed_card_artifact_register.py # C2-LT-B6 reviewed artifact 审计器
├── audit_human_infra_c2_longtail_third_batch_source_extraction_register.py # C2-LT-B3 来源抽取寄存器审计器
├── audit_human_infra_c2_longtail_third_batch_local_review_register.py # C2-LT-B3 本地来源语境复核审计器
├── audit_human_infra_c2_longtail_third_batch_source_resolution_register.py # C2-LT-B3 source-resolution 审计器
├── audit_human_infra_c2_longtail_third_batch_independent_fresh_review_protocol.py # C2-LT-B3 独立 fresh review 协议审计器
├── audit_human_infra_c2_longtail_third_batch_independent_fresh_review_verdict_register.py # C2-LT-B3 独立 fresh review 判定审计器
├── audit_human_infra_c2_longtail_third_batch_corrected_source_reextraction_queue.py # C2-LT-B3 corrected source re-extraction 队列审计器
├── audit_human_infra_c2_longtail_third_batch_corrected_source_reextraction_register.py # C2-LT-B3 corrected source re-extraction 完成审计器
├── audit_human_infra_c2_longtail_third_batch_corrected_source_fresh_review_verdict_register.py # C2-LT-B3 corrected source fresh review 判定审计器
├── audit_human_infra_c2_longtail_third_batch_reviewed_card_artifact_register.py # C2-LT-B3 reviewed artifact 审计器
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
- `audit_human_infra_model_admission_contract.py` 只检查模型准入契约的 L0-L5 层级、MAC gates、hard abort gates、方法锚点、入口索引和校准/个体用途阻塞状态，不证明任何 reviewed artifact 已可作为真实模型参数。
- `audit_human_infra_model_admission_candidate_registry.py` 只检查模型准入候选注册表是否覆盖契约中的 reviewed artifact registers、数量是否回到来源、L1/L2/L3/L4/L5 边界是否一致，不证明任何候选已经可校准或可用于个体预测。
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
- `audit_human_infra_c2_longtail_first_batch_blocked_source_resolution_register.py` 只检查 `docs/reference/human-infra-c2-longtail-first-batch-blocked-source-resolution-register.json` 是否覆盖 6 个非 eligible C2-LT-B1 来源行、准备来源校正候选并保持 artifact 晋升和模型准入阻塞；它不证明这些 blocked rows 已通过 fresh review。
- `audit_human_infra_c2_longtail_first_batch_source_resolution_fresh_review_verdict_register.py` 只检查 `docs/reference/human-infra-c2-longtail-first-batch-source-resolution-fresh-review-verdict-register.json` 是否覆盖 6 个来源纠偏行、16 个候选判定和 corrected source re-extraction 边界；它不证明 blocked rows 已经能直接晋升 artifact 或进入模型。
- `audit_human_infra_c2_longtail_first_batch_corrected_source_reextraction_queue.py` 只检查 `docs/reference/human-infra-c2-longtail-first-batch-corrected-source-reextraction-queue.json` 是否把 selected corrected candidates 派生成重新抽取任务，并继续阻塞 route-only 候选、artifact 晋升和模型准入；它不证明 corrected re-extraction 已完成。
- `audit_human_infra_c2_longtail_first_batch_corrected_source_reextraction_register.py` 只检查 `docs/reference/human-infra-c2-longtail-first-batch-corrected-source-reextraction-register.json` 是否覆盖 10/10 个 corrected re-extraction 任务、补足来源身份/endpoint/不确定性/迁移边界/降级/模型位置字段，并继续阻塞 route/index/fulltext 行、artifact 晋升和模型准入；它不证明 independent fresh review 已通过。
- `audit_human_infra_c2_longtail_first_batch_corrected_source_fresh_review_verdict_register.py` 只检查 `docs/reference/human-infra-c2-longtail-first-batch-corrected-source-fresh-review-verdict-register.json` 是否覆盖 10/10 个 corrected extraction outputs、把 5 行限定为 bounded artifact prep、把 5 行保持 lineage/route/index/fulltext 阻塞，并继续阻塞 reviewed artifact 创建和模型准入；它不证明 artifacts 已创建。
- `audit_human_infra_c2_longtail_first_batch_corrected_source_reviewed_card_artifact_register.py` 只检查 `docs/reference/human-infra-c2-longtail-first-batch-corrected-source-reviewed-card-artifact-register.json` 是否把 5 个 eligible corrected rows 落成 30 个 bounded reviewed artifacts，并保留 5 个 lineage/route/index/fulltext blocked rows；它不证明剩余 C2 长尾域闭合或模型准入完成。
- `audit_human_infra_c2_longtail_second_batch_promotion_queue.py` 只检查 `docs/reference/human-infra-c2-longtail-second-batch-promotion-queue.json` 是否选择 12 个非 B1 的剩余 C2 长尾域、绑定 24 个 web-checked 候选来源、保留晋升步骤和模型准入阻塞；它不证明 source extraction、fresh review 或 reviewed artifacts 已完成。
- `audit_human_infra_c2_longtail_second_batch_source_extraction_queue.py` 只检查 `docs/reference/human-infra-c2-longtail-second-batch-source-extraction-queue.json` 是否把 C2-LT-B2 24 个候选来源派生成 source-specific 深读任务，保持 required slots、问题、阻塞用途和索引；它不证明来源已读完、fresh review 通过或模型准入完成。
- `audit_human_infra_c2_longtail_second_batch_source_extraction_register.py` 只检查 `docs/reference/human-infra-c2-longtail-second-batch-source-extraction-register.json` 是否完成 C2-LT-B2 24/24 个来源语境字段抽取、保持降级触发、阻塞用途和索引；它不证明本地复核、fresh review、reviewed artifact 或模型准入完成。
- `audit_human_infra_c2_longtail_second_batch_local_review_register.py` 只检查 `docs/reference/human-infra-c2-longtail-second-batch-local-review-register.json` 是否完成 C2-LT-B2 24/24 个来源抽取行的本地结构复核、反查队列与抽取账本、保持阻塞用途并只路由到 independent fresh review；它不证明 reviewed artifacts、Source Card 晋升或模型准入已经完成。
- `audit_human_infra_c2_longtail_second_batch_independent_fresh_review_protocol.py` 只检查 `docs/reference/human-infra-c2-longtail-second-batch-independent-fresh-review-protocol.json` 是否把 C2-LT-B2 24 个本地复核行拆成 2 个 independent fresh-review 批次、保留 verdict taxonomy、晋升边界和禁止用途；它不存放 reviewer verdict，不创建 reviewed artifacts，也不打开模型准入。
- `audit_human_infra_c2_longtail_second_batch_independent_fresh_review_verdict_register.py` 只检查 `docs/reference/human-infra-c2-longtail-second-batch-independent-fresh-review-verdict-register.json` 是否完成 C2-LT-B2 24/24 个来源的 independent fresh-review 判定、只允许 23 个 bounded artifact-fill 行、保留 1 个 downgrade-before-fill 行并继续阻塞模型准入；它不创建 reviewed artifacts。
- `audit_human_infra_c2_longtail_second_batch_reviewed_card_artifact_register.py` 只检查 `docs/reference/human-infra-c2-longtail-second-batch-reviewed-card-artifact-register.json` 是否把 23 个 eligible C2-LT-B2 verdict rows 落成 138 个 bounded reviewed artifacts，并保留 1 个 downgrade-before-fill row；它不证明剩余 C2 长尾域闭合或模型准入完成。
- `audit_human_infra_c2_longtail_third_batch_promotion_queue.py` 只检查 `docs/reference/human-infra-c2-longtail-third-batch-promotion-queue.json` 是否选择 12 个非 B1/B2 的神经-感知-认知 C2 长尾域、绑定 24 个 web-checked 候选来源、保留晋升步骤和模型准入阻塞；它不证明 source extraction、fresh review 或 reviewed artifacts 已完成。
- `audit_human_infra_c2_longtail_fourth_batch_promotion_queue.py` 只检查 `docs/reference/human-infra-c2-longtail-fourth-batch-promotion-queue.json` 是否选择 12 个非 B1/B2/B3 的代谢、内分泌、肾肝、电解质和携氧稳态 C2 长尾域、绑定 24 个 web-checked 候选来源、保留晋升步骤和模型准入阻塞；它不证明 source extraction、fresh review 或 reviewed artifacts 已完成。
- `audit_human_infra_c2_longtail_third_batch_source_extraction_queue.py` 只检查 `docs/reference/human-infra-c2-longtail-third-batch-source-extraction-queue.json` 是否把 C2-LT-B3 24 个候选来源派生成 source-specific 深读任务，保持 required slots、问题、阻塞用途和索引；它不证明来源已读完、fresh review 通过或模型准入完成。
- `audit_human_infra_c2_longtail_fourth_batch_source_extraction_queue.py` 只检查 `docs/reference/human-infra-c2-longtail-fourth-batch-source-extraction-queue.json` 是否把 C2-LT-B4 24 个候选来源派生成 source-specific 深读任务，保持 required slots、问题、阻塞用途和索引；它不证明来源已读完、fresh review 通过或模型准入完成。
- `audit_human_infra_c2_longtail_fourth_batch_source_extraction_register.py` 只检查 `docs/reference/human-infra-c2-longtail-fourth-batch-source-extraction-register.json` 是否完成 C2-LT-B4 24/24 个来源语境字段抽取、保留无摘要全文复核、重复共识路线、降级触发、阻塞用途和索引；它不证明本地复核、fresh review、reviewed artifact 或模型准入完成。
- `audit_human_infra_c2_longtail_fourth_batch_local_review_register.py` 只检查 `docs/reference/human-infra-c2-longtail-fourth-batch-local-review-register.json` 是否完成 C2-LT-B4 24/24 个来源抽取行本地结构复核、反查队列与抽取账本、保留 1 个重复共识路线行和 3 个无摘要需全文行、保持阻塞用途并只路由到 independent fresh review 或 source resolution；它不证明 reviewed artifacts、Source Card 晋升或模型准入已经完成。
- `audit_human_infra_c2_longtail_fourth_batch_source_resolution_register.py` 只检查 `docs/reference/human-infra-c2-longtail-fourth-batch-source-resolution-register.json` 是否覆盖 C2-LT-B4 4 个本地复核问题行、准备 8 个重复路线或全文路线候选、保留 fresh-review/manual-fulltext 后续门槛，并继续阻塞 reviewed artifacts、Source Card 晋升和模型准入。
- `audit_human_infra_c2_longtail_fourth_batch_manual_fulltext_extraction_register.py` 只检查 `docs/reference/human-infra-c2-longtail-fourth-batch-manual-fulltext-extraction-register.json` 是否覆盖 C2-LT-B4 8 个 source-resolution 候选、完成有界全文/官方页路线抽取、区分 3 个 bounded fresh-review 候选和 5 个 duplicate/route-only/manual-access 阻塞行，并继续阻塞 reviewed artifacts、Source Card 晋升和模型准入。
- `audit_human_infra_c2_longtail_fourth_batch_manual_fulltext_fresh_review_verdict_register.py` 只检查 `docs/reference/human-infra-c2-longtail-fourth-batch-manual-fulltext-fresh-review-verdict-register.json` 是否完成 C2-LT-B4 8 个 manual/fulltext extraction 行的 independent fresh-review 判定、只允许 3 行进入 bounded reviewed artifact prep、保留 5 个 blocked/context-only 行，并继续阻塞 reviewed artifacts 创建和模型准入。
- `audit_human_infra_c2_longtail_fourth_batch_manual_fulltext_reviewed_card_artifact_register.py` 只检查 `docs/reference/human-infra-c2-longtail-fourth-batch-manual-fulltext-reviewed-card-artifact-register.json` 是否把 3 个 eligible manual/fulltext fresh-review rows 晋升为 18 个 bounded reviewed artifacts、保留 5 个 duplicate/route-only/manual-access/context-only blockedRows，并继续阻塞校准预测、个体建议、干预排序、临床有效性主张和死亡日期输出。
- `audit_human_infra_c2_longtail_fifth_batch_promotion_queue.py` 只检查 `docs/reference/human-infra-c2-longtail-fifth-batch-promotion-queue.json` 是否选择 12 个非 B1/B2/B3/B4 的细胞质量控制、细胞器通信、分子运输、膜脂韧性、清除和屏障底座 C2 长尾域、绑定 24 个 web/API-checked 候选来源、保留晋升步骤和模型准入阻塞；它不证明 source extraction、fresh review 或 reviewed artifacts 已完成。
- `audit_human_infra_c2_longtail_sixth_batch_promotion_queue.py` 只检查 `docs/reference/human-infra-c2-longtail-sixth-batch-promotion-queue.json` 是否选择 12 个非 B1/B2/B3/B4/B5 的跨代连续性、生殖、孕产新生儿和儿童源体维护 C2 长尾域、绑定 24 个 web-checked 候选来源、保留晋升步骤和模型准入阻塞；它不证明 source extraction、fresh review 或 reviewed artifacts 已完成。
- `audit_human_infra_c2_longtail_seventh_batch_promotion_queue.py` 只检查 `docs/reference/human-infra-c2-longtail-seventh-batch-promotion-queue.json` 是否选择 12 个非 B1/B2/B3/B4/B5/B6 的癌症控制、幸存者连续性、移植安全、器官捐献和工程器官替换 C2 长尾域、绑定 24 个 web-checked 候选来源、保留晋升步骤和模型准入阻塞；它不证明 source extraction、fresh review 或 reviewed artifacts 已完成。
- `audit_human_infra_c2_longtail_seventh_batch_source_extraction_queue.py` 只检查 `docs/reference/human-infra-c2-longtail-seventh-batch-source-extraction-queue.json` 是否把 C2-LT-B7 晋升队列派生成 24 个 source-specific 深读任务、保留必填抽取槽位、问题、索引和阻塞用途；它不证明来源已复核、fresh review 或 reviewed artifacts 已完成。
- `audit_human_infra_c2_longtail_seventh_batch_source_extraction_register.py` 只检查 `docs/reference/human-infra-c2-longtail-seventh-batch-source-extraction-register.json` 是否完成 C2-LT-B7 24/24 个来源语境字段抽取、保留 FDA 404 路线、动态注册页、重复 CDC 来源、筛查边界、降级触发、阻塞用途和索引；它不证明本地复核、fresh review、reviewed artifact 或模型准入完成。
- `audit_human_infra_c2_longtail_seventh_batch_local_review_register.py` 只检查 `docs/reference/human-infra-c2-longtail-seventh-batch-local-review-register.json` 是否完成 C2-LT-B7 24/24 个来源抽取行的本地结构复核、保留 6 个 FDA route、动态注册或重复来源问题行、阻塞用途和索引；它不证明 fresh review、reviewed artifact 或模型准入完成。
- `audit_human_infra_c2_longtail_sixth_batch_source_extraction_queue.py` 只检查 `docs/reference/human-infra-c2-longtail-sixth-batch-source-extraction-queue.json` 是否把 C2-LT-B6 晋升队列派生成 24 个 source-specific 深读任务、保留必填抽取槽位、问题、索引和阻塞用途；它不证明来源已复核、fresh review 或 reviewed artifacts 已完成。
- `audit_human_infra_c2_longtail_sixth_batch_source_extraction_register.py` 只检查 `docs/reference/human-infra-c2-longtail-sixth-batch-source-extraction-register.json` 是否完成 C2-LT-B6 24/24 个来源语境字段抽取、保留 guideline route、publisher/manual review、source-lineage、降级触发、阻塞用途和索引；它不证明本地复核、fresh review、reviewed artifact 或模型准入完成。
- `audit_human_infra_c2_longtail_sixth_batch_local_review_register.py` 只检查 `docs/reference/human-infra-c2-longtail-sixth-batch-local-review-register.json` 是否完成 C2-LT-B6 24/24 个来源抽取行的本地结构复核、保留 7 个 source-resolution/manual/fulltext/source-lineage 问题行、阻塞用途和索引；它不证明 fresh review、reviewed artifact 或模型准入完成。
- `audit_human_infra_c2_longtail_sixth_batch_source_resolution_register.py` 只检查 `docs/reference/human-infra-c2-longtail-sixth-batch-source-resolution-register.json` 是否把 C2-LT-B6 7 个问题行整理为 19 个官方页、PubMed/PMC、OUP/LWW/AAP 或 CDC 路线候选、保留 manual/fulltext 与 fresh review 阻塞边界；它不证明 reviewed artifact 或模型准入完成。
- `audit_human_infra_c2_longtail_sixth_batch_manual_fulltext_extraction_register.py` 只检查 `docs/reference/human-infra-c2-longtail-sixth-batch-manual-fulltext-extraction-register.json` 是否覆盖 C2-LT-B6 19 个 source-resolution 候选、只允许 7 个 bounded fresh-review 候选、保留 12 个 route-only、bibliographic、summary、companion-lineage 或 policy-resource context 阻塞行，并继续阻塞 reviewed artifacts、Source Card 晋升和模型准入。
- `audit_human_infra_c2_longtail_sixth_batch_independent_fresh_review_verdict_register.py` 只检查 `docs/reference/human-infra-c2-longtail-sixth-batch-independent-fresh-review-verdict-register.json` 是否完成 C2-LT-B6 17 个非问题来源抽取行和 19 个 manual/fulltext 行的 independent fresh-review 判定、只允许 24 行进入 bounded reviewed artifact prep、保留 12 个 manual route-only、bibliographic、summary、companion-lineage 或 policy-resource context 阻塞行，并继续阻塞 reviewed artifacts 创建和模型准入。
- `audit_human_infra_c2_longtail_sixth_batch_reviewed_card_artifact_register.py` 只检查 `docs/reference/human-infra-c2-longtail-sixth-batch-reviewed-card-artifact-register.json` 是否把 C2-LT-B6 24 个 eligible fresh-review rows 晋升为 144 个 Source/变量/endpoint/uncertainty/transfer/downgrade artifacts、保留 12 个 manual blocked/context rows，并继续阻塞模型准入。
- `audit_human_infra_c2_longtail_fifth_batch_source_extraction_queue.py` 只检查 `docs/reference/human-infra-c2-longtail-fifth-batch-source-extraction-queue.json` 是否把 C2-LT-B5 晋升队列派生成 24 个 source-specific 深读任务、保留必填抽取槽位、问题、索引和阻塞用途；它不证明来源已复核、fresh review 或 reviewed artifacts 已完成。
- `audit_human_infra_c2_longtail_fifth_batch_source_extraction_register.py` 只检查 `docs/reference/human-infra-c2-longtail-fifth-batch-source-extraction-register.json` 是否完成 C2-LT-B5 24/24 个来源语境字段抽取、保留无开放全文、跨域复用、模型生物/综述边界、降级触发、阻塞用途和索引；它不证明本地复核、fresh review、reviewed artifact 或模型准入完成。
- `audit_human_infra_c2_longtail_fifth_batch_local_review_register.py` 只检查 `docs/reference/human-infra-c2-longtail-fifth-batch-local-review-register.json` 是否完成 C2-LT-B5 24/24 个来源抽取行本地结构复核、反查队列与抽取账本、保留 8 个无开放全文或跨域复用问题行、保持阻塞用途并只路由到 independent fresh review 或 source resolution；它不证明 reviewed artifacts、Source Card 晋升或模型准入已经完成。
- `audit_human_infra_c2_longtail_fifth_batch_source_resolution_register.py` 只检查 `docs/reference/human-infra-c2-longtail-fifth-batch-source-resolution-register.json` 是否覆盖 C2-LT-B5 8 个本地复核问题行、准备 14 个无开放全文/人工全文或跨域复用来源路线候选、保留 manual/fulltext extraction 和 fresh-review 后续门槛，并继续阻塞 reviewed artifacts、Source Card 晋升和模型准入。
- `audit_human_infra_c2_longtail_fifth_batch_manual_fulltext_extraction_register.py` 只检查 `docs/reference/human-infra-c2-longtail-fifth-batch-manual-fulltext-extraction-register.json` 是否覆盖 C2-LT-B5 14 个 source-resolution 候选、只允许 2 个 bounded fresh-review 候选、保留 12 个 route-only/manual-access/duplicate 阻塞行，并继续阻塞 reviewed artifacts、Source Card 晋升和模型准入。
- `audit_human_infra_c2_longtail_fifth_batch_independent_fresh_review_verdict_register.py` 只检查 `docs/reference/human-infra-c2-longtail-fifth-batch-independent-fresh-review-verdict-register.json` 是否完成 C2-LT-B5 16 个非问题来源抽取行和 14 个 manual/fulltext 行的 independent fresh-review 判定、只允许 17 行进入 bounded reviewed artifact prep、保留 13 个 manual route-only/manual-access/duplicate/context-only 阻塞行，并继续阻塞 reviewed artifacts 创建和模型准入。
- `audit_human_infra_c2_longtail_fifth_batch_reviewed_card_artifact_register.py` 只检查 `docs/reference/human-infra-c2-longtail-fifth-batch-reviewed-card-artifact-register.json` 是否把 17 个 eligible fresh-review rows 晋升为 102 个有界 reviewed artifacts、保留 13 个 blocked manual rows，并继续阻塞校准预测、个体建议、干预排序、临床有效性主张和死亡日期输出。
- `audit_human_infra_c2_longtail_third_batch_source_extraction_register.py` 只检查 `docs/reference/human-infra-c2-longtail-third-batch-source-extraction-register.json` 是否完成 C2-LT-B3 24/24 个来源语境字段抽取、保留 source-resolution 标记、降级触发、阻塞用途和索引；它不证明本地复核、fresh review、reviewed artifact 或模型准入完成。
- `audit_human_infra_c2_longtail_third_batch_local_review_register.py` 只检查 `docs/reference/human-infra-c2-longtail-third-batch-local-review-register.json` 是否完成 C2-LT-B3 24/24 个来源抽取行本地结构复核、反查队列与抽取账本、保留 5 个 source-resolution/manual-access 问题行、保持阻塞用途并只路由到 independent fresh review 或 source resolution；它不证明 reviewed artifacts、Source Card 晋升或模型准入已经完成。
- `audit_human_infra_c2_longtail_third_batch_source_resolution_register.py` 只检查 `docs/reference/human-infra-c2-longtail-third-batch-source-resolution-register.json` 是否覆盖 C2-LT-B3 5 个本地复核问题行、准备 7 个 corrected/split/route-normalized 候选、保留 fresh-review 和 corrected-reextraction 后续门槛，并继续阻塞 reviewed artifacts、Source Card 晋升和模型准入。
- `audit_human_infra_c2_longtail_third_batch_independent_fresh_review_protocol.py` 只检查 `docs/reference/human-infra-c2-longtail-third-batch-independent-fresh-review-protocol.json` 是否把 C2-LT-B3 24 个本地复核行拆成 2 个 fresh-review 批次、把 5 个 source-resolution issue rows 纳入纠偏检查，并继续禁止协议内 verdict、reviewed artifacts 和模型准入。
- `audit_human_infra_c2_longtail_third_batch_independent_fresh_review_verdict_register.py` 只检查 `docs/reference/human-infra-c2-longtail-third-batch-independent-fresh-review-verdict-register.json` 是否完成 C2-LT-B3 24/24 个来源的 fresh-review 判定、把 18 行限定为 bounded artifact fill、把 5 个问题行限定为 corrected-source re-extraction、把 1 行保持 downgrade-before-fill，并继续阻塞 reviewed artifacts 和模型准入。
- `audit_human_infra_c2_longtail_third_batch_corrected_source_reextraction_queue.py` 只检查 `docs/reference/human-infra-c2-longtail-third-batch-corrected-source-reextraction-queue.json` 是否把 5 个 source-resolution-supported 问题行的 7 个 corrected/split/route-normalized 候选派生成 corrected source re-extraction 任务，并继续阻塞 artifact 晋升和模型准入。
- `audit_human_infra_c2_longtail_third_batch_corrected_source_reextraction_register.py` 只检查 `docs/reference/human-infra-c2-longtail-third-batch-corrected-source-reextraction-register.json` 是否覆盖 7/7 个 corrected re-extraction 任务、补足来源身份/endpoint/不确定性/迁移边界/降级/模型位置字段，并继续阻塞 route/split 行、artifact 晋升和模型准入；它不证明 independent fresh review 已通过。
- `audit_human_infra_c2_longtail_third_batch_corrected_source_fresh_review_verdict_register.py` 只检查 `docs/reference/human-infra-c2-longtail-third-batch-corrected-source-fresh-review-verdict-register.json` 是否覆盖 7/7 个 corrected extraction outputs、把 6 行限定为 bounded artifact prep、把 1 行保持 duplicate/split route 阻塞、记录 AAO-HNS publisher route 可读事实，并继续阻塞 reviewed artifact 创建和模型准入；它不证明 artifacts 已创建。
- `audit_human_infra_c2_longtail_third_batch_reviewed_card_artifact_register.py` 只检查 `docs/reference/human-infra-c2-longtail-third-batch-reviewed-card-artifact-register.json` 是否把 18 个原始 eligible 行和 6 个 corrected eligible 行落成 144 个 bounded reviewed artifacts，并保留 EXT-022 downgrade-before-fill 与 C2LTB3-CREXT-004 duplicate/split route blocked row；它不证明剩余 C2 长尾域闭合或模型准入完成。
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
