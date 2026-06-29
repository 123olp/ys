# Citation Context Review Packet

Date: 2026-06-29T00:00:00.000Z
Input: `web/src/data/effective-immortality-evidence.json`
Output JSON: `web/src/data/effective-immortality-flywheel/CITATION_CONTEXT_REVIEW_PACKET.json`

## Status

Verdict: `READY_FOR_EXTERNAL_REVIEW`

Reason: `packet_generated_no_external_judgment`

A structured packet for fresh reviewer sentence-level citation-context review has been generated from the Claim Register, Claim Evidence Map, Citation Context Register, and Reference Registry.

This packet is designed for a fresh reviewer thread. It is not a reviewer verdict.

## Fresh Reviewer Instructions

- Use a fresh context with no prior conversation state.
- Verify source existence and metadata through DOI, arXiv, PubMed, publisher, official standard, or official registry pages.
- Judge whether the cited source supports the exact claim and context, not merely a related topic.
- Preserve the does-not-support boundary when the reference only provides method language, governance language, association evidence, or task-limited evidence.
- Flag any source used to support effective immortality, lifespan extension, or individual prediction when it only supports a weaker claim.

## Review Questions

1. Does each reference exist and match the registered title, authors, year, venue, DOI or URL?
2. Does each reference support the exact usedFor claim for its citation context?
3. Does any prose overstate a method source, governance framework, observational association, mechanism review, or task-limited AI study?
4. Are all doesNotSupport boundaries honored by the current working paper and Web page?
5. Should any claim be softened, any citation replaced, or any reference removed?

## Packet Metrics

| Metric | Count |
| --- | ---: |
| Claims | 7 |
| Citation contexts | 12 |
| Reference entries | 53 |
| Claim-context links | 29 |
| Context-reference links | 49 |

## Context Index

| Context | Claims using it | References | Local status | Non-support boundary |
| --- | --- | ---: | --- | --- |
| CTX1 | CL2, CL3, CL7 | 2 | KEEP | 不证明任何具体延寿、健康、AI 或资源干预有效。 |
| CTX2 | CL1, CL2 | 3 | KEEP WITH BOUNDARY | 不能完整定义主体连续性，也不能替代个体医学判断。 |
| CTX3 | CL7 | 3 | KEEP WITH BOUNDARY | 不能把机制综述、预测关联或认知储备直接写成干预效果。 |
| CTX4 | CL1, CL2 | 4 | KEEP WITH BOUNDARY | 时间本身不会自动产生能力；错误反馈和低质量重复可能反向损害表现。 |
| CTX5 | CL1, CL2, CL5 | 3 | KEEP WITH BOUNDARY | 不能把社会关系关联直接升级成具体干预的因果延寿结论。 |
| CTX6 | CL1, CL2 | 3 | KEEP WITH BOUNDARY | 不能证明采用后的技术一定有效，也不能覆盖所有高风险医学或神经技术。 |
| CTX7 | CL1, CL2, CL4, CL7 | 4 | KEEP WITH BOUNDARY | 不能泛化为通用智能增强、健康寿命延长或永生收益。 |
| CTX8 | CL2, CL4, CL6, CL7 | 6 | KEEP | 治理框架和交互指南不提供收益估计，也不证明 AI 能延寿。 |
| CTX9 | CL3, CL6, CL7 | 11 | KEEP | 不能消除所有不可测混杂，也不证明任何注册试验或预测模型有效。 |
| CTX10 | CL6 | 4 | KEEP WITH BOUNDARY | 早筛、追踪或数字孪生概念不等于死亡风险下降或医疗结局改善。 |
| CTX11 | CL6 | 4 | KEEP WITH BOUNDARY | 哲学和系统框架不提供数值效应估计，也不能证明数字副本等同于本人。 |
| CTX12 | CL1, CL2, CL5 | 2 | KEEP WITH BOUNDARY | 规范框架不提供寿命预测，也不能替代具体政策或医疗干预评估。 |

## Claim Review Packets

### CL1: 有效永生应被建模为主体持续性、能力系统、技术系统和可能性空间的反馈问题，而非单次寿命长度问题。

- Claim type: Conceptual framing
- Current status: Framework proposal
- Alignment verdict: FRAMEWORK_ONLY
- Current support: 各局部边有方法、机制、关联、实验或规范来源支撑；完整飞轮仍是综合框架主张。
- Evidence edges: T -> E; E -> R; R -> C; C -> A; A -> Q; Q -> O; O -> T/E
- Falsifiers: 关键边长期不成立; 负向通道压过正向通道; 新增寿命无法转化为有效时间
- Upgrade gate: 完成至少一个案例研究或仿真，证明该框架比单一寿命指标更能解释长期行动能力。

#### CTX2: Grossman Health Capital; WHO HALE; NICE QALY

- Used for: 把日历寿命转译为健康质量、有效时间和质量调整时间。
- Supports: T -> E 的测量语言和健康质量调整视角。
- Does not support: 不能完整定义主体连续性，也不能替代个体医学判断。
- Local citation status: KEEP WITH BOUNDARY
- References:
  - `grossman1972healthcapital` (1972). On the Concept of Health Capital and the Demand for Health. DOI: 10.1086/259880. Local status: crossref-verified.
  - `niceEconomicEvaluation` (n.d.). Economic evaluation. URL: https://www.nice.org.uk/process/pmg36/chapter/economic-evaluation-2. Local status: official-url-200.
  - `whohale7752` (n.d.). Healthy life expectancy (HALE) metadata. URL: https://www.who.int/data/gho/indicator-metadata-registry/imr-details/7752. Local status: official-url-200.

