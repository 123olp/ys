# Enteral Feeding Tube Nutrition Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/enteral-feeding-tube-nutrition-continuity` |
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

Enteral feeding tube nutrition continuity studies non-oral nutrition pathways when swallowing or intake is insufficient, focusing on nutrition delivery continuity, device dependence, infection risk, caregiver burden, dignity, and decision boundaries.

核心问题：

> 管饲不是“营养自动解决”，而是把营养入口转移到设备、护理、供应、并发症和决策权共同维护的外部系统。

## 先验位置

```text
主体持续性最大化
  -> 主体必须持续获得水分、能量和药物
  -> 口服路径不足时可能需要非口服营养通道
  -> 管路、配方、泵、护理、感染和供应链成为新的单点失效
  -> 因而管饲营养连续性是吞咽失败后的外部入口基础设施
```

## 关注对象

- 鼻胃管、胃造瘘、肠造瘘、配方供应、管路维护、泵、感染、堵管、照护者负担和意愿决策。
- 与 `nutrition-metabolic-health/` 的关系：营养域关注营养状态；本域关注管饲入口和执行链。
- 与 `advance-care-planning-medical-decision-continuity/` 的关系：决策域关注意愿和代理；本域只整理管饲作为研究对象。

## Human Infra 模型链路

```text
营养评估 / 管饲路径 / 供应链 / 护理流程 T
  -> 改变能量水分进入、设备依赖、感染风险和照护负担变量 X
  -> 改变营养状态、家庭执行、尊严和医疗依赖状态 S
  -> 改变营养不足、脱水、感染、住院和照护崩溃风险 λ(t)
  -> 影响恢复能力、主体自主性和未来选择权
```

## 非目标

- 不提供管饲适应证、置管选择、配方、速率、冲管、护理、并发症处理或伦理决策建议。
- 不根据个体吞咽、体重、疾病、管路或营养数据判断是否需要管饲。
- 不替代营养、胃肠、外科、护理、言语语言治疗、伦理咨询或临床服务。

## Source Signals

- ASPEN / ESPEN enteral nutrition guideline materials as professional context。
- MedlinePlus feeding tube public medical materials。
- Long-term care and home health literature as implementation context。
