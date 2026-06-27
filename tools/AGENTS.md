# tools 目录说明

`tools/` 保存仓库维护脚本和可迁移工程工具。这里的脚本不是产品运行时代码，默认从仓库根目录执行，也应尽量保持可复制到其他仓库使用。

## 目录结构

```text
tools/
├── AGENTS.md                         # 本目录架构说明
├── README.md                         # 工具入口和常用命令
├── arxiv_html_paper_tool.py          # arXiv HTML papers 复用 CLI
├── check_repository.py               # 仓库结构和 Markdown 链接检查
└── arxiv-html-paper/
    ├── AGENTS.md                     # arXiv 复用工具包说明
    ├── README.md                     # 安装、校验和脚手架命令
    ├── assets/                       # 小型补丁静态资源
    └── templates/
        ├── PaperReaderLayout.astro   # 论文阅读器布局模板
        └── paper.astro               # 最小论文页面骨架
```

## 职责边界

- `check_repository.py` 只检查仓库结构、临时文件名、Python 缓存和本地 Markdown 链接。
- `arxiv_html_paper_tool.py` 只负责 arXiv HTML papers 资源安装、资产校验、Astro 布局和页面骨架生成。
- `arxiv-html-paper/templates/` 保留可复制模板，不承载 Human Infra 正文理论。
- 工具脚本应优先使用 Python 标准库；只有外部工具本身是任务对象时，才在文档中要求 `wget`、`monolith`、`LaTeXML` 等依赖。

## 维护规则

- 新增工具必须更新 `tools/README.md` 和本文件。
- 新增工具包目录必须有自己的 `AGENTS.md` 和 `README.md`。
- 工具默认不得写入个人数据、医疗数据或远程服务凭据。
- 面向全局复用的工具不得硬编码 Human Infra 正文内容；项目特有内容只能作为示例或调用参数存在。
