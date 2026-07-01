# C2 可能性源体维护层 目录说明

## 目录结构

```text
c2-source-maintenance/
├── AGENTS.md
├── README.md
└── <research-domain>/
    ├── AGENTS.md
    └── README.md
```

## 职责边界

- 本目录是 `C2` 研究域的物理容器，不是独立研究域。
- 本目录不承载证据正文、论文、数据或脚本；这些内容留在具体研究域目录中。
- `C2` 的判定真相源是 `../_possibility-space-control/classification.tsv`。

## 维护规则

- 移入或移出研究域时，先更新分类表，再执行目录移动。
- 不在本目录创建与具体研究域同级的临时资料、草稿或脚本。
- 若分级规则变化，优先更新 `_possibility-space-control/rubric.md`，再批量迁移。
