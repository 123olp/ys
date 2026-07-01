# Sepsis Shock Early Recognition Resuscitation Continuity

`sepsis-shock-early-recognition-resuscitation-continuity/` 研究脓毒症、感染性休克、早期识别、抗感染窗口、液体/血流动力学复苏、ICU 转入和质量改进如何影响急性死亡风险。

> 核心问题：脓毒症是感染、免疫、循环和器官功能同时失控的系统性死亡边界。它需要被建模为时间关键型多器官失效风险，而不是普通感染。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体可被感染诱发的全身炎症、休克和器官衰竭快速终止
  -> 生存依赖早期识别、病原控制、复苏、监测和 ICU 支持
  -> 延迟识别会让可逆感染进入不可逆多器官失效
  -> 因此脓毒症与休克是感染风险进入主体持续性模型的急性失效域
```

## 关注对象

- Sepsis screening、shock、SOFA/qSOFA、time-to-treatment、source control、ICU admission、bundle compliance、mortality、post-sepsis syndrome。
- 抗微生物耐药、感染控制、诊断质量、血流动力学监测和器官支持之间的耦合。
- 与 `antimicrobial-resilience/` 的边界：抗菌韧性关注药物与耐药；本域关注感染进入休克和多器官失效后的急性救援链。
- 与 `intensive-care-organ-support-delirium-continuity/` 的关系：脓毒症常是 ICU 多器官支持入口。

## Human Infra 模型链路

```text
脓毒症早识别与复苏 T
  -> 改变筛查、诊断延迟、抗感染窗口、源控制和器官支持变量 X
  -> 改变休克逆转、多器官功能、ICU 病程和恢复状态 S
  -> 改变急性死亡、长期虚弱和认知功能下降风险 λ(t)
  -> 影响主体存活、恢复能力和有效时间
```

## 非目标

- 不提供感染诊断、抗生素选择、液体复苏、升压药、ICU 转诊或个体治疗建议。
- 不生成临床路径、医嘱、triage 决策、风险评分或替代 Surviving Sepsis / 医院方案。
- 不收集个案生命体征、实验室结果、培养报告、用药、病历或 ICU 资料。

## Source Signals

- Surviving Sepsis Campaign: https://www.sccm.org/clinical-resources/guidelines/guidelines/surviving-sepsis-guidelines-2021
- CDC Sepsis: https://www.cdc.gov/sepsis/
- WHO Sepsis: https://www.who.int/news-room/fact-sheets/detail/sepsis

## 下一步

- 建立 Sepsis Rescue Card：infection signal, organ dysfunction, shock, time-to-treatment, source control, ICU support, recovery burden。
- 与 `antimicrobial-resilience/`、`clinical-laboratory-diagnostic-quality/` 和 `intensive-care-organ-support-delirium-continuity/` 建立接口。
