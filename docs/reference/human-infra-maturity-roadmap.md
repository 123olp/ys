# Human Infra Maturity Roadmap

本文档定义 Human Infra 从“讲清楚价值”走向“严肃研究框架”和“可运行定量模型”的 100% 状态。它不是宣传稿，而是验收契约：任何阶段都必须能说明目标、对象、边界、证据、模型和不能外推的部分。

## 总判断

截至 2026-07-02，项目已经完成了价值追问、域地图、主流 LEV 路线和 Web 叙事的主体搭建，但尚未达到完整研究工程系统。

| 轴线 | 当前成熟度 | 100% 状态 | 当前最大缺口 |
| --- | ---: | --- | --- |
| 项目价值 | 70% | 不同受众能用同一核心命题理解 Human Infra 的必要性 | 缺少统一成熟度契约和外部框架对齐 |
| 研究框架 | 35% | 每条主张都进入 Source Card、Claim-Evidence Matrix、变量表和反证条件 | 研究域多，但主张级证据闭环还不均匀 |
| 定量模型 | 10% | 有可运行、可复现、可审查的场景级模型管线 | Web 主要是示意计算，缺少独立模型输入、导出器和模型卡 |

## 价值层 100%

价值层的 100% 不是写更多宏大叙事，而是让项目在不同入口都指向同一个第一原理：

```text
一切目标、价值和创造都预设一个能够持续行动的主体
  -> 主体持续性不是普通目标之一，而是所有目标成立的边界条件
  -> Human Infra 的对象是维持、延展、增强主体持续性所需的生命、认知、时间、资源、工具、环境和协作系统
  -> 项目价值不是单点延寿，而是扩大主体未来仍能存在、行动、学习、修正和选择的可能性空间
```

验收条件：

- 有一个 100 字内总定义，能解释目标、对象和约束。
- 有至少三种价值视角：主体持续性、通用资源增量、反稀缺工程。
- 每种视角都能说明它改变的稀缺资源：寿命、健康寿命、有效时间、注意力、认知、恢复、资金、社会支持、环境和未来选择权。
- 能区分 Human Infra 与健康管理、长寿知识库、AI 工具箱、社会政策百科和医学建议系统。
- 能把价值语言连接到外部理论脊柱：能力方法、健康作为身体/心理/社会福祉、福祉测量、复杂干预和预测模型报告规范。

## 研究框架 100%

研究框架的 100% 是让每个研究域和每条主张都能被审查。

最低结构：

```text
研究问题
  -> 研究域对象
  -> 变量表
  -> 机制链路
  -> Source Cards
  -> Claim-Evidence Matrix
  -> 反证条件
  -> 模型位置
  -> 治理边界
```

验收条件：

- 研究域必须进入 C1-C6 物理分级目录，并在 README / AGENTS 中说明对象、非目标和上下游。
- 每个进入主论文或 Web 页的强主张必须绑定来源、证据等级、适用范围和禁止外推边界。
- 每个定量相关主张必须区分相关性、因果效应、预测能力、机制合理性和治理判断。
- 每条路线必须拆出概率门：技术窗口、可及性、采用概率、持续时间、组合性、尾部风险、机会成本。
- 模型必须区分 `screening model`、`toy model`、`calibrated predictive model` 和 `decision model`。
- 高风险领域必须写明中止条件，而不是只写“未来可能”。

## 定量模型 100%

定量模型的 100% 不是预测个人死亡日期，而是建立可复现的场景级生命路径模型。

目标形态：

```text
versioned inputs
  -> executable model
  -> generated scenario outputs
  -> Web visualization
  -> model card
  -> sanity checks
  -> governance boundary
```

最小可运行模型必须做到：

- 从版本化 JSON / TSV 输入读取场景，而不是把参数只写在前端脚本里。
- 命令行能生成 Web 数据文件。
- 输出群体/合成队列的风险函数、生存曲线、健康质量积分、有效时间和 LEV 阈值状态。
- 不输出个体死亡日期，不给个体医疗建议，不声明真实疗效。
- 包含模型卡：用途、非用途、输入来源、证据等级、主要假设、已知限制和升级条件。
- 包含 sanity checks：生存曲线单调、概率范围合法、无个人预测字段、场景 ID 唯一。

