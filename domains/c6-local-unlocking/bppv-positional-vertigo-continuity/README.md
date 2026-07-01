# BPPV Positional Vertigo Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/bppv-positional-vertigo-continuity` |
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

BPPV positional vertigo continuity studies benign paroxysmal positional vertigo as a high-frequency vestibular failure mode where specific head positions can trigger brief vertigo, instability, activity avoidance, and fall exposure.

核心问题：

> 主体不是只需要“有移动能力”，还需要转头、躺下、起身、弯腰和转身这些日常姿势切换不触发空间错觉；BPPV 会把普通动作变成不可预测的眩晕触发器。

## 先验位置

```text
主体持续性最大化
  -> 主体必须能安全完成姿势切换和方向调整
  -> 内耳前庭信号必须与重力和头部位置保持可解释关系
  -> BPPV 使特定头位触发短暂眩晕、失衡和行动回避
  -> 因而 BPPV 是空间行动基础设施中的位置触发型失效模式
```

## 关注对象

- 位置性眩晕、头位触发、翻身、低头、仰头、起卧和转身。
- 眩晕发作对跌倒风险、驾驶/通勤担忧、睡眠姿势、工作任务和活动回避的影响。
- 与 `vestibular-balance-spatial-orientation/` 的关系：父域关注前庭平衡总框架；本域只关注 BPPV 这种位置触发型眩晕。
- 与 `fall-risk-prevention-home-safety-continuity/` 的关系：后者关注家庭防跌倒系统；本域关注头位-前庭信号失配。

## Human Infra 模型链路

```text
识别 / 转诊 / 前庭评估 / 康复路径 T
  -> 改变位置性眩晕触发、姿势切换信心和回避行为 X
  -> 改变移动半径、睡眠姿势、工作动作和跌倒暴露状态 S
  -> 改变跌倒、活动减少、孤立和有效时间损耗风险 λ(t)
  -> 影响行动密度、独立生活、任务完成和未来选择权
```

## 非目标

- 不提供 BPPV 诊断、体位试验解释、复位手法、康复动作、药物或急诊判断。
- 不根据个人眩晕描述判断是否 BPPV、是否可开车、是否需要影像或是否需要急诊。
- 不替代耳鼻喉、神经、前庭康复、物理治疗或急诊专业服务。

## Source Signals

- NIDCD balance disorders resources。
- Mayo Clinic BPPV overview as clinical education context。
- CDC STEADI fall prevention resources as downstream risk context。
