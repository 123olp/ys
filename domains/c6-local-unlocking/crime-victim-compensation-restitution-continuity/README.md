# crime-victim-compensation-restitution-continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/crime-victim-compensation-restitution-continuity` |
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


`crime-victim-compensation-restitution-continuity` 研究犯罪伤害后的 victim compensation、restitution、emergency assistance、medical/mental health cost coverage、funeral costs、lost wages、property limits、eligibility records 和 appeal 如何影响主体经济恢复、治疗连续性和重新开始能力。

## Scope

- Crime victim compensation、VOCA、state compensation programs、restitution、emergency assistance、medical expenses、mental health counseling、lost wages 和 funeral support。
- 资格、申请窗口、文档负担、合作要求、报销限制、上诉、语言可达、残障可达和隐私。
- 与保险、医疗账单、工伤、家庭暴力、性暴力、人身伤害和死亡后遗属连续性的交叉。

## Continuity Logic

```text
犯罪伤害造成医疗、心理、收入、财产或丧葬成本
-> 主体恢复依赖可支付治疗、临时现金和损失补偿
-> victim compensation 与 restitution 把伤害后成本接入公共/司法恢复机制
-> 资格、证明或支付失败会把伤害转化为债务、治疗中断和长期贫困风险
```

## Source Spine

- OVC victim compensation and compensation program materials.
- VOCA and Crime Victims Fund public materials.
- State victim compensation program public materials.
- DOJ and court restitution public information.

## Evidence Boundary

本域只整理公开犯罪受害者补偿、restitution、资格、成本类别和制度边界资料。

Do not include:

- 个案申请建议、赔偿金额估计、资格判断、上诉策略、医疗账单谈判、诉讼策略或税务建议。
- 伪造犯罪、虚构损失、重复索赔、夸大伤害、伪造医疗/收入/丧葬文件或保险欺诈。
- 个案身份、案件编号、医疗记录、财务记录、未成年人资料或具体补偿申请材料。

## Upstream / Downstream

- Upstream: `victim-witness-rights-notification-continuity/`, `sexual-assault-forensic-exam-advocacy-continuity/`, `domestic-violence-coercive-control-safety-continuity/`.
- Downstream: `medical-payment-billing-cost-protection` family domains, `debt-obligation-collection-relief-continuity/`, `funeral-cremation-burial-disposition-continuity/`.
