# Housing Choice Voucher Public Housing Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/housing-choice-voucher-public-housing-continuity` |
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


住房选择券、公屋与补贴住房连续性域研究“低收入住房支持是否能把名义补贴转化为真实可入住、可续租、可迁移、可检查和可保留的住房稳定”。

## Human Infra 价值

补贴住房决定许多家庭是否能把收入用于食物、医疗、教育、交通和照护，而不是被 rent burden 吞噬。Housing Choice Voucher、公屋和项目型补贴的失败模式通常不是“没有政策”，而是等待名单、可接受房源、检查、租金分担、续期、迁移和程序负担。

```text
housing subsidy
  -> eligibility, waitlist, voucher use, inspection, recertification
  -> affordable rent and stable tenancy
  -> recovery, work, school, care
```

## 关注对象

- Housing Choice Voucher、public housing、project-based voucher 和 subsidized housing。
- waitlist、briefing、voucher search time、rent reasonableness、inspection、lease-up 和 portability。
- annual recertification、income changes、family composition、reasonable accommodation 和 termination risk。
- PHA capacity、landlord participation、source-of-income barriers 和 geographic opportunity。

## 不做什么

- 不提供资格判断、申请建议、等待名单策略、PHA 选择、房源推荐、租金计算、申诉、法律或搬迁建议。
- 不提供收入隐瞒、家庭组成造假、文件伪造、规避 inspection、voucher 滥用或欺诈方法。
- 不解释任何个人补贴、租金份额、voucher、inspection 或 termination notice。

## 证据与来源

- HUD Housing Choice Voucher Program.
- HUD Public Housing and assisted housing resources.
- HUD Office of Public and Indian Housing guidance.

## 上下游关系

- 上游：`social-protection-benefits-delivery`、`income-payroll-employment-record-continuity`、`household-composition-dependent-eligibility-continuity`。
- 下游：`rental-lease-tenancy-rights-continuity`、`fair-housing-discrimination-reasonable-accommodation-continuity`、`housing-habitability-inspection-code-enforcement-continuity`。
