# Citation Context Local Review

Date: 2026-06-29T00:00:00.000Z
Input: `web/src/data/effective-immortality-flywheel/CITATION_CONTEXT_REVIEW_PACKET.json`
Output JSON: `web/src/data/effective-immortality-flywheel/CITATION_CONTEXT_LOCAL_REVIEW.json`

## Summary

Verdict: `LOCAL_REVIEW_COMPLETE_REQUIRES_FRESH_REVIEW`

Reason: `all_contexts_have_local_source_boundaries`

All registered citation contexts have local safe-use, forbidden-use, reference-state, and fresh-reviewer focus records. Fresh independent sentence-level citation review remains required before formal submission.

This is a local source-boundary review for every registered citation context. It improves traceability and fresh-reviewer readiness, but it is not an independent sentence-level citation audit.

| Metric | Count |
| --- | ---: |
| Contexts | 12 |
| Reviewed contexts | 12 |
| Blocked contexts | 0 |
| High-risk contexts with dedicated review | 1 |

## Context Review Table

| Context | Risk tier | Local verdict | Claims | References | Boundary action |
| --- | --- | --- | --- | ---: | --- |
| CTX1 | LOW | KEEP_AS_METHOD_OR_FRAME_LANGUAGE | CL2, CL3, CL7 | 2 | Fresh reviewer can sample after higher-risk contexts are resolved. |
| CTX2 | HIGH | KEEP_WITH_STRICT_BOUNDARY | CL1, CL2 | 3 | Keep only the registered safe-use sentence. Fresh reviewer must inspect exact source-to-claim support before formal submission. |
| CTX3 | MEDIUM | KEEP_WITH_BOUNDARY | CL7 | 3 | Keep the does-not-support boundary visible in prose, tables, and figure captions. |
| CTX4 | LOW | KEEP_WITH_BOUNDARY | CL1, CL2 | 4 | Keep the does-not-support boundary visible in prose, tables, and figure captions. |
| CTX5 | MEDIUM | KEEP_WITH_BOUNDARY | CL1, CL2, CL5 | 3 | Keep the does-not-support boundary visible in prose, tables, and figure captions. |
| CTX6 | LOW | KEEP_WITH_BOUNDARY | CL1, CL2 | 3 | Keep the does-not-support boundary visible in prose, tables, and figure captions. |
| CTX7 | MEDIUM | KEEP_WITH_BOUNDARY | CL1, CL2, CL4, CL7 | 4 | Keep the does-not-support boundary visible in prose, tables, and figure captions. |
| CTX8 | LOW | KEEP_AS_METHOD_OR_FRAME_LANGUAGE | CL2, CL4, CL6, CL7 | 6 | Fresh reviewer can sample after higher-risk contexts are resolved. |
| CTX9 | MEDIUM | KEEP_WITH_BOUNDARY | CL3, CL6, CL7 | 11 | Keep the does-not-support boundary visible in prose, tables, and figure captions. |
| CTX10 | MEDIUM | KEEP_WITH_BOUNDARY | CL6 | 4 | Keep the does-not-support boundary visible in prose, tables, and figure captions. |
| CTX11 | MEDIUM | KEEP_WITH_BOUNDARY | CL6 | 4 | Keep the does-not-support boundary visible in prose, tables, and figure captions. |
| CTX12 | MEDIUM | KEEP_WITH_BOUNDARY | CL1, CL2, CL5 | 2 | Keep the does-not-support boundary visible in prose, tables, and figure captions. |

## Context Details

### CTX1: Kaplan-Meier 1958; Cox 1972

- Risk tier: LOW
- Local verdict: KEEP_AS_METHOD_OR_FRAME_LANGUAGE
- Claims: CL2, CL3, CL7
- Used for: 定义 T、生存函数 S(t)、删失数据和风险函数 lambda(t) 的统计语言。
- Safe use: 事件时间、删失、生存曲线和协变量风险建模的基础方法。
- Forbidden use: 不证明任何具体延寿、健康、AI 或资源干预有效。
- Boundary action: Fresh reviewer can sample after higher-risk contexts are resolved.
- Fresh reviewer focus:
  - 确认 forbidden use 没有在正文、图注、表格或摘要中被暗示。
  - 确认正文只使用 safe use，不把来源升级为飞轮整体成立的证据。

