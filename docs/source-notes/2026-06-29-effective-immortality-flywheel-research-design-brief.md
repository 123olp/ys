# 有效永生飞轮 Research Design Brief v0.1

Status: ARS deep-research Phase 1 scoping  
Date: 2026-06-29  
Target paper: [Effective Immortality Acceleration Flywheel](../explanations/effective-immortality-acceleration-flywheel.md)  
Web mirror: [`web/src/data/effective-immortality-evidence.json`](../../web/src/data/effective-immortality-evidence.json)

## Purpose

本文件把“有效永生带来的主体持续性加速回报飞轮”从宏大叙事压成可执行研究设计。它不新增实证结论，只冻结下一轮科研的入口：研究问题、范围、方法、有效性标准、路线图和检索种子。

## Primary Research Question

在明确证据和治理约束下，主体持续时间的延展是否会通过有效时间、学习轮次、积累资本、技术采用、行动质量和可能性空间形成可观测的正反馈？

## FINER Assessment

| Criterion | Score | Justification |
| --- | --- | --- |
| Feasible | 4/5 | 可以先用二级数据、任务实验、公开队列、系统日志和仿真模型研究局部边；完整飞轮仍需长期纵向数据。 |
| Interesting | 5/5 | 它把长寿、AI 增强、学习积累、社会支持和风险治理放进同一主体持续性问题。 |
| Novel | 4/5 | 各分支已有成熟谱系，但以 `T/E/R/C/A/Q/O` 反馈链连接有效永生与加速回报仍是项目级综合模型。 |
| Ethical | 4/5 | 当前只做概念、证据矩阵和群体级模型设计；硬约束是不输出个体死亡日期、不替代医学判断、不把增强技术去风险化。 |
| Relevant | 5/5 | 直接决定 Human Infra 的目标、对象、预测模型、Web 传播和后续研究优先级。 |

## Scope

In scope:

- `T/E/R/C/A/Q/O` 变量定义与可测量代理；
- 链路边的证据等级、反证条件和因果协议；
- AI、医学、可穿戴、知识管理、自动化和资源环境技术族；
- 群体级、任务级或场景级路径位移模型；
- 治理边界、风险扣减、停止条件和回滚条件。

Out of scope:

- 证明永生已经实现；
- 输出个人死亡日期或个体寿命承诺；
- 把短期 AI 任务收益外推为健康寿命收益；
- 把数字副本、记忆保存或工具外化自动视为同一主体延续；
- 提供医学、投资、法律或政策处方。

## Methodology Blueprint

研究范式采用 pragmatist mixed-methods。原因是研究对象横跨生存分析、学习科学、技术采用、人机协作、公共健康和规范治理；单一范式不足以覆盖变量定义、因果识别、仿真和传播边界。

当前方法是：

```text
框架建模
  -> 系统性文献映射
  -> target-trial style 因果协议
  -> 竞争模型比较
  -> 任务级实验证据整合
  -> 可复现 Web 论文表达
```

核心有效性标准：

| Criterion | Strategy |
| --- | --- |
| Construct validity | 变量字典必须给出单位、代理指标、失败模式和模型用途，防止概念滑移。 |
| Internal validity | 强因果主张必须通过 target-trial style 协议，并显式处理混杂、time zero、删失和比较组。 |
| External validity | 按任务族、人群、资源条件、制度环境和技术可及性分层，不从局部任务收益直接外推。 |
| Citation validity | Reference Registry、Citation Context Register、Local Review、Fresh Reviewer Handoff 和结果 schema 共同约束引用语境。 |
| Governance validity | 每个技术族同时记录 downside channel、停止条件、回滚路径和事故复盘入口。 |

## Execution Roadmap

| Stage | Purpose | Deliverable | Status |
| --- | --- | --- | --- |
| P1 Scoping | 冻结研究问题、变量边界、非主张边界和最小方法蓝图。 | Research Question Brief；Methodology Blueprint；Model Contract | current |
| P2 Literature Mapping | 按 `T/E/R/C/A/Q/O` 和 `A/Q -> risk` 补齐来源卡片与引用语境。 | Source Cards；Reference Registry；Citation Context Register | active |
| P3 Evidence Synthesis | 识别每条链路边的证据强度、冲突、空白和反证条件。 | Evidence Matrix；Claim Evidence Map；Threats to Validity | active |
| P4 Quantitative Contract | 把变量、边和技术族写成 estimand、analysis plan 和 model comparison contract。 | Estimand Registry；Analysis Plan Registry；CM1-CM7 Model Comparison Protocol | active |
| P5 External Audit | 让独立 reviewer 逐条核查引用语境、主张边界和来源使用。 | Fresh Reviewer CTX results；assembled results ledger | pending_external |
| P6 Visualization | 把证据矩阵、模型比较和路径位移做成可审查 Web 图表。 | D3 evidence graph；toy curve；model result panels | next |

## Search Strategy Seeds

下一轮深度科研从五组检索种子开始：

| Branch | Query | Purpose |
| --- | --- | --- |
| Survival and healthspan modeling | `(survival analysis OR restricted mean survival time OR multistate model) AND (healthspan OR healthy life expectancy OR disability-free survival)` | 补 `T -> E` 的统计底座和健康质量调整时间表达。 |
| Learning rounds and capability accumulation | `(deliberate practice OR self-regulated learning OR feedback intervention OR learning curve) AND (skill acquisition OR expertise OR longitudinal performance)` | 补 `E -> R` 与 `R -> C` 的轮次、反馈、学习曲线和衰减项。 |
| Technology adoption and human-AI productivity | `(technology acceptance OR UTAUT OR diffusion of innovations OR generative AI productivity OR human-AI collaboration) AND (experiment OR field study OR randomized)` | 补 `C -> A` 与 `A -> Q` 的采用、任务收益、异质性和 QA 成本。 |
| Option space and social determinants | `(capability approach OR social determinants of health OR social capital OR healthcare access) AND (mortality OR healthspan OR agency OR opportunity)` | 补 `Q -> O` 与 `O -> T/E` 的真实可进入路径、资源入口和社会支持。 |
| Risk governance and failure modes | `(AI risk management OR automation bias OR brain-computer interface ethics OR clinical AI reporting) AND (governance OR safety OR adverse events OR human oversight)` | 补 `A/Q -> risk` 和治理门禁。 |

## Current Interpretation

这一步把项目从“发散理论”推进到“可执行科研入口”。下一步最重要的不是继续扩写口号，而是按检索种子补空白边、用真实来源卡片更新 Reference Registry，并保持 fresh reviewer citation audit 的 pending 状态，直到外部逐项结果回填。
