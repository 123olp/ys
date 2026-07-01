# Cataract Vision Restoration Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/cataract-vision-restoration-continuity` |
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


`cataract-vision-restoration-continuity/` 负责整理白内障、晶状体混浊、可逆性视力下降、手术服务可及性和视觉恢复连续性。

核心问题：

> 白内障会把可恢复的视觉输入退化成阅读、移动、驾驶、工作和照护摩擦；它的 Human Infra 价值不在“眼病本身”，而在可恢复功能是否能及时回到主体行动系统。

## 先验位置

```text
主体持续性最大化
  -> 主体必须持续获得清晰、稳定、可行动的外部视觉输入
  -> 晶状体混浊会降低清晰度、对比度、夜间视觉和任务可靠性
  -> 可恢复视力若因等待、费用、服务断点或术后衔接延迟而丢失，会压缩有效时间和独立生活
  -> 因此白内障视觉恢复连续性是视觉输入基础设施中的可逆功能恢复路径
```

## 关注对象

- 白内障、晶状体混浊、视力模糊、眩光、夜间视觉下降和对比敏感度下降。
- 眼科评估、手术可及性、等待时间、费用覆盖、术后随访和屈光矫正衔接。
- 老年人跌倒、驾驶、阅读、用药识别、工作参与和照护依赖。
- 与 `vision-eye-health-continuity/` 的关系：本域聚焦白内障这类常见且可恢复的视觉失效模式。

## Human Infra 模型链路

```text
白内障筛查 / 手术服务 / 术后衔接 T
  -> 改变晶状体透明度、视觉清晰度、眩光、夜间视觉和服务等待变量 X
  -> 改变主体阅读、移动、驾驶、工作和自理状态 S
  -> 改变跌倒、事故、照护依赖、任务失败和有效时间损耗风险
  -> 增加视觉行动窗口、独立生活能力和未来选择权
```

## 非目标

- 不提供白内障诊断、手术适应证、人工晶体选择、术前术后医嘱或个体风险判断。
- 不比较具体医院、医生、手术方式、镜片品牌或保险资格。
- 不把白内障手术写成无风险恢复承诺；必须保留并发症、随访和个体差异边界。

## Source Signals

- National Eye Institute Cataracts: https://www.nei.nih.gov/learn-about-eye-health/eye-conditions-and-diseases/cataracts
- CDC Vision Health: https://www.cdc.gov/vision-health/
- WHO Blindness and visual impairment: https://www.who.int/news-room/fact-sheets/detail/blindness-and-visual-impairment

## 下一步

- 建立白内障 Source Card，区分功能损害、服务可及性、手术恢复和主体持续性终点。
- 对接跌倒预防、驾驶移动、老年照护和低视力康复域。