#### CTX4: Deliberate Practice; Law of Practice; Self-Regulated Learning; Feedback Intervention Theory

- Used for: 解释 E -> R -> C：有效时间如何在有目标、有反馈和可修正的任务中沉淀为能力。
- Supports: 学习轮次、反馈质量、练习曲线和能力积累的条件。
- Does not support: 时间本身不会自动产生能力；错误反馈和低质量重复可能反向损害表现。
- Local citation status: KEEP WITH BOUNDARY
- References:
  - `ericsson1993deliberatePractice` (1993). The role of deliberate practice in the acquisition of expert performance. DOI: 10.1037/0033-295X.100.3.363. Local status: crossref-verified.
  - `kluger1996feedback` (1996). The effects of feedback interventions on performance: A historical review, a meta-analysis, and a preliminary feedback intervention theory. DOI: 10.1037/0033-2909.119.2.254. Local status: crossref-verified.
  - `newell1981lawPractice` (2013). Mechanisms of Skill Acquisition and the Law of Practice: Allen Newell and Paul S. Rosenbloom. DOI: 10.4324/9780203728178-6. Local status: crossref-verified-corrected-doi.
  - `zimmerman2002selfRegulated` (2002). Becoming a Self-Regulated Learner: An Overview. DOI: 10.1207/S15430421TIP4102_2. Local status: doi-verified.

#### CTX5: Human Capital; Social Capital; Social Relationships Mortality

- Used for: 说明经验、资源、信誉和协作网络如何进入 C 与 O，并可能反哺 T/E。
- Supports: 积累资本、社会支持和死亡风险关联的讨论。
- Does not support: 不能把社会关系关联直接升级成具体干预的因果延寿结论。
- Local citation status: KEEP WITH BOUNDARY
- References:
  - `coleman1988socialCapital` (1988). Social Capital in the Creation of Human Capital. DOI: 10.1086/228943. Local status: doi-verified.
  - `holtlunstad2010social` (2010). Social Relationships and Mortality Risk: A Meta-analytic Review. DOI: 10.1371/journal.pmed.1000316. Local status: crossref-verified.
  - `mincer1974humanCapital` (1974). Schooling, Experience, and Earnings. URL: https://www.nber.org/books-and-chapters/schooling-experience-and-earnings. Local status: official-archive.

#### CTX6: TAM; UTAUT; Diffusion of Innovations

- Used for: 解释 C -> A：技术采用受有用性、易用性、促进条件、资源和社会影响约束。
- Supports: 技术采用能力的分解：access、understanding、evaluation、trial、integration。
- Does not support: 不能证明采用后的技术一定有效，也不能覆盖所有高风险医学或神经技术。
- Local citation status: KEEP WITH BOUNDARY
- References:
  - `davis1989tam` (1989). Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology. DOI: 10.2307/249008. Local status: crossref-verified.
  - `rogers2003diffusion` (2003). Diffusion of Innovations. URL: https://archive.org/details/diffusionofinnov0005roge. Local status: bibliographic-record-verified-isbn.
  - `venkatesh2003utaut` (2003). User Acceptance of Information Technology: Toward a Unified View. DOI: 10.2307/30036540. Local status: crossref-verified.

#### CTX7: Generative AI at Work; Noy and Zhang; GitHub Copilot; Jagged Technological Frontier

- Used for: 支持 A -> Q 在限定任务中的生产率、速度、质量或任务边界证据。
- Supports: 生成式 AI 在客服、写作、编程或知识工作实验中的任务内效果与异质性。
- Does not support: 不能泛化为通用智能增强、健康寿命延长或永生收益。
- Local citation status: KEEP WITH BOUNDARY
- References:
  - `brynjolfsson2025generative` (2025). Generative AI at Work. DOI: 10.1093/qje/qjae044. Local status: crossref-verified-corrected-doi.
  - `dellacqua2026jagged` (2026). Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality. DOI: 10.1287/orsc.2025.21838. Local status: crossref-verified.
  - `noy2023productivity` (2023). Experimental evidence on the productivity effects of generative artificial intelligence. DOI: 10.1126/science.adh2586. Local status: crossref-verified.
  - `peng2023copilot` (2023). The Impact of AI on Developer Productivity: Evidence from GitHub Copilot. URL: https://arxiv.org/abs/2302.06590. Local status: arxiv-api-verified.

#### CTX12: Capability Approach; WHO SDOH; WHO Primary Health Care

- Used for: 定义 O 可能性空间为真实可进入路径，并把资源、制度、医疗和社会条件纳入反哺路径。
- Supports: 真实选择权、健康决定因素、医疗可及和连续照护的规范/公共卫生框架。
- Does not support: 规范框架不提供寿命预测，也不能替代具体政策或医疗干预评估。
- Local citation status: KEEP WITH BOUNDARY
- References:
  - `robeyns2021capability` (2021). The Capability Approach. URL: https://plato.stanford.edu/entries/capability-approach/. Local status: official-web-registered.
  - `whoSdhPhc` (n.d.). Social determinants of health and primary health care. URL: https://www.who.int/health-topics/social-determinants-of-health. Local status: official-urls-200.

### CL2: T/E/R/C/A/Q/O 是第一版最小变量接口，可把寿命、有效时间、轮次、积累、技术采用、行动质量和可能性空间放入同一模型。

