# Dietary Supplement Nutraceutical Evidence Safety Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/dietary-supplement-nutraceutical-evidence-safety-continuity` |
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

<!-- domain-research-skeleton:start -->
## 研究推进骨架

### 最小问题集

- 界定转化瓶颈：研究发现、数据、临床、制度、身份、资金、可及性或操作接口。
- 说明接口机制：潜在可能性如何经过标准、流程、记录、组织或平台变成可用路径。
- 记录必要证据：登记系统、指南、监管材料、数据库、标准文档或真实世界部署资料。
- 识别摩擦指标：时间成本、资金成本、信息成本、合规成本、可及性和协作成本。
- 列出失败点：证据断裂、监管阻塞、制度排斥、隐私风险、责任不清或资源不可达。

### 变量接口

- 输入变量：本域直接处理的对象、资源、技术、环境、制度或状态。
- 中间机制：变量通过什么因果路径改变主体状态、系统状态或外部条件。
- 状态改变：身体、认知、能力、资源、风险暴露、可及性、时间成本或协作条件如何变化。
- 风险 / 成本函数：死亡风险、失能风险、工程风险、尾部风险、机会成本、维护成本或治理成本如何变化。
- 输出指标：有效寿命、健康寿命、有效时间、主观时间、相对时间、行动能力、恢复能力或未来选择权。

### 证据入口

- 官方 / 原始资料：监管文件、数据库、临床登记、标准、论文原文、项目白皮书或一手报告。
- 综述 / 指南 / 标准：系统综述、领域指南、技术标准、伦理规范和权威机构材料。
- 数据集 / 登记系统：可复核的数据表、代码、实验记录、登记号、版本和采集边界。
- 反例 / 失败案例：负结果、副作用、安全事故、不可复现结果、伦理争议和误用案例。

### 最小产出

- Source Signals：记录候选资料、来源、日期、主张和待核验点。
- Source Cards：提取 claim、变量、机制、证据类型、边界、反证条件和可迁移位置。
- Claim-Evidence Matrix：把每个稳定主张绑定到来源、证据等级、适用范围和不确定性。
- 变量表：列出输入变量、中间变量、状态变量、风险变量、输出指标和可观测代理指标。
- 上下游关系：说明本域依赖哪些更根本域，并向哪些转化、应用或基础设施域输出。
<!-- domain-research-skeleton:end -->

`dietary-supplement-nutraceutical-evidence-safety-continuity/` 研究膳食补充剂、nutraceuticals、维生素、矿物质、植物提取物、益生菌、运动补剂和“长寿补剂”如何进入证据、安全、标签和药物相互作用治理。

> 核心问题：补剂不是低风险药物，也不是天然即安全。它们必须被放进成分、剂量、标签、污染、相互作用、不良事件和证据等级系统中审查。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要稳定营养输入、恢复能力和风险控制
  -> 补剂可能影响缺乏状态、代谢、免疫、睡眠、运动恢复和药物暴露
  -> 但补剂市场存在证据弱、标签不准、污染、相互作用和夸大宣传
  -> 因此补剂必须作为证据安全治理域，而不是长寿捷径
```

## 关注对象

- vitamins、minerals、omega-3、creatine、probiotics、botanicals、NAD+ precursors、polyphenols、adaptogens、运动与减重产品。
- 标签声明、成分数据库、第三方检测、药物相互作用、不良事件、污染掺假、特殊人群风险和营销 claims。
- 与 `nutrition-metabolic-health/` 的边界：营养代谢域关注饮食和代谢状态；本域关注补剂产品、标签、证据和安全。
- 与 `pharmacovigilance-drug-safety-monitoring/` 的边界：药物安全域关注药品安全；本域关注食品/补剂监管框架与消费品风险。

## Human Infra 模型链路

```text
补剂 / nutraceutical T
  -> 影响营养缺乏、代谢、炎症、睡眠、运动恢复或药物相互作用 X
  -> 改变身体状态 S 或风险暴露
  -> 改变健康寿命、有效时间、恢复能力或副作用风险
  -> 若证据弱、标签不明或相互作用不可控，则进入风险扣减而非收益项
```

## 非目标

- 不提供补剂购买、剂量、品牌、搭配、周期、检测解释或个体建议。
- 不把“天然”“热门”“动物研究”“机制合理”写成安全或有效。
- 不替代营养、医学、药学、毒理、孕产、儿童或慢病专业判断。
- 不推广减重、增肌、性功能、认知增强或抗衰营销 claims。

## Source Signals

- NIH Office of Dietary Supplements: https://ods.od.nih.gov/
- ODS Dietary Supplements: What You Need to Know: https://ods.od.nih.gov/factsheets/WYNTK-Consumer/
- ODS Dietary Supplement Fact Sheets: https://ods.od.nih.gov/factsheets/list-all/
- ODS Dietary Supplement Label Database: https://ods.od.nih.gov/Research/Dietary_Supplement_Label_Database.aspx
- FDA Dietary Supplements: https://www.fda.gov/food/dietary-supplements
- FDA 101 Dietary Supplements: https://www.fda.gov/consumers/consumer-updates/fda-101-dietary-supplements

## 下一步

1. 建立补剂证据分层：缺乏纠正、疾病终点、运动表现、替代 biomarker、长期安全和特殊人群。
2. 建立 label / ingredient / interaction / adverse event 四卡片审查模板。
3. 与 `medicine-access-treatment-continuity/`、`pharmaceutical-quality-supply-integrity/` 和 `nutrition-metabolic-health/` 建立边界。
