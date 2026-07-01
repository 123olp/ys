# Bloodborne Pathogens Sharps Injury Worker Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/bloodborne-pathogens-sharps-injury-worker-continuity` |
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


`bloodborne-pathogens-sharps-injury-worker-continuity/` 研究血源性病原体、针刺/锐器伤、医疗和照护工作者暴露、报告、随访、污名和长期心理负担如何影响主体持续性。

核心问题：

> 照护别人时，主体可能通过血液、锐器和体液暴露承担感染和焦虑风险；安全系统必须保护照护者本身的身体、时间和尊严。

## 先验位置

```text
有效永生 / 主体持续性
  -> 医疗、照护、清洁和应急工作需要接触血液、锐器和体液
  -> 针刺或锐器伤可能暴露 HBV、HCV、HIV 等血源性病原体
  -> 暴露后报告、评估、随访和心理负担会影响工作者持续行动
  -> 因此血源性病原体与锐器伤治理是照护系统保护自身的条件
```

## 关注对象

- Bloodborne pathogens、needlestick injuries、sharps injury、HBV/HCV/HIV exposure context、exposure control plan、reporting and follow-up。
- 风险链：照护/清洁任务 -> 锐器/血液暴露 -> 报告/随访断裂 -> 感染风险/焦虑/污名 -> 工作退出或持续负担。
- 制度链：engineering controls、safer devices、training、vaccination context、post-exposure workflow、confidentiality。

## Human Infra 模型位置

```text
照护/医疗任务 T
  -> 改变血液和锐器暴露 X
  -> 改变感染风险、心理负担和工作状态 S
  -> 改变长期健康/工作退出风险 lambda(t)
  -> 改变照护人力、家庭资源和未来选择权
```

## 非目标

- 不提供暴露后处理、PEP、检测、疫苗、用药、针刺处置、感染判断、职业健康流程、报告表填写或个人医疗建议。
- 不判断个人风险、雇主责任、工伤、隐私投诉、OSHA 违规、复工或法律策略。
- 不帮助隐藏暴露、规避报告、重复使用锐器、绕开感染控制或收集可识别健康资料。

## Source Signals

- OSHA Bloodborne Pathogens: https://www.osha.gov/bloodborne-pathogens
- CDC/NIOSH Bloodborne Infectious Diseases: https://www.cdc.gov/niosh/topics/bbp/

## 下一步

- 建立 Sharps Exposure Continuity Card：task context、sharp type、exposure pathway、reporting latency、follow-up boundary、stigma/confidentiality。
- 与 `health-workforce-capacity/`、`sterilization-disinfection-infection-control/` 和 `occupational-exposure-industrial-hygiene/` 建立接口。