- Claim type: Model interface
- Current status: Operational definition
- Alignment verdict: OPERATIONAL_INTERFACE
- Current support: 七变量接口把不同文献谱系压缩为可建模字段；当前只证明字段可讨论，不证明字段充分。
- Evidence edges: T -> E; E -> R; R -> C; C -> A; A -> Q; Q -> O; O -> T/E; A/Q -> risk
- Falsifiers: 变量无法被稳定代理测量; 变量之间高度重叠导致不可识别; 关键主体状态被遗漏
- Upgrade gate: 为每个变量补齐单位、代理指标、缺失处理、时间窗、适用人群和可重复测量方案。

#### CTX1: Kaplan-Meier 1958; Cox 1972

- Used for: 定义 T、生存函数 S(t)、删失数据和风险函数 lambda(t) 的统计语言。
- Supports: 事件时间、删失、生存曲线和协变量风险建模的基础方法。
- Does not support: 不证明任何具体延寿、健康、AI 或资源干预有效。
- Local citation status: KEEP
- References:
  - `cox1972regression` (1972). Regression Models and Life-Tables. DOI: 10.1111/j.2517-6161.1972.tb00899.x. Local status: crossref-verified.
  - `kaplan1958incomplete` (1958). Nonparametric Estimation from Incomplete Observations. DOI: 10.1080/01621459.1958.10501452. Local status: crossref-verified.

#### CTX2: Grossman Health Capital; WHO HALE; NICE QALY

- Used for: 把日历寿命转译为健康质量、有效时间和质量调整时间。
- Supports: T -> E 的测量语言和健康质量调整视角。
- Does not support: 不能完整定义主体连续性，也不能替代个体医学判断。
- Local citation status: KEEP WITH BOUNDARY
- References:
  - `grossman1972healthcapital` (1972). On the Concept of Health Capital and the Demand for Health. DOI: 10.1086/259880. Local status: crossref-verified.
  - `niceEconomicEvaluation` (n.d.). Economic evaluation. URL: https://www.nice.org.uk/process/pmg36/chapter/economic-evaluation-2. Local status: official-url-200.
  - `whohale7752` (n.d.). Healthy life expectancy (HALE) metadata. URL: https://www.who.int/data/gho/indicator-metadata-registry/imr-details/7752. Local status: official-url-200.

#### CTX4: Deliberate Practice; Law of Practice; Self-Regulated Learning; Feedback Intervention Theory

- Used for: 解释 E -> R -> C：有效时间如何在有目标、有反馈和可修正的任务中沉淀为能力。
- Supports: 学习轮次、反馈质量、练习曲线和能力积累的条件。
- Does not support: 时间本身不会自动产生能力；错误反馈和低质量重复可能反向损害表现。
- Local citation status: KEEP WITH BOUNDARY
- References:
  - `ericsson1993deliberatePractice` (1993). The role of deliberate practice in the acquisition of expert performance. DOI: 10.1037/0033-295X.100.3.363. Local status: crossref-verified.
  - `kluger1996feedback` (1996). The effects of feedback interventions on performance: A historical review, a meta-analysis, and a preliminary feedback intervention theory. DOI: 10.1037/0033-2909.119.2.254. Local status: crossref-verified.
  - `newell1981lawPractice` (2013). Mechanisms of Skill Acquisition and the Law of Practice: Allen Newell and Paul S. Rosenbloom. DOI: 10.4324/9780203728178-6. Local status: crossref-verified-corrected-doi.
  - `zimmerman2002selfRegulated` (2002). Becoming a Self-Regulated Learner: An Overview. DOI: 10.1207/S15430421TIP4102_2. Local status: doi-verified.

#### CTX5: Human Capital; Social Capital; Social Relationships Mortality

- Used for: 说明经验、资源、信誉和协作网络如何进入 C 与 O，并可能反哺 T/E。
- Supports: 积累资本、社会支持和死亡风险关联的讨论。
- Does not support: 不能把社会关系关联直接升级成具体干预的因果延寿结论。
- Local citation status: KEEP WITH BOUNDARY
- References:
  - `coleman1988socialCapital` (1988). Social Capital in the Creation of Human Capital. DOI: 10.1086/228943. Local status: doi-verified.
  - `holtlunstad2010social` (2010). Social Relationships and Mortality Risk: A Meta-analytic Review. DOI: 10.1371/journal.pmed.1000316. Local status: crossref-verified.
  - `mincer1974humanCapital` (1974). Schooling, Experience, and Earnings. URL: https://www.nber.org/books-and-chapters/schooling-experience-and-earnings. Local status: official-archive.

#### CTX6: TAM; UTAUT; Diffusion of Innovations

- Used for: 解释 C -> A：技术采用受有用性、易用性、促进条件、资源和社会影响约束。
- Supports: 技术采用能力的分解：access、understanding、evaluation、trial、integration。
- Does not support: 不能证明采用后的技术一定有效，也不能覆盖所有高风险医学或神经技术。
- Local citation status: KEEP WITH BOUNDARY
- References:
  - `davis1989tam` (1989). Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology. DOI: 10.2307/249008. Local status: crossref-verified.
  - `rogers2003diffusion` (2003). Diffusion of Innovations. URL: https://archive.org/details/diffusionofinnov0005roge. Local status: bibliographic-record-verified-isbn.
  - `venkatesh2003utaut` (2003). User Acceptance of Information Technology: Toward a Unified View. DOI: 10.2307/30036540. Local status: crossref-verified.

#### CTX7: Generative AI at Work; Noy and Zhang; GitHub Copilot; Jagged Technological Frontier

