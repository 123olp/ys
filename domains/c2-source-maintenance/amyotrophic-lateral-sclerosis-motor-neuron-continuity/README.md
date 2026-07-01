# Amyotrophic Lateral Sclerosis Motor Neuron Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/amyotrophic-lateral-sclerosis-motor-neuron-continuity` |
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


`amyotrophic-lateral-sclerosis-motor-neuron-continuity/` 研究 ALS、运动神经元退行、肌无力、吞咽呼吸风险、沟通能力和照护连续性如何影响主体持续性。

## Core Question

当运动神经元退行持续剥夺行动、呼吸、吞咽和表达能力时，主体如何保留沟通、选择、尊严、照护协作和未来选择权？

## 先验位置

- 与 `neuro-continuity/` 的关系：ALS 直接挑战行动输出通道和表达通道。
- 与 `respiratory-oxygenation/` 的关系：呼吸肌受累会让通气支持和急性风险成为关键边界。
- 与 `speech-language-communication-continuity/` 的关系：沟通辅助决定主体偏好和同意能否继续表达。

## 关注对象

- 肌无力、运动功能、吞咽、呼吸、沟通、营养、辅助技术、照护者负担、预先照护计划和尊严边界。
- 诊断漫游、专科团队可及、临床试验信号、进展速度和服务承接断点。

## Human Infra 模型链路

```text
运动神经元退行
-> 行动、呼吸、吞咽和表达通道受损
-> 主体行动密度、沟通权和照护协作能力下降
-> 尊严、同意、未来选择权和长期项目被压缩
-> 主体持续性下降
```

## 非目标

- 不提供 ALS 诊断、基因/肌电/影像判读、药物、通气、营养管、沟通设备、临床试验或照护计划建议。
- 不输出个体生存期、进展速度、治疗选择、机构选择、保险或法律判断。

## Source Signals

- NINDS ALS: https://www.ninds.nih.gov/health-information/disorders/amyotrophic-lateral-sclerosis-als

## 下一步

- 建立 motor-neuron continuity card：把行动输出、呼吸、吞咽、沟通和照护边界并列审查。
