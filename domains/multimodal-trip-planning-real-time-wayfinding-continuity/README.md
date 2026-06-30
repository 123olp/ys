# Multimodal Trip Planning Real Time Wayfinding Continuity

`multimodal-trip-planning-real-time-wayfinding-continuity` 研究路线规划、实时到站、GTFS/GTFS-Realtime、无障碍路径、服务中断、导航、站内导向和语言可达如何影响主体能否把出行计划转成真实到达。

> 核心问题：交通选项存在不等于主体能使用；如果路线、时间、换乘、无障碍路径和服务中断信息不可知，主体会在规划、等待、换乘和迷路中消耗有效时间。

## 关注对象

- GTFS、GTFS-Realtime、公交/轨道实时信息、换乘、站点导向、无障碍路径、步行连接、服务中断和多语言信息。
- 医疗预约、工作通勤、学校接送、夜间出行、游客、认知障碍者、低视力/低听力者和低数字技能人群。
- 与地理空间导航、公共交通运营、语言可达、无障碍、通知警报和数字包容的接口。

## Human Infra 链路

```text
出行信息连续
  -> 路线、时间、换乘、无障碍和中断信息可被理解
  -> 等待、迷路、错过换乘和迟到成本下降
  -> 多模式交通从抽象网络转化为可执行路径
  -> 主体有效时间、服务到达率和行动信心增强
```

## 非目标

- 不提供逃票、绕过安检、跟踪他人、抓取私有位置数据、破坏交通数据或规避平台限制方法。
- 不替代交通运营商、地图平台、应急警报、无障碍服务、旅行安全、医疗或本地服务渠道。
- 不收集个人位置轨迹、常用路线、家庭地址、工作地址、医疗预约、儿童路线或账号 token。

## Source Signals

- GTFS Schedule: https://gtfs.org/schedule/
- GTFS Realtime: https://gtfs.org/realtime/
- FTA Transit Data and Mobility resources: https://www.transit.dot.gov/
- ADA.gov Transportation: https://www.ada.gov/topics/transportation/

## 下一步

- 建立 `origin/destination -> route data -> real-time signal -> accessibility path -> arrival outcome` 变量表。
- 区分公共静态数据、实时中断、站内导向、语言可达、无障碍路径和数字排除。
- 与 `geospatial-navigation-location-infrastructure`、`public-transit-service-operations-continuity`、`language-access-plain-communication` 和 `notification-alert-routing-attention-continuity` 建立边界。
