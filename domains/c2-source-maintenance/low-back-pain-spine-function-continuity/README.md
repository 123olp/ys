# Low Back Pain Spine Function Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/low-back-pain-spine-function-continuity` |
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


`low-back-pain-spine-function-continuity/` 研究腰背痛、脊柱功能、工作活动负荷、影像与转诊、康复可及和复发预防如何影响主体持续性。

> 核心问题：腰背痛是高频、复发、跨年龄和跨职业的行动能力断点；它通过疼痛、恐惧回避、工作限制和医疗路径摩擦持续吞噬有效时间。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要稳定移动、坐立、弯腰、搬运和工作参与能力
  -> 腰背痛会造成行动受限、任务中断、医疗利用和复发风险
  -> 结果取决于危险信号识别、保守治疗可及、康复、工作设计和复发预防
  -> 因此腰背痛是脊柱功能和长期执行能力的关键维护域
```

## 关注对象

- Low back pain、spine function、red flags、physical therapy access、activity continuation、work modification、imaging overuse risk、recurrence prevention。
- 与 `musculoskeletal-integrity/` 的边界：该域关注肌骨结构总问题；本域聚焦腰背痛这个高频任务执行断点。
- 与 `chronic-pain-functional-restoration-continuity/` 的关系：腰背痛可进入慢性疼痛系统，但需要单独处理脊柱功能、工作负荷和复发路径。

## Human Infra 模型链路

```text
腰背痛脊柱功能维护系统 T
  -> 改变疼痛、活动耐受、工作负荷、康复可及、影像路径和复发预防变量 X
  -> 改变移动能力、工作参与、睡眠、医疗摩擦和恐惧回避状态 S
  -> 改变有效时间损耗、失能风险、收入连续性和慢性疼痛转化 λ(t)
  -> 影响主体长期行动半径、任务完成能力和未来选择权
```

## 非目标

- 不提供个人腰背痛诊断、影像判读、康复动作、拉伸、药物、注射、手术、红旗分诊或工作限制建议。
- 不生成治疗计划、运动计划、复工判断、设备购买、保险或工伤建议。
- 不收集个案疼痛、影像、神经症状、职业暴露、工伤或医疗记录。

## Source Signals

- NIAMS back pain: https://www.niams.nih.gov/health-topics/back-pain
- CDC musculoskeletal pain and work-related health signals: https://www.cdc.gov/niosh/musculoskeletal/
- WHO musculoskeletal health: https://www.who.int/news-room/fact-sheets/detail/musculoskeletal-conditions

## 下一步

- 建立 Spine Function Card：duration, red-flag routing, activity limitation, work exposure, rehabilitation access, recurrence prevention。
- 与 `musculoskeletal-integrity/`、`chronic-pain-functional-restoration-continuity/` 和 `workplace-accommodation-return-to-work-continuity/` 建立接口。
