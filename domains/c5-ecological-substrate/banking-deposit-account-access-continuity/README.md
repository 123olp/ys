# 银行账户、存款保险与账户访问连续性

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/banking-deposit-account-access-continuity` |
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


本域研究银行账户、存款保险、账户访问、支付入口和账户恢复如何支撑主体对日常资源的持续控制。它关注的是主体能否稳定保存、接收、支付和转移资源，而不是个人开户、理财、贷款或银行操作建议。

## 研究对象

- 银行账户、信用社账户、储蓄账户、支票账户和账户访问凭据。
- 存款保险、机构倒闭处置、账户冻结、错误交易、争议和恢复入口。
- 直接存款、电子支付、账单支付、自动扣款和身份验证断点。
- 银行服务可及性与数字身份、地址、收入、福利、税务和照护代理的依赖关系。

## 价值链路

```text
主体需要持续控制可用资金
  -> 银行和信用社账户把收入、福利、储蓄和支付连接到日常生活
  -> 存款保险、账户恢复、错误纠正和争议机制降低账户失效风险
  -> 账户冻结、凭据丢失、机构倒闭、身份错配或数字排除会截断资源流
  -> 银行账户连续性把金融资源从名义资产转化为可调用的行动能力
```

## 关键问题

- 账户访问失败会如何影响住房、食物、医疗、交通、通信和照护支付？
- 存款保险、机构处置和账户迁移如何降低金融机构失效对主体的冲击？
- 数字身份、地址、姓名、死亡/失能记录和代理权限如何影响账户连续性？
- 账户争议、错误交易、欺诈恢复和投诉系统如何把资金损失转化为可修复问题？

## 上游与下游

- 上游：`digital-identity-security/`、`name-change-identity-record-synchronization-continuity/`、`address-residency-mail-service-continuity/`、`income-payroll-employment-record-continuity/`。
- 下游：`financial-inclusion-payment-systems/`、`social-protection-benefits-delivery/`、`financial-fiduciary-power-of-attorney-continuity/`、`fraud-scams-consumer-protection/`、`contract-subscription-billing-consent-continuity/`。

## 非目标

- 不提供开户、换银行、存款分散、理财、投资、借贷、信用卡、税务、债务、保险或个体金融建议。
- 不判断个人账户冻结、争议、欺诈、机构倒闭赔付、投诉或法律责任。
- 不协助规避 KYC、反洗钱、制裁、税务、债务、法院命令或账户风控。

## 初始资料入口

- FDIC: Deposit Insurance
- FDIC: BankFind Suite and consumer resources
- NCUA: Share Insurance
- CFPB: Bank accounts and payment complaints
- Federal Reserve: Payment systems materials
