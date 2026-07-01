# Prostate Cancer Screening Treatment Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/prostate-cancer-screening-treatment-continuity` |
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


`prostate-cancer-screening-treatment-continuity/` 研究前列腺癌 PSA 筛查争议、风险分层、主动监测、治疗副作用、泌尿/性功能、心理负担和生活质量如何影响主体持续性。

> 核心问题：前列腺癌连续性不是“筛查越多越好”；它需要同时处理早发现、过度诊断、治疗伤害、主动监测焦虑和男性健康沟通断点。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖高发癌种被合理分层而不过度伤害
  -> 前列腺癌筛查和治疗选择改变死亡风险、尿控/性功能、焦虑和生活质量
  -> 风险分层、主动监测、治疗副作用管理和共享决策决定净持续性收益
  -> 因此前列腺癌是癌症连续性中的收益伤害权衡域
```

## 关注对象

- Prostate cancer screening, PSA controversy, risk stratification, active surveillance, treatment side effects, urinary function, sexual function, shared decision-making。
- 与 `cancer-screening-early-detection-continuity/` 的边界：本域专注前列腺癌特有的筛查争议、过度诊断和功能副作用。
- 与 `urogenital-continuity/` 和 `sexual-health-sti-prevention-continuity/` 的关系：治疗后尿控和性功能是主体连续性的关键变量。

## Human Infra 模型链路

```text
前列腺癌连续性系统 T
  -> 改变 PSA 筛查、风险分层、主动监测、治疗副作用、尿控/性功能和共享决策变量 X
  -> 改变癌症死亡风险、过度诊断、焦虑、身体功能和关系状态 S
  -> 改变死亡、治疗后功能损失、心理负担和有效时间损失 λ(t)
  -> 影响主体健康寿命、尊严、关系安全和未来选择权
```

## 非目标

- 不提供 PSA 判读、筛查决策、活检建议、影像/病理解释、分期、主动监测、治疗方案、用药、手术、放疗或个体建议。
- 不生成个人前列腺癌风险计算器、PSA 解释器、治疗排序、性功能方案或商业检测推广。
- 不收集个案 PSA、MRI、病理、尿控、性功能、症状或治疗资料。

## Source Signals

- NCI prostate cancer: https://www.cancer.gov/types/prostate
- NCI prostate cancer screening: https://www.cancer.gov/types/prostate/screening
- CDC prostate cancer: https://www.cdc.gov/prostate-cancer/

## 下一步

- 建立 Prostate Cancer Continuity Card：screening controversy, risk stratification, active surveillance, treatment burden, urinary / sexual function, shared decision。
- 与 `cancer-control/`、`urogenital-continuity/` 和 `cancer-survivorship-late-effects-continuity/` 建立接口。