| Reference | Audit status | Live status | Registered use |
| --- | --- | --- | --- |
| `cox1972regression` | crossref-verified | PASS | 定义协变量、风险函数和 lambda(t) 的统计语言。 |
| `kaplan1958incomplete` | crossref-verified | PASS | 定义生存曲线、删失数据和 T 的统计语言。 |

### CTX2: Grossman Health Capital; WHO HALE; NICE QALY

- Risk tier: HIGH
- Local verdict: KEEP_WITH_STRICT_BOUNDARY
- Claims: CL1, CL2
- Used for: 把日历寿命转译为健康质量、有效时间和质量调整时间。
- Safe use: T -> E 的测量语言和健康质量调整视角。
- Forbidden use: 不能完整定义主体连续性，也不能替代个体医学判断。
- Boundary action: Keep only the registered safe-use sentence. Fresh reviewer must inspect exact source-to-claim support before formal submission.
- Fresh reviewer focus:
  - 优先检查是否把测量语言、规范语言或任务内效果外推成主体持续性、寿命或未来选择权结论。
  - 拒绝从方法、关联或指标语言直接跳到具体延寿效果。
  - 确认 forbidden use 没有在正文、图注、表格或摘要中被暗示。
  - 确认正文只使用 safe use，不把来源升级为飞轮整体成立的证据。

| Reference | Audit status | Live status | Registered use |
| --- | --- | --- | --- |
| `grossman1972healthcapital` | crossref-verified | PASS | 把健康资本、有效时间和日历时间区分开。 |
| `niceEconomicEvaluation` | official-url-200 | PASS | 提供 QALY 与健康经济评价的政策语言。 |
| `whohale7752` | official-url-200 | PASS | 提供健康寿命指标的官方定义入口。 |

### CTX3: Hallmarks of Aging; GrimAge; Cognitive Reserve

- Risk tier: MEDIUM
- Local verdict: KEEP_WITH_BOUNDARY
- Claims: CL7
- Used for: 提出身体状态、衰老机制、生物年龄信号和认知储备候选变量。
- Safe use: 状态变量和风险信号的机制/关联入口。
- Forbidden use: 不能把机制综述、预测关联或认知储备直接写成干预效果。
- Boundary action: Keep the does-not-support boundary visible in prose, tables, and figure captions.
- Fresh reviewer focus:
  - 确认 forbidden use 没有在正文、图注、表格或摘要中被暗示。
  - 确认正文只使用 safe use，不把来源升级为飞轮整体成立的证据。

| Reference | Audit status | Live status | Registered use |
| --- | --- | --- | --- |
| `lopezotin2013hallmarks` | crossref-verified | PASS | 提出衰老状态变量和机制入口。 |
| `lu2019grimage` | crossref-verified | PASS | 作为生物年龄、死亡风险和健康寿命信号入口。 |
| `stern2012cognitiveReserve` | crossref-verified | PASS | 说明认知储备作为状态变量和风险信号的边界。 |

### CTX4: Deliberate Practice; Law of Practice; Self-Regulated Learning; Feedback Intervention Theory

- Risk tier: LOW
- Local verdict: KEEP_WITH_BOUNDARY
- Claims: CL1, CL2
- Used for: 解释 E -> R -> C：有效时间如何在有目标、有反馈和可修正的任务中沉淀为能力。
- Safe use: 学习轮次、反馈质量、练习曲线和能力积累的条件。
- Forbidden use: 时间本身不会自动产生能力；错误反馈和低质量重复可能反向损害表现。
- Boundary action: Keep the does-not-support boundary visible in prose, tables, and figure captions.
- Fresh reviewer focus:
  - 确认 forbidden use 没有在正文、图注、表格或摘要中被暗示。
  - 确认正文只使用 safe use，不把来源升级为飞轮整体成立的证据。

| Reference | Audit status | Live status | Registered use |
| --- | --- | --- | --- |
| `ericsson1993deliberatePractice` | crossref-verified | PASS | 解释有效时间进入有反馈练习轮次的条件。 |
| `kluger1996feedback` | crossref-verified | PASS | 说明反馈可能提升表现，也可能因设计错误降低表现。 |
| `newell1981lawPractice` | crossref-verified-corrected-doi | PASS | 为重复轮次、练习曲线和能力增长提供认知模型入口。 |
| `zimmerman2002selfRegulated` | doi-verified | PASS | 说明学习轮次需要目标设定、自我监控、反馈和策略调整。 |

