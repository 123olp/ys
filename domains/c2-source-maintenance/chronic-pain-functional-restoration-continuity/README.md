# Chronic Pain Functional Restoration Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/chronic-pain-functional-restoration-continuity` |
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

`chronic-pain-functional-restoration-continuity/` 研究慢性疼痛、功能恢复、疼痛干预可及、用药风险、工作参与和生活质量如何影响主体持续性。

> 核心问题：慢性疼痛不是单纯感觉变量，而是会长期压缩注意力、睡眠、行动半径、情绪稳定、劳动能力和社会参与的有效时间损耗系统。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要可持续行动、恢复、学习和参与
  -> 慢性疼痛会持续占用注意力并降低行动质量
  -> 结果取决于功能恢复、疼痛管理、心理社会支持、用药风险控制和工作适配
  -> 因此慢性疼痛是有效时间密度和主体行动能力的关键维护域
```

## 关注对象

- Chronic pain、functional restoration、multimodal pain care、opioid risk、sleep disruption、work participation、activity pacing、psychological burden。
- 与 `pain-suffering-control/` 的边界：该域关注痛苦控制总问题；本域关注慢性疼痛作为长期功能恢复和有效时间损耗系统。
- 与 `occupational-work-design/` 和 `workplace-accommodation-return-to-work-continuity/` 的关系：疼痛负担会改变工作任务设计、返岗和长期劳动参与。

## Human Infra 模型链路

```text
慢性疼痛功能恢复系统 T
  -> 改变疼痛强度、睡眠、活动耐受、用药暴露、情绪负荷和工作适配变量 X
  -> 改变行动半径、注意力、任务持续时间、恢复能力和社会参与状态 S
  -> 改变有效时间损耗、失能风险、物质风险、精神健康风险和收入连续性 λ(t)
  -> 影响主体长期行动质量、创造密度和未来选择权
```

## 非目标

- 不提供个人疼痛诊断、用药、阿片类药物、康复动作、神经阻滞、手术、补充剂、设备或疼痛评分建议。
- 不生成个人治疗计划、用药调整、戒断方案、工伤/残障/保险判断或远程医疗建议。
- 不收集个案疼痛、用药、影像、精神健康、工作能力或保险资料。

## Source Signals

- CDC chronic pain information: https://www.cdc.gov/chronic-pain/
- CDC opioid prescribing guideline: https://www.cdc.gov/mmwr/volumes/71/rr/rr7103a1.htm
- NIH pain research: https://www.nih.gov/research-training/pain-research

## 下一步

- 建立 Chronic Pain Function Card：duration, interference, sleep, medication exposure, work participation, functional restoration access。
- 与 `pain-suffering-control/`、`physical-activity-mobility/` 和 `workplace-accommodation-return-to-work-continuity/` 建立接口。