- Used for: 支持 A -> Q 在限定任务中的生产率、速度、质量或任务边界证据。
- Supports: 生成式 AI 在客服、写作、编程或知识工作实验中的任务内效果与异质性。
- Does not support: 不能泛化为通用智能增强、健康寿命延长或永生收益。
- Local citation status: KEEP WITH BOUNDARY
- References:
  - `brynjolfsson2025generative` (2025). Generative AI at Work. DOI: 10.1093/qje/qjae044. Local status: crossref-verified-corrected-doi.
  - `dellacqua2026jagged` (2026). Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality. DOI: 10.1287/orsc.2025.21838. Local status: crossref-verified.
  - `noy2023productivity` (2023). Experimental evidence on the productivity effects of generative artificial intelligence. DOI: 10.1126/science.adh2586. Local status: crossref-verified.
  - `peng2023copilot` (2023). The Impact of AI on Developer Productivity: Evidence from GitHub Copilot. URL: https://arxiv.org/abs/2302.06590. Local status: arxiv-api-verified.

#### CTX8: NIST AI RMF; Guidelines for Human-AI Interaction; NASA-TLX; Automation taxonomy

- Used for: 给 A/Q -> risk、QA 成本、任务负荷、自动化等级和人机控制权提供治理语言。
- Supports: 风险识别、测量、纠错、回滚和人机协作设计边界。
- Does not support: 治理框架和交互指南不提供收益估计，也不证明 AI 能延寿。
- Local citation status: KEEP
- References:
  - `amershi2019hai` (2019). Guidelines for Human-AI Interaction. DOI: 10.1145/3290605.3300233. Local status: crossref-verified.
  - `burwell2017bciEthics` (2017). Ethical aspects of brain computer interfaces: a scoping review. DOI: 10.1186/s12910-017-0220-y. Local status: doi-verified.
  - `dellacqua2026jagged` (2026). Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality. DOI: 10.1287/orsc.2025.21838. Local status: crossref-verified.
  - `nasaTlx` (n.d.). NASA Task Load Index. URL: https://www.nasa.gov/human-systems-integration-division/nasa-task-load-index-tlx/. Local status: official-web-registered.
  - `nist2023airmf` (2023). Artificial Intelligence Risk Management Framework (AI RMF 1.0). URL: https://www.nist.gov/itl/ai-risk-management-framework. Local status: official-url-200.
  - `parasuraman2000automation` (2000). A model for types and levels of human interaction with automation. DOI: 10.1109/3468.844354. Local status: crossref-verified.

#### CTX12: Capability Approach; WHO SDOH; WHO Primary Health Care

- Used for: 定义 O 可能性空间为真实可进入路径，并把资源、制度、医疗和社会条件纳入反哺路径。
- Supports: 真实选择权、健康决定因素、医疗可及和连续照护的规范/公共卫生框架。
- Does not support: 规范框架不提供寿命预测，也不能替代具体政策或医疗干预评估。
- Local citation status: KEEP WITH BOUNDARY
- References:
  - `robeyns2021capability` (2021). The Capability Approach. URL: https://plato.stanford.edu/entries/capability-approach/. Local status: official-web-registered.
  - `whoSdhPhc` (n.d.). Social determinants of health and primary health care. URL: https://www.who.int/health-topics/social-determinants-of-health. Local status: official-urls-200.

### CL3: 技术或干预应被表示为改变状态转移 P(X_{t+1}|X_t,U_t) 或风险函数 lambda(t|X_t,U_t) 的算子。

- Claim type: Method claim
- Current status: Methodologically supported
- Alignment verdict: METHOD_SUPPORTED
- Current support: 生存分析、风险模型和 target-trial style 因果协议支持把技术写成状态转移或风险函数上的算子。
- Evidence edges: U_t -> causal claim; T -> E
- Falsifiers: 没有 comparator; time zero 错误; 结局定义偷换; 不可测混杂压倒识别假设
- Upgrade gate: 每个技术族必须给出 population、intervention、comparator、time zero、outcome、estimand 和识别假设。

#### CTX1: Kaplan-Meier 1958; Cox 1972

- Used for: 定义 T、生存函数 S(t)、删失数据和风险函数 lambda(t) 的统计语言。
- Supports: 事件时间、删失、生存曲线和协变量风险建模的基础方法。
- Does not support: 不证明任何具体延寿、健康、AI 或资源干预有效。
- Local citation status: KEEP
- References:
  - `cox1972regression` (1972). Regression Models and Life-Tables. DOI: 10.1111/j.2517-6161.1972.tb00899.x. Local status: crossref-verified.
  - `kaplan1958incomplete` (1958). Nonparametric Estimation from Incomplete Observations. DOI: 10.1080/01621459.1958.10501452. Local status: crossref-verified.

#### CTX9: Target Trial Emulation; ClinicalTrials.gov; WHO ICTRP; TRIPOD+AI; PROBAST+AI; CONSORT-AI; SPIRIT-AI

