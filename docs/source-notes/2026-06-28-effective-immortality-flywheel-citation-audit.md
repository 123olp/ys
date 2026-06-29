# 有效永生飞轮 Citation Audit v1.1

Status: citation context, claim alignment, local claim-context audit, reference metadata, primary-source reference verification, AI task method-audit, declaration coverage, estimand protocol coverage, analysis-plan coverage, and AI research failure-mode coverage v1.1  
Date: 2026-06-28  
Target paper: [Effective Immortality Acceleration Flywheel](../explanations/effective-immortality-acceleration-flywheel.md)  
Web page: [`web/src/pages/papers/effective-immortality-flywheel.astro`](../../web/src/pages/papers/effective-immortality-flywheel.astro)

## Scope

本轮只审查对论文论证最关键、也最容易被审稿人追问的引用组：

1. 生存分析与健康资本方法源；
2. AI productivity 实证源；
3. target trial / 因果协议方法源；
4. AI 风险与人机交互治理源；
5. 数字孪生、个人信息学和可能性空间的框架源。

本文件不是最终全量新线程 `citation-audit`，也不替代后续逐句引用语境核查。它记录本轮已完成的来源规范化、引用上下文注册、机器可读引用产物和仍需补做的审查项。

## Verified / Normalized Entries

| Entry | Current action | Notes |
| --- | --- | --- |
| Brynjolfsson, Li & Raymond, *Generative AI at Work* | Normalized to QJE 2025, 140(2):889-942 | 用于支持限定客服任务中的 `A -> Q`，不能泛化为所有知识工作。 |
| Noy & Zhang, *Experimental evidence on the productivity effects of generative artificial intelligence* | Normalized to Science 2023, 381(6654):187-192 | 用于支持写作任务内的生产率提升，不能支持通用智能增强。 |
| Dell'Acqua et al., *Navigating the Jagged Technological Frontier* | Normalized to Organization Science 2026 and DOI `10.1287/orsc.2025.21838` | 用于支持 AI 收益和风险具有任务边界。 |
| Peng et al., *The Impact of AI on Developer Productivity* | Kept as arXiv:2302.06590 | 用于编程任务生产率入口，需保留预印本边界。 |
| Hernan, Wang & Leaf, *Target Trial Emulation* | Normalized to JAMA 2022 PubMed record | 用于支持因果协议门禁，不证明任何具体技术有效。 |
| Kaplan-Meier 1958 and Cox 1972 | Kept as method standards | 只支持生存曲线和风险函数语言。 |
| Grossman 1972 health capital | Kept as theoretical economics source | 用于区分健康资本、有效时间和日历时间。 |

## Context Checks

| Claim location | Citation group | Verdict | Reason |
| --- | --- | --- | --- |
| `T / E` 生存曲线、风险函数、有效时间 | Kaplan-Meier, Cox, Grossman, HALE, QALY | KEEP | 上下文只使用其方法语言和测量语言，没有声称这些来源证明某项干预延寿。 |
| `A -> Q` AI 工具提升单位时间行动质量 | Brynjolfsson et al.; Noy & Zhang; Peng et al. | KEEP WITH BOUNDARY | 页面已写明“限定任务”和“异质性”，符合来源可支持范围。 |
| `A/Q -> risk` 技术收益与风险并存 | Dell'Acqua et al.; NIST AI RMF; HAI Guidelines | KEEP | 上下文用于建立边界和治理门禁，不用于夸大收益。 |
| `U_t -> causal claim` 因果协议 | Target Trial Emulation; ClinicalTrials.gov API; WHO ICTRP; TRIPOD+AI; PROBAST+AI; CONSORT-AI; SPIRIT-AI | KEEP | 上下文用于方法门禁、试验注册、预测模型报告和 AI 临床试验报告标准，不声称其证明飞轮成立。 |
| `O` 可能性空间 | Capability Approach; social determinants; social capital | KEEP WITH BOUNDARY | 上下文将其用作规范和测量框架，不承担数值预测。 |

