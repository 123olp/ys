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
