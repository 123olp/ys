# Vestibular Rehabilitation Balance Compensation Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/vestibular-rehabilitation-balance-compensation-continuity` |
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


Vestibular rehabilitation and balance compensation continuity studies structured rehabilitation, adaptation, substitution, habituation, assistive strategies, and adherence as infrastructure for restoring spatial action after vestibular loss.

核心问题：

> 前庭系统受损后，主体不一定只能被动承受；恢复依赖大脑补偿、训练、环境适配和长期执行，但这些机制若不可及或不可坚持，功能就停留在损伤状态。

## 先验位置

```text
主体持续性最大化
  -> 主体必须能在损伤后重新建立行动能力
  -> 前庭康复通过适应、替代、习惯化和任务训练促进补偿
  -> 服务可及、依从、环境适配和反馈决定恢复是否持续
  -> 因而前庭康复是空间行动损伤后的能力重建基础设施
```

## 关注对象

- 前庭康复、平衡训练、凝视稳定、习惯化、替代策略、家庭执行和服务可及。
- 依从性、训练反馈、康复师可及、保险覆盖、远程康复和长期维护。
- 与 `rehabilitation-functioning/` 的关系：康复域关注总体功能恢复；本域聚焦前庭和平衡补偿。
- 与 `implementation-science-adherence-behavior-change/` 的关系：实施科学域关注行为改变；本域关注前庭康复执行。

## Human Infra 模型链路

```text
康复服务 / 训练计划 / 反馈系统 / 环境适配 T
  -> 改变凝视稳定、姿势控制、回避行为、依从和补偿能力 X
  -> 改变外出、工作、交通、家庭任务和跌倒暴露状态 S
  -> 改变失能、复发恐惧、孤立和照护依赖风险 λ(t)
  -> 影响恢复速度、行动密度和未来选择权
```

## 非目标

- 不提供具体康复动作、训练剂量、个体训练计划、设备建议、症状解释或治疗承诺。
- 不根据个人眩晕类型决定康复适应证、强度、频率或预后。
- 不替代前庭康复、物理治疗、耳鼻喉、神经或康复医学服务。

## Source Signals

- Academy of Neurologic Physical Therapy / APTA vestibular rehabilitation clinical practice guidelines。
- WHO Rehabilitation 2030 resources。
- NIDCD balance disorders resources。
