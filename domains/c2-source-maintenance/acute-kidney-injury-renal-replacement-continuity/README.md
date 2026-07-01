# Acute Kidney Injury Renal Replacement Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/acute-kidney-injury-renal-replacement-continuity` |
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

`acute-kidney-injury-renal-replacement-continuity/` 研究急性肾损伤、体液/电解质/酸碱失衡、透析/肾脏替代治疗、ICU 肾支持和长期肾功能恢复如何影响主体持续性。

> 核心问题：肾功能失败会让毒素、容量、电解质和酸碱平衡失控。肾脏替代治疗是把内环境崩溃转化为可支持窗口的基础技术。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要清除代谢废物并维持体液、电解质和酸碱稳态
  -> 急性肾损伤可在脓毒症、创伤、药物、手术或休克中迅速出现
  -> 肾脏替代治疗可争取恢复窗口，但受容量、血流动力学、感染和资源约束
  -> 因此 AKI 与肾脏替代治疗是内环境失败的急性支持域
```

## 关注对象

- AKI detection、KDIGO staging、fluid balance、electrolytes、acid-base、CRRT/intermittent dialysis、ICU renal support、kidney recovery、CKD transition。
- 与 `renal-hepatic-clearance/` 的边界：清除域关注长期器官功能；本域关注急性肾失败与设备支持。
- 与 `sepsis-shock-early-recognition-resuscitation-continuity/` 的关系：脓毒症和休克是 AKI 的重要上游。

## Human Infra 模型链路

```text
AKI 与肾脏替代支持 T
  -> 改变毒素、容量、电解质、酸碱、设备可用和肾恢复变量 X
  -> 改变内环境稳定、ICU 病程、长期肾功能和治疗负担状态 S
  -> 改变急性死亡、心律风险、脑功能损害、CKD 转化和再住院风险 λ(t)
  -> 影响主体恢复能力、治疗选择和有效时间
```

## 非目标

- 不提供透析适应证、参数、饮食、补液、用药、实验室解读、肾病治疗或个体医疗建议。
- 不生成 CRRT/透析设置、医院路径、设备操作、保险或转院建议。
- 不收集肌酐、电解质、尿量、透析记录、病历、设备日志或保险资料。

## Source Signals

- KDIGO Acute Kidney Injury: https://kdigo.org/guidelines/acute-kidney-injury/
- National Kidney Foundation AKI: https://www.kidney.org/kidney-topics/acute-kidney-injury-aki
- NIH Kidney Failure Treatment: https://www.niddk.nih.gov/health-information/kidney-disease/kidney-failure/choosing-treatment

## 下一步

- 建立 Renal Support Card：AKI signal, fluid/electrolyte risk, support modality, hemodynamic tolerance, recovery, CKD transition。
- 与 `renal-hepatic-clearance/`、`fluid-electrolyte-acid-base-homeostasis/` 和 `intensive-care-organ-support-delirium-continuity/` 建立接口。
