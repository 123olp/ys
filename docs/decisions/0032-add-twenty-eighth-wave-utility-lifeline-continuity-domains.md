# 0032. Add Twenty-Eighth-Wave Utility Lifeline Continuity Domains

Date: 2026-06-30

## Status

Accepted.

## Context

Human Infra 已经覆盖海岸、渔业、防洪、公共工程、城市规划和绿蓝基础设施。但主体持续性还缺少一组更直接的“公用事业生命线”域：电网必须可靠，水务和污水系统必须持续，燃料与热能服务必须保障取暖制冷，公共交通必须运营而不只是道路存在，关键基础设施之间的互依赖必须可识别，公用事业服务必须在账单压力下仍能真实到达主体。

这些方向不能只归入 `energy-access-resilience/`、`water-sanitation-hygiene-continuity/`、`transportation-access-mobility/`、`telecommunications-network-resilience-continuity/`、`risk-engineering/` 或 `social-protection-benefits-delivery/`。它们各自拥有独立机制、证据体系、失败模式和安全边界。

## Decision

Add six formal domains:

- `domains/electric-grid-reliability-resilience-continuity/`
- `domains/water-wastewater-utility-service-continuity/`
- `domains/fuel-thermal-energy-service-continuity/`
- `domains/public-transit-service-operations-continuity/`
- `domains/critical-infrastructure-lifeline-interdependency-resilience/`
- `domains/utility-affordability-shutoff-protection-continuity/`

Update root navigation, docs navigation, reference maps, radar, ethics boundaries, changelog and repository checks so the new domains are discoverable and validated.

## Consequences

- Electric grid reliability, water/wastewater utilities, fuel and thermal energy services, public transit operations, lifeline interdependencies and utility affordability become first-class Human Infra layers.
- Human Infra can now describe how infrastructure service continuity differs from mere infrastructure existence: a grid, water plant, bus fleet or utility program has value only when it keeps reaching people under stress.
- Safety boundaries must explicitly prohibit operational guidance, sensitive facility details, attack/avoidance methods, engineering instructions, fare evasion, utility meter bypass, shutoff manipulation and individual legal/benefit/consumer advice.
- Future evidence work can organize source cards around DOE, NERC, EIA, EPA, FTA, FEMA, CISA, ACF, FCC, IEA and local utility/regulatory sources.

## Non-Goals

- No electric grid, water/wastewater, fuel, thermal, transit or critical infrastructure operating instructions.
- No sensitive facility lists, control-system details, attack paths, bypass methods, sabotage, theft, fare evasion, meter tampering or shutoff manipulation.
- No engineering design, construction, repair, maintenance, procurement, trading, real-time outage routing or emergency command.
- No individual utility bill, benefit eligibility, legal, debt, credit, consumer dispute, service restoration or program-application advice.
- No claim that utility lifeline resilience alone is sufficient for effective immortality; it is an upstream boundary condition.
