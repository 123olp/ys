# 0120. Add One-Hundred-Fifteenth Wave Long-Term Care Execution Domains

Date: 2026-07-01

## Status

Accepted

## Context

`caregiving-long-term-care/` 已经把家庭照护、长期照护、居家社区支持、照护协调、照护者负担和尊严边界纳入 Human Infra。`family-caregiver-respite-work-continuity/` 进一步把家庭照护者支持、respite care、照护培训、工作灵活性和照护者负担放进工作与收入连续性框架。

但长期照护真正失效时，通常不是因为“长期照护”这个概念缺失，而是执行层断裂：白天无人监督、没有交通交接、居家照护人员短缺、respite 有名无量、照护者没有训练、照护者自身已经 burnout、家庭任务清单和 care plan 无法交接。继续只保留上位域会把服务接口、劳动力条件、排班瓶颈、技能风险、照护者健康和家庭任务协调混成一个大桶，无法判断每个机制如何影响主体持续性。

## Decision

新增第 115 波 6 个长期照护执行连续性研究域：

- `adult-day-services-supervision-transport-continuity/`
- `home-care-aide-personal-care-workforce-continuity/`
- `respite-care-provider-capacity-scheduling-continuity/`
- `caregiver-training-skills-safety-continuity/`
- `caregiver-health-burnout-screening-support-continuity/`
- `home-care-task-coordination-care-plan-continuity/`

这些域共同把“长期照护能不能持续执行”拆成可审查链路：成人日间服务与交通监督、居家 personal care 劳动力、喘息服务供给与排班、照护者训练与安全技能、照护者健康与 burnout 支持、家庭照护任务与 care plan 协调。

## Consequences

- `caregiving-long-term-care/` 继续保留上位理论与尊严边界，不承载全部执行层细节。
- `family-caregiver-respite-work-continuity/` 继续关注照护责任如何影响岗位、收入和工作角色；新增域则下钻到长期照护的每日执行条件。
- 资料使用必须回到 ACL NFCSP、ACL Lifespan Respite、Eldercare Locator、Medicaid HCBS / LTSS、NIA caregiving / long-term care、CMS home health、AHRQ care coordination 等公开来源。
- 禁止把这些域转化为成人日间服务推荐、居家照护雇佣、护理操作、排班安排、心理诊断、危机干预、福利资格判断、家庭照护计划制定、法律、保险或个案建议。

## Verification

- 每个新增域必须包含 `README.md` 和 `AGENTS.md`。
- 根 `README.md`、根 `AGENTS.md`、`domains/README.md`、`domains/AGENTS.md`、`docs/README.md`、`docs/AGENTS.md`、`docs/reference/domain-map.md`、`docs/reference/research-domain-atlas.md`、`docs/reference/research-domain-radar.md`、`docs/reference/applications-and-literature.md` 和 `docs/reference/ethics-and-safety-boundaries.md` 必须同步索引。
- `tools/check_repository.py` 必须登记新增目录、README/AGENTS 和本 ADR。
