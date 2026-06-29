# 有效永生飞轮 Search Execution Register v0.1

日期：2026-06-29

用途：把 ARS deep-research Phase 2 的 Literature Gap Map 转成可执行检索队列。这里记录的是候选来源，不是正式 Reference Registry；任何候选在进入正文强主张前，仍需完成全文阅读、元数据核验、Source Card、Citation Context Register 和 fresh reviewer 引用语境审查。

## 处理原则

- 候选来源只代表“值得筛选”，不代表已经支持本文主张。
- 每条候选必须绑定到一条链路边，不能只因为主题相近而进入队列。
- 初筛决策沿用 `SOURCE_CARD`、`METHOD_GATE`、`BACKGROUND_ONLY`、`REJECT` 四类。
- `METHOD_GATE` 只约束方法、报告、审计或建模流程，不提供实证效果。
- `SOURCE_CARD` 候选只有在全文边界明确后，才能进入 Source Cards 和 Reference Registry。
- 当前所有候选的机器状态均为 `candidate_queue_only`，表示它们只进入检索执行队列。

## Candidate Queue

| ID | Edge | Candidate | Source | Initial decision | Boundary |
| --- | --- | --- | --- | --- | --- |
| SER1 | `T -> E` | Restricted Mean Survival Time for Survival Analysis: A Quick Guide for Clinical Researchers | PubMed / PMC | `METHOD_GATE` | 可帮助表达固定时间窗内的有效时间或生存时间差；不能定义主体连续性，也不能证明干预延寿。 |
| SER2 | `E -> R` | A Systematic Review of Learning Analytics-Incorporated Interventions Implemented on Learning Management Systems | Journal of Learning Analytics | `SOURCE_CARD` | 可帮助把有效时间转成学习动作、反馈事件和 LMS 干预记录；不能证明寿命延长自动产生高质量学习轮次。 |
| SER3 | `R -> C` | A Systematic Review of Self-Regulated Learning through Integration with Data Science Techniques | Springer | `SOURCE_CARD` | 可补学习轮次、监控、控制行为和数据痕迹到能力积累代理指标；不能解决迁移、遗忘和饱和问题。 |
| SER4 | `C -> A` | The Impact of Dynamic Capabilities on Resource Access and Development | INFORMS / Organization Science | `SOURCE_CARD` | 可补能力积累如何影响资源获取与资源发展；不能直接泛化到生物医学或神经技术采用。 |
| SER5 | `A -> Q` | Generative AI and labour productivity: a field experiment on coding | BIS Working Papers | `SOURCE_CARD` | 可补 AI 编程任务中的生产率与异质性；不能外推为通用智能、健康寿命或主体持续性收益。 |
| SER6 | `Q -> O` | Empirical Challenges in the Capability Approach: Measuring Capability as an Opportunity Set | IZA / RePEc | `METHOD_GATE` | 可补可能性空间测量方法；不能证明任务质量提升必然扩大真实选择权。 |
| SER7 | `O -> T/E` | Effects of Social Support Interventions on Medical Patient Survival | PubMed / PMC | `SOURCE_CARD` | 可检验社会支持作为干预是否影响生存相关结局；不能替代具体干预的因果协议。 |
| SER8 | `A/Q -> risk` | Challenges to the Monitoring of Deployed AI Systems | NIST | `METHOD_GATE` | 可补部署后监测、事故、近失事件和风险控制语言；不能量化具体 AI 干预净收益。 |
| SER9 | `U_t -> causal claim` | Target trial emulation: bridging observational studies and randomized trials | PubMed / PMC | `METHOD_GATE` | 可补 time zero、comparator、outcome、estimand 和协议化因果门禁；不能验证任何 Human Infra 干预。 |

## Next Actions

1. 对 SER1-SER9 做全文阅读或官方页面核查。
2. 将通过筛选的来源写成 Source Card，并补 `claim`、`variables`、`mechanism`、`evidenceRole`、`boundary`、`doesNotSupport`。
3. 只把通过核验的来源加入 `referenceRegistry`，并重新运行 `npm run export:references` 与 `npm run verify:references`。
4. 候选来源必须先进入 `searchExecutionVerificationRegister`，记录 URL/DOI/题名/出版状态/使用边界和阻塞项。
5. 若来源承担正文主张，必须新增或更新 `citationContextRegister`，再运行 `npm run audit:paper-integrity`。
6. 若来源只是方法门禁，只允许进入模型契约、审计协议或方法说明，不得写成效果证据。

## Current Interpretation

Search Execution Register 让“继续找论文”不再是口号，而是可追踪队列：每条缺口都有候选、数据库、检索式、初筛决策、边界和下一步动作。它推进论文从定性框架走向可复现科研系统，但不会绕过全文阅读和外部引用审查。
