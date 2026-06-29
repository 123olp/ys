# 有效永生飞轮 Source Cards v0.5

Status: draft card pack v0.5  
Related run: [automated research run](2026-06-28-effective-immortality-flywheel-automated-research-run.md)  
Target paper: [Effective Immortality Acceleration Flywheel](../explanations/effective-immortality-acceleration-flywheel.md)

## Card 1: Kaplan-Meier Survival Curve

| Field | Notes |
| --- | --- |
| Source identity | Kaplan, E. L.; Meier, P. 1958. *Nonparametric Estimation from Incomplete Observations*. JASA. <https://www.tandfonline.com/doi/abs/10.1080/01621459.1958.10501452> |
| One-sentence use | 为 `T` 和生存曲线提供基础统计语言。 |
| Human Infra mapping | 主体持续时间、寿命路径分布、删失数据。 |
| Model position | `lifespan`, `survival curve P(T > t)`, observation boundary. |
| Evidence role | Method standard. |
| Transfer boundary | 只能说明如何估计生存分布，不能证明任何干预有效。 |
| Repository action | 用于论文方法底座和预测模型契约。 |

## Card 2: Cox Proportional Hazards

| Field | Notes |
| --- | --- |
| Source identity | Cox, D. R. 1972. *Regression Models and Life-Tables*. JRSS-B. <https://rss.onlinelibrary.wiley.com/doi/10.1111/j.2517-6161.1972.tb00899.x> |
| One-sentence use | 把变量、干预或状态放进风险函数 `lambda(t)`。 |
| Human Infra mapping | 技术/资源/健康变量如何改变失效风险。 |
| Model position | `hazard lambda(t | X_t, U_t)`. |
| Evidence role | Method standard. |
| Transfer boundary | 比例风险假设需要检验；不能自动处理复杂反馈飞轮。 |
| Repository action | 支撑“技术不是神奇延寿变量，而是改变风险函数的算子”。 |

## Card 3: Hallmarks of Aging

| Field | Notes |
| --- | --- |
| Source identity | Lopez-Otin et al. 2013. *The Hallmarks of Aging*. Cell / PMC. <https://pmc.ncbi.nlm.nih.gov/articles/PMC3836174/> |
| One-sentence use | 给身体状态 `X_t` 的衰老机制提供变量候选。 |
| Human Infra mapping | 身体健康、健康寿命、恢复能力、死亡风险。 |
| Model position | State variables, transitions, biological mechanisms. |
| Evidence role | Mechanism review. |
| Transfer boundary | 机制框架不等于某个干预已经能延寿；人体转化需要临床证据。 |
| Repository action | 进入身体状态变量字典。 |

## Card 4: DNAm GrimAge

| Field | Notes |
| --- | --- |
| Source identity | Lu et al. 2019. *DNA methylation GrimAge strongly predicts lifespan and healthspan*. Aging. <https://www.aging-us.com/article/101684> |
| One-sentence use | 连接生物年龄标志物、死亡风险和健康寿命信号。 |
| Human Infra mapping | 观测能力、生物年龄、风险函数。 |
| Model position | Observation process, risk prediction, lifespan / healthspan. |
| Evidence role | Biomarker / association / endpoint prediction. |
| Transfer boundary | 不能用于输出个体死亡日期；不同人群、实验平台和干预情境需要校准。 |
| Repository action | 作为观测层案例，不作为干预效果证明。 |

## Card 5: Dynamic Digital Twin

| Field | Notes |
| --- | --- |
| Source identity | Mulder et al. 2022. *Dynamic Digital Twin: Diagnosis, Treatment, Prediction, and Prevention of Disease During the Life Course*. JMIR. <https://www.jmir.org/2022/9/e35675> |
| One-sentence use | 说明主体状态可被多模态观测、预测和生命周期建模。 |
| Human Infra mapping | 数字孪生、状态观测、预防、生命路径模拟。 |
| Model position | Observation process, state transition, policy simulation. |
| Evidence role | Conceptual / tooling support. |
| Transfer boundary | 医疗数字孪生仍有数据、验证、伦理和临床实施障碍。 |
| Repository action | 支撑预测模型和 Web 交互模拟方向。 |

## Card 6: Deliberate Practice

| Field | Notes |
| --- | --- |
| Source identity | Ericsson et al. 1993. *The Role of Deliberate Practice in the Acquisition of Expert Performance*. ERIC record. <https://eric.ed.gov/?id=EJ471947> |
| One-sentence use | 把“时间变长”转译为“有反馈的练习轮次增加”。 |
| Human Infra mapping | `R -> C`，学习轮次、能力增长、外部约束。 |
| Model position | State transition from practice rounds to capability. |
| Evidence role | Mechanism and empirical support. |
| Transfer boundary | 专家表现有领域特异性；时间堆积不自动等于能力增长。 |
| Repository action | 写入学习轮次变量说明。 |

## Card 7: Law of Practice

| Field | Notes |
| --- | --- |
| Source identity | Newell & Rosenbloom. *Mechanisms of Skill Acquisition and the Law of Practice*. <https://www.taylorfrancis.com/chapters/edit/10.4324/9780203728178-6/mechanisms-skill-acquisition-law-practice-allen-newell-paul-rosenbloom> |
| One-sentence use | 给“重复轮次如何改变表现”提供学习曲线模型入口。 |
| Human Infra mapping | 学习/试错/修正轮次到单位时间行动质量。 |
| Model position | `R -> C`, `R -> Q`. |
| Evidence role | Cognitive model / mechanism. |
| Transfer boundary | 学习曲线可能饱和，也可能被遗忘、任务变化或个体差异打断。 |
| Repository action | 支撑玩具模型的学习曲线参数。 |