### CTX5: Human Capital; Social Capital; Social Relationships Mortality

- Risk tier: MEDIUM
- Local verdict: KEEP_WITH_BOUNDARY
- Claims: CL1, CL2, CL5
- Used for: 说明经验、资源、信誉和协作网络如何进入 C 与 O，并可能反哺 T/E。
- Safe use: 积累资本、社会支持和死亡风险关联的讨论。
- Forbidden use: 不能把社会关系关联直接升级成具体干预的因果延寿结论。
- Boundary action: Keep the does-not-support boundary visible in prose, tables, and figure captions.
- Fresh reviewer focus:
  - 确认 forbidden use 没有在正文、图注、表格或摘要中被暗示。
  - 确认正文只使用 safe use，不把来源升级为飞轮整体成立的证据。

| Reference | Audit status | Live status | Registered use |
| --- | --- | --- | --- |
| `coleman1988socialCapital` | doi-verified | PASS | 说明关系、信任、规范和网络如何成为能力形成条件。 |
| `holtlunstad2010social` | crossref-verified | PASS | 讨论社会关系与死亡风险的关联证据边界。 |
| `mincer1974humanCapital` | official-archive | PASS | 说明教育、经验和长期积累如何进入人力资本模型。 |

### CTX6: TAM; UTAUT; Diffusion of Innovations

- Risk tier: LOW
- Local verdict: KEEP_WITH_BOUNDARY
- Claims: CL1, CL2
- Used for: 解释 C -> A：技术采用受有用性、易用性、促进条件、资源和社会影响约束。
- Safe use: 技术采用能力的分解：access、understanding、evaluation、trial、integration。
- Forbidden use: 不能证明采用后的技术一定有效，也不能覆盖所有高风险医学或神经技术。
- Boundary action: Keep the does-not-support boundary visible in prose, tables, and figure captions.
- Fresh reviewer focus:
  - 确认 forbidden use 没有在正文、图注、表格或摘要中被暗示。
  - 确认正文只使用 safe use，不把来源升级为飞轮整体成立的证据。

| Reference | Audit status | Live status | Registered use |
| --- | --- | --- | --- |
| `davis1989tam` | crossref-verified | PASS | 解释技术采用能力中的有用性和易用性。 |
| `rogers2003diffusion` | bibliographic-record-verified-isbn | PASS | 说明技术成熟、扩散、采用者差异和社会系统时间窗口。 |
| `venkatesh2003utaut` | crossref-verified | PASS | 解释技术采用中的促进条件、社会影响和努力预期。 |

### CTX7: Generative AI at Work; Noy and Zhang; GitHub Copilot; Jagged Technological Frontier

- Risk tier: MEDIUM
- Local verdict: KEEP_WITH_BOUNDARY
- Claims: CL1, CL2, CL4, CL7
- Used for: 支持 A -> Q 在限定任务中的生产率、速度、质量或任务边界证据。
- Safe use: 生成式 AI 在客服、写作、编程或知识工作实验中的任务内效果与异质性。
- Forbidden use: 不能泛化为通用智能增强、健康寿命延长或永生收益。
- Boundary action: Keep the does-not-support boundary visible in prose, tables, and figure captions.
- Fresh reviewer focus:
  - 确认 forbidden use 没有在正文、图注、表格或摘要中被暗示。
  - 确认正文只使用 safe use，不把来源升级为飞轮整体成立的证据。

| Reference | Audit status | Live status | Registered use |
| --- | --- | --- | --- |
| `brynjolfsson2025generative` | crossref-verified-corrected-doi | PASS | 支持限定客服任务中的 AI productivity 证据。 |
| `dellacqua2026jagged` | crossref-verified | PASS | 支持 AI 收益与风险具有任务边界。 |
| `noy2023productivity` | crossref-verified | PASS | 支持写作任务内的生成式 AI 生产率证据。 |
| `peng2023copilot` | arxiv-api-verified | PASS | 支持限定编程任务中的 AI pair programmer 生产率入口。 |

### CTX8: NIST AI RMF; Guidelines for Human-AI Interaction; NASA-TLX; Automation taxonomy