## Citation Context Register v0.1

| ID | 来源组 | 使用语境 | 支持范围 | 不可支持范围 | 状态 |
| --- | --- | --- | --- | --- | --- |
| CTX1 | Kaplan-Meier 1958; Cox 1972 | 定义 `T`、生存函数 `S(t)`、删失数据和风险函数 `lambda(t)` 的统计语言 | 事件时间、删失、生存曲线和协变量风险建模的基础方法 | 不证明任何具体延寿、健康、AI 或资源干预有效 | KEEP |
| CTX2 | Grossman Health Capital; WHO HALE; NICE QALY | 把日历寿命转译为健康质量、有效时间和质量调整时间 | `T -> E` 的测量语言和健康质量调整视角 | 不能完整定义主体连续性，也不能替代个体医学判断 | KEEP WITH BOUNDARY |
| CTX3 | Hallmarks of Aging; GrimAge; Cognitive Reserve | 提出身体状态、衰老机制、生物年龄信号和认知储备候选变量 | 状态变量和风险信号的机制/关联入口 | 不能把机制综述、预测关联或认知储备直接写成干预效果 | KEEP WITH BOUNDARY |
| CTX4 | Deliberate Practice; Law of Practice; Self-Regulated Learning; Feedback Intervention Theory | 解释 `E -> R -> C`：有效时间如何在有目标、有反馈和可修正的任务中沉淀为能力 | 学习轮次、反馈质量、练习曲线和能力积累的条件 | 时间本身不会自动产生能力；错误反馈和低质量重复可能反向损害表现 | KEEP WITH BOUNDARY |
| CTX5 | Human Capital; Social Capital; Social Relationships Mortality | 说明经验、资源、信誉和协作网络如何进入 `C` 与 `O`，并可能反哺 `T/E` | 积累资本、社会支持和死亡风险关联的讨论 | 不能把社会关系关联直接升级成具体干预的因果延寿结论 | KEEP WITH BOUNDARY |
| CTX6 | TAM; UTAUT; Diffusion of Innovations | 解释 `C -> A`：技术采用受有用性、易用性、促进条件、资源和社会影响约束 | 技术采用能力的分解：access、understanding、evaluation、trial、integration | 不能证明采用后的技术一定有效，也不能覆盖所有高风险医学或神经技术 | KEEP WITH BOUNDARY |
| CTX7 | Generative AI at Work; Noy and Zhang; GitHub Copilot; Jagged Technological Frontier | 支持 `A -> Q` 在限定任务中的生产率、速度、质量或任务边界证据 | 生成式 AI 在客服、写作、编程或知识工作实验中的任务内效果与异质性 | 不能泛化为通用智能增强、健康寿命延长或永生收益 | KEEP WITH BOUNDARY |
| CTX8 | NIST AI RMF; Guidelines for Human-AI Interaction; NASA-TLX; Automation taxonomy | 给 `A/Q -> risk`、QA 成本、任务负荷、自动化等级和人机控制权提供治理语言 | 风险识别、测量、纠错、回滚和人机协作设计边界 | 治理框架和交互指南不提供收益估计，也不证明 AI 能延寿 | KEEP |
| CTX9 | Target Trial Emulation; ClinicalTrials.gov API; WHO ICTRP; TRIPOD+AI; PROBAST+AI; CONSORT-AI; SPIRIT-AI | 定义 `U_t -> causal claim` 的因果门禁、试验注册入口、预测模型报告门禁和 AI 临床试验报告门禁 | population、intervention、comparator、time zero、outcome、estimand、试验登记、AI 干预描述、输入输出、人机交互、错误案例、验证、校准和偏倚审查 | 不能消除所有不可测混杂，也不证明任何注册试验、预测模型或 AI 干预有效 | KEEP |
| CTX10 | Apple Heart Study; Personal Informatics; Lived Informatics; Dynamic Digital Twin | 说明观测、反馈、个人数据系统和生命过程建模如何进入状态观测层 | `observation -> action` 的路径和自我追踪/数字孪生的系统问题 | 早筛、追踪或数字孪生概念不等于死亡风险下降或医疗结局改善 | KEEP WITH BOUNDARY |
| CTX11 | Extended Mind; Engelbart; Cognition in the Wild | 支撑工具、记忆外化、分布式认知和认知增强进入主体系统的理论位置 | 主体能力可以由人、工具、表征、环境和协作流程共同支撑 | 哲学和系统框架不提供数值效应估计，也不能证明数字副本等同于本人 | KEEP WITH BOUNDARY |
| CTX12 | Capability Approach; WHO SDOH; WHO Primary Health Care | 定义 `O` 可能性空间为真实可进入路径，并把资源、制度、医疗和社会条件纳入反哺路径 | 真实选择权、健康决定因素、医疗可及和连续照护的规范/公共卫生框架 | 规范框架不提供寿命预测，也不能替代具体政策或医疗干预评估 | KEEP WITH BOUNDARY |

