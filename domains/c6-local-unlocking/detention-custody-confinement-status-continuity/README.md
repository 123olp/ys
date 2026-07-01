# Detention Custody Confinement Status Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/detention-custody-confinement-status-continuity` |
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


本域研究逮捕、拘留、羁押、移民拘押、审前羁押、监禁、释放和监管状态如何影响主体行动自由、通信、家庭、医疗、法律救济和服务连续性。

> 核心问题：拘押不是单一健康问题，而是主体行动边界被制度重写；若状态、通知、法律入口、通信、药物、身份文件和释放转接断裂，主体持续性会在短时间内急剧恶化。

## 关注对象

- 逮捕、审前羁押、监禁、移民拘押、释放、保释/监管、通信、探视、法律联系和家属通知。
- 拘押状态与医疗、药物、心理、残障便利、语言、身份文件、财务、家庭照护、住房和工作断点。
- 释放前后与 `correctional-health-reentry-continuity/` 的接口：该域关注健康与重返服务；本域关注拘押状态本身和自由/通信/程序入口。
- 拘押系统中的透明度、标准、记录、申诉、过度羁押、弱势群体保护和数据敏感性。

## Human Infra 链路

```text
拘押 / 羁押 / 监管状态连续
  -> 主体行动自由受限时，状态、位置、联系、法律入口和照护仍可被记录与恢复
  -> 医疗、药物、家庭责任、收入、住房、身份文件和法律救济断裂风险下降
  -> 释放或状态转换时服务、记录和支持可衔接
  -> 主体在强制限制状态下仍保留最低连续性和恢复路径
```

## 非目标

- 不提供刑事案件、保释、假释、移民拘押、申诉、上诉、逃避监管、设施规避或法律建议。
- 不提供拘押设施弱点、通信规避、违禁品、逃脱、隐藏身份、对抗执法或规避筛查方法。
- 不替代律师、法院、拘押机构、监察机构、医疗人员、危机热线或家属通知系统。

## Source Signals

- ICE Detention Management: https://www.ice.gov/detain/detention-management
- Federal Bureau of Prisons: https://www.bop.gov/
- Bureau of Justice Statistics Corrections: https://bjs.ojp.gov/topics/corrections
- WHO Prisons and Health: https://www.who.int/europe/publications/i/item/9789289058674

## 下一步

- 建立拘押状态变量表：状态类型、位置通知、通信、法律入口、医疗药物、家庭责任、文件、释放转接和监督机制。
- 整理 ICE、BOP、BJS、WHO prisons、CDC correctional health 和 reentry continuity Source Cards。
- 与 `correctional-health-reentry-continuity/` 明确分工：本域关注拘押状态和制度转换，后者关注羁押健康与释放后照护。