## Card 8: Human Capital

| Field | Notes |
| --- | --- |
| Source identity | Mincer, J. 1974. *Schooling, Experience, and Earnings*. NBER. <https://www.nber.org/books-and-chapters/schooling-experience-and-earnings> |
| One-sentence use | 说明教育和经验如何被建模为人力资本。 |
| Human Infra mapping | `C` 中的技能、经验和长期积累。 |
| Model position | State variable and accumulation process. |
| Evidence role | Economic model / association. |
| Transfer boundary | 收入不是主体持续性的唯一结果；人力资本模型需要扩展到健康、行动和选择权。 |
| Repository action | 用于定义积累资本 `C`。 |

## Card 9: Social Capital

| Field | Notes |
| --- | --- |
| Source identity | Coleman, J. S. 1988. *Social Capital in the Creation of Human Capital*. AJS. <https://www.journals.uchicago.edu/doi/10.1086/228943> |
| One-sentence use | 说明关系、信任、规范和网络如何成为能力形成条件。 |
| Human Infra mapping | 协作网络、信誉资产、资源可及性。 |
| Model position | `C`, option value, social support. |
| Evidence role | Theory / mechanism. |
| Transfer boundary | 社会资本可能排他、封闭或带来路径锁定，不总是正向。 |
| Repository action | 用于扩展 `C` 和 `O`。 |

## Card 10: Technology Acceptance

| Field | Notes |
| --- | --- |
| Source identity | Davis, F. D. 1989. *Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology*. MIS Quarterly. <https://misq.umn.edu/misq/article/13/3/319/191/Perceived-Usefulness-Perceived-Ease-of-Use-and> |
| One-sentence use | 为技术采用能力 `A` 提供可操作变量。 |
| Human Infra mapping | 新技术理解、评估和采用。 |
| Model position | Action policy `pi`, adoption capacity. |
| Evidence role | Behavioral model / empirical instrument. |
| Transfer boundary | 采用不等于有效增强；高风险医学或神经技术需要额外治理。 |
| Repository action | 用于技术采用变量字典。 |

## Card 11: Diffusion of Innovations

| Field | Notes |
| --- | --- |
| Source identity | Rogers, E. M. *Diffusion of Innovations*. Free Press. Internet Archive bibliographic record: <https://archive.org/details/diffusionofinnov0005roge> |
| One-sentence use | 说明技术成熟和采用发生在社会系统与时间窗口中。 |
| Human Infra mapping | 等待技术成熟、进入技术窗口、采用者差异。 |
| Model position | Environment, access, adoption timing. |
| Evidence role | Theory synthesis. |
| Transfer boundary | 扩散理论不能保证某项技术有正效应，也不能替代具体安全证据。 |
| Repository action | 支撑“更长主体持续时间增加等待技术窗口的概率”。 |

## Card 12: Generative AI at Work

| Field | Notes |
| --- | --- |
| Source identity | Brynjolfsson, Li & Raymond. 2025. *Generative AI at Work*. Quarterly Journal of Economics, 140(2):889-942. <https://academic.oup.com/qje/article/140/2/889/7990658> |
| One-sentence use | 提供 AI 工具提高单位时间任务产出的实证入口。 |
| Human Infra mapping | `A -> Q`，技术采用到单位时间行动质量。 |
| Model position | Intervention, productivity endpoint, heterogeneity. |
| Evidence role | Functional endpoint evidence. |
| Transfer boundary | 客服场景不等于所有知识工作；工具收益有异质性，不应泛化成“AI 必然增强”。 |
| Repository action | 支撑 AI 工具增强的第一批实证卡。 |

## Card 13: Extended Mind

| Field | Notes |
| --- | --- |
| Source identity | Clark & Chalmers. 1998. *The Extended Mind*. Analysis. <https://academic.oup.com/analysis/article-pdf/58/1/7/359060/58-1-7.pdf> |
| One-sentence use | 给记忆外化、工具嵌入和认知扩展提供哲学语言。 |
| Human Infra mapping | 记忆、工具、环境和主体边界。 |
| Model position | Cognitive state, observation process, tool-mediated agency. |
| Evidence role | Narrative / theory support. |
| Transfer boundary | 哲学论证不等于工具有效性证据；主体连续性仍需单独处理。 |
| Repository action | 支撑记忆外化和 AI 工具的边界讨论。 |

## Card 14: Augmenting Human Intellect

| Field | Notes |
| --- | --- |
| Source identity | Engelbart, D. C. 1962. *Augmenting Human Intellect: A Conceptual Framework*. <https://www.dougengelbart.org/pubs/augment-3906.html> |
| One-sentence use | 将个人、工具、概念、方法和协作看作可系统增强的整体。 |
| Human Infra mapping | 工具增强、系统协作、行动质量。 |
| Model position | Intervention stack, capability amplification. |
| Evidence role | Foundational narrative / system framing. |
| Transfer boundary | 概念框架不是效果估计；需要具体工具和任务证据补充。 |
| Repository action | 支撑 Human Infra 的工具增强谱系。 |

## Card 15: Capability Approach

