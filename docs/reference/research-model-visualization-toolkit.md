# Research Model and Visualization Toolkit

本文档沉淀 Human Infra 定量模型与 Web 可视化的科研化方法：如何读论文、选工具、建模型、画图、审查和迭代。

它服务于两个页面和三类文档：

- `singularity-human-infra.html`：面向传播和学习的专项展示页。
- `human-infra-dashboard.html`：生命路径预测模型的交互看板。
- `web/`：基于 Observable Framework 的正式多页科研叙事与交互模型应用。
- `docs/explanations/life-path-prediction-model.md`、`docs/reference/life-path-prediction-model-contract.md`、`docs/reference/life-path-prediction-model-governance.md`：模型说明、契约和治理。

## 1. 工作目标

Human Infra 的定量层不应停留在“好看的模拟图”。它应逐步变成一套研究型模型系统：

```text
研究问题
  -> 文献证据
  -> 因果问题定义
  -> 生存/持续时间模型
  -> 校准与验证
  -> 可视化表达
  -> 审查与治理
  -> Web 展示
```

静态页面可以保留交互原型；正式 Web 主线进入 `web/`，逐步把“展示用参数”升级为“研究问题、证据等级、估计目标、模型族和验证指标”。

## 2. 论文阅读与资料处理标准

### 2.1 三遍阅读法

采用 S. Keshav 的三遍阅读法作为基本流程：

| 遍数 | 目标 | Human Infra 输出 |
| --- | --- | --- |
| 第一遍 | 看标题、摘要、引言、结论和图表，判断是否相关 | `候选文献`，只记录主题和可能用途 |
| 第二遍 | 读方法、关键图表和证据链，判断是否可用 | `证据摘录`，记录模型、数据、边界和假设 |
| 第三遍 | 复现推理，检查限制和反证条件 | `稳定引用`，进入模型契约或治理文档 |

每篇核心论文必须回答五个问题：

```text
它研究什么问题？
它定义了什么变量、结局和时间范围？
它用了什么数据、设计和模型？
它的结论能迁移到 Human Infra 哪个变量？
它的失败条件和不能迁移的边界是什么？
```

### 2.2 证据进入模型前的分层

| 层级 | 可进入位置 | 不能做什么 |
| --- | --- | --- |
| 机制合理性 | 概念图、理论说明 | 不能当作寿命效应估计 |
| 动物/体外数据 | 证据背景 | 不能直接外推到人类健康寿命 |
| 人体早期数据 | 候选参数范围 | 不能作为稳定个体预测 |
| 队列/注册数据 | 风险模型、关联分析 | 不能自动解释为干预因果效应 |
| RCT / 目标试验模拟 | 干预效应估计 | 仍需适用人群、随访期和外部验证 |
| 长期死亡率/健康寿命 | 模型核心证据 | 仍需处理竞争风险、选择偏差和可及性 |

## 3. 文献脊梁

### 3.1 预测模型报告与偏差审查

| 主题 | 核心资料 | 用途 |
| --- | --- | --- |
| 预测模型报告 | TRIPOD / TRIPOD+AI | 规范说明样本、预测目标、候选变量、建模方法、性能和外部验证 |
| 偏差风险 | PROBAST / PROBAST+AI | 审查参与者、预测因子、结局、分析和适用性偏差 |
| 临床 AI 研究 | CONSORT-AI, SPIRIT-AI, DECIDE-AI | 约束 AI 干预、临床试验、早期临床评估和人机流程 |

Human Infra 使用方式：

```text
每个预测模型必须声明：
population
intervention / exposure
comparator
outcome
horizon
data source
model family
validation method
prohibited use
```

### 3.2 因果推断与目标试验

| 主题 | 核心资料 | 用途 |
| --- | --- | --- |
| 目标试验模拟 | Hernan / Robins target trial emulation | 把观察性数据问题改写为理想随机试验规格 |
| 因果图 | DAG / SCM / do-calculus | 明确混杂、中介、碰撞变量和不可识别路径 |
| 时间变化混杂 | Marginal structural models, g-methods | 处理健康状态、治疗选择和风险随时间共同演化 |
| 动态策略 | Dynamic treatment regimes / optimal regimes | 建模不同时间点采用不同策略的长期结果 |

Human Infra 使用方式：

```text
技术 T 不能直接写成“延寿变量”。
必须先写成：
T -> X_t -> state transition / hazard / observation / policy -> S(t)
```

### 3.3 生存分析与生命路径模型

