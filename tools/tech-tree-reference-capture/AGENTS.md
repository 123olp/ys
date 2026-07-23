# 科技树候选采集工具

本目录编排成熟命令行工具，负责候选网页的可重复采集、哈希和状态输出，不解析或复刻第三方业务代码。

```text
tech-tree-reference-capture/
├── AGENTS.md  # 工具职责与边界
├── CAPTURE-CONTRACT.md # Historical Tech Tree 完整抓取与证据契约
├── README.md  # 使用方法和输出契约
├── build_standalone_viewer.py # 将候选清单嵌入单文件元页面
├── capture.sh # wget、Chrome 与 sha256sum 编排入口
├── capture-historical-tech-tree.ps1 # Windows 真实站点抓取、落盘、重放和打包总控
├── historical-tech-tree-browser.mjs # Chrome/CDP 资源发现和交互门禁
├── import_workflow_reference.py # 导入既有 Windows 工作流参考快照
├── verify_historical_capture.py # 图数据、文件闭合和逐文件哈希审计
└── viewer/
    └── index.html # 单端口候选切换、外站预览与评估元页面
```

候选批量入口的输入是 `docs/reference/tech-tree-web-candidates/candidates.json`；Historical Tech Tree 专项入口在 Windows 上抓取真实站点。输出进入被 Git 忽略的研究快照目录，每次运行必须使用不可覆盖的批次目录。导入器只处理其他项目的工作流参考，不得把参考对象冒充目标对象。不得绕过登录、验证码、付费墙、robots 或访问控制，不得将第三方 HTML、CSS、JavaScript 自动导入 `web/`。
