# 消费者退货、退款与争议解决连续性

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/consumer-return-refund-dispute-resolution-continuity` |
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


本域研究退货政策、退款、换货、store credit、取消、商家争议和消费者投诉入口如何影响主体资金恢复、时间恢复和任务连续性。它关注交易失败后的资源回收机制，而不是个案退款、投诉、诉讼或法律建议。

## 研究对象

- 退货政策、退款方式、退款时限、换货、store credit、取消规则和收据要求。
- 商品不符、缺陷、服务未完成、商家拒绝处理、客服循环和投诉升级路径。
- 争议记录、订单记录、支付记录、物流记录、保修记录和消费者投诉数据。
- 与支付卡争议、合同订阅账单、产品安全召回、诈骗消费者保护和法律援助的边界。

## 价值链路

```text
交易结果与主体需求不匹配
  -> 退货、退款、换货和争议机制决定资金与时间能否恢复
  -> 清晰政策、记录留存和投诉入口降低资源沉没成本
  -> 拒绝退款、模糊规则、客服循环或强制储值会延长任务中断
  -> 退货退款连续性把失败交易从资源黑洞转化为可恢复的纠错流程
```

## 关键问题

- 退货、退款和换货规则如何改变主体现金流、替代采购和任务恢复时间？
- Store credit、礼品卡退款和原路退款之间有哪些不同的资源控制后果？
- 商家争议、支付争议和消费者投诉应如何区分为不同机制层？
- 消费者投诉数据如何作为市场失灵、暗黑模式或履约风险的信号？

## 上游与下游

- 上游：`online-retail-order-shipping-fulfillment-continuity/`、`contract-subscription-billing-consent-continuity/`、`product-safety-recall-systems/`、`information-integrity-trust/`。
- 下游：`payment-card-dispute-unauthorized-charge-continuity/`、`gift-card-prepaid-stored-value-continuity/`、`fraud-scams-consumer-protection/`、`access-to-justice-legal-aid/`。

## 非目标

- 不提供个案退货、退款、投诉、仲裁、诉讼、chargeback、谈判、客服话术或法律建议。
- 不判断某个消费者是否应获得退款、商家是否必须退款、政策是否有效或争议胜率。
- 不协助滥用退货、虚构未收到货、伪造证据、重复索赔、退款套利或操控投诉系统。

## 初始资料入口

- FTC: Consumer advice on refunds, returns and billing problems
- USA.gov: Consumer complaints
- CFPB: Consumer complaints and payment dispute materials
- State consumer protection agencies and attorneys general official materials
