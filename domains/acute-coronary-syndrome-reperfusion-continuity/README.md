# Acute Coronary Syndrome Reperfusion Continuity

`acute-coronary-syndrome-reperfusion-continuity/` 研究急性冠脉综合征、胸痛识别、心电图/肌钙蛋白路径、再灌注窗口、导管室/转运能力和心肌损伤后恢复如何影响主体持续性。

> 核心问题：急性冠脉综合征把冠状动脉供血失败转化为分钟到小时级心肌损失。有效永生需要把“可再灌注窗口”建模为避免骤停、心衰和长期失能的关键条件。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖持续心肌供血维持循环和行动能力
  -> 冠脉急性闭塞会快速改变死亡、心衰和有效时间风险
  -> 结果取决于识别、转运、诊断、再灌注和康复链条
  -> 因此急性冠脉综合征是心血管连续性的时间关键失效域
```

## 关注对象

- Chest pain systems、ECG delay、troponin pathways、STEMI/NSTEMI routing、PCI access、time-to-reperfusion、cardiac rehabilitation、secondary prevention handoff。
- 与 `cardiovascular-resilience/` 的边界：该域关注长期心血管韧性；本域关注急性冠脉事件的再灌注窗口和急性后续恢复。
- 与 `cardiac-arrest-cpr-defibrillation-continuity/` 的关系：ACS 是骤停上游原因之一，但本域关注骤停前的可逆窗口。

## Human Infra 模型链路

```text
ACS 再灌注系统 T
  -> 改变识别延迟、诊断延迟、转运、再灌注和康复变量 X
  -> 改变心肌坏死范围、循环稳定性、心衰风险和功能恢复状态 S
  -> 改变急性死亡、再住院、心衰和长期有效时间损失 λ(t)
  -> 影响主体存活、行动能力和未来选择权
```

## 非目标

- 不提供胸痛判断、是否呼叫急救、心电图/肌钙蛋白解读、药物、介入、溶栓、医院选择或个体治疗建议。
- 不生成 STEMI/NSTEMI 临床路径、分诊工具、转运建议、再灌注决策或康复处方。
- 不收集个案症状、心电图、检验值、用药、病历、位置或急救资料。

## Source Signals

- AHA / ACC acute coronary syndrome guideline materials: https://www.heart.org/
- Professional Heart Daily guideline materials: https://professional.heart.org/
- NCBI / NHLBI heart attack public materials: https://www.nhlbi.nih.gov/health/heart-attack

## 下一步

- 建立 ACS Reperfusion Card：symptom-to-contact, ECG, troponin, transfer, PCI/reperfusion, post-event recovery。
- 与 `cardiovascular-resilience/`、`cardiac-arrest-cpr-defibrillation-continuity/` 和 `intensive-care-organ-support-delirium-continuity/` 建立接口。
