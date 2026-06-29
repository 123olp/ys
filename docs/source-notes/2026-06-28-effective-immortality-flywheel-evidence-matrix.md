# 有效永生飞轮 Evidence Matrix v1.3

Status: draft evidence matrix v1.3  
Related paper: [Effective Immortality Acceleration Flywheel](../explanations/effective-immortality-acceleration-flywheel.md)  
Related cards: [Source Cards v0.5](2026-06-28-effective-immortality-flywheel-source-cards.md)
Web data mirror: [`web/src/data/effective-immortality-evidence.json`](../../web/src/data/effective-immortality-evidence.json)

## Purpose

本文件不作为文献列表使用；它把“有效永生带来的主体持续性加速回报飞轮”拆成可验证的边。每一行都回答：

```text
链路边
  -> 要验证的问题
  -> 可复用的科研来源
  -> 它真正支持什么
  -> 它不能支持什么
  -> 下一步如何进入模型
```

## Evidence Matrix

| 链路边 | 可检验问题 | 候选来源 | 证据角色 | 当前置信 | 断裂条件 | 下一步任务 |
| --- | --- | --- | --- | --- | --- | --- |
| `T -> E` | 寿命窗口延长是否转化为有效时间，而不是单纯延长失能期 | Kaplan-Meier；Cox；Grossman health capital；WHO HALE；QALY 评估传统 | 生存函数、风险函数、健康资本和质量调整时间的语言 | Medium | 寿命延长但健康质量、行动能力、主体性下降 | 定义 `E = survival * health_quality * agency` 的路径积分 |
| `E -> R` | 有效时间是否增加学习、试错、复盘和长期项目轮次 | Deliberate Practice；Law of Practice；Self-Regulated Learning | 说明轮次必须带有目标、反馈、调整和可迁移练习 | Medium | 低质量重复、无反馈、注意力碎片、目标漂移 | 区分日历时间、清醒时间、有效学习时间和反馈轮次 |
| `R -> C` | 轮次如何沉淀为经验、技能、判断、知识和网络 | Deliberate Practice；Law of Practice；Feedback Intervention Theory；Human/Social Capital | 支撑能力积累、学习曲线、反馈质量和资本沉淀 | Medium | 学习饱和、错误反馈、遗忘、能力不可迁移 | 建立非线性学习曲线和衰减项 |
| `C -> A` | 经验、资源、信誉和网络是否提高技术采用能力 | TAM；UTAUT；Diffusion of Innovations；Human Capital | 技术采用受有用性、易用性、社会影响、资源和情境约束影响 | Medium | 技术不可及、学习成本过高、信任错误、采用后无法整合 | 将采用拆成 access、understanding、evaluation、trial、integration |
| `A -> Q` | 技术采用是否提高单位时间行动质量和创造密度 | Generative AI at Work；Noy & Zhang；GitHub Copilot RCT；Jagged Technological Frontier | AI 工具在限定任务中提升速度、质量或吞吐，并显示异质性 | Medium-High for narrow tasks | 任务在 AI 能力边界外、过度依赖、幻觉、缺少 QA | 建立按任务类型分层的 AI frontier map |
| `Q -> O` | 更高行动质量是否扩大真实可能性空间 | Capability Approach；Human/Social Capital；AI productivity evidence | 把产出能力转译为真实可行选择权和路径入口 | Medium-Low | 产出不等于选择权；制度、身份、资源和风险限制进入 | 定义 `O` 为 feasible option set，而不是抽象愿望 |
| `O -> T/E` | 可能性空间如何反过来强化主体持续性 | Social relationships mortality meta-analysis；Health Capital；Digital Twin；care access literature | 资源、关系、医疗可及性和恢复系统可能影响生存与健康质量 | Medium | 选择权无法访问、社会资本排他、资源转化失败 | 拆分 resources、support、care、recovery、risk governance |
| `A/Q -> risk` | 技术增强是否同时引入副作用和尾部风险 | Jagged Frontier；AI risk governance；BCI ethics；evidence policy | 增强技术可能越界、误导、放大监控或降低判断质量 | Medium | 把技术效果只记为正收益，忽略误用、依赖和治理失败 | 为每个技术干预增加 downside channel 和治理门禁 |
| `U_t -> causal claim` | 技术或干预能否从相关信号升级为因果主张 | Target trial emulation；marginal structural models；model governance contract | 要求先定义 population、comparator、time zero、outcome、estimand 和识别假设 | High as method gate | 不可测混杂、阳性失败、选择偏差、time zero 错误 | 将每个干预卡片改写成 target-trial protocol |

## Claim Register v0.1

Claim Register 的用途是把论文核心主张拆成可审查对象。它不增加证明强度，只规定每条主张当前属于哪种类型、已有支持是什么、升级到更强论文结论还需要补什么。

| 编号 | 主张类型 | 当前状态 | 升级要求 |
| --- | --- | --- | --- |
| CL1 | Conceptual framing | 有效永生飞轮是框架提案 | 需要变量字典和案例研究证明其解释力超过单一寿命指标 |
| CL2 | Model interface | `T/E/R/C/A/Q/O` 是第一版操作定义 | 需要补单位、代理指标、缺失处理和可重复测量方案 |
| CL3 | Method claim | 技术作为状态转移或风险函数算子的表述有方法论支持 | 每个技术族必须写成 target-trial style protocol |
| CL4 | Task-limited empirical claim | AI 工具收益只支持限定任务内的 `A -> Q` | 需要任务族分层和 downside channel 同步测量 |
| CL5 | Normative and measurement claim | 可能性空间采用 Capability Approach 语言 | 需要把 `O` 拆成真实可进入路径和进入条件 |
| CL6 | Governance claim | 所有增强技术必须建模负向通道 | 需要停止条件、回滚条件和事故复盘模板 |
| CL7 | Prohibited claim boundary | 本文不证明永生实现，不输出个人死亡日期 | 后续页面、图表和模型输出必须持续保留该边界 |

## Alternative Explanations / Rival Models v0.1

本节把飞轮模型放进竞争解释集合中。后续定量分析必须先让更简单模型解释数据，再检验 `T/E/R/C/A/Q/O` 反馈项是否提供额外解释力。

| 模型 | 核心解释 | 关键检验 |
| --- | --- | --- |
| 单纯寿命窗口模型 | `T` 增加带来更多等待和行动机会 | `T` 增加后若 `E/R/C/A/Q/O` 不随之增长，飞轮不成立 |
| 健康资本 / 有效时间模型 | 健康质量和可行动时间 `E` 解释主体持续性 | 若 `E` 能解释大部分长期行动能力变化，飞轮反馈项需要降级 |
| 能力积累 / 人力资本模型 | 学习、经验、资源和协作网络 `C` 解释长期表现 | 若 `C` 的差异独立解释技术采用和行动质量，模型中心应转向积累质量 |
| AI / 工具增强模型 | 技术采用 `A` 直接提高任务质量 `Q` | 若收益只发生在短期任务边界内，不应外推为主体持续性飞轮 |
| 能力方法 / 社会决定因素模型 | 真实可能性空间 `O` 由资源、制度、医疗和社会支持决定 | 若 `Q` 提升但真实入口不增加，`Q -> O` 边被否定 |
| 风险反噬 / 治理失败模型 | 技术和复杂性同时增加依赖、事故、监控和尾部风险 | 若风险扣减高于收益，飞轮应改写为负反馈或风险放大器 |
| Human Infra 飞轮模型 | 多条边形成正反馈，且负向通道未压过正向通道 | 只有替代模型不能单独解释，且反馈项跨时间稳定时才升级为飞轮主张 |

## Model Comparison Protocol v0.1

Model Comparison Protocol 将替代模型表转成可执行门禁。后续任何玩具模型、案例研究或预测模型都必须按此顺序报告，不允许直接拟合飞轮曲线并宣称加速回报。

