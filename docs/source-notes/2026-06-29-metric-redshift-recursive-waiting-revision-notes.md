# 度规红移递归等待假设论文优化记录

日期：2026-06-29

## 目标

使用 auto-research 工具链的论文结构、方案细化、可视化和引用审查原则，对 `web/src/pages/papers/metric-redshift-recursive-waiting.astro` 进行第一轮科研化扩写。

## 使用的工具原则

- `academic-research-suite`：按论文工作流拆分研究问题、结构、论证、引用和格式边界。
- `research-refine`：冻结 Problem Anchor，避免把“黑洞等待室”泛化成不可审查的未来主义叙事。
- `paper-write`：按工作论文结构补充贡献、物理接口、模型变量、研究协议和边界声明。
- `citation-audit`：把引用分成“支持哪一层”的上下文，不让实验红移、黑洞科普、Malament-Hogarth 时空和主体持续性框架互相越界。
- `visualization_agent`：本轮采用 arXiv 原生兼容的文字图和表格，不引入新图表库，避免破坏阅读器框架。

## 本轮结构改动

原页面是 v0.1 概念短稿，核心只有命名、假设、最小模型、递归等待、可达性、反证和非目标。本轮升级为 v0.2 工作论文结构：

```text
Abstract
  -> 研究问题
  -> 贡献
  -> 概念命名
  -> 物理接口
  -> 核心假设
  -> 生命周期状态机
  -> 最小模型
  -> 递归等待飞轮
  -> 文献地图
  -> 可达性阶梯
  -> 失败条件
  -> 研究协议
  -> 非目标与治理边界
  -> References
```

## Problem Anchor

底层问题不是“能不能制造黑洞”，而是：

> 强红移时空导致的主体固有时差分，能否在满足可进入、可停留、可通信、可退出、可维生、可治理和主体连续性条件时，成为 Human Infra 的未来等待路径。

必须解决的瓶颈：

- 时间倍率 `K` 不能替代工程可行性。
- 等待不能只描述“进去”，还必须描述退出、采用技术和下一轮安全性提升。
- 文献证据必须分层，不能把实验红移或 Malament-Hogarth 理论误写成现实等待室证明。

## Source Card 草案

| 来源 | 进入模型的位置 | 支持内容 | 使用边界 |
| --- | --- | --- | --- |
| Pound and Rebka, 1959 | E1 实验基础 | 引力红移可观测。 | 不支持黑洞等待室可行。 |
| Vessot et al., 1980 | E1 实验基础 | 空间氢钟测试相对论引力效应。 | 不支持长期人体等待。 |
| Ashby, 2003 | E1 实验基础 | GPS 系统需要相对论修正。 | 不支持强场工程。 |
| NASA black hole pages | E2 强场直觉 | 黑洞附近存在极端红移、时间膨胀和事件视界风险。 | 科普材料，不能替代论文推导。 |
| Grib and Pavlov, 2009 | E3 黑洞未来观察限制 | 自由落体黑洞观察外部无限未来存在限制。 | 不覆盖所有旋转黑洞特殊轨道。 |
| Pavlov, 2012 | E3 黑洞未来观察限制 | 不同黑洞类型下观察未来的理论条件。 | 不是工程可行性证明。 |
| Etesi and Nemeti, 2002 | E4 极限时空 | Malament-Hogarth 时空和相对论超计算。 | 不是普通黑洞等待室。 |
| Welch, 2006 | E4 极限时空 | Malament-Hogarth 计算能力边界。 | 不支持人体路径。 |
| Earman and Norton | E4 哲学边界 | Supertask 和 Malament-Hogarth 时空哲学讨论。 | 不提供物理工程路线。 |
| Human Infra 有效永生飞轮 | E5 主体持续性 | 将等待收益放回主体持续性和可能性空间。 | 不替代物理证据。 |

## 下一步任务

