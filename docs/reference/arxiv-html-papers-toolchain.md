# arXiv HTML Papers Toolchain Analysis

本文档记录 `https://arxiv.org/html/2606.26689v1` 的页面工具链、下载方法、可复用结构和 Human Infra 复刻边界。

## 结论

目标页面不是普通静态博客模板，而是论文转换和阅读器系统：

```text
TeX / LaTeX source
  -> LaTeXML 0.8.8
  -> ltx_* semantic HTML / MathML / figures
  -> arXiv HTML papers scaffold
  -> ar5iv CSS + arXiv theme CSS + reader JS
  -> browser-side ToC / reading mode / theme / feedback controls
```

Human Infra 的 arXiv-style 页面应直接复用已下载的 arXiv HTML papers CSS、JS、图标、Typekit 字体和控件结构，只替换论文正文内容。

## 已核验来源

- 远端页面：`https://arxiv.org/html/2606.26689v1`
- 本地 SingleFile 快照：`<windows-home>/Downloads/An algebraic study of ideals of weak graph homomorphisms (2026_6_27 02：58：35).html`
- LaTeXML 官方站点：`https://dlmf.nist.gov/LaTeXML/`

目标页面头部包含生成信息：

```text
Generated on Thu Jun 25 07:17:29 2026 by LaTeXML (version 0.8.8)
```

## 页面资源

远端 HTML 入口加载的核心资源：

```text
/static/browse/0.3.4/css/arxiv-html-papers-20260131.css
/static/browse/0.3.4/js/arxiv-html-papers-20260131.js
https://use.typekit.net/utz6mli.css
```

本地实现使用下载镜像中的 Typekit 字体，但会把查询串字体 URL 归一化为稳定的本地 `.woff2` 文件，避免 Astro/Vite 静态服务把 `%3F` 路径解析成 404：

```text
/use.typekit.net/utz6mli.css
/use.typekit.net/font-files/*.woff2
```

主 CSS 再导入：

```text
ar5iv.0.8.5.css
arxiv-html-papers-theme-20250131.css
```

正文结构的关键类：

```text
arxiv-html-header
ltx_page_navbar
ltx_TOC
ltx_page_main
ltx_page_content
ltx_document
ltx_title_document
ltx_abstract
ltx_section
ltx_bibliography
```

阅读器状态由 HTML 属性表达：

```text
data-theme="light|dark"
data-toc-display="block|none"
data-reading-mode="enabled|disabled"
```

浏览器持久化键：

```text
ar5iv_theme
arxiv_html_paper_toc_display
arxiv_html_paper_reading_mode
```

## 本地下载工具链

本轮使用两个成熟工具下载，用途不同：

```bash
monolith --isolate --ignore-errors --timeout 120 \
  --output .research/arxiv-html/2606.26689v1/monolith/2606.26689v1.singlefile.html \
  https://arxiv.org/html/2606.26689v1
```

`monolith` 用于生成单文件、可归档、可离线视觉对照的 HTML 快照。

```bash
wget --page-requisites --convert-links --adjust-extension --span-hosts \
  --domains=arxiv.org,static.arxiv.org,use.typekit.net \
  --no-parent --wait=0.2 --timeout=30 --tries=2 \
  --directory-prefix=.research/arxiv-html/2606.26689v1/wget \
  https://arxiv.org/html/2606.26689v1
```

`wget` 用于生成结构化资源镜像，便于单独分析 CSS、JS、图片和字体请求。

本机已存在：

```text
wget
monolith
pandoc
```

本机未安装：

```text
latexml / latexmlc
httrack
```

后续如果需要从 `.tex` 直接生产 HTML paper，应补充 `LaTeXML`。如果需要更完整的网站递归镜像，可再引入 `HTTrack`，但当前单页复刻不需要增加该依赖。

## Human Infra 复用方案

正式实现采用：

```text
Astro route /paper/
  -> PaperReaderLayout.astro
  -> public/static/browse/0.3.4/css/arxiv-html-papers-20260131.css
  -> public/static/browse/0.3.4/js/arxiv-html-papers-20260131.js
  -> ltx_* semantic content
```

保留：

