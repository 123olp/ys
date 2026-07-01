# Hurricane Storm Surge Evacuation Shelter Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/hurricane-storm-surge-evacuation-shelter-continuity` |
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


`hurricane-storm-surge-evacuation-shelter-continuity/` 研究飓风、风暴潮、强风、降雨、停电、撤离区、避难所和灾后返回如何影响主体持续性。

> 核心问题：飓风不是单一风雨事件，而是风暴潮、内陆洪水、停电、交通拥堵、医疗中断和住房破坏的组合风险。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体持续性依赖住房、交通、电力、水、通信、医疗和家庭照护
  -> 飓风会同时破坏这些生命线
  -> 若撤离区理解、转移交通、避难接纳和返回判断失败，灾害会从急性危险扩展为长期位移
  -> 因而飓风风暴潮撤离与避难是沿海主体连续性的执行域
```

## 关注对象

- 飓风 watch/warning、风暴潮、强风、内陆洪水、停电、供水中断、医疗设备供能和燃料短缺。
- 撤离区、撤离命令、交通瓶颈、避难所、宠物/服务动物、无障碍需求和灾后返回。
- 与 `coastal-marine-resilience-blue-economy-continuity/` 的边界：该域关注海岸系统长期韧性；本域关注飓风窗口中的撤离、避难和生命线连续性。

## Human Infra 模型链路

```text
飓风撤离与避难系统 T
  -> 改变风暴潮暴露、撤离时间、交通可达、避难接纳、电水通信和医疗供能变量 X
  -> 改变主体在沿海风暴中的安全与服务状态 S
  -> 改变溺水、创伤、热/冷暴露、治疗中断、流离和资源耗竭风险 λ(t)
  -> 影响恢复速度、家庭稳定、有效时间和未来选择权
```

## 非目标

- 不提供实时飓风路径、撤离命令解释、路线选择、避难所推荐、发电机操作、保险或地产建议。
- 不替代 NHC/NWS、FEMA、州/地方应急管理、交通部门或公共安全机构。
- 不鼓励等待最后一刻撤离、穿越封闭道路、规避官方命令或传播未核实路径图。

## Source Signals

- NWS Hurricane Safety: https://www.weather.gov/safety/hurricane
- National Hurricane Center: https://www.nhc.noaa.gov/
- Ready.gov Hurricanes: https://www.ready.gov/hurricanes

## 下一步

- 建立风暴潮、撤离区、避难所、停电生命线、医疗设备供能和灾后返回 source card。
- 与 `backup-power-battery-generator-safety-continuity/`、`pet-disaster-evacuation-sheltering-continuity/` 和 `critical-infrastructure-lifeline-interdependency-resilience/` 对齐。
