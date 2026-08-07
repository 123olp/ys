# 永生史展示与出版架构

本文说明 Human Infra《永生史》从资料整理到时间轴展示、再到叙事出版物的分层结构。

## 1. 分层原则

展示和出版不能直接消费全部原始资料，必须先经过资料分层：

```text
raw_timeline（全部资料）
  -> works_subset（作品子集）
    -> local_review（本地复核）
      -> fresh_review（独立审阅）
        -> narrative（出版物正文）
```

| 层 | 文件 | 作用 | 是否可被正文引用 |
| --- | --- | --- | --- |
| 原始年表 | `timeline.json` | 检索、扩充、补录、复核工作台 | 否 |
| 作品子集 | `works-subset.v1.json` | 明确第一版出版候选范围 | 否 |
| 本地复核 | `works-review-register.v1.json` | 记录来源可达性和本地结论 | 部分 |
| 出版物 | `docs/publications/` | 对外/内部叙事正文 | 必须达到对应 `review_gate` |

## 2. 时间轴展示方式

当前采用 ECharts 图表作为增强展示层，psql ASCII 表格作为核心资料层，不再回退到 TimelineJS 全量叙事渲染。

`preview.html` 提供三档范围：

1. `全部资料`：显示 `timeline.json` 中全部 2592 条事件，用于资料巡检。
2. `作品子集`：只显示 `works-subset.v1.json` 中 400 条候选事件，用于作品编辑。
3. `本地已复核`：只显示 `verification_status=locally_reviewed` 的事件，用于审阅推进。

每档都必须显示 `evidence_grade`、`verification_status`、`event_id` 和来源链接，避免把未复核资料误读为出版结论。

预览页遵循 `Design.md` 的零美化语义界面：默认浏览器渲染、psql ASCII 文本表格作为资料事实来源、ECharts 只作为增强视图。`preview.js` 按需加载 `timelinejs.json`，提供按路径族散点、年代密度、时间窗口，以及图表上方的单行 psql 当前事件阅读器。路径族展示使用中文标签，但 `timeline.json` 仍保留英文机器值。

页面布局把事件阅读器置于最上方，时间轴图表紧随其后，查询条件放在图表下方；路径族概览、范围与复核状态、资料说明和已复核事件列表折叠在下方资料区块中。

## 3. 出版物入口

`publication-manifest.v1.json` 是展示和出版的机器契约，定义四类出版物：

| publication_id | 类型 | review_gate | 当前状态 |
| --- | --- | --- | --- |
| `pub-history-timeline` | 交互时间轴 | `locally_reviewed` | working_draft |
| `pub-history-narrative` | 永生史正文 | `fresh_reviewed` | working_draft |
| `pub-health-handbook` | 健康手册 | `none` | working_draft |
| `pub-effective-immortality-guide` | 永生指南 | `none` | working_draft |

规则：

- 时间轴预览可以展示全部资料，但必须同时展示复核状态。
- 叙事正文只允许引用达到自身 `review_gate` 的事件。
- 健康手册和指南不依赖历史年表子集，但仍按各自证据制度维护。

## 4. 当前缺口

- `works-subset.v1.json` 400 条中仅 31 条完成本地复核。
- `fresh_reviewed` 尚未开放，因此 `pub-history-narrative` 还不能视为可发布正文。
- 后续应继续推进本地复核，并在独立 fresh review 后把事件状态推进到 `fresh_reviewed`，再更新叙事正文。
