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
- 完成年表扩录与日期补齐：`timeline.json` 2592 条事件、`sources.json` 2602 个来源卡、`periods.json` 31 个时期定义；预览切换为 ECharts 图表模式，并新增 `works-subset.v1.json` 与 `works-review-register.v1.json`。
- 完成首批本地复核：31/400 条作品子集事件标记为 `locally_reviewed`，同步修正 McCay、Klass、Hayflick、HeLa、Dolly、CRISPR 2016 与日本 iPS 监管报道等来源/证据问题。
- 新增展示与出版层：`publication-manifest.v1.json` 与 `PUBLICATION.md` 定义原始资料、作品子集、复核登记和出版物四层关系；时间轴预览增加“全部资料 / 作品子集 / 本地已复核”三档范围。
- 优化时间轴查看与阅读：`preview.html` 不再内嵌全量数据，改为按需加载 `timelinejs.json`；新增按路径族散点、年代密度、时间窗口、事件详情、图表上方的单行 psql 事件阅读器，并生成独立 `timeline-events.psql.txt` 全量表格。
- 调整时间轴页面布局：事件阅读器置顶，时间轴图表紧随其后，查询条件位于图表下方；路径族概览、范围与复核状态、资料说明和已复核事件列表折叠在下方。