| 阶段 | 科研门禁 |
| --- | --- |
| MCP1 候选模型冻结 | 分析前冻结候选模型、变量接口、非主张边界和失败条件 |
| MCP2 共享结局定义 | 所有模型预测同一组 `E/R/C/A/Q/O`、风险扣减和净主体持续性结局 |
| MCP3 简单模型优先 | 先让单变量或低反馈模型解释结果，再加入飞轮反馈项 |
| MCP4 反馈项增量检验 | 检查滞后项、交互项、中介路径和敏感性分析是否支持正反馈 |
| MCP5 风险扣减与净值判断 | 同步计算 downside channel、QA 成本、恢复负担、事故率和停止条件 |
| MCP6 外推边界检查 | 按任务族、人群、资源条件、制度环境和技术可及性分层 |
| MCP7 决策规则 | 只有简单模型不足、反馈项有增量、风险扣减后为正、外推边界清楚且 citation context 通过审查时，才升级为飞轮主张 |

## Candidate Model Specification Registry v0.1

候选模型规格表规定每个模型的变量、反馈项、主结局、比较角色和降级条件。后续定量模型必须先声明自己属于哪一个候选模型，或明确说明为什么需要新增模型。

| ID | 模型 | 变量与反馈 | 主结局 | 比较角色 |
| --- | --- | --- | --- | --- |
| CM1 | 单纯寿命窗口模型 | `T`；无反馈项 | 生存时间、等待窗口、可观察未来年份 | 最低复杂度基线 |
| CM2 | 健康资本 / 有效时间模型 | `T/E`；健康状态转移 | 健康质量调整有效时间、无失能生存、可行动小时数 | 检验健康质量是否足以解释主体持续性 |
| CM3 | 能力积累 / 人力资本模型 | `R/C`；学习曲线、衰减项、迁移项 | 能力存量、任务迁移表现、资源和协作网络增长 | 检验积累质量是否足以解释长期表现 |
| CM4 | AI / 工具增强模型 | `A/Q`；任务级工具增益和 QA 扣减 | 质量调整任务产出率、完成时间、错误率、返工率 | 检验收益是否只是任务级增强 |
| CM5 | 能力方法 / 社会决定因素模型 | `O`；真实可进入路径、资源和制度入口 | 可行选择集合、真实进入率、资源/制度/照护入口变化 | 检验未来选择权是否由社会条件解释 |
| CM6 | 风险反噬 / 治理失败模型 | `Risk_t`；负反馈、尾部风险和收益扣减 | 净主体持续性价值、事故率、回滚成功率 | 检验正反馈是否被副作用和治理成本抵消 |
| CM7 | Human Infra 飞轮模型 | `T/E/R/C/A/Q/O/Risk_t`；正反馈与负反馈全链路 | 风险扣减后的主体持续性、行动质量、能力系统和可能性空间复合变化 | 完整模型，只在简单模型不足时进入强解释位置 |

## Model Comparison Reporting Matrix v0.1

Model Comparison Reporting Matrix 是未来模型结果的最小报告清单。它防止只展示支持飞轮的曲线，而不报告基线模型、不确定性、风险扣减和失败条件。

| 项目 | 必须回答的问题 |
| --- | --- |
| MCR1 冻结模型集 | 参与比较的模型是否在分析前冻结，是否能回到 CM1-CM7 |
| MCR2 共享结局与估计量 | 所有模型是否预测同一批结局和估计量 |
| MCR3 Time zero 与随访窗口 | 起点、滞后、随访和删失规则是否一致 |
| MCR4 缺失、删失和测量误差 | 是否报告缺失率、删失率、测量误差和敏感性版本 |
| MCR5 简单模型基线表现 | CM1-CM6 是否先于飞轮模型被报告 |
| MCR6 反馈项增量 | 飞轮反馈项是否提供稳定增量 |
| MCR7 风险扣减后净值 | 正向收益是否扣除了 downside channel、QA 成本和恢复负担 |
| MCR8 不确定性与校准 | 关键效应是否带置信区间、预测区间或校准证据 |
| MCR9 敏感性、负控和反证 | 参数扫描、负控和失败案例是否进入报告 |
| MCR10 分层与外推边界 | 成立边界和不可外推边界是否同时报告 |
| MCR11 决策与降级 | 模型胜出、平局、降级或拒绝如何决定 |
| MCR12 可复现产物 | 每个数值和图表是否能回到数据、参数、命令、hash 和审计日志 |

## Model Comparison Result Contract v0.1

Model Comparison Result Contract 是未来定量结果的字段级接口。它要求每一次模型比较都用同一套字段导出，避免论文、网页和图表引用了无法追溯、无法比较或无法降级的结果。

| 字段 | 必须回答的问题 |
| --- | --- |
| runId | 这一次模型比较运行是否有唯一编号 |
| contractVersion | 结果是否使用当前字段契约 |
| modelId | 结果是否能回到 CM1-CM7 中的某个候选模型 |
| outcome | 结果预测或解释的是哪一个主体持续性结局 |
| estimand | 结果是描述、预测还是因果估计，目标量是否明确 |
| timeZero | 模型计时起点是否明确 |
| populationOrScope | 结果适用于什么人群、任务或场景 |
| dataWindow | 随访、滞后、删失和数据窗口是否明确 |
| estimator | 使用了什么统计、因果、预测或模拟方法 |
| effectEstimate | 主效应大小、方向和单位是否明确 |
| uncertainty | 是否报告置信区间、预测区间、后验区间或场景区间 |
| calibrationOrFit | 是否报告校准、拟合、预测或解释性指标 |
| riskAdjustment | 是否扣减副作用、QA 成本、依赖、事故和恢复负担 |
| sensitivityStatus | 敏感性、负控或反证检查是否完成 |
| reproducibilityArtifacts | 数据、参数、命令、输出、图表和 hash 是否可追溯 |
| claimUpgradeDecision | 该结果允许升级、保留、降级还是拒绝主张 |
| citationContextGate | 引用语境是否通过、警告、待审或失败 |

## Claim Evidence Map v0.1

Claim Evidence Map 是 Claim Register 的审计层。它把每个核心主张连接到正文位置、证据边、引用上下文、反证条件和升级门槛，避免后续写作把真实来源用于错误主张。

| 主张 | 正文位置 | 证据边 | 引用上下文 | 当前判定 | 反证条件 | 升级门槛 |
| --- | --- | --- | --- | --- | --- | --- |
| CL1 | S1；S2；S4；S6 | `T -> E`；`E -> R`；`R -> C`；`C -> A`；`A -> Q`；`Q -> O`；`O -> T/E` | CTX2；CTX4；CTX5；CTX6；CTX7；CTX12 | FRAMEWORK_ONLY | 关键边长期不成立；负向通道压过正向通道；新增寿命无法转化为有效时间 | 完成至少一个案例研究或仿真，证明该框架比单一寿命指标更能解释长期行动能力 |
| CL2 | S5；S12；S13 | `T -> E`；`E -> R`；`R -> C`；`C -> A`；`A -> Q`；`Q -> O`；`O -> T/E`；`A/Q -> risk` | CTX1；CTX2；CTX4；CTX5；CTX6；CTX7；CTX8；CTX12 | OPERATIONAL_INTERFACE | 变量无法被稳定代理测量；变量之间高度重叠导致不可识别；关键主体状态被遗漏 | 为每个变量补齐单位、代理指标、缺失处理、时间窗、适用人群和可重复测量方案 |
| CL3 | S5；S11；S13 | `U_t -> causal claim`；`T -> E` | CTX1；CTX9 | METHOD_SUPPORTED | 没有 comparator；time zero 错误；结局定义偷换；不可测混杂压倒识别假设 | 每个技术族必须给出 population、intervention、comparator、time zero、outcome、estimand 和识别假设 |
| CL4 | S8；S10；S12 | `A -> Q`；`A/Q -> risk` | CTX7；CTX8 | BOUNDED_EMPIRICAL | 任务进入 jagged frontier 失败区；QA 成本抵消速度收益；幻觉或自动化偏差提高返工；高技能主体收益不稳定 | 按任务族建立 AI frontier map，并同步记录速度、质量、错误、QA 成本、依赖和异质性 |
| CL5 | S3；S8；S12 | `Q -> O`；`O -> T/E` | CTX5；CTX12 | NORMATIVE_MEASUREMENT | 产出提高但资源、权限、身份或制度入口不增加；机会只能叙述不能进入；新增路径带来更高暴露和恢复负担 | 把 `O` 拆成资源入口、制度入口、协作入口、技术窗口和可逆选择，并定义进入条件 |
| CL6 | S10；S11；S14 | `A/Q -> risk`；`U_t -> causal claim` | CTX8；CTX9；CTX10；CTX11 | GOVERNANCE_REQUIRED | 技术收益只记正项；停止条件缺失；回滚路径缺失；事故复盘缺失；主体权利和同意边界缺失 | 为每个技术族建立 downside channel、监测指标、停止条件、回滚条件和事故复盘模板 |
| CL7 | S3；S7；S11；S14；S16 | `U_t -> causal claim`；`A/Q -> risk` | CTX1；CTX3；CTX7；CTX8；CTX9 | HARD_BOUNDARY | 页面输出个体死亡日期；机制合理被写成干预效果；短期任务收益被写成寿命延长；引用上下文越界 | 后续图表、模型和传播材料必须持续保留非主张边界，并接受 claim-to-source 审计 |

