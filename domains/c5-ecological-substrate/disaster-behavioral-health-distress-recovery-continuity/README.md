# Disaster Behavioral Health Distress Recovery Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/disaster-behavioral-health-distress-recovery-continuity` |
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

<!-- domain-research-skeleton:start -->
## 研究推进骨架

### 最小问题集

- 界定外部承载条件：能源、水、食物、住房、通信、交通、治理、经济或公共基础设施。
- 说明它如何改变主体展开未来所需的稳定性、冗余、可获得性和安全边界。
- 记录基础设施依赖：供应链、地理环境、制度、资金、维护能力和公共服务。
- 识别冲击场景：灾害、战争、断供、污染、气候、系统失灵或社会支持崩溃。
- 建立韧性指标：可用率、恢复时间、冗余、成本、覆盖范围、可负担性和风险暴露。

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

`disaster-behavioral-health-distress-recovery-continuity/` 研究灾害后的心理痛苦、创伤压力、哀伤、睡眠破坏、照护者负担、热线和危机咨询如何影响主体恢复。

> 核心问题：灾害恢复不是只有房屋和金钱；恐惧、失去、失眠、孤立和持续压力会吞噬判断、行动、学习和照护能力。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体持续行动依赖注意力、睡眠、情绪调节、社会连接和恢复能力
  -> 灾害造成创伤、失去、持续压力、家庭负担和社区断裂
  -> 心理健康支持决定主体能否重新组织行动和长期恢复
  -> 因此灾害行为健康是主体恢复连续性的认知情绪域
```

## 关注对象

- SAMHSA Disaster Distress Helpline、FEMA/SAMHSA Crisis Counseling Assistance and Training Program、Psychological First Aid 和地方灾害行为健康服务。
- 心理痛苦、创伤压力、哀伤、睡眠、物质使用风险、儿童家庭、照护者、热线可达、语言服务和危机转介。
- 与 `mental-health-crisis-continuity/` 的边界：该域关注一般危机；本域关注灾害恢复语境。

## Human Infra 模型链路

```text
灾害行为健康支持 T
  -> 改变痛苦识别、热线可达、危机咨询、睡眠恢复和社会支持变量 X
  -> 改变主体灾后认知情绪恢复状态 S
  -> 改变自伤、物质使用、照护崩溃、工作学习中断和长期 PTSD 风险 λ(t)
  -> 影响有效时间、判断质量、恢复能力和未来选择权
```

## 非目标

- 不提供心理诊断、治疗方案、自杀风险评估、危机干预替代、药物建议或个案咨询。
- 不收集创伤经历、精神健康史、热线记录、未成年人信息、家庭暴力或自伤细节。
- 若存在即时危险，应使用当地紧急服务或官方危机热线；本域只做研究边界和资源谱系。

## Source Signals

- SAMHSA Disaster Distress Helpline: https://www.samhsa.gov/find-help/disaster-distress-helpline
- SAMHSA DTAC: https://www.samhsa.gov/dtac
- FEMA Crisis Counseling Assistance and Training Program: https://www.fema.gov/assistance/individual/crisis-counseling
- Psychological First Aid: https://www.ptsd.va.gov/professional/treat/type/psych_firstaid_manual.asp
