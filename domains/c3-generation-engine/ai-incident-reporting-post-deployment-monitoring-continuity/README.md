# AI Incident Reporting Post Deployment Monitoring Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/ai-incident-reporting-post-deployment-monitoring-continuity` |
| 分级 | `C3` - 可能性生成引擎层 |
| 控制轴 | 主体能力生成 |
| 分级理由 | 关键词显示该域主要增强认知、学习、工具、AI、技能或沟通能力。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何放大主体生成新路径的能力，例如认知、学习、注意力、记忆、AI、工具和反馈复利？

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

- 界定被放大的通用能力资源：智力、注意力、记忆、学习、判断、执行、反馈或工具使用。
- 说明任务链路：能力变化如何改变问题求解、行动质量、创造密度或学习轮次。
- 识别复利结构：能力增强、工具采用、协作网络、经验积累和自我升级如何互相强化。
- 记录依赖条件：AI、数据、界面、训练、外部工具、社会支持或反馈系统。
- 列出误用、过载、依赖、幻觉、注意力破坏、人格边界和安全风险。

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

`ai-incident-reporting-post-deployment-monitoring-continuity/` 研究 AI 事故报告、部署后监控、漂移告警、用户反馈、纠错学习和停用升级机制，如何让 AI 系统在真实世界中持续可审查。

> 核心问题：AI 风险不会在上线前全部暴露。若部署后没有监控、事故记录和纠错机制，AI 增强会从能力工具变成不可见风险源。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要 AI 工具长期参与真实任务
  -> 真实任务会暴露评测阶段未覆盖的分布漂移、误用、事故和社会反馈
  -> 若事故不可报告、不可追踪、不可纠错，主体会重复暴露在同类风险中
  -> 因此 AI 事故报告与部署后监控是 AI 长期可用性的学习系统域
```

## 关注对象

- 事故报告、near miss、用户反馈、模型漂移、性能退化、安全告警、审计日志和停用升级。
- 事故分类、影响范围、根因分析、纠正措施、复发检查、版本回滚和发布后治理。
- AI 事件数据库、行业事故监测、监管报告、组织内部 incident response 与公众透明度。
- 与 `incident-reporting-just-culture-learning-continuity/` 的关系：该域关注人因与组织学习；本域关注 AI 部署后的事件系统。
- 与 `trustworthy-scientific-communication-peer-review/` 的边界：科研传播域关注论文传播；本域关注上线后的 AI 系统事故。

## Human Infra 模型链路

```text
AI 事故报告与部署后监控 T
  -> 改变事故可见性、漂移信号、用户反馈、根因记录和纠错速度变量 X
  -> 改变 AI 系统运行状态、回滚状态、警戒状态和发布策略 S
  -> 改变重复事故、隐性伤害、过度依赖和长期风险积累 λ(t)
  -> 影响主体安全、协作信任、有效时间和技术采用能力
```

## 非目标

- 不提供攻击复现、事故利用、泄露材料扩散、舆论操控或监管规避方法。
- 不替代组织安全团队、法律、监管、事故响应或平台官方渠道。
- 不把事故监控写成对个人或员工的惩罚性监控工具。

## Source Signals

- OECD AI Incidents Monitor: https://oecd.ai/en/incidents
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- NIST AI RMF Generative AI Profile: https://www.nist.gov/itl/ai-risk-management-framework/generative-artificial-intelligence-profile
- AI Incident Database: https://incidentdatabase.ai/
- EU AI Act information portal: https://artificialintelligenceact.eu/

## 下一步

- 建立 AI Incident Source Card 字段：incident type, affected task, version, monitoring signal, root cause, correction, residual risk。
- 与 `ai-data-provenance-contamination-drift-continuity/` 和 `ai-resource-cost-latency-budget-continuity/` 建立部署后漂移与运行预算接口。
