# Consumer Guide

本文档说明其他项目如何消费 arXiv HTML Paper Reuse Kit。目标是让一个 Astro 项目快速获得 arXiv HTML papers 同款阅读器框架，而不是重新设计论文页。

## 适用对象

适合：

- 研究论文式长文。
- 理论谱系、模型契约、资料综述和参考文献页。
- 需要目录、阅读模式、明暗主题和论文语义结构的页面。

不适合：

- 营销首页。
- 仪表盘主界面。
- 自定义品牌视觉优先的站点。
- 需要自动从 LaTeX 生产完整 HTML 的流水线。

## 复制工具包

从 Human Infra 仓库复制：

```text
tools/arxiv_html_paper_tool.py
tools/arxiv-html-paper/
```

目标仓库应保持：

```text
target-repo/
├── tools/
│   ├── arxiv_html_paper_tool.py
│   └── arxiv-html-paper/
└── web/
    ├── public/
    └── src/
```

如果目标 Astro 应用不叫 `web/`，用 `--web-root` 指定实际路径。

## 准备镜像

在目标仓库打印推荐下载命令：

```bash
python3 tools/arxiv_html_paper_tool.py print-mirror-command
```

推荐把镜像放入 `.research/`：

```text
.research/arxiv-html/<paper-id>/wget/
.research/arxiv-html/<paper-id>/monolith/
```

`.research/` 是研究缓存，不是运行时代码。目标仓库通常应在 `.gitignore` 中忽略它。

## 一键脚手架

```bash
python3 tools/arxiv_html_paper_tool.py scaffold \
  --web-root web \
  --source .research/arxiv-html/2606.26689v1/wget \
  --title "Research Paper Title" \
  --author "Research Group" \
  --arxiv-id "local.paper.0001" \
  --category "cs.HC" \
  --force
```

生成结果：

```text
web/
├── public/
│   ├── static/browse/0.3.4/
│   └── use.typekit.net/
└── src/
    ├── layouts/PaperReaderLayout.astro
    └── pages/paper.astro
```

## 分步安装

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

只写页面：

```bash
python3 tools/arxiv_html_paper_tool.py write-page \
  --target web/src/pages/paper.astro \
  --layout-target web/src/layouts/PaperReaderLayout.astro \
  --title "Research Paper Title" \
  --author "Research Group" \
  --arxiv-id "local.paper.0001" \
  --category "cs.HC" \
  --force
```

## 验证

安装后执行：

```bash
python3 tools/arxiv_html_paper_tool.py verify-assets --public-dir web/public
```

需要给 CI 或其他脚本消费时：

```bash
python3 tools/arxiv_html_paper_tool.py verify-assets --public-dir web/public --json
```

成功条件：

```text
ok: true
required_paths_present == required_paths_total
typekit_font_file_count >= 10
```

这一步只验证资源，不验证阅读器 DOM 和控件。凡是你改过 layout、把外部 HTML 注入 `PaperReaderLayout`、写了 post-process、或生成本地静态预览，都必须再做浏览器级检查：

```text
页面存在 .ltx_page_navbar > nav.ltx_TOC
目录项数量大于 0
页面存在 .ltx_document、.ltx_abstract、.ltx_bibliography
点击目录按钮后 documentElement.dataset.tocDisplay 会在 none/block 间切换
移动端宽度下目录按钮仍可切换
DOM 中没有重复 class 属性
```

不要只看“正文能显示”。arXiv reader 的目录、阅读模式和主题按钮依赖固定 DOM 契约；正文可见但 `.ltx_page_navbar > nav.ltx_TOC` 缺失时，目录控件会静默失效。

## 内容维护

目标项目只维护正文内容：

```text
web/src/pages/paper.astro
```

建议保留 `ltx_*` 语义类，以便后续承接 LaTeXML、Pandoc 或其他论文转换工具。不要把 Human Infra 的正文复制进模板；模板只做结构，正文属于消费项目。

如果消费项目从数据库、Markdown、LaTeXML 片段或其他 HTML 生成页面，推荐使用原生 `templates/paper.astro` 的 `slot="toc"` 和正文 slot，而不是只向 layout 传一个完整正文字符串。未被 layout 消费的 props 不能当作功能已经存在的证据。

## 升级流程

1. 在目标仓库创建干净版本点。
2. 复制新版 `tools/arxiv_html_paper_tool.py` 和 `tools/arxiv-html-paper/`。
3. 阅读 [CHANGELOG.md](CHANGELOG.md) 与 [CONTRACT.md](CONTRACT.md)。
4. 运行 `verify-assets`。
5. 如需刷新布局，运行 `write-layout --force`。
6. 不要用 `write-page --force` 覆盖已经人工维护过的正文，除非确认要重建页面。
7. 运行目标仓库构建、截图或 smoke test。

## 常见问题

### 页面样式没有加载

检查目标项目是否从 `public/` 根路径服务资源，并运行：

```bash
python3 tools/arxiv_html_paper_tool.py verify-assets --public-dir web/public
```

### Typekit 或字体出现 404

重新执行 `install-assets`。安装过程会把下载镜像中的查询串字体文件归一化到：

```text
use.typekit.net/font-files/*.woff2
```

运行时不应访问 `p.typekit.net`。

### 底部黑色浮动控件从哪里来

这是 arXiv HTML papers 阅读器框架自带控件，来自复用的 CSS/JS/DOM 结构，不是消费项目单独添加的组件。

### 目录按钮点击后没反应

先检查 DOM，而不是先改 CSS：

```text
.ltx_page_navbar > nav.ltx_TOC
html[data-toc-display]
button 或控件点击后 data-toc-display 是否变化
```

常见根因是页面生成时只注入正文，绕过了 `slot="toc"`，导致 `.ltx_TOC` 不在 `.ltx_page_navbar` 下。另一个常见根因是 HTML post-process 追加 class 时生成了重复 `class` 属性，浏览器解析后丢失了框架需要的语义类。

### 需要完全换视觉风格

不要在本工具包里改。另建目标项目自己的布局；本工具包的价值是稳定复用 arXiv HTML papers 论文阅读器。
