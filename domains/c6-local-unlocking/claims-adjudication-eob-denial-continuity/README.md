# Claims Adjudication EOB Denial Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/claims-adjudication-eob-denial-continuity` |
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


## 定位

本域研究医疗 claim 提交、adjudication、EOB、payer denial、coordination of benefits、resubmission、appeal window 和 denial reason 如何影响服务发生后的支付闭环。

它不是理赔申诉、账单争议、编码优化或拒付对抗工具。

## 先验问题

```text
医疗服务完成后如何不变成债务？
  -> claim 必须被正确提交和 adjudicate
  -> EOB 必须把 payer payment、adjustment 和 patient responsibility 讲清楚
  -> denial reason、resubmission 和 appeal window 必须可追踪
  -> 否则服务完成后仍会转化为账单、债务和行政负担
```

## 研究对象

- Claim submission、clearinghouse、payer adjudication、EOB、ERA/EFT 和 claim status。
- Denial reason、coordination of benefits、secondary payer、timely filing 和 appeal deadline。
- Coding mismatch、medical necessity denial、eligibility denial、network denial 和 duplicate claim。

## 关键变量

- Claim acceptance、denial rate、days in adjudication、EOB clarity。
- Appeal / resubmission rate、denial reversal、timely filing failure。
- Patient responsibility mismatch、provider-payer correction workload。

## 证据入口

- CMS claims、Medicare appeals and grievances、HIPAA transaction standards。
- X12 claim / remittance standards、CAQH CORE operating rules。
- KFF、AHRQ、Health Affairs 医疗理赔和拒付研究。

## 非目标

- 不解释个人 EOB、claim、denial、billing code、legal deadline 或 payer decision。
- 不代写 claim appeal、grievance、provider dispute、编码说明或法律信。
- 不提供 upcoding、unbundling、虚假材料、规避审核或欺诈策略。

## 上下游

- 上游：`medical-service-prior-authorization-utilization-management-continuity/`、`insurance-eligibility-benefits-verification-continuity/`。
- 下游：`patient-billing-payment-plan-continuity/`、`charity-care-financial-assistance-medical-debt-continuity/`。