## Claim Alignment Addendum v0.1

本轮新增 `claimEvidenceMap`。它不替代逐条全文引用核查，只把七条核心主张映射到正文位置、证据边、引用上下文、反证条件和升级门槛，用于后续 claim-to-source 审计。

| 主张 | 判定 | 关键上下文 | 必须防止的越界 |
| --- | --- | --- | --- |
| CL1 | FRAMEWORK_ONLY | CTX2；CTX4；CTX5；CTX6；CTX7；CTX12 | 把完整飞轮写成已被实证证明 |
| CL2 | OPERATIONAL_INTERFACE | CTX1；CTX2；CTX4；CTX5；CTX6；CTX7；CTX8；CTX12 | 把七变量接口写成充分且唯一的变量集 |
| CL3 | METHOD_SUPPORTED | CTX1；CTX9 | 没有比较组、time zero 和结局定义时写因果结论 |
| CL4 | BOUNDED_EMPIRICAL | CTX7；CTX8 | 把 AI 任务内收益泛化为通用智能增强或寿命收益 |
| CL5 | NORMATIVE_MEASUREMENT | CTX5；CTX12 | 把抽象机会写成真实可进入选择权 |
| CL6 | GOVERNANCE_REQUIRED | CTX8；CTX9；CTX10；CTX11 | 只记录技术正收益，不记录副作用、停止条件和回滚路径 |
| CL7 | HARD_BOUNDARY | CTX1；CTX3；CTX7；CTX8；CTX9 | 输出个体死亡日期，或把机制合理、短期功能改善写成寿命延长 |

## Reference Metadata Registry v0.3

本轮新增 `referenceRegistry`，位于 `web/src/data/effective-immortality-evidence.json`。它将 Web References 从手写 HTML 列表升级为机器可审计元数据。

| 指标 | 数量 | 说明 |
| --- | --- | --- |
| Total registry entries | 48 | 覆盖当前 Web 论文 References、Source Cards 和 evidence source alias 所需的核心条目 |
| DOI / PubMed / arXiv / publisher verified entries | 34 | 覆盖 Crossref DOI、PubMed、arXiv API、publisher page、official archive 等可追溯入口 |
| arXiv verified entries | 1 | `arXiv:2302.06590` 通过 arXiv Atom API 核对标题和作者 |
| Official web / registry entries | 13 | WHO、NICE、NIST、ClinicalTrials.gov、WHO ICTRP、TRIPOD+AI、PROBAST+AI、GRADE 等官方页面、registry 或官方工具入口 |
| Local project entries | 1 | 本项目 source-note |

## Coverage Audit v0.3

本轮新增 `web/scripts/audit-effective-immortality-coverage.mjs`，用于检查 `evidenceEdges[*].sources` 与 `technologyFamilies[*].evidenceSources` 中的来源别名是否能回到 Source Card 和 Reference Registry。

