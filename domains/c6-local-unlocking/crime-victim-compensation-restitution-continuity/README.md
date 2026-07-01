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

<!-- domain-research-skeleton:start -->
## 研究推进骨架

### 最小问题集

- 界定局部阻塞：某一疾病、流程、服务、职业、家庭、社区或专项风险中的具体失败点。
- 说明受影响任务：它阻碍了主体完成什么行动、服务、照护、转换或恢复过程。
- 记录可测改善：等待时间、错误率、成本、可及性、完成率、伤害率或恢复速度。
- 明确升级边界：何时应转交 C2-C5 的上层生命、能力、转化或基础设施域。
- 避免把局部改良包装成根本性解决方案，必须标注适用范围和外部依赖。

### 变量接口

- 输入变量：本域直接处理的对象、资源、技术、环境、制度或状态。
- 中间机制：变量通过什么因果路径改变主体状态、系统状态或外部条件。
- 状态改变：身体、认知、能力、资源、风险暴露、可及性、时间成本或协作条件如何变化。
- 风险 / 成本函数：死亡风险、失能风险、工程风险、尾部风险、机会成本、维护成本或治理成本如何变化。
- 输出指标：有效寿命、健康寿命、有效时间、主观时间、相对时间、行动能力、恢复能力或未来选择权。

### 证据入口

- 官方 / 原始资料：监管文件、数据库、临床登记、标准、论文原文、项目白皮书或一手报告。
- 综述 / 指南 / 标准：系统综述、领域指南、技术标准、伦理规范和权威机构材料。
- 数据集 / 登记系统：可复核的数据表、代码、实验记录、登记号、版本和采集边界。
- 反例 / 失败案例：负结果、副作用、安全事故、不可复现结果、伦理争议和误用案例。

### 最小产出

- Source Signals：记录候选资料、来源、日期、主张和待核验点。
- Source Cards：提取 claim、变量、机制、证据类型、边界、反证条件和可迁移位置。
- Claim-Evidence Matrix：把每个稳定主张绑定到来源、证据等级、适用范围和不确定性。
- 变量表：列出输入变量、中间变量、状态变量、风险变量、输出指标和可观测代理指标。
- 上下游关系：说明本域依赖哪些更根本域，并向哪些转化、应用或基础设施域输出。
<!-- domain-research-skeleton:end -->

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
