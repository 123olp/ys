# Drought Water Restriction Household Health Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/drought-water-restriction-household-health-continuity` |
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


`drought-water-restriction-household-health-continuity/` 研究干旱、供水限制、井水/水源压力、食品和野火协同风险如何影响主体持续性。

> 核心问题：干旱不是单纯降雨不足，而是水、食物、卫生、能源、热风险、野火和经济压力共同改变主体可持续生活条件。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要稳定、安全、可负担的水输入
  -> 干旱会压缩饮水、卫生、农业、能源、生态和消防缓冲
  -> 若水限制、供水替代、健康沟通和资源支持失败，慢性自然压力会转化为健康与经济风险
  -> 因而干旱和家庭水限制是主体资源连续性执行域
```

## 关注对象

- 干旱监测、干旱早期预警、供水限制、井水风险、水价压力、农业/食品影响和野火协同。
- 家庭用水、卫生、饮水安全、热风险、慢病/药物需求、社区援助和公共沟通。
- 与 `soil-health-land-degradation-drought-resilience/` 的边界：该域关注土壤土地和旱灾韧性；本域关注家庭/社区水限制和健康执行链。

## Human Infra 模型链路

```text
干旱与水限制治理系统 T
  -> 改变水量、水质、价格、卫生、食品供应、热暴露和野火协同变量 X
  -> 改变主体资源输入和健康维护状态 S
  -> 改变脱水、感染、营养不稳、热病、经济冲击和迁移风险 λ(t)
  -> 影响有效时间、家庭稳定、恢复储备和未来选择权
```

## 非目标

- 不提供水权、农业灌溉、井水处理、法律合规、投资、地产、家庭用水处方或医疗建议。
- 不替代 Drought.gov、地方供水机构、公共卫生、农业推广或应急管理机构。
- 不鼓励违反水限制、囤积关键资源、传播水源恐慌或基于未核实数据做迁移建议。

## Source Signals

- Drought.gov: https://www.drought.gov/
- U.S. Drought Monitor: https://droughtmonitor.unl.edu/
- Ready.gov Drought: https://www.ready.gov/drought

## 下一步

- 建立干旱监测、家庭水限制、公共卫生、食品价格、野火协同和社区支持 source card。
- 与 `water-sanitation-hygiene-continuity/`、`water-wastewater-utility-service-continuity/` 和 `wildfire-landscape-fire-resilience/` 对齐。
