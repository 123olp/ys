# Ferroptosis Lipid Peroxidation Membrane Resilience Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/ferroptosis-lipid-peroxidation-membrane-resilience-continuity` |
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

Ferroptosis Lipid Peroxidation Membrane Resilience Continuity 负责整理铁死亡、脂质过氧化、膜脂稳态、铁代谢、抗氧化防御和细胞膜损伤扩增机制。

核心问题：

> 细胞持续性不只取决于 DNA 和蛋白，还取决于膜系统是否能抵抗脂质过氧化失控；铁死亡把代谢、铁、氧化压力和细胞死亡连接成高后果风险通道。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 细胞需要维持膜脂组成、铁代谢和氧化还原平衡
  -> 脂质过氧化会破坏膜结构并触发 ferroptosis 等细胞死亡路径
  -> 铁死亡可能参与神经退行、缺血再灌注、癌症治疗、炎症和器官损伤
  -> 若膜脂损伤不可控，组织功能和恢复窗口会被快速压缩
  -> 因此脂质过氧化与铁死亡是细胞死亡风险函数的重要下层机制
```

## 关注对象

- ferroptosis、lipid peroxidation、iron metabolism、GPX4、glutathione、PUFA membrane composition、oxidative stress。
- 与 `mitochondrial-bioenergetics/` 的关系：线粒体域关注能量和细胞器功能，本域关注膜脂氧化和铁依赖细胞死亡。
- 与 `cancer-control/` 的关系：铁死亡可作为癌症研究靶点资料，但本域不提供治疗方案。

## Human Infra 模型链路

```text
铁死亡 / 脂质过氧化观测 T
  -> 改变膜脂氧化、铁稳态、GPX4/谷胱甘肽防御和细胞死亡倾向 X
  -> 改变细胞膜韧性和应激恢复状态 S
  -> 改变神经退行、缺血损伤、炎症、癌症治疗反应和器官功能风险
  -> 改变恢复能力、健康寿命和未来选择权
```

## 非目标

- 不提供铁剂、抗氧化剂、饮食、补剂、药物、癌症治疗、神经保护、检测解释或临床建议。
- 不把 ferroptosis 标志物、铁指标或脂质过氧化指标写成个体健康结论。
- 不提供细胞死亡诱导、药筛、动物实验、癌症治疗或人体干预协议。

## Source Signals

- Hallmarks of Aging: https://pubmed.ncbi.nlm.nih.gov/36599349/
- Ferroptosis turns 10: https://pmc.ncbi.nlm.nih.gov/articles/PMC9273022/
- Ferroptosis and lipid peroxidation aging literature: https://pubmed.ncbi.nlm.nih.gov/?term=ferroptosis+lipid+peroxidation+aging+review
