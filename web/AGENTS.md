# web 目录说明

`web/` 是 Human Infra 的 Astro + D3 Web 应用目录，用于把科研叙事、书籍转译、预测模型和可视化组织成可发布的多页站点。

## 目录结构

```text
web/
├── AGENTS.md                    # 本目录架构说明
├── README.md                    # 运行方式、页面职责和边界
├── astro.config.mjs             # Astro 配置
├── package.json                 # Web 应用依赖与脚本
└── src/
    ├── components/              # Astro 页面组件
    ├── data/                    # 小型结构化展示数据
    ├── layouts/                 # 页面布局
    ├── pages/                   # Astro 路由页面
    ├── scripts/                 # D3 图表和交互脚本
    └── styles/                  # 全局视觉系统
```

## 职责边界

- `src/pages/*.astro` 是页面真相源，负责叙事结构、页面路由和内容组织。
- `src/scripts/model-charts.js` 保存演示计算和 D3 图表逻辑，不保存页面长文。
- `src/components/` 保存可复用的 Astro 页面组件。
- `src/data/` 保存 Web 展示所需的小型结构化数据，不保存原始研究数据、医疗数据或个人数据。
- `web/dist/` 是构建产物，不进入版本库。
- 根目录 `singularity-human-infra.html` 保留为历史静态专项页；新的正式 Web 版本以 `web/` 为主。

## 维护规则

- 新增页面时，必须同步更新 `README.md` 和本文件目录结构。
- 新增图表时，优先复用 `src/scripts/model-charts.js` 的模型计算和 D3 绘图约定。
- 页面中的预测模型必须保留用途边界：研究展示、变量解释、群体级路径位移，不输出个体死亡日期。
- 任何从书籍、论文或网页引入的观点必须标明它是学习资料、转译、假设还是研究标准。
- 引入新的前端依赖前，先确认 Astro / MDX / D3 是否已经足够；复杂状态管理再评估 Svelte islands 或 React islands。