| 模型族 | 适用问题 | Human Infra 映射 |
| --- | --- | --- |
| Kaplan-Meier / Nelson-Aalen | 基础生存曲线和累计风险 | 生命路径基线展示 |
| Cox / AFT | 协变量对事件时间的影响 | 干预或状态变量对死亡/失能风险的影响 |
| Restricted Mean Survival Time | 固定时间窗内的生存时间积分 | 比“某岁死亡”更适合表达有效时间差 |
| Competing risks | 多种互斥事件 | 死亡、失能、重大疾病、事故等竞争风险 |
| Multi-state models | 状态转移 | 健康、慢病、失能、恢复、死亡之间的路径 |
| Joint models | 纵向指标 + 事件时间 | 生物标志物、可穿戴数据和事件风险联动 |

推荐把当前“分布位移”升级为多层输出：

```text
baseline survival curve
intervention survival curve
restricted mean effective time
state occupancy probability
competing cumulative incidence
LEV ratio
resource budget delta
```

### 3.4 可视化理论

| 主题 | 核心资料 | 用途 |
| --- | --- | --- |
| Grammar of Graphics | Wilkinson | 把数据、尺度、几何对象、坐标系和图层分开 |
| D3 | Bostock et al. Data-Driven Documents | 自定义交互图、机制图、状态图和精确 SVG 控制 |
| Vega-Lite / Altair | Declarative visualization grammar | 可复现图表规格、研究图和仪表板原型 |
| Observable Plot | Observable 官方工具 | 快速生成解释型统计图 |
| Munzner nested model | Visualization design and validation | 从任务、数据、编码、算法四层验证可视化设计 |

Human Infra 的前端策略：

```text
自定义机制图 / 特殊交互：D3
标准统计图 / 快速探索：Vega-Lite / Observable Plot / Altair
研究报告图：优先声明式规格
传播页主图：D3 + 明确叙事
```

## 4. 工具栈建议

### 4.1 论文检索与研究自动化

| 工具 | 用途 | 进入仓库的方式 |
| --- | --- | --- |
| Stanford How to Read a Paper | 论文阅读流程 | 作为人工阅读标准 |
| Supervisor-Skills | 多代理监督、任务拆分和技能协作参考 | 借鉴研究任务的 supervisor / worker 模式 |
| academic-research-skills-codex | Codex 学术研究技能集合 | 借鉴论文检索、综述、阅读和写作 workflow |
| Auto-claude-code-research-in-sleep | 长时间自动研究流水线参考 | 借鉴 overnight research / batch research 的任务容器思想 |
| Semantic Scholar / OpenAlex / PubMed / arXiv | 文献发现和元数据 | 后续可进入 `tools/` 或 source-note 流程 |
| Zotero / CSL | 文献管理和引用格式 | 后续用于 bibliography 管理 |

短期不直接引入这些外部仓库作为依赖。它们先作为方法参考，避免把仓库变成多套 agent 框架的拼盘。

### 4.2 Python / R 科研建模工具

| 任务 | 推荐工具 | 用途 |
| --- | --- | --- |
| 生存分析 | `lifelines`, `scikit-survival`, R `survival` | KM、Cox、AFT、C-index、Brier score |
| 竞争风险/多状态 | R `mstate`, `cmprsk`, `riskRegression` | 多状态生命路径和竞争风险 |
| 贝叶斯建模 | Stan, PyMC | 参数不确定性、层级模型、先验和后验预测 |
| 因果推断 | DAGitty, DoWhy, EconML, CausalML | DAG、识别、估计和反事实 |
| 统计报告 | Quarto / Jupyter / Observable | 研究笔记和可复现图表 |

### 4.3 Web 可视化工具

| 工具 | 适合场景 | 判断 |
| --- | --- | --- |
| D3.js | 自定义机制图、状态图、复合交互 | 当前最适合 Human Infra 的 Web 展示核心工具 |
| Vega-Lite | 标准统计图和可复现图表规格 | 适合研究图和模型审查图 |
| Observable Plot | 快速探索和解释型图表 | 适合轻量原型 |
| Plotly | 快速交互图和科研分享 | 适合数据探索，但自定义叙事弱于 D3 |
| Mermaid | README 结构图 | 适合静态文档，不适合复杂模型图 |

## 5. 模型优化方向

### 5.1 从演示模型到科研模型

当前 Web 模型是“解释型模拟器”。下一阶段应分成四层：