| Field | Notes |
| --- | --- |
| Source identity | Robeyns & Byskov, SEP *The Capability Approach*; Sen, *Commodities and Capabilities*. <https://plato.stanford.edu/entries/capability-approach/> |
| One-sentence use | 把可能性空间 `O` 表达为真实可行能力和选择自由。 |
| Human Infra mapping | 未来选择权、制度入口、资源可达、主体行动余地。 |
| Model position | Option value, agency, welfare boundary. |
| Evidence role | Normative framework. |
| Transfer boundary | 规范框架不提供寿命预测；需要和生存模型、技术模型分层使用。 |
| Repository action | 支撑“未来选择权”定义。 |

## Card 16: Health Capital

| Field | Notes |
| --- | --- |
| Source identity | Grossman, M. 1972. *On the Concept of Health Capital and the Demand for Health*. Journal of Political Economy. DOI: 10.1086/259880. <https://www.journals.uchicago.edu/doi/10.1086/259880> |
| One-sentence use | 把健康看成影响时间、能力和生产活动的资本存量。 |
| Human Infra mapping | `T -> E`，健康质量决定寿命窗口能否转化为有效时间。 |
| Model position | Health state, depreciation, investment, effective time. |
| Evidence role | Economic theory / foundational model. |
| Transfer boundary | 健康资本模型不是医学干预证据；需要和生物机制、临床证据分层使用。 |
| Repository action | 用于补强“有效时间不是日历时间”的定义。 |

## Card 17: Cognitive Reserve

| Field | Notes |
| --- | --- |
| Source identity | Stern, Y. 2012. *Cognitive reserve in ageing and Alzheimer's disease*. Lancet Neurology. DOI: 10.1016/S1474-4422(12)70191-6. <https://pubmed.ncbi.nlm.nih.gov/23079557/> |
| One-sentence use | 说明教育、经验和认知活动可能影响脑病理负担下的功能表现。 |
| Human Infra mapping | `C -> E/Q`，积累资本可能影响认知持续性和有效行动质量。 |
| Model position | Cognitive state, resilience, delayed functional decline. |
| Evidence role | Review / mechanism and epidemiological synthesis. |
| Transfer boundary | 不能把认知储备解释为不会患病；其作用和个体差异、疾病进展相关。 |
| Repository action | 用于补强“能力积累可能保护未来行动能力”的边。 |

## Card 18: Social Relationships and Mortality Risk

| Field | Notes |
| --- | --- |
| Source identity | Holt-Lunstad, Smith & Layton. 2010. *Social Relationships and Mortality Risk: A Meta-analytic Review*. PLoS Medicine. DOI: 10.1371/journal.pmed.1000316. <https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1000316> |
| One-sentence use | 说明社会关系与死亡风险之间存在稳定观察关联。 |
| Human Infra mapping | `O -> T/E`，关系网络和社会支持可能进入主体持续性。 |
| Model position | Social support, risk exposure, recovery resource. |
| Evidence role | Meta-analysis / observational association. |
| Transfer boundary | 关联不等于干预因果；社会关系质量、文化和健康选择偏差需要处理。 |
| Repository action | 用于将协作网络从“生产力变量”扩展为“持续性变量”。 |

## Card 19: Self-Regulated Learning

| Field | Notes |
| --- | --- |
| Source identity | Zimmerman, B. J. 2002. *Becoming a Self-Regulated Learner: An Overview*. Theory Into Practice. <https://www.tandfonline.com/doi/abs/10.1207/s15430421tip4102_2> |
| One-sentence use | 说明学习轮次需要目标设定、自我监控、反馈和策略调整。 |
| Human Infra mapping | `E -> R -> C`，有效时间要通过自我调节转化为学习轮次。 |
| Model position | Policy quality, feedback loop, learning efficiency. |
| Evidence role | Learning science framework. |
| Transfer boundary | 自我调节模型不保证所有长期项目成功；环境、资源和任务难度仍是约束。 |
| Repository action | 用于防止把“时间更多”直接等同“能力更强”。 |

## Card 20: Feedback Intervention Theory

| Field | Notes |
| --- | --- |
| Source identity | Kluger & DeNisi. 1996. *The effects of feedback interventions on performance*. Psychological Bulletin. DOI: 10.1037/0033-2909.119.2.254. <https://doi.org/10.1037/0033-2909.119.2.254> |
| One-sentence use | 说明反馈可能提升表现，也可能因注意力转移或错误设计而降低表现。 |
| Human Infra mapping | `R -> C/Q`，轮次质量依赖反馈结构。 |
| Model position | Feedback quality, learning gain, negative feedback channel. |
| Evidence role | Meta-analysis / theory. |
| Transfer boundary | 反馈不是单向正变量；设计错误时会破坏学习飞轮。 |
| Repository action | 用于建立“学习断点”和负向路径。 |

## Card 21: Unified Theory of Acceptance and Use of Technology

| Field | Notes |
| --- | --- |
| Source identity | Venkatesh et al. 2003. *User Acceptance of Information Technology: Toward a Unified View*. MIS Quarterly. DOI: 10.2307/30036540. <https://misq.umn.edu/misq/article/27/3/425/1340/User-Acceptance-of-Information-Technology-Toward-A> |
| One-sentence use | 把技术采用拆成绩效预期、努力预期、社会影响和促进条件。 |
| Human Infra mapping | `C -> A`，主体积累如何影响技术接触、理解、采用和使用。 |
| Model position | Adoption capacity, enabling conditions, behavioral intention. |
| Evidence role | Integrated behavioral model / empirical framework. |
| Transfer boundary | 一般 IT 采用模型不能直接覆盖高风险医学、BCI 或生物技术干预。 |
| Repository action | 用于补强技术采用变量 `A` 的二级字段。 |

## Card 22: Generative AI Writing Productivity