| 指标 | 数量 | 说明 |
| --- | --- | --- |
| Evidence source aliases | 54 | 来自 evidence edges 与 technology families 的去重来源别名 |
| AI task reference keys | 4 | 来自 `aiTaskEvidenceRegister[*].referenceKey` 的去重引用键 |
| Source Cards | 47 | Source Cards v0.5 中的 `## Card` 条目 |
| Reference Registry entries | 48 | `referenceRegistry` 中的机器可读条目 |
| AI task required fields | 14 | `aiTaskEvidenceRegister` 中每条记录必须包含 full-text verification 与 `methodAudit` 入口字段 |
| AI task method-audit fields | 7 | 每条 `methodAudit` 必须包含主表/主图、主要规格、统计列、不确定性、评分协议、QA 成本和外推限制 |
| Research declarations | 8 | `researchDeclarations` 必须包含数据、代码、伦理安全、AI 辅助披露、利益冲突、资金、作者贡献和使用限制 |
| Estimand registry rows | 9 | 每条 `evidenceEdges[*].edge` 必须对应一条 `estimandRegistry`，并补齐 population、intervention/exposure、comparator、time zero、outcome、estimand、identification risk 和 current status |
| Analysis plan registry rows | 9 | 每条 `evidenceEdges[*].edge` 必须对应一条 `analysisPlanRegistry`，并补齐 study question、candidate design、minimum data、primary estimator、diagnostics、sensitivity checks、reporting output 和 current status |
| AI research failure mode rows | 7 | `aiResearchFailureModeAudit` 必须覆盖 FM1-FM7，并补齐适用范围、本文风险、当前证据、控制、状态、阻塞条件和下一步 |
| Coverage verdict | PASS | 无缺失 alias mapping、无缺失 Source Card、无缺失 registry key、无 AI task reference key 断链、无 AI task 必填字段缺失、无 method-audit 字段缺失、无 research declaration 缺失、无 estimand registry 缺失、无 analysis plan registry 缺失、无 AI research failure mode audit 缺失、无 claim/context/edge 断链 |

关键修复：原 Source Cards 中 `Generative AI at Work` 的 DOI 写成 `10.1093/qje/qjaf005`，Crossref 返回的实际论文是另一篇 QJE 文章。已更正为 `10.1093/qje/qjae044`。

## Primary-Source Reference Verification v0.1

本轮新增 `web/scripts/verify-reference-registry.mjs`，对 Reference Registry 执行联网 primary-source 核验。它不替代逐句 citation context reviewer，但能把“本地写了 auditStatus”升级为可重复运行的外部元数据检查。

| 指标 | 数量 | 说明 |
| --- | --- | --- |
| Reference Registry entries | 48 | 全部进入联网核验 |
| PASS | 48 | DOI/Crossref、arXiv API、官方 URL、可访问书目/作者页或本地 artifact 通过 |
| WARN | 0 | 当前无自动访问 WARN |
| FAIL | 0 | 当前无 DOI、arXiv、官方 URL 或本地 artifact 硬失败 |

关键修复：

- `newell1981lawPractice` 的 DOI 从不可解析的 `10.4324/9780203728178-1` 修正为 `10.4324/9780203728178-6`。
- `probastAi2025` 的标题改为 BMJ/Crossref 标题：`PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods`。
- `rogers2003diffusion` 改用 Internet Archive 可访问书目页，`hutchins1995cognition` 改用 Edwin Hutchins 作者页书籍介绍，避免出版社页面 403 造成机器核验噪音。

## Claim Context Alignment Audit v0.1

本轮新增 `web/scripts/audit-claim-context-alignment.mjs`。它检查本地结构是否满足 claim-reference alignment 的最低门槛：每条核心主张必须有 claim evidence row，每个 citation context 必须存在并写明 supports 与 doesNotSupport，每个 context 必须被至少一条 Reference Registry 支撑，且 Reference Verification 不能存在 FAIL。

