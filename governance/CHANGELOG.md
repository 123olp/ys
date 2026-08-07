---
id: GOV-CHANGELOG
type: changelog
status: current
owner: engineering
created: 2026-08-06
last_reviewed: 2026-08-06
review_cycle: P90D
---

# 治理包变更记录

- 初始化治理包。
- 新增永生史历史年表治理标准、机器契约 `control-plane/history-timeline-contract.v1.yaml`、GATE-0002/GATE-0003，并接入 `make history-timeline-gate` 与 GitHub CI。
- 新增 ADR-0001：历史年表采用可复核数据管线与成熟发布工具组合；完成 TimelineJS、PeriodO、Wikibase、Neatline 等数字人文工具成熟度调研，并把推荐链写入 `docs/reference/history-timeline/TOOLS.md`。
- 完成年表首版结构化：`timeline.json` 61 条事件、`sources.json` 58 个来源卡、`periods.json` 21 个时期定义，并新增 `make history-timeline-preview` 生成 TimelineJS 原型；机器门禁升级为引用式来源/时期契约。