| Field | Notes |
| --- | --- |
| Source identity | Noy & Zhang. 2023. *Experimental evidence on the productivity effects of generative artificial intelligence*. Science, 381(6654):187-192. DOI: 10.1126/science.adh2586. <https://www.science.org/doi/10.1126/science.adh2586> |
| One-sentence use | 说明生成式 AI 在写作任务中可提升生产率，并改变质量分布。 |
| Human Infra mapping | `A -> Q`，AI 工具采用到单位时间行动质量。 |
| Model position | Task productivity endpoint, AI intervention, heterogeneity. |
| Evidence role | Randomized experiment. |
| Transfer boundary | 写作任务不代表所有创造、判断或长期问题求解；外推必须分任务。 |
| Repository action | 用于构建 AI 增强证据族。 |

## Card 23: Jagged Technological Frontier

| Field | Notes |
| --- | --- |
| Source identity | Dell'Acqua et al. 2026. *Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of AI on Knowledge Worker Productivity and Quality*. Organization Science. DOI: 10.1287/orsc.2025.21838. <https://pubsonline.informs.org/doi/10.1287/orsc.2025.21838> |
| One-sentence use | 说明 AI 能力边界呈参差形状，某些任务增强明显，某些任务可能被误导。 |
| Human Infra mapping | `A -> Q` and `A/Q -> risk`，技术增强和技术副作用共存。 |
| Model position | Task frontier, risk channel, governance breakpoint. |
| Evidence role | Field experiment / boundary evidence. |
| Transfer boundary | 咨询类实验不能泛化到全部 AI 使用；但适合作为“任务边界”警告。 |
| Repository action | 用于把技术采用从单一正收益改成收益-风险双通道。 |

## Card 24: GitHub Copilot Productivity Experiment

| Field | Notes |
| --- | --- |
| Source identity | Peng et al. 2023. *The Impact of AI on Developer Productivity: Evidence from GitHub Copilot*. arXiv:2302.06590. <https://arxiv.org/abs/2302.06590> |
| One-sentence use | 提供 AI 编程助手影响任务完成时间的实验入口。 |
| Human Infra mapping | `A -> Q`，专业工具如何改变单位时间任务完成能力。 |
| Model position | Productivity gain, task time, tool adoption. |
| Evidence role | Controlled experiment / preprint. |
| Transfer boundary | 编程任务范围有限；预印本和平台情境需要标注。 |
| Repository action | 用于扩展 AI 增强证据族到工程任务。 |

## Card 25: Generative AI at Work QJE Field Evidence

| Field | Notes |
| --- | --- |
| Source identity | Brynjolfsson, Li & Raymond. 2025. *Generative AI at Work*. Quarterly Journal of Economics, 140(2):889-942. DOI: 10.1093/qje/qjae044. <https://academic.oup.com/qje/article/140/2/889/7990658> |
| One-sentence use | 提供真实工作场景中 AI 助手对生产率和质量影响的证据。 |
| Human Infra mapping | `A -> Q`，技术采用到行动质量、反馈速度和组织产出。 |
| Model position | Workplace productivity, skill heterogeneity, AI assistance. |
| Evidence role | Field evidence / published article. |
| Transfer boundary | 客服场景和任务结构具体；不能泛化成所有职业都会等量受益。 |
| Repository action | 用于将 AI 工具增强从概念层推进到实证层。 |

## Card 26: Target Trial Emulation

| Field | Notes |
| --- | --- |
| Source identity | Hernan et al. target trial emulation materials; PubMed metadata retained in core literature pack. <https://pubmed.ncbi.nlm.nih.gov/36508210/> Open tutorial substitute: Jafarzadeh & Neogi / Matthews et al. <https://pmc.ncbi.nlm.nih.gov/articles/PMC9910387/> |
| One-sentence use | 把“某技术是否有用”转成先定义理想随机试验、再审查观察数据能否模拟的问题。 |
| Human Infra mapping | 技术/干预进入 `T/E/R/C/A/Q/O` 飞轮之前的因果门禁。 |
| Model position | Action policy, comparator, time zero, outcome, estimand, identification assumptions. |
| Evidence role | Method standard for causal inference. |
| Transfer boundary | 目标试验模拟不能消除所有不可测混杂；数据缺失、阳性假设失败和选择偏差仍会破坏识别。 |
| Repository action | 用于新增“因果评估协议”并阻止把相关性直接写成干预效果。 |

## Card 27: HALE / QALY Effective-Time Language

| Field | Notes |
| --- | --- |
| Source identity | WHO HALE metadata. <https://www.who.int/data/gho/indicator-metadata-registry/imr-details/7752>; NICE economic evaluation and QALY reference. <https://www.nice.org.uk/process/pmg36/chapter/economic-evaluation-2> |
| One-sentence use | 提供把寿命长度和健康质量放到同一时间语言中的公共卫生与经济评估入口。 |
| Human Infra mapping | `T -> E`，从日历寿命转向健康寿命、健康质量调整时间和有效时间代理。 |
| Model position | Outcome definition, quality-adjusted time, effective-time proxy. |
| Evidence role | Measurement / policy evaluation language. |
| Transfer boundary | QALY/HALE 不能完整表达主体尊严、身份连续性、主观时间和可能性空间；权重假设必须公开。 |
| Repository action | 用于定义 `E` 时避免把所有活着时间视为等价时间。 |

## Technology Family Addendum v0.3

本节把 Evidence Matrix 中的六类技术/干预族补成可追溯来源卡。第一轮每类先补 2 张，目标不是证明技术必然增强主体，而是明确每类技术进入模型前需要回答什么问题、使用什么证据、在哪里失败。

