# Acute Heart Failure Decompensation Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/acute-heart-failure-decompensation-continuity` |
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


`acute-heart-failure-decompensation-continuity/` 研究急性心衰失代偿、容量负荷、肺水肿、低灌注、急诊/住院路径、再入院和功能恢复如何影响主体持续性。

> 核心问题：心衰失代偿不是单纯慢病加重，而是循环、呼吸、肾脏和药物管理同时失衡的急性状态。主体能否恢复有效时间，取决于稳定、去充血、监测、出院交接和再入院预防。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖心脏泵功能维持供氧、行动和器官灌注
  -> 急性失代偿会把慢性心衰推入呼吸衰竭、肾损伤和住院循环
  -> 恢复依赖识别、稳定、监测、出院计划和长期随访
  -> 因此急性心衰失代偿是心血管持续性的急性执行域
```

## 关注对象

- Acute decompensated heart failure、pulmonary edema、congestion、hypoperfusion、renal interaction、hospitalization、readmission、transition of care、cardiac rehab / self-management support。
- 与 `cardiovascular-resilience/` 的边界：该域关注心血管长期风险；本域关注失代偿急性窗口和出院后恢复。
- 与 `mechanical-ventilation-respiratory-failure-continuity/` 的关系：严重肺水肿可进入呼吸支持，但本域关注心衰失代偿链条。

## Human Infra 模型链路

```text
急性心衰失代偿系统 T
  -> 改变容量负荷、去充血、灌注、肾心交互、出院交接变量 X
  -> 改变呼吸状态、肾功能、住院负担、再入院和运动能力 S
  -> 改变急性死亡、再住院、长期虚弱和有效时间损失 λ(t)
  -> 影响主体行动能力、恢复能力和未来选择权
```

## 非目标

- 不提供利尿剂、血压、氧疗、液体、饮食、设备、急诊分诊、住院或个体治疗建议。
- 不生成心衰临床路径、药物调整、再入院预测、出院计划或个案监测工具。
- 不收集个案体重、血压、氧饱和度、化验、影像、药物、设备或住院资料。

## Source Signals

- 2022 AHA/ACC/HFSA heart failure guideline materials: https://professional.heart.org/
- NHLBI heart failure public materials: https://www.nhlbi.nih.gov/health/heart-failure
- CDC heart failure public health materials: https://www.cdc.gov/heart-disease/about/heart-failure.html

## 下一步

- 建立 Acute HF Decompensation Card：congestion, perfusion, renal interaction, respiratory support, discharge handoff, readmission。
- 与 `cardiovascular-resilience/`、`mechanical-ventilation-respiratory-failure-continuity/` 和 `acute-kidney-injury-renal-replacement-continuity/` 建立接口。
