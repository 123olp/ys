# Bilateral Vestibular Hypofunction Gaze Gait Stability Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/bilateral-vestibular-hypofunction-gaze-gait-stability-continuity` |
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

Bilateral vestibular hypofunction gaze and gait stability continuity studies chronic loss of vestibular function on both sides as a failure of stable vision during movement, gait confidence, night walking, and spatial navigation.

核心问题：

> 主体移动时不仅要腿能走，还要眼睛能在头部运动中稳定看见世界；双侧前庭功能下降会让走路、转头、夜间移动和复杂地面变成高负荷任务。

## 先验位置

```text
主体持续性最大化
  -> 主体必须能在头动和行走中保持视觉稳定
  -> 双侧前庭输入不足削弱凝视稳定、步态反馈和空间安全感
  -> 夜间、崎岖地面和复杂环境中的移动风险上升
  -> 因而双侧前庭功能下降是移动中的视觉-步态稳定基础设施失效
```

## 关注对象

- 双侧前庭功能下降、凝视稳定、振动幻视、步态不稳、夜间行走和复杂地面。
- 行动半径、户外移动、楼梯、交通换乘、跌倒暴露和辅助补偿。
- 与 `low-vision-rehabilitation-assistive-technology-continuity/` 的关系：低视力域关注视觉输入补偿；本域关注头动时视觉稳定。
- 与 `peripheral-neuropathy-somatosensory-continuity/` 的关系：周围神经域关注本体/触觉反馈；本域关注前庭反馈。

## Human Infra 模型链路

```text
前庭评估 / 康复 / 辅助补偿 / 环境适配 T
  -> 改变凝视稳定、步态信心、夜间移动和复杂地面耐受 X
  -> 改变行动半径、外出频率、跌倒暴露和任务参与状态 S
  -> 改变跌倒、隔离、依赖和有效时间损耗风险 λ(t)
  -> 影响独立生活、移动自由和未来选择权
```

## 非目标

- 不提供前庭测试解释、诊断、康复训练、助行器建议、用药建议或个人跌倒风险判断。
- 不根据个人步态或眩晕描述判断病因、外出许可或驾驶许可。
- 不替代耳鼻喉、神经、前庭康复、物理治疗或老年医学服务。

## Source Signals

- Vestibular rehabilitation clinical practice guideline for peripheral vestibular hypofunction。
- NIDCD balance disorders resources。
- CDC STEADI fall prevention resources as downstream risk context。