## Estimand Registry v0.1

Estimand Registry 将每条证据边压成后续可估计的研究契约。它不证明效应成立，只规定任何定量模型或实证研究必须先补齐人群、干预或暴露、比较组、time zero、结局、估计对象和识别风险。

| 链路边 | Population | Intervention / Exposure | Comparator | Outcome / Estimand | 主要识别风险 |
| --- | --- | --- | --- | --- | --- |
| `T -> E` | 给定年龄、疾病状态、资源条件和主体连续性阈值的主体或人群 | 延长生存窗口或降低主体失效风险的医学、照护、资源或环境策略 | 常规照护、未干预、延迟干预或替代持续性策略 | 有效时间积分或 `S(t)` 的平均差异 | immortal time bias、适应证混杂、失访、健康质量代理偏差 |
| `E -> R` | 具备最低健康、认知和任务参与能力的主体或人群 | 可行动有效时间增加，或恢复/睡眠/健康管理提高反馈学习时间比例 | 有效时间不变、碎片化时间增加或只增加日历寿命 | 有效学习轮次数的平均差异或比率差异 | 时间质量不可测、任务选择偏差、低质量重复被误计 |
| `R -> C` | 在可比任务领域持续参与学习、工作或研究项目的主体或团队 | 更多高质量反馈轮次、刻意练习、复盘或项目迭代 | 较少轮次、无反馈重复或低质量反馈路径 | 积累资本 `C` 的平均变化差异，含增长和衰减 | 学习饱和、幸存者偏差、反馈质量混杂、能力不可迁移 |
| `C -> A` | 拥有不同经验、资源、技能和协作网络基础的技术使用者或团队 | 知识结构、资源冗余、信誉入口、技术理解和协作网络增强 | 低积累资本或缺少资源/网络/知识支持 | 技术采用成功率、采用时滞或整合质量的平均差异 | 反向因果、资源可及性混杂、采用后失败遗漏 |
| `A -> Q` | 在明确任务族内使用特定技术的人或团队 | 经证据门禁通过的 AI、自动化、知识系统、检测或医学辅助工具采用 | 不使用、延迟使用、替代工具或常规流程 | 质量调整任务产出率 `Q` 的平均处理效应 | 任务 frontier 错判、QA 成本漏计、自动化偏差、选择性使用 |
| `Q -> O` | 在任务、资源、制度和协作入口受约束的主体或团队 | 单位时间行动质量、产出密度、反馈速度和复杂问题处理能力提高 | 行动质量不变或速度提升但质量/可信度下降 | 可行选择集合 `O` 的平均边际变化 | 抽象机会误计、制度门槛、身份/资源限制 |
| `O -> T/E` | 拥有不同社会支持、医疗可及、资源缓冲和制度入口的主体或人群 | 医疗、照护、风险缓冲、资源入口和可逆选择增加 | 可能性空间受限、资源入口少、照护不足或选择不可逆 | `T/E` 的平均差异，优先报告健康质量调整时间 | 社会资本选择偏差、地区制度混杂、反向因果 |
| `A/Q -> risk` | 使用增强技术、自动化、AI、检测、医学或神经工具的主体或团队 | 技术采用和行动质量提高，同时暴露于副作用、依赖、误用、监控或尾部风险 | 不采用技术、低自动化、人工复核更强或治理门禁更严格 | `Risk_t` 的平均增量及其对净主体持续性价值的扣减 | 负面事件低频、漏报、组织沉默、短随访、幸存者偏差 |
| `U_t -> causal claim` | 任何声称技术、医学、工具、环境或资源策略改变主体持续性的研究对象 | 候选技术或干预 `U_t` | 不干预、常规照护、替代策略、延迟策略或不同强度策略 | `U_t` 相对 comparator 对目标结局的因果效应 | 比较组缺失、time zero 错误、替代终点偷换、时间变化混杂 |

## Analysis Plan Registry v0.1

Analysis Plan Registry 是 Estimand Registry 的下一层：每条边必须有候选研究设计、最小数据、主估计器、诊断、敏感性检查和报告输出。它的作用是防止“可估计对象”停留在协议名词，而没有实际分析路径。

| 链路边 | 候选设计 | 主估计器 | 必须诊断 | 敏感性检查 | 报告输出 |
| --- | --- | --- | --- | --- | --- |
| `T -> E` | RCT、target trial emulation、前瞻队列、自然实验或 registry cohort | Kaplan-Meier、RMST、Cox 或 flexible survival model | 删失、比例风险、失访、结局一致性 | competing risks、IPCW、未测混杂 | 生存曲线差、RMST 差、健康质量调整有效时间差 |
| `E -> R` | 纵向日志、时间使用研究、N-of-1 或多基线设计 | mixed-effects count model、event-rate model 或 interrupted time series | 轮次编码、过度离散、零膨胀、任务难度漂移 | 排除无反馈重复、轮次阈值扫描、任务族分层 | 高质量反馈轮次率、轮次质量分布、无效重复比例 |
| `R -> C` | 技能纵向评估、刻意练习 cohort、learning curve 或项目组合追踪 | hierarchical learning curve、growth curve 或 state-space model | 测验等值性、ceiling effect、迁移有效性 | 不同学习曲线形式、反馈质量剔除、衰减率扫描 | 能力增长率、迁移效果、资本存量变化和饱和点 |
| `C -> A` | 技术采用 cohort、diffusion study、quasi-experiment 或平台日志 | discrete-time hazard、adoption time model 或 mediation model | 反向因果、选择进入、右删失、采用定义 | 技术族分层、成功阈值变化、废弃作为失败事件 | 采用时滞、采用成功率、整合质量和废弃比例 |
| `A -> Q` | 任务随机实验、field rollout、stepped-wedge 或 A/B test | ITT/TOT contrasts、DiD 或 hierarchical task model | frontier 分类、污染、学习效应、评分者一致性 | QA 成本扣减、边界外任务报告、技能分层 | 质量调整任务产出率、速度-质量权衡、净效应和失败率 |
| `Q -> O` | opportunity-set panel、项目/职业面板、网络资源研究或 mixed methods | panel model、transition model、network growth 或 capability-set index | 真实入口验证、路径重复计数、制度门槛遗漏 | 路径质量加权、可逆性阈值、资源限制分层 | 可行选择集合变化、真实进入率和路径质量分布 |
| `O -> T/E` | 自然实验、政策差异、社会支持 cohort、医疗可及 cohort 或 target trial emulation | MSM、DiD、IV 或 time-varying survival model | 时间变化混杂、反向因果、地区趋势、政策暴露 | 负控、placebo timing、IPW truncation、未测混杂分析 | 生存/健康寿命差、有效时间差和资源转化失败率 |
| `A/Q -> risk` | safety surveillance、incident registry、post-deployment monitoring 或 red-team evaluation | adverse event rate、time-to-incident 或 severity-weighted harm index | 低频事件功效、漏报、组织沉默、暴露误分 | 主动/被动监测对比、近失事件、尾部风险场景 | 风险增量、净效应扣减、停止条件触发率和回滚成功率 |
| `U_t -> causal claim` | target trial protocol、registered RCT、前瞻观察协议或 prediction-model validation | risk difference、hazard ratio、RMST difference、ATE/CATE 或校准/区分指标 | 交换性、一致性、阳性、time zero、缺失、外部验证 | negative controls、quantitative bias analysis、alternative estimands | 目标试验协议表、主估计、敏感性分析、非主张边界 |

