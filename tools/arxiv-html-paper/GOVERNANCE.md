# Governance

本文档规定 arXiv HTML Paper Reuse Kit 的维护规则。目标是让它成为可复制、可审查、可升级的工具包，而不是一次性页面补丁。

## 真相源

工具包真相源：

```text
tools/arxiv_html_paper_tool.py
tools/arxiv-html-paper/
```

契约真相源：

```text
tools/arxiv-html-paper/CONTRACT.md
tools/arxiv-html-paper/arxiv-html-paper.contract.v1.json
```

页面实现真相源：

```text
web/src/layouts/PaperReaderLayout.astro
web/src/pages/paper.astro
```

`web/` 中的实现是消费样例，不是工具包模板本身。模板变更必须先进入 `tools/arxiv-html-paper/templates/`，再由 CLI 写入目标项目。

## 维护原则

- 保持 arXiv HTML papers 的前端框架形态，不建立第二套视觉系统。
- 复用成熟工具：`wget` 负责结构化资源镜像，`monolith` 负责单文件视觉对照，LaTeXML 负责未来可能的 `.tex -> HTML`。
- 自研代码只做资源复制、字体归一化、模板渲染、资产校验和消费契约表达。
- 运行时资源必须本地化，避免页面依赖远端 arXiv 或 Typekit。
- 模板不得包含 Human Infra 正文，避免污染其他项目消费。

## 变更等级

Patch 变更：

- 文档修正。
- 说明补充。
- fallback 图标补齐。
- `verify-assets` 输出信息增强。
- 不改变命令、目录、DOM 类、状态键和视觉资源版本。

Minor 变更：

- 新增非破坏性 CLI 参数。
- 新增模板占位符。
- 新增校验项。
- 新增消费指南或维护脚本。
- 默认行为保持兼容。

Major 变更：

- 改变目标框架。
- 改变默认路径。
- 重命名 CLI 命令。
- 替换 arXiv HTML papers CSS/JS 主版本。
- 改变 `ltx_*` 语义骨架。
- 改变阅读器状态属性或 localStorage 键。

## 评审门禁

每次修改前检查：

```text
是否改变了消费契约
是否改变了 arXiv 原框架结构
是否引入运行时远端依赖
是否把项目正文写入模板
是否让其他 Astro 项目迁移更困难
```

每次修改后至少运行：

```bash
python3 tools/arxiv_html_paper_tool.py verify-assets --public-dir web/public
git diff --check
make check
```

如果修改模板或运行时交互，还应在浏览器中检查：

```text
/paper/
明暗主题切换
目录显示/隐藏
阅读模式
移动端宽度
字体是否无 404
```

## 资源治理

下载镜像默认进入 `.research/`，它是缓存和溯源材料，不是运行时产物。

目标项目应自行决定是否提交安装后的 `public/static/` 与 `public/use.typekit.net/`。如果提交，必须确认目标项目的许可证、字体许可和第三方资源标注策略。

禁止：

- 绕过来源站点访问控制。
- 将私有或受限资源打包进通用工具包。
- 删除 Typekit 许可说明头。
- 用自定义 CSS 覆盖来伪装成 arXiv 同款。

## 兼容策略

保持兼容的变更可以直接更新 `VERSION` 的 patch 或 minor 位。

破坏性变更必须：

1. 更新 `VERSION` major 位。
2. 新增 `arxiv-html-paper.contract.vN.json`。
3. 在 [CHANGELOG.md](CHANGELOG.md) 写明迁移步骤。
4. 保留旧契约文档或明确说明删除理由。
5. 在消费指南中写明升级风险。

## 发布清单

- [ ] `VERSION` 已更新。
- [ ] [CONTRACT.md](CONTRACT.md) 已同步。
- [ ] [arxiv-html-paper.contract.v1.json](arxiv-html-paper.contract.v1.json) 已同步。
- [ ] [CONSUMER_GUIDE.md](CONSUMER_GUIDE.md) 已同步。
- [ ] [MAINTENANCE.md](MAINTENANCE.md) 已同步。
- [ ] `tools/AGENTS.md` 和本目录 `AGENTS.md` 已同步。
- [ ] `verify-assets` 通过。
- [ ] `make check` 通过。
