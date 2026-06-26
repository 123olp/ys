# Human Infra Web

`web/` 是 Human Infra 的正式 Web 应用目录，采用 Observable Framework 组织科研叙事、预测模型和交互图表。

## 目录结构

```text
web/
├── AGENTS.md
├── README.md
├── observablehq.config.js
├── package.json
└── src/
    ├── index.md
    ├── book.md
    ├── model.md
    ├── research-standards.md
    ├── style.css
    ├── components/
    │   └── model.js
    └── data/
        └── book-signals.json
```

## 页面职责

- `src/index.md`：首页，把《奇点更近》学习资料、Human Infra 主体持续性和预测模型放在同一个叙事入口。
- `src/book.md`：书籍介绍与 Human Infra 转译，承载章节主线、技术链路和边界说明。
- `src/model.md`：交互预测模型页，展示寿命、有效时间、主观时间、相对时间和未来选择权的模型位置。
- `src/research-standards.md`：科研标准页，记录论文阅读、预测模型报告、因果推断、可视化和工具链标准。
- `src/components/model.js`：图表和模型计算组件，只表达演示模型，不输出个体死亡日期。
- `src/data/book-signals.json`：书籍观点到 Human Infra 变量的结构化映射。

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
