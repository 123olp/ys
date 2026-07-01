# Musculoskeletal Integrity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/musculoskeletal-integrity` |
| 分级 | `C2` - 可能性源体维护层 |
| 控制轴 | 生命载体维护 |
| 分级理由 | 直接维护身体、脑、器官、衰老、损伤或生命系统这些可能性源体。 |
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


Musculoskeletal Integrity 负责整理肌肉、骨骼、关节、肌少症、骨质疏松、跌倒、连接组织和承载行动的结构完整性。

核心问题：

> 有效永生不是只让器官存活，还要让主体能站立、移动、抓取、工作和照护自己；肌骨系统决定行动能力和失能边界。

## 先验位置

```text
主体持续性最大化
  -> 主体必须拥有可承载行动的结构系统
  -> 肌肉、骨骼、关节和连接组织决定力量、移动、疼痛和跌倒风险
  -> 肌骨退化会把寿命转化为失能时间
  -> 因此肌骨完整性是有效时间和独立行动的基础条件
```

## 关注对象

- 肌少症、骨质疏松、骨折、关节退化、跌倒、慢性肌骨疼痛和行动限制。
- 肌骨状态与营养、活动、康复、疼痛、感官、环境和辅助技术的关系。
- 力量、平衡、步态、骨密度、跌倒风险和功能终点。
- 与 `rehabilitation-functioning/` 的关系：本域关注结构和承载系统；康复域关注疾病或损伤后的功能恢复过程。

## Human Infra 模型链路

```text
肌骨维护 / 风险控制 T
  -> 改变肌肉、骨骼、关节、疼痛和平衡变量 X
  -> 改变行动承载状态 S
  -> 改变跌倒、骨折、失能、疼痛和照护依赖风险
  -> 改变有效时间、独立性和任务完成能力
```

## 非目标

- 不提供训练处方、康复计划、影像诊断、药物、手术或设备建议。
- 不把肌肉量、骨密度或步数单指标等同于主体持续性。
- 不鼓励忽略疼痛、疲劳和受伤风险。

## Source Signals

- WHO Musculoskeletal Conditions: https://www.who.int/news-room/fact-sheets/detail/musculoskeletal-conditions
- WHO Falls: https://www.who.int/news-room/fact-sheets/detail/falls