1. 为每个来源创建正式 Source Card：`claim / variable / mechanism / evidence role / boundary / falsifier`。
2. 把 `K`、`P_exit`、`P_adopt`、`P_continuity`、`R_tail` 等变量接入 Human Infra 生命路径模型契约。
3. 给论文页补一个交互式模型版本，但必须继续复用 arXiv HTML Paper 阅读器框架，不修改 CSS、JS、字体和 DOM 契约。
4. 追加浏览器级断言：TOC 存在、目录项存在、摘要存在、参考文献存在、正文无重复 class。

## v0.2 数据化补强

本轮继续把论文页从“静态长文”推进到“可审查研究资产”：

- 新增 `web/src/data/metric-redshift-recursive-waiting.json`，作为度规红移递归等待论文页的结构化真相源。
- 新增 `web/scripts/audit-metric-redshift-paper.mjs`，检查 Claim Register、Claim-Evidence Matrix、Source Cards、变量契约、章节和页面必需字符串。
- 新增 `npm run audit:metric-redshift`，生成 `web/src/data/metric-redshift-recursive-waiting/COVERAGE_AUDIT.json` 和 `COVERAGE_AUDIT.md`。
- 页面新增 `Claim-Evidence Matrix` 和 `变量契约` 两节，由 JSON 渲染，不再手写散落表格。

专项审查当前结果：

```text
metric-redshift coverage verdict PASS
claims 7
sources 12
variables 13
findings 0
```

新的主张边界：

```text
MRW-CL7:
Malament-Hogarth 和时间旅行哲学文献只能提供极限时空与概念边界，
不能被直接转写为人体等待工程证据。
```

## v0.2 论文页面工具化补强

本轮按 arXiv HTML Paper Reuse Kit 的正式消费路径补齐页面创建证据：

- 调用 `python3 tools/arxiv_html_paper_tool.py write-page` 生成 `web/src/data/metric-redshift-recursive-waiting/TOOL_GENERATED_PAGE_SEED.astro`，作为该论文页的工具生成 seed。
- 正式路由继续使用 `web/src/pages/papers/metric-redshift-recursive-waiting.astro`，只在工具模板契约允许的正文层扩展论文内容，不修改 arXiv CSS、JS、字体或阅读器控件。
- `web/scripts/audit-metric-redshift-paper.mjs` 已升级为同时检查工具 seed、Paper Plan、Figure Plan、Citation Context Register、S1-S16 章节和页面必需字符串。
- 页面新增 `图表计划与引用预审`，把 figure-designer 与 citation-audit 的本地预审结果写成可执行研究队列。

工具化约束：

```text
工具 seed 证明页面入口来自 arXiv HTML Paper Reuse Kit
  -> 正式论文页只消费结构化研究数据和正文内容
  -> 审计脚本检查 DOM 契约、章节、主张、来源、变量、图表计划和引用语境
  -> 不允许通过自定义 CSS/JS/字体破坏 arXiv 阅读器框架
```

## v0.3 Derivation Package

### Target

解释“度规红移递归等待假设”的最小判定式：为什么 `K` 只能作为主体固有时压缩指标，而 `NCG` 才是 Human Infra 中判断等待路径是否值得继续研究的决策对象。

### Status

COHERENT AFTER REFRAMING / EXTRA ASSUMPTION

本轮没有把 `NCG` 写成物理定律或经验结论，而是把它重构为一个规范化决策对象。它需要额外假设：风险、机会成本和技术收益必须先归一到同一持续性尺度。

### Invariant Object

不变量是单轮等待对主体持续性的净贡献 `NCG_i`，而不是红移倍率 `K_i`。`K_i` 是局部代理变量，只描述外部参考时间和主体固有时的比例。

### Assumptions

- `MRW-A1`: 等待场景必须指定外部参考观察者、主体世界线和等待区度规条件。
- `MRW-A2`: 主体固有时必须大于 0，且主体在该固有时内保持最低生命支持和连续性。
- `MRW-A3`: `K` 是场景相关的有限倍率，必须绑定轨道、区域、潮汐、辐射、通信和退出条件。
- `MRW-A4`: `PWindow`、`PExit`、`PAdopt`、`PContinuity` 是条件概率门，不默认独立。
- `MRW-A5`: `U` 只表示主体退出后可获得、可理解、可承受并可整合的技术升级收益。
- `MRW-A6`: `RLife`、`REngineering`、`RTail`、`COpportunity` 必须归一到与 `NCG` 可比较的持续性成本尺度。
- `MRW-A7`: 递归等待只有在本轮升级改善下一轮参数时成立。
- `MRW-A8`: 单点不可逆失败、主体连续性破坏或不可治理尾部风险优先触发中止。