## AI Task Evidence Register v0.3

`A -> Q` 的证据必须从“技术叙事”下降到具体任务。v0.3 注册表只收录四个高相关 AI 任务实验，并把每条证据限制在它真正能支持的模型位置。该表已补 full-text audit 和 method-audit 字段：样本、设计、效应估计、统计不确定性、主表/主图、主要规格、质量评分协议、QA 成本、证据等级和外推边界。

| ID | 来源键 | 证据等级 | 样本与设计 | 效应估计 | 统计/不确定性 | QA / 外推边界 |
| --- | --- | --- | --- | --- | --- | --- |
| AQ1 | `brynjolfsson2025generative` | Level III controlled workplace rollout | QJE 正式版约 5,172 名客服；NBER full-text audit 版本 5,179 名客服、约 300 万次聊天；分阶段上线，agent-month 层级分析 | Table 2 preferred level outcome：每小时解决数 `0.301`，SE `0.0498`；preferred log outcome `0.138`，SE `0.0199` | DiD / fixed effects；标准误聚类到 agent location；Appendix Table A.1 替代 DiD 估计范围 `0.116-0.257` | 只支持结构化客服任务内 `A -> Q`；直接 QA 审阅时间未量化，需并行看 resolution rate、NPS、sentiment、AHT 和异常案例 |
| AQ2 | `noy2023productivity` | Level II randomized online experiment | 453 名有经验、大学学历专业人员；预注册在线随机实验；约一半随机获得 ChatGPT access | 完成时间约下降 40%；评分质量约提高 18%；后测少用约 11 分钟，评分提高约 0.45 SD | 时间和评分 p<0.001；处理组注册成功率约 92%，对照组存在 10-20% 使用污染 | 支持短写作任务内速度/质量改善；不能外推到长周期研究、战略判断或主体持续性 |
| AQ3 | `peng2023copilot` | Level II randomized experiment, preprint | 95 名 Upwork 程序员；45 treatment、50 control；35/35 完成任务进入时间比较 | treatment 71.17 分钟，control 160.89 分钟；完成时间下降 55.8% | t-test p=0.0017；95% CI [21%, 89%]；成功率 +7pp 不显著，CI [-0.11, 0.25] | 支持局部编程任务提速；不能外推到大型系统设计、长期维护或安全关键代码 |
| AQ4 | `dellacqua2026jagged` | Level II professional-task experiment | 852 名咨询人员回应，758 名完成；随机分配 no AI、GPT-4、GPT-4 + prompt overview；385 frontier 内任务，373 frontier 外任务 | frontier 内 Table 1/2/3：质量、完成率和时间显著改善；frontier 外 Table 4：正确率下降 `0.139-0.245` | 线性回归与稳健标准误；outside-frontier 显示速度和推荐质量可改善，但正确率下降 | 同时支持 `A -> Q` 和 `A/Q -> risk`；必须先判断任务是否在 AI 能力边界内 |

### AI Task Method Audit v0.3

| ID | 主表/主图与规格 | 统计列与不确定性 | 质量评分协议 | QA 成本与外推限制 |
| --- | --- | --- | --- | --- |
| AQ1 | NBER full-text Table 2 columns 3/6；Table 3；Table 4；Appendix Table A.1。主规格为 staggered rollout DiD，并包含 year-month、location、agent、agent-tenure FE。 | Table 2：`0.301` resolutions/hour，SE `0.0498`；log outcome `0.138`，SE `0.0199`。Table 3 记录 AHT、calls/hour、resolution rate、NPS；Table 4 记录 customer/agent sentiment。 | resolutions/hour 为主结局；AHT、calls/hour、resolution rate、NPS 和 SiEBERT sentiment 为质量代理；AI 建议由 agent 采纳或忽略。 | 直接 QA 审阅时间未量化；外推只限结构化客服任务。 |
| AQ2 | Figure 1/2、Table 1、footnotes 22-27。主规格为 within-participant pre/post change regression，含 occupation-by-task-order FE 和 incentive-arm FE。 | 时间少约 11 分钟，`0.75 SD`，control mean 27 分钟，`p<0.001`；评分 `+0.45 SD`，`p<0.001`；15 分钟固定时间组 `+0.33 SD` 不显著。 | 三名同职业盲评者按 1-7 分评分；平均 within-essay cross-evaluator correlation 为 `0.44`。 | 92% 注册、80% 使用；对照污染约 10-20%；事实核查成本未数值化。 |
| AQ3 | Figure 6 完成时间分布；Table 1 异质性回归；随机分配 Copilot access，主要时间比较限定完成者。 | Treatment `71.17` 分钟，control `160.89` 分钟；下降 `55.8%`，t-test `p=0.0017`，95% CI `[21%, 89%]`；成功率 `+7pp` 不显著。 | HTTP server 任务必须通过 12 个测试；时间从 repo creation 到 first commit passing all tests。 | QA 不覆盖长期维护、安全、code review 或隐藏缺陷；外推只限小型局部实现。 |
| AQ4 | Inside-frontier Tables 1-3；outside-frontier Tables 4-6；Figures 3/4/7；随机分配 no AI、GPT-4、GPT-4 + prompt overview。 | Inside：quality `1.556-1.746`，completion `0.090-0.111`，time `-1388` 到 `-1129` 秒。Outside：correctness `-0.139` 到 `-0.245`，time `-689` 到 `-407` 秒，recommendation quality `1.046-1.475`。 | Frontier 内两名 human graders 逐题评分并计算 composite Quality；frontier 外 correctness 为二元指标，recommendation quality 按 1-10 rubric 评分。 | 直接量化边界外失败：更快输出和更高表象质量可伴随正确率下降 13-25 个百分点。 |

## Variable Dictionary v0.1

变量字典的用途是把 `T/E/R/C/A/Q/O` 从解释性概念升级为可建模字段。每个变量都必须说明角色、状态类型、单位、代理指标、失败模式和模型用途，后续图表和定量草案优先消费 Web JSON 中的同名字段。

