# Auditory Processing Listening Effort Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/auditory-processing-listening-effort-continuity` |
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


`auditory-processing-listening-effort-continuity/` 负责整理听觉处理、噪声中听懂、听觉努力、课堂/会议参与和认知带宽连续性。

核心问题：

> 有些听觉问题不是声音能否进入耳朵，而是大脑能否在真实噪声环境中把声音变成可用信息；听觉处理和听觉努力直接消耗注意力、学习和工作带宽。

## 先验位置

```text
主体持续性最大化
  -> 主体必须把声音信号转化为可理解、可行动的信息
  -> 听觉处理困难会在课堂、会议、公共空间和噪声环境中放大理解成本
  -> 过高听觉努力会挤占注意力、记忆、执行功能和社交参与
  -> 因此听觉处理与听觉努力连续性是听觉输入转化为认知行动的接口层
```

## 关注对象

- 听觉处理困难、噪声中言语识别、听觉努力、课堂/会议参与和疲劳。
- 儿童学习、成人工作、老年沟通、辅助听觉策略、声学环境和可访问沟通。
- 注意力、工作记忆、听觉疲劳、误解、社交回避和有效时间损耗。
- 与 `hearing-auditory-communication-continuity/` 的关系：本域聚焦听觉信息加工和认知负担。

## Human Infra 模型链路

```text
声学环境 / 沟通适配 / 听觉支持 T
  -> 改变噪声中理解、听觉努力、注意力占用和沟通疲劳变量 X
  -> 改变主体课堂、会议、服务沟通和社交参与状态 S
  -> 改变信息遗漏、学习损失、工作错误和有效时间损耗风险
  -> 增加认知带宽、任务质量和未来选择权
```

## 非目标

- 不提供听觉处理障碍诊断、测试解释、训练方案、学校便利、设备处方或个体教育建议。
- 不根据听力、注意力或学习表现判断认知能力、残障资格或工作/学习许可。
- 不替代听力学、言语语言治疗、教育评估、心理测评或职业康复服务。

## Source Signals

- NIDCD Auditory Processing Disorder: https://www.nidcd.nih.gov/health/auditory-processing-disorder
- NIDCD Assistive Devices: https://www.nidcd.nih.gov/health/assistive-devices-people-hearing-voice-speech-or-language-disorders
- ASHA Hearing and Balance resources: https://www.asha.org/public/hearing/

## 下一步

- 建立听觉处理 Source Card，区分声音进入、信息加工、认知负担和参与终点。
- 对接教育、会议沟通、声环境、注意力和无障碍设计域。
