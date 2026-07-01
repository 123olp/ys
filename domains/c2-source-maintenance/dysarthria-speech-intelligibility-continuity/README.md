# Dysarthria Speech Intelligibility Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/dysarthria-speech-intelligibility-continuity` |
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


Dysarthria speech intelligibility continuity studies motor speech weakness, slowness, incoordination, and reduced intelligibility as constraints on interaction speed, safety signaling, and social participation.

核心问题：

> 构音障碍不是语言知识消失，而是把语言通过肌肉运动清晰输出的执行链受损；说得出但说不清，会让沟通被延迟、误解或替代。

## 先验位置

```text
主体持续性最大化
  -> 主体必须能把意图转成可理解的声音输出
  -> 构音、呼吸、发声、共鸣和韵律运动失调会降低清晰度
  -> 求助、工作沟通、关系互动和身份表达成本上升
  -> 因而构音障碍是语言意图到可听输出之间的运动执行失效模式
```

## 关注对象

- 神经系统疾病、脑损伤或运动系统问题相关构音障碍、言语清晰度、疲劳和说话效率。
- 交谈修复、环境噪声、听者负担、辅助沟通和身份尊严。
- 与 `neuro-continuity/` 的关系：神经域关注上游病变；本域关注言语输出可懂度。
- 与 `voice-disorders-phonation-communication-continuity/` 的关系：嗓音域关注发声质量；本域关注运动言语清晰度。

## Human Infra 模型链路

```text
识别 / 言语支持 / 沟通策略 / 环境适配 T
  -> 改变清晰度、说话速度、疲劳、听者负担和沟通修复变量 X
  -> 改变求助、工作、医疗会谈和关系互动状态 S
  -> 改变误解、被忽视、社会退缩和服务失败风险 λ(t)
  -> 影响主体表达能力、社会参与和未来选择权
```

## 非目标

- 不提供构音障碍诊断、病因判断、训练动作、治疗方案、设备处方或预后评估。
- 不根据个人声音或言语样本判断神经疾病、药物副作用或急症。
- 不替代神经、言语语言治疗、康复、耳鼻喉或急诊服务。

## Source Signals

- ASHA dysarthria practice materials。
- NIDCD speech and language disorder resources。
- Neurologic motor speech disorder literature as research context。
