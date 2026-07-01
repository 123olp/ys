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