### Notation

- `DeltaTExternal_i`: 第 `i` 轮外部参考时间增量。
- `DeltaTauSubject_i`: 第 `i` 轮主体固有时增量。
- `K_i = DeltaTExternal_i / DeltaTauSubject_i`: 未来等待倍率。
- `U_i`: 外部技术升级收益。
- `PWindow_i`、`PExit_i`、`PAdopt_i`、`PContinuity_i`: 技术窗口、退出、采用和连续性的概率门。
- `RLife_i`、`REngineering_i`、`RTail_i`、`COpportunity_i`: 生命支持、工程、尾部风险和机会成本扣减项。
- `Theta_i`: 第 `i` 轮等待前的主体和基础设施状态。

### Derivation Strategy

从主体持续性的净贡献出发，而不是从黑洞或时间旅行叙事出发。先定义局部时间差分 `K_i`，再把它嵌入概率门和风险扣减，最后给出递归条件。

### Derivation Map

1. 由 `MRW-A1` 和 `MRW-A2` 定义可比较时间量 `DeltaTExternal_i` 与 `DeltaTauSubject_i`。
2. 由定义得到 `K_i = DeltaTExternal_i / DeltaTauSubject_i`。
3. 由 `MRW-A3` 得出 `K_i` 只是有限场景参数，不是收益对象。
4. 由 `MRW-A4` 和 `MRW-A5` 将倍率收益乘以窗口、退出、采用和连续性概率门。
5. 由 `MRW-A6` 扣除生命支持、工程、尾部风险和机会成本。
6. 由 `MRW-A7` 给出递归改善条件。
7. 由 `MRW-A8` 给出中止规则。

### Main Derivation

Step 1. 定义单轮等待倍率：

```text
K_i = DeltaTExternal_i / DeltaTauSubject_i
```

该步骤是定义，不是经验命题。它只在参考观察者、主体世界线和固有时都已定义时成立。

Step 2. 将倍率从“时间比例”转成“可能收益”的上游项：

```text
Gross_i = K_i * U_i * PWindow_i * PExit_i * PAdopt_i * PContinuity_i
```

该步骤是模型假设。它表达的是：外部时间更长只有在技术窗口出现、主体能退出、能采用技术且连续性保持时，才可能转为主体收益。

Step 3. 扣除风险和机会成本：

```text
NCG_i = Gross_i - RLife_i - REngineering_i - RTail_i - COpportunity_i
```

该步骤是规范化判定式，需要 `MRW-A6`。如果各项没有归一到同一持续性成本尺度，不能相加减。

Step 4. 定义递归条件：

```text
Theta_{i+1} = F(Theta_i, Upgrade_i)
RecursiveGain_i requires NCG_{i+1}(Theta_{i+1}) > NCG_i(Theta_i)
```

该步骤是机制命题，不是保证。它要求本轮升级真实改善下一轮等待倍率、概率门、风险项或机会成本。

Step 5. 定义中止条件：

```text
Abort_i if PExit_i = 0
Abort_i if PContinuity_i = 0
Abort_i if RTail_i exceeds governance threshold
```

该步骤是治理命题。不可逆失败优先于倍率收益。

### Remarks and Interpretation

- `K` 是必要但远不充分的指标。
- `NCG` 的作用是阻止“高时间膨胀”被误读成“高主体持续性收益”。
- 递归等待的真正难点不是等待一次，而是退出后能否改善下一轮等待条件。
- 该模型允许未来扩展为场景卡片和交互图表，但当前不输出任何现实任务建议。

### Boundaries and Non-Claims

