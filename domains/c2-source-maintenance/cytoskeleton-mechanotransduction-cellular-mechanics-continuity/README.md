# Cytoskeleton Mechanotransduction Cellular Mechanics Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/cytoskeleton-mechanotransduction-cellular-mechanics-continuity` |
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

This domain studies how cytoskeletal architecture, mechanotransduction, force sensing, cell shape, and intracellular mechanics affect subject continuity.

> Core question: can cells continue to sense, bear, and translate mechanical forces into adaptive behavior without drifting into frailty, fibrosis, vascular failure, or impaired regeneration?

## 先验位置

有效永生要求身体不只是化学系统，也是机械系统。细胞骨架、黏附、核-细胞骨架耦合、力传导和机械感知决定细胞如何读取外部环境、维持形态、迁移、分裂、修复和响应组织刚度。机械信息失真会影响血管、骨、肌肉、纤维化、癌症和衰老。

## 关注对象

- Actin、microtubules、intermediate filaments、黏附和细胞形态。
- mechanotransduction、force sensing、shear stress、基质刚度和核-细胞骨架耦合。
- 机械衰老、组织刚度、纤维化、血管功能和再生环境。
- 力学信号如何连接 ECM、核结构、细胞命运和组织功能。

## Human Infra 模型链路

```text
细胞骨架和机械转导
-> 力感知、形态、迁移、核耦合和组织刚度响应
-> 血管、肌骨、纤维化、再生和癌症风险改变
-> 功能储备、行动能力和恢复能力改变
-> 主体持续性改变
```

## 非目标

- 不提供机械刺激、康复动作、训练处方、设备、物理治疗、检测解释或治疗建议。
- 不把 mechanotransduction 信号写成个体寿命预测或抗衰操作。
- 不提供细胞力学实验、基质工程、设备参数或人体试验建议。

## Source Signals

- PubMed: [The cellular mechanobiology of aging: from biology to mechanics](https://pubmed.ncbi.nlm.nih.gov/33231326/).
- PubMed: [Integrating molecular and cellular components of endothelial shear stress mechanotransduction](https://pubmed.ncbi.nlm.nih.gov/39178024/).
- PubMed: [Force-sensing protein expression in response to cardiovascular mechanotransduction](https://pubmed.ncbi.nlm.nih.gov/39481337/).
