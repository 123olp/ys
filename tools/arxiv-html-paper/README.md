# arXiv HTML Paper Reuse Kit

本工具包把 arXiv HTML papers 的前端阅读器框架沉淀成可迁移工具：下载镜像进入目标 `public/`，写入 `PaperReaderLayout.astro`，生成最小 `ltx_*` 论文页面骨架，并校验 CSS、JS、图标和 Typekit 字体资源是否齐全。

## 适用场景

- 在 Astro 项目里做 arXiv 同款论文阅读页。
- 把研究长文、理论谱系、模型契约和参考文献组织成论文式 Web 页面。
- 保留 arXiv HTML papers 的顶栏、侧边目录、阅读模式、明暗主题和反馈控件。

不适合：

- 普通营销页或仪表盘首页。
- 需要自定义品牌视觉系统的站点。
- 需要从 LaTeX 自动转 HTML 的完整生产流水线；那一层应接入 LaTeXML 或 Pandoc。

## 快速使用

从 Human Infra 仓库根目录执行：

```bash
python3 tools/arxiv_html_paper_tool.py verify-assets --public-dir web/public
```

在当前 `web/` Astro 应用里重新生成布局和页面：

```bash
python3 tools/arxiv_html_paper_tool.py scaffold \
  --web-root web \
  --source .research/arxiv-html/2606.26689v1/wget \
  --force
```

只安装资源：

```bash
python3 tools/arxiv_html_paper_tool.py install-assets \
  --source .research/arxiv-html/2606.26689v1/wget \
  --public-dir web/public
```

只写布局：

```bash
python3 tools/arxiv_html_paper_tool.py write-layout \
  --target web/src/layouts/PaperReaderLayout.astro \
  --force
```

只写页面骨架：

```bash
python3 tools/arxiv_html_paper_tool.py write-page \
  --target web/src/pages/paper.astro \
  --layout-target web/src/layouts/PaperReaderLayout.astro \
  --title "My Research Paper" \
  --author "Local Research Notes" \
  --force
```

## 迁移到其他 Astro 项目

复制下面两个对象到目标仓库：

```text
tools/arxiv_html_paper_tool.py
tools/arxiv-html-paper/
```

在目标仓库执行：

```bash
python3 tools/arxiv_html_paper_tool.py scaffold \
  --web-root path/to/astro-app \
  --source path/to/wget-mirror \
  --title "Research Paper Title" \
  --author "Research Group" \
  --arxiv-id "local.paper.0001" \
  --category "cs.HC" \
  --force
```

生成后目标项目应得到：

```text
path/to/astro-app/
├── public/
│   ├── p.typekit.net/
│   ├── static/browse/0.3.4/
│   └── use.typekit.net/
└── src/
    ├── layouts/PaperReaderLayout.astro
    └── pages/paper.astro
```

## 下载镜像命令

工具可以打印本轮采用的下载命令：

```bash
python3 tools/arxiv_html_paper_tool.py print-mirror-command
```

命令分工：

- `wget`：下载结构化资源镜像，用于复制 CSS、JS、图标和字体。
- `monolith`：生成单文件快照，用于视觉对照和离线归档。

## 必需资源

`verify-assets` 会检查：

```text
static/browse/0.3.4/css/ar5iv.0.8.5.css
static/browse/0.3.4/css/arxiv-html-papers-20260131.css
static/browse/0.3.4/css/arxiv-html-papers-theme-20250131.css
static/browse/0.3.4/js/arxiv-html-papers-20260131.js
static/browse/0.3.4/images/arxiv-logo-one-color-white.svg
static/browse/0.3.4/images/icons/apple-touch-icon.png
static/browse/0.3.4/images/icons/favicon-16x16.png
static/browse/0.3.4/images/icons/favicon-32x32.png
static/browse/0.3.4/images/icons/safari-pinned-tab.svg
static/browse/0.3.4/images/icons/site.webmanifest
use.typekit.net/utz6mli.css
p.typekit.net/p.css*
use.typekit.net/af/*/*/*/*
```

## 实现边界

- 复用 arXiv HTML papers 的前端资源和 DOM 协议。
- 不重写 CSS、JS、主题系统和阅读器控件。
- 不把 Human Infra 正文写入模板。
- 不自动从 LaTeX 生成正文；页面内容仍由目标项目维护。
