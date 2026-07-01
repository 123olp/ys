# Replication Reproducibility Many Labs Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/replication-reproducibility-many-labs-continuity` |
| 分级 | `C6` - 局部可能性解锁层 |
| 控制轴 | 局部阻塞解除 |
| 分级理由 | 未命中更高层边界、载体、能力、转换或生态规则，暂归为具体场景的局部可能性解锁。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域解除的是哪一个具体疾病、流程、服务、职业、家庭、社区或专项风险中的局部阻塞？

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

- 界定局部阻塞：某一疾病、流程、服务、职业、家庭、社区或专项风险中的具体失败点。
- 说明受影响任务：它阻碍了主体完成什么行动、服务、照护、转换或恢复过程。
- 记录可测改善：等待时间、错误率、成本、可及性、完成率、伤害率或恢复速度。
- 明确升级边界：何时应转交 C2-C5 的上层生命、能力、转化或基础设施域。
- 避免把局部改良包装成根本性解决方案，必须标注适用范围和外部依赖。

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

`replication-reproducibility-many-labs-continuity/` 研究复制研究、复现实验、多实验室协作、再分析和结果稳健性如何影响 Human Infra 证据可靠性。

> 核心问题：单一研究即使发表也可能不可复制；主体持续性模型需要知道结论是否能在不同数据、实验室、方法和人群中重复出现。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要把技术和干预放入长期决策模型
  -> 单次研究结果可能来自偶然、偏倚、过拟合或情境依赖
  -> 复制、复现、多实验室验证和再分析决定结果稳健性
  -> 因此复制/复现/多实验室连续性是证据从信号变成可靠输入的门槛
```

## 关注对象

- Replication、reproducibility、robustness、multisite study、Many Labs、reanalysis、registered replication report 和 computational reproducibility。
- 直接复制、概念复制、独立数据再分析、跨实验室异质性和失败复制解释。
- 与 `research-software-capsule-reproducibility-continuity/` 的边界：软件胶囊域关注计算环境；本域关注研究结论跨团队和情境是否稳健。
- 与 `meta-analysis-effect-size-heterogeneity-continuity/` 的边界：Meta 域量化多研究效应；本域关注复制设计和失败解释。

## Human Infra 模型链路

```text
复制复现与多实验室验证 T
  -> 改变 replication_status、reproducibility_status、cross_site_heterogeneity、robustness 变量 X
  -> 改变效应估计、证据确定性和模型输入可信状态 S
  -> 改变不可复制结论、过拟合、场景外推和技术采用误判风险 λ(t)
  -> 影响长期研究组合、模型校准和主体持续性路径判断
```

## 非目标

- 不提供数据伪造、复现实验操控、显著性追逐、论文代写、实验规避或对作者的不端指控。
- 不把失败复制自动解释为原研究错误；必须记录情境、方法和样本差异。
- 不提供湿实验、人体实验或临床操作协议。

## Source Signals

- National Academies, Reproducibility and Replicability in Science: https://nap.nationalacademies.org/catalog/25303/reproducibility-and-replicability-in-science
- Center for Open Science: https://www.cos.io/
- Many Labs projects, Center for Open Science: https://www.cos.io/initiatives
- Registered Reports, Center for Open Science: https://www.cos.io/initiatives/registered-reports
- OSF Registries: https://osf.io/registries

## 下一步

- 给 Source Card 增加 `replication_status`、`reproducibility_package`、`multisite_signal`、`failed_replication_context` 和 `robustness_note` 字段。
- 与 Meta 分析、风险偏倚、预注册和研究软件胶囊域建立复核链。
