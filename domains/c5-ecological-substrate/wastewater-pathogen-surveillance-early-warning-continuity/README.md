# Wastewater Pathogen Surveillance Early Warning Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/wastewater-pathogen-surveillance-early-warning-continuity` |
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


`wastewater-pathogen-surveillance-early-warning-continuity/` 研究污水病原体监测、早期预警、趋势解释、地域聚合、隐私边界和公共卫生决策接口如何支撑主体持续性。

> 核心问题：污水信号把个体无法及时报告的感染变化转化为社区级早期预警，但它必须被正确聚合、解释和治理。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 暴发早期个体检测和就医信号常常滞后
  -> 污水监测提供社区级病原体趋势观测
  -> 早期预警使公共卫生、学校、医疗和家庭系统更早调整风险控制
```

## 关注对象

- NWSS、污水病原体监测、采样网络、趋势信号、社区聚合、隐私边界、结果沟通和公共卫生触发器。
- 与 `water-wastewater-utility-service-continuity/` 的关系：水务域关注公用事业服务；本域关注污水作为公共卫生早期预警信号。

## Human Infra 模型链路

```text
污水病原体早期预警
  -> 改变社区级传播趋势观测和预警时滞
  -> 改变学校、医疗、公共卫生和家庭准备的提前量
  -> 降低暴发发现过晚、医疗挤兑和过度/不足响应风险
  -> 增强风险治理、有效行动和主体持续性
```

## 非目标

- 不提供采样教程、设施定位、结果个体化解释、社区点名、污名化、实时恐慌传播或检测规避。
- 不提供水务设施操作、排污绕行、样本处理、实验室协议或地方政策指挥。
- 不把社区趋势信号写成个体诊断或确定性预测。

## Source Signals

- CDC National Wastewater Surveillance System: https://www.cdc.gov/nwss/
- CDC wastewater surveillance data: https://www.cdc.gov/nwss/wastewater-surveillance.html
- WHO wastewater surveillance resources: https://www.who.int/
- WastewaterSCAN public dashboard: https://data.wastewaterscan.org/

## 下一步

- 建立变量表：采样覆盖、检测目标、趋势变化、报告延迟、地域聚合、隐私边界、触发规则和风险沟通。
- 与 `immunization-public-health-surveillance/`、`public-health-laboratory-diagnostic-capacity/`、`water-wastewater-utility-service-continuity/` 和 `community-testing-screening-access-continuity/` 建立接口。
