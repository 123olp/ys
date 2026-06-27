# Human Infra Web

`web/` 是 Human Infra 的正式 Web 应用目录，采用 Astro + D3 组织科研叙事、书籍转译、预测模型和交互图表。

Astro 负责页面结构、长文叙事、组件化和静态发布；D3 负责机制图、预测有效寿命曲线、LEV 阈值和模型状态读数。MDX 已作为内容层能力接入，后续可用于资料卡片和长文研究页。

## 目录结构

```text
web/
├── AGENTS.md
├── README.md
├── astro.config.mjs
├── package.json
├── public/
│   ├── static/browse/0.3.4/
│   └── use.typekit.net/
│       ├── font-files/
│       └── utz6mli.css
└── src/
    ├── components/
    │   ├── Hero.astro
    │   ├── MetricGrid.astro
    │   └── SectionHeader.astro
    ├── data/
    │   └── book-signals.json
    ├── layouts/
    │   ├── PaperReaderLayout.astro
    │   └── ResearchLayout.astro
    ├── pages/
    │   ├── index.astro
    │   ├── paper.astro
    │   ├── book.astro
    │   ├── model.astro
    │   └── research-standards.astro
    ├── scripts/
    │   └── model-charts.js
    └── styles/
        └── global.css
```

## 页面职责

- `src/pages/index.astro`：首页，把《奇点更近》学习资料、Human Infra 主体持续性和预测模型放在同一个叙事入口。
- `src/pages/paper.astro`：arXiv HTML papers 风格论文页，用学术阅读器展示 Human Infra 的理论、模型和工具链。
- `src/pages/book.astro`：书籍介绍与 Human Infra 转译，承载章节主线、技术链路和边界说明。
- `src/pages/model.astro`：交互预测模型页，展示寿命、有效时间、主观时间、相对时间和未来选择权的模型位置。
- `src/pages/research-standards.astro`：科研标准页，记录论文阅读、预测模型报告、因果推断、可视化和工具链标准。
- `src/scripts/model-charts.js`：D3 图表和模型计算脚本，只表达演示模型，不输出个体死亡日期。
- `public/static/browse/0.3.4/`、`public/use.typekit.net/`：从 arXiv HTML papers 页面下载并复用的 CSS、JS、图标、webmanifest 和归一化 Typekit 字体资源。
- `src/data/book-signals.json`：书籍观点到 Human Infra 变量的结构化映射。

arXiv-style 论文页的可复用工具链已经沉淀在 [`../tools/arxiv-html-paper/`](../tools/arxiv-html-paper/README.md)。校验当前资源：

```bash
python3 tools/arxiv_html_paper_tool.py verify-assets --public-dir web/public
```

## 正式路线

仓库根目录里的单文件 HTML 只保留为历史原型或快速展示，不再作为新增交互页面的默认位置。

新增 Web 内容按下面顺序进入：

```text
资料卡片
  -> 结构化数据
  -> 页面叙事
  -> D3 组件
  -> 构建校验
```

页面分工保持清晰：

| 页面 | 主要任务 | 不承载 |
| --- | --- | --- |
| `index.astro` | 对外解释 Human Infra 与专项资料的整体价值 | 细节方法论堆叠 |
| `paper.astro` | 承载论文式理论、定义、谱系、模型契约和工具链说明 | 自定义论文阅读器样式或控件逻辑 |
| `book.astro` | 承载书籍、作者观点和 Human Infra 转译 | 模型参数实现 |
| `model.astro` | 承载生命路径、有效时间、主观时间、相对时间和未来选择权的模型可视化 | 医疗建议或个人结论 |
| `research-standards.astro` | 承载论文、工具、模型报告和可视化规范 | 宣传文案 |

实现优先级：

1. 先把外部资料做成 [资料卡片](../docs/reference/source-card-system.md)。
2. 再把卡片中的变量、技术信号和限制写入 `src/data/`。
3. 最后在 `src/scripts/` 或 `src/components/` 中实现可复用 D3 / Astro 组件。

## 本地运行

```bash
cd web
npm install
npm run dev -- --host 0.0.0.0 --port 18764
```

Windows 浏览器访问：

```text
http://localhost:18764/
```

构建静态站点：

```bash
cd web
npm run build
```

构建产物在 `web/dist/`，该目录不进入仓库。

## 设计边界

- 本目录是 Web 展示和研究解释层，不承载采集脚本、个人预测服务或医学决策逻辑。
- 预测模型图表只展示群体/模型层面的路径位移、阈值和预算变化。
- 正式研究结论必须回到 `docs/reference/` 的模型契约、证据政策和治理文档。