| 指标 | 数量 | 说明 |
| --- | --- | --- |
| Claim Register rows | 7 | CL1-CL7 全部覆盖 |
| Claim Evidence Map rows | 7 | 每条核心主张都有正文位置、证据边、引用上下文、反证条件和升级门槛 |
| Citation Contexts | 12 | CTX1-CTX12 均有 supports / doesNotSupport |
| Reference Registry entries | 48 | 所有被主张使用的上下文都能回到至少一条 reference |
| Reference Verification FAIL rows | 0 | 无 DOI、arXiv、官方 URL 或本地 artifact 硬失败 |
| Verdict | PASS | 本地 claim-context-reference 结构闭环通过 |

## Citation Context Risk Triage v0.1

本轮新增 `web/scripts/audit-citation-context-risk-triage.mjs`。它不是 reviewer verdict，而是把 12 个 Citation Context 按过度外推风险、边界敏感性、主张类型和 Reference Verification 状态排序，让后续 fresh reviewer 优先处理最容易被误用的来源组。

| 指标 | 数量 | 说明 |
| --- | --- | --- |
| Citation contexts | 12 | CTX1-CTX12 全部进入风险分诊 |
| BLOCKER | 0 | 当前无本地结构性 blocker |
| HIGH | 1 | `CTX2`：Grossman、WHO HALE、NICE QALY，容易从健康质量调整时间过度外推到主体性和未来选择权 |
| MEDIUM | 7 | 需要保留边界的机制、任务效果、治理和观测类上下文 |
| LOW | 4 | 主要作为方法或规范语言使用 |
| Verdict | REQUIRES_FRESH_REVIEW | 风险排序完成，但仍要求正式提交前独立逐句审查 |

## High-Risk Citation Context Review v0.1

本轮新增 `web/scripts/audit-high-risk-citation-contexts.mjs`。它只处理风险分诊中的 HIGH/BLOCKER 队列，先把最高风险 `CTX2` 拆成来源角色、支持范围、不可支持范围和后续行动。

| 指标 | 数量 | 说明 |
| --- | --- | --- |
| HIGH/BLOCKER contexts | 1 | 当前只有 `CTX2` 需要最高优先级审查 |
| Reviewed contexts | 1 | `CTX2` 已完成本地来源边界审查 |
| Missing reviews | 0 | 当前无 HIGH/BLOCKER 上下文缺本地审查 |
| Verdict | PASS_WITH_LIMITATIONS | `CTX2` 可保留为 `T -> E` 的健康质量调整时间语言；不得让 Grossman、WHO HALE 或 NICE QALY 承担主体连续性、行动能力、未来选择权的完整论证 |

## Citation Context Local Review v0.1

本轮新增 `web/scripts/audit-citation-context-local-review.mjs`。它覆盖 CTX1-CTX12，不读取全文替代 reviewer，而是把每个引用语境的 safe use、forbidden use、reference verification state、local verdict 和 fresh reviewer focus 固定为机器可审查账本。

| 指标 | 数量 | 说明 |
| --- | --- | --- |
| Citation contexts | 12 | CTX1-CTX12 全部进入本地来源边界审查 |
| Reviewed contexts | 12 | 每个上下文均有本地 verdict、边界行动和 reviewer focus |
| Blocked contexts | 0 | 当前无 reference verification FAIL 导致的上下文阻塞 |
| Dedicated high-risk reviews | 1 | `CTX2` 已由 High-Risk Citation Context Review 单独展开 |
| Verdict | LOCAL_REVIEW_COMPLETE_REQUIRES_FRESH_REVIEW | 本地上下文边界齐全，但正式提交前仍需独立 fresh reviewer 逐句判断 |

## Fresh Reviewer Citation Audit Protocol v0.1