## Card 28: NIST AI Risk Management Framework

| Field | Notes |
| --- | --- |
| Source identity | NIST. *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*. <https://www.nist.gov/itl/ai-risk-management-framework> |
| Technology family | AI 工具。 |
| One-sentence use | 为 AI 工具进入飞轮模型时的风险识别、测量、治理和回滚提供标准语言。 |
| Human Infra mapping | `A/Q -> risk`，幻觉、自动化偏差、隐私泄漏、错误依赖和治理失败。 |
| Model position | Risk channel, governance gate, evaluation checklist. |
| Evidence level | Governance standard / official framework. |
| Transfer boundary | 它是治理框架，不提供 AI 工具收益估计，也不能替代具体任务实验。 |
| Repository action | 给 AI 技术族新增风险门禁字段：validity、privacy、safety、accountability、fallback。 |

## Card 29: Guidelines for Human-AI Interaction

| Field | Notes |
| --- | --- |
| Source identity | Amershi et al. 2019. *Guidelines for Human-AI Interaction*. CHI. DOI: 10.1145/3290605.3300233. <https://dl.acm.org/doi/10.1145/3290605.3300233> |
| Technology family | AI 工具。 |
| One-sentence use | 把 AI 工具增强拆成人机交互、可理解反馈、纠错、控制权和用户校准问题。 |
| Human Infra mapping | `A -> Q` and `A/Q -> risk`，AI 工具只有在可校准、可控、可纠错时才可能提高行动质量。 |
| Model position | Human-AI interaction, policy quality, QA cost. |
| Evidence level | HCI empirical synthesis / design guideline. |
| Transfer boundary | 交互指南不能证明某个模型有医学、认知或寿命收益；只能作为工具可用性和安全边界。 |
| Repository action | Web 技术族面板应把 AI 收益和 QA/纠错成本放在同一行。 |

## Card 30: ClinicalTrials.gov Trial Registry

| Field | Notes |
| --- | --- |
| Source identity | U.S. National Library of Medicine. *ClinicalTrials.gov*. <https://clinicaltrials.gov/>; *ClinicalTrials.gov Data API*. <https://clinicaltrials.gov/data-api/about-api>; WHO *International Clinical Trials Registry Platform*. <https://www.who.int/tools/clinical-trials-registry-platform> |
| Technology family | 医学干预。 |
| One-sentence use | 为医学干预提供试验登记、机器读取、国际注册网络、适应证、比较组、结局、状态和结果回填入口。 |
| Human Infra mapping | `U_t -> causal claim`，医学技术必须先说明人群、干预、比较组、时间零点和临床终点。 |
| Model position | Trial registry, API ingestion, evidence traceability, intervention contract. |
| Evidence level | Official registry / source of trial metadata. |
| Transfer boundary | 登记存在不等于干预有效；结果缺失、发表偏倚和终点替换仍需审查。 |
| Repository action | 医学技术族新增字段：registry_source、trial_id、phase、comparator、primary_outcome、follow_up、results_status、api_record_url。 |

## Card 31: TRIPOD and PROBAST

| Field | Notes |
| --- | --- |
| Source identity | TRIPOD+AI. DOI: 10.1136/bmj-2023-078378. <https://www.tripod-statement.org/>; PROBAST+AI. DOI: 10.1136/bmj-2024-082505. <https://www.probast.org/>; CONSORT-AI. DOI: 10.1038/s41591-020-1034-x; SPIRIT-AI. DOI: 10.1038/s41591-020-1037-7. |
| Technology family | 医学干预 / 预测模型 / AI 临床试验。 |
| One-sentence use | 约束寿命、健康寿命和风险预测模型的报告质量、偏倚风险、适用性，以及 AI 干预临床试验的协议和结果报告。 |
| Human Infra mapping | `observation -> lambda(t)`，预测模型必须说明数据来源、特征、结局、验证和偏倚。 |
| Model position | Prediction model reporting, risk-of-bias assessment, applicability, AI trial protocol/reporting, external validation. |
| Evidence level | Reporting guideline / risk-of-bias tool / consensus statement. |
| Transfer boundary | 报告规范不能证明模型准确或干预有效；还需要外部验证、校准、真实世界监测和临床结局证据。 |
| Repository action | 预测模型契约加入 TRIPOD+AI / PROBAST+AI 字段：participants、predictors、outcome、validation、calibration、bias_domain、applicability、fairness；AI 临床试验卡加入 CONSORT-AI / SPIRIT-AI 字段：ai_intervention、input_output_handling、human_ai_interaction、error_case_analysis。 |

## Card 32: Apple Heart Study

| Field | Notes |
| --- | --- |
| Source identity | Perez et al. 2019. *Large-Scale Assessment of a Smartwatch to Identify Atrial Fibrillation*. NEJM. DOI: 10.1056/NEJMoa1901183. <https://www.nejm.org/doi/full/10.1056/NEJMoa1901183> |
| Technology family | 可穿戴与检测。 |
| One-sentence use | 展示消费级可穿戴设备如何进入大规模风险提示和临床验证通道。 |
| Human Infra mapping | `observation -> action`，检测技术先改变观测能力，再可能改变诊疗路径和风险管理。 |
| Model position | Observation process, alert quality, downstream care. |
| Evidence level | Large pragmatic study / clinical endpoint pathway. |
| Transfer boundary | 早筛信号不等于死亡风险下降；误报、依从性、确认诊断和后续治疗决定真实价值。 |
| Repository action | 可穿戴技术族新增字段：alert_rate、positive_predictive_value、confirmatory_test、downstream_action、overdiagnosis_risk。 |

