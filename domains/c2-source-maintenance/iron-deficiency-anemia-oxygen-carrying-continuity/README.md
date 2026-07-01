# Iron Deficiency Anemia Oxygen Carrying Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/iron-deficiency-anemia-oxygen-carrying-continuity` |
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


`iron-deficiency-anemia-oxygen-carrying-continuity/` 研究铁缺乏、贫血、氧输送、疲劳、认知体力、月经/胃肠/营养来源和治疗可及如何影响主体持续性。

> 核心问题：铁缺乏和贫血会把氧输送不足转化为疲劳、注意力下降、运动耐受下降、妊娠风险和有效时间损耗。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要稳定血红蛋白、氧输送、体力和认知速度
  -> 铁缺乏和贫血会造成疲劳、气短、注意力下降、运动能力下降和阶段性风险
  -> 结果取决于来源识别、营养/出血/吸收路径、检测、治疗可及和复发预防
  -> 因此铁缺乏贫血是有效时间、能量系统和风险追踪的关键维护域
```

## 关注对象

- Iron deficiency、anemia、hemoglobin、oxygen carrying capacity、fatigue、exercise intolerance、heavy menstrual bleeding, GI blood loss, pregnancy, nutrition, absorption。
- 与 `blood-oxygen-hemostasis/` 的边界：该域关注血氧与止血总机制；本域聚焦铁缺乏贫血对能量、认知和病因追踪的影响。
- 与 `menstrual-health-cycle-literacy-continuity/` 和 `inflammatory-bowel-disease-digestive-continuity/` 的关系：月经过多、胃肠失血和吸收问题可能是重要上游。

## Human Infra 模型链路

```text
铁缺乏贫血识别与恢复系统 T
  -> 改变铁储备、血红蛋白、出血/吸收来源、疲劳、运动耐受和治疗可及变量 X
  -> 改变体力、注意力、工作学习效率、妊娠风险和疾病追踪状态 S
  -> 改变有效时间损耗、失能风险、诊断延迟风险和阶段性风险 λ(t)
  -> 影响主体能量预算、行动质量和未来选择权
```

## 非目标

- 不提供个人贫血诊断、化验判读、补铁剂量、输血、胃肠检查、月经处理、妊娠或饮食建议。
- 不生成个人治疗计划、补充剂计划、检查排序、失血来源判断、运动或工作限制建议。
- 不收集个案化验、月经、胃肠症状、妊娠、饮食、用药或保险资料。

## Source Signals

- NHLBI anemia: https://www.nhlbi.nih.gov/health/anemia
- NHLBI iron-deficiency anemia: https://www.nhlbi.nih.gov/health/anemia/iron-deficiency-anemia
- NIH Office of Dietary Supplements iron fact sheet: https://ods.od.nih.gov/factsheets/Iron-Consumer/

## 下一步

- 建立 Anemia Energy Card：hemoglobin/iron status boundary, fatigue, source pathway, menstruation/GI/nutrition overlap, treatment access。
- 与 `blood-oxygen-hemostasis/`、`menstrual-health-cycle-literacy-continuity/` 和 `inflammatory-bowel-disease-digestive-continuity/` 建立接口。
