# Parking Curb Access Towing Impound Continuity

`parking-curb-access-towing-impound-continuity` 研究停车、路缘上下客、装卸、残障停车、罚单、拖车、扣押、取回流程和费用如何影响主体能否完成出行并保留车辆移动能力。

> 核心问题：到达目的地不等于完成出行；如果停车、路缘访问、拖车和扣押链失控，移动任务会在最后几十米、罚费和车辆取回流程上失败。

## 关注对象

- 停车位、路缘管理、上下客、装卸、残障停车、停车支付、罚单、拖车、扣押、取回和费用。
- 医疗、照护、学校、工作、配送、搬家、灾害撤离和低收入车辆依赖场景。
- 与城市规划、公共交通、道路安全、消费者保护、法律援助和财务韧性的接口。

## Human Infra 链路

```text
停车与路缘访问连续
  -> 出行的最后一段、上下客和车辆保留可执行
  -> 罚单、拖车、扣押和费用冲击不再轻易切断移动能力
  -> 目的地可达性从地图路径转化为真实任务完成
  -> 主体医疗、工作、照护和公共服务接入增强
```

## 非目标

- 不提供逃避停车执法、规避罚单、隐藏车辆、绕过拖车、伪造残障许可或法律个案策略。
- 不替代本地交通部门、停车机构、DMV、法院、律师、执法、拖车场或消费者保护机构。
- 不收集车牌、停车记录、罚单、扣押单、位置轨迹、残障许可或个人支付信息。

## Source Signals

- U.S. DOT Curb Management resources: https://www.transportation.gov/
- FHWA Curbside Inventory / Curb Management materials: https://ops.fhwa.dot.gov/
- ADA.gov Parking guidance: https://www.ada.gov/
- USA.gov Traffic Tickets: https://www.usa.gov/traffic-tickets

## 下一步

- 建立 `destination -> curb/parking access -> payment/enforcement -> vehicle retention -> task completion` 变量表。
- 区分残障停车、医疗上下客、商业装卸、住宅停车、拖车扣押和罚费负担。
- 与 `urban-planning-land-use-zoning-resilience`、`transportation-access-mobility`、`access-to-justice-legal-aid` 和 `financial-resilience-access` 建立边界。
