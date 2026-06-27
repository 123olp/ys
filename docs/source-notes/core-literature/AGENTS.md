# core-literature 目录说明

`docs/source-notes/core-literature/` 保存 Human Infra 谱系论文集的可追踪清单和 Source Card 草案。

## 目录结构

```text
core-literature/
├── AGENTS.md
├── README.md
├── reading-reports/
│   ├── AGENTS.md
│   ├── README.md
│   ├── 01-observation-personal-informatics/
│   ├── 02-aging-healthspan-biology/
│   ├── 03-survival-causal-models/
│   ├── 04-digital-twin-life-path/
│   ├── 05-cognition-identity-augmentation/
│   ├── 06-neuroethics-bci/
│   ├── 07-visualization-research-ui/
│   ├── 08-ai-risk-governance/
│   └── _original/
├── 2026-06-28-human-infra-genealogy-download-manifest.md
└── 2026-06-28-human-infra-core-12-source-card-pack.md
```

## 职责边界

- 本目录记录论文、网页、开放 PDF、公开课程副本、公共仓储副本和 metadata-only 条目的来源、下载状态、Human Infra 映射和后续处理动作。
- 原文缓存放在 `.research/literature/human-infra-genealogy/`，不进入 Git。
- `reading-reports/` 保存论文解读报告，按 Human Infra 谱系层级分类，不按下载顺序堆放。
- 本目录不替代稳定参考文档；稳定结论应晋升到 `docs/reference/` 或 `docs/explanations/`。
- Source Card 目前是草案包；精读完成后可拆成单篇卡片。

## 维护规则

- 新增论文前先判断它属于 core、adjunct、methods 还是 backlog。
- 不绕过付费墙、登录墙、验证码或下载挑战；无法合法下载全文时记录 metadata-only。
- Public course copy、repository copy、mirror copy 必须明确标注，不能伪装成 canonical publisher PDF。
- 每条资料必须写清楚模型位置、证据角色和迁移边界。
