# Medicine Access Treatment Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/medicine-access-treatment-continuity` |
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


`medicine-access-treatment-continuity/` 研究药品可及、用药安全、药品信息、短缺、支付覆盖和治疗连续性，负责把“处方能否变成持续、可理解、可负担、不断供的治疗路径”纳入 Human Infra。

> 核心问题：主体即使获得医疗建议，也可能因为药品短缺、费用、标签不可理解、药房断点、用药错误或覆盖失败而无法持续治疗。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 可修复风险需要持续干预和治疗执行
  -> 关键药物必须可得、可负担、可理解且供应不断
  -> 治疗连续性决定医疗建议能否转化为真实恢复和风险下降
```

## 关注对象

- 基本药物、药品短缺、药品目录、标签说明、患者药品信息和用药安全。
- 处方覆盖、费用负担、药房可及、供应连续、替代路径和用药错误防护。
- 药品作为医疗系统、供应链、支付系统和患者理解能力之间的接口。
- 与 `healthcare-access-continuity/`、`supply-chain-continuity/`、`health-literacy-navigation/` 和 `financial-resilience-access/` 的交叉。

## Human Infra 模型链路

```text
药品与治疗连续性基础设施
  -> 改变关键药物可得性、可负担性、标签理解、供应稳定和用药安全
  -> 改变治疗执行状态和可修复风险控制能力
  -> 降低治疗中断、用药错误、疾病进展和恢复失败风险
  -> 增强健康寿命、有效时间和未来选择权
```

## 非目标

- 不提供用药建议、剂量、替代药物、停药建议、购药建议或处方解释。
- 不替代医生、药师、保险计划、监管机构或急救服务。
- 不把药品目录、短缺信息或标签资料写成个体可用性、保险覆盖或治疗适用性结论。

## Source Signals

- WHO Essential Medicines Lists: https://www.who.int/groups/expert-committee-on-selection-and-use-of-essential-medicines/essential-medicines-lists
- WHO Medication Without Harm: https://www.who.int/initiatives/medication-without-harm
- FDA Drug Shortages: https://www.fda.gov/drugs/drug-safety-and-availability/drug-shortages
- DailyMed: https://dailymed.nlm.nih.gov/dailymed/
- CDC Medication Safety Program: https://www.cdc.gov/medication-safety/

## 下一步

- 建立治疗连续性变量表：可得性、短缺、费用、覆盖、标签、理解、药房接入、错误防护和供应恢复。
- 将药品供应与 `supply-chain-continuity/` 的通用供应链问题拆清。
- 整理基本药物、用药安全、药品短缺和患者药品信息的 Source Cards。
