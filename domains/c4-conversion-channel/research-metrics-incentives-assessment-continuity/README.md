# Research Metrics Incentives Assessment Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/research-metrics-incentives-assessment-continuity` |
| 分级 | `C4` - 可能性转换通道层 |
| 控制轴 | 路径转换接口 |
| 分级理由 | 关键词显示该域主要处理研究、数据、模型、服务入口、身份记录、转化或治理接口。 |
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


`research-metrics-incentives-assessment-continuity/` 研究科研评价指标、激励结构、影响因子、H-index、Altmetrics、评价改革和 Goodhart 风险如何影响 Human Infra 证据生态。

> 核心问题：证据生产不是中性的；如果指标奖励论文数量、影响因子和可见度，研究系统会改变行为，进而改变模型可获得证据的质量。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要长期稳定的高质量研究供给
  -> 研究者、机构、期刊和资助方会响应评价指标与激励
  -> 错误指标会推动 salami slicing、夸大结论、刷引用和短期化选题
  -> 因此科研指标与激励评估是证据生态质量的上游制度域
```

## 关注对象

- Impact factor、H-index、citation count、Altmetrics、journal ranking、grant incentives、promotion criteria 和 responsible metrics。
- DORA、Leiden Manifesto、Metric Tide、CoARA、narrative CV 和开放科学激励。
- 与 `research-portfolio-prioritization-funding-governance/` 的边界：组合治理域关注资金和研究选择；本域关注评价指标和激励如何扭曲证据生产。
- 与 `citation-network-claim-propagation-continuity/` 的边界：引用传播域关注主张网络；本域关注指标化评价。

## Human Infra 模型链路

```text
科研指标与激励 T
  -> 改变 publication_pressure、citation_incentive、novelty_bias、open_science_incentive 变量 X
  -> 改变研究供给、报告质量、可复现性和证据生态状态 S
  -> 改变伪创新、不可复现、夸大结论和资源错配风险 λ(t)
  -> 影响 Human Infra 的研究组合、证据质量和长期技术窗口判断
```

## 非目标

- 不提供刷指标、刷引用、Altmetrics 操控、期刊排名套利、基金包装或学术履历优化服务。
- 不把单一指标用于评价个人、机构或论文质量。
- 不提供招聘、晋升、基金评审或机构排名建议。

## Source Signals

- DORA: https://sfdora.org/
- Leiden Manifesto: https://www.leidenmanifesto.org/
- CoARA Agreement: https://coara.eu/agreement/the-agreement-full-text/
- The Metric Tide: https://responsiblemetrics.org/the-metric-tide/
- National Academies, Next Generation Researchers Initiative: https://nap.nationalacademies.org/

## 下一步

- 给研究域 Source Card 增加 `metric_pressure`、`responsible_metrics_signal`、`novelty_incentive` 和 `open_science_incentive` 字段。
- 在研究组合治理中标记“高指标压力但低可复核性”的证据生态风险。
