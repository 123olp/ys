# Multiomics Personal Baseline Systems Biology

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/multiomics-personal-baseline-systems-biology` |
| 分级 | `C3` - 可能性生成引擎层 |
| 控制轴 | 主体能力生成 |
| 分级理由 | 关键词显示该域主要增强认知、学习、工具、AI、技能或沟通能力。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何放大主体生成新路径的能力，例如认知、学习、注意力、记忆、AI、工具和反馈复利？

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

- 界定被放大的通用能力资源：智力、注意力、记忆、学习、判断、执行、反馈或工具使用。
- 说明任务链路：能力变化如何改变问题求解、行动质量、创造密度或学习轮次。
- 识别复利结构：能力增强、工具采用、协作网络、经验积累和自我升级如何互相强化。
- 记录依赖条件：AI、数据、界面、训练、外部工具、社会支持或反馈系统。
- 列出误用、过载、依赖、幻觉、注意力破坏、人格边界和安全风险。

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

`multiomics-personal-baseline-systems-biology/` 研究基因组、转录组、表观组、蛋白组、代谢组、微生物组、临床数据和连续感知如何构成主体状态的系统生物学底图。

> 核心问题：单一指标不足以描述一个长期运行的主体。Human Infra 需要的是跨层状态图：哪些变量在变、为什么变、如何相互作用、能否被干预。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体状态由多层生物系统共同决定
  -> 单一检测无法覆盖基因、表达、蛋白、代谢、免疫、微生物和行为状态
  -> 多组学和个人基线可提供动态状态估计
  -> 数据质量、解释性、隐私和可迁移性失败会制造错误模型
  -> 因此多组学个人基线是生命路径建模的数据底座
```

## 关注对象

- Genomics、epigenomics、transcriptomics、proteomics、metabolomics、microbiomics、single-cell、spatial omics 和 clinical phenotyping。
- 个人基线、纵向变化、跨组学整合、系统生物学网络、因果假设和风险预测。
- 数据批次效应、样本偏差、缺失数据、算法解释、隐私、代表性和临床可用性。
- 与 `health-data-privacy-governance/` 的边界：隐私治理域关注权利和数据治理；本域关注生物状态建模。
- 与 `biological-age-clocks-biomarker-validation/` 的边界：年龄钟域关注衰老指标；本域关注全局系统状态。

## Human Infra 模型链路

```text
多组学观测 O
  -> 描述主体多层状态 X
  -> 改善疾病风险、恢复能力、干预反应和个体差异估计 S
  -> 改变风险函数 λ(t) 和行动策略 A_t
  -> 影响健康寿命、有效时间和未来选择权
```

## 非目标

- 不提供个体基因组解释、疾病诊断、治疗建议、检测购买或保险/就业决策建议。
- 不把相关网络、聚类、风险分数或 AI 解释写成确定因果。
- 不把多组学数据收集本身写成健康收益；必须说明反馈和行动路径。
- 不保存个人敏感数据、原始基因组数据或可识别健康数据。

## Source Signals

- NIH Human BioMolecular Atlas Program: https://commonfund.nih.gov/hubmap
- NIH Bridge2AI: https://commonfund.nih.gov/bridge2ai
- GTEx Portal: https://gtexportal.org/
- All of Us Research Program: https://allofus.nih.gov/
- Human Cell Atlas: https://www.humancellatlas.org/

## 下一步

1. 建立多组学变量契约：数据层、样本来源、时间尺度、可解释性、隐私等级和证据用途。
2. 与 `biological-age-clocks-biomarker-validation/`、`measurement-feedback/`、`health-data-privacy-governance/` 建立接口。
3. 将代表性多组学平台资料转成 Source Cards。
