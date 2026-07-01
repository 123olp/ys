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
