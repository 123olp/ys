# Landscaping Horticulture Worker Equipment Injury Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/landscaping-horticulture-worker-equipment-injury-continuity` |
| 分级 | `C5` - 可能性生态承载层 |
| 控制轴 | 外部生态承载 |
| 分级理由 | 关键词显示该域主要承载能源、水、食物、住房、治理、经济、通信、灾害或基础设施环境。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何承载主体展开未来的外部世界条件，例如能源、水、食物、住房、通信、治理、经济和基础设施？

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


`landscaping-horticulture-worker-equipment-injury-continuity` 研究园林、草坪、树木维护、户外工人、设备伤害、热/化学/生物暴露和工作连续性的关系。

> 核心问题：园林维护不是单纯美化；它把切割设备、跌落、噪声、热暴露、农药、毒植物、病媒、交通和季节性劳动组织叠加到同一个工作系统里。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖可维护的户外环境和安全劳动系统
  -> 园林/园艺工作会集中暴露设备、热、噪声、化学、植物和病媒风险
  -> 培训、PPE、设备维护、任务设计、天气调整和应急连接构成工作前提
  -> 若该前提失败，户外工人健康、公共空间维护、住房环境和恢复绿地都会被压缩
```

## 关注对象

- Landscaping、horticulture、草坪/树木维护、切割设备、跌落、噪声、热暴露、毒植物、农药和病媒。
- 工人培训、PPE、设备维护、季节性劳动、语言可及、伤害记录和职业健康连接。
- 与 `occupational-exposure-industrial-hygiene/` 的边界：上位域关注职业暴露总论；本域关注园林/园艺这一复合户外执行场景。

## Human Infra 链路

```text
园林园艺劳动风险被工程化管理
  -> 设备伤害、热应激、化学暴露和生物暴露下降
  -> 户外工人、公共空间、住房维护和绿地恢复更稳定
  -> 劳动持续性、城市恢复空间和主体行动条件被保护
```

## 非目标

- 不提供设备操作、树木作业、PPE 选型、农药使用、施工流程、雇佣合规、事故处理或职业法律建议。
- 不替代 OSHA、NIOSH、雇主安全计划、职业健康、设备制造商、园林承包商或急救医疗。
- 不把安全清单、天气、设备型号、现场照片或 AI 输出写成作业许可。

## Source Signals

- OSHA Landscaping and Horticultural Services: https://www.osha.gov/landscaping
- CDC/NIOSH Outdoor Workers: https://www.cdc.gov/niosh/topics/outdoor/
- CDC/NIOSH Poisonous Plants: https://www.cdc.gov/niosh/topics/plants/

## 下一步

- 建立 `landscape task -> equipment / heat / chemical / biological exposure -> work interruption -> continuity cost` 变量表。
- 区分草坪维护、树木修剪、灾后清理、公共绿地、移民/季节性工人和住房维护场景。