- 不声明人工黑洞、类黑洞或强红移等待区当前可制造。
- 不声明任何现实黑洞路径具有正 `NCG`。
- 不声明有限固有时可以观察外部无限未来。
- 不提供航天、轨道、生命支持或人体实验步骤。
- 不把 Malament-Hogarth 理论、时间旅行哲学或 NASA 科普材料转写为工程可行性证据。

### Open Risks

- `NCG` 的风险和收益归一化尺度仍需要后续定义。
- 各概率门不是独立变量，后续模型必须处理条件依赖。
- `Theta_{i+1}` 的状态转移函数仍是框架级表达，缺少场景数据。
- 当前公式适合科研组织和可视化，不适合作为工程设计或个人决策工具。

## v0.4 Claim Maturity and Falsifier Register

本轮使用 pre-submission review 和 paper-claim-audit 的审查原则，但不把概念论文伪装成实验论文：当前没有 raw experiment results，因此不执行数字型 paper-claim-audit；改为对每条核心主张建立成熟度、证据状态、缺失证据、晋升门槛和反证触发条件。

新增结构：

```text
Claim Register
  -> Claim-Evidence Matrix
  -> Claim Maturity Register
  -> Falsifier Register
```

成熟度分层：

| 层级 | 含义 |
| --- | --- |
| M2 conceptual-definition | 可作为定义或对象边界使用，但还不能声称场景可行。 |
| M2 mechanism-hypothesis | 机制链条内部连贯，但缺少场景数据或状态转移函数。 |
| M2 research-architecture | 可作为研究架构和分类法，但不是技术成熟度路线图。 |
| M3 model-boundary | 有实验或文献支持底层边界，但不支持工程可行性。 |
| M3 literature-boundary | 文献足以约束过度叙述，但不支持正向可行性。 |
| M3 governance-rule | 可作为治理判定规则，但仍需阈值和归一化尺度。 |
| M3 conceptual-boundary | 可作为概念边界和引用语境约束，不可迁移为工程证据。 |

反证队列的作用：

```text
每条主张必须说明：
  -> 什么情况会使它降级
  -> 降级后采取什么动作
  -> 继续使用前必须检查什么
```

本轮新增页面章节：

```text
14. 主张成熟度与反证队列
```

专项审计新增检查：

- 每个 claim 必须有且只有一个 maturity entry。
- 每个 claim 必须有且只有一个 falsifier entry。
- maturity / falsifier 引用的 claimId 必须存在。
- 页面必须包含 `主张成熟度与反证队列`。

本轮设计取舍：

- 没有新增外部 reviewer verdict，因为当前还没有真实投稿稿件和实验结果文件。
- 没有把成熟度写成证据等级分数，因为这会制造虚假精度。
- 先用 register 固定主张边界，后续再为每个 claim 增加正式 Source Card 和场景卡片。

## v0.5 Source Card Ledger

本轮把早期 Source Card 草案正式化为 `sourceCardLedger`。目标不是新增外部结论，而是把已有 12 个来源的证据角色、允许用途、禁止用途、映射主张、映射变量、反证条件和下一步动作写成机器可查账本。

新增结构：

```text
Source Cards
  -> Source Card Ledger
  -> Claim-Evidence Matrix
  -> Citation Context Register
```

每个来源现在必须记录：

- `sourceKey`: 回到 `sourceCards` 的唯一键。
- `sourceRole`: 该来源在论文中的证据角色。
- `mappedClaims`: 可支持或约束的主张。
- `mappedVariables`: 进入的模型变量。
- `mechanismUse`: 在机制链中的使用方式。
- `allowedUse`: 允许支持的语境。
- `forbiddenUse`: 禁止外推的语境。
- `falsifier`: 何种写法会导致引用语境失败。
- `nextAction`: 后续正式 Source Card 或场景卡片任务。

Source Card Ledger 的核心规则：

```text
来源存在
  -> 不等于主张成立
  -> 不等于工程可行
  -> 不等于可迁移到人体等待
  -> 必须说明证据角色和禁止外推边界
```

专项审计新增检查：

