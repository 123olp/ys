# Human Infra Core Literature Pack

本目录记录 Human Infra 谱系研究的第一批论文集。目标不是堆论文，而是把论文变成可进入项目的 Source Card：每篇资料都要说明它支持什么变量、机制、模型位置和边界。

## 本地缓存

原文缓存位置：

```text
.research/literature/human-infra-genealogy/
├── core-12/
├── adjunct/
└── methods/
```

`.research/` 已被仓库忽略；这里的 Markdown 只保存可追踪清单和卡片草案。

## 当前文件

- `2026-06-28-human-infra-genealogy-download-manifest.md`：核心论文、扩展谱系、方法论文的下载状态、合法获取边界、local path 和下一步。
- `2026-06-28-human-infra-core-12-source-card-pack.md`：首批 12 篇的 Source Card 草案。
- `reading-reports/`：论文 Markdown 解读报告，按 Human Infra 谱系层级分类。

## 使用顺序

1. 先读 download manifest，确认哪些是 PDF、HTML、metadata-only。
2. 再读 Source Card pack，理解每篇进入 Human Infra 的位置。
3. 再读 `reading-reports/README.md`，按谱系层级进入论文解读。
4. 精读后把高价值条目拆成单篇 research card。
5. 只有经过复核的结论才能晋升到 `docs/reference/`、`docs/explanations/` 或 Web 页面。

## 下载边界

- 允许：arXiv、PMC/开放 HTML、出版方开放 PDF、作者或机构公开页面。
- 记录但不绕过：付费墙、Cloudflare、登录墙、下载挑战、机构订阅限制。
- PMC 直接 PDF 或出版社 PDF 若返回浏览器校验页，不保存为论文 PDF；改存 article HTML 或合法公开副本。
- Public course copy、repository copy、mirror copy 必须在 manifest 中标明来源等级，不能当作 canonical publisher source。
