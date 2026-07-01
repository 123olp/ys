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
