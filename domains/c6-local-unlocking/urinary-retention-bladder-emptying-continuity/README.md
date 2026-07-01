# Urinary Retention and Bladder Emptying Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/urinary-retention-bladder-emptying-continuity` |
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

`urinary-retention-bladder-emptying-continuity/` 研究急性/慢性尿潴留、膀胱排空失败、梗阻、神经源性因素、导尿依赖和肾脏上游压力如何影响主体持续性。

> 核心问题：尿液不能排出时，排泄系统会从后台稳态变成疼痛、感染、肾积水、急性服务依赖和行动中断。

## 先验位置

```text
有效永生
  -> 主体必须持续排出液体废物
  -> 膀胱排空失败会造成疼痛、感染和肾脏压力
  -> 因此尿潴留是排泄出口连续性的基础断点
```

## 关注对象

- Acute urinary retention, chronic retention, bladder emptying, obstruction, neurogenic bladder context, catheter dependency, hydronephrosis risk, pain and urgent access。
- 与 `benign-prostatic-hyperplasia-luts-continuity/` 的关系：BPH 域关注常见下尿路症状来源，本域覆盖所有排空失败机制。

## Human Infra 模型链路

```text
排空失败识别与通道恢复 T
  -> 改变膀胱压力、疼痛、感染、肾脏上游压力和设备依赖 X
  -> 改变排泄安全、睡眠、行动、工作和急性服务状态 S
  -> 改变 AKI、感染、住院、跌倒和长期照护依赖 lambda(t)
  -> 改变有效时间和未来选择权
```

## 非目标

- 不提供导尿操作、药物、设备、急诊判断、检查解释、神经源性膀胱管理或个体治疗建议。
- 不输出个人潴留风险、排尿量判断、影像/尿流检查解读或返工/旅行许可。

## Source Signals

- NIDDK urinary retention materials.
- MedlinePlus urinary retention public materials.
- AUA / professional lower urinary tract references for terminology boundary.