```text
Layer 1: Concept model
  用于讲清楚技术如何影响主体持续性。

Layer 2: Evidence model
  每个变量绑定来源、证据等级、适用人群和反证条件。

Layer 3: Statistical model
  使用生存分析、因果模型、多状态模型估计路径变化。

Layer 4: Decision model
  输出 RMST、健康状态积分、资源预算增量和治理扣减。
```

### 5.2 目标函数重写

原始目标“寿命延长”太窄。推荐目标函数：

```text
maximize:
  E[effective_time]
  + E(healthy_state_integral)
  + E(option_value)
  + E(recovery_capacity)
  - expected_tail_risk
  - governance_friction
```

对应输出：

| 输出 | 解释 |
| --- | --- |
| `effective_time_delta` | 有效行动时间增量 |
| `healthy_state_integral` | 生存状态乘健康质量的积分 |
| `option_value_delta` | 未来可选路径增量 |
| `recovery_capacity` | 失效后的恢复能力 |
| `lev_ratio` | 进步速度 / 衰老速度 |
| `risk_adjusted_continuity` | 扣除风险后的主体持续性 |

### 5.3 因果规格模板

每个技术或因素必须写成：

```text
Question:
  技术 T 是否改变主体持续性？

Target trial:
  population:
  eligibility:
  time_zero:
  intervention:
  comparator:
  outcome:
  follow_up:
  causal_contrast:
  analysis_plan:

Mechanism:
  T -> intermediate X
  X -> state transition / hazard / observation / policy
  state -> survival / effective time / option value

Known threats:
  confounding:
  selection_bias:
  measurement_bias:
  survivorship_bias:
  competing_risks:
  missing_data:
```

## 6. 可视化优化方向

### 6.1 图表从“好看”改为“科研表达”

| 图 | 表达对象 | 标准实现 |
| --- | --- | --- |
| Causal DAG | 技术、变量、状态、结果的因果结构 | D3 force / Dagre / Graphviz |
| State transition diagram | 健康、疾病、失能、恢复、死亡状态 | D3 Sankey / alluvial / directed graph |
| Survival curve | 生存概率随时间变化 | D3 / Vega-Lite line |
| RMST bar | 固定窗口内有效时间积分差 | Vega-Lite bar |
| Competing risk plot | 不同失败事件的累计发生 | Stacked area / cumulative incidence |
| LEV gauge | 进步速度临界 | D3 gauge / threshold chart |
| Resource budget plot | 时间、注意力、认知、恢复、选择权增量 | Diverging bar |
| Calibration plot | 预测与观察是否一致 | Vega-Lite scatter / line |
| Sensitivity tornado | 参数变化对输出的影响 | Bar ranking |

### 6.2 页面结构建议

传播页和研究页分工：

| 页面 | 主要读者 | 图表要求 |
| --- | --- | --- |
| 专项传播页 | 新读者、传播、社群 | 叙事清晰，突出机制链和价值 |
| 研究模型页 | 贡献者、审查者 | 展示目标试验、模型族、验证指标和敏感性 |
| 数据审查页 | 维护者 | 来源、变量、证据等级、偏差风险和更新状态 |

`singularity-human-infra.html` 属于专项传播页。正式科研叙事、预测模型和交互图表应进入 `web/` 的 Observable Framework 应用。

### 6.3 主图与审查图分离

用户传播主图可以保持简洁，不强制把所有不确定性都画在曲线上。

科研审查层必须保留：

```text
assumption table
parameter range
calibration result
sensitivity result
external validation status
known bias
prohibited interpretation
```

这样可以兼顾传播清晰度和科研可审查性。

## 7. 实现路线

### 7.1 短期：整理与页面逻辑优化

1. 为每个页面建立 `modelSpec`：
   - variables
   - formulas
   - chart bindings
   - source notes
   - prohibited use
2. 把 D3 绘图函数按图表拆分：
   - `drawConvergenceMap`
   - `drawLifePath`
   - `drawEscapeVelocity`
   - `drawResourceBudget`
3. 每张图写清：
   - x/y 轴含义
   - 单位
   - 数据来源
   - 模型假设
   - 不允许解释成什么

### 7.2 中期：研究数据结构

推荐新增结构：

```text
docs/source-notes/
  singularity-study-note.md

docs/reference/
  research-model-visualization-toolkit.md

future optional:
  data/model-evidence/
    interventions.json
    variables.json
    sources.json
    model-spec.json
```

短期只新增本文档，不新增数据目录，避免所有权面过早膨胀。

