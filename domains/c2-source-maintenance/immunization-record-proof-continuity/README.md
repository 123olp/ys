# Immunization Record Proof Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/immunization-record-proof-continuity` |
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

Immunization Record Proof Continuity 研究疫苗接种记录、免疫登记系统、学校/工作/旅行证明、补种历史和跨州/跨机构记录可得性如何影响主体进入教育、医疗、工作、旅行和公共卫生系统。

> 核心问题：疫苗接种本身是医学事件，免疫记录则是制度通行能力；记录缺失会让已有保护无法转化为服务、入学、就业和旅行连续性。

## 研究对象

- Immunization record、IIS、疫苗卡、学校/雇主/旅行证明、补种记录和免疫豁免资料。
- 跨州、跨国、儿童转学、成人补种、灾害丢失和纸质/数字凭证迁移。
- 记录错误、重复、缺失、隐私、伪造、防欺诈和数据共享边界。

## 先验链路

```text
免疫保护需要接种事件和可验证记录共同存在
  -> 学校、工作、旅行、医疗和公共卫生系统会依赖免疫记录作出准入或风险判断
  -> 记录丢失、错误或不可携带会迫使主体重复接种、延迟入学就业或失去服务资格
  -> 可访问、可纠错、可验证的免疫记录降低重复、排除和公共卫生风险
  -> 因而免疫记录证明是身体保护转化为制度行动能力的接口
```

## 关键变量

- 记录完整性、来源、接种日期、疫苗类型、批号口径、IIS 覆盖和跨机构交换。
- 证明场景、隐私权限、纠错流程、数字凭证、纸质备份和反伪造机制。
- 儿童、老人、移民、灾害流离失所、无保险和跨境旅行场景。

## 证据入口

- CDC vaccination record and immunization information system materials.
- State immunization registry materials.
- WHO International Certificate of Vaccination materials.
- School and workplace public health requirement materials.

## 非目标

- 本域不建议是否接种、何时接种、补种、豁免、旅行疫苗或处理不良反应。
- 不代写疫苗证明、豁免、学校/雇主/旅行材料或记录更正请求。
- 不收集疫苗卡、IIS 记录、健康资料、身份文件、学校、雇主或旅行资料。

## 上下游

- 上游：`immunization-public-health-surveillance/`、`health-data-privacy-governance/`、`verifiable-credential-wallet-interoperability/`。
- 下游：`school-enrollment-attendance-continuity/`、`employment-algorithmic-hiring-screening-continuity/`、`passport-travel-document-mobility-continuity/`。
