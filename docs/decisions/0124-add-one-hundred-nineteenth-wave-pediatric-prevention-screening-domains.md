# 0124 Add One Hundred Nineteenth Wave Pediatric Prevention Screening Domains

## Status

Accepted.

## Context

第 118 波已经补齐围产期连续性，但从出生后公共卫生筛查到儿童预防照护、免疫记录、发育行为筛查、环境铅风险和复杂儿童照护协调之间仍存在独立断点。这些断点不能只放进 `maternal-newborn-child-development`、`immunization-public-health-surveillance`、`early-intervention-idea-part-c-developmental-services-continuity`、`lead-heavy-metal-exposure-control` 或学校健康域，因为它们发生在儿科预防入口和家庭-公共卫生-学校-保险交接处。

## Decision

新增第 119 波儿科预防与早期筛查连续性研究域：

- `newborn-screening-result-followup-continuity/`
- `well-child-visit-preventive-care-continuity/`
- `childhood-immunization-schedule-record-continuity/`
- `developmental-behavioral-screening-referral-continuity/`
- `pediatric-lead-screening-environmental-followup-continuity/`
- `children-youth-special-health-care-needs-care-coordination-continuity/`

每个域只建立 `README.md` 和 `AGENTS.md`，不创建空数据、脚本或自动化目录。

## Consequences

- Human Infra 能把出生后早期可逆风险、预防照护入口、公共卫生记录、发育支持、环境暴露和复杂儿童照护协调作为独立基础设施层管理。
- 所有域必须保留儿童、家庭、遗传、疫苗、筛查结果、学校、保险和残障数据的高敏感边界。
- 这些域不提供个体儿科、疫苗、筛查、发育、铅暴露、教育、保险、福利、法律或紧急建议。

## Verification

- `tools/check_repository.py` 必须检查 6 个新域的 `README.md` 和 `AGENTS.md`。
- 根 `README.md`、根 `AGENTS.md`、`domains/README.md`、`domains/AGENTS.md`、`docs/README.md`、`docs/AGENTS.md`、`docs/reference/domain-map.md`、`docs/reference/research-domain-atlas.md`、`docs/reference/research-domain-radar.md`、`docs/reference/applications-and-literature.md` 和 `docs/reference/ethics-and-safety-boundaries.md` 必须包含第 119 波入口或边界说明。