### 7.3 长期：科研工具流水线

可逐步建立：

```text
literature search
  -> metadata table
  -> paper reading note
  -> evidence extraction
  -> variable registry
  -> model spec
  -> chart spec
  -> review checklist
  -> web rendering
```

如果后续要自动化，可借鉴用户提供的三个 GitHub 项目，但先以 Human Infra 自己的文档契约为真相源。

## 8. 审查清单

### 8.1 模型审查

- 是否定义了 population / intervention / comparator / outcome / horizon。
- 是否区分 prediction、causal effect、mechanistic plausibility。
- 是否处理 censoring、competing risks、time-varying confounding。
- 是否使用 RMST 或健康状态积分替代单一“寿命均值”。
- 是否记录外部验证、校准、敏感性和适用边界。
- 是否避免输出个人死亡日期或治疗建议。

### 8.2 可视化审查

- 图标题是否表达一个明确问题。
- 坐标轴是否中文、带单位、含时间范围。
- 图例是否能区分基线、场景、状态和阈值。
- 主图是否避免过度装饰。
- 研究图是否保留模型假设、参数范围和审查入口。
- 图表是否能从数据/模型规格复现，而不是只靠手写视觉效果。

### 8.3 文献审查

- 是否回到原论文、官方文档或项目 README。
- 是否区分作者预测、事实陈述、模型推断和 Human Infra 转译。
- 是否记录不能迁移的条件。
- 是否记录下一轮需要补证的关键词和数据库。

## 9. Web 标杆与页面模板复用

这次专项页采用“先找标杆，再按模型约束吸收”的方式。标杆分成五类，不直接复制技术栈，只复用成熟的信息架构。

### 9.1 Cloudflare Workers Templates

`https://workers.new/templates/` 是模板市场型页面。当前抓取结果显示：

- 外壳是动态 React 应用，入口为 `div#root`。
- 页面标题是 `Cloudflare Workers Templates`。
- 构建产物包括 `/templates/assets/index-CEnsSKpZ.js` 和 `/templates/assets/index-DYxxPdGb.css`。
- CSS 是 Tailwind 风格 utility bundle，页面使用 `bg-stone-50`、`max-w-7xl`、`grid-cols-*`、`rounded-*`、`shadow-*` 等类。
- 主要布局为：顶部导航、橙色 Hero、模板卡片市场、筛选侧栏、模板详情弹层、技术细节、资源链接和部署 CTA。

Human Infra 复用点：

- 用“模板卡片网格”表达研究模块，而不是把所有内容堆成长文。
- 用“约束侧栏”说明页面如何在模型、证据和仓库类型下运行。
- 用“详情/技术细节”的思路组织每个研究模块的用途、输入、输出和升级路径。

当前暂缓采用：

- 暂不引入 React、React Router、Tailwind 和 Vite 构建链。
- 原因是当前正式 Web 主线已经由 Observable Framework 承载；再引入 React/Tailwind 会增加第二套构建链、样式系统和路由体系。

升级触发：

- 出现真实数据集、搜索筛选、模型版本化、图表配置导出或在线实验时，优先扩展 Observable Framework；只有出现复杂状态管理、用户会话或应用级交互时，再评估 React 或 Astro。

### 9.2 科研解释型网页

代表对象：

- Distill
- Observable Framework / Observable Plot
- D3 gallery and examples

复用模式：

- 以一个核心问题开篇。
- 概念、机制、证据和图表同步出现。
- 图表能解释变量之间的关系，而不是只做装饰。
- 重要判断必须能回到文献、数据或模型假设。

Human Infra 页面约束：

- 预测模型图表要围绕 `T -> X -> S -> lambda(t) -> S(t)` 的因果链。
- 生存曲线、RMST、LEV 临界面和资源预算图要服务于同一个主体持续性问题。
- 传播页可以简化语言，但不能把远期设想写成既成事实。

### 9.3 证据产品型网页

代表对象：

- Our World in Data
- 数据浏览器、图表库、主题页和来源说明系统

复用模式：

- 主题页提供问题框架。
- 图表页承载数据探索。
- 来源说明记录指标定义、数据来源、处理方法和更新状态。
- 同一主题可以被文章、图表、数据表和下载入口同时表达。

Human Infra 页面约束：

- `singularity-human-infra.html` 只做专项展示，正式多页研究产品放在 `web/`。
- 后续真实研究页应把模型、数据、图表和来源拆成可追踪资产。
- 如果新增数据，必须记录字段定义、数据来源、更新时间、转换脚本和不可用边界。

