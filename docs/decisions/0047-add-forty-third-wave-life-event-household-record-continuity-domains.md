# 0047 Add Forty-Third-Wave Life Event Household Record Continuity Domains

Date: 2026-06-30

## Status

Accepted

## Context

Human Infra 的先验追问继续从工作中断和照护事件下探：主体和家庭要持续接入医疗、学校、福利、税务、保险、法院、住房、金融和公共服务，必须先被制度稳定识别为“同一个人”“某个家庭关系中的人”“某个地址或辖区中的人”以及“某个照护/责任结构中的人”。

既有 `legal-identity-civil-registration/`、`social-protection-benefits-delivery/`、`child-protection-family-safety/`、`childcare-family-continuity/` 和 `access-to-justice-legal-aid/` 已经覆盖身份、福利、儿童安全、托育和法律援助的上位问题，但不足以表达生命事件记录、姓名同步、地址邮件路由、household 定义、家庭法院责任和儿童安置路径这些更细的制度断点。

## Decision

新增第四十三波 6 个正式研究域：

- `domains/c4-conversion-channel/vital-records-life-event-continuity/`
- `domains/c4-conversion-channel/name-change-identity-record-synchronization-continuity/`
- `domains/c6-local-unlocking/address-residency-mail-service-continuity/`
- `domains/c4-conversion-channel/household-composition-dependent-eligibility-continuity/`
- `domains/c6-local-unlocking/family-law-custody-child-support-continuity/`
- `domains/c6-local-unlocking/kinship-foster-adoption-care-continuity/`

这些域共同承载“家庭事实与制度记录连续性”：生命事件记录确认人和关系，姓名同步确认同一主体，地址邮件确认位置和通知路由，household/dependent 关系确认资格单位，家庭法和子女抚养确认照护责任，亲属照护/寄养/收养确认原照护失稳后的儿童连续性。

## Consequences

- `domains/` 继续按“主体持续性成立条件”扩展，而不是按单一政府部门、单一法律制度或单一福利项目组织。
- 这些域不能被写成个人证件办理、改名、地址变更、税务 household、福利资格、监护权、子女抚养、寄养、收养、移民、法律、保险、学校或家庭法院建议。
- 证据入口应优先使用 USA.gov、CDC/NCHS、SSA、State Department、USPS、IRS、HealthCare.gov、ACF Child Support、Child Welfare Information Gateway、州/地方官方机构和法院/法律援助官方资料。
- 任何涉及身份文件、家庭法院、儿童安置、福利资格或地址安全的内容都必须保留反欺诈、反胁迫、反规避、隐私和儿童安全边界。

## Validation

- 新增域必须在 `domains/README.md`、`domains/AGENTS.md`、`docs/README.md`、`docs/AGENTS.md`、`docs/reference/domain-map.md`、`docs/reference/research-domain-atlas.md`、`docs/reference/research-domain-radar.md`、`docs/reference/applications-and-literature.md`、`docs/reference/ethics-and-safety-boundaries.md` 和 `tools/check_repository.py` 中可发现。
- `python3 tools/check_repository.py`
- `make check`
