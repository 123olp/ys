# arxiv-html-paper 工具包说明

`tools/arxiv-html-paper/` 是 arXiv HTML papers 前端框架的可复用模板包，配合 `tools/arxiv_html_paper_tool.py` 使用。

## 目录结构

```text
arxiv-html-paper/
├── AGENTS.md
├── README.md
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
- 本目录不保存下载来的 CSS、JS 或字体；这些资源通过 CLI 从镜像安装到目标项目 `public/`。
- 本目录不保存 Human Infra 的具体正文；正文在目标项目页面里维护。

## 维护规则

- 修改布局模板前，先和真实 arXiv HTML paper 页面做结构与样式对照。
- 不在模板里新增自定义视觉系统；复用目标是保持 arXiv HTML papers 读者框架。
- 占位符统一使用 `{{NAME}}` 形式，由 CLI 渲染。
- 新增模板时必须同步更新 `README.md` 和 `tools/arxiv_html_paper_tool.py`。
