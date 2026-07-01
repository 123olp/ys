# Inflammaging Chronic Low Grade Inflammation Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/inflammaging-chronic-low-grade-inflammation-continuity` |
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

Inflammaging Chronic Low Grade Inflammation Continuity 负责整理炎症衰老、慢性低度炎症、免疫代谢、组织损伤信号和多病共存风险。

核心问题：

> 慢性低度炎症不是单一疾病，而是多个衰老、感染、代谢、组织损伤和社会环境因素汇合后的系统状态；它会持续抬高风险底噪并压缩恢复能力。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要长期保持低损伤、可恢复、可适应的系统状态
  -> 年龄、感染、代谢失衡、衰老细胞、组织损伤和压力暴露会累积炎症信号
  -> 慢性低度炎症会影响心血管、代谢、神经、免疫和癌症风险
  -> 风险底噪升高会降低恢复能力、行动质量和健康寿命
  -> 因此 inflammaging 是连接多个机制域的系统性风险条件
```

## 关注对象

- inflammaging、chronic low-grade inflammation、immune-metabolic crosstalk、CRP/IL-6/TNF 等炎症信号边界。
- 衰老细胞、感染、肥胖、睡眠、压力、污染、牙周炎、肠道屏障和社会逆境的交叉影响。
- 与 `cellular-senescence-clearance/` 的关系：衰老细胞/SASP 是来源之一，不是全部 inflammaging。
- 与 `immune-maintenance/` 的关系：本域关注低度慢炎症状态；免疫域关注整体防御、耐受和监视。

## Human Infra 模型链路

```text
炎症调节 / 暴露治理 T
  -> 改变慢性炎症信号、免疫代谢和组织损伤反馈 X
  -> 改变系统恢复与风险底噪状态 S
  -> 改变心血管、代谢、神经退行、癌症、感染和衰弱风险
  -> 改变健康寿命、有效时间和主体行动稳定性
```

## 非目标

- 不提供抗炎药、补剂、饮食、运动、睡眠、检验解读或个体治疗建议。
- 不把单一炎症指标下降写成寿命延长。
- 不把 inflammaging 作为包打天下的解释，必须追问上游来源和下游终点。

## Source Signals

- NIA Biology of Aging Program: https://www.nia.nih.gov/research/dab/biology-aging-program
- Immune aging, immunosenescence, and inflammaging review: https://pmc.ncbi.nlm.nih.gov/articles/PMC12286891/
- Chronic inflammation and the hallmarks of aging: https://pmc.ncbi.nlm.nih.gov/articles/PMC10359950/
