# Acute Heart Failure Decompensation Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/acute-heart-failure-decompensation-continuity` |
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

`acute-heart-failure-decompensation-continuity/` 研究急性心衰失代偿、容量负荷、肺水肿、低灌注、急诊/住院路径、再入院和功能恢复如何影响主体持续性。

> 核心问题：心衰失代偿不是单纯慢病加重，而是循环、呼吸、肾脏和药物管理同时失衡的急性状态。主体能否恢复有效时间，取决于稳定、去充血、监测、出院交接和再入院预防。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖心脏泵功能维持供氧、行动和器官灌注
  -> 急性失代偿会把慢性心衰推入呼吸衰竭、肾损伤和住院循环
  -> 恢复依赖识别、稳定、监测、出院计划和长期随访
  -> 因此急性心衰失代偿是心血管持续性的急性执行域
```

## 关注对象

- Acute decompensated heart failure、pulmonary edema、congestion、hypoperfusion、renal interaction、hospitalization、readmission、transition of care、cardiac rehab / self-management support。
- 与 `cardiovascular-resilience/` 的边界：该域关注心血管长期风险；本域关注失代偿急性窗口和出院后恢复。
- 与 `mechanical-ventilation-respiratory-failure-continuity/` 的关系：严重肺水肿可进入呼吸支持，但本域关注心衰失代偿链条。

## Human Infra 模型链路

```text
急性心衰失代偿系统 T
  -> 改变容量负荷、去充血、灌注、肾心交互、出院交接变量 X
  -> 改变呼吸状态、肾功能、住院负担、再入院和运动能力 S
  -> 改变急性死亡、再住院、长期虚弱和有效时间损失 λ(t)
  -> 影响主体行动能力、恢复能力和未来选择权
```

## 非目标

- 不提供利尿剂、血压、氧疗、液体、饮食、设备、急诊分诊、住院或个体治疗建议。
- 不生成心衰临床路径、药物调整、再入院预测、出院计划或个案监测工具。
- 不收集个案体重、血压、氧饱和度、化验、影像、药物、设备或住院资料。

## Source Signals

- 2022 AHA/ACC/HFSA heart failure guideline materials: https://professional.heart.org/
- NHLBI heart failure public materials: https://www.nhlbi.nih.gov/health/heart-failure
- CDC heart failure public health materials: https://www.cdc.gov/heart-disease/about/heart-failure.html

## 下一步

- 建立 Acute HF Decompensation Card：congestion, perfusion, renal interaction, respiratory support, discharge handoff, readmission。
- 与 `cardiovascular-resilience/`、`mechanical-ventilation-respiratory-failure-continuity/` 和 `acute-kidney-injury-renal-replacement-continuity/` 建立接口。
