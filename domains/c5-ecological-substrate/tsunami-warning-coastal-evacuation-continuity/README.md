# Tsunami Warning and Coastal Evacuation Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/tsunami-warning-coastal-evacuation-continuity` |
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


## 核心问题

海啸风险决定沿海主体能否在短时间窗口内接收预警、理解风险、完成撤离，并在冲击后恢复住房、医疗、通信、交通和供水。

Human Infra 关注的问题不是海洋学本身，而是：

```text
海啸预警、撤离路径和灾后恢复如何决定沿海主体是否能穿过极短风险窗口？
```

## 先验位置

主体持续性需要危机信息可达、撤离路径可行、物理移动能力可用、照护对象可转移、公共通信可持续。海啸把预警、空间规划、交通、无障碍和社区信任压缩成分钟级生命窗口。

## 关注对象

- 地震海啸、远场海啸、近场海啸、预警系统、潮位监测和警报分发。
- 疏散路线、垂直避难、无障碍撤离、交通拥堵、社区演练和风险沟通。
- 灾后饮水、卫生、住房、医疗、通信、港口和经济恢复。

## Human Infra 模型链路

```text
海啸触发事件
  -> 预警、理解、撤离和避难链条被测试
  -> 沿海主体面临短窗口高后果冲击
  -> 住房、交通、医疗、港口和基础服务恢复压力上升
  -> 主体持续性取决于预警-行动-恢复系统是否闭环
```

## 非目标

- 不提供实时海啸预警、撤离路线、避难点选择或个人风险判断。
- 不替代 NOAA、地方应急管理、海岸工程或公共安全机构。
- 不把海啸风险写成旅游、购房、保险或投资建议。

## Source Signals

- NOAA Tsunami: https://www.tsunami.gov/
- NOAA Tsunami Warning Centers: https://www.tsunami.gov/?page=warning_centers
- Ready.gov Tsunami: https://www.ready.gov/tsunamis
