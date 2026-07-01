# Xenotransplantation Bioengineered Organ Replacement

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/xenotransplantation-bioengineered-organ-replacement` |
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


`xenotransplantation-bioengineered-organ-replacement/` 研究异种移植、基因编辑动物器官、工程化器官、器官保存灌注和替代性器官供给如何影响器官衰竭、等待名单和主体持续性。

> 核心问题：主体持续性会被关键器官失败直接截断。器官替换路线的价值在于增加可用器官和修复窗口，但其风险包括免疫排斥、感染、动物源风险、伦理和长期功能不确定性。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要心、肾、肝、肺、胰等关键器官长期维持功能
  -> 器官衰竭会直接压缩生命、有效时间和未来选择权
  -> 异种移植、工程器官和灌注保存可能扩大器官供给与修复窗口
  -> 免疫、感染、伦理、质量和长期功能失败会限制可用性
  -> 因此器官替换平台是关键器官持续性的研究域
```

## 关注对象

- 基因编辑猪器官、异种移植、去细胞支架、组织工程器官、3D 生物打印、器官灌注保存和器官评估。
- 免疫排斥、感染和人畜共患风险、动物源材料、伦理、器官质量、长期功能、可及性和公平分配。
- 与 `blood-organ-tissue-biovigilance-transplantation/` 的边界：生物警戒域关注现有血液/器官/组织安全；本域关注下一代器官供给和替换技术。
- 与 `regenerative-medicine/` 的边界：再生医学域关注修复总路线；本域关注完整器官替换和供给平台。

## Human Infra 模型链路

```text
器官替换平台 T
  -> 改变器官供给、器官质量、免疫匹配、保存时间和移植可及性 X
  -> 改变器官衰竭、等待名单和恢复状态 S
  -> 改变死亡风险、失能风险、感染风险和长期并发症 λ(t)
  -> 影响健康寿命、有效时间和主体持续性
```

## 非目标

- 不提供移植选择、器官等待、医疗决策、免疫抑制、手术、动物处理或实验操作建议。
- 不把个案移植新闻、短期存活或早期试验写成技术成熟。
- 不提供动物源材料获取、设施操作、病原检测、器官保存或监管规避信息。
- 不把器官替换写成永生保证；它只是关键器官失败的一类候选路径。

## Source Signals

- FDA Xenotransplantation: https://www.fda.gov/vaccines-blood-biologics/xenotransplantation
- FDA Source Animal, Product, Preclinical, and Clinical Issues Concerning the Use of Xenotransplantation Products: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/source-animal-product-preclinical-and-clinical-issues-concerning-use-xenotransplantation-products
- HRSA Organ Donation and Transplantation: https://www.organdonor.gov/
- OPTN data: https://optn.transplant.hrsa.gov/data/
- NIH organ transplantation research: https://www.niaid.nih.gov/research/transplantation

## 下一步

1. 建立器官替换变量表：器官类型、来源、免疫风险、感染风险、保存时间、长期功能和伦理边界。
2. 与 `blood-organ-tissue-biovigilance-transplantation/`、`immune-maintenance/`、`regenerative-medicine/` 和 `clinical-trials-regulatory-science-translation/` 建立接口。
3. 将代表性异种移植和工程器官资料转为 Source Cards。