- Used for: 定义 U_t -> causal claim 的因果门禁和预测模型报告门禁。
- Supports: population、intervention、comparator、time zero、outcome、estimand、试验登记、AI 干预报告、验证、校准和偏倚审查。
- Does not support: 不能消除所有不可测混杂，也不证明任何注册试验或预测模型有效。
- Local citation status: KEEP
- References:
  - `clinicaltrialsGov` (n.d.). ClinicalTrials.gov. URL: https://clinicaltrials.gov/. Local status: official-url-200.
  - `clinicaltrialsGovApi` (n.d.). ClinicalTrials.gov Data API. URL: https://clinicaltrials.gov/data-api/about-api. Local status: official-url-200.
  - `consortAi2020` (2020). Reporting guidelines for clinical trial reports for interventions involving artificial intelligence: the CONSORT-AI extension. DOI: 10.1038/s41591-020-1034-x. Local status: doi-verified.
  - `gradeHandbook` (n.d.). GRADE Handbook. URL: https://gdt.gradepro.org/app/handbook/handbook.html. Local status: official-web.
  - `hernan2022targetTrial` (2022). Target Trial Emulation. DOI: 10.1001/jama.2022.21383. Local status: crossref-verified.
  - `probastAi2025` (2025). PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods. DOI: 10.1136/bmj-2024-082505. Local status: doi-and-official-site-verified.
  - `robins2000marginalStructural` (2000). Marginal Structural Models and Causal Inference in Epidemiology. DOI: 10.1097/00001648-200009000-00011. Local status: pubmed-verified.
  - `spiritAi2020` (2020). Guidelines for clinical trial protocols for interventions involving artificial intelligence: the SPIRIT-AI extension. DOI: 10.1038/s41591-020-1037-7. Local status: doi-verified.
  - `tripodAi2024` (2024). TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods. DOI: 10.1136/bmj-2023-078378. Local status: doi-and-official-site-verified.
  - `tripodProbast` (n.d.). TRIPOD Statement and PROBAST. URL: https://www.tripod-statement.org/. Local status: official-urls-200.
  - `whoIctrp` (n.d.). International Clinical Trials Registry Platform (ICTRP). URL: https://www.who.int/tools/clinical-trials-registry-platform. Local status: official-url-200.

### CL4: AI 工具可在限定任务内提高单位时间行动质量，但收益具有任务边界和人群异质性。

- Claim type: Task-limited empirical claim
- Current status: Supported only for bounded tasks
- Alignment verdict: BOUNDED_EMPIRICAL
- Current support: AI 工具在客服、写作、编程和部分知识任务中有任务内收益证据；该证据只支持限定任务边界。
- Evidence edges: A -> Q; A/Q -> risk
- Falsifiers: 任务进入 jagged frontier 失败区; QA 成本抵消速度收益; 幻觉或自动化偏差提高返工; 高技能主体收益不稳定
- Upgrade gate: 按任务族建立 AI frontier map，并同步记录速度、质量、错误、QA 成本、依赖和异质性。

#### CTX7: Generative AI at Work; Noy and Zhang; GitHub Copilot; Jagged Technological Frontier

- Used for: 支持 A -> Q 在限定任务中的生产率、速度、质量或任务边界证据。
- Supports: 生成式 AI 在客服、写作、编程或知识工作实验中的任务内效果与异质性。
- Does not support: 不能泛化为通用智能增强、健康寿命延长或永生收益。
- Local citation status: KEEP WITH BOUNDARY
- References:
  - `brynjolfsson2025generative` (2025). Generative AI at Work. DOI: 10.1093/qje/qjae044. Local status: crossref-verified-corrected-doi.
  - `dellacqua2026jagged` (2026). Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality. DOI: 10.1287/orsc.2025.21838. Local status: crossref-verified.
  - `noy2023productivity` (2023). Experimental evidence on the productivity effects of generative artificial intelligence. DOI: 10.1126/science.adh2586. Local status: crossref-verified.
  - `peng2023copilot` (2023). The Impact of AI on Developer Productivity: Evidence from GitHub Copilot. URL: https://arxiv.org/abs/2302.06590. Local status: arxiv-api-verified.

#### CTX8: NIST AI RMF; Guidelines for Human-AI Interaction; NASA-TLX; Automation taxonomy

- Used for: 给 A/Q -> risk、QA 成本、任务负荷、自动化等级和人机控制权提供治理语言。
- Supports: 风险识别、测量、纠错、回滚和人机协作设计边界。
- Does not support: 治理框架和交互指南不提供收益估计，也不证明 AI 能延寿。
- Local citation status: KEEP
- References:
  - `amershi2019hai` (2019). Guidelines for Human-AI Interaction. DOI: 10.1145/3290605.3300233. Local status: crossref-verified.
  - `burwell2017bciEthics` (2017). Ethical aspects of brain computer interfaces: a scoping review. DOI: 10.1186/s12910-017-0220-y. Local status: doi-verified.
  - `dellacqua2026jagged` (2026). Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality. DOI: 10.1287/orsc.2025.21838. Local status: crossref-verified.
  - `nasaTlx` (n.d.). NASA Task Load Index. URL: https://www.nasa.gov/human-systems-integration-division/nasa-task-load-index-tlx/. Local status: official-web-registered.
  - `nist2023airmf` (2023). Artificial Intelligence Risk Management Framework (AI RMF 1.0). URL: https://www.nist.gov/itl/ai-risk-management-framework. Local status: official-url-200.
  - `parasuraman2000automation` (2000). A model for types and levels of human interaction with automation. DOI: 10.1109/3468.844354. Local status: crossref-verified.

### CL5: 可能性空间必须定义为主体真实可进入的路径集合，不能只统计抽象机会或叙事愿望。

- Claim type: Normative and measurement claim
- Current status: Normative framework with measurement task
- Alignment verdict: NORMATIVE_MEASUREMENT
- Current support: 能力方法、社会资本和公共健康框架支持把可能性空间定义为真实可进入路径集合。
- Evidence edges: Q -> O; O -> T/E
- Falsifiers: 产出提高但资源、权限、身份或制度入口不增加; 机会只能叙述不能进入; 新增路径带来更高暴露和恢复负担
- Upgrade gate: 把 O 拆成资源入口、制度入口、协作入口、技术窗口和可逆选择，并定义进入条件。

#### CTX5: Human Capital; Social Capital; Social Relationships Mortality

