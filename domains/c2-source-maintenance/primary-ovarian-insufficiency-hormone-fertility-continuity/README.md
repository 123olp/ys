# Primary Ovarian Insufficiency Hormone Fertility Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/primary-ovarian-insufficiency-hormone-fertility-continuity` |
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

`primary-ovarian-insufficiency-hormone-fertility-continuity/` 研究原发性卵巢功能不全、卵巢激素不足、月经改变、生育窗口、骨骼心血管风险、心理社会负担和长期监测连续性如何影响主体持续性。

> 核心问题：POI 不是单纯“提前绝经”，而是会同时改变生育未来、激素环境、骨骼和心血管风险、身份体验、关系压力和长期医疗决策。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要在生殖年龄阶段保留激素稳定、骨骼保护、生育选择权和身份/关系连续性
  -> POI 会改变卵巢激素、月经、骨密度、心血管风险、生育窗口、情绪和关系变量
  -> 结果取决于识别、病因/遗传边界、生育保存或 ART 接口、长期激素/骨骼监测和心理支持
  -> 因此 POI 是性腺轴、生育未来和中长期健康风险的关键域
```

## 关注对象

- Primary ovarian insufficiency、premature ovarian failure historical term, irregular/absent periods context, estrogen deficiency context, fertility uncertainty, bone/cardiovascular risk, emotional burden, long-term monitoring。
- 与 `menstrual-health-cycle-literacy-continuity/` 的关系：周期改变可进入本域，但本域聚焦 POI 及其激素/生育/骨骼风险。
- 与 `assisted-reproductive-technology-ivf-cycle-continuity/` 和 `fertility-preservation-gamete-embryo-cryostorage-continuity/` 的关系：本域只整理接口，不提供生殖治疗建议。

## Human Infra 模型链路

```text
POI 识别与长期支持系统 T
  -> 改变卵巢激素、月经、生育窗口、骨密度、心血管风险、情绪和关系变量 X
  -> 改变未来生育选择权、身份体验、长期健康监测、工作生活参与和资源规划状态 S
  -> 改变骨折、心血管、心理负担、生育窗口损耗、治疗中断和有效时间损耗风险 λ(t)
  -> 影响主体身体自主、未来选择权和长期健康寿命
```

## 非目标

- 不提供个人诊断、FSH/AMH/雌激素/遗传结果判读、月经/妊娠判断、激素治疗、生育保存、IVF、供卵、避孕、骨密度治疗、补剂或个体医疗建议。
- 不生成检查排序、生育方案、激素方案、胚胎/供体选择、保险申诉、伴侣沟通、心理处置、工作/学校证明或法律材料。
- 不收集个案化验、遗传结果、月经记录、妊娠资料、生育计划、ART records、伴侣资料、处方、骨密度或保险资料。

## Source Signals

- MedlinePlus primary ovarian insufficiency: https://medlineplus.gov/primaryovarianinsufficiency.html
- NICHD primary ovarian insufficiency: https://www.nichd.nih.gov/health/topics/poi

## 下一步

- 建立 POI Continuity Card：hormone state, fertility uncertainty, bone/cardiovascular interface, psychosocial burden, ART/fertility-preservation boundary。
- 与 `menstrual-health-cycle-literacy-continuity/`、`reproductive-fertility-continuity/`、`fertility-preservation-gamete-embryo-cryostorage-continuity/` 和 `perimenopause-menopause-midlife-health-continuity/` 建立接口。
