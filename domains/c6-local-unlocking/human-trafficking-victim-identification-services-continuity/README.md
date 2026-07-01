# human-trafficking-victim-identification-services-continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/human-trafficking-victim-identification-services-continuity` |
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


`human-trafficking-victim-identification-services-continuity` 研究 labor trafficking、sex trafficking、force/fraud/coercion、victim identification、screening、service referral、immigration relief interface、child trafficking 和 survivor-centered response 如何影响主体自由、身份、住房、医疗、就业和长期恢复。

## Scope

- Human trafficking、forced labor、sex trafficking、commercial sexual exploitation、force/fraud/coercion、screening indicators、referral pathways 和 survivor services。
- HHS OTIP、DOJ、DHS Blue Campaign、OVC、child trafficking、labor enforcement、healthcare screening 和 immigration relief interface 的公开资料。
- 创伤知情、受害者中心、语言可达、移民身份风险、未成年人保护、隐私和报复风险。

## Continuity Logic

```text
人口贩运或强迫劳动/性剥削
-> 主体自由、身份文件、收入、住所、医疗、通信和安全被控制
-> 识别、筛查、服务转介、法律/移民接口和长期恢复成为重新获得主体性的条件
-> 识别失败或服务断裂会让剥削继续、创伤加深并阻断未来选择权
```

## Source Spine

- HHS Office on Trafficking in Persons victim identification and services materials.
- DOJ human trafficking and OVC trafficking victim services materials.
- DHS Blue Campaign awareness and indicators materials.
- Department of Labor forced labor / labor trafficking public materials where relevant.

## Evidence Boundary

本域只整理公开人口贩运识别、筛查、服务转介、权利和恢复资料。

Do not include:

- 个案识别判断、救援计划、逃离路线、执法策略、移民申请建议、卧底、追踪或调查方法。
- 可用于招募、控制、运输、剥削、规避执法、隐藏受害者或报复的信息。
- 可识别受害者、儿童、服务点、庇护所、调查人员、位置或案件信息。

## Upstream / Downstream

- Upstream: `personal-safety-violence-prevention/`, `labor-rights-workplace-protection/`, `migration-displacement-humanitarian-continuity/`, `online-safety-digital-harm-prevention/`.
- Downstream: `survivor-safe-housing-emergency-transfer-continuity/`, `victim-witness-rights-notification-continuity/`, `immigration-status-residency-work-authorization-continuity/`, `mental-health-affective-stability/`.
