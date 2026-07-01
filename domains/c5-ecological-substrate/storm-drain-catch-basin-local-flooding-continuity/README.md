# Storm Drain Catch Basin Local Flooding Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/storm-drain-catch-basin-local-flooding-continuity` |
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


`storm-drain-catch-basin-local-flooding-continuity/` 研究雨水口、catch basin、街道积水、局部内涝、落叶垃圾堵塞和雨洪服务请求如何影响邻里出行、住房边界和公共服务可达。

## 先验链路

```text
主体日常行动依赖街道和入口在降雨后仍可通过
  -> 雨水口和 catch basin 把降雨从道路和人行道转移出去
  -> 堵塞、维护延误、低洼积水和局部内涝会切断通行、公交、急救和住房入口
  -> 水深、污染、车辆溅水、绕行和地下室进水风险增加
  -> 邻里级排水失败把天气事件转成行动、住房和卫生连续性损伤
```

## 研究对象

- storm drain、catch basin、local flooding、street flooding、stormwater maintenance、debris blockage、green infrastructure、service request 和降雨后通行状态。

## 不能做

- 不提供排水施工、清掏操作、涉水驾驶、洪水救援、污染判断、地下室抽水、保险索赔、法律责任或个案住房建议。
- 不收集住址、积水照片元数据、车辆信息、保险文件、地下室照片、维修合同或个人位置资料。

## Source Signals

- EPA stormwater management: https://www.epa.gov/npdes/npdes-stormwater-program
- EPA green infrastructure: https://www.epa.gov/green-infrastructure
- FEMA flood safety: https://www.ready.gov/floods
- Open311 GeoReport v2: https://wiki.open311.org/GeoReport_v2/

## 上下游关系

- 上游：`water-resources-hydrology-drought-planning/`、`water-wastewater-utility-service-continuity/`、`green-blue-infrastructure-urban-nature-cooling/`。
- 下游：`basement-flooding-sump-pump-moisture-recovery-continuity/`、`river-flash-flood-warning-evacuation-continuity/`、`municipal-311-service-request-continuity/`。
