# Mechanical Ventilation Respiratory Failure Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/mechanical-ventilation-respiratory-failure-continuity` |
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

`mechanical-ventilation-respiratory-failure-continuity/` 研究急性呼吸衰竭、氧合/通气失败、机械通气、撤机、呼吸治疗和长期呼吸功能恢复如何影响主体持续性。

> 核心问题：呼吸失败会在短时间内切断氧供。机械通气是把不可逆缺氧变成可支持、可恢复窗口的核心生命支持技术之一。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体持续性依赖氧合、通气和酸碱平衡
  -> 肺炎、ARDS、创伤、神经肌肉失败或麻醉可导致急性呼吸衰竭
  -> 机械通气可暂时代替呼吸功能，但也带来肺损伤、感染、谵妄和撤机风险
  -> 因此机械通气是呼吸失败进入生命支持模型的核心域
```

## 关注对象

- Acute respiratory failure、ARDS、oxygenation、ventilation、noninvasive/invasive ventilation、ventilator-associated harm、weaning、respiratory therapy、long-term recovery。
- 与 `respiratory-oxygenation/` 的边界：呼吸氧合域关注基础生理；本域关注急性失败和设备支持。
- 与 `home-oxygen-respiratory-equipment-supply-continuity/` 的关系：后者关注居家设备供应；本域关注急性和 ICU 生命支持。

## Human Infra 模型链路

```text
机械通气与呼吸衰竭支持 T
  -> 改变氧合、通气、设备可用、撤机、感染和肺保护变量 X
  -> 改变缺氧、二氧化碳潴留、ICU 病程和肺功能恢复状态 S
  -> 改变急性死亡、脑缺氧、呼吸机相关损伤和长期功能下降风险 λ(t)
  -> 影响主体存在、认知连续性和恢复能力
```

## 非目标

- 不提供氧疗、呼吸机参数、撤机、气道管理、ARDS 治疗、呼吸训练或个体医疗建议。
- 不生成设备设置、医院流程、居家呼吸设备操作、急救指导或替代呼吸治疗师的内容。
- 不收集呼吸机参数、血气、影像、SpO2、病历、设备日志或家庭医疗资料。

## Source Signals

- ATS/ESICM/SCCM Mechanical Ventilation Guideline: https://www.thoracic.org/statements/resources/cc/mechanical-ventilation-ards.pdf
- NIH Respiratory Failure: https://www.nhlbi.nih.gov/health/respiratory-failure
- CDC Ventilator-associated Event: https://www.cdc.gov/nhsn/psc/vae/index.html

## 下一步

- 建立 Respiratory Support Card：failure type, oxygenation, ventilation, device support, complications, weaning, recovery。
- 与 `respiratory-oxygenation/`、`intensive-care-organ-support-delirium-continuity/` 和 `home-oxygen-respiratory-equipment-supply-continuity/` 建立接口。
