# Home Clutter Pathway Trip Fall Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/home-clutter-pathway-trip-fall-continuity` |
| 分级 | `C5` - 可能性生态承载层 |
| 控制轴 | 外部生态承载 |
| 分级理由 | 关键词显示该域主要承载能源、水、食物、住房、治理、经济、通信、灾害或基础设施环境。 |
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


`home-clutter-pathway-trip-fall-continuity` 研究地面杂物、临时堆放、通道占用、地毯边缘、玩具、衣物、包裹和夜间路径如何影响跌倒风险、照护执行和家庭任务连续性。

> 核心问题：主体不是只在“设计好的房间”里行动，而是在不断变化的物品流、包裹、衣物、玩具和临时堆放之间行动；通道被杂物侵占时，行动能力会被日常摩擦切断。

## 关注对象

- 走道、卧室到浴室路径、厨房通道、门口、楼梯口、床边、玄关和紧急出口附近的临时物品占用。
- 地毯边缘、电线交叉、包裹堆放、衣物篮、玩具、宠物用品、清洁工具和夜间低可见度场景。
- 老人、儿童、低视力者、术后恢复者、行动辅助器具使用者、照护者和高频夜间起身者。
- 通道状态如何影响跌倒、取物、照护响应、用药、夜间如厕、撤离和家庭协作。

## Human Infra 链路

```text
家庭通道杂物可控
  -> 地面路径、床边和门口的绊倒暴露下降
  -> 夜间起身、照护响应、取物、撤离和日常移动更稳定
  -> 跌倒、延迟、回避行动和照护负担减少
  -> 主体行动半径、有效时间和家庭任务连续性提高
```

## 非目标

- 不提供家庭改造、收纳产品购买、现场整理服务、跌倒急救、个体医疗评估、照护监控、保险、租房纠纷或法律建议。
- 不替代 CDC、NIA、地方公共卫生、医疗人员、职业治疗师、物业、消防或建筑安全专业人员。
- 不把“整洁”当作道德要求；只讨论通道、路径、物品流和任务执行之间的风险关系。

## Source Signals

- CDC STEADI Check for Safety: https://www.cdc.gov/steadi/pdf/STEADI-Brochure-CheckForSafety-508.pdf
- NIA Prevent Falls and Fractures: https://www.nia.nih.gov/health/falls-and-falls-prevention/prevent-falls-and-fractures
- CDC Older Adult Falls: https://www.cdc.gov/falls/

## 下一步

- 建立 `pathway obstruction -> trip exposure -> task interruption -> continuity outcome` 变量表。
- 区分临时杂物、结构性拥挤、照明不足、辅助器具转弯半径不足和紧急出口占用。
- 与 `fall-risk-prevention-home-safety-continuity`、`stairs-steps-handrail-threshold-fall-safety-continuity` 和 `home-lighting-nighttime-pathway-visibility-continuity` 建立边界。
