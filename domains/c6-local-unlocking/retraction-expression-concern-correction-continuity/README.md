# Retraction Expression Concern Correction Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/retraction-expression-concern-correction-continuity` |
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

`retraction-expression-concern-correction-continuity/` 研究撤稿、表达关注、勘误、更正、版本更新和出版状态信号如何影响证据能否继续用于 Human Infra。

> 核心问题：一篇论文不是发表后就永久稳定；撤稿、expression of concern、correction 和 updated version 会改变它在模型中的地位。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要长期复用论文、综述、指南和模型证据
  -> 出版物状态会随撤稿、关注表达、勘误和版本更新改变
  -> 若模型不追踪出版状态，旧证据会在撤回后继续污染推理
  -> 因此撤稿/关注/更正连续性是证据时效与可信度的更新门槛
```

## 关注对象

- Retraction、expression of concern、correction、erratum、corrigendum、updated version、withdrawal 和 Crossmark 状态。
- 撤稿原因、影响范围、版本链、引用继续传播、二次综述修订和媒体更正。
- 与 `living-evidence-surveillance-update-continuity/` 的边界：活证据域关注持续监测；本域关注出版状态信号本身如何解释和传播。
- 与 `persistent-identifier-doi-citation-metadata-continuity/` 的边界：持久标识域关注对象解析；本域关注对象状态改变。

## Human Infra 模型链路

```text
撤稿/关注/更正状态 T
  -> 改变 publication_status、version_status、correction_reason、citation_warning 变量 X
  -> 改变 Source Card、系统综述、图表、论文页和模型输入状态 S
  -> 改变旧证据继续被引用、错误结论扩散和技术窗口误判风险 λ(t)
  -> 影响研究组合、传播材料、模型可信度和主体持续性决策
```

## 非目标

- 不提供撤稿规避、声誉洗白、引文操控、出版商申诉代写或法律意见。
- 不把撤稿等同于作者故意不端；撤稿原因必须分层记录。
- 不抓取受限出版系统、审稿系统或非公开撤稿材料。

## Source Signals

- COPE Retraction Guidelines: https://publicationethics.org/retraction-guidelines
- Crossref Crossmark: https://www.crossref.org/services/crossmark/
- Retraction Watch Database: https://retractiondatabase.org/
- ICMJE Corrections, Retractions and Expressions of Concern: https://www.icmje.org/recommendations/

## 下一步

- 给 Source Card 增加 `publication_status`、`correction_type`、`status_date`、`status_source` 和 `reuse_policy` 字段。
- 建立“已撤稿材料进入模型时必须降级或移除”的文档门槛。
