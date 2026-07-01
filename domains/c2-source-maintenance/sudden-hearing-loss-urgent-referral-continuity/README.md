# Sudden Hearing Loss Urgent Referral Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/sudden-hearing-loss-urgent-referral-continuity` |
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


`sudden-hearing-loss-urgent-referral-continuity/` 负责整理突发听力下降、急性耳科转诊、时间敏感治疗窗口和听觉沟通急性保护连续性。

核心问题：

> 突发听损是时间敏感型听觉连续性事件；如果被误认为普通耳堵或延迟转诊，主体可能在短时间内失去关键沟通通道。

## 先验位置

```text
主体持续性最大化
  -> 主体必须保护听觉沟通通道免于急性崩溃
  -> 突发听损可在短时间内显著降低听觉输入
  -> 症状识别、急转速度和专科衔接决定恢复窗口是否被浪费
  -> 因此突发听损急转连续性是听觉输入的急性救援路径
```

## 关注对象

- 突发听力下降、单侧/双侧听损、耳鸣、眩晕、急诊/耳鼻喉转诊和随访。
- 初级接触点、听力评估、时间敏感窗口、治疗路径边界和恢复支持。
- 沟通中断、工作失能、心理压力、安全警报接收和社会参与。
- 与 `hearing-auditory-communication-continuity/` 的关系：本域聚焦急性听觉输入崩溃和转诊窗口。

## Human Infra 模型链路

```text
症状识别 / 急转通道 / 听力评估衔接 T
  -> 改变转诊延迟、听觉输入、伴随症状、恢复窗口和随访变量 X
  -> 改变主体沟通、工作、安全和心理状态 S
  -> 改变不可逆听损、隔离、任务失败和长期支持需求风险
  -> 保护急性听觉连续性、关系参与和未来选择权
```

## 非目标

- 不提供分诊、是否急诊判断、药物建议、影像/听力图解释、治疗窗口判断或个体预后。
- 不根据症状描述判断突发性耳聋、耳垢、感染、神经疾病或眩晕风险。
- 不替代急诊、耳鼻喉、听力学、神经或心理健康专业服务。

## Source Signals

- NIDCD Sudden Deafness: https://www.nidcd.nih.gov/health/sudden-deafness
- NIDCD Tinnitus: https://www.nidcd.nih.gov/health/tinnitus
- WHO Deafness and hearing loss: https://www.who.int/news-room/fact-sheets/detail/deafness-and-hearing-loss

## 下一步

- 建立突发听损 Source Card，区分症状信号、急转通道、恢复窗口和沟通功能终点。
- 对接急诊转诊、耳鸣、眩晕、工作连续性和患者权益沟通域。
