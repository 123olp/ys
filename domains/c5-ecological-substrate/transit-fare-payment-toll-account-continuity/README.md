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
