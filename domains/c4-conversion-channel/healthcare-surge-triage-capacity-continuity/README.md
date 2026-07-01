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
