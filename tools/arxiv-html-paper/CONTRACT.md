# arXiv HTML Paper Reuse Contract

状态：active  
契约版本：1.0.0  
机器可读版本：[arxiv-html-paper.contract.v1.json](arxiv-html-paper.contract.v1.json)

本契约定义其他项目消费 `tools/arxiv-html-paper/` 和 `tools/arxiv_html_paper_tool.py` 时可以依赖的稳定边界。它约束的是前端阅读器框架复用，不约束具体论文正文。

## 稳定接口

可复制对象：

```text
tools/arxiv_html_paper_tool.py
tools/arxiv-html-paper/
```

稳定 CLI 命令：

```text
print-mirror-command
install-assets
verify-assets
write-layout
write-page
scaffold
```

默认目标结构：

```text
<astro-app>/
├── public/
│   ├── static/browse/0.3.4/
│   └── use.typekit.net/
└── src/
    ├── layouts/PaperReaderLayout.astro
    └── pages/paper.astro
```

稳定模板占位符：

```text
{{LAYOUT_IMPORT}}
{{TITLE}}
{{AUTHOR}}
{{DATE_LABEL}}
{{ARXIV_ID}}
{{CATEGORY}}
{{ABSTRACT}}
{{KEYWORDS}}
```

## DOM 与运行时契约

消费项目必须保留 arXiv HTML papers 的语义骨架：

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

阅读器状态由这些属性表达：

```text
data-theme
data-toc-display
data-reading-mode
```

浏览器持久化键保持为：

```text
ar5iv_theme
arxiv_html_paper_toc_display
arxiv_html_paper_reading_mode
```

这些类、属性和键属于兼容边界。修改它们必须按破坏性变更处理。

## 资产契约

`verify-assets` 必须通过。核心资源包括：

```text
static/browse/0.3.4/css/ar5iv.0.8.5.css
static/browse/0.3.4/css/arxiv-html-papers-20260131.css
static/browse/0.3.4/css/arxiv-html-papers-theme-20250131.css
static/browse/0.3.4/js/arxiv-html-papers-20260131.js
static/browse/0.3.4/images/arxiv-logo-one-color-white.svg
static/browse/0.3.4/images/icons/*
use.typekit.net/utz6mli.css
use.typekit.net/font-files/*.woff2
```

Typekit 字体在安装阶段归一化为本地 `.woff2` 文件。运行时不应再请求 `p.typekit.net` 或远端 Typekit CSS。

## 消费方义务

- 将下载镜像放在 `.research/` 或其他缓存目录，并按目标仓库规则决定是否忽略。
- 将安装后的静态资源从目标项目 `public/` 根路径提供服务。
- 安装或升级后运行 `verify-assets`。
- 只把正文、标题、作者、摘要、章节和参考文献当作目标项目内容维护。
- 不直接修改复制来的 arXiv CSS、JS、字体文件；需要变化时先升级本工具包契约。
- 遵守目标项目对第三方静态资源、字体和来源标注的许可要求。

## 提供方保证

- CLI 只使用 Python 标准库。
- 模板不包含 Human Infra 的具体正文。
- 模板默认面向 Astro 静态站点。
- 安装后的页面不依赖 arXiv 或 Typekit 运行时网络请求。
- 小型 fallback 图标资源从 `assets/` 自动补齐。

## 非目标

- 不负责 `.tex -> HTML` 转换；需要时接入 LaTeXML。
- 不负责 PDF 生成。
- 不提供 React、Vue、Svelte 或非 Astro 适配器。
- 不做品牌视觉重设计。
- 不验证论文内容、研究结论或医学事实。

## 版本规则

- Patch：文档修正、校验信息补充、小型 fallback 资源补齐，不改变命令和 DOM。
- Minor：新增非破坏性 CLI 参数、模板占位符或校验项。
- Major：改变默认目录、重命名命令、改变 DOM 类/属性、替换 arXiv 资源版本、改变目标框架。

## 验收标准

```bash
python3 tools/arxiv_html_paper_tool.py verify-assets --public-dir web/public
python3 tools/arxiv_html_paper_tool.py verify-assets --public-dir web/public --json
```

在项目级交付前，还应运行目标仓库自己的构建或检查命令。
