# ART Clinic Success Rate Quality Reporting Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/art-clinic-success-rate-quality-reporting-continuity` |
| 分级 | `C4` - 可能性转换通道层 |
| 控制轴 | 路径转换接口 |
| 分级理由 | 关键词显示该域主要处理研究、数据、模型、服务入口、身份记录、转化或治理接口。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何把潜在可能性转成真实可用路径，例如研究、医疗、数据、制度、身份、资金或转化接口？

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


ART 诊所成功率、质量报告与数据可解释连续性，关注 fertility clinic reporting、CDC ART success rates、NASS、数据校验、报告口径、患者构成、分母定义和可解释边界如何影响主体选择和信任。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要把复杂技术服务转化为可比较、可审查、可行动的选择
  -> ART 成功率高度依赖年龄、卵源、周期类型、分母和诊所报告口径
  -> 如果数据不可解释，主体会在高成本、高情绪负担服务中失去判断能力
  -> 因此 ART 质量报告是生殖技术选择权的观测与治理接口
```

## 关注对象

- CDC ART Success Rates、National ART Surveillance System、clinic-specific reports、national summary 和 state-specific surveillance。
- 成功率分母、患者年龄、own eggs / donor eggs、intended retrieval、actual retrieval、transfer、live birth、multiple birth 和数据延迟。
- 数据校验、discrepancy rate、非报告诊所、隐私保护、患者构成差异和误读风险。
- 与 `assisted-reproductive-technology-ivf-cycle-continuity/` 的边界：IVF 域关注周期执行；本域关注周期结果如何被报告、比较和解释。

## Human Infra 模型链路

```text
ART 质量报告 T
  -> 改变成功率口径、诊所可见性、数据质量、风险透明度和选择信息变量 X
  -> 改变主体对服务路径、费用风险、时间窗口和预期管理状态 S
  -> 改变误选、过度承诺、机会成本、资源耗尽和信任崩溃风险 lambda(t)
  -> 影响未来选择权、资源持续性和高成本生殖技术的可审查性
```

## 非目标

- 不提供诊所排名、诊所推荐、成功率个体解释、治疗选择、保险支付或法律建议。
- 不把 clinic-specific ART success rates 写成个人生育概率。
- 不使用报告数据进行个人价值判断、群体污名化或商业营销。

## Source Signals

- CDC ART Success Rates: https://www.cdc.gov/art/success-rates/index.html
- CDC National ART Surveillance System: https://www.cdc.gov/art/php/nass/index.html
- CDC NASS Data Validation: https://www.cdc.gov/art/php/nass/data-validation.html
- CDC Accessing NASS Data: https://www.cdc.gov/art/php/data-access/index.html

## 下一步

1. 建立 ART reporting card：reporting unit、denominator、outcome、lag、validation、privacy 和 interpretation boundary。
2. 与 `assisted-reproductive-technology-ivf-cycle-continuity/`、`uncertainty-quantification-model-calibration/` 和 `data-quality-missingness-representativeness/` 建立接口。
