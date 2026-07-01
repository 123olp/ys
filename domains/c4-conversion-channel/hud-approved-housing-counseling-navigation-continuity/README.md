# HUD Approved Housing Counseling Navigation Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/hud-approved-housing-counseling-navigation-continuity` |
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


HUD 批准住房咨询与导航连续性域研究“主体是否能在租房、买房、拖欠、止赎、灾害、反向抵押和住房选择中获得可信、非掠夺性的导航支持”。

## Human Infra 价值

住房系统高度复杂，普通主体很难独自理解租赁、购房、贷款、补贴、灾后恢复、违约、止赎和诈骗风险。可信住房咨询能降低信息成本、程序成本和错误决策成本。

```text
housing decision or crisis
  -> HUD-approved counseling / navigation
  -> better understanding, referrals, fraud avoidance
  -> housing continuity
```

## 关注对象

- HUD-approved housing counseling agencies、rental counseling、pre-purchase counseling、default counseling 和 foreclosure prevention counseling。
- disaster recovery counseling、HECM counseling、budgeting support 和 referral navigation。
- 诈骗防护、掠夺性服务识别、语言/无障碍和信任边界。
- 咨询容量、地域可达性、数字入口和结果指标。

## 不做什么

- 不提供个人购房、租房、贷款、止赎、反向抵押、预算、信用修复、债务、投资、税务或法律建议。
- 不替代 HUD-approved counselor、律师、贷款服务商、PHA、房东、法院或福利机构。
- 不推荐具体机构、贷款产品、房源、搬迁方案或个案行动。

## 证据与来源

- HUD Housing Counseling Program.
- CFPB housing and mortgage help resources.
- USA.gov housing help resources.

## 上下游关系

- 上游：`housing-built-environment-stability`、`mortgage-origination-servicing-foreclosure-continuity`、`rental-lease-tenancy-rights-continuity`。
- 下游：`eviction-prevention-court-diversion-continuity`、`emergency-rental-assistance-arrears-continuity`、`fair-housing-discrimination-reasonable-accommodation-continuity`。
