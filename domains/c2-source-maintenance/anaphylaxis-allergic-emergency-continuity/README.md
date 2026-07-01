# Anaphylaxis Allergic Emergency Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/anaphylaxis-allergic-emergency-continuity` |
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

`anaphylaxis-allergic-emergency-continuity/` 研究过敏性休克、严重过敏、触发物识别、肾上腺素自动注射器可及、急救接入、学校/工作/公共场所计划和复发预防如何影响主体持续性。

> 核心问题：过敏性休克会在分钟级内同时影响气道、循环和意识。它不是普通过敏，而是触发物、识别、可及药物、场所准备和后续评估共同决定的急性主体中断风险。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖气道和循环不被免疫反应突然关闭
  -> 过敏性休克可在短时间内造成窒息、休克和死亡
  -> 结果取决于触发物管理、识别、应急药物可及、场所计划和急救转接
  -> 因此过敏急症是免疫-气道-循环交界的急性失效域
```

## 关注对象

- Anaphylaxis recognition systems, allergen exposure context, epinephrine auto-injector access, school/workplace plans, EMS handoff, biphasic risk, follow-up allergy care。
- 与 `immune-maintenance/` 的边界：该域关注免疫系统长期维护；本域关注严重过敏急性窗口。
- 与 `medical-id-allergy-critical-alert-continuity/` 的关系：关键过敏身份信息可影响本域的识别和转接。

## Human Infra 模型链路

```text
过敏急症准备系统 T
  -> 改变触发物暴露、识别延迟、药物可及、场所计划和急救转接变量 X
  -> 改变气道、循环、意识、急诊观察和复发风险状态 S
  -> 改变窒息、休克、死亡和长期活动受限风险 λ(t)
  -> 影响主体存活、活动边界和未来选择权
```

## 非目标

- 不提供过敏诊断、肾上腺素使用、剂量、急救步骤、食物/药物挑战、脱敏、学校计划或个案医疗建议。
- 不生成 anaphylaxis action plan、过敏风险评分、暴露规避、处方或现场处理工具。
- 不收集个案过敏史、药物、食物、学校/工作地点、急救事件或医疗资料。

## Source Signals

- World Allergy Organization anaphylaxis guidance: https://www.worldallergy.org/
- NIAID food allergy guideline materials: https://www.niaid.nih.gov/
- AAAAI anaphylaxis practice parameter materials: https://www.aaaai.org/

## 下一步

- 建立 Anaphylaxis Continuity Card：trigger, recognition, epinephrine access, place plan, EMS transfer, follow-up。
- 与 `immune-maintenance/`、`medical-id-allergy-critical-alert-continuity/` 和 `school-health-services-chronic-condition-continuity/` 建立接口。
