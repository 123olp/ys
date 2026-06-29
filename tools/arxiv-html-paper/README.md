# arXiv HTML Paper Reuse Kit

本工具包把 arXiv HTML papers 的前端阅读器框架沉淀成可迁移工具：下载镜像进入目标 `public/`，写入 `PaperReaderLayout.astro`，生成最小 `ltx_*` 论文页面骨架，并校验 CSS、JS、图标和 Typekit 字体资源是否齐全。

当前版本见 [VERSION](VERSION)。稳定消费边界见 [CONTRACT.md](CONTRACT.md) 和 [arxiv-html-paper.contract.v1.json](arxiv-html-paper.contract.v1.json)。

## 文档入口

| 文档 | 用途 |
| --- | --- |
| [CONTRACT.md](CONTRACT.md) | 人读消费契约：稳定接口、DOM 边界、资产要求和非目标 |
| [arxiv-html-paper.contract.v1.json](arxiv-html-paper.contract.v1.json) | 机器可读契约：给脚本、CI 或其他项目索引使用 |
| [CONSUMER_GUIDE.md](CONSUMER_GUIDE.md) | 其他项目复制和使用本工具包的操作指南 |
| [GOVERNANCE.md](GOVERNANCE.md) | 维护治理：版本等级、评审门禁、资源治理和发布清单 |
| [MAINTENANCE.md](MAINTENANCE.md) | 维护运行手册：镜像刷新、资源安装、模板升级和故障处理 |
| [CHANGELOG.md](CHANGELOG.md) | 工具包版本变更记录 |

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

`verify-assets` 只证明资源齐全，不证明阅读器控件可用。涉及 layout、TOC、HTML 注入、post-process 或静态预览时，还必须做浏览器级断言：`.ltx_page_navbar > nav.ltx_TOC` 存在、目录项存在、`.ltx_document` / `.ltx_abstract` / `.ltx_bibliography` 存在、点击目录按钮后 `data-toc-display` 会变化。

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

完整迁移步骤见 [CONSUMER_GUIDE.md](CONSUMER_GUIDE.md)。

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
│   ├── static/browse/0.3.4/
│   └── use.typekit.net/
│       ├── font-files/
│       └── utz6mli.css
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
use.typekit.net/font-files/*.woff2
```

## 实现边界

- 复用 arXiv HTML papers 的前端资源和 DOM 协议。
- 不重写 CSS、JS、主题系统和阅读器控件。
- 保留原生 TOC slot 结构和 `.ltx_page_navbar > nav.ltx_TOC`；不要只注入正文来绕过阅读器 DOM 契约。
- Typekit 字体会从下载镜像归一化为稳定本地 `.woff2`，不保留 `p.typekit.net` 统计 CSS 作为运行时依赖。
- 不把 Human Infra 正文写入模板。
- 不自动从 LaTeX 生成正文；页面内容仍由目标项目维护。
- 破坏性变更必须更新 [CONTRACT.md](CONTRACT.md)、机器可读契约和 [CHANGELOG.md](CHANGELOG.md)。
