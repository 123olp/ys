# 有效永生飞轮 Systematic Search Protocol v0.1

Status: ARS deep-research Phase 2 investigation protocol  
Date: 2026-06-29  
Target paper: [Effective Immortality Acceleration Flywheel](../explanations/effective-immortality-acceleration-flywheel.md)  
Web mirror: [`web/src/data/effective-immortality-evidence.json`](../../web/src/data/effective-immortality-evidence.json)

## Purpose

本文件把上一轮 Research Design Brief 中的检索种子升级成可复现检索协议。目标不是一次性证明飞轮成立，而是系统收集能支持、限制或反驳 `T/E/R/C/A/Q/O` 每条链路边的来源。

## Review Question

哪些研究传统、方法标准、任务实验证据和治理框架能支持或约束 `T/E/R/C/A/Q/O` 主体持续性飞轮的每一条链路边？

## Database Plan

| Source | Use |
| --- | --- |
| PubMed / MEDLINE | 健康寿命、衰老机制、生物年龄、社会关系、医学 AI 和临床报告标准。 |
| Crossref / DOI resolver | 核验正式出版物元数据，补 DOI、期刊、卷期页和出版年份。 |
| Semantic Scholar / OpenAlex | 查找引用网络、相邻论文、去重候选和文献簇。 |
| arXiv / SSRN / NBER | AI 生产率、工具增强、早期方法论文和预印本证据。 |
| ClinicalTrials.gov / WHO ICTRP | 医学干预、AI 医疗工具、可穿戴和预防策略的试验注册入口。 |
| Official standards and institutional sources | NIST AI RMF、EQUATOR guidelines、WHO、OECD、FDA 等治理与报告标准。 |

## Inclusion Criteria

| Criterion | Include | Exclude |
| --- | --- | --- |
| Link relevance | 直接支持或约束 `T/E/R/C/A/Q/O`、`A/Q -> risk` 或 `U_t -> causal claim` 中至少一条边。 | 只讨论健康、技术或未来主义，但无法映射到任何链路边。 |
| Evidence role clarity | 能明确标注为方法标准、机制综述、关联证据、任务实验、治理框架或规范框架。 | 证据角色不清、只提供结论口号或无法区分事实和预测。 |
| Source traceability | 可回到 DOI、PMID、arXiv ID、机构页面、注册号或本地 artifact。 | 无法追溯原始来源或只有二手摘要。 |
| Boundary usefulness | 能说明支持范围、不可支持范围、反证条件或外推边界。 | 只强化正向叙事，不能提供边界或失败条件。 |

## Screening Flow

```text
Pass 1 title and abstract
  -> include / exclude / uncertain
  -> 记录链路边、证据角色、排除原因和是否需要全文

Pass 2 full text or official page
  -> source card / background only / reject
  -> 记录 claim、变量、机制、证据等级、边界、不可支持范围和模型用途

Deduplication
  -> merge / keep separate / mark version relation
  -> 优先 DOI、PMID、arXiv ID、Semantic Scholar ID 和标题标准化去重

Distributional skew advisory
  -> keep scope / expand search
  -> 检查时间、地域、方法、证据类型和出版状态是否过度集中
```

## Screening Rubric

| Decision | Meaning | Required action |
| --- | --- | --- |
| SOURCE_CARD | 来源能直接支撑或约束至少一条链路边，并且可明确写出支持范围和不可支持范围。 | 进入 Source Cards、Reference Registry 和 Citation Context Register。 |
| BACKGROUND_ONLY | 来源能帮助理解语境或术语，但不能承担核心主张证据。 | 可进入背景阅读清单，不进入强 claim-to-source map。 |
| METHOD_GATE | 来源主要是方法或报告标准，用来约束模型、因果协议、预测报告或审计流程。 | 进入 Evidence Classes、Model Contract 或审计门禁。 |
| REJECT | 来源不可追溯、证据角色不清、过度宣传或无法映射到链路边。 | 记录排除原因，不进入正文引用。 |

## Literature Gap Map

| Edge | Gap | Next search |
| --- | --- | --- |
| `T -> E` | 缺少把主体性、行动能力和健康质量统一成 `E_t` 路径积分的可操作测量方案。 | `restricted mean survival time healthspan disability-free survival agency` |
| `E -> R` | 缺少把有效时间转换为高质量反馈轮次的日志数据和编码规则。 | `time use feedback loops self-regulated learning longitudinal log data` |
| `R -> C` | 缺少跨任务迁移、遗忘、饱和和错误反馈的衰减模型。 | `skill acquisition transfer forgetting learning curve saturation feedback quality` |
| `C -> A` | 缺少从资源、信誉和协作网络到高风险技术整合能力的实证路径。 | `technology adoption resources expertise trust network high risk technology` |
| `A -> Q` | 缺少长期任务、QA 成本、依赖、返工和能力退化的纵向证据。 | `generative AI productivity longitudinal quality assurance rework dependency` |
| `Q -> O` | 缺少把产出质量转成真实可进入路径集合的测量规则。 | `capability set measurement opportunity set agency resources access` |
| `O -> T/E` | 缺少区分资源入口、照护可及、恢复系统和风险缓冲的动态因果模型。 | `healthcare access social support survival longitudinal causal model` |
| `A/Q -> risk` | 缺少部署后事故率、近失事件、停止条件和回滚成功率的实证资料。 | `AI deployment incident monitoring automation bias rollback post deployment safety` |
| `U_t -> causal claim` | 缺少把每个技术族统一改写成 target-trial protocol 的实例库和失败案例库。 | `target trial emulation technology intervention time zero estimand causal protocol examples` |

## Search Execution Register

下一步执行层已经沉淀为 `2026-06-29-effective-immortality-flywheel-search-execution-register.md` 和 `web/src/data/effective-immortality-evidence.json` 的 `searchExecutionRegister`。该队列把每条缺口映射到候选来源、数据库、检索式、初筛决策、边界用途和下一步动作。

当前登记表覆盖九条边：

- `T -> E`
- `E -> R`
- `R -> C`
- `C -> A`
- `A -> Q`
- `Q -> O`
- `O -> T/E`
- `A/Q -> risk`
- `U_t -> causal claim`

候选记录仍处于 `candidate_queue_only` 状态，不等同于正式引用。候选进入正文前必须完成全文阅读、Source Card、Reference Registry、Citation Context Register 和 fresh reviewer 引用语境审查。

## Required Outputs

每一轮检索必须产出：

- Search Strategy Report；
- Screening Log；
- Annotated Bibliography；
- Source Cards；
- Reference Registry updates；
- Citation Context Register updates；
- Evidence Matrix updates；
- Distributional Skew Advisory。

## Current Interpretation

这一步把“继续找论文”改成了可执行的 Phase 2 协议。后续新增来源时，不能只把论文塞进参考文献，而要给出链路边、证据角色、支持范围、不可支持范围、筛选决策和后续模型用途。
