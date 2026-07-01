# Registries Real World Data Governance

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/registries-real-world-data-governance` |
| 分级 | `C4` - 可能性转换通道层 |
| 控制轴 | 路径转换接口 |
| 分级理由 | 主要把科学、医疗、数据、制度或技术从潜在能力转成真实可用路径。 |
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


`registries-real-world-data-governance/` 研究患者登记、疾病登记、产品登记、真实世界数据、真实世界证据、数据模型、质量评估和治理边界，如何把现实照护过程转化为可审查证据。

> 核心问题：很多 Human Infra 路径不可能只靠随机试验理解。药物、器械、罕见病、长期照护、复杂慢病和高风险技术都需要登记系统与真实世界数据反馈。但登记系统如果定义混乱、缺失严重或治理失效，会制造规模化误判。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要理解技术和照护在真实世界中的长期效果、安全性和可及性
  -> 真实世界证据依赖登记系统、数据模型、质量控制、结局定义和治理
  -> 登记缺失、选择偏差、数据漂移和用途越界会污染效果与风险判断
  -> 因此登记与真实世界数据治理是技术进入现实后的反馈域
```

## 关注对象

- 患者登记、疾病登记、产品登记、器械登记、治疗登记、罕见病登记和结局登记。
- 真实世界数据、真实世界证据、EHR、claims、患者报告数据、数据模型、数据质量和治理。
- 长期安全、有效性、可及性、公平性、上市后反馈和技术扩散监测。
- 与 `clinical-trials-regulatory-science-translation/` 的边界：临床试验域关注试验与监管证据路径；本域关注真实世界登记和持续反馈。
- 与 `patient-data-interoperability/` 的边界：患者数据互操作域关注数据流通标准；本域关注登记系统作为证据工具的治理与质量。

## Human Infra 模型链路

```text
登记与真实世界数据治理 T
  -> 改变结局定义、数据完整性、随访、代表性、质量审计和用途边界变量 X
  -> 改变技术真实世界效果、安全性和扩散状态 S
  -> 改变上市后风险遗漏、效果外推、数据漂移和证据错配风险 λ(t)
  -> 影响技术采用、监管反馈、患者安全和主体持续性路径修正
```

## 非目标

- 不提供越权访问 EHR、重新识别、规避 HIPAA/IRB、操控登记入组或选择性报告策略。
- 不把真实世界数据写成自动因果结论；必须区分描述、预测、因果和监管证据。
- 不替代监管机构、数据使用协议、隐私审查或统计分析计划。

## Source Signals

- AHRQ Registries for Evaluating Patient Outcomes: https://effectivehealthcare.ahrq.gov/products/registries-guide-4th-edition/research
- FDA Real-World Evidence: https://www.fda.gov/science-research/science-and-research-special-topics/real-world-evidence
- FDA Real-World Data and Real-World Evidence Guidances: https://www.fda.gov/science-research/science-and-research-special-topics/real-world-evidence
- OHDSI OMOP Common Data Model: https://ohdsi.github.io/CommonDataModel/
- ClinicalTrials.gov: https://clinicaltrials.gov/

## 下一步

- 建立登记系统变量表：目标人群、入组规则、结局定义、随访、缺失、数据来源、质量审计和用途限制。
- 与 `pharmacovigilance-drug-safety-monitoring/`、`medical-device-equipment-safety-maintenance/`、`rare-disease-diagnostic-odyssey-care-coordination/` 和 `causal-inference-target-trial-emulation/` 建立接口。
