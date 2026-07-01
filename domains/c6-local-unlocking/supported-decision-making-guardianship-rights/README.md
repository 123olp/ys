# Supported Decision Making Guardianship Rights

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/supported-decision-making-guardianship-rights` |
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

Supported Decision Making Guardianship Rights 关注支持性决策、监护、保护性安排、能力评估和权利限制如何影响主体在认知、精神、发育、老年或残障状态下继续表达意愿、控制生活和参与制度。

## 对象

- Supported decision-making、guardianship、conservatorship、substituted decision-making 和 least restrictive alternative。
- 认知障碍、精神健康、发育障碍、老年衰弱、残障和复杂照护状态下的决策支持。
- 法院、社会服务、家庭、照护者、医疗机构和金融机构之间的权力边界。

## Human Infra 价值

```text
主体持续性需要决策能力被支持而不是直接剥夺
-> 疾病、残障或认知下降会让主体完成复杂任务更困难
-> 若制度只提供替代决策，主体容易被失权、隔离或被他人控制
-> 支持性决策把帮助理解、沟通、比较和执行选择作为优先路径
-> 只有在必要且有监督时才进入限制性监护安排
-> 主体的自主性、权利和未来选择权更可能被保留
```

## 边界

- 本域不提供监护申请、诉讼、能力判断、法院策略、家庭纠纷、财务控制或机构选择建议。
- 不判断某个人是否需要监护、是否有能力或谁应成为监护人。
- 不替代律师、法院、保护服务、医疗评估、社会工作或残障权利机构。
- 只整理权利框架、支持模型、滥用风险、监督机制和研究资料。

## 上游与下游

- 上游：`disability-services-independent-living/`、`dementia-cognitive-decline-care-continuity/`、`mental-health-affective-stability/`、`legal-identity-civil-registration/`。
- 下游：`elder-justice-adult-protective-services/`、`access-to-justice-legal-aid/`、`financial-fiduciary-power-of-attorney-continuity/`、`governance-rights/`。

## 初始资料线索

- Administration for Community Living supported decision-making resources.
- National Council on Disability and disability rights materials on guardianship alternatives.
- ABA Commission on Law and Aging resources on guardianship and decision support.