本轮新增 `web/scripts/export-fresh-reviewer-citation-audit-protocol.mjs`。它把 Citation Context Review Packet、Risk Triage、Local Review、High-Risk Review、Reference Verification 和 Citation Audit 组合成一个外部审稿协议：不是替代 reviewer，而是把 reviewer 必须检查的队列、独立性要求、pass gate、逐项 prompt 和 blocking condition 固定下来。

| 字段 | 结果 | 说明 |
| --- | --- | --- |
| Verdict | `READY_FOR_FRESH_REVIEWER` | 审稿协议已导出，可以交给 fresh reviewer 执行 |
| Contexts | 12 | CTX1-CTX12 全部进入队列 |
| High or blocker | 1 | `CTX2` 优先审查 |
| Medium | 7 | 高风险清完后再审 |
| Low | 4 | 作为抽样或低风险完整性检查 |

## Fresh Reviewer Citation Results Audit v0.1

本轮新增 `web/scripts/audit-fresh-reviewer-citation-results.mjs`。它生成 reviewer results 模板，并在真实 `FRESH_REVIEWER_CITATION_AUDIT_RESULTS.json` 出现后验证结果是否覆盖全部 CTX、是否包含 source URL、是否存在 `WRONG`、`PRESENT` 或未解决改写等阻塞项。

| 字段 | 结果 | 说明 |
| --- | --- | --- |
| Verdict | `PENDING_EXTERNAL_REVIEW_RESULTS` | 当前没有真实 reviewer results |
| Required contexts | 12 | 必须覆盖 CTX1-CTX12 |
| Completed contexts | 0 | 真实 reviewer 尚未执行或尚未落账 |
| Blocking findings | 0 | pending 状态不伪造阻塞，也不伪造通过 |

## Fixes Applied

