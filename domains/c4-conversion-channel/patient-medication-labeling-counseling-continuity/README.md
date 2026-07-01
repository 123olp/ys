# Patient Medication Labeling Counseling Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/patient-medication-labeling-counseling-continuity` |
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


## 定位

本域研究药品标签、Medication Guide、Patient Medication Information、处方标签、说明书、药师咨询、语言可及和健康素养如何影响主体理解药物用途、风险、执行要求和求助信号。

它不是药品说明书解释器、诊断建议或个案用药咨询入口。

## 先验问题

```text
药物何以被安全使用？
  -> 风险和执行要求必须以主体能理解的形式出现
  -> 标签、说明、咨询和语言服务必须可达
  -> 主体必须知道何时求助而不是自行猜测
  -> 否则药物信息会成为新的行动摩擦和安全风险
```

## 研究对象

- FDA labeling、Medication Guides、Patient Medication Information。
- 处方瓶标签、辅助标签、用药说明、风险沟通和药师咨询。
- 语言可及、plain language、低健康素养、视觉/认知可访问性。
- OTC 与处方药信息差异、警示疲劳和风险理解。

## 关键变量

- 标签理解度、回忆率、用法错误、风险识别和咨询可达性。
- 语言服务覆盖、字体/版式可读性、认知负担和信息一致性。
- Medication Guide 提供率、咨询率和高风险药物信息完整性。

## 证据入口

- FDA drug labeling、Medication Guides、Patient Medication Information 资料。
- AHRQ health literacy、plain language 和 patient safety 资料。
- 药学、HCI、健康传播和用药安全研究。

## 非目标

- 不解释某个药品对某个人是否适用、如何服用、是否停药或如何处理副作用。
- 不生成个体药品说明、风险判断、患者教育材料或药师咨询替代文本。
- 不收集药名、处方、诊断、药品照片、过敏史或副作用个案。

## 上下游

- 上游：`medicine-access-treatment-continuity/`、`language-access-plain-communication/`、`health-literacy-navigation/`。
- 下游：`medication-reconciliation-regimen-adherence-continuity/`、`pharmacovigilance-drug-safety-monitoring/`。
