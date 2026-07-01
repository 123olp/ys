# Acute Coronary Syndrome Reperfusion Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/acute-coronary-syndrome-reperfusion-continuity` |
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

`acute-coronary-syndrome-reperfusion-continuity/` 研究急性冠脉综合征、胸痛识别、心电图/肌钙蛋白路径、再灌注窗口、导管室/转运能力和心肌损伤后恢复如何影响主体持续性。

> 核心问题：急性冠脉综合征把冠状动脉供血失败转化为分钟到小时级心肌损失。有效永生需要把“可再灌注窗口”建模为避免骤停、心衰和长期失能的关键条件。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖持续心肌供血维持循环和行动能力
  -> 冠脉急性闭塞会快速改变死亡、心衰和有效时间风险
  -> 结果取决于识别、转运、诊断、再灌注和康复链条
  -> 因此急性冠脉综合征是心血管连续性的时间关键失效域
```

## 关注对象

- Chest pain systems、ECG delay、troponin pathways、STEMI/NSTEMI routing、PCI access、time-to-reperfusion、cardiac rehabilitation、secondary prevention handoff。
- 与 `cardiovascular-resilience/` 的边界：该域关注长期心血管韧性；本域关注急性冠脉事件的再灌注窗口和急性后续恢复。
- 与 `cardiac-arrest-cpr-defibrillation-continuity/` 的关系：ACS 是骤停上游原因之一，但本域关注骤停前的可逆窗口。

## Human Infra 模型链路

```text
ACS 再灌注系统 T
  -> 改变识别延迟、诊断延迟、转运、再灌注和康复变量 X
  -> 改变心肌坏死范围、循环稳定性、心衰风险和功能恢复状态 S
  -> 改变急性死亡、再住院、心衰和长期有效时间损失 λ(t)
  -> 影响主体存活、行动能力和未来选择权
```

## 非目标

- 不提供胸痛判断、是否呼叫急救、心电图/肌钙蛋白解读、药物、介入、溶栓、医院选择或个体治疗建议。
- 不生成 STEMI/NSTEMI 临床路径、分诊工具、转运建议、再灌注决策或康复处方。
- 不收集个案症状、心电图、检验值、用药、病历、位置或急救资料。

## Source Signals

- AHA / ACC acute coronary syndrome guideline materials: https://www.heart.org/
- Professional Heart Daily guideline materials: https://professional.heart.org/
- NCBI / NHLBI heart attack public materials: https://www.nhlbi.nih.gov/health/heart-attack

## 下一步

- 建立 ACS Reperfusion Card：symptom-to-contact, ECG, troponin, transfer, PCI/reperfusion, post-event recovery。
- 与 `cardiovascular-resilience/`、`cardiac-arrest-cpr-defibrillation-continuity/` 和 `intensive-care-organ-support-delirium-continuity/` 建立接口。
