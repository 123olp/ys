# Civil Commitment Involuntary Treatment Rights Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/civil-commitment-involuntary-treatment-rights-continuity` |
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


本域研究精神健康危机、非自愿评估、民事收治、强制治疗、能力限制和权利保护如何影响主体自主性、医疗连续性、法律入口和恢复路径。

> 核心问题：危机状态下的保护措施可能防止即时伤害，也可能造成权利、记忆、关系、工作、居住和信任断裂；Human Infra 需要把安全、最小限制、正当程序和恢复连续性放进同一框架。

## 关注对象

- 非自愿评估、民事收治、强制治疗、危机响应、最小限制替代、同意能力、复查和申诉。
- 危机状态与医疗记录、药物、工作/学校、住房、家庭、财务、监护、隐私和污名的接口。
- 与 `mental-health-affective-stability/`、`suicide-crisis-response-continuity/`、`supported-decision-making-guardianship-rights/` 和 `access-to-justice-legal-aid/` 的边界。
- 机构化风险、过度强制、残障权利、语言可达、创伤知情照护和出院后恢复路径。

## Human Infra 链路

```text
非自愿治疗与民事收治权利连续
  -> 急性风险被处理时，主体的权利、同意、最小限制和复查路径仍被保护
  -> 医疗、住房、工作、家庭、财务和社会信任断裂风险下降
  -> 出院后照护、支持性决策和社区恢复可以衔接
  -> 危机干预不把主体推出长期自主性和未来选择权
```

## 非目标

- 不提供个人危机判断、收治标准、强制治疗、出院、法律申诉、医疗、用药或安全计划建议。
- 不指导如何规避危机服务、躲避评估、控制他人、强迫治疗、监控定位或制造证据。
- 若存在即时伤害风险，应联系当地紧急服务、危机热线、医疗机构或专业人员。

## Source Signals

- SAMHSA Crisis Services: https://www.samhsa.gov/find-help
- HHS Office for Civil Rights Civil Rights: https://www.hhs.gov/civil-rights/index.html
- DOJ Civil Rights Division Disability Rights: https://www.justice.gov/crt/disability-rights-section
- WHO Guidance on Community Mental Health Services: https://www.who.int/publications/i/item/9789240025707

## 下一步

- 建立非自愿治疗连续性变量表：触发条件、复查、最小限制、同意能力、语言、残障权利、出院计划和社区支持。
- 整理 SAMHSA、HHS OCR、DOJ Civil Rights、WHO community mental health 和 disability rights Source Cards。
- 与 `suicide-crisis-response-continuity/` 明确分工：危机响应域关注即时求助网络，本域关注强制性制度入口和权利连续性。
