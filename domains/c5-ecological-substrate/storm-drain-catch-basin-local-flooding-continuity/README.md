# Storm Drain Catch Basin Local Flooding Continuity

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
