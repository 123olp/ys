# 在线零售订单、发货与履约连续性

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/online-retail-order-shipping-fulfillment-continuity` |
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


本域研究在线、电话、邮购和平台零售中的订单确认、发货承诺、交付延迟、未交付、取消和履约纠错如何影响主体时间、金钱和任务连续性。它关注的是购买意图如何转化为可用物品或服务，而不是购物推荐、商家选择、退款策略或个案消费建议。

## 研究对象

- 在线、电话、邮购、平台订单、订单确认、库存承诺、发货时间、交付窗口和延迟通知。
- 未交付、部分交付、替代交付、订单取消、商家履约失败和平台责任边界。
- 订单记录、收据、物流记录、通知渠道、客服入口和投诉转介路径。
- 与 `postal-parcel-delivery-pickup-continuity/`、`contract-subscription-billing-consent-continuity/`、`payment-card-dispute-unauthorized-charge-continuity/`、`fraud-scams-consumer-protection/` 的边界。

## 价值链路

```text
主体形成购买意图
  -> 订单、付款、发货和交付承诺把金钱转成可用物品
  -> 履约透明、延迟通知和取消退款机制降低等待成本
  -> 未交付、虚假发货、库存错配或平台推诿会锁住资金和任务进度
  -> 订单履约连续性把交易从不确定等待转化为可追踪、可纠错的资源转换过程
```

## 关键问题

- 订单确认、发货承诺和交付窗口如何影响主体任务计划？
- 延迟、未交付或部分交付如何造成时间、资金和替代采购成本？
- 平台、商家、物流和支付记录如何共同构成履约证据链？
- 哪些履约失败应进入消费者投诉、支付争议、邮政包裹或诈骗识别域？

## 上游与下游

- 上游：`financial-inclusion-payment-systems/`、`contract-subscription-billing-consent-continuity/`、`postal-parcel-delivery-pickup-continuity/`、`information-integrity-trust/`。
- 下游：`consumer-return-refund-dispute-resolution-continuity/`、`payment-card-dispute-unauthorized-charge-continuity/`、`fraud-scams-consumer-protection/`、`household-appliance-maintenance-repair-continuity/`。

## 非目标

- 不提供购物推荐、平台选择、价格比较、抢购、套利、商家谈判、投诉脚本、个案退款或法律建议。
- 不判断某笔订单是否应退款、商家是否违法、平台是否担责或消费者应采取何种争议路径。
- 不协助虚假下单、刷单、套券、滥用退款、绕过风控、规避条款或操控平台履约系统。

## 初始资料入口

- FTC: Mail, Internet, or Telephone Order Merchandise Rule
- FTC: Consumer advice on billed items not received and unordered merchandise
- USA.gov: Consumer complaints
- State attorneys general and consumer protection agencies official materials