- 每个 `sourceCards[*].key` 必须有且只有一个 `sourceCardLedger` 条目。
- 每个 ledger 条目的 `mappedClaims` 必须指向现有 claim。
- 每个 ledger 条目的 `mappedVariables` 必须指向现有变量。
- ledger 必须包含 allowed / forbidden / falsifier / nextAction。
- 页面必须包含 `Source Card Ledger`。

当前 ledger 覆盖：

```text
12 source cards
  -> 12 source ledger entries
  -> 7 claims
  -> 13 variables
```

## v0.6 Scenario Card Template and Evaluation Registry

本轮使用 experiment-plan 的 claim-driven 思路，但不制造实验结果：把“候选等待路径”先转成场景卡片协议，明确每个场景需要什么输入、何时中止、何时不能进入 `NCG` 判定。

新增结构：

```text
Scenario Card Template
  -> Metric Card
  -> Orbit / Region Card
  -> Continuity Card
  -> Window Card
  -> Risk Card
  -> Exit Card
  -> Scenario Evaluation Registry
```

模板规则：

```text
候选场景
  -> 六类卡片齐全
  -> 无 abort 条件触发
  -> 才能进入 NCG toy evaluation
```

四个初始场景：

| 场景 | 类型 | 当前状态 | 用途 |
| --- | --- | --- | --- |
| `MRW-SC0` | calibration-baseline | not-a-waiting-room | 用弱场相对论时钟差校准 `K` 的概念。 |
| `MRW-SC1` | negative-boundary-case | literature-constrained | 约束普通黑洞自由落体“看无限未来”的过度叙述。 |
| `MRW-SC2` | theoretical-stress-test | blocked-by-engineering-and-risk | 压力测试高 `K` 但风险扣减导致 `NCG` 不成立的场景。 |
| `MRW-SC3` | future-hypothesis | speculative-architecture | 承载“若未来存在可控强红移等待区”的条件性对象。 |

本轮刻意保持保守：

- `MRW-SC0` 不是等待室，只是校准基线。
- `MRW-SC1` 和 `MRW-SC2` 是负例或压力测试，不输出可行性。
- `MRW-SC3` 是远期假设，六类卡片全部缺失时禁止进入可行性判断。

专项审计新增检查：

- `scenarioCardTemplate.requiredCards` 至少 6 类。
- 每类卡片必须有 `requiredFields` 和 `rejectIfMissing`。
- `scenarioEvaluationRegistry` 至少 4 个场景。
- 每个场景必须有 linked claims、key variables、card status、NCG status、stop gate 和 non-claim。
- 每个场景必须覆盖模板中的六类卡片状态。

## v0.7 Toy NCG Evaluation Protocol

本轮继续使用 `experiment-plan` 的 claim-driven 思路，把场景卡片后的下一层补齐为 `Toy NCG Evaluation Protocol`。重点不是制造数值结果，而是把“哪些资料足够进入 NCG 判定”变成可审查协议。

新增结构：

```text
Scenario Card Template
  -> Toy NCG Evaluation Protocol
  -> Toy NCG Evaluation Registry
  -> blocker / next work / non-claim
```

协议输入：

```text
K
  -> U
  -> PWindow
  -> PExit
  -> PAdopt
  -> PContinuity
  -> RLife / REngineering / RTail
  -> COpportunity
  -> NCG direction
```

核心规则：

```text
先判断能不能算
  -> 再判断方向性
  -> 不输出现实可行性
  -> 不输出个体寿命预测
  -> 不把 K 的数量级替代 NCG
```

四个 toy 评估：

| 评估 | 场景 | 状态 | 用途 |
| --- | --- | --- | --- |
| `MRW-TOY0` | `MRW-SC0` | calibration-only | 只校准弱场时钟差概念，不进入主体持续性收益。 |
| `MRW-TOY1` | `MRW-SC1` | blocked | 由退出门和连续性门阻断普通黑洞自由落体正收益叙述。 |
| `MRW-TOY2` | `MRW-SC2` | blocked-by-risk-costs | 作为高 `K` 低 / 负 `NCG` 的压力测试反例。 |
| `MRW-TOY3` | `MRW-SC3` | cannot-evaluate | 远期假设缺少六卡片时禁止方向性收益判断。 |

