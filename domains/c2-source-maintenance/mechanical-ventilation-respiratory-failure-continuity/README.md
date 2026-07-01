# Mechanical Ventilation Respiratory Failure Continuity

`mechanical-ventilation-respiratory-failure-continuity/` 研究急性呼吸衰竭、氧合/通气失败、机械通气、撤机、呼吸治疗和长期呼吸功能恢复如何影响主体持续性。

> 核心问题：呼吸失败会在短时间内切断氧供。机械通气是把不可逆缺氧变成可支持、可恢复窗口的核心生命支持技术之一。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体持续性依赖氧合、通气和酸碱平衡
  -> 肺炎、ARDS、创伤、神经肌肉失败或麻醉可导致急性呼吸衰竭
  -> 机械通气可暂时代替呼吸功能，但也带来肺损伤、感染、谵妄和撤机风险
  -> 因此机械通气是呼吸失败进入生命支持模型的核心域
```

## 关注对象

- Acute respiratory failure、ARDS、oxygenation、ventilation、noninvasive/invasive ventilation、ventilator-associated harm、weaning、respiratory therapy、long-term recovery。
- 与 `respiratory-oxygenation/` 的边界：呼吸氧合域关注基础生理；本域关注急性失败和设备支持。
- 与 `home-oxygen-respiratory-equipment-supply-continuity/` 的关系：后者关注居家设备供应；本域关注急性和 ICU 生命支持。

## Human Infra 模型链路

```text
机械通气与呼吸衰竭支持 T
  -> 改变氧合、通气、设备可用、撤机、感染和肺保护变量 X
  -> 改变缺氧、二氧化碳潴留、ICU 病程和肺功能恢复状态 S
  -> 改变急性死亡、脑缺氧、呼吸机相关损伤和长期功能下降风险 λ(t)
  -> 影响主体存在、认知连续性和恢复能力
```

## 非目标

- 不提供氧疗、呼吸机参数、撤机、气道管理、ARDS 治疗、呼吸训练或个体医疗建议。
- 不生成设备设置、医院流程、居家呼吸设备操作、急救指导或替代呼吸治疗师的内容。
- 不收集呼吸机参数、血气、影像、SpO2、病历、设备日志或家庭医疗资料。

## Source Signals

- ATS/ESICM/SCCM Mechanical Ventilation Guideline: https://www.thoracic.org/statements/resources/cc/mechanical-ventilation-ards.pdf
- NIH Respiratory Failure: https://www.nhlbi.nih.gov/health/respiratory-failure
- CDC Ventilator-associated Event: https://www.cdc.gov/nhsn/psc/vae/index.html

## 下一步

- 建立 Respiratory Support Card：failure type, oxygenation, ventilation, device support, complications, weaning, recovery。
- 与 `respiratory-oxygenation/`、`intensive-care-organ-support-delirium-continuity/` 和 `home-oxygen-respiratory-equipment-supply-continuity/` 建立接口。
