# Hypertensive Crisis End Organ Risk Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/hypertensive-crisis-end-organ-risk-continuity` |
| 分级 | `C2` - 可能性源体维护层 |
| 控制轴 | 生命载体维护 |
| 分级理由 | 关键词显示该域主要维护身体、脑、器官、细胞、急性生命风险或衰老损伤控制。 |
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

`hypertensive-crisis-end-organ-risk-continuity/` 研究高血压危象、急性靶器官风险、脑/心/肾/主动脉事件、诊断接入和长期血压治理交接如何影响主体持续性。

> 核心问题：血压不是孤立数字，而是脑、心、肾和血管壁承受的机械负荷。高血压危象需要被建模为急性靶器官损伤窗口，而不是泛化的慢性血压管理。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖血管压力处在器官可承受范围内
  -> 极端血压和靶器官损伤会快速改变卒中、心衰、肾损伤和主动脉风险
  -> 结果取决于识别、诊断接入、急性稳定和长期交接
  -> 因此高血压危象是血管负荷进入急性器官风险的研究域
```

## 关注对象

- Hypertensive emergency / urgency distinction as system concept, end-organ injury, stroke link, acute heart failure, AKI, aortic syndromes, access to follow-up, medication continuity。
- 与 `cardiovascular-resilience/` 的边界：该域关注长期血压风险；本域关注急性靶器官损伤和连续性断点。
- 与 `cerebrovascular-stroke-brain-perfusion-resilience/` 和 `acute-kidney-injury-renal-replacement-continuity/` 的关系：高血压危象可进入脑、心、肾急性事件。

## Human Infra 模型链路

```text
高血压危象治理系统 T
  -> 改变测量可信度、识别延迟、靶器官评估、急性稳定和随访变量 X
  -> 改变脑灌注、心脏负荷、肾功能、血管事件和用药连续性 S
  -> 改变卒中、心衰、AKI、主动脉事件和死亡风险 λ(t)
  -> 影响主体存活、认知、行动和未来选择权
```

## 非目标

- 不提供血压读数判断、急诊分诊、降压药、剂量、家庭处理、用药调整、检查选择或个体治疗建议。
- 不生成高血压危象评分、监测工具、药物路径、家庭血压解释或预后判断。
- 不收集个案血压、症状、化验、影像、用药、设备或位置数据。

## Source Signals

- AHA high blood pressure guideline materials: https://professional.heart.org/
- CDC high blood pressure materials: https://www.cdc.gov/high-blood-pressure/
- NHLBI high blood pressure materials: https://www.nhlbi.nih.gov/health/high-blood-pressure

## 下一步

- 建立 Hypertensive Crisis Card：measurement, symptoms, end-organ screen, acute stabilization boundary, follow-up continuity。
- 与 `cardiovascular-resilience/`、`cerebrovascular-stroke-brain-perfusion-resilience/` 和 `acute-kidney-injury-renal-replacement-continuity/` 建立接口。
