# 科技树 Web 候选资料

本目录保存 Human Infra 交互式研究科技树的外部参考研究、状态与复用边界，不保存第三方站点镜像，也不直接定义正式产品实现。

```text
tech-tree-web-candidates/
├── AGENTS.md              # 目录职责、依赖和维护边界
├── README.md              # 候选组合结论与阅读入口
├── candidates.json        # 候选站点、适配度和来源清单
├── capture-status.json    # 研究快照与原始抓取批次状态
├── interaction-patterns.md # 节点、边、状态、详情和证据交互契约
└── site-notes.md          # 逐站视觉、数据和许可观察
```

上游输入是公开站点、官方文档和 `tools/tech-tree-reference-capture/` 生成的本地证据；下游是 Human Infra 路线图的信息架构与交互设计。`candidates.json` 负责候选事实，`capture-status.json` 负责执行状态，二者不得互相替代。第三方原始 HTML、CSS、JavaScript、图片、WARC 和 ZIP 只能进入被 Git 忽略的 `build/reference-captures/` 或 Windows 外部快照目录。
