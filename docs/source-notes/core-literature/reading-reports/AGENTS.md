# reading-reports 目录说明

`reading-reports/` 保存 Human Infra 谱系论文的 Markdown 解读报告。这里是精读工作台，不是稳定结论层。

## 目录结构

```text
reading-reports/
├── AGENTS.md
├── README.md
├── 01-observation-personal-informatics/
├── 02-aging-healthspan-biology/
├── 03-survival-causal-models/
├── 04-digital-twin-life-path/
├── 05-cognition-identity-augmentation/
├── 06-neuroethics-bci/
├── 07-visualization-research-ui/
├── 08-ai-risk-governance/
└── _original/
```

## 职责边界

- 本目录保存论文解读、材料完整性判断、三遍阅读记录和迁移建议。
- 稳定结论必须晋升到 `docs/reference/` 或 `docs/explanations/` 后才能作为项目主张使用。
- 论文原文缓存仍在 `.research/literature/human-infra-genealogy/`，本目录只保存解读报告。
- `_original/` 只保存原始包索引，不能作为当前分类真相源。

## 维护规则

- 新增解读报告时，按 Human Infra 谱系层级归类，不按下载顺序堆放。
- 如果论文缓存状态更新，只在 `README.md` 或对应报告中注明，不直接改写论文结论。
- 不把 URL-only 报告当作完整审稿结论；必须标注材料不足和证据边界。
- 拆分、晋升或引用报告时，保留原始文件名中的编号，便于回溯到核心论文集。
