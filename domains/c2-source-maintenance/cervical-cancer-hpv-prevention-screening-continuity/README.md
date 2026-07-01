# Cervical Cancer HPV Prevention Screening Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/cervical-cancer-hpv-prevention-screening-continuity` |
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

`cervical-cancer-hpv-prevention-screening-continuity/` 研究宫颈癌 HPV 预防、疫苗接种、筛查、异常结果追踪、阴道镜入口、治疗负担、生殖/性健康和公平可及如何影响主体持续性。

> 核心问题：宫颈癌是可预防性很强的癌种；主体持续性损失常来自 HPV 预防失败、筛查断线、异常结果失访、污名和生殖健康服务不可及。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖可预防癌种被疫苗、筛查和异常闭环提前控制
  -> HPV 预防和宫颈筛查改变癌前病变、癌症阶段、治疗强度和死亡风险
  -> 隐私、污名、性/生殖健康服务和公平可及决定系统是否真正可用
  -> 因此宫颈癌是癌症连续性中的感染预防与筛查闭环域
```

## 关注对象

- Cervical cancer, HPV vaccination, screening, abnormal result follow-up, colposcopy access, reproductive health, sexual health stigma, equity。
- 与 `sexual-health-sti-prevention-continuity/` 的边界：该域关注 STI 预防和性健康；本域关注 HPV 到宫颈癌的预防、筛查和异常闭环。
- 与 `reproductive-fertility-continuity/` 和 `healthcare-access-continuity/` 的关系：宫颈癌连续性强依赖性/生殖健康服务可及。

## Human Infra 模型链路

```text
宫颈癌 HPV 预防筛查系统 T
  -> 改变 HPV 预防、疫苗可及、筛查覆盖、异常追踪、阴道镜入口和隐私保护变量 X
  -> 改变癌前病变控制、癌症阶段、治疗负担、污名压力和生殖健康状态 S
  -> 改变死亡、治疗后功能损失、心理负担和有效时间损失 λ(t)
  -> 影响主体健康寿命、身体自主、关系安全和未来选择权
```

## 非目标

- 不提供 HPV/宫颈筛查结果解释、疫苗个体建议、筛查年龄/频率、阴道镜判断、病理判读、治疗方案、用药、手术或个体建议。
- 不生成个人宫颈癌筛查推荐器、HPV 结果解释器、疫苗排序、异常结果处理建议或商业检测推广。
- 不收集个案 HPV、宫颈细胞学、阴道镜、病理、性史、生殖史或治疗资料。

## Source Signals

- NCI cervical cancer: https://www.cancer.gov/types/cervical
- NCI cervical cancer screening: https://www.cancer.gov/types/cervical/screening
- CDC HPV and cancer: https://www.cdc.gov/hpv/

## 下一步

- 建立 Cervical Cancer Continuity Card：HPV prevention, vaccination access, screening, abnormal follow-up, colposcopy, stigma, reproductive health。
- 与 `sexual-health-sti-prevention-continuity/`、`reproductive-fertility-continuity/` 和 `cancer-survivorship-late-effects-continuity/` 建立接口。
