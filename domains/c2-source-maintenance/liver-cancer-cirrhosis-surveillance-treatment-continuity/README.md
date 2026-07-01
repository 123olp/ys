# Liver Cancer Cirrhosis Surveillance Treatment Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/liver-cancer-cirrhosis-surveillance-treatment-continuity` |
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

`liver-cancer-cirrhosis-surveillance-treatment-continuity/` 研究肝癌、肝硬化监测、病毒性肝炎/MASLD 上游风险、超声/AFP 监测、治疗可及、肝功能储备和移植/支持照护入口如何影响主体持续性。

> 核心问题：肝癌连续性不只看肿瘤，也看肝硬化和肝功能储备；主体风险来自癌症进展、失代偿、感染/代谢上游和治疗窗口同时变化。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖肝脏解毒、代谢和合成能力长期维持
  -> 肝癌常与肝硬化、病毒性肝炎、MASLD/MASH 和失代偿风险交织
  -> 监测、治疗、肝功能储备、移植入口和上游风险治理决定主体是否保留生理冗余
  -> 因此肝癌是癌症连续性与肝脏基础设施交叉域
```

## 关注对象

- Liver cancer / hepatocellular carcinoma, cirrhosis surveillance, viral hepatitis, MASLD / MASH, ultrasound / AFP pathway, liver function reserve, treatment access, transplant / supportive continuity。
- 与 `chronic-viral-hepatitis-screening-liver-protection-continuity/` 和 `chronic-liver-disease-masld-mash-continuity/` 的关系：本域承接上游肝病风险进入肝癌监测和治疗窗口。
- 与 `renal-hepatic-clearance/` 的关系：肝功能储备是主体基础代谢设施的一部分。

## Human Infra 模型链路

```text
肝癌肝硬化监测系统 T
  -> 改变上游肝病控制、监测覆盖、异常追踪、治疗可及、肝功能储备和移植/支持入口变量 X
  -> 改变肿瘤阶段、肝失代偿、治疗耐受性、感染/出血风险和资源状态 S
  -> 改变死亡、急性失代偿、有效时间损失和照护资源消耗 λ(t)
  -> 影响主体健康寿命、生理冗余、行动能力和未来选择权
```

## 非目标

- 不提供超声/AFP 判读、监测频率、肝硬化分期、肝病治疗、抗病毒/代谢治疗、介入治疗、移植判断、用药或个体建议。
- 不生成个人肝癌风险计算器、影像/肿瘤标志物解释、治疗排序、移植资格判断或商业检测推广。
- 不收集个案肝病史、影像、AFP、病毒指标、肝功能、病理、饮酒史或治疗资料。

## Source Signals

- NCI liver cancer: https://www.cancer.gov/types/liver
- CDC liver cancer: https://www.cdc.gov/cancer/liver/
- CDC viral hepatitis: https://www.cdc.gov/hepatitis/

## 下一步

- 建立 Liver Cancer Continuity Card：cirrhosis surveillance, viral / metabolic upstream, abnormal follow-up, liver reserve, treatment access, transplant / supportive pathway。
- 与 `chronic-viral-hepatitis-screening-liver-protection-continuity/`、`chronic-liver-disease-masld-mash-continuity/` 和 `renal-hepatic-clearance/` 建立接口。