- Web References 中 `Generative AI at Work` 补齐 QJE 卷期页码。
- Source Cards 中 `Generative AI at Work` 的 QJE DOI 从错误的 `10.1093/qje/qjaf005` 修正为 `10.1093/qje/qjae044`。
- Web References 中 `Noy & Zhang` 补齐 Science 卷期页码。
- Web References 中 `Dell'Acqua et al.` 从 SSRN / Organization Science 模糊写法改为 Organization Science 2026 DOI 页面。
- Web References 中 target trial entry 改为 Hernan, Wang & Leaf 的 JAMA 2022 PubMed record。
- Source Cards 同步更新 AI productivity 关键条目。
- 论文页和 Markdown 论文新增 Citation Context Register，覆盖 12 组关键来源和不可支持范围。
- 论文页、Markdown 论文和 Evidence Matrix 新增 Claim Evidence Map，覆盖 CL1-CL7 的正文位置、证据边、上下文、反证条件和升级门槛。
- 结构化证据数据新增 Reference Registry，当前 Web References 改为从 JSON 渲染，避免 HTML 手写列表和审计数据分叉。
- 新增 `web/scripts/export-reference-registry.mjs`，从 Reference Registry 生成 `references.bib`、`CITATION_AUDIT.json` 和 `CITATION_AUDIT.md`。
- 新增 `web/scripts/verify-reference-registry.mjs`，生成 `REFERENCE_VERIFICATION.json` 和 `REFERENCE_VERIFICATION.md`，对 DOI/Crossref、arXiv API、官方 URL 和本地 artifact 做联网核验。
- 新增 `web/scripts/audit-claim-context-alignment.mjs`，生成 `CLAIM_CONTEXT_AUDIT.json` 和 `CLAIM_CONTEXT_AUDIT.md`，对核心主张、引用上下文、不可支持边界和 Reference Registry 反向覆盖做本地结构审计。
- 新增 `web/scripts/export-citation-context-review-packet.mjs`，生成 `CITATION_CONTEXT_REVIEW_PACKET.json` 和 `CITATION_CONTEXT_REVIEW_PACKET.md`，给 fresh reviewer 提供逐句 citation-context 输入包。
- 新增 `web/scripts/audit-citation-context-risk-triage.mjs`，生成 `CITATION_CONTEXT_RISK_TRIAGE.json` 和 `CITATION_CONTEXT_RISK_TRIAGE.md`，把 12 个引用语境排成优先审查队列。
- 新增 `web/scripts/audit-high-risk-citation-contexts.mjs`，生成 `HIGH_RISK_CITATION_CONTEXT_REVIEW.json` 和 `HIGH_RISK_CITATION_CONTEXT_REVIEW.md`，对 HIGH/BLOCKER 引用语境先做来源边界审查。
- 新增 `web/scripts/audit-citation-context-local-review.mjs`，生成 `CITATION_CONTEXT_LOCAL_REVIEW.json` 和 `CITATION_CONTEXT_LOCAL_REVIEW.md`，对 CTX1-CTX12 做全量本地来源边界审查。
- 新增 `web/scripts/export-fresh-reviewer-citation-audit-protocol.mjs`，生成 `FRESH_REVIEWER_CITATION_AUDIT_PROTOCOL.json` 和 `FRESH_REVIEWER_CITATION_AUDIT_PROTOCOL.md`，把剩余逐句引用语境审查转成外部 reviewer 可执行协议。
- 新增 `web/scripts/audit-fresh-reviewer-citation-results.mjs`，生成 reviewer results template 和 results audit，当前状态保持 `PENDING_EXTERNAL_REVIEW_RESULTS`。
- 新增 `web/scripts/audit-effective-immortality-coverage.mjs`，生成 `COVERAGE_AUDIT.json` 和 `COVERAGE_AUDIT.md`，覆盖 54 个 source alias、4 个 AI task reference key、14 个 AI task 必填字段、7 个 method-audit 字段、47 张 Source Card 和 53 条 Reference Registry。
- 生成的 Citation Audit 产物明确保留 `WARN`：它是本地元数据注册表导出，不是 fresh reviewer thread 的逐句引用审查。
- 有效永生飞轮论文组内的干预符号统一为 `U_t`，避免和技术采用能力 `A_t` 冲突。
- 新增 `aiTaskEvidenceRegister`，把四条 `A -> Q` AI 任务证据补齐任务族、人群/任务、干预、比较对象、效应摘要、QA 成本、风险边界和模型用途。
- `aiTaskEvidenceRegister` 已做 full-text verification 升级，补齐样本与设计、效应估计、统计不确定性、证据等级、COI/场景边界和 verification status。
- `aiTaskEvidenceRegister` 已做 method-audit 升级，补齐 Brynjolfsson/Noy/Peng/Dell'Acqua 四项实验的主表/主图、主要规格、统计列、标准误或区间、质量评分协议、QA 成本量化和外推限制。
- `researchDeclarations` 已补数据可得性、代码可得性、伦理安全、AI 辅助披露、利益冲突、资金、作者贡献和使用限制，并进入 coverage audit。
- `estimandRegistry` 已补 9 条证据边的 population、intervention/exposure、comparator、time zero、outcome、estimand、identification risk 和 current status，并进入 coverage audit。
- `analysisPlanRegistry` 已补 9 条证据边的 study question、candidate design、minimum data、primary estimator、diagnostics、sensitivity checks、reporting output 和 current status，并进入 coverage audit。
- `aiResearchFailureModeAudit` 已补 FM1-FM7 七类 AI 辅助科研失败模式，并进入 coverage audit，作为后续自动化科研的 integrity gate。
- CTX9 拆分为试验注册、机器 API、国际注册网络、TRIPOD+AI、PROBAST+AI、CONSORT-AI 和 SPIRIT-AI，避免继续用 `TRIPOD/PROBAST` 合并入口遮蔽具体治理工具。

## Remaining Audit Queue

