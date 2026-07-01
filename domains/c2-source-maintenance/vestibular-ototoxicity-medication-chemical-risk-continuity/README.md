# Vestibular Ototoxicity Medication Chemical Risk Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/vestibular-ototoxicity-medication-chemical-risk-continuity` |
| 分级 | `C2` - 可能性源体维护层 |
| 控制轴 | 生命载体维护 |
| 分级理由 | 关键词显示该域主要维护身体、脑、器官、细胞、急性生命风险或衰老损伤控制。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何维护产生可能性的生命载体，例如身体、脑、器官、细胞、急性生命风险或衰老损伤控制？

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

- 界定生命载体变量：细胞、组织、器官、脑、免疫、代谢、急性风险或衰老损伤。
- 说明影响机制：修复、替换、再生、控制、筛查、预防、维持或风险降低。
- 列出可观察状态：功能指标、生物标志物、疾病终点、失能时间、恢复能力或死亡风险。
- 记录副作用、过度干预、癌变、免疫、长期安全性和尾部风险。
- 区分机制合理性、体外证据、动物证据、人体早期数据、临床终点和长期安全性。

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

Vestibular ototoxicity medication and chemical risk continuity studies medicines, chemicals, and exposures that can damage hearing or balance, turning treatment, work exposure, or environmental contact into long-term sensory-spatial risk.

核心问题：

> 有些技术和治疗本来为了降低风险，却可能通过耳毒性损害听觉或前庭功能；Human Infra 必须把“干预副作用如何改变主体持续性”纳入同一模型。

## 先验位置

```text
主体持续性最大化
  -> 干预和环境暴露不能只看目标收益
  -> 药物和化学暴露可能影响耳蜗或前庭系统
  -> 听觉和平衡损伤会改变沟通、空间行动、跌倒风险和有效时间
  -> 因而耳毒性是技术/治疗副作用进入主体持续性模型的感官边界
```

## 关注对象

- 耳毒性、药物相关听损/平衡风险、职业化学暴露、溶剂、重金属、噪声协同和监测。
- 治疗收益与长期听觉/前庭成本之间的模型边界。
- 与 `medicine-access-treatment-continuity/` 的关系：药品域关注可及和用药连续性；本域关注药物/化学暴露的听觉前庭副作用。
- 与 `occupational-exposure-industrial-hygiene/` 的关系：职业暴露域关注总体工业卫生；本域关注听觉和平衡终点。

## Human Infra 模型链路

```text
药物 / 化学暴露 / 噪声协同 T
  -> 改变耳蜗、前庭、听力、平衡和监测需求 X
  -> 改变沟通、空间行动、跌倒暴露、工作任务和治疗权衡状态 S
  -> 改变听损、平衡障碍、事故、孤立和有效时间损耗风险 λ(t)
  -> 影响技术收益净值、主体持续性和未来选择权
```

## 非目标

- 不提供用药建议、停药建议、暴露限值解释、个人监测计划、职业法律判断或毒理诊断。
- 不根据药名、剂量、工作环境或症状判断个人耳毒性风险。
- 不替代医生、药师、职业卫生、毒理、听力学、耳鼻喉或监管专业服务。

## Source Signals

- CDC/NIOSH ototoxic chemicals and noise resources。
- OSHA occupational noise and chemical safety context。
- NIDCD hearing and balance resources as outcome context。
