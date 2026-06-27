# arxiv-html-paper 工具包说明

`tools/arxiv-html-paper/` 是 arXiv HTML papers 前端框架的可复用模板包，配合 `tools/arxiv_html_paper_tool.py` 使用。

## 目录结构

```text
arxiv-html-paper/
├── AGENTS.md
├── CHANGELOG.md
├── CONSUMER_GUIDE.md
├── CONTRACT.md
├── GOVERNANCE.md
├── MAINTENANCE.md
├── README.md
├── VERSION
├── arxiv-html-paper.contract.v1.json
├── assets/
│   └── static/browse/0.3.4/images/icons/
└── templates/
    ├── PaperReaderLayout.astro
    └── paper.astro
```

## 职责边界

- `templates/PaperReaderLayout.astro` 复用 arXiv HTML papers 的资源路径、顶栏、目录、阅读模式、明暗主题、反馈 modal 和底部结构。
- `templates/paper.astro` 提供最小 `ltx_*` 论文页面骨架，用占位符接收标题、作者、摘要、分类和关键词。
- `assets/` 只保存镜像工具可能漏下、但布局会引用的小型图标补丁资源。
- `CONTRACT.md` 和 `arxiv-html-paper.contract.v1.json` 定义其他项目可依赖的稳定消费契约。
- `CONSUMER_GUIDE.md` 面向外部项目消费，说明复制、安装、验证、升级和故障处理。
- `GOVERNANCE.md` 规定版本等级、评审门禁、资源治理和发布清单。
- `MAINTENANCE.md` 面向维护者，记录镜像刷新、资源安装、模板升级和发布验证。
- `VERSION` 与 `CHANGELOG.md` 记录工具包版本和演进历史。
- 本目录不保存下载来的 CSS、JS 或字体；这些资源通过 CLI 从镜像安装到目标项目 `public/`。
- 本目录不保存 Human Infra 的具体正文；正文在目标项目页面里维护。

## 维护规则

- 修改布局模板前，先和真实 arXiv HTML paper 页面做结构与样式对照。
- 不在模板里新增自定义视觉系统；复用目标是保持 arXiv HTML papers 读者框架。
- 占位符统一使用 `{{NAME}}` 形式，由 CLI 渲染。
- 新增模板时必须同步更新 `README.md` 和 `tools/arxiv_html_paper_tool.py`。
- 改变命令、默认路径、DOM 类、状态属性、localStorage 键或资源版本时，必须同步更新契约、版本和变更记录。
- 面向其他项目的使用方法必须先写入 `CONSUMER_GUIDE.md`，再在 README 中放入口。