| 符号 | 变量 | 状态类型 | 单位 | 代理指标 | 失败模式 | 模型用途 |
| --- | --- | --- | --- | --- | --- | --- |
| `T` | 主体持续时间 | time / survival | 年、随访时间或给定时间窗内的生存概率 | 生存状态；`S(t)=P(T>t)`；全因死亡或主体失效终点 | 日历寿命增加，但失能、失智、依赖或主体性丧失占主导 | 作为有效时间积分的外层边界，并进入风险函数与生存曲线 |
| `E` | 有效时间 | quality-adjusted agency time | 可行动小时、质量调整年或健康行动时间比例 | HALE/QALY 代理；ADL/IADL；认知功能；可行动小时 | 新增时间被疾病、疲劳、疼痛、依赖或注意力碎片化吸收 | 驱动学习轮次 `R`，是寿命叙事进入问题求解模型的桥梁 |
| `R` | 学习/修正轮次 | process count | 反馈闭环、项目迭代或刻意练习周期 | 刻意练习次数；项目迭代数；复盘记录；反馈循环 | 无反馈重复、目标漂移、错误反馈、低质量练习或学习饱和 | 把有效时间转换为积累资本 `C` |
| `C` | 积累资本 | stock | 潜在能力、资源和网络存量 | 技能测试；知识资产；资源储备；网络强度；信誉资产 | 遗忘、衰退、路径锁定、不可迁移、资源耗散或关系失效 | 降低长期目标成本，并提高技术采用能力 `A` |
| `A` | 技术采用能力 | policy / action capacity | 成功整合概率、采用速度或可靠使用率 | 技术可及性；理解成本；评估准确率；试用转整合比例；工作流嵌入率 | 盲目采用、误信工具、工具锁定、不可及、不可维护或误用 | 选择会改变状态转移、观测能力、行动质量或风险函数的干预 |
| `Q` | 单位时间行动质量 | performance rate | 质量调整任务产出 / 有效时间 | 任务吞吐；质量评分；错误率；反馈延迟；可处理复杂度 | 速度增加但质量下降、QA 成本上升、幻觉、返工或自动化偏差 | 把技术采用与积累资本转化为可解决问题范围和可能性空间 `O` |
| `O` | 可能性空间 | feasible option set | 可进入路径的数量、质量、可逆性和进入概率 | 医疗可及；资源入口；制度入口；协作机会；可逆选择；技术窗口 | 机会只停留在叙事层，受身份、资源、制度、风险或健康限制无法进入 | 通过照护、恢复、风险治理、资源和技术窗口反哺 `T` 与 `E` |

## Model Contract v0.1

公式推导采用 `formula-derivation` 的约束：先冻结不变量，再定义状态、行动、算子、目标函数和边界。当前状态是 `COHERENT AFTER REFRAMING`：研究对象已从寿命长度模型重定向为折现主体持续性价值模型。

| 字段 | 契约内容 |
| --- | --- |
| 不变量 | 折现主体持续性价值，即主体在未来时间窗内持续存在、行动、学习、恢复和选择的综合价值 |
| 时间索引 | 离散时间 `t`，时间步长可按年、季度、月或项目周期设定；所有结论必须声明时间窗 |
| 状态向量 | `X_t=(T_t,E_t,R_t,C_t,A_t,Q_t,O_t,Risk_t)` |
| 行动向量 | `U_t=(medical,AI,wearable,knowledge_system,automation,resource_environment)` |
| 状态转移算子 | `P(X_{t+1}|X_t,U_t)` |
| 风险算子 | `lambda(t|X_t,U_t)` |
| 目标函数 | `maximize_pi E[sum_t delta^t*(E_t + alpha Q_t + beta O_t - gamma Risk_t)]` |
| 约束 | 主体连续性阈值；证据门禁；同意与权利保护；禁止输出个人死亡日期；因果主张必须声明 population、comparator、time zero、outcome、estimand |
| 非主张 | 不证明永生已经实现；不输出个体死亡日期；不把机制合理或短期功能改善升级成寿命延长结论；不把技术存在等同于主体增强 |

## Derivation Map v0.1

| 步骤 | 类型 | 内容 |
| --- | --- | --- |
| D1 | definition | 选择折现主体持续性价值作为不变量，避免把单一寿命长度误当成最终研究对象 |
| D2 | approximation | 用 `T/E/R/C/A/Q/O/Risk` 表示主体状态的第一版低维代理，而非完整人体、社会和技术系统 |
| D3 | definition | 把医学、AI、检测、知识系统、自动化和资源环境写成行动向量 `U_t` |
| D4 | method | 任何技术价值只通过状态转移 `P(X_{t+1}|X_t,U_t)` 或风险函数 `lambda(t|X_t,U_t)` 进入模型 |
| D5 | interpretation | 有效永生被解释为受证据、风险、伦理和主体连续性约束的动态策略问题 |
| D6 | boundary | 模型禁止输出个体死亡日期，禁止把探索性相关、机制合理或短期任务收益伪装成寿命结论 |

## Threats to Validity v0.1

| 威胁 | 风险 | 后果 | 缓解方式 |
| --- | --- | --- | --- |
| 证据层级混合 | Source Cards 同时包含方法标准、机制综述、观察关联、随机实验、治理框架和规范哲学 | 读者可能把方法语言、机制合理性或规范框架误读为干预效果证据 | Claim Register、Evidence Classes 和 Citation Audit 分开标注主张类型、证据用途和不可支持范围 |
| 外推边界 | AI 写作、客服、编程和咨询任务实验只覆盖限定任务族 | 局部任务收益可能被误用为通用智力、健康寿命或永生收益 | 所有 `A -> Q` 主张必须保留任务边界、QA 成本、幻觉、返工和异质性说明 |
| 变量代理偏差 | `E`、`Q`、`O` 等变量只能通过代理指标观测，且代理会受地区、制度、资源和文化影响 | 不同主体或人群之间的数值不可直接比较 | 变量字典要求记录单位、代理指标、失败模式和适用时间窗，后续模型必须做敏感性分析 |
| 因果识别不足 | 技术采用、资源可及和健康状态之间存在时间变化混杂、选择偏差和中介路径 | 相关信号可能被错误升级为干预效果 | 任何强因果主张必须先通过 `U_t -> causal claim` 门禁，写明 population、comparator、time zero、outcome 和 estimand |
| 治理反噬 | 增强技术可能引入依赖、误用、监控、剥削、隐私泄漏和尾部风险 | 飞轮可能从主体持续性增强机制变成风险放大器 | 技术族注册表要求同时记录 upside、downside、停止条件、回滚路径和事故复盘入口 |

## AI Research Failure Mode Audit v0.1

本节把 AI 辅助科研的常见失败模式显式接入 Evidence Matrix。它不证明论文已经达到投稿级别，只规定下一轮自动化科研不能越过的完整性门禁。

| ID | 失败模式 | 当前状态 | 阻塞条件 |
| --- | --- | --- | --- |
| FM1 | 实现错误通过 AI 自审 | CLEAR_FOR_CURRENT_DRAFT | 新增实验、仿真或模型曲线数值但没有运行日志、参数文件和输出证据 |
| FM2 | 幻觉引用 | WARN_NOT_FULLY_CLEARED | 正式投稿前未完成 fresh reviewer thread 的逐句引用语境审查 |
| FM3 | 幻觉实验结果 | CLEAR_FOR_CURRENT_DRAFT | 正文声称完成模型拟合、预测或实验而仓库没有对应数据与脚本 |
| FM4 | 依赖捷径特征 | WARN_MONITORED | 后续预测模型只依赖单一代理指标且不做敏感性分析 |
| FM5 | 把实现错误改写成创新点 | CLEAR_FOR_CURRENT_DRAFT | 验证失败、渲染失败或数据缺口被写成理论发现 |
| FM6 | 方法编造 | CLEAR_WITH_BOUNDARY | 把尚未执行的因果估计、仿真、实验或审稿流程写成已完成 |
| FM7 | 早期框架锁定 | WARN_MONITORED | 后续只维护当前飞轮叙事而不补反例、负向路径和替代模型 |

## Reproducibility Anchors v0.1