- Used for: 说明经验、资源、信誉和协作网络如何进入 C 与 O，并可能反哺 T/E。
- Supports: 积累资本、社会支持和死亡风险关联的讨论。
- Does not support: 不能把社会关系关联直接升级成具体干预的因果延寿结论。
- Local citation status: KEEP WITH BOUNDARY
- References:
  - `coleman1988socialCapital` (1988). Social Capital in the Creation of Human Capital. DOI: 10.1086/228943. Local status: doi-verified.
  - `holtlunstad2010social` (2010). Social Relationships and Mortality Risk: A Meta-analytic Review. DOI: 10.1371/journal.pmed.1000316. Local status: crossref-verified.
  - `mincer1974humanCapital` (1974). Schooling, Experience, and Earnings. URL: https://www.nber.org/books-and-chapters/schooling-experience-and-earnings. Local status: official-archive.

#### CTX12: Capability Approach; WHO SDOH; WHO Primary Health Care

- Used for: 定义 O 可能性空间为真实可进入路径，并把资源、制度、医疗和社会条件纳入反哺路径。
- Supports: 真实选择权、健康决定因素、医疗可及和连续照护的规范/公共卫生框架。
- Does not support: 规范框架不提供寿命预测，也不能替代具体政策或医疗干预评估。
- Local citation status: KEEP WITH BOUNDARY
- References:
  - `robeyns2021capability` (2021). The Capability Approach. URL: https://plato.stanford.edu/entries/capability-approach/. Local status: official-web-registered.
  - `whoSdhPhc` (n.d.). Social determinants of health and primary health care. URL: https://www.who.int/health-topics/social-determinants-of-health. Local status: official-urls-200.

### CL6: 所有增强技术都必须同时建模正向通道、负向通道、治理门禁和回滚条件。

- Claim type: Governance claim
- Current status: Governance requirement
- Alignment verdict: GOVERNANCE_REQUIRED
- Current support: AI 风险、人机交互、个人数据系统和认知工具谱系共同要求把副作用、误用、回滚和治理门禁并入模型。
- Evidence edges: A/Q -> risk; U_t -> causal claim
- Falsifiers: 技术收益只记正项; 停止条件缺失; 回滚路径缺失; 事故复盘缺失; 主体权利和同意边界缺失
- Upgrade gate: 为每个技术族建立 downside channel、监测指标、停止条件、回滚条件和事故复盘模板。

#### CTX8: NIST AI RMF; Guidelines for Human-AI Interaction; NASA-TLX; Automation taxonomy

- Used for: 给 A/Q -> risk、QA 成本、任务负荷、自动化等级和人机控制权提供治理语言。
- Supports: 风险识别、测量、纠错、回滚和人机协作设计边界。
- Does not support: 治理框架和交互指南不提供收益估计，也不证明 AI 能延寿。
- Local citation status: KEEP
- References:
  - `amershi2019hai` (2019). Guidelines for Human-AI Interaction. DOI: 10.1145/3290605.3300233. Local status: crossref-verified.
  - `burwell2017bciEthics` (2017). Ethical aspects of brain computer interfaces: a scoping review. DOI: 10.1186/s12910-017-0220-y. Local status: doi-verified.
  - `dellacqua2026jagged` (2026). Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality. DOI: 10.1287/orsc.2025.21838. Local status: crossref-verified.
  - `nasaTlx` (n.d.). NASA Task Load Index. URL: https://www.nasa.gov/human-systems-integration-division/nasa-task-load-index-tlx/. Local status: official-web-registered.
  - `nist2023airmf` (2023). Artificial Intelligence Risk Management Framework (AI RMF 1.0). URL: https://www.nist.gov/itl/ai-risk-management-framework. Local status: official-url-200.
  - `parasuraman2000automation` (2000). A model for types and levels of human interaction with automation. DOI: 10.1109/3468.844354. Local status: crossref-verified.

#### CTX9: Target Trial Emulation; ClinicalTrials.gov; WHO ICTRP; TRIPOD+AI; PROBAST+AI; CONSORT-AI; SPIRIT-AI

- Used for: 定义 U_t -> causal claim 的因果门禁和预测模型报告门禁。
- Supports: population、intervention、comparator、time zero、outcome、estimand、试验登记、AI 干预报告、验证、校准和偏倚审查。
- Does not support: 不能消除所有不可测混杂，也不证明任何注册试验或预测模型有效。
- Local citation status: KEEP
- References:
  - `clinicaltrialsGov` (n.d.). ClinicalTrials.gov. URL: https://clinicaltrials.gov/. Local status: official-url-200.
  - `clinicaltrialsGovApi` (n.d.). ClinicalTrials.gov Data API. URL: https://clinicaltrials.gov/data-api/about-api. Local status: official-url-200.
  - `consortAi2020` (2020). Reporting guidelines for clinical trial reports for interventions involving artificial intelligence: the CONSORT-AI extension. DOI: 10.1038/s41591-020-1034-x. Local status: doi-verified.
  - `gradeHandbook` (n.d.). GRADE Handbook. URL: https://gdt.gradepro.org/app/handbook/handbook.html. Local status: official-web.
  - `hernan2022targetTrial` (2022). Target Trial Emulation. DOI: 10.1001/jama.2022.21383. Local status: crossref-verified.
  - `probastAi2025` (2025). PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods. DOI: 10.1136/bmj-2024-082505. Local status: doi-and-official-site-verified.
  - `robins2000marginalStructural` (2000). Marginal Structural Models and Causal Inference in Epidemiology. DOI: 10.1097/00001648-200009000-00011. Local status: pubmed-verified.
  - `spiritAi2020` (2020). Guidelines for clinical trial protocols for interventions involving artificial intelligence: the SPIRIT-AI extension. DOI: 10.1038/s41591-020-1037-7. Local status: doi-verified.
  - `tripodAi2024` (2024). TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods. DOI: 10.1136/bmj-2023-078378. Local status: doi-and-official-site-verified.
  - `tripodProbast` (n.d.). TRIPOD Statement and PROBAST. URL: https://www.tripod-statement.org/. Local status: official-urls-200.
  - `whoIctrp` (n.d.). International Clinical Trials Registry Platform (ICTRP). URL: https://www.who.int/tools/clinical-trials-registry-platform. Local status: official-url-200.

