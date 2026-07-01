# Vestibular Migraine Dizziness Sensory Load Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/vestibular-migraine-dizziness-sensory-load-continuity` |
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


Vestibular migraine dizziness and sensory load continuity studies migraine-linked vertigo, motion sensitivity, light/sound sensitivity, cognitive fog, and episodic disability as a cross-domain burden on effective time.

核心问题：

> 偏头痛相关眩晕不是单纯头痛，也不是单纯平衡问题；它会把光、声、运动、屏幕、通勤和认知任务组合成一组发作性行动限制。

## 先验位置

```text
主体持续性最大化
  -> 主体必须能在感官负荷和空间运动中保持任务能力
  -> 偏头痛相关前庭症状会同时扰动眩晕、光声敏感、注意和恢复
  -> 发作和残余期会压缩工作、学习、出行和社交窗口
  -> 因而前庭性偏头痛是感官负荷与有效时间之间的交叉失效模式
```

## 关注对象

- 前庭性偏头痛、眩晕、运动敏感、光声敏感、脑雾、恶心和发作后疲劳。
- 屏幕任务、会议、驾驶/通勤、学习负担、社交参与和恢复安排。
- 与 `migraine-headache-effective-time-burden/` 的关系：偏头痛域关注总体失能；本域关注眩晕和感官负荷交叉。
- 与 `tinnitus-sound-tolerance-sleep-continuity/` 的关系：耳鸣域关注内源声音；本域关注偏头痛相关声光运动敏感。

## Human Infra 模型链路

```text
识别 / 负荷管理 / 工作学习适配 / 恢复支持 T
  -> 改变眩晕发作、感官敏感、认知雾和恢复时间 X
  -> 改变屏幕工作、出行、学习、社交和休息状态 S
  -> 改变失能天数、事故暴露、孤立和有效时间损耗风险 λ(t)
  -> 影响长期能力积累、角色维持和未来选择权
```

## 非目标

- 不提供前庭性偏头痛诊断、药物、补剂、饮食、触发因素处方、驾驶或工作限制建议。
- 不根据个人症状区分偏头痛、BPPV、梅尼埃病、PPPD 或脑血管事件。
- 不替代神经、耳鼻喉、康复、心理健康或急诊服务。

## Source Signals

- NIDCD balance disorders resources。
- American Migraine Foundation / NIH migraine education as secondary context。
- Vestibular migraine consensus literature as research context。
