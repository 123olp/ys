# Employment Algorithmic Hiring Screening Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/employment-algorithmic-hiring-screening-continuity` |
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

Employment Algorithmic Hiring Screening Continuity 关注 AI 招聘、自动化简历筛选、测评、视频面试、背景筛查、disparate impact 和合理便利如何影响主体进入工作、收入和技能增长路径。

## 对象

- Algorithmic hiring tools、resume screening、assessment tests、video interview scoring、job matching 和 automated employment decision systems。
- 数据偏差、代理变量、残障合理便利、透明度、告知、审计、申诉和人类复核。
- 招聘、晋升、排班、绩效、解雇、平台劳动和劳动力服务中的算法筛查层。

## Human Infra 价值

```text
主体持续性需要工作入口不被不透明算法错误排除
-> 工作入口决定收入、保险、身份、学习机会和社会参与
-> 自动化筛查会把数据偏差、代理变量和不可解释评分转成排除
-> 告知、审计、合理便利、人类复核和反歧视边界降低错误筛除
-> 能力更可能转化为真实工作机会和长期资源循环
```

## 边界

- 本域不提供求职优化、简历规避、面试作弊、背景调查规避、法律、劳动争议、歧视投诉或雇主合规建议。
- 不判断某招聘工具、雇主行为、测评结果或拒绝录用是否合法。
- 不替代 EEOC、DOL、州劳动机构、律师、雇主、工会、人力资源或残障权利机构。
- 只整理公开资料、算法机制、风险变量、治理边界、审计线索和禁止用途。

## 上游与下游

- 上游：`labor-rights-workplace-protection/`、`workforce-employment-services/`、`background-check-record-screening-continuity/`、`model-cards-ai-audit-documentation/`。
- 下游：`financial-resilience-access/`、`healthcare-access-continuity/`、`education-access-lifelong-learning/`、`administrative-burden-procedural-friction/`。

## 初始资料线索

- EEOC Artificial Intelligence and Algorithmic Fairness Initiative.
- EEOC technical assistance on AI and selection procedures.
- NIST AI Risk Management Framework.
