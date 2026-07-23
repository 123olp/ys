# 科技树 Web 候选参考包

本参考包服务于 Human Infra 的“目的 -> 永生 / 记忆编辑”交互式研究科技树。它把外部候选拆成视觉骨架、依赖解锁、科研证据、成熟度门禁和实现引擎，不把任何单一站点当作完整模板。

## 组合结论

```text
Calitree 的节点状态与进度环
  -> Tree 的前置依赖、逐级点亮和战争迷雾
  -> Path of Exile 的大图缩放与路径高亮
  -> roadmap.sh 的节点详情与资源组织
  -> NASA TRL 的成熟度门禁
  -> ProbKnow、3ie、ORKG、MIRA 的主张—论文—证据结构
  -> React Flow + ELK/Dagre 的工程实现
```

正式产品采用纵向有向无环图、可审计点亮条件、专业研究配色、右侧证据抽屉和论文来源跳转，不复制候选站点的品牌和内容。

## 状态

| 状态 | 含义 |
|---|---|
| `research_snapshot_complete` | 已完成公开页面结构与交互研究 |
| `raw_capture_complete` | WARC、响应、渲染 DOM、截图和哈希均已生成 |
| `raw_capture_partial` | 只取得部分原始资产 |
| `raw_capture_blocked` | 环境、登录墙或站点策略阻止原始采集 |
| `reference_only` | 只用于概念参考，禁止复制实现或资产 |

结构化候选见 `candidates.json`，逐站研究见 `site-notes.md`，交互契约见 `interaction-patterns.md`，逐站状态见 `capture-status.json`。采集工具位于 `../../../tools/tech-tree-reference-capture/`，原始输出位于被 Git 忽略的 `build/reference-captures/tech-tree/`。

## 选定候选

`Historical Tech Tree` 已选为主要视觉与交互参考，并进入专项完整镜像流程。其 Windows 抓取入口、离线闭合方式、完整性证据和许可边界见 `../../../tools/tech-tree-reference-capture/CAPTURE-CONTRACT.md`；第三方资产继续只保存在本地研究快照目录，不进入正式产品源码。

原始镜像固定在 `20260723T214152Z` 批次，本地优化副本位于
`D:\.projects\human-infra-reference-captures\historical-tech-tree\optimized-source`。
原版预览使用 `http://localhost:18779/`，优化版使用
`http://localhost:18780/`。优化副本拥有独立 Git 历史，基线提交
`577e2af`，性能修复提交 `6e1e4bf`；详细对照证据见优化副本的
`DEBUG.md`。
