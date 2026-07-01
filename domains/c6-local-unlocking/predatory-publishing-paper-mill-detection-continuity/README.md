# Predatory Publishing Paper Mill Detection Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/predatory-publishing-paper-mill-detection-continuity` |
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

`predatory-publishing-paper-mill-detection-continuity/` 研究掠夺性出版、paper mill、系统性伪造、操控同行评审和异常论文网络如何污染 Human Infra 证据。

> 核心问题：当低质量出版和 paper mill 把伪造或模板化论文送入检索系统，单纯“有 DOI/有期刊/可检索”不能证明证据可用。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要从海量论文中抽取可靠证据
  -> 检索系统会混入掠夺性出版、paper mill 和系统性操控产物
  -> 若不识别异常出版网络，系统综述和模型会放大伪证据
  -> 因此掠夺性出版与 paper mill 检测是证据污染防火墙
```

## 关注对象

- Predatory journal、paper mill、fake peer review、tortured phrases、image duplication、authorship sale、citation cartel 和 special issue manipulation。
- 出版商政策、期刊透明度、索引状态、撤稿网络、论文相似性和异常引用模式。
- 与 `publication-reporting-bias-detection-continuity/` 的边界：发表偏倚域关注选择性发表和报告；本域关注系统性伪造和出版生态污染。
- 与 `research-misconduct-investigation-correction-continuity/` 的边界：不端域关注调查和责任；本域关注筛查信号和证据防火墙。

## Human Infra 模型链路

```text
掠夺性出版与 paper mill 检测 T
  -> 改变 journal_transparency、paper_mill_signal、similarity_signal、review_integrity_signal 变量 X
  -> 改变论文进入系统综述、雷达和模型输入的过滤状态 S
  -> 改变伪证据累积、错误技术窗口、资源错配和公众误导风险 λ(t)
  -> 影响 Human Infra 研究组合、模型可信度和主体持续性判断
```

## 非目标

- 不提供绕过检测、伪造同行评审、论文买卖、引用操控、图片伪造、期刊黑名单服务或指控代写。
- 不基于单一异常信号断言某论文或作者不端。
- 不抓取受限稿件、审稿系统或私有数据库。

## Source Signals

- COPE paper mills and systematic manipulation resources: https://publicationethics.org/
- Think. Check. Submit.: https://thinkchecksubmit.org/
- Directory of Open Access Journals: https://doaj.org/
- STM Integrity Hub: https://www.stm-assoc.org/stm-integrity-hub/
- Retraction Watch Database: https://retractiondatabase.org/

## 下一步

- 建立 `paper_mill_signal` 的分层字段：journal transparency、image duplication signal、text anomaly、authorship anomaly、citation anomaly 和 retraction cluster。
- 与撤稿、系统综述筛选、引用传播和科研不端调查域建立交叉引用。
