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
