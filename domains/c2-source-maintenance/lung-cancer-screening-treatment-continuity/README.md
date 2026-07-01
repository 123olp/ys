# Lung Cancer Screening Treatment Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/lung-cancer-screening-treatment-continuity` |
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


`lung-cancer-screening-treatment-continuity/` 研究肺癌低剂量 CT 筛查、烟草暴露、影像异常追踪、诊断延迟、治疗负担、呼吸功能和幸存者连续性如何影响主体持续性。

> 核心问题：肺癌死亡风险高，且筛查对象、烟草污名、影像假阳性、诊断容量、治疗副作用和呼吸功能下降共同决定主体能否保留行动能力。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖高死亡风险癌种被提前识别且治疗负担可控
  -> 肺癌筛查和异常影像追踪改变诊断阶段、治疗选择和死亡风险
  -> 呼吸功能、烟草风险、污名和照护入口决定主体行动能力是否被持续保护
  -> 因此肺癌是癌症连续性中的高死亡风险和呼吸功能交叉域
```

## 关注对象

- Lung cancer screening, low-dose CT, smoking exposure, abnormal imaging follow-up, diagnostic delay, treatment toxicity, breathlessness, functional capacity。
- 与 `tobacco-nicotine-cessation-continuity/` 的边界：该域关注烟草暴露控制；本域关注肺癌筛查、诊断、治疗和呼吸功能后果。
- 与 `respiratory-oxygenation/` 和 `diagnostic-imaging-order-scheduling-report-continuity/` 的关系：肺癌连续性依赖影像和呼吸储备。

## Human Infra 模型链路

```text
肺癌连续性系统 T
  -> 改变筛查资格、LDCT 可及、影像异常追踪、诊断延迟、治疗负担和呼吸功能变量 X
  -> 改变癌症阶段、治疗毒性、气促、活动能力、污名压力和照护状态 S
  -> 改变死亡、失能、呼吸功能损失和有效时间损失 λ(t)
  -> 影响主体健康寿命、行动半径、恢复能力和未来选择权
```

## 非目标

- 不提供影像判读、筛查资格判断、烟草戒断医疗方案、肺结节解释、分期、治疗、氧疗、手术、放化疗、免疫治疗或个体建议。
- 不生成个人肺癌筛查推荐器、结节风险评估、治疗排序、戒烟处方或商业检测推广。
- 不收集个案 CT、肺结节、病理、吸烟史、症状、氧疗或治疗资料。

## Source Signals

- NCI lung cancer: https://www.cancer.gov/types/lung
- NCI lung cancer screening: https://www.cancer.gov/types/lung/screening
- CDC lung cancer: https://www.cdc.gov/lung-cancer/

## 下一步

- 建立 Lung Cancer Continuity Card：LDCT boundary, tobacco exposure, abnormal imaging follow-up, diagnostic delay, treatment burden, respiratory function。
- 与 `tobacco-nicotine-cessation-continuity/`、`respiratory-oxygenation/` 和 `cancer-survivorship-late-effects-continuity/` 建立接口。
