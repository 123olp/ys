# Polycystic Ovary Syndrome Metabolic Reproductive Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/polycystic-ovary-syndrome-metabolic-reproductive-continuity` |
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

`polycystic-ovary-syndrome-metabolic-reproductive-continuity/` 研究 PCOS 作为内分泌、代谢、生殖、皮肤表现、心理负担和长期心血管/糖尿病风险交叉域，如何影响主体持续性、有效时间和未来选择权。

> 核心问题：PCOS 不是单一“月经问题”或“生育问题”，而是会通过代谢风险、排卵不规律、症状污名、体重压力、胰岛素抵抗和长期风险管理改变主体行动质量的系统性状态。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要稳定代谢、可预测身体信号、生殖自主和长期风险可见性
  -> PCOS 会把内分泌节律、代谢状态、生育窗口、皮肤/毛发症状和心理负担连接起来
  -> 若症状被污名化或延迟识别，主体会损失有效时间、身体自主、未来生育选择和长期风险控制窗口
  -> 因此 PCOS 是内分泌-代谢-生殖连续性的关键研究域
```

## 关注对象

- PCOS/多囊卵巢综合征、排卵不规律、高雄激素表现、胰岛素抵抗、代谢综合征、2 型糖尿病风险、心血管风险、皮肤/毛发表现、心理负担和生殖选择权。
- 与 `endocrine-hormonal-regulation/` 的边界：上位域关注激素调节总机制；本域关注 PCOS 这一多系统状态如何进入主体持续性模型。
- 与 `menstrual-health-cycle-literacy-continuity/` 的边界：月经域关注周期素养、用品和参与；本域关注 PCOS 的内分泌、代谢和生殖风险链。
- 与 `reproductive-fertility-continuity/` 的关系：PCOS 是影响未来生育选择权的一类机制，但不能被简化为不孕标签。

## Human Infra 模型链路

```text
PCOS 识别与管理基础设施 T
  -> 改变内分泌节律、排卵模式、代谢风险、症状污名、心理负担和生殖规划变量 X
  -> 改变主体身体自主、有效时间、长期风险可见性、生育选择权和医疗导航状态 S
  -> 改变糖尿病、心血管风险、诊断延迟、心理负担、未来选择受限和资源消耗 lambda(t)
  -> 影响主体健康寿命、行动质量、关系路径和未来选择权
```

## 非目标

- 不提供 PCOS 诊断、化验解释、超声判断、激素治疗、避孕药、促排、减重、饮食、补剂、运动、皮肤/脱发处理或生育治疗建议。
- 不把体重、月经、痤疮、多毛、胰岛素或生育力写成个体判断。
- 不收集个人月经、性健康、妊娠、体重、影像、化验、精神健康或身份敏感资料。

## Source Signals

- MedlinePlus polycystic ovary syndrome: https://medlineplus.gov/polycysticovarysyndrome.html
- NICHD PCOS: https://www.nichd.nih.gov/health/topics/pcos
- CDC diabetes and PCOS context: https://www.cdc.gov/diabetes/risk-factors/pcos-polycystic-ovary-syndrome.html

## 下一步

- 建立 PCOS Continuity Card：cycle pattern, androgen symptoms, metabolic risk, fertility planning, stigma, mental health, evidence boundary。
- 与 `endocrine-hormonal-regulation/`、`nutrition-metabolic-health/`、`reproductive-fertility-continuity/` 和 `mental-health-affective-stability/` 建立接口。
