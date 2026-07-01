# Pharmacovigilance Drug Safety Monitoring

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/pharmacovigilance-drug-safety-monitoring` |
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


药物警戒、上市后药品安全与不良反应监测域研究：当主体持续性依赖长期药物、疫苗、生物制品和治疗组合时，上市后安全信号、风险评估、标签更新和用药错误监测如何决定治疗收益能否超过伤害。

## 对象

- 药物警戒、不良事件报告、FAERS、主动监测、真实世界安全信号和风险评估。
- 药品、疫苗、生物制品、组合治疗、长期用药、多重用药、相互作用和脆弱人群安全。
- 标签更新、黑框警告、REMS、用药错误、药品召回、风险沟通和患者/临床决策支持。
- 上市前试验与上市后真实世界使用之间的证据缺口。
- 药物安全对治疗连续性、信任、依从性、健康寿命、成本和未来选择权的影响。

## Human Infra 价值

医学技术进入真实人群后，风险函数会继续变化。药物警戒域把“治疗工具在现实世界中是否持续安全”纳入主体持续性模型，避免把药品价值只看成疗效、可及性或价格问题。

```text
药品上市后安全信号被监测和反馈
  -> 不良反应、用药错误和风险沟通滞后下降
  -> 治疗组合更可审查、更可调整、更可信
  -> 主体修复收益和长期用药安全边界提高
```

## 边界

本域只整理公开药物警戒、不良事件、上市后安全、风险沟通和监管资料。

不提供：

- 个体用药、停药、换药、剂量、相互作用判断、疫苗选择或治疗建议。
- 不良事件个案归因、法律责任、索赔、诉讼、医疗纠纷或药品恐慌传播。
- 药品购买、替代、囤积、规避处方、规避 REMS、规避监管或标签绕过建议。
- 数据挖掘用于操纵舆论、商业攻击、虚假不良事件或市场套利。

## 上游与下游

- 上游：`medicine-access-treatment-continuity/`、`clinical-trials-regulatory-science-translation/`、`patient-data-interoperability/`、`health-data-privacy-governance/`。
- 下游：`patient-safety-organizational-learning/`、`measurement-feedback/`、`healthcare-access-continuity/`、`pharmaceutical-quality-supply-integrity/`。

## 初始资料线索

- FDA FAERS resources。
- FDA postmarket drug safety and surveillance resources。
- WHO pharmacovigilance resources。
- WHO Medication Without Harm resources。
