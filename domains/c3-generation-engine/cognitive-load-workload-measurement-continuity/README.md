# Cognitive Load Workload Measurement Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/cognitive-load-workload-measurement-continuity` |
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

Cognitive Load Workload Measurement Continuity 研究任务负荷、认知负荷、时间压力、挫败感和工作记忆限制如何影响主体持续行动、学习和安全执行。

> 核心问题：很多失败不是“不努力”，而是任务把人的工作记忆、注意力和恢复能力推过了负荷边界。

## 研究对象

- Cognitive load、mental workload、NASA-TLX、工作记忆限制、任务复杂度、信息密度和时间压力。
- 学习材料、工作界面、AI 工具、操作流程和高压任务中的负荷测量与负荷设计。
- 负荷如何影响错误率、学习速度、疲劳、依从、创造密度和有效时间。

## 先验链路

```text
主体执行复杂任务需要有限认知资源
  -> 任务负荷占用工作记忆、注意力、时间和情绪恢复能力
  -> 负荷超过边界会导致遗漏、误判、放弃、学习失败和疲劳累积
  -> 单位时间行动质量下降，任务成本和恢复成本上升
  -> 长期学习轮次、试错轮次和创造密度下降
  -> 因而认知负荷是主体持续性的任务资源消耗层
```

## 关键变量

- Mental demand、physical demand、temporal demand、effort、frustration、perceived performance。
- 信息量、步骤数、切换成本、界面密度、先验知识、反馈延迟和错误恢复成本。
- 把负荷测量用于绩效压迫、个体筛除、心理诊断或算法管理的风险。

## 证据入口

- NASA Task Load Index / Hart and Staveland NASA-TLX。
- Cognitive Load Theory 相关论文。
- Human-AI interaction guidelines and workload literature。

## 非目标

- 本域不提供心理诊断、学习障碍诊断、个人效率处方、绩效评分或招聘筛选方案。
- 不把 NASA-TLX 或负荷量表用作临床工具、惩罚工具或个体能力标签。
- 不收集个人心理状态、工作监控、学习成绩、生产率、医疗或学校个案资料。

## 上下游

- 上游：`attention-executive-control/`、`learning-skill-acquisition/`、`human-factors-ergonomics-task-system-continuity/`。
- 下游：`alert-fatigue-interruption-signal-management-continuity/`、`situational-awareness-decision-environment-continuity/`、`automation-bias-mode-confusion-oversight-continuity/`。