专项审计新增检查：

- `toyNcgEvaluationSpec` 必须包含协议版本、目的、输入契约、归一化规则、公式、评估步骤、解释规则、禁止用法和晋升门槛。
- 每个 `inputContract` 必须引用现有变量和现有 Scenario Card。
- 每个 toy step 必须包含 `step`、`operation`、`reason` 和 `failureIf`。
- 每个 `toyNcgEvaluationRegistry` 条目必须引用现有 scenario、claim 和变量。
- 页面必须包含 `Toy NCG Evaluation Protocol` 和 `Toy NCG Evaluation Registry`。

## v0.8 F4 NCG Formula Decomposition

本轮使用 `figure-designer` 的图表设计规则，把原先 Figure Plan 中 `planned` 状态的 F4 落成数据驱动图表。由于当前论文没有真实场景数值，F4 不使用柱状图、折线图或坐标轴，而采用公式分解图。

图表目标：

```text
NCG Formula Decomposition
  -> time-and-upgrade-gain
  -> probability-gates
  -> risk-deductions
  -> opportunity-cost
  -> decision-output
```

图表主张：

```text
K 是固有时压缩代理变量
  -> 不是等待路径收益本身
  -> 必须乘以技术收益和概率门
  -> 必须扣除生命、工程、尾部风险和机会成本
  -> 才能得到方向性的 NCG 研究分类
```

实现位置：

- `web/src/data/metric-redshift-recursive-waiting.json` 新增 `ncgFormulaDecompositionFigure`。
- `web/src/pages/papers/metric-redshift-recursive-waiting.astro` 在 S7 最小模型中渲染 `Figure 4`。
- `F4.status` 从 `planned` 改为 `implemented as data-backed formula decomposition figure`。

专项审计新增检查：

- `ncgFormulaDecompositionFigure.figureId` 必须指向现有 `figurePlan`。
- 每个分解块必须包含 `id`、`group`、`operation`、`variables`、`role` 和 `interpretation`。
- 每个分解块引用的变量必须存在于 `variableDictionary`。
- 页面必须包含 `NCG Formula Decomposition`。

## v0.9 Pre-Submission Review Register

本轮使用 `pre-submission-reviewer` 的提交前审稿思路，但不伪装成外部审稿结果。新增 `Pre-Submission Review Register`，把当前工作论文仍然不能直接投稿的原因显式化。

核心判断：

```text
工作论文
  -> 已有术语、模型、场景卡、toy NCG、图表和审计账本
  -> 仍缺外部引用语境核验、可复现 evaluator、量纲归一化方案、系统 related work 和目标 venue 格式
  -> 因此推荐继续作为 working paper 迭代
  -> 不应声明 ready to submit
```

新增阻塞项：

| 编号 | 严重性 | 维度 | 当前动作 |
| --- | --- | --- | --- |
| `MRW-PSR1` | CRITICAL | citation-grounding | 完成 MRW-CTX1 到 MRW-CTX7 的 fresh reviewer citation audit。 |
| `MRW-PSR2` | CRITICAL | evidence-and-experiment | 增加最小可复现 scenario evaluator。 |
| `MRW-PSR3` | MAJOR | model-validity | 明确 NCG 归一化尺度与 qualitative / quantitative 分层。 |
| `MRW-PSR4` | MAJOR | related-work | 补强强场工程、任务设计、生命支持与风险治理 related work。 |
| `MRW-PSR5` | MINOR | figure-quality | 后续生成 SVG/PDF 图，同时保留 HTML table fallback。 |
| `MRW-PSR6` | MAJOR | format-and-language | 冻结中文 source of truth 后再生成英文 LaTeX draft。 |

专项审计新增检查：

- `preSubmissionReviewRegister` 至少 6 条。
- 每条必须包含维度、严重性、发现、证据片段、提交前 gate、修复动作、关联章节和状态。
- 严重性只允许 `CRITICAL`、`MAJOR`、`MINOR`。
- 状态只允许 `blocks-submission`、`major-revision-needed`、`polish-before-submission`。
- 在外部证据和可复现性缺口关闭前，至少保留一个 `CRITICAL` 阻塞项。
- 页面章节从 S18 扩展到 S19，S18 为提交前审稿风险，S19 为非目标与治理边界。

