# 0031. Add Twenty-Seventh-Wave Coastal Civil And Urban Infrastructure Domains

Date: 2026-06-30

## Status

Accepted.

## Context

Human Infra 已经覆盖自然系统、农业、土壤、水文、生态服务、野火和物流冷链。但主体持续性还依赖另一组“自然系统与城市/工程资产交界”的基础条件：海岸和海洋系统必须可居住可治理，水生食物系统必须持续产出，防洪工程不能把低概率风险放大成灾难，公共工程资产必须被维护，城市空间结构不能持续制造时间损耗和暴露，城市绿蓝基础设施必须承担降温、雨洪和恢复服务。

这些方向不能只归入 `water-resources-hydrology-flood-drought-management/`、`biodiversity-ecosystem-services-resilience/`、`freight-logistics-port-cold-chain-continuity/`、`transportation-access-mobility/`、`housing-built-environment-stability/` 或 `planetary-health-environment/`。它们各自拥有独立机制、证据体系、失败模式和治理边界。

## Decision

Add six formal domains:

- `domains/c5-ecological-substrate/coastal-marine-resilience-blue-economy-continuity/`
- `domains/c5-ecological-substrate/fisheries-aquatic-food-systems-continuity/`
- `domains/c5-ecological-substrate/dams-levees-flood-control-infrastructure-safety/`
- `domains/c4-conversion-channel/public-works-civil-infrastructure-asset-management/`
- `domains/c5-ecological-substrate/urban-planning-land-use-zoning-resilience/`
- `domains/c5-ecological-substrate/green-blue-infrastructure-urban-nature-cooling/`

Update root navigation, docs navigation, reference maps, radar, ethics boundaries, changelog and repository checks so the new domains are discoverable and validated.

## Consequences

- Coastal/marine systems, aquatic foods, flood-control assets, civil infrastructure asset management, land-use planning and green-blue urban infrastructure become first-class Human Infra layers.
- Human Infra can now describe how coasts, oceans, fisheries, dams, levees, public works, zoning and urban nature shape lifetime risk, effective time, recovery, nutrition and future option value.
- Safety boundaries must explicitly prohibit real-time disaster action, vessel/port operations, engineering design/operation, sensitive infrastructure details, illegal fishing/logistics evasion, property speculation and project-level legal or investment advice.
- Future evidence work can organize source cards around NOAA, FAO, FEMA, USACE, FHWA, World Bank, UN-Habitat, OECD, EPA, WHO and UNEP sources.

## Non-Goals

- No real-time coastal, storm-surge, flood, dam, levee, evacuation, vessel, port, drainage or disaster response instructions.
- No engineering design, inspection, repair, operations, procurement, permitting, zoning, land-use appeal, construction or maintenance advice.
- No illegal fishing, quota evasion, customs evasion, sanctions evasion, smuggling, infrastructure sabotage or sensitive-facility exploitation guidance.
- No coastal real estate, blue economy, fisheries, infrastructure, urban development, carbon credit, insurance, legal or investment conclusions.
- No claim that infrastructure resilience alone is sufficient for effective immortality; it is an upstream boundary condition.
