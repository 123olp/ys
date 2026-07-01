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
