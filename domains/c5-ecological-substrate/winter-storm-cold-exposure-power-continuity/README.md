# Winter Storm Cold Exposure Power Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/winter-storm-cold-exposure-power-continuity` |
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


`winter-storm-cold-exposure-power-continuity/` 研究冬季风暴、极寒、冰雪、停电、供暖、道路中断和低体温风险如何影响主体持续性。

> 核心问题：冬季风暴把温度、住房、供电、取暖燃料、交通、药物和医疗设备连接成一个急性生命线系统。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要可维持体温的住房、能源和交通服务
  -> 冬季风暴会同时制造寒冷暴露、停电、道路封闭、跌倒和医疗延迟
  -> 若供暖、备用电、通信、食水和交通失败，寒冷会从环境变量变成急性死亡风险
  -> 因而冬季风暴与寒冷暴露是主体温控和生命线连续性执行域
```

## 关注对象

- Winter storm warning、冰雪、冰冻降雨、风寒、低体温、冻伤、道路封闭、跌倒和孤立。
- 供暖、电力、燃料、备用电、CO 风险、医疗设备、药物冷链、家庭照护和无家可归暴露。
- 与 `thermal-homeostasis-resilience/` 的边界：该域关注生理体温调节；本域关注冬季风暴造成的住房、能源和服务执行断裂。

## Human Infra 模型链路

```text
冬季风暴与寒冷防护系统 T
  -> 改变室内温度、供电供暖、交通可达、跌倒暴露、药物设备和通信变量 X
  -> 改变主体在极寒窗口中的稳定状态 S
  -> 改变低体温、冻伤、CO 中毒、治疗中断、跌倒和孤立风险 λ(t)
  -> 影响急性生存、恢复能力、有效时间和照护负担
```

## 非目标

- 不提供实时道路、取暖设备操作、发电机使用、低体温急救、药物处理、车辆救援或个体医疗建议。
- 不替代 NWS、地方应急管理、公用事业、消防、医疗或公共安全机构。
- 不鼓励室内使用危险燃烧设备、封闭空间发电、冒险出行或忽视撤离/保暖警告。

## Source Signals

- NWS Winter Weather Safety: https://www.weather.gov/safety/winter
- Ready.gov Winter Weather: https://www.ready.gov/winter-weather
- CDC Winter Weather: https://www.cdc.gov/winter-weather/

## 下一步

- 建立 wind chill、停电供暖、CO 风险、道路封闭、跌倒、药物/医疗设备和照护者准备 source card。
- 与 `backup-power-battery-generator-safety-continuity/`、`carbon-monoxide-alarm-combustion-appliance-safety-continuity/` 和 `fuel-thermal-energy-service-continuity/` 对齐。
