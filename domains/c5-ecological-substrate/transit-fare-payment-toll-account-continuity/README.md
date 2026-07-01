# Transit Fare Payment Toll Account Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/transit-fare-payment-toll-account-continuity` |
| 分级 | `C5` - 可能性生态承载层 |
| 控制轴 | 外部生态承载 |
| 分级理由 | 关键词显示该域主要承载能源、水、食物、住房、治理、经济、通信、灾害或基础设施环境。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何承载主体展开未来的外部世界条件，例如能源、水、食物、住房、通信、治理、经济和基础设施？

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

- 界定外部承载条件：能源、水、食物、住房、通信、交通、治理、经济或公共基础设施。
- 说明它如何改变主体展开未来所需的稳定性、冗余、可获得性和安全边界。
- 记录基础设施依赖：供应链、地理环境、制度、资金、维护能力和公共服务。
- 识别冲击场景：灾害、战争、断供、污染、气候、系统失灵或社会支持崩溃。
- 建立韧性指标：可用率、恢复时间、冗余、成本、覆盖范围、可负担性和风险暴露。

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

`transit-fare-payment-toll-account-continuity` 研究公交地铁票卡、移动支付、低收入票价、转乘、通勤补贴、过路费、ETC、账户恢复和罚费如何影响主体能否持续支付移动任务。

> 核心问题：交通服务存在不等于能乘坐；如果票卡、账户、手机支付、优惠资格或过路费链断裂，移动会被小额支付、罚费和账户恢复摩擦截断。

## 关注对象

- 交通卡、移动票务、现金支付、低收入票价、学生/老人/残障优惠、转乘、月票、通勤福利、过路费和 toll account。
- 账户恢复、余额迁移、退款、罚费、欠费、设备丢失、手机没电、跨机构互操作和无银行账户支付。
- 与金融包容、数字身份、公共交通、交通执法、消费者保护和行政负担的接口。

## Human Infra 链路

```text
移动支付连续
  -> 主体能稳定进入公交、轨道、收费道路和共享交通
  -> 小额支付失败、账户丢失、罚费和优惠断裂不再放大成移动排除
  -> 交通服务从物理存在转化为可支付、可恢复、可迁移能力
  -> 工作、医疗、学习和照护出行连续性增强
```

## 非目标

- 不提供逃票、绕过收费、破解票卡、规避过路费、优惠资格造假、罚费申诉策略或支付规避方法。
- 不替代交通运营商、收费机构、银行、福利机构、律师、消费者保护或本地服务渠道。
- 不收集票卡号、账户、余额、过路费账单、支付凭证、乘车记录或位置轨迹。

## Source Signals

- FTA Fare Collection and Mobility Payment resources: https://www.transit.dot.gov/
- FHWA Tolling and Pricing resources: https://ops.fhwa.dot.gov/
- CFPB Consumer Financial Protection materials: https://www.consumerfinance.gov/
- FDIC Bank On / financial inclusion materials: https://www.fdic.gov/

## 下一步

- 建立 `trip -> fare/toll medium -> eligibility/payment -> account recovery -> mobility outcome` 变量表。
- 区分现金、票卡、手机、银行账户、低收入优惠、跨机构转乘和收费道路账户。
- 与 `financial-inclusion-payment-systems`、`public-transit-service-operations-continuity`、`digital-identity-security` 和 `administrative-burden-procedural-friction` 建立边界。