### 9.4 传播型交互叙事

代表对象：

- The Pudding
- Explorable Explanations
- Nicky Case style interactives

复用模式：

- 用强开场降低进入门槛。
- 用滚动叙事或可操作控件让读者参与理解。
- 把抽象系统压缩成少数可见变量。
- 先让读者看见“机制如何动”，再给术语和方法。

Human Infra 页面约束：

- 传播层可以强表达，但必须和科研层分离。
- 可视化默认展示群体/模型层面的路径位移，不输出个人死亡日期。
- 页面要明确哪些是书内观点、哪些是 Human Infra 转译、哪些是未来建模方向。

### 9.5 当前 Web 的采用清单

| 标杆模式 | 已采用位置 | 实现方式 |
| --- | --- | --- |
| 模板市场卡片 | `web/src/index.md` 页面入口和卡片导航 | Observable Framework `grid` / `card` |
| 约束侧栏 | `web/src/model.md` 控制台和禁止用途卡片 | Framework responsive card |
| 科研解释结构 | `web/src/book.md`、`web/src/research-standards.md` | Markdown longform |
| 可复现图表入口 | `web/src/model.md` | D3 + Observable Plot |
| 证据产品入口 | 资料组织层、工具包文档 | Markdown source traceability |
| 传播型主张 | `web/src/index.md` Hero 和机制图 | narrative copy + D3 map |

## 10. Source Traceability

### User-provided research automation references

- HKUSTDial, `Supervisor-Skills`: https://github.com/HKUSTDial/Supervisor-Skills
- Imbad0202, `academic-research-skills-codex`: https://github.com/Imbad0202/academic-research-skills-codex
- wanshuiyin, `Auto-claude-code-research-in-sleep`: https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep
- S. Keshav, `How to Read a Paper`: https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf

### Core literature and standards to use next

- TRIPOD Statement / TRIPOD+AI:
  - https://www.tripod-statement.org/
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC4297220/
  - https://www.bmj.com/content/385/bmj-2023-078378
- PROBAST:
  - https://www.probast.org/
  - https://pubmed.ncbi.nlm.nih.gov/30596876/
- CONSORT-AI / SPIRIT-AI:
  - https://www.equator-network.org/reporting-guidelines/consort-artificial-intelligence/
  - https://www.nature.com/articles/s41591-020-1037-7
- Target trial emulation:
  - https://pubmed.ncbi.nlm.nih.gov/26994063/
  - https://academic.oup.com/aje/article/183/8/758/1739860
- Competing risks and multi-state models:
  - https://pubmed.ncbi.nlm.nih.gov/17031868/
  - https://onlinelibrary.wiley.com/doi/10.1002/sim.2712
- Restricted mean survival time:
  - https://pubmed.ncbi.nlm.nih.gov/24314264/
  - https://link.springer.com/article/10.1186/1471-2288-13-152
- D3: Data-Driven Documents:
  - https://vis.stanford.edu/papers/d3
  - https://ieeexplore.ieee.org/document/6064996
- Vega-Lite:
  - https://vega.github.io/vega-lite/
  - https://vis.csail.mit.edu/pubs/vega-lite/
- Munzner nested model:
  - https://www.cs.ubc.ca/labs/imager/tr/2009/NestedModel/NestedModel.pdf
  - https://ieeexplore.ieee.org/document/5290695/

### Web benchmark references

- Cloudflare Workers Templates:
  - https://workers.new/templates/
  - https://github.com/cloudflare/templates
- Distill:
  - https://distill.pub/
- Observable Framework and Plot:
  - https://observablehq.com/framework/
  - https://observablehq.com/plot/
- Our World in Data:
  - https://ourworldindata.org/
  - https://github.com/owid
- The Pudding:
  - https://pudding.cool/
- Explorable Explanations:
  - https://explorabl.es/

### Official tool docs to consult during implementation

- D3: https://d3js.org/
- Vega-Lite: https://vega.github.io/vega-lite/
- Observable Plot: https://observablehq.com/plot/
- Altair: https://altair-viz.github.io/
- lifelines: https://lifelines.readthedocs.io/
- scikit-survival: https://scikit-survival.readthedocs.io/
- Stan: https://mc-stan.org/
- PyMC: https://www.pymc.io/
- DoWhy: https://www.pywhy.org/dowhy/
- EconML: https://econml.azurewebsites.net/
- DAGitty: https://www.dagitty.net/