- Risk tier: LOW
- Local verdict: KEEP_AS_METHOD_OR_FRAME_LANGUAGE
- Claims: CL2, CL4, CL6, CL7
- Used for: 给 A/Q -> risk、QA 成本、任务负荷、自动化等级和人机控制权提供治理语言。
- Safe use: 风险识别、测量、纠错、回滚和人机协作设计边界。
- Forbidden use: 治理框架和交互指南不提供收益估计，也不证明 AI 能延寿。
- Boundary action: Fresh reviewer can sample after higher-risk contexts are resolved.
- Fresh reviewer focus:
  - 确认 forbidden use 没有在正文、图注、表格或摘要中被暗示。
  - 确认正文只使用 safe use，不把来源升级为飞轮整体成立的证据。

| Reference | Audit status | Live status | Registered use |
| --- | --- | --- | --- |
| `amershi2019hai` | crossref-verified | PASS | 提供人机协作设计、纠错和控制权边界。 |
| `burwell2017bciEthics` | doi-verified | PASS | 为脑机接口、神经技术、同意、身份和主体边界提供风险治理入口。 |
| `dellacqua2026jagged` | crossref-verified | PASS | 支持 AI 收益与风险具有任务边界。 |
| `nasaTlx` | official-web-registered | PASS | 提供任务负荷、时间压力、努力和挫败感测量入口。 |
| `nist2023airmf` | official-url-200 | PASS | 提供 AI 风险识别、测量、治理和回滚语言。 |
| `parasuraman2000automation` | crossref-verified | PASS | 拆分自动化类型、等级和人机控制权。 |

### CTX9: Target Trial Emulation; ClinicalTrials.gov; WHO ICTRP; TRIPOD+AI; PROBAST+AI; CONSORT-AI; SPIRIT-AI

- Risk tier: MEDIUM
- Local verdict: KEEP_WITH_BOUNDARY
- Claims: CL3, CL6, CL7
- Used for: 定义 U_t -> causal claim 的因果门禁和预测模型报告门禁。
- Safe use: population、intervention、comparator、time zero、outcome、estimand、试验登记、AI 干预报告、验证、校准和偏倚审查。
- Forbidden use: 不能消除所有不可测混杂，也不证明任何注册试验或预测模型有效。
- Boundary action: Keep the does-not-support boundary visible in prose, tables, and figure captions.
- Fresh reviewer focus:
  - 拒绝从任务内 AI 效果直接跳到通用能力增强、健康寿命收益或永生收益。
  - 确认 forbidden use 没有在正文、图注、表格或摘要中被暗示。
  - 确认正文只使用 safe use，不把来源升级为飞轮整体成立的证据。

| Reference | Audit status | Live status | Registered use |
| --- | --- | --- | --- |
| `clinicaltrialsGov` | official-url-200 | PASS | 提供临床试验登记、人群、比较组、结局和结果回填入口。 |
| `clinicaltrialsGovApi` | official-url-200 | PASS | 提供结构化试验注册与结果数据的机器读取入口，用于后续试验证据采集和协议字段回填。 |
| `consortAi2020` | doi-verified | PASS | 约束 AI 干预临床试验结果报告中的干预说明、输入输出、人机交互和错误案例分析。 |
| `gradeHandbook` | official-web | PASS | 提供证据确定性、收益风险权衡和从证据到建议的政策语言。 |
| `hernan2022targetTrial` | crossref-verified | PASS | 定义因果协议门禁和观察数据因果推断边界。 |
| `probastAi2025` | doi-and-official-site-verified | PASS | 提供 AI 预测模型研究的偏倚风险、适用性、可信度、公平性和质量审查门禁。 |
| `robins2000marginalStructural` | pubmed-verified | PASS | 说明时间变化混杂下的因果估计入口和边界。 |
| `spiritAi2020` | doi-verified | PASS | 约束 AI 干预临床试验方案中的协议透明度、输入输出、人机交互和错误分析计划。 |
| `tripodAi2024` | doi-and-official-site-verified | PASS | 提供 AI/机器学习临床预测模型的报告清单、外部验证、校准和透明度门禁。 |
| `tripodProbast` | official-urls-200 | PASS | 约束预测模型报告质量、偏倚风险、校准和外部验证。 |
| `whoIctrp` | official-url-200 | PASS | 提供国际临床试验注册网络、WHO 数据集和试验透明度原则的上位入口。 |

