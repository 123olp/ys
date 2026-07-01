# 礼品卡、预付卡与储值余额连续性

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/gift-card-prepaid-stored-value-continuity` |
| 分级 | `C6` - 局部可能性解锁层 |
| 控制轴 | 局部阻塞解除 |
| 分级理由 | 未命中更高层边界、载体、能力、转换或生态规则，暂归为具体场景的局部可能性解锁。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域解除的是哪一个具体疾病、流程、服务、职业、家庭、社区或专项风险中的局部阻塞？

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


本域研究礼品卡、预付卡、store credit、平台余额、忠诚度余额、到期、费用、余额查询和诈骗风险如何影响主体资源可用性。它关注储值余额作为弱流动性资源的连续性，而不是买卖卡密、找回个案余额或套利建议。

## 研究对象

- 礼品卡、预付卡、reloadable prepaid cards、store credit、平台钱包、忠诚度积分和账户余额。
- 到期规则、维护费用、余额查询、退款转储值、卡片丢失、停用和发行方破产/停运风险。
- 礼品卡诈骗、退款到礼品卡、预付卡错误解决、余额迁移和记录保存。
- 与退款争议、支付卡争议、诈骗消费者保护、银行账户和平台账号的边界。

## 价值链路

```text
主体把现金转为储值余额
  -> 礼品卡、预付卡和 store credit 改变资源流动性、可追踪性和恢复能力
  -> 清晰余额、低费用、可用渠道和错误解决降低沉没风险
  -> 到期、费用、诈骗、平台关闭或强制储值会削弱实际购买力
  -> 储值连续性把非现金余额纳入主体资源账本和风险治理
```

## 关键问题

- 储值余额与现金、银行账户、信用卡额度相比有哪些连续性差异？
- 礼品卡诈骗为什么会利用不可逆、难追踪和跨渠道转移特征？
- 退款转 store credit 如何改变主体资金恢复和选择权？
- 预付卡消费者保护如何影响无银行账户或低银行服务人群的资源连续性？

## 上游与下游

- 上游：`financial-inclusion-payment-systems/`、`consumer-return-refund-dispute-resolution-continuity/`、`payment-card-dispute-unauthorized-charge-continuity/`、`platform-account-suspension-appeals-continuity/`。
- 下游：`fraud-scams-consumer-protection/`、`digital-identity-security/`、`price-fee-disclosure-junk-fee-continuity/`、`administrative-burden-procedural-friction/`。

## 非目标

- 不提供礼品卡找回、卡密买卖、二级市场、套利、转卖、折扣购买、充值、提现或个案追回建议。
- 不判断某张卡是否有效、是否可退款、是否被骗、是否可转让或余额是否应恢复。
- 不协助洗钱、诈骗、卡密交易、规避平台规则、虚假退款、盗用余额或绕过身份/风控检查。

## 初始资料入口

- FTC: Gift card scams
- CFPB: Prepaid cards
- FTC and federal gift card expiration and fee consumer materials
- State consumer protection agencies official materials
