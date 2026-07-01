# Geroprotective Drug Repurposing Trial Governance Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/geroprotective-drug-repurposing-trial-governance-continuity` |
| 分级 | `C4` - 可能性转换通道层 |
| 控制轴 | 路径转换接口 |
| 分级理由 | 关键词显示该域主要处理研究、数据、模型、服务入口、身份记录、转化或治理接口。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何把潜在可能性转成真实可用路径，例如研究、医疗、数据、制度、身份、资金或转化接口？

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

- 界定转化瓶颈：研究发现、数据、临床、制度、身份、资金、可及性或操作接口。
- 说明接口机制：潜在可能性如何经过标准、流程、记录、组织或平台变成可用路径。
- 记录必要证据：登记系统、指南、监管材料、数据库、标准文档或真实世界部署资料。
- 识别摩擦指标：时间成本、资金成本、信息成本、合规成本、可及性和协作成本。
- 列出失败点：证据断裂、监管阻塞、制度排斥、隐私风险、责任不清或资源不可达。

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

`geroprotective-drug-repurposing-trial-governance-continuity/` 研究 metformin、rapamycin、acarbose、canagliflozin、NAD+ 相关分子和其他候选 geroprotective agents 如何从动物实验、机制叙事、药物再利用和临床试验治理进入 Human Infra。

> 核心问题：抗衰药物候选不是“延寿变量”。它们只有在明确终点、剂量、适用对象、安全监测、试验设计和证据等级后，才可能进入主体持续性模型。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要降低慢病、衰弱、失能和死亡风险
  -> 药物再利用可能影响衰老相关通路和多病共因
  -> 动物寿命延长、机制合理性和人体可及性不能自动推出人体健康寿命收益
  -> 因此 geroprotective drug repurposing 必须进入试验治理和证据边界域
```

## 关注对象

- NIA Interventions Testing Program、TAME-style 试验设想、MILES、PEARL、rapalogs、mTOR、AMPK、糖代谢药物和多病终点设计。
- 动物寿命、健康寿命、frailty、sarcopenia、认知、代谢、感染、肿瘤、免疫抑制和药物相互作用。
- 药物再利用的证据层级：机制、模型动物、多中心动物寿命、人体 biomarker、RCT、真实终点、长期安全性。
- 与 `longevity-evidence/` 的边界：长寿证据域保存证据账本；本域审查药物再利用进入试验和治理模型的条件。
- 与 `pharmacovigilance-drug-safety-monitoring/` 的边界：药物安全域关注上市后安全信号；本域关注 anti-aging 语境下的再利用和试验边界。

## Human Infra 模型链路

```text
候选抗衰药物 T
  -> 影响 mTOR、AMPK、代谢、炎症、细胞衰老、免疫和组织修复变量 X
  -> 改变身体状态 S 和多病风险组合
  -> 改变风险函数 lambda(t)、失能时间和健康寿命曲线
  -> 若证据、剂量、安全和可及性不足，则阻塞进入主体持续性模型
```

## 非目标

- 不提供药物、剂量、处方、离标签使用、购买、联合用药、停药、检测或个体医学建议。
- 不把小鼠寿命、动物健康指标、机制通路或商业临床项目写成人体延寿结论。
- 不替代监管、伦理、药品安全、临床试验或医生判断。
- 不整理 DIY 抗衰药物方案、灰色市场、进口规避或试验入组策略。

## Source Signals

- NIA Interventions Testing Program: https://www.nia.nih.gov/research/dab/interventions-testing-program-itp/about-itp
- NIA ITP supported interventions: https://www.nia.nih.gov/research/dab/interventions-testing-program-itp/supported-interventions
- NIA ITP design paper: https://pmc.ncbi.nlm.nih.gov/articles/PMC2585647/
- NIA ITP overview: https://pmc.ncbi.nlm.nih.gov/articles/PMC5514387/
- Rapamycin and aging review: https://pubmed.ncbi.nlm.nih.gov/25269671/

## 下一步

1. 建立 geroprotective candidates 的 Source Card：物种、剂量、终点、性别差异、安全信号和证据等级。
2. 把药物再利用拆成 trial governance、pharmacovigilance、access、off-label hype 四个审查门。
3. 与 `survival-analysis-healthspan-risk-modeling/`、`causal-inference-target-trial-emulation/` 和 `biological-age-clocks-biomarker-validation/` 建立变量接口。
