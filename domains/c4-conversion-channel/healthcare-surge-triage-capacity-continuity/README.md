# Healthcare Surge Triage Capacity Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/healthcare-surge-triage-capacity-continuity` |
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

<!-- domain-research-skeleton:start -->
## 研究推进骨架

### 最小问题集

- 界定转化瓶颈：研究发现、数据、临床、制度、身份、资金、可及性或操作接口。
- 说明接口机制：潜在可能性如何经过标准、流程、记录、组织或平台变成可用路径。
- 记录必要证据：登记系统、指南、监管材料、数据库、标准文档或真实世界部署资料。
- 识别摩擦指标：时间成本、资金成本、信息成本、合规成本、可及性和协作成本。
- 列出失败点：证据断裂、监管阻塞、制度排斥、隐私风险、责任不清或资源不可达。

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

`healthcare-surge-triage-capacity-continuity/` 研究暴发期间医疗挤兑、床位、人力、分诊、危机标准、延迟照护和转运网络如何影响主体持续性。

> 核心问题：医疗系统不是无限缓冲器；暴发一旦超过容量，可修复风险会变成不可逆死亡、失能和长期功能损失。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体面对急性风险时依赖医疗系统容量
  -> 暴发会同时增加需求、减少人力、压缩床位和推迟常规照护
  -> 医疗挤兑连续性决定可修复风险是否仍能被接住
```

## 关注对象

- 医疗 surge capacity、床位、人力、PPE、分诊原则、危机标准、转运、远程分流、延迟照护和伦理治理。
- 与 `emergency-medical-services-prehospital-care/` 和 `healthcare-access-continuity/` 的关系：本域聚焦暴发导致的系统容量挤兑。

## Human Infra 模型链路

```text
医疗挤兑与容量治理
  -> 改变急诊、住院、ICU、人力、物资和转运可用性
  -> 改变急性事件、慢病、手术、产科和感染治疗被延迟或拒绝的概率
  -> 降低可修复风险转化为死亡、失能和长期损伤的概率
  -> 增强健康寿命、恢复能力和主体持续性
```

## 非目标

- 不提供临床分诊决策、治疗优先级、床位选择、转院建议、用药、急救或危机标准个案解释。
- 不提供医疗资源抢占、规避分诊、虚假病情、设施安全弱点或现场指挥建议。
- 不替代医疗机构、公共卫生部门、伦理委员会或临床专业判断。

## Source Signals

- ASPR TRACIE healthcare system preparedness: https://asprtracie.hhs.gov/
- ASPR TRACIE crisis standards of care resources: https://asprtracie.hhs.gov/technical-resources/63/crisis-standards-of-care/0
- CDC healthcare preparedness resources: https://www.cdc.gov/healthcare-preparedness/
- WHO health emergency preparedness: https://www.who.int/emergencies

## 下一步

- 建立变量表：床位、人力、PPE、转运、ICU、分诊规则、延迟照护、伦理治理、非 COVID 医疗挤出和恢复时间。
- 与 `medical-countermeasure-stockpile-distribution-continuity/`、`emergency-medical-services-prehospital-care/` 和 `patient-safety-organizational-learning/` 建立接口。
