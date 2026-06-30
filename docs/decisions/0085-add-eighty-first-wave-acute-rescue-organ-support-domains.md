# 0085 Add Eighty-First Wave Acute Rescue Organ Support Domains

Date: 2026-07-01

## Status

Accepted

## Context

Human Infra 已经覆盖 EMS、手术麻醉、血液/器官、毒理、卒中/TBI 和长期身体系统，但有效永生 / 主体持续性最大化还需要单独拆出“急性死亡边界”中的可逆救援链。心脏骤停、脓毒症休克、创伤出血、ICU 多器官支持、呼吸衰竭、ECMO、急性肾损伤、输血、大量过量/中毒和严重烧伤都具有独立的时间窗、设备依赖、组织能力、结局指标和禁止用途。

如果这些只被塞进通用 `emergency-medical-services-prehospital-care/`、`surgical-anesthesia-perioperative-safety/`、`blood-organ-tissue-biovigilance-transplantation/` 或 `chemical-safety-poison-control-toxicology/`，模型会丢失“突然中断事件如何被转化为可逆窗口”的结构。

## Decision

新增第八十一波急性救援与临时器官支持研究域：

- `cardiac-arrest-cpr-defibrillation-continuity/`
- `sepsis-shock-early-recognition-resuscitation-continuity/`
- `trauma-system-hemorrhage-control-continuity/`
- `intensive-care-organ-support-delirium-continuity/`
- `mechanical-ventilation-respiratory-failure-continuity/`
- `ecmo-extracorporeal-life-support-continuity/`
- `acute-kidney-injury-renal-replacement-continuity/`
- `transfusion-blood-management-hemorrhage-continuity/`
- `overdose-poisoning-reversal-toxicology-continuity/`
- `burn-injury-critical-care-rehabilitation-continuity/`

每个域只建立 `README.md` 和 `AGENTS.md`，用于定义先验位置、对象、Human Infra 模型链路、非目标和 Source Signals。暂不创建数据目录、临床协议、算法评分、个人风险预测、急救流程或工具脚本。

## Consequences

- 急性死亡边界从“急救/临床服务”总桶中拆出，进入可独立审查的研究域。
- `docs/reference/domain-map.md`、`research-domain-atlas.md`、`research-domain-radar.md`、`applications-and-literature.md` 和 `ethics-and-safety-boundaries.md` 必须同步新增索引与边界。
- `tools/check_repository.py` 必须把新增域和 ADR 纳入结构门禁。
- 公开表达必须持续强调：这些域是研究、建模和证据边界，不是 CPR、除颤、抗生素、ICU、呼吸机、ECMO、透析、输血、中毒处理、烧伤处理或个案医疗建议。

## Source Signals

- AHA CPR and ECC Guidelines: https://cpr.heart.org/en/resuscitation-science/cpr-and-ecc-guidelines
- Surviving Sepsis Campaign: https://www.sccm.org/clinical-resources/guidelines/guidelines/surviving-sepsis-guidelines-2021
- WHO Emergency Care: https://www.who.int/health-topics/emergency-care
- SCCM ICU Liberation: https://www.sccm.org/clinical-resources/iculiberation-home
- ATS/ESICM/SCCM Mechanical Ventilation Guideline: https://www.thoracic.org/statements/resources/cc/mechanical-ventilation-ards.pdf
- ELSO Guidelines: https://www.elso.org/ecmo-resources/elso-ecmo-guidelines.aspx
- KDIGO Acute Kidney Injury: https://kdigo.org/guidelines/acute-kidney-injury/
- AABB Clinical Practice Guidelines: https://www.aabb.org/news-resources/resources/clinical-practice-guidelines
- Poison Help: https://www.poisonhelp.org/
- WHO Burns: https://www.who.int/news-room/fact-sheets/detail/burns