- arXiv HTML papers 的整体信息架构。
- `ltx_*` 语义类，方便后续承接 LaTeXML/Pandoc 生成内容。
- 顶部工具栏、侧边目录、阅读模式、目录切换、明暗主题。
- 论文式标题、作者、摘要、章节、图表、公式、参考文献。

替换：

- 原论文正文和图片。

不替换：

- arXiv HTML papers 的 CSS/JS 资源。
- 顶栏控件结构。
- 目录、阅读模式、明暗主题和反馈 modal 的原始交互形式。

## 已沉淀工具

本项目已把复用流程沉淀为仓库工具：

```text
tools/arxiv_html_paper_tool.py
tools/arxiv-html-paper/
```

工具职责：

- `print-mirror-command`：打印 `wget` 与 `monolith` 镜像命令。
- `install-assets`：从 `wget` 镜像复制 arXiv CSS、JS、图标和 Typekit 字体到目标项目 `public/`，并把 Typekit 查询串字体资源归一化为稳定 `.woff2`。
- `verify-assets`：校验目标项目是否具备核心 arXiv HTML papers 资源。
- `write-layout`：写入 `PaperReaderLayout.astro`。
- `write-page`：写入最小 `ltx_*` 论文页面骨架。
- `scaffold`：一次完成资源安装、布局写入、页面生成和资产校验。

当前项目校验命令：

```bash
python3 tools/arxiv_html_paper_tool.py verify-assets --public-dir web/public
```

## 消费契约与治理文档

arXiv HTML paper 复用能力已经沉淀为可被其他项目复制的工具包。稳定消费入口：

```text
tools/arxiv-html-paper/CONTRACT.md
tools/arxiv-html-paper/arxiv-html-paper.contract.v1.json
tools/arxiv-html-paper/CONSUMER_GUIDE.md
tools/arxiv-html-paper/GOVERNANCE.md
tools/arxiv-html-paper/MAINTENANCE.md
```

文档分工：

- [消费契约](../../tools/arxiv-html-paper/CONTRACT.md)：稳定 CLI、模板占位符、DOM 类、状态属性、资产路径和非目标。
- [机器可读契约](../../tools/arxiv-html-paper/arxiv-html-paper.contract.v1.json)：供 CI、脚本或外部项目索引使用。
- [消费指南](../../tools/arxiv-html-paper/CONSUMER_GUIDE.md)：外部 Astro 项目的复制、安装、验证和升级步骤。
- [维护治理](../../tools/arxiv-html-paper/GOVERNANCE.md)：版本等级、评审门禁、资源治理和发布清单。
- [维护手册](../../tools/arxiv-html-paper/MAINTENANCE.md)：镜像刷新、资产安装、模板升级和故障处理。

迁移到其他 Astro 项目时，复制：

```text
tools/arxiv_html_paper_tool.py
tools/arxiv-html-paper/
```

然后执行：

```bash
python3 tools/arxiv_html_paper_tool.py scaffold \
  --web-root path/to/astro-app \
  --source path/to/wget-mirror \
  --title "Research Paper Title" \
  --author "Research Group" \
  --force
```

工具边界：

- 只复用前端阅读器框架，不负责生成研究正文。
- 只安装本地静态资源，不在运行时依赖 arXiv 或 Typekit 外链；`p.typekit.net` 的统计 CSS 不进入运行时资源链。
- 只生成 Astro 页面，不替代 LaTeXML 的 `.tex -> HTML` 转换流水线。
- `wget` 镜像未必下载所有 favicon 变体；工具包用 `tools/arxiv-html-paper/assets/` 保存小型补丁图标，安装时自动补齐。

## 后续升级

1. 安装并验证 `LaTeXML`，用最小 `.tex` 样例生成 HTML。
2. 设计 Human Infra paper frontmatter，统一标题、作者、日期、关键词、分类和参考文献。
3. 将长文研究资料先写成 Markdown/MDX 或 LaTeX，再转为 `ltx_*` 兼容 HTML。
4. 把 `/paper/` 与 `/model/` 连接：论文页负责论证，模型页负责交互实验。
5. 对 mobile、dark mode、reading mode、ToC collapse 做 Playwright 截图回归。
