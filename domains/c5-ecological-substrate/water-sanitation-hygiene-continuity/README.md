# Water Sanitation Hygiene Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/water-sanitation-hygiene-continuity` |
| 分级 | `C5` - 可能性生态承载层 |
| 控制轴 | 外部生态承载 |
| 分级理由 | 主要提供主体展开未来所需的基础环境、资源、治理或基础设施。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何承载主体展开未来的外部世界条件，例如能源、水、食物、住房、通信、治理、经济和基础设施？

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


`water-sanitation-hygiene-continuity/` 研究安全饮用水、卫生设施和基本卫生实践能否持续支撑主体健康、尊严、感染控制和日常生活。

> 核心问题：没有安全水、卫生设施和卫生服务，主体持续性会被感染、脱水、照护负担、尊严丧失和公共卫生风险反复截断。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要安全饮用水、排泄处理、洗手和卫生环境
  -> WASH 系统必须可用、可达、可靠、安全且在灾害中不断线
  -> 感染控制、营养吸收、照护、尊严和公共卫生才有基础条件
```

## 关注对象

- 安全饮用水、卫生设施、污水处理、洗手设施、卫生服务和 WASH 覆盖。
- 水源污染、服务中断、灾害下供水、学校/医疗机构 WASH、脆弱群体卫生可及。
- 与胃肠屏障、感染控制、皮肤伤口、家庭照护、灾害响应和住房环境的接口。

## Human Infra 模型链路

```text
水、环境卫生与个人卫生连续性
  -> 安全饮水、排泄处理和卫生实践稳定可用
  -> 感染、脱水、胃肠疾病、照护负担和尊严损害减少
  -> 恢复能力、健康寿命、公共卫生安全和有效时间提高
  -> 主体持续性获得基础生活卫生条件
```

## 非目标

- 不提供个体补水、电解质、疾病处理、水质检测解释、净水设备购买或灾害取水操作建议。
- 不提供污水处理施工、危险环境处置、规避监管或非法取水建议。
- 不把 WASH 问题归因于个人卫生习惯，忽视基础设施、贫困、住房和公共服务条件。

## Source Signals

- WHO/UNICEF JMP: https://washdata.org/
- WHO Drinking-water: https://www.who.int/news-room/fact-sheets/detail/drinking-water
- UNICEF WASH: https://www.unicef.org/wash

## 下一步

- 建立 WASH 变量表：安全水、可及距离、服务可靠性、卫生设施、洗手设施、医疗/学校 WASH 和灾害连续性。
- 整理 WHO/UNICEF JMP、WHO drinking-water、UNICEF WASH 和公共卫生应急 WASH Source Cards。
- 与 `fluid-electrolyte-acid-base-homeostasis/` 明确分工：本域研究外部水卫生系统，后者研究体内水电解质稳态。
