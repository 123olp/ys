# Inflammatory Bowel Disease Digestive Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/inflammatory-bowel-disease-digestive-continuity` |
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

`inflammatory-bowel-disease-digestive-continuity/` 研究 Crohn 病、溃疡性结肠炎、消化道炎症、营养吸收、flare、用药监测和长期生活参与如何影响主体持续性。

> 核心问题：炎症性肠病把免疫炎症、腹痛腹泻、营养损耗、医疗监测、手术风险和污名共同转化为有效时间和行动半径的长期损耗。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要稳定吸收营养、维持体力并可预测地参与生活
  -> IBD 会造成 flare、疼痛、腹泻、疲劳、营养缺口和治疗风险
  -> 结果取决于早诊、疾病控制、营养支持、药物监测、手术路径和心理社会支持
  -> 因此 IBD 是消化连续性、免疫稳态和有效时间保护的关键维护域
```

## 关注对象

- Crohn's disease、ulcerative colitis、flare、bowel symptoms、nutrition, anemia, biologics / immunomodulators, surgery pathway, school/work participation。
- 与 `gastrointestinal-barrier-absorption/` 的边界：该域关注胃肠屏障和吸收总机制；本域聚焦 IBD 的慢性炎症病程和照护连续性。
- 与 `chronic-pain-functional-restoration-continuity/` 的关系：腹痛和疲劳会把 IBD 转化为任务中断与有效时间损耗。

## Human Infra 模型链路

```text
IBD 消化连续性照护系统 T
  -> 改变炎症活动、腹痛腹泻、营养吸收、贫血、用药监测和手术路径变量 X
  -> 改变体力、学校/工作参与、心理负担、医疗利用和社会活动状态 S
  -> 改变失能风险、营养风险、感染/治疗风险和有效时间损耗 λ(t)
  -> 影响主体长期行动能力、恢复能力和未来选择权
```

## 非目标

- 不提供个人 IBD 诊断、内镜/化验判读、饮食、药物、生物制剂、免疫抑制、手术、flare 处理或疫苗建议。
- 不生成治疗计划、营养计划、用药调整、检查周期、厕所/学校/工作便利或保险建议。
- 不收集个案症状、内镜、化验、药物、营养、学校/工作或保险资料。

## Source Signals

- NIDDK Crohn's disease: https://www.niddk.nih.gov/health-information/digestive-diseases/crohns-disease
- NIDDK ulcerative colitis: https://www.niddk.nih.gov/health-information/digestive-diseases/ulcerative-colitis
- CDC IBD information: https://www.cdc.gov/ibd/

## 下一步

- 建立 IBD Continuity Card：disease type, flare burden, nutrition/anemia, medication monitoring, surgery pathway, participation support。
- 与 `gastrointestinal-barrier-absorption/`、`immune-maintenance/` 和 `iron-deficiency-anemia-oxygen-carrying-continuity/` 建立接口。
