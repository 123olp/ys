# Insurance Underwriting Algorithmic Risk Scoring Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/insurance-underwriting-algorithmic-risk-scoring-continuity` |
| 分级 | `C5` - 可能性生态承载层 |
| 控制轴 | 外部生态承载 |
| 分级理由 | 关键词显示该域主要承载能源、水、食物、住房、治理、经济、通信、灾害或基础设施环境。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何承载主体展开未来的外部世界条件，例如能源、水、食物、住房、通信、治理、经济和基础设施？

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

- 界定外部承载条件：能源、水、食物、住房、通信、交通、治理、经济或公共基础设施。
- 说明它如何改变主体展开未来所需的稳定性、冗余、可获得性和安全边界。
- 记录基础设施依赖：供应链、地理环境、制度、资金、维护能力和公共服务。
- 识别冲击场景：灾害、战争、断供、污染、气候、系统失灵或社会支持崩溃。
- 建立韧性指标：可用率、恢复时间、冗余、成本、覆盖范围、可负担性和风险暴露。

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

Insurance Underwriting Algorithmic Risk Scoring Continuity 关注保险承保、风险评分、费率、索赔自动化、外部数据、AI 模型和公平性治理如何影响主体获得风险转移和损失恢复的能力。

## 对象

- Insurance underwriting、risk scoring、premium rating、claims automation、external consumer data and information sources、AI/model governance。
- 健康、生命、车险、房屋、灾害、残障和长期照护保险中的准入、价格、拒保和理赔判定。
- 数据质量、代理变量、歧视性影响、模型透明度、监管审查、申诉和消费者保护。

## Human Infra 价值

```text
主体持续性需要风险转移入口不被不透明评分错误关闭
-> 保险把高成本风险从个体转移到风险池
-> 算法评分和外部数据会影响承保、费率、拒保和索赔恢复
-> 数据准确性、模型治理、监管审查和申诉机制降低错误排除
-> 疾病、事故、灾害和失能冲击更可能被风险池接住
```

## 边界

- 本域不提供保险购买、理赔、承保、保费、投资、法律、投诉、核保规避或个案申诉建议。
- 不判断某保险产品、模型、费率、拒保或理赔决定是否合法或划算。
- 不替代 NAIC、州保险监管机构、保险公司、经纪人、律师、精算师或消费者保护机构。
- 只整理公开资料、算法风险、监管框架、数据边界、消费者保护和禁止用途。

## 上游与下游

- 上游：`insurance-risk-transfer/`、`health-economics-value-assessment/`、`model-cards-ai-audit-documentation/`、`uncertainty-quantification-model-calibration/`。
- 下游：`financial-resilience-access/`、`disaster-recovery-relief-continuity/`、`healthcare-access-continuity/`、`housing-built-environment-stability/`。

## 初始资料线索

- NAIC artificial intelligence and insurance regulatory materials.
- State insurance regulator consumer protection resources.
- NIST AI Risk Management Framework.
