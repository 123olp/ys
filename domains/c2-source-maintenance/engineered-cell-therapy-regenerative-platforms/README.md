# Engineered Cell Therapy Regenerative Platforms

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/engineered-cell-therapy-regenerative-platforms` |
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

`engineered-cell-therapy-regenerative-platforms/` 研究 CAR-T、TCR-T、TIL、干细胞衍生细胞、免疫细胞工程和再生性细胞平台如何改变疾病控制、组织修复和主体持续性。

> 核心问题：细胞可以成为药物、传感器和修复单元。但工程细胞进入人体后，安全性、持久性、扩增、归巢、免疫反应和可关闭性决定它是基础设施还是新风险。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要更强的癌症控制、免疫修复、组织再生和功能恢复能力
  -> 工程细胞可能作为活体药物改变系统状态
  -> 细胞扩增失控、细胞因子风暴、脱靶、持久性不足和制造失败会限制收益
  -> 因此工程细胞疗法是医学增强和再生平台研究域
```

## 关注对象

- CAR-T、TCR-T、TIL、NK 细胞、巨噬细胞、iPSC 衍生细胞、干细胞衍生组织细胞和可编程细胞平台。
- 适应证、制造、质量、安全开关、持久性、复发、免疫毒性、肿瘤风险和长期随访。
- 与 `cancer-control/` 的边界：癌症域关注肿瘤控制全链条；本域关注工程细胞平台。
- 与 `regenerative-medicine/` 的边界：再生医学域关注组织修复整体；本域关注细胞作为工程平台。

## Human Infra 模型链路

```text
工程细胞疗法 T
  -> 改变免疫识别、细胞杀伤、组织修复和再生能力 X
  -> 改变癌症、免疫、退行性疾病或组织损伤状态 S
  -> 改变复发、失能、死亡和恢复风险 λ(t)
  -> 影响健康寿命、有效时间和主体持续性
```

## 非目标

- 不提供细胞制备、扩增、载体、靶点、给药、预处理、临床治疗或副作用处理建议。
- 不把某一批准适应证外推为通用抗衰、再生或增强路线。
- 不提供商业疗法选择、医院选择、入组建议或个体医疗建议。
- 不保存制造协议、质量放行流程或可操作实验细节。

## Source Signals

- FDA Cellular & Gene Therapy Products: https://www.fda.gov/vaccines-blood-biologics/cellular-gene-therapy-products
- NCI CAR T-cell therapy overview: https://www.cancer.gov/about-cancer/treatment/research/car-t-cells
- FDA CAR T-cell therapy safety communication: https://www.fda.gov/vaccines-blood-biologics/safety-availability-biologics/fda-requires-boxed-warning-secondary-t-cell-malignancies-following-treatment-bcma-directed-or-cd19-directed
- ISSCR Guidelines for Stem Cell Research and Clinical Translation: https://www.isscr.org/guidelines
- NIH Regenerative Medicine Program archive: https://commonfund.nih.gov/stemcells

## 下一步

1. 建立平台分类表：细胞来源、工程方式、适应证、持久性、安全开关、毒性和证据层级。
2. 与 `cancer-control/`、`immune-maintenance/`、`regenerative-medicine/`、`clinical-trials-regulatory-science-translation/` 建立接口。
3. 为工程细胞疗法补 Claim-Evidence Matrix。
