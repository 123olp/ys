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