## Card 33: Stage-Based Model of Personal Informatics

| Field | Notes |
| --- | --- |
| Source identity | Li, Dey & Forlizzi. 2010. *A Stage-Based Model of Personal Informatics Systems*. CHI. DOI: 10.1145/1753326.1753409. <https://dl.acm.org/doi/10.1145/1753326.1753409> |
| Technology family | 可穿戴与检测。 |
| One-sentence use | 把自我追踪拆成准备、收集、整合、反思和行动，而不是只看数据采集。 |
| Human Infra mapping | `E/R/C/A`，观测必须转化为反思和行动，才可能进入飞轮。 |
| Model position | Personal data pipeline, feedback loop, behavior translation. |
| Evidence level | HCI model / empirical grounded framework. |
| Transfer boundary | 自我追踪不自动改善健康；中断、负担、解释错误和行动失败都会切断链路。 |
| Repository action | 可穿戴技术族应把 data capture、interpretation、reflection、action 分开建模。 |

## Card 34: Lived Informatics

| Field | Notes |
| --- | --- |
| Source identity | Epstein et al. 2015. *A Lived Informatics Model of Personal Informatics*. UbiComp. DOI: 10.1145/2750858.2804250. <https://dl.acm.org/doi/10.1145/2750858.2804250> |
| Technology family | 知识管理与记忆外化 / 可穿戴与检测。 |
| One-sentence use | 说明自我数据系统嵌入真实生活，会受到日常节奏、目标变化、遗忘和维护负担影响。 |
| Human Infra mapping | `E -> R` and `R -> C`，记录系统必须适应生活，才能长期支持学习和复盘。 |
| Model position | Longitudinal tracking, maintenance burden, lived context. |
| Evidence level | HCI field model. |
| Transfer boundary | 个人信息学模型不能直接证明寿命收益；它主要解释数据系统为什么容易断裂。 |
| Repository action | 记忆外化技术族新增负向指标：maintenance_burden、data_fatigue、context_loss、abandonment_rate。 |

## Card 35: Cognition in the Wild

| Field | Notes |
| --- | --- |
| Source identity | Hutchins, E. 1995. *Cognition in the Wild*. MIT Press. <https://mitpress.mit.edu/9780262581462/cognition-in-the-wild/> |
| Technology family | 知识管理与记忆外化。 |
| One-sentence use | 把认知看成分布在个人、工具、表征、环境和协作流程中的系统。 |
| Human Infra mapping | `C/Q/O`，工具和环境不是外部装饰，而是主体任务能力的一部分。 |
| Model position | Distributed cognition, tool-mediated capability, environment coupling. |
| Evidence level | Foundational cognitive science / ethnographic framework. |
| Transfer boundary | 分布式认知框架不能给出数值效应；具体工具仍需任务实验和错误分析。 |
| Repository action | 知识管理技术族应记录 external_memory、shared_representation、coordination_protocol、failure_recovery。 |

## Card 36: NASA Task Load Index

| Field | Notes |
| --- | --- |
| Source identity | NASA. *NASA Task Load Index (NASA-TLX)*. <https://www.nasa.gov/human-systems-integration-division/nasa-task-load-index-tlx/> |
| Technology family | 自动化与执行系统。 |
| One-sentence use | 为任务系统的心理负荷、时间压力、努力、挫败感和表现代价提供测量入口。 |
| Human Infra mapping | `A -> Q` and `A/Q -> risk`，自动化若降低执行成本但提高认知负担，净收益可能为负。 |
| Model position | Workload metric, friction cost, human factors endpoint. |
| Evidence level | Measurement instrument / human factors standard. |
| Transfer boundary | TLX 是主观负荷测量，不等于客观产出、健康结局或寿命结局。 |
| Repository action | 自动化技术族新增字段：workload_delta、time_pressure、frustration、mental_demand、performance_cost。 |

## Card 37: Types and Levels of Automation

| Field | Notes |
| --- | --- |
| Source identity | Parasuraman, Sheridan & Wickens. 2000. *A Model for Types and Levels of Human Interaction with Automation*. IEEE Transactions on Systems, Man, and Cybernetics. DOI: 10.1109/3468.844354. <https://ieeexplore.ieee.org/document/844354> |
| Technology family | 自动化与执行系统。 |
| One-sentence use | 把自动化拆成信息获取、信息分析、决策选择和行动执行的不同等级。 |
| Human Infra mapping | `A -> Q`，自动化增强必须说明替代了哪一层任务，以及人类保留什么控制权。 |
| Model position | Automation taxonomy, control allocation, failure mode. |
| Evidence level | Human factors model / taxonomy. |
| Transfer boundary | 自动化等级越高不必然越好；失去情境意识、过度信任和异常恢复失败会破坏飞轮。 |
| Repository action | 自动化技术族应记录 automation_level、human_override、exception_handling、situational_awareness_risk。 |

## Card 38: WHO Social Determinants of Health

| Field | Notes |
| --- | --- |
| Source identity | World Health Organization. *Social determinants of health*. <https://www.who.int/health-topics/social-determinants-of-health> |
| Technology family | 资源与环境干预。 |
| One-sentence use | 把健康、寿命和行动能力放回收入、教育、住房、工作、社会保护和环境条件中理解。 |
| Human Infra mapping | `O -> T/E`，可能性空间只有在资源和环境允许时才会反哺主体持续性。 |
| Model position | Environment, access, risk exposure, recovery capacity. |
| Evidence level | Public health framework / official synthesis. |
| Transfer boundary | 社会决定因素框架不能替代具体干预评估；不同地区和制度下路径强度不同。 |
| Repository action | 资源环境技术族新增字段：housing、income_security、education_access、work_conditions、care_access、pollution_exposure。 |

