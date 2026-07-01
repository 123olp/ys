# 0118. Add One-Hundred-Thirteenth Wave Neighborhood Public Space Maintenance Service Request Domains

Date: 2026-07-01

## Status

Accepted

## Context

Human Infra 已经覆盖家庭内部运行、公共空间生存接入、个人移动和公共工程资产管理，但仍缺少一组更贴近日常行动的“邻里公共空间维护执行层”：问题如何从居民观察进入服务请求系统，夜间路径是否可见，人行道和坡道是否可通行，冬季雪冰是否把路径封死，街道树木是树荫资产还是断枝/根系风险，雨水口是否能在降雨后维持街道可通过。

这些对象不是 `public-works-civil-infrastructure-asset-management` 的重复。公共工程资产管理关注资产组合与机构能力，本批域关注主体在街区尺度遇到的可报告、可维护、可修复的行动接口。

## Decision

新增 6 个正式研究域：

- `domains/municipal-311-service-request-continuity/`
- `domains/streetlight-outage-nighttime-visibility-continuity/`
- `domains/sidewalk-curb-ramp-maintenance-access-continuity/`
- `domains/snow-ice-sidewalk-winter-access-continuity/`
- `domains/street-tree-branch-hazard-shade-maintenance-continuity/`
- `domains/storm-drain-catch-basin-local-flooding-continuity/`

这批域共同构成“邻里公共空间维护、地方服务请求与最后一公里公共工程执行连续性”视角，关注公共空间问题如何从个人暴露转化为可报告、可派单、可维护、可复盘的服务对象。

## Boundaries

- 不提供紧急报警替代、维修施工、除雪操作、涉水驾驶、树木修剪、照明工程、ADA 法律意见、投诉代写、执法规避、服务商推荐、保险理赔或个案安全建议。
- 不收集住址、精确位置、行程轨迹、照片元数据、车牌、邻居身份、残障证明、事故记录、投诉记录、保险文件或法律材料。
- 不替代 911/应急服务、地方 311/公共工程、交通部门、无障碍协调员、树木管理部门、雨洪管理机构、执法、医疗、保险或法律渠道。
- 每个域必须保留 `public-space condition -> service request/maintenance state -> access/safety/restoration burden -> continuity outcome` 的链路。

## Consequences

- 根 README、docs 路由、domain map、domain atlas、radar、伦理边界和应用文献表都需要同步新增入口。
- `tools/check_repository.py` 必须把 6 个目录、README、AGENTS 和本 ADR 纳入结构门禁。
- 这批域与 `walking-bicycling-micromobility-continuity`、`public-accommodation-accessibility-service-continuity`、`public-works-civil-infrastructure-asset-management`、`green-blue-infrastructure-urban-nature-cooling`、`water-wastewater-utility-service-continuity` 和 `municipal/311` 类服务请求系统保持上下游关系，但不合并。
