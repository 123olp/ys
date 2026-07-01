# Hypertensive Crisis End Organ Risk Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/hypertensive-crisis-end-organ-risk-continuity` |
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


`hypertensive-crisis-end-organ-risk-continuity/` 研究高血压危象、急性靶器官风险、脑/心/肾/主动脉事件、诊断接入和长期血压治理交接如何影响主体持续性。

> 核心问题：血压不是孤立数字，而是脑、心、肾和血管壁承受的机械负荷。高血压危象需要被建模为急性靶器官损伤窗口，而不是泛化的慢性血压管理。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖血管压力处在器官可承受范围内
  -> 极端血压和靶器官损伤会快速改变卒中、心衰、肾损伤和主动脉风险
  -> 结果取决于识别、诊断接入、急性稳定和长期交接
  -> 因此高血压危象是血管负荷进入急性器官风险的研究域
```

## 关注对象

- Hypertensive emergency / urgency distinction as system concept, end-organ injury, stroke link, acute heart failure, AKI, aortic syndromes, access to follow-up, medication continuity。
- 与 `cardiovascular-resilience/` 的边界：该域关注长期血压风险；本域关注急性靶器官损伤和连续性断点。
- 与 `cerebrovascular-stroke-brain-perfusion-resilience/` 和 `acute-kidney-injury-renal-replacement-continuity/` 的关系：高血压危象可进入脑、心、肾急性事件。

## Human Infra 模型链路

```text
高血压危象治理系统 T
  -> 改变测量可信度、识别延迟、靶器官评估、急性稳定和随访变量 X
  -> 改变脑灌注、心脏负荷、肾功能、血管事件和用药连续性 S
  -> 改变卒中、心衰、AKI、主动脉事件和死亡风险 λ(t)
  -> 影响主体存活、认知、行动和未来选择权
```

## 非目标

- 不提供血压读数判断、急诊分诊、降压药、剂量、家庭处理、用药调整、检查选择或个体治疗建议。
- 不生成高血压危象评分、监测工具、药物路径、家庭血压解释或预后判断。
- 不收集个案血压、症状、化验、影像、用药、设备或位置数据。

## Source Signals

- AHA high blood pressure guideline materials: https://professional.heart.org/
- CDC high blood pressure materials: https://www.cdc.gov/high-blood-pressure/
- NHLBI high blood pressure materials: https://www.nhlbi.nih.gov/health/high-blood-pressure

## 下一步

- 建立 Hypertensive Crisis Card：measurement, symptoms, end-organ screen, acute stabilization boundary, follow-up continuity。
- 与 `cardiovascular-resilience/`、`cerebrovascular-stroke-brain-perfusion-resilience/` 和 `acute-kidney-injury-renal-replacement-continuity/` 建立接口。
