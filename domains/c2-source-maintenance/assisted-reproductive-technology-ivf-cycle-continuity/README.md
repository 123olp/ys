# Assisted Reproductive Technology IVF Cycle Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/assisted-reproductive-technology-ivf-cycle-continuity` |
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


辅助生殖技术与 IVF 周期连续性，关注 ART、IVF cycle、促排监测、取卵、实验室受精、胚胎培养、移植、周期取消、并发症边界、费用负担、预约节律和数据记录如何影响生育未来选择权。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体持续性不仅包含当前身体存续，也包含未来选择权和代际路径
  -> 生殖衰老、疾病治疗、结构性不孕和生育窗口会压缩这些选择权
  -> ART/IVF 把配子、胚胎、实验室流程、临床周期、费用和时间窗口连接起来
  -> 因此 IVF 周期连续性是生殖未来选择权被工程化维护的执行接口
```

## 关注对象

- ART 定义、IVF 周期、intended retrieval、actual retrieval、embryo transfer 和 live-birth outcome。
- 促排、监测、取卵、受精、胚胎培养、移植、冷冻、周期取消和多胎风险边界。
- 诊所预约、实验室任务、药品供应、费用支付、工作时间、交通、语言、隐私和心理负担。
- 与 `reproductive-fertility-continuity/` 的边界：上位域关注生殖未来选择权；本域关注 ART/IVF 周期执行链。

## Human Infra 模型链路

```text
ART/IVF 周期 T
  -> 改变取卵机会、受精机会、胚胎可用性、移植机会、费用负担和时间窗口变量 X
  -> 改变主体的生殖计划、心理负担、资源配置和未来选择权状态 S
  -> 改变不孕持续、周期中断、并发症、多胎、费用耗尽和选择权丧失风险 lambda(t)
  -> 影响主体长期计划、有效时间、资源复利和代际路径可选性
```

## 非目标

- 不提供不孕诊断、IVF 方案、促排用药、胚胎移植、周期时机、诊所选择、成功率解释或个体医疗建议。
- 不把 CDC 成功率、估算器或诊所报告写成个人预后。
- 不提供保险、融资、法律、跨境医疗、供体、代孕或胚胎处置建议。

## Source Signals

- CDC About ART: https://www.cdc.gov/art/about/index.html
- CDC ART Success Rates: https://www.cdc.gov/art/success-rates/index.html
- CDC How to Interpret ART Success Rates: https://www.cdc.gov/art/success-rates/interpret.html
- CDC IVF Success Estimator: https://www.cdc.gov/art/ivf-success-estimator/index.html

## 下一步

1. 建立 IVF cycle card：cycle start、retrieval、fertilization、transfer、freeze、cancel、outcome 和 follow-up。
2. 与 `art-clinic-success-rate-quality-reporting-continuity/`、`fertility-preservation-gamete-embryo-cryostorage-continuity/` 和 `preimplantation-genetic-testing-embryo-selection-governance-continuity/` 建立接口。
