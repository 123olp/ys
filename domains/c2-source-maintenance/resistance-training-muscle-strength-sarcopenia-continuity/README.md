# Resistance Training Muscle Strength Sarcopenia Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/resistance-training-muscle-strength-sarcopenia-continuity` |
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

`resistance-training-muscle-strength-sarcopenia-continuity/` 研究抗阻训练、肌力、肌肉量、肌少症、虚弱、跌倒风险和功能独立如何进入主体持续性模型。

> 核心问题：肌肉不是审美变量，而是行动、代谢、跌倒防护、康复储备和晚年独立性的基础执行器。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体必须能移动、搬运、起立、避险、照护自己并完成现实任务
  -> 年龄相关肌力下降和肌少症会压缩行动范围、恢复能力和独立性
  -> 抗阻训练可能提高肌力、功能表现、骨骼负荷和代谢储备
  -> 因此肌力和抗阻训练是有效时间和行动密度的执行层研究域
```

## 关注对象

- resistance training、progressive overload、grip strength、sit-to-stand、gait speed、SPPB、lean mass、dynapenia、sarcopenia 和 frailty。
- 老年人、慢病人群、康复期、跌倒高风险和久坐人群中的安全、依从性、可及性与效果测量。
- 与 `physical-activity-mobility/` 的边界：身体活动域关注行动整体；本域关注力量、肌肉功能和抗阻训练。
- 与 `musculoskeletal-integrity/` 的边界：肌骨完整性域关注结构承载；本域关注训练干预和肌力功能储备。

## Human Infra 模型链路

```text
抗阻训练 T
  -> 影响肌力、肌肉量、神经肌肉控制、骨负荷、胰岛素敏感性和功能表现 X
  -> 改变行动状态 S、跌倒风险、失能风险和恢复储备
  -> 改变健康寿命、有效时间、照护依赖和未来选择权
```

## 非目标

- 不提供训练计划、重量、动作处方、康复方案、伤病处理或个体运动建议。
- 不把单一动作、网红训练、肌肉量数字或穿戴设备数据写成长期健康结论。
- 不替代医生、物理治疗师、运动专业人员或老年照护评估。
- 不鼓励高风险人群自行开始高强度训练或忽视疼痛、心血管、骨骼和跌倒风险。

## Source Signals

- HHS Physical Activity Guidelines for Americans: https://odphp.health.gov/our-work/nutrition-physical-activity/physical-activity-guidelines
- WHO physical activity and sedentary behaviour guidelines: https://www.who.int/publications/i/item/9789240015128
- CDC adult physical activity basics: https://www.cdc.gov/physical-activity-basics/guidelines/adults.html
- NIA exercise types for older adults: https://www.nia.nih.gov/health/exercise-and-physical-activity/three-types-exercise-can-improve-your-health-and-physical
- Resistance exercise and sarcopenia review: https://pmc.ncbi.nlm.nih.gov/articles/PMC4849483/

## 下一步

1. 建立肌力功能变量表：grip strength、chair stand、gait speed、SPPB、fall history、lean mass。
2. 将抗阻训练证据拆成预防、康复、老年虚弱、慢病和高风险禁忌五类。
3. 与 `fall-prevention-home-safety-continuity/`、`musculoskeletal-integrity/` 和 `rehabilitation-functioning/` 建立边界。
