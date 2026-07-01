# Age Related Hearing Loss Hearing Aid Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/age-related-hearing-loss-hearing-aid-continuity` |
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


`age-related-hearing-loss-hearing-aid-continuity/` 负责整理年龄相关性听力下降、言语识别、助听器可及、验配维护和沟通参与连续性。

核心问题：

> 年龄相关听损不是单纯“听不清”；它会把关系、医疗沟通、警报接收和日常服务理解转化为持续摩擦，最终压缩社会参与和主体行动质量。

## 先验位置

```text
主体持续性最大化
  -> 主体必须持续接入语言、关系、服务和环境声音
  -> 年龄相关听损会降低言语识别、噪声环境沟通和警报接收
  -> 助听支持若不可及、不可维护或不适配，会放大孤立、疲劳和误解
  -> 因此年龄相关听损与助听连续性是晚年沟通和安全输入基础设施
```

## 关注对象

- 年龄相关性听力下降、言语识别、双耳听觉、沟通疲劳和听觉努力。
- 助听器、OTC 助听器、验配、维护、电池/耗材、费用和可及性。
- 医疗沟通、家庭关系、公共服务理解、声音警报和社会参与。
- 与 `hearing-auditory-communication-continuity/` 的关系：本域聚焦老年听损和助听执行链。

## Human Infra 模型链路

```text
听力评估 / 助听器可及 / 维护支持 T
  -> 改变言语识别、噪声沟通、警报接收、设备可用性和沟通疲劳变量 X
  -> 改变主体关系参与、医疗理解、服务办理和安全响应状态 S
  -> 改变孤立、误解、认知负担、事故和任务中断风险
  -> 增加沟通连续性、有效时间和未来选择权
```

## 非目标

- 不提供听力诊断、听力图解释、助听器处方、设备调试、品牌推荐或购买建议。
- 不根据听力指标判断认知、驾驶、工作、福利或保险资格。
- 不替代听力学、耳鼻喉、验配师、言语语言治疗或康复专业服务。

## Source Signals

- NIDCD Age-Related Hearing Loss: https://www.nidcd.nih.gov/health/age-related-hearing-loss
- NIDCD Hearing Aids: https://www.nidcd.nih.gov/health/hearing-aids
- WHO Deafness and hearing loss: https://www.who.int/news-room/fact-sheets/detail/deafness-and-hearing-loss

## 下一步

- 建立年龄相关听损 Source Card，区分听觉变量、设备可及性、维护摩擦和沟通参与终点。
- 对接老年照护、医疗沟通、辅助技术和社会连接域。
