# Transit Fare Payment Toll Account Continuity

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
