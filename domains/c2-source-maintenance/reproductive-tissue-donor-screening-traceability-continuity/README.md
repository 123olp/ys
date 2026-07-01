# Reproductive Tissue Donor Screening Traceability Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/reproductive-tissue-donor-screening-traceability-continuity` |
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


生殖组织供体筛查、检测、标签和可追溯连续性，关注 sperm、oocyte、embryo donation、HCT/P donor eligibility、communicable disease screening/testing、directed donor、anonymous/nonidentified donor、标签警示和记录保存如何影响安全、身份与未来权利。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 生殖技术把身体材料、亲缘关系、感染风险、身份信息和未来子代权利连接起来
  -> 供体筛查、检测、标签和记录决定材料能否被安全、可解释、可追溯地使用
  -> 如果追溯链断裂，主体和后代会面对感染、身份、法律、心理和医学信息风险
  -> 因此生殖组织供体可追溯性是 ART 安全与主体连续性的治理接口
```

## 关注对象

- FDA HCT/P、donor eligibility、donor screening/testing、reproductive cells and tissue、directed reproductive donor 和 donor summary records。
- sperm/oocyte/embryo donor evaluation、遗传/感染/心理筛查边界、标签、记录、样本身份和后代可识别性。
- 与 `fertility-preservation-gamete-embryo-cryostorage-continuity/` 的边界：冷冻域关注长期保存；本域关注供体资格、检测、标签和可追溯。

## Human Infra 模型链路

```text
供体筛查与追溯 T
  -> 改变感染风险识别、遗传资料、身份记录、标签警示、样本链和后代信息变量 X
  -> 改变主体使用生殖材料、信任诊所、管理亲缘/医学信息和保护后代权益状态 S
  -> 改变传播风险、样本错配、身份冲突、资料不可得和法律伦理争议风险 lambda(t)
  -> 影响生殖技术安全性、关系连续性和未来选择权的可治理性
```

## 非目标

- 不提供供体选择、筛查结果解释、遗传风险解释、感染风险判断、捐精捐卵、胚胎捐赠、法律或亲子关系建议。
- 不处理可执行实验室、采样、储存、运输或匿名识别操作。
- 不鼓励规避 FDA、CDC、ASRM、诊所、法律或伦理审查要求。

## Source Signals

- FDA What You Should Know - Reproductive Tissue Donation: https://www.fda.gov/vaccines-blood-biologics/safety-availability-biologics/what-you-should-know-reproductive-tissue-donation
- FDA Recommendations for Determining Eligibility of Donors of HCT/Ps: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/recommendations-determining-eligibility-donors-human-cells-tissues-and-cellular-and-tissue-based
- FDA Testing Donors of HCT/P Specific Requirements: https://www.fda.gov/vaccines-blood-biologics/safety-availability-biologics/testing-donors-human-cells-tissues-and-cellular-and-tissue-based-products-hctp-specific-requirements
- ASRM Gamete and embryo donation guidance: https://www.asrm.org/practice-guidance/practice-committee-documents/guidance-regarding-gamete-and-embryo-donation/

## 下一步

1. 建立 reproductive donor traceability card：donor type、eligibility、testing、labeling、records、identity boundary 和 offspring information rights。
2. 与 `third-party-reproduction-surrogacy-donor-legal-ethics-continuity/`、`health-data-privacy-governance/` 和 `biobanking-biospecimen-chain-of-custody/` 建立接口。
