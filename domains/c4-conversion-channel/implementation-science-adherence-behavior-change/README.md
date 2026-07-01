# Implementation Science Adherence Behavior Change

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/implementation-science-adherence-behavior-change` |
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

本域研究实施科学、依从性、行为改变和服务落地如何决定技术干预是否真的进入主体生命路径。

Human Infra 的模型不能只评估“干预在论文里是否有效”，还要评估它能否被理解、获得、坚持、融入生活、被服务系统支持，并在现实约束下保持效果。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 技术效果只有进入现实行动才改变生命路径
  -> 现实中存在可及性、理解、依从性、费用、摩擦和服务碎片化
  -> 需要实施科学和行为改变框架评估 efficacy 到 effectiveness 的落差
  -> implementation-science-adherence-behavior-change
```

## 关注对象

- 实施结果：reach、adoption、implementation、maintenance、fidelity 和 sustainment。
- 依从性、坚持性、行为摩擦、认知负担、行政负担、社会支持和环境约束。
- COM-B、RE-AIM、CFIR 等实施和行为改变框架。
- 临床疗效、真实世界效果、服务可及性和长期维护之间的落差。
- 技术采用、自我升级和加速回报飞轮中的实际执行门槛。

## Human Infra 模型链路

```text
技术/干预存在
  -> 主体必须能知道、理解、获得、支付、开始和持续使用
  -> 行为、服务和环境摩擦决定真实采用概率
  -> 实施质量决定论文效果能否转化为现实状态改变
  -> 现实状态改变才进入风险函数、生存曲线和有效时间模型
```

## 非目标

- 不提供个体行为治疗、心理治疗、成瘾治疗、医疗依从性或生活方式处方。
- 不提供组织管理压榨、员工监控、操控性 nudging 或强制行为控制策略。
- 不把个体失败归咎为意志问题；必须同时审查环境、资源和系统约束。
- 不提供临床服务设计、收费、资格或报销建议。

## Source Signals

- RE-AIM framework: https://re-aim.org/
- Original RE-AIM paper: https://pubmed.ncbi.nlm.nih.gov/10499394/
- CFIR implementation framework: https://implementationscience.biomedcentral.com/articles/10.1186/1748-5908-4-50
- COM-B behaviour change model: https://implementationscience.biomedcentral.com/articles/10.1186/1748-5908-6-42

## 下一步

- 给每个干预域增加 `efficacy -> effectiveness -> implementation -> maintenance` 审查字段。
- 将 adoption、adherence、fidelity、sustainment 纳入 Human Infra 的概率门。
- 和 `time-allocation-effective-time/`、`health-literacy-navigation/`、`community-resource-navigation/` 对接，分析摩擦成本。
