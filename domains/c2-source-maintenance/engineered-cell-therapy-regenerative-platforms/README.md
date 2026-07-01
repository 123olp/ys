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