## v0.10 Symbolic Scenario Evaluator

本轮使用 `experiment-plan` 的可复现评估思路，补齐 `MRW-PSR2` 指出的最小 evaluator 缺口。新增脚本不是物理仿真，也不输出现实可行性；它只把已有 Scenario Evaluation Registry 和 Toy NCG Evaluation Registry 转换成机器可审查的分类账本。

新增脚本：

```text
web/scripts/evaluate-metric-redshift-scenarios.mjs
  -> 读取 metric-redshift-recursive-waiting.json
  -> 合并 MRW-SC* 与 MRW-TOY*
  -> 计算 evaluationClass
  -> 判定 canEnterQuantitativeNcg
  -> 输出 SCENARIO_EVALUATION_AUDIT.json / .md
```

当前 evaluator 输出：

```text
4 scenarios
4 toy evaluations
0 quantitative-ready evaluations
evaluation classes:
  calibration-only: 1
  blocked: 2
  cannot-evaluate: 1
```

关键语义修正：

```text
弱场时钟校准场景
  -> 可用于校准 K 的概念
  -> 不是等待室
  -> 不允许进入 quantitative NCG
```

因此当前结论保持保守：

```text
有可复现 symbolic evaluator
  -> 但没有任何场景 quantitative-ready
  -> MRW-PSR2 从 CRITICAL 降为 MAJOR
  -> MRW-PSR1 仍保持 CRITICAL
```

专项审计新增检查：

- `audit:metric-redshift` 先运行 `evaluate:metric-redshift`，再运行 coverage audit。
- `scenarioEvaluationAuditRows` 至少 4 条。
- 每条 scenario audit row 必须引用已有 scenario 和 toy NCG evaluation。
- 页面必须包含 `Scenario Evaluation Audit`。

## v0.11 Citation Context Packet and Local Review

本轮使用 `citation-audit` 的引用语境审查原则，处理 `MRW-PSR1` 的第一阶段：先生成外部审查输入包和本地边界审查账本。注意：这不是外部 fresh reviewer verdict，因此 `MRW-PSR1` 仍保持 `CRITICAL`。

新增脚本：

```text
web/scripts/export-metric-redshift-citation-context-review-packet.mjs
  -> CITATION_CONTEXT_REVIEW_PACKET.json
  -> CITATION_CONTEXT_REVIEW_PACKET.md

web/scripts/audit-metric-redshift-citation-context-local-review.mjs
  -> CITATION_CONTEXT_LOCAL_REVIEW.json
  -> CITATION_CONTEXT_LOCAL_REVIEW.md
```

当前本地审查结果：

```text
7 citation contexts
7 local reviews
verdict: LOCAL_REVIEW_COMPLETE_REQUIRES_FRESH_REVIEW
```

语义边界：

```text
local review complete
  -> 说明 safe use / forbidden use / risk tier / reviewer focus 已登记
  -> 不说明引用已经被外部独立审稿人验证
  -> 不允许把 MRW-PSR1 降级为非阻塞项
```

`MRW-PSR1` 更新为：

```text
已生成 citation context review packet 和本地边界审查
  -> 仍缺外部 fresh reviewer 逐项 PASS / WARN / FAIL
  -> 保持 CRITICAL
```

专项审计新增检查：

- `audit:metric-redshift` 会先运行 metric citation context packet export 和 local review。
- `citationContextReviewPacketRows` 至少 7 条。
- `citationContextLocalReviewRows` 至少 7 条。
- coverage audit 验证 packet verdict 为 `READY_FOR_EXTERNAL_REVIEW`。
- coverage audit 验证 local review verdict 为 `LOCAL_REVIEW_COMPLETE_REQUIRES_FRESH_REVIEW`。
- 页面必须包含 `Citation Context Review Packet` 和 `Citation Context Local Review`。
