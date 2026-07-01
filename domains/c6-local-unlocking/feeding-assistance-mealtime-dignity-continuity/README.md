# Feeding Assistance Mealtime Dignity Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/feeding-assistance-mealtime-dignity-continuity` |
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

Feeding assistance mealtime dignity continuity studies how human help, timing, environment, adaptive tools, social context, and care quality determine whether people can eat safely, sufficiently, and with dignity.

核心问题：

> 进食不是把热量送入口中；它是时间、姿势、节奏、帮助、关系和尊严共同维护的日常主体活动。

## 先验位置

```text
主体持续性最大化
  -> 主体必须把营养摄入转化为可承受、可持续、可尊严的日常活动
  -> 吞咽困难、残障、衰弱或认知下降可能使独立进食失效
  -> 进食协助质量影响摄入量、误吸暴露、照护关系和主体尊严
  -> 因而进食协助是营养入口和人格尊严之间的照护基础设施
```

## 关注对象

- 喂食协助、用餐时间、姿势支持、辅助餐具、人员培训、长期照护、社交餐食、进食尊严和照护者负担。
- 与 `caregiving-long-term-care/` 的关系：照护域关注长期照护系统；本域关注用餐执行。
- 与 `dignity-personhood-respect-continuity/` 的关系：尊严域关注人格尊重；本域关注进食场景中的尊严。

## Human Infra 模型链路

```text
人员协助 / 用餐环境 / 辅助工具 / 时间安排 T
  -> 改变摄入量、进食速度、误吸暴露、关系体验和尊严变量 X
  -> 改变营养状态、情绪恢复、照护负担和社会参与状态 S
  -> 改变营养不足、脱水、误吸、孤立、拒食和照护崩溃风险 λ(t)
  -> 影响有效时间、生活质量和未来选择权
```

## 非目标

- 不提供喂食技巧、姿势、速度、饮食质地、人员培训方案、护理处置、机构合规判断或虐待判定。
- 不根据个体进食表现、照护环境或机构记录判断服务质量和责任。
- 不替代护理、营养、言语语言治疗、职业治疗、长期照护监管或法律服务。

## Source Signals

- CMS paid feeding assistant and long-term-care materials。
- ASHA adult dysphagia and pediatric feeding/swallowing materials。
- Person-centered care and dignity literature as research context。
