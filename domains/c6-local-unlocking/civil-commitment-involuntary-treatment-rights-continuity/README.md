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