## Card 39: WHO Primary Health Care

| Field | Notes |
| --- | --- |
| Source identity | World Health Organization. *Primary health care*. <https://www.who.int/health-topics/primary-health-care> |
| Technology family | 资源与环境干预。 |
| One-sentence use | 把医疗可及性、预防、连续照护和社区层面的恢复系统纳入主体持续性模型。 |
| Human Infra mapping | `O -> T/E`，资源和制度入口影响早期发现、持续治疗、恢复和风险缓冲。 |
| Model position | Care access, prevention, recovery infrastructure, continuity of care. |
| Evidence level | Public health framework / official synthesis. |
| Transfer boundary | 初级卫生体系是环境条件，不是个体技术；其效果受制度、资金、地理和服务质量约束。 |
| Repository action | 资源环境技术族新增字段：primary_care_access、continuity_of_care、prevention_coverage、follow_up_capacity。 |

## Card 40: BCI Ethics and Neurotechnology Governance

| Field | Notes |
| --- | --- |
| Source identity | Burwell, Sample & Racine. 2017. *Ethical aspects of brain computer interfaces: a scoping review*. BMC Medical Ethics. DOI: 10.1186/s12910-017-0220-y. <https://bmcmedethics.biomedcentral.com/articles/10.1186/s12910-017-0220-y> |
| Technology family | BCI / 神经技术 / 高风险增强技术。 |
| One-sentence use | 为脑机接口、神经数据、同意、身份、责任和主体边界提供伦理审查入口。 |
| Human Infra mapping | `A/Q -> risk` and `C/Q/O`，增强技术可能改变主体能力，也可能改变主体边界和权利结构。 |
| Model position | Risk channel, consent boundary, identity boundary, governance gate. |
| Evidence level | Scoping review / neuroethics. |
| Transfer boundary | 伦理综述不证明 BCI 有效，也不提供临床收益估计；它只限定哪些风险和权利问题必须进入模型。 |
| Repository action | 高风险技术族必须记录 consent、agency、identity、privacy、control、accountability 和 reversibility。 |

## Card 41: GRADE Evidence Certainty

| Field | Notes |
| --- | --- |
| Source identity | GRADE Working Group. *GRADE Handbook*. <https://gdt.gradepro.org/app/handbook/handbook.html> |
| Technology family | 医学干预 / 证据政策 / 治理。 |
| One-sentence use | 把证据质量、证据确定性、收益风险权衡、适用人群和建议强度分开处理。 |
| Human Infra mapping | `U_t -> causal claim` and `A/Q -> risk`，技术价值需要同时记录证据等级、收益、伤害、不确定性和适用边界。 |
| Model position | Evidence policy, causal gate, recommendation boundary. |
| Evidence level | Evidence-to-decision guideline / official handbook. |
| Transfer boundary | GRADE 不替代原始研究，也不证明某个干预有效；它是判断证据质量和建议强度的框架。 |
| Repository action | 每个技术干预卡片应记录 certainty、benefit、harm、values、resources、equity、acceptability 和 feasibility。 |

## Card 42: Marginal Structural Models

| Field | Notes |
| --- | --- |
| Source identity | Robins, Hernan & Brumback. 2000. *Marginal Structural Models and Causal Inference in Epidemiology*. Epidemiology. DOI: 10.1097/00001648-200009000-00011. <https://pubmed.ncbi.nlm.nih.gov/10955408/> |
| Technology family | 因果推断 / 纵向干预评估。 |
| One-sentence use | 处理长期生命路径中时间变化混杂，让“某阶段行动影响后续状态和后续行动”的问题可被审查。 |
| Human Infra mapping | `U_t -> causal claim`，技术、资源和健康状态会随时间互相影响，不能用静态相关性替代因果估计。 |
| Model position | Time-varying confounding, longitudinal causal inference, intervention protocol. |
| Evidence level | Method standard / epidemiological causal inference. |
| Transfer boundary | 方法本身不保证识别成功；权重模型、阳性假设、未测混杂和数据质量仍会造成失败。 |
| Repository action | 后续定量模型应把时间变化混杂、处理历史、删失和敏感性分析列为强因果主张前置条件。 |

## Candidate Promotion Addendum v0.5

本节把 Candidate Source Extraction v0.1 中的 P1 来源晋升为 Source Card 草案。晋升只表示“可进入资料卡片和模型方法层”，不表示它们已经成为正文强引用或完成 fresh reviewer citation-context 审查。

## Card 43: Restricted Mean Survival Time Quick Guide

| Field | Notes |
| --- | --- |
| Source identity | Han & Jung. 2022. *Restricted Mean Survival Time for Survival Analysis: A Quick Guide for Clinical Researchers*. Korean Journal of Radiology. DOI: 10.3348/kjr.2022.0061. <https://pmc.ncbi.nlm.nih.gov/articles/PMC9081686/> |
| Candidate source | SEE1 / SEV1 / SER1. |
| One-sentence use | 为有限随访窗口内的生存曲线面积和 RMST 差异提供有效时间报告语言。 |
| Human Infra mapping | `T -> E`，把生存时间窗口转换成可比较的时间积分代理。 |
| Model position | Survival-curve summary, time horizon, effective-time reporting, censoring boundary. |
| Evidence role | Method source / reporting language. |
| Transfer boundary | RMST 只定义统计摘要，不定义主体连续性、健康质量、行动能力或任何具体干预效果。 |
| Repository action | 用于补强 `T -> E` 的报告字段：time_horizon、rmst_delta、follow_up_window、censoring_rule、clinical_interpretation_boundary。 |