#### CTX10: Apple Heart Study; Personal Informatics; Lived Informatics; Dynamic Digital Twin

- Used for: 说明观测、反馈、个人数据系统和生命过程建模如何进入状态观测层。
- Supports: observation -> action 的路径和自我追踪/数字孪生的系统问题。
- Does not support: 早筛、追踪或数字孪生概念不等于死亡风险下降或医疗结局改善。
- Local citation status: KEEP WITH BOUNDARY
- References:
  - `epstein2015lived` (2015). A lived informatics model of personal informatics. DOI: 10.1145/2750858.2804250. Local status: crossref-verified.
  - `li2010personalInformatics` (2010). A stage-based model of personal informatics systems. DOI: 10.1145/1753326.1753409. Local status: crossref-verified.
  - `mulder2022dynamicDigitalTwin` (2022). Dynamic Digital Twin: Diagnosis, Treatment, Prediction, and Prevention of Disease During the Life Course. DOI: 10.2196/35675. Local status: publisher-verified.
  - `perez2019appleHeart` (2019). Large-Scale Assessment of a Smartwatch to Identify Atrial Fibrillation. DOI: 10.1056/NEJMoa1901183. Local status: crossref-verified.

#### CTX11: Extended Mind; Engelbart; Cognition in the Wild

- Used for: 支撑工具、记忆外化、分布式认知和认知增强进入主体系统的理论位置。
- Supports: 主体能力可以由人、工具、表征、环境和协作流程共同支撑。
- Does not support: 哲学和系统框架不提供数值效应估计，也不能证明数字副本等同于本人。
- Local citation status: KEEP WITH BOUNDARY
- References:
  - `burwell2017bciEthics` (2017). Ethical aspects of brain computer interfaces: a scoping review. DOI: 10.1186/s12910-017-0220-y. Local status: doi-verified.
  - `clark1998extended` (1998). The Extended Mind. DOI: 10.1093/analys/58.1.7. Local status: crossref-verified.
  - `engelbart1962augmenting` (1962). Augmenting Human Intellect: A Conceptual Framework. URL: https://www.dougengelbart.org/pubs/augment-3906.html. Local status: official-archive-registered.
  - `hutchins1995cognition` (1995). Cognition in the Wild. URL: https://pages.ucsd.edu/~ehutchins/citw.html. Local status: author-page-verified.

### CL7: 本文不证明永生已经实现，不输出个体死亡日期，不把机制合理或短期功能改善升级成寿命延长结论。

- Claim type: Prohibited claim boundary
- Current status: Hard boundary
- Alignment verdict: HARD_BOUNDARY
- Current support: 方法标准、预测模型治理、AI 风险治理和证据政策共同限定本文不能输出个人死亡日期或把短期功能改善升级成寿命结论。
- Evidence edges: U_t -> causal claim; A/Q -> risk
- Falsifiers: 页面输出个体死亡日期; 机制合理被写成干预效果; 短期任务收益被写成寿命延长; 引用上下文越界
- Upgrade gate: 后续图表、模型和传播材料必须持续保留非主张边界，并接受 claim-to-source 审计。

#### CTX1: Kaplan-Meier 1958; Cox 1972

- Used for: 定义 T、生存函数 S(t)、删失数据和风险函数 lambda(t) 的统计语言。
- Supports: 事件时间、删失、生存曲线和协变量风险建模的基础方法。
- Does not support: 不证明任何具体延寿、健康、AI 或资源干预有效。
- Local citation status: KEEP
- References:
  - `cox1972regression` (1972). Regression Models and Life-Tables. DOI: 10.1111/j.2517-6161.1972.tb00899.x. Local status: crossref-verified.
  - `kaplan1958incomplete` (1958). Nonparametric Estimation from Incomplete Observations. DOI: 10.1080/01621459.1958.10501452. Local status: crossref-verified.

#### CTX3: Hallmarks of Aging; GrimAge; Cognitive Reserve

- Used for: 提出身体状态、衰老机制、生物年龄信号和认知储备候选变量。
- Supports: 状态变量和风险信号的机制/关联入口。
- Does not support: 不能把机制综述、预测关联或认知储备直接写成干预效果。
- Local citation status: KEEP WITH BOUNDARY
- References:
  - `lopezotin2013hallmarks` (2013). The Hallmarks of Aging. DOI: 10.1016/j.cell.2013.05.039. Local status: crossref-verified.
  - `lu2019grimage` (2019). DNA methylation GrimAge strongly predicts lifespan and healthspan. DOI: 10.18632/aging.101684. Local status: crossref-verified.
  - `stern2012cognitiveReserve` (2012). Cognitive reserve in ageing and Alzheimer's disease. DOI: 10.1016/S1474-4422(12)70191-6. Local status: crossref-verified.

#### CTX7: Generative AI at Work; Noy and Zhang; GitHub Copilot; Jagged Technological Frontier

