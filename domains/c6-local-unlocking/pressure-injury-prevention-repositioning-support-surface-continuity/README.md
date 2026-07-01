# Pressure Injury Prevention, Repositioning and Support Surface Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/pressure-injury-prevention-repositioning-support-surface-continuity` |
| 分级 | `C6` - 局部可能性解锁层 |
| 控制轴 | 局部阻塞解除 |
| 分级理由 | 未命中更高层边界、载体、能力、转换或生态规则，暂归为具体场景的局部可能性解锁。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域解除的是哪一个具体疾病、流程、服务、职业、家庭、社区或专项风险中的局部阻塞？

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


`pressure-injury-prevention-repositioning-support-surface-continuity/` 研究长期卧床、行动受限、感觉减退、潮湿、营养不足和支撑面失效如何造成压力损伤，并进一步压缩主体行动能力、感染安全和照护资源。

> 核心问题：压力损伤不是单一皮肤问题，而是行动、感觉、护理、支撑面、营养和环境连续性共同失败后的组织损伤。

## 先验位置

```text
有效永生
  -> 主体必须长期保持身体边界和组织完整性
  -> 行动受限或感觉反馈不足会让压力、剪切、潮湿和局部缺血持续累积
  -> 压力损伤会增加疼痛、感染、住院、照护负担和死亡风险
  -> 因此压力损伤预防是失能状态下维持主体边界的执行域
```

## 关注对象

- Pressure injury, pressure ulcer, support surface, repositioning, shear, moisture, immobility, sensory loss and long-term care risk。
- 与 `skin-barrier-wound-healing/` 的关系：父域关注皮肤边界总框架，本域关注压力、支撑面和翻身/减压执行链。

## Human Infra 模型链路

```text
减压与支撑面连续性 T
  -> 改变局部压力、剪切、潮湿、感觉反馈和护理执行 X
  -> 改变皮肤/软组织完整性、疼痛和感染入口 S
  -> 改变感染、住院、失能和死亡风险 lambda(t)
  -> 改变有效时间、照护成本和主体恢复窗口
```

## 非目标

- 不提供压力损伤分期、伤口判断、翻身时间表、支撑面选择、敷料、药物、清创或个体护理建议。
- 不根据照片、症状或位置输出诊断、分级、急诊判断或护理计划。

## Source Signals

- AHRQ pressure injury prevention toolkit.
- NPIAP pressure injury staging materials.
- MedlinePlus pressure injuries materials.
