# 0015 Add Eleventh Wave Civic Safety Continuity Domains

## Status

Accepted

## Context

Human Infra 已经把主体持续性从身体、认知、资源、服务、生计和风险分摊扩展到多个独立域。第十波之后仍有一组必要条件没有独立承载：权利救济、公共决策参与、迁移和流离失所后的人道服务连续性、数字连接可达、人身安全和产品缺陷召回。

这些对象不能继续只放在 `governance-rights/`、`resource-social-infra/`、`risk-engineering/` 或 `supply-chain-continuity/` 中，因为它们各自有独立机制、证据体系、失败模式和伦理边界。

## Decision

新增第十一波 6 个研究域：

- `access-to-justice-legal-aid/`
- `civic-participation-election-access/`
- `migration-displacement-humanitarian-continuity/`
- `digital-inclusion-connectivity/`
- `personal-safety-violence-prevention/`
- `product-safety-recall-systems/`

每个域本轮只建立 `README.md` 和 `AGENTS.md`，作为研究域骨架，不创建数据目录、采集脚本或产品实现。

## Rationale

- 司法可及与法律援助决定主体是否能把名义权利转成真实救济。
- 公民参与与选举接入决定主体是否能参与会分配资源、风险和权利的公共规则生成。
- 迁移、流离失所与人道连续性决定主体跨地点、跨制度后是否仍能获得身份、医疗、教育、庇护和保护。
- 数字包容与连接决定数字化社会中的医疗、福利、教育、工作和公共服务入口是否可达。
- 人身安全与暴力预防决定主体是否被暴力、胁迫、犯罪伤害和创伤长期截断。
- 产品安全与召回系统决定外部产品缺陷能否被报告、发现、召回和纠正，避免工具系统反向伤害主体。

## Consequences

- `README.md`、根 `AGENTS.md`、`domains/README.md`、`domains/AGENTS.md`、`docs/reference/domain-map.md`、`docs/reference/research-domain-atlas.md`、`docs/reference/research-domain-radar.md` 和 `docs/reference/ethics-and-safety-boundaries.md` 必须同步更新。
- `tools/check_repository.py` 必须把新域 README / AGENTS 和目录列入结构检查。
- 新域只能整理公开资料、变量、边界和 Source Cards，不提供法律、选举、移民、暴力处置、数字绕过、产品维修、医疗或个体申请建议。

## Validation

- `python3 tools/check_repository.py`
- `make check`
