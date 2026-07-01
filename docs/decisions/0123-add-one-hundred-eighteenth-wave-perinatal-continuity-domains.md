# 0123. Add One-Hundred-Eighteenth Wave Perinatal Continuity Domains

## Status

Accepted.

## Context

Human Infra 已有 `maternal-newborn-child-development/` 和 `obstetric-emergency-hemorrhage-hypertension-continuity/`，但围产期日常连续性仍被压在上位母婴域中。产前接入、产后随访、哺乳支持、NICU 出院、妊娠丧失和围产期心理健康各自有独立资料源、服务接口、风险窗口、隐私边界和禁止用途，不能只作为母婴健康的描述性段落。

## Decision

新增第 118 波围产期连续性研究域：

- `prenatal-care-access-risk-screening-continuity/`
- `postpartum-care-recovery-follow-up-continuity/`
- `lactation-breastfeeding-support-continuity/`
- `preterm-birth-nicu-discharge-transition-continuity/`
- `pregnancy-loss-stillbirth-bereavement-continuity/`
- `perinatal-mental-health-screening-referral-continuity/`

这些域只整理公开资料、机制、变量、证据边界和禁止用途，不提供个体怀孕、产后、哺乳、新生儿、妊娠丧失、心理危机、法律、工作学校或保险建议。

## Consequences

- `maternal-newborn-child-development/` 保持上位早期生命与发展入口。
- 围产期执行断点被拆成可独立维护的资料域和安全边界。
- 后续若继续拆分剖宫产、产科麻醉、母婴转运、home visiting 或孕产照护荒漠，应先检查是否属于本波六域的下级资料，而不是直接新增同义目录。

## Verification

- 每个新域必须有 `README.md` 和 `AGENTS.md`。
- 根 `README.md`、根 `AGENTS.md`、`domains/README.md`、`domains/AGENTS.md`、`docs/README.md`、`docs/reference/domain-map.md`、`docs/reference/research-domain-atlas.md`、`docs/reference/research-domain-radar.md`、`docs/reference/applications-and-literature.md`、`docs/reference/ethics-and-safety-boundaries.md` 和 `tools/check_repository.py` 必须同步更新。
