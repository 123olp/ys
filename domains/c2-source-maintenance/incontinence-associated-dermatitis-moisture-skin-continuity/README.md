# Incontinence-Associated Dermatitis, Moisture and Skin Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/incontinence-associated-dermatitis-moisture-skin-continuity` |
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

`incontinence-associated-dermatitis-moisture-skin-continuity/` 研究尿失禁、粪失禁、潮湿暴露、摩擦、清洁用品、屏障产品和照护执行如何影响皮肤屏障、尊严、感染入口和长期照护质量。

> 核心问题：排泄失控不仅是泌尿或肠道问题，它会通过潮湿和刺激直接破坏皮肤边界与主体尊严。

## 先验位置

```text
有效永生
  -> 主体必须在排泄、清洁和皮肤保护之间保持稳定闭环
  -> 潮湿、尿液、粪便、摩擦和清洁失败会破坏屏障
  -> 屏障破坏增加疼痛、感染、压力损伤和照护羞耻负担
  -> 因此潮湿相关皮炎是排泄连续性与皮肤边界之间的接口域
```

## 关注对象

- Incontinence-associated dermatitis, moisture-associated skin damage, urine/stool exposure, cleansing, barrier products, friction and dignity。
- 与 `urogenital-continuity/` 的关系：后者关注排泄功能总框架，本域关注排泄暴露对皮肤边界的影响。

## Human Infra 模型链路

```text
潮湿暴露与皮肤保护连续性 T
  -> 改变尿/粪暴露、潮湿时间、摩擦、清洁和屏障用品可及 X
  -> 改变皮肤完整性、疼痛、感染入口和尊严状态 S
  -> 改变感染、压力损伤、照护负担和失能风险 lambda(t)
  -> 改变有效时间、照护质量和社会参与
```

## 非目标

- 不提供失禁用品选择、皮肤产品推荐、护理步骤、皮炎诊断、感染判断或个体照护建议。
- 不处理个人排泄、皮肤照片、长期照护机构或产品采购资料。

## Source Signals

- NCBI pressure injuries and skin integrity materials.
- CMS long-term-care quality and skin integrity materials.
- MedlinePlus urinary incontinence and skin care related materials.
