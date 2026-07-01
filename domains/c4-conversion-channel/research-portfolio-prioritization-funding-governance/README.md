# Research Portfolio Prioritization Funding Governance

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/research-portfolio-prioritization-funding-governance` |
| 分级 | `C4` - 可能性转换通道层 |
| 控制轴 | 路径转换接口 |
| 分级理由 | 主要把科学、医疗、数据、制度或技术从潜在能力转成真实可用路径。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何把潜在可能性转成真实可用路径，例如研究、医疗、数据、制度、身份、资金或转化接口？

```text
研究域对象
  -> 影响变量 / 中间机制
  -> 改变主体状态或外部条件
  -> 改变风险、能力、时间成本或可达性
  -> 改变有效寿命、有效时间或未来选择权
```

### 使用边界

- 本域是研究与建模单元，不是个体医疗、法律、金融、工程、教育或安全操作建议。
- 新增内容必须标明来源、适用对象、证据等级和不确定性；AI 总结不能作为事实源。
- 若内容会改变分级、目录位置或上下游关系，先更新 `domains/_possibility-space-control/classification.tsv`。
<!-- domain-standard:end -->

<!-- domain-research-skeleton:start -->
## 研究推进骨架

### 最小问题集

- 界定转化瓶颈：研究发现、数据、临床、制度、身份、资金、可及性或操作接口。
- 说明接口机制：潜在可能性如何经过标准、流程、记录、组织或平台变成可用路径。
- 记录必要证据：登记系统、指南、监管材料、数据库、标准文档或真实世界部署资料。
- 识别摩擦指标：时间成本、资金成本、信息成本、合规成本、可及性和协作成本。
- 列出失败点：证据断裂、监管阻塞、制度排斥、隐私风险、责任不清或资源不可达。

### 变量接口

- 输入变量：本域直接处理的对象、资源、技术、环境、制度或状态。
- 中间机制：变量通过什么因果路径改变主体状态、系统状态或外部条件。
- 状态改变：身体、认知、能力、资源、风险暴露、可及性、时间成本或协作条件如何变化。
- 风险 / 成本函数：死亡风险、失能风险、工程风险、尾部风险、机会成本、维护成本或治理成本如何变化。
- 输出指标：有效寿命、健康寿命、有效时间、主观时间、相对时间、行动能力、恢复能力或未来选择权。

### 证据入口

- 官方 / 原始资料：监管文件、数据库、临床登记、标准、论文原文、项目白皮书或一手报告。
- 综述 / 指南 / 标准：系统综述、领域指南、技术标准、伦理规范和权威机构材料。
- 数据集 / 登记系统：可复核的数据表、代码、实验记录、登记号、版本和采集边界。
- 反例 / 失败案例：负结果、副作用、安全事故、不可复现结果、伦理争议和误用案例。

### 最小产出

- Source Signals：记录候选资料、来源、日期、主张和待核验点。
- Source Cards：提取 claim、变量、机制、证据类型、边界、反证条件和可迁移位置。
- Claim-Evidence Matrix：把每个稳定主张绑定到来源、证据等级、适用范围和不确定性。
- 变量表：列出输入变量、中间变量、状态变量、风险变量、输出指标和可观测代理指标。
- 上下游关系：说明本域依赖哪些更根本域，并向哪些转化、应用或基础设施域输出。
<!-- domain-research-skeleton:end -->

## 定位

本域研究研究组合、优先级设定、资金治理、价值信息分析、项目组合管理和公共/慈善/机构资助机制，如何决定 Human Infra 应该把有限注意力、时间、资金和审查能力投向哪些研究域。

Human Infra 的研究域会持续扩展，但资源不会无限。真正的瓶颈不仅是“发现更多可能”，也是“决定先研究什么、为什么、用什么证据进入下一阶段、何时停止”。本域负责把研究发散转化为可审查的组合治理。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 可能路径很多，但研究资源、注意力和验证能力有限
  -> 需要按影响、可行性、证据缺口、风险和组合多样性排序
  -> 需要研究组合优先级和资金治理机制
  -> research-portfolio-prioritization-funding-governance
```

## 关注对象

- Research portfolio、priority setting、program governance、stage-gate 和里程碑审查。
- Value of information、expected impact、evidence gap、option value、risk-adjusted learning。
- NIH/ARPA-H/DARPA 式组合管理、资助机制、项目经理模型和失败容忍。
- 公共研究、慈善资助、开放科学、专利激励和可及性之间的张力。
- Human Infra 中域晋升、Source Card 精读、模型开发、Web 展示和论文写作的资源分配规则。

## Human Infra 模型链路

```text
大量候选研究域
  -> 组合优先级和资金治理
  -> 按主体持续性影响、证据缺口、可行性、风险和学习价值排序
  -> 决定哪些域进入精读、建模、网页、论文和工具化
  -> 提高有限资源下的研究复利和纠错效率
```

## 非目标

- 不提供基金申请操控、资助游说、项目包装、关系路径或评审规避策略。
- 不把研究组合评分写成真理排序、商业估值、投资建议或机构背书。
- 不用单一指标压倒伦理、可及性、弱势群体需求和长期公共价值。
- 不替代 `technology-foresight-horizon-scanning/`；本域负责排序和资源治理，预见域负责发现候选信号。

## Source Signals

- NIH Office of Portfolio Analysis: https://dpcpsi.nih.gov/opa
- NIH RePORTER: https://reporter.nih.gov/
- WHO research priority setting: https://www.who.int/activities/setting-research-priorities
- ARPA-H: https://arpa-h.gov/
- DARPA: https://www.darpa.mil/
- PCORI research methodology resources: https://www.pcori.org/research-results/research-methodology

## 下一步

- 建立 Research Portfolio Card：domain、expected subject-continuity impact、evidence gap、tractability、risk、option value、next proof point、stop condition。
- 给 `docs/reference/research-domain-radar.md` 增加优先级字段和复核周期。
- 与 `technology-foresight-horizon-scanning/` 对接，把弱信号队列转成研究组合决策。
