# Age Related Macular Degeneration Central Vision Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/age-related-macular-degeneration-central-vision-continuity` |
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


`age-related-macular-degeneration-central-vision-continuity/` 负责整理年龄相关性黄斑变性、中央视力、阅读识别、治疗随访和低视力衔接。

核心问题：

> AMD 主要压缩中央视觉，使阅读、面孔识别、用药识别、屏幕工作和精细任务变慢或失效；它直接侵蚀主体获取信息和维持独立生活的能力。

## 先验位置

```text
主体持续性最大化
  -> 主体必须持续读写、识别细节和处理近距离视觉任务
  -> 黄斑功能损伤会首先破坏中央视觉和精细识别
  -> 中央视力下降会降低学习、工作、社交识别、自我管理和独立生活
  -> 因此 AMD 中央视觉连续性是信息获取和精细行动的基础条件
```

## 关注对象

- 年龄相关性黄斑变性、干性/湿性 AMD、中央视力、阅读速度、面孔识别和精细任务。
- 监测、治疗随访、注射治疗路径、低视力转介和辅助工具衔接。
- 老年独立生活、药品标签识别、账单处理、屏幕使用和社交连接。
- 与 `low-vision-rehabilitation-assistive-technology-continuity/` 的关系：本域关注 AMD 机制与治疗链，低视力域关注补偿和适配。

## Human Infra 模型链路

```text
AMD 监测 / 治疗随访 / 低视力衔接 T
  -> 改变中央视力、阅读速度、识别能力、治疗延迟和辅助适配变量 X
  -> 改变主体信息获取、自理、财务/药物管理和社交状态 S
  -> 改变独立生活下降、任务失败、照护依赖和有效时间损耗风险
  -> 保护学习入口、日常自理和未来选择权
```

## 非目标

- 不提供 AMD 诊断、影像判读、注射治疗建议、补剂建议、复查间隔或个体预后。
- 不判断个人能否驾驶、工作、独立生活或使用特定视觉辅助设备。
- 不把任何治疗或补偿工具写成恢复中央视力的承诺。

## Source Signals

- National Eye Institute Age-Related Macular Degeneration: https://www.nei.nih.gov/learn-about-eye-health/eye-conditions-and-diseases/age-related-macular-degeneration
- CDC Vision Health: https://www.cdc.gov/vision-health/
- WHO Blindness and visual impairment: https://www.who.int/news-room/fact-sheets/detail/blindness-and-visual-impairment

## 下一步

- 建立 AMD Source Card，区分中央视觉、治疗随访、低视力支持和独立生活终点。
- 对接老年照护、数字无障碍、用药自理和低视力康复域。
