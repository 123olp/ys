# Singularity Control Interpretability Boundary

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c1-boundary-rewriting/singularity-control-interpretability-boundary` |
| 分级 | `C1` - 可能性边界改写层 |
| 控制轴 | 控制/解释权边界 |
| 分级理由 | 研究超人 AI 或奇点式系统出现后，人类解释、控制、治理和未来选择权是否发生边界断裂。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何直接改写主体持续性边界，例如寿命、死亡、时间差分、身份连续性或未来抵达能力？

```text
研究域对象
  -> 影响变量 / 中间机制
  -> 改变主体状态或外部条件
  -> 改变风险、能力、时间成本或可达性
  -> 改变有效寿命、有效时间或未来选择权
```

### 使用边界

- 本域是研究与建模单元，不是个体医疗、法律、金融、工程、教育或安全操作建议。
- 新增内容必须标明来源、适用对象、证据等级和不确定性；AI 总结不能作为事实源。
- 若内容会改变分级、目录位置或上下游关系，先更新 `domains/_possibility-space-control/classification.tsv`。
<!-- domain-standard:end -->

<!-- domain-research-skeleton:start -->
## 研究推进骨架

### 最小问题集

- 界定本域直接改写的主体持续性边界：寿命、死亡、身份连续性、时间差分或未来抵达能力。
- 说明主体连续性条件：身体、记忆、人格、行动能力或法律身份中哪些必须保持。
- 列出不可越过的中止门槛：退出失败、连续性失败、尾部风险、不可逆损伤或治理失效。
- 说明它如何改变有效寿命、有效时间、未来选择权或可能性空间。
- 明确本域不能被宣传成现实永生、工程可行性或个体行动方案。

### 变量接口

- 输入变量：本域直接处理的对象、资源、技术、环境、制度或状态。
- 中间机制：变量通过什么因果路径改变主体状态、系统状态或外部条件。
- 状态改变：身体、认知、能力、资源、风险暴露、可及性、时间成本或协作条件如何变化。
- 风险 / 成本函数：死亡风险、失能风险、工程风险、尾部风险、机会成本、维护成本或治理成本如何变化。
- 输出指标：有效寿命、健康寿命、有效时间、主观时间、相对时间、行动能力、恢复能力或未来选择权。

### 证据入口

- 官方 / 原始资料：监管文件、数据库、临床登记、标准、论文原文、项目白皮书或一手报告。
- 综述 / 指南 / 标准：系统综述、领域指南、技术标准、伦理规范和权威机构材料。
- 数据集 / 登记系统：可复核的数据表、代码、实验记录、登记号、版本和采集边界。
- 反例 / 失败案例：负结果、副作用、安全事故、不可复现结果、伦理争议和误用案例。

### 最小产出

- Source Signals：记录候选资料、来源、日期、主张和待核验点。
- Source Cards：提取 claim、变量、机制、证据类型、边界、反证条件和可迁移位置。
- Claim-Evidence Matrix：把每个稳定主张绑定到来源、证据等级、适用范围和不确定性。
- 变量表：列出输入变量、中间变量、状态变量、风险变量、输出指标和可观测代理指标。
- 上下游关系：说明本域依赖哪些更根本域，并向哪些转化、应用或基础设施域输出。
<!-- domain-research-skeleton:end -->

本域研究奇点叙事中最关键的负向边界：当系统能力、速度和复杂度超过人类审查能力时，主体是否还能保持解释权、控制权、退出权、分配权和未来选择权。

## 核心链路

```text
AI 能力和技术窗口速度上升
  -> 人类解释、复现、审查和治理速度相对下降
  -> 科学、医学、经济和基础设施决策更依赖不可完全理解的系统
  -> 主体获得新技术收益的同时承担控制、分配和尾部风险
  -> 未来选择权可能扩张，也可能被系统性削弱
```

## 关键变量

- `InterpretabilityGap`：系统输出与人类可解释、可复现、可审查之间的差距。
- `ControlLatency`：发现问题、暂停系统、回滚系统和修正后果的时间。
- `GovernanceCapacity`：制度、组织、监管和公众理解对齐前沿系统的能力。
- `DistributionControl`：谁控制算力、数据、模型、接口、知识产权和收益分配。
- `TailRiskExposure`：系统性失控、滥用、不可逆错误、军备竞赛和基础设施依赖风险。

## 非目标

- 不提供模型越权、规避监管、扩散危险能力或绕过安全边界的方法。
- 不把“不可解释”简单写成“不可使用”；本域关注解释不足时的审查、控制和中止门槛。
- 不把 AI 风险叙事替代 AI 自动科研证据；风险和收益必须分开建模。

## Source Signals

- Nick Bostrom, *Superintelligence*。
- Stuart Russell, *Human Compatible*。
- NIST AI RMF、AI incident reporting、frontier model system card、AI Safety Institute 和 METR 资料可作为后续 Source Cards 候选。

## 与相邻域的关系

- 接收 `superhuman-intelligence-threshold/` 的能力阈值信号。
- 接收 `recursive-self-improvement-intelligence-explosion/` 的递归速度信号。
- 接收 `accelerating-returns-technology-convergence/` 的技术窗口收敛信号。
- 向 C3 `ai-agency-safety/`、C4 `model-cards-ai-audit-documentation/` 和 C4 研究转化域输出治理约束。
