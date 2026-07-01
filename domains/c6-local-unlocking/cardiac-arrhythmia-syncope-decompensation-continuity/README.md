# Cardiac Arrhythmia Syncope Decompensation Continuity

`cardiac-arrhythmia-syncope-decompensation-continuity/` 研究心律失常、晕厥、传导异常、心房颤动、室性心律失常、猝死前风险和监测/转诊路径如何影响主体持续性。

> 核心问题：心律节律失稳会把主体从正常行动突然推入晕厥、跌倒、卒中、心衰或骤停。它需要被建模为“节律连续性”而不是泛化的心血管风险。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖稳定心律维持脑灌注、循环输出和行动安全
  -> 心律失常和晕厥可突然造成跌倒、缺血、栓塞或骤停
  -> 风险取决于监测、识别、转诊、抗凝/节律管理系统和安全交接
  -> 因此心律失常与晕厥是主体连续性的突发失稳域
```

## 关注对象

- Atrial fibrillation、syncope、bradyarrhythmia、tachyarrhythmia、ventricular arrhythmia、ambulatory monitoring、stroke risk, fall risk, sudden cardiac death precursors。
- 与 `cardiovascular-resilience/` 的边界：本域聚焦节律/传导失稳及突发事件链。
- 与 `cardiac-arrest-cpr-defibrillation-continuity/` 的关系：恶性心律失常可进入骤停；本域关注骤停前的识别、监测和稳定链。

## Human Infra 模型链路

```text
心律与晕厥管理系统 T
  -> 改变监测可及、风险识别、转诊、抗凝/节律治理和安全交接变量 X
  -> 改变脑灌注、跌倒、卒中、心衰、骤停前状态 S
  -> 改变急性死亡、失能、认知损伤和行动受限风险 λ(t)
  -> 影响主体行动连续性和未来选择权
```

## 非目标

- 不提供心电图判读、晕厥分诊、抗凝、用药、起搏器/除颤器、消融、设备选择或个体医疗建议。
- 不生成心律失常评分、卒中风险计算、跌倒处理、驾驶限制、运动建议或监测工具。
- 不收集个案心电图、设备数据、症状、用药、卒中风险因素或位置数据。

## Source Signals

- 2023 AHA/ACC/HRS atrial fibrillation guideline materials: https://professional.heart.org/
- 2017 ACC/AHA/HRS syncope guideline materials: https://professional.heart.org/
- NHLBI arrhythmia public materials: https://www.nhlbi.nih.gov/health/arrhythmias

## 下一步

- 建立 Rhythm Stability Card：monitoring, syncope, AF/stroke link, ventricular risk, fall risk, device pathway。
- 与 `cardiovascular-resilience/`、`cerebrovascular-stroke-brain-perfusion-resilience/` 和 `cardiac-arrest-cpr-defibrillation-continuity/` 建立接口。