## 外部方法锚点

这些锚点只提供方法约束，不直接证明 Human Infra 的任何具体主张。

| 来源 | Human Infra 使用位置 | 边界 |
| --- | --- | --- |
| Stanford Encyclopedia of Philosophy: Capability Approach | 把项目价值从资源占有转向真实能力、功能和选择空间 | 不把能力方法直接等同于永生伦理 |
| WHO Constitution | 把健康理解为身体、心理和社会福祉，而非仅无病 | 不把 WHO 定义当作具体干预证据 |
| MRC complex interventions framework | 复杂干预需要开发、评估、实施和语境分析 | 不替代具体临床试验 |
| TRIPOD+AI | 预测模型需要透明报告、开发/验证/更新边界 | 不表示当前 toy model 已达临床预测标准 |
| PROBAST / PROBAST+AI | 预测模型偏倚和适用性需要系统评估 | 不表示当前模型已具备低偏倚 |
| ISPOR Modeling Good Research Practices | 模型需要结构、参数、验证、报告和决策语境 | 不表示当前模型可用于真实资源分配 |
| DYNAMO-HIA / Future Elderly Model / OHDSI PLP | 可参考群体健康模拟、老龄化微观仿真和患者级预测工程 | 不直接复用为 Human Infra 校准模型 |

## 阶段路线

### Stage 1: 价值和边界冻结

完成条件：

- README、Web 首页、论文页和 reference 文档都使用同一套目标、对象、约束语言。
- 价值视角不再互相竞争，而是作为同一第一原理的不同投影。
- 每个传播性概念都有正式研究名和禁止误读说明。

### Stage 2: 研究域证据闭环

完成条件：

- C1 / C2 核心域优先完成 Source Cards 和 Claim-Evidence Matrix。
- 每个主流 LEV 路线都有路线卡、概率门、负向链路和证据边界。
- 所有强主张都能回到本地文档、来源链接和审查状态。

### Stage 3: Toy model 可运行

完成条件：

- 存在独立脚本可从版本化输入导出 Web 模型数据。
- Web 页面消费导出数据，而不是只用内嵌示意参数。
- CI / make check 能至少编译模型脚本。

### Stage 4: 校准模型预备

完成条件：

- 明确 target population、estimand、time zero、outcome、predictors、censoring 和 validation plan。
- 明确可用数据源、数据质量、缺失、代表性和伦理边界。
- 引入 TRIPOD+AI、PROBAST+AI、MRC 和 ISPOR 的最低报告字段。

### Stage 5: 严肃研究系统

完成条件：

- 模型、文档、Source Cards、Web 可视化和审计账本可一起复现。
- 能清楚说明某个技术或资源如何改变变量、状态、风险函数、生存曲线、有效时间和未来选择权。
- 能清楚说明当前不能算什么、为什么不能算、缺什么数据才能算。

## 当前下一步

最小正确下一步不是继续扩域，而是补定量管线：

```text
life_path_toy_model_scenarios.json
  -> run_life_path_toy_model.py
  -> life-path-toy-model.json
  -> /model/ Web 图表
  -> model card + sanity checks
```

这一步完成后，项目会从“有定量想法的研究叙事”进入“有最小可执行模型管线的研究系统”。

## 参考入口

- Stanford Encyclopedia of Philosophy, Capability Approach: https://plato.stanford.edu/entries/capability-approach/
- WHO Constitution: https://www.who.int/about/governance/constitution
- MRC framework for complex interventions: https://www.bmj.com/content/374/bmj.n2061
- TRIPOD statement: https://www.tripod-statement.org/
- PROBAST: https://www.probast.org/
- ISPOR Good Practices Reports: https://www.ispor.org/heor-resources/good-practices
- DYNAMO-HIA: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0033317
- Future Elderly Model: https://schaeffer.usc.edu/data/future-elderly-model/
- OHDSI Patient-Level Prediction: https://www.ohdsi.org/web/wiki/doku.php?id=projects:workgroups:patient-level_prediction
- WHO HALE metadata: https://www.who.int/data/gho/indicator-metadata-registry/imr-details/7752
