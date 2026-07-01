# Tinnitus Sound Tolerance Sleep Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/tinnitus-sound-tolerance-sleep-continuity` |
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


`tinnitus-sound-tolerance-sleep-continuity/` 负责整理耳鸣、声音耐受、睡眠中断、注意力负担和长期有效时间连续性。

核心问题：

> 耳鸣常常不是“听见声音”这么简单；它会通过睡眠、注意力、情绪和声音环境耐受，把主体的恢复系统和任务执行窗口持续拉低。

## 先验位置

```text
主体持续性最大化
  -> 主体必须维持睡眠、注意力、情绪和声音环境耐受
  -> 耳鸣会在外部声源不存在时持续占用感知和认知资源
  -> 睡眠中断、烦扰、焦虑和听觉疲劳会降低有效时间和恢复能力
  -> 因此耳鸣与声音耐受连续性是听觉-恢复交叉基础设施
```

## 关注对象

- 耳鸣、声音敏感、烦扰、睡眠中断、注意力负担和生活质量。
- 听力损失、噪声暴露、心理负担、声环境、助听/声音支持和服务可及性。
- 工作、学习、关系、睡眠恢复、焦虑抑郁交叉和有效时间损耗。
- 与 `hearing-auditory-communication-continuity/` 的关系：本域聚焦耳鸣负担和恢复影响。

## Human Infra 模型链路

```text
耳鸣评估 / 声环境支持 / 睡眠与心理服务 T
  -> 改变耳鸣烦扰、睡眠、声音耐受、注意力和情绪变量 X
  -> 改变主体恢复、工作学习、社交和长期参与状态 S
  -> 改变失眠、焦虑、沟通疲劳、有效时间损耗和任务中断风险
  -> 增加恢复质量、注意力稳定和未来选择权
```

## 非目标

- 不提供耳鸣诊断、治疗方案、补剂、设备、药物、声音疗法参数或产品推荐。
- 不根据耳鸣描述判断听损、神经疾病、急症、心理风险或个体预后。
- 不替代耳鼻喉、听力学、睡眠医学、心理健康或神经专业服务。

## Source Signals

- NIDCD Tinnitus: https://www.nidcd.nih.gov/health/tinnitus
- NIDCD Noise-Induced Hearing Loss: https://www.nidcd.nih.gov/health/noise-induced-hearing-loss
- WHO Deafness and hearing loss: https://www.who.int/news-room/fact-sheets/detail/deafness-and-hearing-loss

## 下一步

- 建立耳鸣 Source Card，区分声音感知、烦扰、睡眠、注意力和有效时间终点。
- 对接睡眠、心理健康、噪声暴露和听觉沟通域。
