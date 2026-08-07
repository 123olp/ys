# 历史年表契约

## 1. 目的

本契约定义 Human Infra 永生史年表的结构化数据规则，保证年表可作为严肃历史证据基础设施被复用、复核、版本化与可视化。

## 2. 真相源

- 机器真相源：年表 JSON 文件，必须符合 `timeline.schema.json`。
- 来源真相源：`sources.json`，必须符合 `sources.schema.json`。
- 时期真相源：`periods.json`，必须符合 `periods.schema.json`。
- 人工可读底稿：`docs/source-notes/2026-08-06-human-immortality-research-major-events-timeline.md`。
- 公共作品：`docs/publications/history-of-immortality.md`，只引用已复核事件。
- 原文缓存：`.research/literature/`，git 忽略，不作为正文引用源。

正式数据文件：

```text
timeline.json   事件
sources.json    来源卡
periods.json    时期定义与 PeriodO 映射
works-subset.schema.json  作品子集 Schema
works-subset.v1.json  第一版作品子集登记
works-review-register.schema.json  本地复核登记 Schema
works-review-register.v1.json  首批本地复核登记
publication-manifest.schema.json  展示与出版清单 Schema
publication-manifest.v1.json  展示与出版机器契约
PUBLICATION.md  展示与出版架构说明
preview.js      图表交互与事件阅读增强脚本
preview-core.js 核心纯函数（浏览器与 Node 共用，可单测）
echarts.min.js  本地化 ECharts 图表运行时（第三方资产）
timeline-events.psql.txt  完整事件明细 psql 表格（生成物）
timelinejs.json  图表发布数据，保留 TimelineJS JSON 兼容结构（生成物）
timelinejs.light.json  图表与筛选用轻量发布数据，不含完整正文与来源链接（生成物）
preview.html     ECharts 图表模式预览页（生成物）
```

事件不得内嵌完整来源对象，必须通过 `sources` 数组引用 `sources.json` 中的 `source_id`。
`timelinejs.json`、`timelinejs.light.json` 和 `preview.html` 是发布生成物，任何事件数据变化后都必须通过 `make history-timeline-preview` 重新生成，并保持门禁一致。当前预览只使用图表模式，不再回退到 TimelineJS 全量叙事渲染；`preview.js` 先加载轻量数据用于图表、筛选和聚合，事件完整正文在初始化时自动从 `timelinejs.json` 加载并直接显示；核心纯函数从 `preview-core.js` 导入，ECharts 使用本地 `echarts.min.js`，不依赖外部 CDN。

`works-subset.v1.json` 只登记“进入作品化评审”的事件 ID，不表示复核通过；事件仍必须经历 `locally_reviewed` 和 `fresh_reviewed` 后才能进入 `published`。

`works-review-register.v1.json` 记录本地复核结论，必须与 `timeline.json` 的 `verification_status`、`works-subset.v1.json` 的计数保持一致。

`publication-manifest.v1.json` 定义展示与出版入口。时间轴展示可以包含全部资料，但必须持续显示复核状态；叙事出版物只能引用达到自身 `review_gate` 的事件。

## 3. 事件标识

事件 ID 格式：

```text
HIT-<三字母类别>-<三位序号>
```

示例：

```text
HIT-MTH-001   神话与宗教
HIT-TEC-002   技术事件
HIT-FAI-003   失败教训
```

类别代码：

| 代码 | 含义 |
| --- | --- |
| MTH | 神话与宗教 |
| THT | 思想与概念 |
| PRA | 实践与方法 |
| SCI | 科学与医学 |
| TEC | 技术与工程 |
| INS | 制度与机构 |
| LIT | 文学与作品 |
| FAI | 失败与教训 |
| DEM | 人口与统计 |
| POL | 政策与治理 |

## 4. 必填字段

每个事件必须包含：

```text
event_id
title
date_start
date_type
civilization
region
path_family
event_type
claim
summary
sources
evidence_grade
verification_status
status
```

事件创建时必须写入 `created_at`，任何实质修改必须更新 `updated_at` 和 `last_reviewed`。

## 5. 日期规则

- 日期使用 EDTF 或 ISO 8601 字符串。
- 无法精确断年时，使用 `date_type=approx`、`range` 或 `long_process`，不得伪造精确年份。
- `era` 用于长期文明阶段，例如“中世纪”“近现代”。
- 日期含义必须绑定事件本身的解释，不把文学传说写成史实。

## 6. 来源规则

- 每条来源必须有 `source_id`、类型、标题或标签、可访问 URL/DOI。
- 来源类型：`primary`、`secondary`、`tertiary`、`expert_narrative`。
- 证据分级沿用项目规则：`S` 史实、`M` 神话传说、`I` 思想学说、`T` 技术事件、`L` 失败教训。
- 一手史料与二手综述不得混为同一证据等级。
- 来源无法访问或只登记元数据时，状态保持 `blocked` 或 `needs_revision`。
- 同一来源可被多个事件引用，但必须先在 `sources.json` 注册一次；重复引用或疑似错源要在 `note` 中显式标注。

## 7. 路径族

事件必须映射到永生路径族之一：

```text
maintenance        生物维护
reconstruction     生物重建
suspension         生物暂停
digital_migration  数字迁移
cognitive_extension 认知外延
social_composite   社会复合
philosophical      哲学判据
cross_path         跨路径
```

`timeline.json` 的 `path_family` 必须保存英文机器值；中文标签只用于展示层映射。禁止把中文标签写回 `path_family` 字段。

## 8. 禁止用途

- 禁止把神话、文学或思想事件写成已验证史实。
- 禁止把动物实验、细胞实验或远期预测写成人体有效结论。
- 禁止把年表事件直接作为医疗、投资、法律或政策建议。
- 禁止删除来源、隐藏争议或把“待考证”升级为“已证明”。
- 禁止把单一来源的日期或解释当作权威终判。

## 9. 机器校验

每次新增或修改事件后，至少执行：

```bash
python3 -m json.tool docs/reference/history-timeline/example-events.json >/dev/null
```

正式门禁：

```bash
make history-timeline-gate
```

正式数据接入后，应使用 JSON Schema validator 检查：

```text
event_id 唯一
source_id 唯一（来源卡注册表内）
period_id 唯一（时期注册表内）
必填字段齐全
日期格式合法
事件 sources 全部指向已注册来源卡
事件 period_id 指向已注册时期
证据等级合法
路径族合法
verification_status 合法
```