- Used for: 支持 A -> Q 在限定任务中的生产率、速度、质量或任务边界证据。
- Supports: 生成式 AI 在客服、写作、编程或知识工作实验中的任务内效果与异质性。
- Does not support: 不能泛化为通用智能增强、健康寿命延长或永生收益。
- Local citation status: KEEP WITH BOUNDARY
- References:
  - `brynjolfsson2025generative` (2025). Generative AI at Work. DOI: 10.1093/qje/qjae044. Local status: crossref-verified-corrected-doi.
  - `dellacqua2026jagged` (2026). Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality. DOI: 10.1287/orsc.2025.21838. Local status: crossref-verified.
  - `noy2023productivity` (2023). Experimental evidence on the productivity effects of generative artificial intelligence. DOI: 10.1126/science.adh2586. Local status: crossref-verified.
  - `peng2023copilot` (2023). The Impact of AI on Developer Productivity: Evidence from GitHub Copilot. URL: https://arxiv.org/abs/2302.06590. Local status: arxiv-api-verified.

#### CTX8: NIST AI RMF; Guidelines for Human-AI Interaction; NASA-TLX; Automation taxonomy

- Used for: 给 A/Q -> risk、QA 成本、任务负荷、自动化等级和人机控制权提供治理语言。
- Supports: 风险识别、测量、纠错、回滚和人机协作设计边界。
- Does not support: 治理框架和交互指南不提供收益估计，也不证明 AI 能延寿。
- Local citation status: KEEP
- References:
  - `amershi2019hai` (2019). Guidelines for Human-AI Interaction. DOI: 10.1145/3290605.3300233. Local status: crossref-verified.
  - `burwell2017bciEthics` (2017). Ethical aspects of brain computer interfaces: a scoping review. DOI: 10.1186/s12910-017-0220-y. Local status: doi-verified.
  - `dellacqua2026jagged` (2026). Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality. DOI: 10.1287/orsc.2025.21838. Local status: crossref-verified.
  - `nasaTlx` (n.d.). NASA Task Load Index. URL: https://www.nasa.gov/human-systems-integration-division/nasa-task-load-index-tlx/. Local status: official-web-registered.
  - `nist2023airmf` (2023). Artificial Intelligence Risk Management Framework (AI RMF 1.0). URL: https://www.nist.gov/itl/ai-risk-management-framework. Local status: official-url-200.
  - `parasuraman2000automation` (2000). A model for types and levels of human interaction with automation. DOI: 10.1109/3468.844354. Local status: crossref-verified.

#### CTX9: Target Trial Emulation; ClinicalTrials.gov; WHO ICTRP; TRIPOD+AI; PROBAST+AI; CONSORT-AI; SPIRIT-AI

- Used for: 定义 U_t -> causal claim 的因果门禁和预测模型报告门禁。
- Supports: population、intervention、comparator、time zero、outcome、estimand、试验登记、AI 干预报告、验证、校准和偏倚审查。
- Does not support: 不能消除所有不可测混杂，也不证明任何注册试验或预测模型有效。
- Local citation status: KEEP
- References:
  - `clinicaltrialsGov` (n.d.). ClinicalTrials.gov. URL: https://clinicaltrials.gov/. Local status: official-url-200.
  - `clinicaltrialsGovApi` (n.d.). ClinicalTrials.gov Data API. URL: https://clinicaltrials.gov/data-api/about-api. Local status: official-url-200.
  - `consortAi2020` (2020). Reporting guidelines for clinical trial reports for interventions involving artificial intelligence: the CONSORT-AI extension. DOI: 10.1038/s41591-020-1034-x. Local status: doi-verified.
  - `gradeHandbook` (n.d.). GRADE Handbook. URL: https://gdt.gradepro.org/app/handbook/handbook.html. Local status: official-web.
  - `hernan2022targetTrial` (2022). Target Trial Emulation. DOI: 10.1001/jama.2022.21383. Local status: crossref-verified.
  - `probastAi2025` (2025). PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods. DOI: 10.1136/bmj-2024-082505. Local status: doi-and-official-site-verified.
  - `robins2000marginalStructural` (2000). Marginal Structural Models and Causal Inference in Epidemiology. DOI: 10.1097/00001648-200009000-00011. Local status: pubmed-verified.
  - `spiritAi2020` (2020). Guidelines for clinical trial protocols for interventions involving artificial intelligence: the SPIRIT-AI extension. DOI: 10.1038/s41591-020-1037-7. Local status: doi-verified.
  - `tripodAi2024` (2024). TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods. DOI: 10.1136/bmj-2023-078378. Local status: doi-and-official-site-verified.
  - `tripodProbast` (n.d.). TRIPOD Statement and PROBAST. URL: https://www.tripod-statement.org/. Local status: official-urls-200.
  - `whoIctrp` (n.d.). International Clinical Trials Registry Platform (ICTRP). URL: https://www.who.int/tools/clinical-trials-registry-platform. Local status: official-url-200.


## Required Reviewer Output

For every claim-context-reference group, return:

```text
CLAIM_ID:
CONTEXT_ID:
REFERENCE_KEYS:
EXISTENCE: YES / NO / UNCERTAIN
METADATA: CORRECT / FIX_NEEDED / UNCERTAIN
CONTEXT_SUPPORT: SUPPORTS / WEAK / WRONG / AMBIGUOUS
BOUNDARY_OK: YES / NO
RATIONALE:
ACTION: KEEP / FIX_METADATA / SOFTEN_CLAIM / REPLACE_CITATION / REMOVE_CITATION
```

The reviewer must use web/DBLP/arXiv/DOI/publisher lookups and must not rely on this packet as proof that a source supports a claim.