1. 对官方网页条目做周期性复核，尤其是 NICE PMG36、TRIPOD+AI、PROBAST+AI、ClinicalTrials.gov API 和 WHO ICTRP 的页面版本或访问边界变化。
2. 对 `A -> Q` 注册表继续做正式发表版本差异核对，补更多长期 QA 成本、隐藏错误、维护成本、边界外任务和人群异质性证据。
3. 正式提交前运行 fresh reviewer thread 的逐条引用语境审查，验证每个正文 claim 是否被对应来源真实支持；当前 CTX1-CTX12 已有本地来源边界审查，最高风险 `CTX2` 已有本地 `PASS_WITH_LIMITATIONS` 边界审查，且已导出外部 reviewer 协议和 reviewer results 模板，但仍不能替代独立 reviewer verdict。
4. 后续若转为 LaTeX 正式论文，需要把正文 `\cite{}` 语境与当前 `references.bib` 对齐，再重新生成最终 `CITATION_AUDIT.json`。

## Verdict

Current verdict: `WARN`

Reason: 核心引用已经指向真实来源，AI productivity、target trial、longitudinal causal inference 和 governance 关键条目完成第一轮规范化，12 组关键来源已有上下文边界，7 条核心主张已有 claim alignment 契约，Claim Context Audit v0.1 已确认 7 条 claim evidence rows、12 个 citation contexts、53 条 Reference Registry 和 0 gaps，Citation Context Risk Triage v0.1 已把 12 个上下文排成 fresh reviewer 优先级队列，High-Risk Citation Context Review v0.1 已对最高风险 `CTX2` 给出 `PASS_WITH_LIMITATIONS` 来源边界，Citation Context Local Review v0.1 已确认 CTX1-CTX12 全部 reviewed 且 0 blocked，Fresh Reviewer Citation Audit Protocol v0.1 已导出 12 个 contexts 的外部审稿队列、pass gate 和逐项 prompt，Fresh Reviewer Citation Results Audit v0.1 已生成 reviewer results 模板并保持 `PENDING_EXTERNAL_REVIEW_RESULTS`，9 条证据边已有 estimand protocol 契约和 analysis plan 契约，7 条 AI research failure mode 已进入完整性门禁，4 条 `A -> Q` AI 任务证据已进入任务级注册表并补 full-text verification 和 method-audit 字段，8 条 research declarations 已进入结构化数据和 coverage audit，53 条 Web References 已进入 Reference Registry，Reference Verification v0.1 已确认 53 PASS、0 WARN、0 FAIL，并已生成 `references.bib`、`CITATION_AUDIT.json`、`CITATION_AUDIT.md`、`CITATION_CONTEXT_REVIEW_PACKET.json`、`CITATION_CONTEXT_REVIEW_PACKET.md`、`CITATION_CONTEXT_RISK_TRIAGE.json`、`CITATION_CONTEXT_RISK_TRIAGE.md`、`HIGH_RISK_CITATION_CONTEXT_REVIEW.json`、`HIGH_RISK_CITATION_CONTEXT_REVIEW.md`、`CITATION_CONTEXT_LOCAL_REVIEW.json`、`CITATION_CONTEXT_LOCAL_REVIEW.md`、`FRESH_REVIEWER_CITATION_AUDIT_PROTOCOL.json`、`FRESH_REVIEWER_CITATION_AUDIT_PROTOCOL.md`、`FRESH_REVIEWER_CITATION_AUDIT_RESULTS_TEMPLATE.json`、`FRESH_REVIEWER_CITATION_AUDIT_RESULTS_TEMPLATE.md`、`FRESH_REVIEWER_CITATION_AUDIT_RESULTS_AUDIT.json`、`FRESH_REVIEWER_CITATION_AUDIT_RESULTS_AUDIT.md`、`CLAIM_CONTEXT_AUDIT.json`、`CLAIM_CONTEXT_AUDIT.md`、`REFERENCE_VERIFICATION.json`、`REFERENCE_VERIFICATION.md`、`COVERAGE_AUDIT.json` 和 `COVERAGE_AUDIT.md`；但正式提交前仍需 fresh reviewer thread 的逐句引用语境审查。
