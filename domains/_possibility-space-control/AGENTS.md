# AGENTS.md

## 目录结构

```text
_possibility-space-control/
├── AGENTS.md
├── README.md
├── classification.tsv
├── rubric.md
└── summary.md
```

## 职责边界

- 本目录是 `domains/` 的元索引控制面，不是普通研究域。
- `classification.tsv` 负责把全部正式研究域映射到 C1-C6；C0 作为价值核不分配普通研究域。
- `rubric.md` 负责定义分层标尺、判定顺序、边界案例和禁止误用。
- `summary.md` 负责统计各层数量、列出需要人工复核的高影响域和维护状态。

## 维护规则

- 不按近期可行性、证据成熟度、商业化时间或实现难度给研究域降级。
- 优先按“对主体可能性空间的边界、规模、持续时间、未来选择权的控制力”判定。
- 远期思想实验、时间差分、主体连续性、脑保存和有效永生相关路径可以高于近期可执行干预。
- 默认分类可以是 v0.1 初筛，但必须保留 `review_status` 字段，避免把自动归类误写成最终哲学判决。
- 新增、删除或重命名研究域时，必须同步更新 `classification.tsv`、`summary.md` 和必要的根/域索引。
