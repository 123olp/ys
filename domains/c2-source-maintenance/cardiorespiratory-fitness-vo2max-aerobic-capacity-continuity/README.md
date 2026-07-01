# Cardiorespiratory Fitness VO2max Aerobic Capacity Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/cardiorespiratory-fitness-vo2max-aerobic-capacity-continuity` |
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


`cardiorespiratory-fitness-vo2max-aerobic-capacity-continuity/` 研究心肺适能、VO2max、有氧容量、耐力、运动测试和死亡/慢病风险预测如何进入主体持续性模型。

> 核心问题：心肺适能是主体把氧、血流、肌肉和代谢系统组织成持续行动能力的综合指标，但它不能被简化为穿戴设备分数或单次跑步表现。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要长期维持氧输送、循环、代谢和运动耐受
  -> 心肺适能下降会限制工作、避险、康复、旅行、照护和长期任务执行
  -> VO2max / CRF 与死亡率和多种慢病风险存在强相关
  -> 因此有氧容量是寿命模型中的功能储备和风险预测研究域
```

## 关注对象

- cardiorespiratory fitness、VO2max、METs、aerobic capacity、exercise treadmill testing、submaximal estimates、wearable estimates 和 endurance adaptation。
- 死亡率、心血管风险、代谢风险、恢复能力、运动耐受、过度训练、心律风险和测量误差。
- 与 `cardiovascular-resilience/` 的边界：心血管韧性域关注疾病和循环风险；本域关注适能作为功能储备和预测指标。
- 与 `physical-activity-mobility/` 的边界：身体活动域关注活动行为；本域关注心肺适能状态和容量指标。

## Human Infra 模型链路

```text
有氧训练 / 心肺适能 T
  -> 影响 VO2max、心输出量、血管功能、线粒体能力、代谢灵活性和耐力 X
  -> 改变身体状态 S、运动耐受和功能储备
  -> 改变心血管事件、全因死亡、失能和恢复风险
  -> 影响健康寿命、有效时间和未来选择权
```

## 非目标

- 不提供跑步、骑行、HIIT、Zone 2、测试协议、训练计划或个体运动建议。
- 不把 wearables 估算 VO2max、单次测试或竞技表现写成医学结论。
- 不替代心血管评估、运动医学、康复、急性症状分诊或专业测试。
- 不鼓励高风险人群自行进行最大运动测试或高强度训练。

## Source Signals

- HHS Physical Activity Guidelines for Americans: https://odphp.health.gov/our-work/nutrition-physical-activity/physical-activity-guidelines
- WHO physical activity guidelines: https://www.who.int/publications/i/item/9789240015128
- CDC adult physical activity basics: https://www.cdc.gov/physical-activity-basics/guidelines/adults.html
- Cardiorespiratory fitness and long-term mortality: https://pubmed.ncbi.nlm.nih.gov/30646252/
- CRF as quantitative predictor meta-analysis: https://pubmed.ncbi.nlm.nih.gov/19454641/
- CRF and incident chronic conditions review: https://pubmed.ncbi.nlm.nih.gov/38599681/

## 下一步

1. 建立心肺适能变量表：VO2max、METs、静息心率、恢复心率、运动耐受和测量来源。
2. 区分行为输入、适能状态、疾病风险和功能输出，避免把运动量与适能混写。
3. 与 `cardiovascular-resilience/`、`mitochondrial-bioenergetics/` 和 `survival-analysis-healthspan-risk-modeling/` 建立接口。
