# Endocrine Hormonal Regulation

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/endocrine-hormonal-regulation` |
| 分级 | `C2` - 可能性源体维护层 |
| 控制轴 | 生命载体维护 |
| 分级理由 | 直接维护身体、脑、器官、衰老、损伤或生命系统这些可能性源体。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何维护产生可能性的生命载体，例如身体、脑、器官、细胞、急性生命风险或衰老损伤控制？

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

- 界定生命载体变量：细胞、组织、器官、脑、免疫、代谢、急性风险或衰老损伤。
- 说明影响机制：修复、替换、再生、控制、筛查、预防、维持或风险降低。
- 列出可观察状态：功能指标、生物标志物、疾病终点、失能时间、恢复能力或死亡风险。
- 记录副作用、过度干预、癌变、免疫、长期安全性和尾部风险。
- 区分机制合理性、体外证据、动物证据、人体早期数据、临床终点和长期安全性。

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

Endocrine Hormonal Regulation 负责整理内分泌系统、激素轴、代谢信号、压力反应、生长、生殖、骨骼和情绪调节如何支撑主体持续性。

核心问题：

> 主体不是一堆独立器官，而是被激素信号长期协调的动态系统；激素失衡会把代谢、睡眠、情绪、骨骼、免疫和生殖同时推入风险状态。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体必须长期维持跨器官协调
  -> 激素系统调度能量、压力、生长、修复、生殖、骨骼和昼夜节律
  -> 内分泌失衡会改变代谢状态、认知情绪、组织维护和疾病风险
  -> 因此内分泌激素调节是跨系统稳态域
```

## 关注对象

- 甲状腺、胰岛、肾上腺、性腺、垂体、下丘脑和骨代谢相关激素轴。
- 胰岛素、皮质醇、甲状腺激素、性激素、生长激素、维生素 D / PTH 等状态变量。
- 糖尿病、甲状腺疾病、肾上腺异常、骨质疏松、生殖衰退、压力轴紊乱。
- 激素系统与代谢、睡眠、心理、免疫、肌骨、心血管和衰老机制的交叉。

## Human Infra 模型链路

```text
内分泌状态或干预 T
  -> 改变激素水平、受体敏感性、反馈环和跨器官信号 X
  -> 改变代谢、修复、情绪、睡眠、骨骼和免疫状态 S
  -> 改变慢病、失能、认知情绪崩塌和死亡风险 λ(t)
  -> 影响有效时间、恢复能力和长期行动窗口
```

## 非目标

- 不提供激素检测解释、补充、处方、剂量、停药、周期管理或治疗建议。
- 不把单个激素指标写成寿命预测或主体能力判断。
- 不替代 `nutrition-metabolic-health/`、`sleep-circadian-recovery/`、`mental-health-affective-stability/` 或 `musculoskeletal-integrity/`。

## Source Signals

- NIDDK endocrine diseases: https://www.niddk.nih.gov/health-information/endocrine-diseases
- NIDDK diabetes overview: https://www.niddk.nih.gov/health-information/diabetes
- Endocrine Society hormone health resources: https://www.endocrine.org/patient-engagement/endocrine-library

## 下一步

1. 建立激素轴变量表：轴、信号、反馈、目标器官、失败模式和证据类型。
2. 与 `nutrition-metabolic-health/`、`sleep-circadian-recovery/`、`mental-health-affective-stability/` 和 `musculoskeletal-integrity/` 建立边界。
