# 信用卡循环信用、成本与还款连续性

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/credit-card-revolving-credit-cost-continuity` |
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


本域研究信用卡账户、信用额度、APR、费用、宽限期、最低还款、循环余额、逾期和账户关闭如何影响主体现金流、信用入口和未来选择权。它关注短期资源桥接的跨期成本治理，而不是信用卡推荐、还款方案、逃债、套现或金融法律建议。

## 研究对象

- 信用卡账户、信用额度、APR、年费、滞纳金、预借现金费用、余额转移费用和罚息 APR。
- 账单周期、宽限期、最低还款、付款分配、循环余额、逾期、账户关闭和信用报告影响。
- 费用披露、持卡人协议、账单记录、还款记录、自动付款和账单错误入口。
- 与支付卡争议、银行账户访问、信用报告、债务催收和消费者贷款的边界。

## 价值链路

```text
主体使用信用卡平滑短期现金流
  -> 信用额度、APR、费用和最低还款把当前购买转成未来偿付义务
  -> 透明成本、可管理还款和账单记录降低短期流动性冲击
  -> 高利息、滞纳、费用叠加或账户关闭会压缩未来现金流和信用入口
  -> 信用卡连续性把短期资源桥接纳入可审查的跨期成本治理
```

## 关键问题

- 循环余额、最低还款和 APR 如何改变主体未来现金流占用？
- 费用披露、账单周期和宽限期如何影响真实成本理解？
- 逾期、罚息、账户关闭和信用报告如何连接债务连续性？
- 信用卡争议、未授权扣款和普通循环信用成本应如何区分？

## 上游与下游

- 上游：`banking-deposit-account-access-continuity/`、`financial-inclusion-payment-systems/`、`credit-consumer-reporting-access-continuity/`。
- 下游：`debt-obligation-collection-relief-continuity/`、`payment-card-dispute-unauthorized-charge-continuity/`、`consumer-loan-origination-apr-disclosure-continuity/`、`price-fee-disclosure-junk-fee-continuity/`。

## 非目标

- 不提供信用卡推荐、额度申请、还款排序、债务整合、余额转移、套现、积分套利或金融规划建议。
- 不判断某个账户是否应开卡、关卡、延期、拒付、协商、诉讼或破产。
- 不协助虚假申请、收入造假、逃债、套现、欺诈交易、洗钱、规避 KYC、规避信用报告或规避催收。

## 初始资料入口

- CFPB: Credit cards consumer tools
- CFPB: Credit card agreements and billing-error materials
- Federal Reserve consumer credit and credit-card disclosure materials
- FTC consumer finance and unauthorized charge materials
