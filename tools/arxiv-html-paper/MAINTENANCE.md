# Maintenance Runbook

本文档给维护者使用，处理镜像刷新、资产安装、模板升级和发布验证。

## 日常检查

```bash
python3 tools/arxiv_html_paper_tool.py verify-assets --public-dir web/public
python3 tools/arxiv_html_paper_tool.py verify-assets --public-dir web/public --json
```

如果 JSON 中 `ok` 为 `false`，先补资源，不要改页面样式。

## 刷新来源镜像

打印推荐命令：

```bash
python3 tools/arxiv_html_paper_tool.py print-mirror-command
```

用途分工：

```text
wget      -> 结构化资源镜像，用于复制 CSS/JS/图标/字体
monolith  -> 单文件快照，用于视觉对照和离线归档
```

镜像默认位置：

```text
.research/arxiv-html/2606.26689v1/wget/
.research/arxiv-html/2606.26689v1/monolith/
```

`.research/` 默认被仓库忽略。

## 安装资源

```bash
python3 tools/arxiv_html_paper_tool.py install-assets \
  --source .research/arxiv-html/2606.26689v1/wget \
  --public-dir web/public
```

安装会做三件事：

```text
复制 arXiv static/browse/0.3.4 资源
复制 use.typekit.net 资源
将 Typekit 查询串字体归一化为 font-files/*.woff2
```

安装后必须验证：

```bash
python3 tools/arxiv_html_paper_tool.py verify-assets --public-dir web/public
```

## 更新模板

模板源文件：

```text
tools/arxiv-html-paper/templates/PaperReaderLayout.astro
tools/arxiv-html-paper/templates/paper.astro
```

写入当前 Web 应用：

```bash
python3 tools/arxiv_html_paper_tool.py write-layout \
  --target web/src/layouts/PaperReaderLayout.astro \
  --force
```

生成新的页面骨架：

```bash
python3 tools/arxiv_html_paper_tool.py write-page \
  --target web/src/pages/paper.astro \
  --layout-target web/src/layouts/PaperReaderLayout.astro \
  --title "Research Paper Title" \
  --author "Research Group" \
  --force
```

注意：已经写过正文的页面不要直接 `write-page --force`，除非本轮目标就是重建正文。

## 模板变更准则

允许：

- 修复与真实 arXiv HTML papers 不一致的 DOM。
- 增加模板占位符。
- 修复可访问性或静态路径问题。
- 补充语义结构，让后续 LaTeXML/Pandoc 更容易接入。

禁止：

- 新增自定义品牌色、营销区块或卡片化视觉系统。
- 改写 arXiv reader JS 的行为。
- 在模板中写入 Human Infra 正文。
- 删除 `ltx_*` 语义类。

## 故障处理

### 缺少字体文件

现象：

```text
missing required paths:
  - use.typekit.net/font-files/*.woff2
```

处理：

```bash
python3 tools/arxiv_html_paper_tool.py install-assets \
  --source .research/arxiv-html/2606.26689v1/wget \
  --public-dir web/public
```

如果仍失败，说明 `wget` 镜像没有下载 Typekit `af/` 目录，需要重新下载镜像。

### 页面请求 p.typekit.net

运行时不应请求 `p.typekit.net`。重新安装资源后检查：

```text
web/public/use.typekit.net/utz6mli.css
```

其中字体路径应为：

```text
font-files/<name>.woff2
```

### 样式变了

先用 `monolith` 快照和真实 arXiv HTML 页面做视觉对照，再判断是否是资源缺失、模板漂移或上游版本变化。

## 发布验证

```bash
python3 tools/arxiv_html_paper_tool.py verify-assets --public-dir web/public
git diff --check
make check
```

涉及前端视觉时，追加浏览器检查：

```text
/paper/
顶部工具栏
侧边目录
明暗主题
阅读模式
字体加载
移动端滚动
```