### CTX10: Apple Heart Study; Personal Informatics; Lived Informatics; Dynamic Digital Twin

- Risk tier: MEDIUM
- Local verdict: KEEP_WITH_BOUNDARY
- Claims: CL6
- Used for: 说明观测、反馈、个人数据系统和生命过程建模如何进入状态观测层。
- Safe use: observation -> action 的路径和自我追踪/数字孪生的系统问题。
- Forbidden use: 早筛、追踪或数字孪生概念不等于死亡风险下降或医疗结局改善。
- Boundary action: Keep the does-not-support boundary visible in prose, tables, and figure captions.
- Fresh reviewer focus:
  - 确认 forbidden use 没有在正文、图注、表格或摘要中被暗示。
  - 确认正文只使用 safe use，不把来源升级为飞轮整体成立的证据。

| Reference | Audit status | Live status | Registered use |
| --- | --- | --- | --- |
| `epstein2015lived` | crossref-verified | PASS | 说明长期自我追踪系统的生活嵌入、维护负担和断裂点。 |
| `li2010personalInformatics` | crossref-verified | PASS | 提供个人信息学的准备、收集、整合、反思和行动阶段。 |
| `mulder2022dynamicDigitalTwin` | publisher-verified | PASS | 说明生命过程中的状态观测、预测、预防和数字孪生建模入口。 |
| `perez2019appleHeart` | crossref-verified | PASS | 说明可穿戴设备进入大规模风险提示和临床确认通道。 |

### CTX11: Extended Mind; Engelbart; Cognition in the Wild

- Risk tier: MEDIUM
- Local verdict: KEEP_WITH_BOUNDARY
- Claims: CL6
- Used for: 支撑工具、记忆外化、分布式认知和认知增强进入主体系统的理论位置。
- Safe use: 主体能力可以由人、工具、表征、环境和协作流程共同支撑。
- Forbidden use: 哲学和系统框架不提供数值效应估计，也不能证明数字副本等同于本人。
- Boundary action: Keep the does-not-support boundary visible in prose, tables, and figure captions.
- Fresh reviewer focus:
  - 确认 forbidden use 没有在正文、图注、表格或摘要中被暗示。
  - 确认正文只使用 safe use，不把来源升级为飞轮整体成立的证据。

| Reference | Audit status | Live status | Registered use |
| --- | --- | --- | --- |
| `burwell2017bciEthics` | doi-verified | PASS | 为脑机接口、神经技术、同意、身份和主体边界提供风险治理入口。 |
| `clark1998extended` | crossref-verified | PASS | 支撑工具、记忆外化和认知扩展进入主体系统。 |
| `engelbart1962augmenting` | official-archive-registered | PASS | 提供人、工具、概念和方法作为增强系统的经典框架。 |
| `hutchins1995cognition` | author-page-verified | PASS | 提供分布式认知和环境嵌入式问题求解框架。 |

### CTX12: Capability Approach; WHO SDOH; WHO Primary Health Care

- Risk tier: MEDIUM
- Local verdict: KEEP_WITH_BOUNDARY
- Claims: CL1, CL2, CL5
- Used for: 定义 O 可能性空间为真实可进入路径，并把资源、制度、医疗和社会条件纳入反哺路径。
- Safe use: 真实选择权、健康决定因素、医疗可及和连续照护的规范/公共卫生框架。
- Forbidden use: 规范框架不提供寿命预测，也不能替代具体政策或医疗干预评估。
- Boundary action: Keep the does-not-support boundary visible in prose, tables, and figure captions.
- Fresh reviewer focus:
  - 确认 forbidden use 没有在正文、图注、表格或摘要中被暗示。
  - 确认正文只使用 safe use，不把来源升级为飞轮整体成立的证据。

| Reference | Audit status | Live status | Registered use |
| --- | --- | --- | --- |
| `robeyns2021capability` | official-web-registered | PASS | 定义真实可行能力和可能性空间。 |
| `whoSdhPhc` | official-urls-200 | PASS | 把健康和持续性放回收入、教育、住房、工作、环境和医疗可及条件中。 |


## Scope

This artifact checks whether the manuscript has a registered safe-use boundary, forbidden-use boundary, reference list, reference verification state, and fresh-reviewer focus for each citation context. It does not prove the cited sources support every sentence in the manuscript. Formal submission still requires an independent fresh reviewer thread.
