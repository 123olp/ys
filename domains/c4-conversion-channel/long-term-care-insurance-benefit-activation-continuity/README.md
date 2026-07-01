# 长期照护保险与福利启动连续性

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/long-term-care-insurance-benefit-activation-continuity` |
| 分级 | `C4` - 可能性转换通道层 |
| 控制轴 | 路径转换接口 |
| 分级理由 | 关键词显示该域主要处理研究、数据、模型、服务入口、身份记录、转化或治理接口。 |
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


本域研究 long-term care insurance、hybrid life/LTC、activities of daily living、cognitive impairment trigger、elimination period、benefit period、care setting、premium increase、claim 和 care plan 如何影响主体失能后的照护资金和家庭照护负担。它关注私营长期照护风险转移，而不是照护机构选择、保险购买、理赔代办或法律建议。

## 研究对象

- 长期照护保险、hybrid life/LTC、home care、assisted living、nursing home、adult day care 和 care coordination。
- ADL trigger、cognitive impairment trigger、elimination period、daily/monthly benefit、benefit period、inflation protection 和 premium increase。
- claim、assessment、plan of care、provider invoice、reimbursement / indemnity、policy lapse 和 appeals。
- 与长期照护服务、家庭照护、Medicaid HCBS、残障服务和寿险理赔的边界。

## 价值链路

```text
主体进入长期照护或认知/功能衰退状态
  -> 长期照护保险把高成本照护需求转化为保单触发和福利支付问题
  -> 清晰 ADL/认知触发、照护计划和发票记录维持居家或机构照护资金
  -> 等待期、保费上涨、失效或 claim 争议会把照护需求转嫁给家庭现金流
  -> 长期照护保险连续性把失能照护成本纳入可审查的风险转移执行层
```

## 关键问题

- 长期照护保险与健康保险、Medicare、Medicaid HCBS 和寿险如何分界？
- ADL、认知 impairment 和 elimination period 如何决定 benefit activation？
- premium increase、lapse 和 inflation protection 如何影响长期可持续性？
- care setting、provider invoice 和 plan of care 如何连接家庭照护执行？

## 上游与下游

- 上游：`caregiving-long-term-care/`、`dementia-cognitive-decline-care-continuity/`、`disability-services-independent-living/`。
- 下游：`family-caregiver-respite-work-continuity/`、`trust-estate-affairs-succession-continuity/`、`life-insurance-beneficiary-claim-continuity/`、`public-assistance-benefits-continuity/`。

## 非目标

- 不提供长期照护保险购买、保额选择、claim 填写、照护机构选择、Medicaid 规划、遗产规划、法律或税务建议。
- 不判断某人是否触发 ADL/认知条件、某照护服务是否应覆盖或某保费上涨是否合理。
- 不协助伪造照护记录、虚开发票、夸大 ADL 限制、隐瞒保单信息、保险欺诈、规避 Medicaid 规则或骗取照护福利。

## 初始资料入口

- NAIC: Long-term care insurance consumer materials
- State insurance department long-term care and complaint materials
- ACL / Medicare / Medicaid public long-term services context materials
- Official elder care and consumer protection materials
