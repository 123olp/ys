# Skin Cancer UV Protection Early Detection Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/skin-cancer-uv-protection-early-detection-continuity` |
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


`skin-cancer-uv-protection-early-detection-continuity/` 研究 UV 暴露、皮肤癌预防、日晒防护、风险沟通、早期识别、转诊可及和职业/户外环境如何影响主体持续性。

> 核心问题：皮肤癌风险是环境暴露、行为、职业、肤色不平等、早期识别和医疗可及共同决定的长期风险。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体皮肤屏障和户外行动暴露于长期 UV 风险
  -> UV 暴露可改变皮肤癌、眼部损伤、职业风险和未来治疗负担
  -> 结果取决于防晒环境、行为支持、风险沟通、早期识别、转诊和公平可及
  -> 因此皮肤癌与 UV 防护是环境暴露控制和癌症早期检测之间的执行域
```

## 关注对象

- UV exposure、sun protection counseling、shade and occupational exposure, skin cancer prevention, early detection access, suspicious lesion referral, skin tone equity, indoor tanning risk。
- 与 `cancer-screening-early-detection-continuity/` 的边界：该域关注癌症筛查总执行；本域关注皮肤癌、UV 暴露和早期识别。
- 与 `skin-barrier-wound-healing/` 的关系：皮肤屏障域关注组织完整性，本域关注 UV/癌症风险。

## Human Infra 模型链路

```text
UV 防护与皮肤癌早识别系统 T
  -> 改变 UV 暴露、防晒环境、风险沟通、早期识别、转诊可及和肤色公平变量 X
  -> 改变皮肤损伤、癌前风险、治疗时机、职业暴露和心理负荷 S
  -> 改变皮肤癌进展、治疗负担、有效时间损失和死亡风险 λ(t)
  -> 影响主体户外行动、工作可持续性、身体完整性和未来选择权
```

## 非目标

- 不提供个人痣/皮损判断、照片诊断、防晒产品选择、筛查周期、治疗、活检、用药或转诊建议。
- 不生成个人皮肤癌风险评分、职业暴露合规判定、保险路径或医疗分诊。
- 不收集个案皮肤照片、病史、肤色、职业、定位、基因或身份敏感资料。

## Source Signals

- CDC skin cancer prevention: https://www.cdc.gov/skin-cancer/prevention/
- USPSTF skin cancer prevention counseling: https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/skin-cancer-counseling
- NCI skin cancer prevention: https://www.cancer.gov/types/skin/patient/skin-prevention-pdq

## 下一步

- 建立 Skin UV Continuity Card：exposure, protection environment, counseling, early recognition, referral, equity, occupational risk。
- 与 `cancer-screening-early-detection-continuity/`、`skin-barrier-wound-healing/` 和 `occupational-exposure-industrial-hygiene/` 建立接口。