| 产物 | 路径 | 职责 | 检查方式 |
| --- | --- | --- | --- |
| Working paper | `docs/explanations/effective-immortality-acceleration-flywheel.md` | 论文主叙事、变量定义、模型契约和研究路线 | 人工审阅章节结构，并运行 `make check` |
| Web paper page | `web/src/pages/papers/effective-immortality-flywheel.astro` | arXiv-style 阅读页面，消费结构化数据并展示表格和 D3 图 | `npm run build`；`curl` 页面确认 v0.25、schema 2.0、Citation Context Review Packet v0.1、Citation Context Risk Triage v0.1、High-Risk Citation Context Review v0.1、Citation Context Local Review v0.1、Fresh Reviewer Citation Audit Protocol v0.1、Fresh Reviewer Citation Results Audit v0.1、Claim Context Audit v0.1、Reference Verification v0.1、Pre-Submission Review v0.1、Search Execution Register v0.1、Candidate Source Verification v0.1、Candidate Source Extraction v0.1、Estimand Registry v0.1、Analysis Plan Registry v0.1、AI Research Failure Mode Audit v0.1、AI Task Evidence Register v0.3、AI Task Method Audit、Research Declarations、Claim Evidence Map、Reference Registry 和 `U_t` 门禁 |
| Structured evidence data | `web/src/data/effective-immortality-evidence.json` | Claim Register、Claim Evidence Map、AI Task Evidence Register、Reference Registry、变量字典、模型契约、证据边、技术族、威胁和可复现锚点的单一数据源 | Node JSON smoke：schemaVersion、变量数、A -> Q 任务证据、证据等级、效应估计、证据边、主张映射、Estimand Registry、Analysis Plan Registry、AI research failure mode audit、参考文献注册表和必需字段 |
| Reference BibTeX | `web/src/data/effective-immortality-flywheel/references.bib` | 由 Reference Registry 生成的 BibTeX 风格参考文献文件 | `npm run export:references`；确认条目数等于 `referenceRegistry.length`，且 QJE DOI 为 `10.1093/qje/qjae044` |
| Citation Audit JSON | `web/src/data/effective-immortality-flywheel/CITATION_AUDIT.json` | 由 Reference Registry 生成的机器可读引用审计账本 | `npm run export:references`；Node 检查 verdict、total_entries、hashes 和 assurance limitations |
| Citation Audit Markdown | `web/src/data/effective-immortality-flywheel/CITATION_AUDIT.md` | 由 Reference Registry 生成的人类可读引用审计报告 | 确认 WARN 边界、48 条 per-entry ledger 和 assurance limitations 存在 |
| Reference Verification JSON | `web/src/data/effective-immortality-flywheel/REFERENCE_VERIFICATION.json` | 联网 primary-source 参考文献核验账本，检查 DOI/Crossref、arXiv API、官方 URL、可访问书目/作者页和本地 artifact | `npm run verify:references`；确认 verdict 为 PASS，当前 48 PASS、0 WARN、0 FAIL |
| Reference Verification Markdown | `web/src/data/effective-immortality-flywheel/REFERENCE_VERIFICATION.md` | 人类可读 primary-source 参考文献核验报告 | 确认全部 Reference Registry 条目完成机器可达性核验；该报告不替代逐句 citation context reviewer |
| Claim Context Audit JSON | `web/src/data/effective-immortality-flywheel/CLAIM_CONTEXT_AUDIT.json` | 机器可读 claim-context-reference 对齐审计，检查核心主张、引用上下文、不可支持边界和 Reference Registry 反向覆盖 | `npm run audit:claim-context`；确认 verdict 为 PASS，7 条 claim evidence rows、12 个 citation contexts、53 条 Reference Registry 和 0 gaps |
| Claim Context Audit Markdown | `web/src/data/effective-immortality-flywheel/CLAIM_CONTEXT_AUDIT.md` | 人类可读 claim-context-reference 对齐审计报告 | 确认 CL1-CL7 均有边界化 claim evidence row，所有 citation contexts 均有 supports 与 doesNotSupport，且无 reference verification FAIL |
| Citation Context Review Packet JSON | `web/src/data/effective-immortality-flywheel/CITATION_CONTEXT_REVIEW_PACKET.json` | 机器可读逐句 citation-context 外部审查输入包，连接 CL1-CL7、CTX1-CTX12、Reference Registry、supports 和 doesNotSupport 边界 | `npm run export:citation-contexts`；确认 verdict 为 READY_FOR_EXTERNAL_REVIEW，包含 7 条 claim packet、12 条 context packet、48 条 reference 和完整 reviewer instructions |
| Citation Context Review Packet Markdown | `web/src/data/effective-immortality-flywheel/CITATION_CONTEXT_REVIEW_PACKET.md` | 人类可读逐句 citation-context 外部审查输入包 | 确认每条核心主张均列出引用上下文、可支持范围、不可支持范围、引用键和 fresh reviewer 输出格式 |
| Citation Context Risk Triage JSON | `web/src/data/effective-immortality-flywheel/CITATION_CONTEXT_RISK_TRIAGE.json` | 机器可读 L3 引用语境风险分诊账本，按过度外推风险、边界敏感性、参考文献 WARN/FAIL 和主张类型生成 fresh reviewer 优先级队列 | `npm run audit:citation-risk`；确认 verdict 为 REQUIRES_FRESH_REVIEW，12 个 citation contexts 都有 risk tier、risk score、required action 和 reviewer focus |
| Citation Context Risk Triage Markdown | `web/src/data/effective-immortality-flywheel/CITATION_CONTEXT_RISK_TRIAGE.md` | 人类可读 L3 引用语境风险分诊报告 | 确认 HIGH/MEDIUM/LOW 队列列出 safe use、forbidden use 和 reviewer focus，且明确不替代 fresh reviewer 逐句来源判断 |
| High-Risk Citation Context Review JSON | `web/src/data/effective-immortality-flywheel/HIGH_RISK_CITATION_CONTEXT_REVIEW.json` | 机器可读 HIGH/BLOCKER 引用语境来源边界审查账本，先处理 fresh reviewer 队列中最高风险上下文 | `npm run audit:high-risk-citations`；确认 verdict 为 PASS_WITH_LIMITATIONS，所有 HIGH/BLOCKER contexts 均有 source finding、boundary note 和 action |
| High-Risk Citation Context Review Markdown | `web/src/data/effective-immortality-flywheel/HIGH_RISK_CITATION_CONTEXT_REVIEW.md` | 人类可读 HIGH/BLOCKER 引用语境来源边界审查报告 | 确认 CTX2 的 Grossman、WHO HALE 和 NICE QALY 均有来源角色、支持范围、不可支持范围和 fresh reviewer 后续要求 |
| Citation Context Local Review JSON | `web/src/data/effective-immortality-flywheel/CITATION_CONTEXT_LOCAL_REVIEW.json` | 机器可读全量引用语境本地来源边界审查账本，覆盖 CTX1-CTX12 的 safe use、forbidden use、reference state 和 fresh reviewer focus | `npm run audit:citation-contexts-local`；确认 verdict 为 LOCAL_REVIEW_COMPLETE_REQUIRES_FRESH_REVIEW，12 个 citation contexts 全部 reviewed，blocked contexts 为 0 |
| Citation Context Local Review Markdown | `web/src/data/effective-immortality-flywheel/CITATION_CONTEXT_LOCAL_REVIEW.md` | 人类可读全量引用语境本地来源边界审查报告 | 确认每个 CTX 均列出本地 verdict、边界行动、引用键和正式 fresh reviewer focus |
| Fresh Reviewer Citation Audit Protocol JSON | `web/src/data/effective-immortality-flywheel/FRESH_REVIEWER_CITATION_AUDIT_PROTOCOL.json` | 机器可读外部 fresh reviewer 审稿协议，按风险排序 CTX1-CTX12 并给出独立审查契约、pass gate 和逐项 prompt | `npm run export:fresh-reviewer-protocol`；确认 verdict 为 READY_FOR_FRESH_REVIEWER，队列包含 12 个 contexts，HIGH/BLOCKER 为 1 |
| Fresh Reviewer Citation Audit Protocol Markdown | `web/src/data/effective-immortality-flywheel/FRESH_REVIEWER_CITATION_AUDIT_PROTOCOL.md` | 人类可读外部 fresh reviewer 审稿协议 | 确认 reviewer independence contract、pass gate、review queue 和每个 context 的 suggested prompt 存在；它不替代 reviewer verdict |
| Fresh Reviewer Citation Results Template JSON | `web/src/data/effective-immortality-flywheel/FRESH_REVIEWER_CITATION_AUDIT_RESULTS_TEMPLATE.json` | 机器可读外部 reviewer 结果账本模板，用于生成真实 `FRESH_REVIEWER_CITATION_AUDIT_RESULTS.json` | `npm run audit:fresh-reviewer-results`；确认模板包含 12 个 contexts、source protocol hash 和 verdict schema |
| Fresh Reviewer Citation Results Template Markdown | `web/src/data/effective-immortality-flywheel/FRESH_REVIEWER_CITATION_AUDIT_RESULTS_TEMPLATE.md` | 人类可读 reviewer 结果填写说明 | 确认 allowed values、queue 和不得把模板当成 reviewer result 的边界说明存在 |
| Fresh Reviewer Citation Results Audit JSON | `web/src/data/effective-immortality-flywheel/FRESH_REVIEWER_CITATION_AUDIT_RESULTS_AUDIT.json` | 机器可读外部 reviewer 结果审计账本；无真实结果时保持 pending，存在真实结果时验证 blocking conditions | `npm run audit:fresh-reviewer-results`；当前确认 verdict 为 PENDING_EXTERNAL_REVIEW_RESULTS，required contexts 为 12，completed contexts 为 0 |
| Fresh Reviewer Citation Results Audit Markdown | `web/src/data/effective-immortality-flywheel/FRESH_REVIEWER_CITATION_AUDIT_RESULTS_AUDIT.md` | 人类可读外部 reviewer 结果审计报告 | 确认该报告明确说明当前没有真实 reviewer results，不能把 pending 写成 pass |
| Pre-Submission Review JSON | `web/src/data/effective-immortality-flywheel/PRE_SUBMISSION_REVIEW.json` | 机器可读预提交审查账本，检查版本漂移、必需边界、AI 文风词、em dash、核心审计产物和已知提交阻塞项 | `npm run audit:pre-submission`；确认无 CRITICAL，本地结构可以继续推进，fresh reviewer citation audit 仍作为 MAJOR 队列项保留 |
| Pre-Submission Review Markdown | `web/src/data/effective-immortality-flywheel/PRE_SUBMISSION_REVIEW.md` | 人类可读预提交审查报告 | 确认版本漂移为 0，文本机械扫描为 0，剩余 MAJOR 明确指向正式提交前的 fresh reviewer 引用语境审查 |
| Coverage Audit JSON | `web/src/data/effective-immortality-flywheel/COVERAGE_AUDIT.json` | 机器可读覆盖审计，检查 evidence source alias、AI task reference key、AI task full-text verification、method-audit 必填字段、research declarations、estimand registry、analysis plan registry 和 AI research failure mode audit | `npm run audit:effective-immortality`；确认 verdict 为 PASS，source aliases 为 54，AI task reference keys 为 4，AI task required fields 为 14，method-audit fields 为 7，research declarations 为 8，estimand registry rows 为 9，analysis plan rows 为 9，failure mode rows 为 7 |
| Coverage Audit Markdown | `web/src/data/effective-immortality-flywheel/COVERAGE_AUDIT.md` | 人类可读覆盖审计报告 | 确认 54 个 alias、4 个 AI task reference key、14 个 AI task 必填字段、7 个 method-audit 字段、8 个 research declarations、9 个 estimand rows、9 个 analysis plan rows、7 个 failure mode rows、47 张 Source Card、53 条 Reference Registry 无断链 |
| Evidence Matrix | `docs/source-notes/2026-06-28-effective-immortality-flywheel-evidence-matrix.md` | 可检验边、证据角色、断裂条件、模型任务和数据契约说明 | 与 JSON 字段逐项同步，禁止陈旧符号 |
| Derivation package | `docs/source-notes/2026-06-28-effective-immortality-flywheel-derivation-package.md` | 冻结不变量、假设、符号、推导图、主公式、非主张和开放风险 | 确认不变量稳定，定义、近似、方法和边界分开标注 |
| D3 evidence graph | `web/src/scripts/evidence-graph.js` | 从嵌入 JSON 生成主链、反哺路径、风险通道和因果门禁图 | 脚本查找 `U_t -> causal claim`，页面嵌入 JSON 后可渲染 |

