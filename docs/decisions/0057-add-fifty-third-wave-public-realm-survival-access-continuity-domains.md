# 0057 Add Fifty Third Wave Public Realm Survival Access Continuity Domains

Date: 2026-06-30

Status: Accepted

## Context

Human Infra 已经覆盖家庭物理运行、个人移动执行、数字账户、公共服务、住房、交通、水务、能源、无障碍和应急响应等域。但主体离开私人住所和车辆后，仍依赖一组公共空间中的低门槛接入设施：如厕、饮水、休息遮阴、灾害避难、公共网络、公共学习空间、绿地恢复和公共场所无障碍服务。

如果这些接口断裂，主体并不是单纯“不方便”，而是会出现行动半径缩小、离家停留时间下降、热暴露增加、脱水、感染、失联、服务申请失败、公共生活排除和灾害恢复失败。因此需要把公共空间生存接入从泛化的城市宜居或交通可达中拆出，作为独立研究域治理。

## Decision

新增第 53 波 8 个公共空间生存接入连续性研究域：

- `domains/c4-conversion-channel/public-restroom-sanitation-hygiene-access-continuity/`
- `domains/c4-conversion-channel/public-drinking-water-hydration-access-continuity/`
- `domains/c4-conversion-channel/public-seating-shade-rest-cooling-access-continuity/`
- `domains/c5-ecological-substrate/community-resilience-hub-shelter-center-continuity/`
- `domains/c4-conversion-channel/public-library-community-anchor-access-continuity/`
- `domains/c6-local-unlocking/parks-recreation-green-space-access-continuity/`
- `domains/c4-conversion-channel/public-wifi-device-charging-connectivity-continuity/`
- `domains/c4-conversion-channel/public-accommodation-accessibility-service-continuity/`

这些域分别承载公共厕所卫生、公共饮水补水、公共座椅遮阴休息降温、社区韧性/避难中心、公共图书馆社区锚点、公园娱乐绿地、公共 Wi-Fi/设备充电连接和公共场所无障碍服务连续性。

## Boundary

这些域不能简单并入 `housing-built-environment-stability`、`transportation-access-mobility`、`water-sanitation-hygiene-continuity`、`energy-access-resilience`、`digital-inclusion-connectivity`、`public-service-design-accessibility`、`emergency-alerts-communications` 或 `green-blue-infrastructure-urban-nature-cooling`，因为它们关注的是公共空间中主体离家后的实际可停留、可恢复、可通信、可补水、可如厕、可避难和可进入服务的接口。

禁止用途包括：

- 厕所定位跟踪、偷拍骚扰、设施破坏、非法进入或规避公共空间管理。
- 供水系统篡改、污染制造、设施盗水或敏感基础设施细节。
- 露宿/避难资格规避、物资骗领、中心实时拥挤追踪或个案救援指挥。
- 公共 Wi-Fi 攻击、认证绕过、蹭网滥用、设备盗充、公共电脑规避或账号盗用。
- ADA 诉讼策略、服务动物欺诈、伪造残障文件、个案法律建议或骚扰机构。
- 公园违规进入、设施破坏、儿童/弱势群体跟踪、野外风险操作或执法规避。

## Source Signals

优先使用 CDC WASH/handwashing、EPA/CDC drinking water、CDC heat health、EPA heat islands、FEMA Community Lifelines、Ready.gov、CISA critical infrastructure、IMLS public libraries、FCC E-Rate/emergency communications、CDC parks/physical activity、EPA green infrastructure、ADA.gov Title II/III/service animals/effective communication，以及地方公共卫生、图书馆、公园、交通、应急管理和无障碍公开资料。

## Consequences

- `domains/` 增加 8 个新子域，每个子域必须有独立 `README.md` 与 `AGENTS.md`。
- 根 `README.md`、根 `AGENTS.md`、`docs/`、`domains/`、reference 索引和 `tools/check_repository.py` 必须同步补齐。
- 后续研究应把这些域建模为公共空间任务连续性接口，而不是个体设施推荐、城市营销、旅行指南、执法规避或法律/医疗个案服务。
