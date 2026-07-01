# Taxi Rideshare Demand Response Mobility Continuity

`taxi-rideshare-demand-response-mobility-continuity` 研究出租车、网约车、社区按需交通、需求响应公交、司机供给、价格波动、安全、无障碍车辆和平台停权如何影响主体临时移动能力。

> 核心问题：不是所有出行都能提前计划；当公共交通不可达、车辆不可用或紧急任务出现时，按需交通可能是主体进入医疗、工作、照护和安全地点的最后路径。

## 关注对象

- 出租车、TNC/网约车、需求响应交通、社区交通、无障碍车辆、司机供给、等待时间、动态价格和平台治理。
- 夜间、郊区、低密度地区、老年人、残障者、无车家庭、医院出院、危机撤离和安全回家场景。
- 与公共交通、paratransit/NEMT、在线平台治理、消费者保护和人身安全的接口。

## Human Infra 链路

```text
按需移动连续
  -> 临时、低频、紧急和最后一公里出行有替代路径
  -> 无车、行动受限或公共交通不可达主体的任务失败率下降
  -> 移动系统获得弹性冗余
  -> 医疗、工作、照护和安全地点可达性增强
```

## 非目标

- 不提供绕过平台规则、刷单、规避费用、司机/乘客骚扰、跟踪定位、安全规避或个案争议策略。
- 不替代出租车监管机构、平台、交通运营商、保险、执法、律师或安全服务。
- 不收集乘车记录、位置轨迹、司机/乘客身份、支付凭证、争议材料或安全事件细节。

## Source Signals

- FTA Mobility on Demand resources: https://www.transit.dot.gov/
- U.S. DOT Complete Trip / Mobility innovation materials: https://www.transportation.gov/
- FTC Rideshare and gig economy consumer guidance: https://consumer.ftc.gov/
- ADA.gov Transportation: https://www.ada.gov/topics/transportation/

## 下一步

- 建立 `trip urgency -> service option -> wait/price/reliability -> safety/accessibility -> task outcome` 变量表。
- 区分出租车、网约车、微公交、社区交通、无障碍车辆和医院/服务机构协调交通。
- 与 `platform-account-suspension-appeals-continuity`、`personal-safety-violence-prevention`、`public-transit-service-operations-continuity` 和 `paratransit-nemt-access-continuity` 建立边界。