## Evidence Classes

| 类别 | 用途 | 在本模型中的限制 |
| --- | --- | --- |
| 方法标准 | Kaplan-Meier、Cox 等用于定义生存曲线、风险函数和统计语言 | 只提供测量与估计方法，不证明具体干预有效 |
| 机制综述 | Hallmarks of Aging、cognitive reserve 等用于提出状态变量和路径假设 | 不能直接推出个体预测或可执行干预 |
| 关联证据 | 生物标志物、社会关系、认知储备等和寿命/健康结果的关系 | 需要因果审查，不能把相关性当干预效果 |
| 实验证据 | AI 写作、Copilot、客服 AI、咨询任务 AI 实验 | 任务和人群边界强，不能泛化成所有问题求解 |
| 规范框架 | Capability Approach、Extended Mind、Engelbart | 用于定义价值和边界，不承担数值预测 |
| 治理证据 | AI 风险、BCI 伦理、证据政策 | 用于限制用途和识别反向路径，不直接提供收益估计 |

## Metric Registry v0.1

这张表把每条边从“有道理”推进到“可观测”。第一轮不追求完整数据，只要求每个节点至少有一个正向指标、一个反证指标和一个测量说明。

| 链路边 | 正向指标 | 反证指标 | 测量说明 |
| --- | --- | --- | --- |
| `T -> E` | 健康寿命、无失能生存时间、可行动小时数占比 | 失能年数、认知退化、长期不可行动时间增加 | 用 HALE/QALY 作为代理语言，但保留主体性和行动能力的额外字段 |
| `E -> R` | 有反馈学习轮次、项目迭代次数、复盘记录数量 | 无反馈重复、注意力碎片化时长、目标漂移次数 | 只统计进入明确任务和反馈闭环的有效时间 |
| `R -> C` | 技能测试提升、知识资产增长、可迁移项目数量、协作网络质量 | 学习饱和、遗忘率、错误反馈导致的表现下降 | 区分短期熟练度、长期能力和跨任务迁移 |
| `C -> A` | 新技术理解时间缩短、试用转整合比例、工具迁移成功率 | 技术不可及、采用后废弃、误信错误工具 | 采用必须拆成 access、understanding、evaluation、trial、integration |
| `A -> Q` | 单位时间任务完成量、质量评分、错误率下降、反馈速度提升 | 幻觉率、QA 成本、返工率、过度依赖指标上升 | 按任务族分层，不把局部任务收益泛化为通用增强 |
| `Q -> O` | 新任务入口、资源入口、协作入口、制度入口和可逆选择增加 | 产出增加但权限、资源、关系和选择不增加 | 可能性空间只统计主体真实可进入的路径 |
| `O -> T/E` | 医疗可及性、恢复资源、社会支持、风险缓冲和技术窗口增加 | 新路径带来监控、剥削、事故暴露、压力和恢复负担 | 反哺项必须同时计算资源增益和风险暴露 |
| `A/Q -> risk` | 风险被识别、隔离、审计和回滚的比例 | 尾部风险、依赖性、误用率、治理失败事件 | 所有增强技术都必须有 downside channel |
| `U_t -> causal claim` | 明确 population、comparator、time zero、outcome、estimand | immortal time bias、选择偏差、不可测混杂、替代终点偷换 | 没有因果协议时只能保留为机制假设或探索性关联 |

## Technology Family Registry v0.1

`A -> Q` 不能被写成单一“技术提升能力”边。不同技术族作用于不同模型位置，也有不同负向通道。

