# web 目录说明

`web/` 是 Human Infra 的 Observable Framework Web 应用目录，用于把科研叙事、书籍转译、预测模型和可视化组织成可发布的多页站点。

## 目录结构

```text
web/
├── AGENTS.md                    # 本目录架构说明
├── README.md                    # 运行方式、页面职责和边界
├── observablehq.config.js        # Observable Framework 配置
├── package.json                  # Web 应用依赖与脚本
└── src/
    ├── index.md                  # 首页：项目主张、书籍入口、模型摘要
    ├── book.md                   # 《奇点更近》学习资料转译
    ├── model.md                  # 预测模型交互页
    ├── research-standards.md     # 科研标准和工具链页
    ├── style.css                 # Framework 自定义样式
    ├── components/
    │   └── model.js              # D3 / Observable Plot 组件
    └── data/
        └── book-signals.json     # 书籍观点到 Human Infra 变量的映射
```

## 职责边界

- `src/*.md` 是页面真相源，使用 Observable Framework 的 Markdown、`grid`、`card`、响应式图表和代码块。
- `src/components/model.js` 只保存可复用的演示计算和图表组件，不保存页面长文。
- `src/data/` 保存 Web 展示所需的小型结构化数据，不保存原始研究数据、医疗数据或个人数据。
- `web/dist/` 是构建产物，不进入版本库。
- 根目录 `singularity-human-infra.html` 保留为历史静态专项页；新的正式 Web 版本以 `web/` 为主。

## 维护规则

- 新增页面时，必须同步更新 `observablehq.config.js` 的 `pages` 和本文件目录结构。
- 新增图表时，优先使用 Observable Plot；只有机制图、网络图、阈值仪表等自定义图形才使用 D3。
- 页面中的预测模型必须保留用途边界：研究展示、变量解释、群体级路径位移，不输出个体死亡日期。
- 任何从书籍、论文或网页引入的观点必须标明它是学习资料、转译、假设还是研究标准。
- 引入新的前端依赖前，先确认 Observable Framework / D3 / Observable Plot 是否已经足够。
