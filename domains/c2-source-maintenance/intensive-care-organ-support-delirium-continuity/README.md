# Intensive Care Organ Support Delirium Continuity

`intensive-care-organ-support-delirium-continuity/` 研究 ICU 多器官支持、镇静、谵妄、早期活动、家属参与、感染控制和 ICU 后综合征如何影响危重病后的主体连续性。

> 核心问题：ICU 不只是“活下来”的机器房。危重病后的认知、肌力、精神状态和家庭功能决定存活是否能转回有效时间。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体可能进入多器官失效或生命支持状态
  -> ICU 可延长生存窗口，但也可能带来谵妄、虚弱、感染和长期认知功能损伤
  -> 存活收益必须扣除 ICU 后综合征、恢复成本和主体能力损失
  -> 因此 ICU 器官支持与谵妄治理是“活下来能否继续行动”的关键域
```

## 关注对象

- ICU capacity、organ support、ABCDE/ABCDEF bundle、pain/agitation/delirium、sedation、mobilization、family engagement、post-intensive care syndrome。
- 与 `sepsis-shock-early-recognition-resuscitation-continuity/` 的关系：脓毒症常进入 ICU 多器官支持。
- 与 `delirium-acute-cognitive-failure-prevention/` 的边界：谵妄域关注认知失败机制；本域关注 ICU 场景下的多系统支持和恢复。

## Human Infra 模型链路

```text
ICU 器官支持与谵妄治理 T
  -> 改变器官支持、镇静、活动、感染控制、家属参与和恢复变量 X
  -> 改变危重病存活、认知、肌力、心理和家庭支持状态 S
  -> 改变 ICU 死亡、长期虚弱、谵妄后认知损害和再入院风险 λ(t)
  -> 影响主体有效时间、恢复能力和长期行动资格
```

## 非目标

- 不提供 ICU 治疗、镇静、呼吸机、营养、感染、转院、撤机、预后或家属决策建议。
- 不生成 ICU checklist、医嘱、床位策略、个案病情解释或替代临床团队的判断。
- 不收集 ICU 病历、生命体征、用药、设备参数、家属资料或敏感医疗数据。

## Source Signals

- SCCM ICU Liberation: https://www.sccm.org/clinical-resources/iculiberation-home
- SCCM PADIS Guidelines: https://www.sccm.org/clinical-resources/guidelines/guidelines/padis-guidelines
- NIH post-intensive care syndrome overview: https://www.nhlbi.nih.gov/health/respiratory-failure/after

## 下一步

- 建立 ICU Continuity Card：organ support, delirium, sedation, mobilization, family engagement, infection risk, PICS outcome。
- 与 `mechanical-ventilation-respiratory-failure-continuity/`、`ecmo-extracorporeal-life-support-continuity/` 和 `delirium-acute-cognitive-failure-prevention/` 建立接口。