| 技术/干预族 | 主要模型位置 | 正向通道 | 负向通道 | 证据入口 |
| --- | --- | --- | --- | --- |
| AI 工具 | observation / policy / action quality | 检索、写作、编程、诊断辅助、决策支持和反馈速度 | 幻觉、自动化偏差、隐私泄漏、判断退化、QA 成本 | Generative AI at Work；Noy & Zhang；Copilot；Jagged Frontier；NIST AI RMF；Human-AI Interaction Guidelines |
| 医学干预 | state transition / hazard | 疾病进展、恢复速度、健康质量、死亡风险 | 副作用、适应证错误、长期安全性不足、可及性不平等 | Hallmarks；GrimAge；target trial；ClinicalTrials.gov API；WHO ICTRP；TRIPOD+AI；PROBAST+AI；CONSORT-AI；SPIRIT-AI |
| 可穿戴与检测 | observation | 风险早筛、状态监测、反馈频率、行为提示 | 误报、焦虑、过度医疗、数据质量差 | Dynamic Digital Twin；Apple Heart Study；Stage-Based Personal Informatics |
| 知识管理与记忆外化 | cognitive state / policy | 降低遗忘和检索成本，支持复盘、学习和跨任务迁移 | 噪音积累、错误知识固化、工具锁定 | Extended Mind；Engelbart；Lived Informatics；Cognition in the Wild |
| 自动化与执行系统 | action quality / resource | 降低重复任务成本，提高执行稳定性和反馈速度 | 脆弱依赖、流程僵化、异常处理失败 | NASA-TLX；Types and Levels of Automation；Human-AI Interaction Guidelines；AI productivity |
| 资源与环境干预 | state / recovery / option value | 医疗可及、恢复、住房、照护、社会支持和风险缓冲 | 资源门槛、制度排除、监控、外部依赖 | Health Capital；Social relationships；Capability Approach；WHO SDOH；WHO Primary Health Care |

技术族注册表的用途是防止模型把“技术存在”误写成“主体增强”。每个技术族都必须分别声明模型位置、证据入口、反证指标和治理门禁。

## Findings

1. 有效时间 `E` 是从寿命叙事进入问题求解模型的关键桥梁。没有 `E`，`T` 只表示活着多久，不能表示还能做多少事。
2. 学习轮次 `R` 必须绑定反馈、自我调节和任务质量。单纯“存在更久”不会自动产生能力积累。
3. 技术采用 `A` 不是“技术存在”。模型必须拆出接触、理解、评估、试用、整合和长期使用。
4. AI 对 `Q` 的提升是任务边界内的，不是通用万能增益。Jagged frontier 是风险和收益同时存在的核心形状。
5. 可能性空间 `O` 必须用真实可进入路径定义。资源、制度、身份、健康和社会支持决定它能否反过来强化主体持续性。

## Source Traceability

- Grossman health capital: <https://www.journals.uchicago.edu/doi/10.1086/259880>
- WHO HALE metadata: <https://www.who.int/data/gho/indicator-metadata-registry/imr-details/7752>
- NICE economic evaluation and QALY reference: <https://www.nice.org.uk/process/pmg36/chapter/economic-evaluation-2>
- Target trial emulation: <https://pubmed.ncbi.nlm.nih.gov/36508210/>
- Open target trial tutorial substitute: <https://pmc.ncbi.nlm.nih.gov/articles/PMC9910387/>
- Stern cognitive reserve: <https://pubmed.ncbi.nlm.nih.gov/23079557/>
- Holt-Lunstad, Smith, Layton social relationships mortality meta-analysis: <https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1000316>
- Ericsson deliberate practice: <https://eric.ed.gov/?id=EJ471947>
- Newell and Rosenbloom law of practice: <https://www.taylorfrancis.com/chapters/edit/10.4324/9780203728178-6/mechanisms-skill-acquisition-law-practice-allen-newell-paul-rosenbloom>
- Zimmerman self-regulated learning: <https://www.tandfonline.com/doi/abs/10.1207/s15430421tip4102_2>
- Kluger and DeNisi feedback intervention theory: <https://doi.org/10.1037/0033-2909.119.2.254>
- Davis TAM: <https://misq.umn.edu/misq/article/13/3/319/191/Perceived-Usefulness-Perceived-Ease-of-Use-and>
- Venkatesh et al. UTAUT: <https://misq.umn.edu/misq/article/27/3/425/1340/User-Acceptance-of-Information-Technology-Toward-A>
- Rogers diffusion of innovations: <https://www.simonandschuster.com/books/Diffusion-of-Innovations-5th-Edition/Everett-M-Rogers/9780743222099>
- Brynjolfsson, Li, Raymond, Generative AI at Work: <https://academic.oup.com/qje/article/140/2/889/7990658>
- Noy and Zhang, generative AI productivity experiment: <https://www.science.org/doi/10.1126/science.adh2586>
- Dell'Acqua et al., Jagged Technological Frontier: <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4573321>
- Peng et al., GitHub Copilot productivity experiment: <https://arxiv.org/abs/2302.06590>
- Capability Approach, Stanford Encyclopedia of Philosophy: <https://plato.stanford.edu/entries/capability-approach/>
- NIST AI Risk Management Framework: <https://www.nist.gov/itl/ai-risk-management-framework>
- Amershi et al., Guidelines for Human-AI Interaction: <https://dl.acm.org/doi/10.1145/3290605.3300233>
- ClinicalTrials.gov trial registry: <https://clinicaltrials.gov/>
- ClinicalTrials.gov Data API: <https://clinicaltrials.gov/data-api/about-api>
- WHO International Clinical Trials Registry Platform: <https://www.who.int/tools/clinical-trials-registry-platform>
- TRIPOD+AI Statement: <https://www.tripod-statement.org/>
- PROBAST+AI risk of bias and applicability tool: <https://www.probast.org/>
- CONSORT-AI: <https://www.nature.com/articles/s41591-020-1034-x>
- SPIRIT-AI: <https://www.nature.com/articles/s41591-020-1037-7>
- Apple Heart Study / smartwatch atrial fibrillation assessment: <https://www.nejm.org/doi/full/10.1056/NEJMoa1901183>
- Li, Dey, Forlizzi personal informatics model: <https://dl.acm.org/doi/10.1145/1753326.1753409>
- Epstein et al., Lived Informatics: <https://dl.acm.org/doi/10.1145/2750858.2804250>
- Hutchins, Cognition in the Wild: <https://mitpress.mit.edu/9780262581462/cognition-in-the-wild/>
- NASA Task Load Index: <https://www.nasa.gov/human-systems-integration-division/nasa-task-load-index-tlx/>
- Parasuraman, Sheridan, Wickens automation taxonomy: <https://ieeexplore.ieee.org/document/844354>
- WHO social determinants of health: <https://www.who.int/health-topics/social-determinants-of-health>
- WHO primary health care: <https://www.who.int/health-topics/primary-health-care>

## Search Notes

- 本轮按照 `research-lit` 工作流处理：先检查本地论文缓存，再做外部来源查询，再按链路边归因。
- 本项目根目录当前没有 `papers/` 或 `literature/` 本地论文库；核心论文缓存仍在仓库外 `.research/literature/`。
- `openalex_fetch.py` 和 `semantic_scholar_fetch.py` helper 当前不在项目工具目录；本轮使用 Python `requests` 直接访问 OpenAlex API 做 DOI 级核对。
- Semantic Scholar 公共 API 在本轮查询中出现 HTTP 429，暂不把它作为主证据源。
- OpenAlex 关键词搜索存在误召回；最终证据矩阵以 DOI/arXiv ID/官方论文页为主。

## Next Queue

1. 为每个指标补数据源、采样频率、缺失处理和最小可复现实验设计。
2. 在 Web 论文页将指标注册表和技术族注册表转成可交互 evidence panel。
3. 将模型契约中的目标函数接入 D3 玩具曲线，区分固定寿命、有效时间扩展和飞轮路径。
4. 继续把六类技术族扩展到每类 3-5 张 Source Card，并补可观测代理指标和反证条件。
