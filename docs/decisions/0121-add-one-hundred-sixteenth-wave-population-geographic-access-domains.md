# 0121. Add One-Hundred-Sixteenth Wave Population Geographic Access Domains

Date: 2026-07-01

## Status

Accepted

## Context

`rural-health-access-geographic-equity/`、`homelessness-unsheltered-health-continuity/`、`correctional-health-reentry-continuity/` 和 `disability-services-independent-living/` 已经把部分结构性脆弱与连续照护断点纳入 Human Infra。但这些域仍不足以覆盖“同一套基础设施在不同人口身份、地理位置和制度边界中如何变成不同失败模式”的问题。

先验追问到服务可达性之后，还需要继续追问：谁能被服务系统承认，谁被地理隔离，谁在制度转换中掉线，谁的身份或家庭结构不被默认接口接住，谁的健康服务跨越司法、文化、语言、边境或财政边界。若这些条件不被独立建模，Human Infra 会误以为服务只要存在就等于可用。

## Decision

新增第 116 波 6 个人口与地域可达性连续性研究域：

- `tribal-health-sovereignty-service-access-continuity/`
- `veterans-health-benefits-navigation-continuity/`
- `migrant-seasonal-farmworker-health-housing-continuity/`
- `territorial-island-health-infrastructure-access-continuity/`
- `border-community-cross-border-care-continuity/`
- `lgbtq-health-identity-affirming-service-continuity/`

这些域共同把“服务可达”从普通地理距离扩展为主权治理、军转民制度转换、季节性劳动迁移、岛屿/属地供应链、边境跨制度生活和身份承认/反歧视服务接口。

## Consequences

- `rural-health-access-geographic-equity/` 继续关注农村地点、服务密度、宽带、交通和卫生人力，不承载全部人口身份和制度边界差异。
- `migration-displacement-humanitarian-continuity/`、`immigration-status-residency-work-authorization-continuity/` 和 `asylum-refugee-protection-status-continuity/` 继续关注迁移、居留授权和保护身份；新增边境和农业工人域只处理服务连续性与工作/生活接口，不提供移民个案建议。
- `healthcare-civil-rights-nondiscrimination-continuity/` 继续保留医疗民权上位边界；新增 LGBTQ 域下钻到身份承认、肯定性服务、隐私和家庭社区支持。
- 资料使用必须回到 IHS、VA、HRSA、CDC、HHS OCR / Section 1557、Medicaid.gov、ASPR、FEMA、DOL 和公开公共卫生资料。
- 禁止把这些域转化为个体医疗、福利申请、身份判断、移民/边境、跨境就医、劳动纠纷、危机干预、法律、政治或个案建议，也禁止群体定位、身份推断、监控画像或歧视性筛选。

## Verification

- 每个新增域必须包含 `README.md` 和 `AGENTS.md`。
- 根 `README.md`、根 `AGENTS.md`、`domains/README.md`、`domains/AGENTS.md`、`docs/README.md`、`docs/AGENTS.md`、`docs/reference/domain-map.md`、`docs/reference/research-domain-atlas.md`、`docs/reference/research-domain-radar.md`、`docs/reference/applications-and-literature.md` 和 `docs/reference/ethics-and-safety-boundaries.md` 必须同步索引。
- `tools/check_repository.py` 必须登记新增目录、README/AGENTS 和本 ADR。
