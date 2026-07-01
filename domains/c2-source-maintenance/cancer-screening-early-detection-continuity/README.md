# Cancer Screening Early Detection Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/cancer-screening-early-detection-continuity` |
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


`cancer-screening-early-detection-continuity/` 研究癌症筛查、早期发现、随访闭环、假阳性/假阴性、过度诊断、筛查可及和异常结果追踪如何影响主体持续性。

> 核心问题：癌症控制不只发生在治疗阶段；筛查和异常结果追踪决定肿瘤是否在可治疗阶段被发现，也决定人群是否承担过度诊断、焦虑和不公平可及的代价。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖恶性增殖风险被早期识别且不过度伤害
  -> 癌症筛查可改变诊断阶段、治疗负担、死亡风险和过度诊断风险
  -> 结果取决于对象选择、筛查质量、异常追踪、治疗入口和公平可及
  -> 因此癌症筛查与早期发现是癌症控制的前端证据执行域
```

## 关注对象

- Cancer screening programs, colorectal/breast/cervical/lung screening signals, abnormal result follow-up, overdiagnosis, false positive / false negative, equity, registry linkage。
- 与 `cancer-control/` 的边界：该域关注肿瘤发生、治疗、复发和死亡风险；本域关注筛查、早诊和异常结果闭环。
- 与 `clinical-laboratory-diagnostic-quality/` 和 `diagnostic-imaging-order-scheduling-report-continuity/` 的关系：筛查依赖检测和影像质量。

## Human Infra 模型链路

```text
癌症筛查早诊系统 T
  -> 改变筛查覆盖、质量、异常追踪、诊断阶段、过度诊断和公平变量 X
  -> 改变癌症分期、治疗负担、心理负担和长期功能状态 S
  -> 改变癌症死亡、失能、治疗毒性和有效时间损失 λ(t)
  -> 影响主体健康寿命、资源负担和未来选择权
```

## 非目标

- 不提供个人筛查年龄、频率、检查选择、影像/病理/实验室解读、肿瘤风险、治疗或个体医疗建议。
- 不生成个人癌症筛查推荐器、保险申诉、机构选择、检查排序或商业检测推广。
- 不收集个案筛查结果、家族史、遗传信息、影像、病理、症状或诊疗资料。

## Source Signals

- USPSTF recommendations: https://www.uspreventiveservicestaskforce.org/
- NCI cancer screening: https://www.cancer.gov/about-cancer/screening
- CDC cancer screening: https://www.cdc.gov/cancer/screening/

## 下一步

- 建立 Cancer Screening Card：eligibility boundary, modality, abnormal follow-up, overdiagnosis, false result, equity, registry。
- 与 `cancer-control/`、`clinical-laboratory-diagnostic-quality/` 和 `diagnostic-imaging-order-scheduling-report-continuity/` 建立接口。
