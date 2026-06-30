# 0086 Add Eighty-Second Wave Acute Internal Medicine Emergency Domains

Date: 2026-07-01

## Status

Accepted

## Context

Human Infra 已经覆盖心脏骤停、脓毒症休克、创伤出血、ICU、机械通气、ECMO、AKI/RRT、输血、中毒和烧伤这些急性死亡边界，但有效永生 / 主体持续性最大化还需要拆出一组“进入骤停、ICU 或不可逆损伤之前”的急性内科可逆窗口。

急性冠脉综合征、急性心衰失代偿、心律失常/晕厥、静脉血栓栓塞/肺栓塞、高血压危象、糖尿病高低血糖危象、过敏性休克、哮喘/COPD 急性加重、急性消化道出血和产科出血/高血压急症都可能在小时级或天级内改变死亡风险、失能风险、有效时间和未来选择权。

如果这些只被塞进 `cardiovascular-resilience/`、`endocrine-hormonal-regulation/`、`respiratory-oxygenation/`、`maternal-newborn-child-development/` 或第八十一波 ICU 域，模型会丢失“临床急性窗口如何在不可逆失效前被识别、接入、稳定、转运和恢复”的中间层。

## Decision

新增第八十二波急性内科与时间关键急症研究域：

- `acute-coronary-syndrome-reperfusion-continuity/`
- `acute-heart-failure-decompensation-continuity/`
- `cardiac-arrhythmia-syncope-decompensation-continuity/`
- `venous-thromboembolism-pulmonary-embolism-continuity/`
- `hypertensive-crisis-end-organ-risk-continuity/`
- `diabetic-hyperglycemic-hypoglycemic-crisis-continuity/`
- `anaphylaxis-allergic-emergency-continuity/`
- `asthma-copd-exacerbation-airway-continuity/`
- `acute-gastrointestinal-bleeding-endoscopy-continuity/`
- `obstetric-emergency-hemorrhage-hypertension-continuity/`

每个域只建立 `README.md` 和 `AGENTS.md`，用于定义先验位置、对象、Human Infra 模型链路、非目标和 Source Signals。暂不创建临床评分、分诊工具、个体预测、治疗流程、参数推荐、数据采集或自动化脚本。

## Consequences

- 第八十二波把“尚未进入骤停或 ICU 但已高度时间敏感”的急性内科窗口独立出来。
- `docs/reference/domain-map.md`、`research-domain-atlas.md`、`research-domain-radar.md`、`applications-and-literature.md` 和 `ethics-and-safety-boundaries.md` 必须同步新增索引与边界。
- `tools/check_repository.py` 必须把新增域和 ADR 纳入结构门禁。
- 公开表达必须持续强调：这些域是研究、建模和证据边界，不是胸痛、心衰、晕厥、肺栓塞、高血压危象、糖尿病危象、过敏、气道急症、消化道出血或产科急症的个案医疗建议。

## Source Signals

- AHA/ACC ACS guideline signals: https://www.heart.org/
- AHA/ACC/HFSA heart failure guideline signals: https://professional.heart.org/
- AHA/ACC/HRS atrial fibrillation and syncope guideline signals: https://professional.heart.org/
- ESC pulmonary embolism guideline signals: https://www.escardio.org/
- AHA high blood pressure guideline signals: https://professional.heart.org/
- ADA hyperglycemic crises consensus signals: https://diabetesjournals.org/
- World Allergy Organization / NIAID anaphylaxis signals: https://www.worldallergy.org/ and https://www.niaid.nih.gov/
- GINA / GOLD airway exacerbation signals: https://ginasthma.org/ and https://goldcopd.org/
- ACG gastrointestinal bleeding guideline signals: https://gi.org/
- ACOG / WHO obstetric emergency signals: https://www.acog.org/ and https://www.who.int/
