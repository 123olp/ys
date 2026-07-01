# Disaster Unemployment Income Disruption Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/disaster-unemployment-income-disruption-continuity` |
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


`disaster-unemployment-income-disruption-continuity/` 研究灾害导致工作中断、自雇收入中断、工作场所关闭、交通阻断和 Disaster Unemployment Assistance 如何影响主体经济持续性。

> 核心问题：灾害后的收入断裂会迅速传导到住房、食物、医疗、交通、债务和家庭照护；收入恢复窗口决定主体能否从灾害中维持行动。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体长期行动需要现金流、工作连接和基本支付能力
  -> 灾害会切断工作场所、自雇收入、通勤、网络和照护安排
  -> 灾害失业援助和收入接续决定恢复期的资源约束
  -> 因此灾害收入中断是主体恢复连续性的资源域
```

## 关注对象

- Disaster Unemployment Assistance、常规失业保险、工资替代、工作场所关闭、临时工/自雇者、通勤中断和申请窗口。
- 收入中断时间、资格入口、证明材料、数字可达、欺诈治理、语言可达和与住房/医疗/食物援助的耦合。
- 与 `unemployment-insurance-job-loss-continuity/` 的边界：该域关注一般失业；本域关注灾害触发的工作和收入中断。

## Human Infra 模型链路

```text
灾害收入接续系统 T
  -> 改变收入替代、申请窗口、工作连接、现金流和证明材料变量 X
  -> 改变主体恢复期资源状态 S
  -> 改变住房、食物、医疗、债务、交通和照护断裂风险 λ(t)
  -> 影响有效时间、恢复能力和未来选择权
```

## 非目标

- 不提供失业资格判断、申请代办、税务建议、劳动法律建议、欺诈规避或个案收入最大化策略。
- 不收集雇主、收入、社保号、银行、工时、移民身份或家庭财务资料。
- 不替代 DOL、州失业保险机构、雇主、人力资源、工会或法律援助。

## Source Signals

- U.S. Department of Labor Disaster Unemployment Assistance: https://oui.doleta.gov/unemploy/disaster.asp
- CareerOneStop Disaster Unemployment Assistance: https://www.careeronestop.org/LocalHelp/UnemploymentBenefits/disaster-unemployment-assistance.aspx
- FEMA Individual Assistance: https://www.fema.gov/assistance/individual