## Card 44: Learning Analytics Review

| Field | Notes |
| --- | --- |
| Source identity | Pan, Biegley, Taylor & Zheng. 2024. *A Systematic Review of Learning Analytics*. Journal of Learning Analytics. DOI: 10.18608/jla.2023.8093. <https://learning-analytics.info/index.php/JLA/article/view/8093> |
| Candidate source | SEE2 / SEV2 / SER2. |
| One-sentence use | 把有效时间是否进入学习过程，转化为 LMS 日志、学习分析干预、反馈事件和学习结果观测问题。 |
| Human Infra mapping | `E -> R`，有效时间只有被组织成可记录、可反馈、可调整的学习行为，才可能进入轮次变量。 |
| Model position | Learning trace, intervention exposure, feedback loop, process measurement. |
| Evidence role | Systematic review candidate for measurement and learning-intervention taxonomy. |
| Transfer boundary | 学习分析证据不能证明寿命延长自动产生学习，也不能证明所有学习日志都代表高质量能力增长。 |
| Repository action | 给 `R` 变量新增代理指标：logged_learning_action、feedback_event、intervention_exposure、task_completion、reflection_event。 |

## Card 45: Self-Regulated Learning with Multimodal Data and AI

| Field | Notes |
| --- | --- |
| Source identity | de Mooij et al. 2025. *A Systematic Review of Self-Regulated Learning through Integration of Multimodal Data and Artificial Intelligence*. Educational Psychology Review. DOI: 10.1007/s10648-025-10028-0. <https://link.springer.com/article/10.1007/s10648-025-10028-0> |
| Candidate source | SEE3 / SEV3 / SER3. |
| One-sentence use | 为学习轮次中的监控、控制、情绪、动机和策略调整提供过程变量与多模态观测入口。 |
| Human Infra mapping | `R -> C`，学习轮次需要自我调节和过程反馈，才可能沉淀为能力资本。 |
| Model position | SRL process, multimodal traces, temporal sequence, capability accumulation proxy. |
| Evidence role | Systematic review candidate for construct mapping and measurement design. |
| Transfer boundary | SRL 过程观测不证明长期迁移、抗遗忘、跨域能力增长或能力积累不会饱和。 |
| Repository action | 给 `R -> C` 增加代理指标：monitoring_action、control_action、strategy_shift、affective_state、metacognitive_signal、multimodal_trace_quality。 |

## Card 46: NIST Deployed AI Monitoring

| Field | Notes |
| --- | --- |
| Source identity | Rao. 2026. *Challenges to the Monitoring of Deployed AI Systems*. NIST AI 800-4. DOI: 10.6028/NIST.AI.800-4. <https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.800-4.pdf> |
| Candidate source | SEE8 / SEV8 / SER8. |
| One-sentence use | 为 AI 工具进入主体系统后的部署监测、漂移、异常输出、事故和大规模影响提供治理分类。 |
| Human Infra mapping | `A/Q -> risk`，AI 增强必须同时建模净收益、监测成本、漂移风险和回滚能力。 |
| Model position | Post-deployment monitoring, incident tracking, drift detection, compliance and human-factors gate. |
| Evidence role | Official NIST method and governance source. |
| Transfer boundary | 该报告不提供任何具体 AI 系统的收益、失败率或生产率效应，只提供监测挑战和分类语言。 |
| Repository action | 给 AI 技术族新增字段：post_deployment_monitoring、drift_signal、incident_log、human_factor_issue、large_scale_impact、rollback_trigger。 |

## Card 47: Target Trial Emulation Bridge

| Field | Notes |
| --- | --- |
| Source identity | Riggi, Segelov & Di Tanna. 2026. *Target trial emulation: bridging observational studies and randomized trials for health decision-making*. Journal of Comparative Effectiveness Research. DOI: 10.57264/cer-2025-0180. <https://pmc.ncbi.nlm.nih.gov/articles/PMC13044815/> |
| Candidate source | SEE9 / SEV9 / SER9. |
| One-sentence use | 把观察性研究问题转写成人群、策略、分配、随访、结局、估计量和分析方法明确的目标试验协议。 |
| Human Infra mapping | `U_t -> causal claim`，任何技术或干预进入寿命模型前，都必须先写清 target trial 风格的 causal question。 |
| Model position | Protocol specification, time zero, comparator, follow-up, outcome, estimand, analysis plan. |
| Evidence role | Method source / causal protocol bridge. |
| Transfer boundary | 目标试验模拟不能验证具体 Human Infra 干预，也不能自动消除未测混杂、选择偏差、阳性假设失败或测量错误。 |
| Repository action | 对照现有 `estimandRegistry` 和 `analysisPlanRegistry`，继续补 eligibility、assignment_procedure、follow_up_start、censoring_rule、emulation_gap 和 sensitivity_plan。 |

## Immediate Repository Actions

1. 将 v0.5 的新增代理指标同步到 `variableDictionary`、`estimandRegistry` 和 `analysisPlanRegistry`。
2. 在 Web 论文页把技术族卡片做成可展开 evidence panel。
3. 为每个指标补数据源、采样频率、缺失处理和最小可复现实验设计。
4. 继续处理 P2 候选来源：SEE5、SEE6、SEE7；SEE4 保持 metadata-only 暂停。
