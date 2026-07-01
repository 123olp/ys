# Overactive Bladder, Nocturia and Sleep Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/overactive-bladder-nocturia-sleep-continuity` |
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

`overactive-bladder-nocturia-sleep-continuity/` 研究尿急、尿频、夜尿、睡眠中断、跌倒风险、工作疲劳和社交限制如何影响主体持续性。

> 核心问题：膀胱症状不只是局部问题，它会通过睡眠破坏、注意力下降、出行回避、跌倒风险和羞耻成本压缩有效时间。

## 先验位置

```text
有效永生
  -> 主体需要稳定睡眠和可预测行动半径
  -> 尿急尿频夜尿会打断恢复、工作和外出
  -> 因此 OAB / nocturia 是排泄节律影响有效时间的域
```

## 关注对象

- Overactive bladder, urgency, frequency, nocturia, sleep interruption, fall risk, social avoidance, workplace fatigue, continence access boundaries。
- 与 `pelvic-floor-continence-function-continuity/` 的关系：盆底域覆盖控尿控便和功能参与，本域聚焦膀胱节律、夜间恢复和行动半径。

## Human Infra 模型链路

```text
膀胱节律与夜间中断 T
  -> 改变夜醒、睡眠质量、疲劳、出行回避和跌倒暴露 X
  -> 改变恢复状态、注意力、工作可靠性和社交参与 S
  -> 改变失能、跌倒、抑郁、照护依赖和有效时间损失 lambda(t)
  -> 改变健康寿命和未来选择权
```

## 非目标

- 不提供 OAB 诊断、药物、盆底训练、饮水安排、夜尿处理、检查解释、设备或个体治疗建议。
- 不输出个人睡眠/跌倒风险、工作许可、驾驶许可或保险证明。

## Source Signals

- NIDDK bladder control problems.
- MedlinePlus overactive bladder and nocturia public materials.
- NIA falls / sleep public materials for downstream burden boundary.
