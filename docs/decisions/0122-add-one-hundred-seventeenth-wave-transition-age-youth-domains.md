# 0122. Add One-Hundred-Seventeenth Wave Transition-Age Youth Domains

Date: 2026-07-01

## Status

Accepted

## Context

Human Infra 已经覆盖儿童保护、寄养收养、学校服务、学生资助、校园支持、无家可归、心理危机、就业服务和家庭事实记录。但这些域还没有单独表达“青少年从依赖系统进入成年自主系统”这一高风险转变窗口。

先验追问到主体持续性时，青年期不是普通年龄段，而是身份、住所、学校、医疗、心理健康、收入、家庭关系、司法记录和照护责任同时改写的制度转接口。若这个窗口缺少独立研究域，Human Infra 会把青年失联误判为单点教育、住房、就业或医疗问题，忽视它们在成年边界同时发生的级联失败。

## Decision

新增第 117 波 6 个青少年到成年转变连续性研究域：

- `runaway-homeless-youth-outreach-shelter-continuity/`
- `foster-care-aging-out-independent-living-continuity/`
- `juvenile-justice-reentry-aftercare-continuity/`
- `transition-age-youth-mental-health-service-continuity/`
- `opportunity-youth-education-employment-pathway-continuity/`
- `pregnant-parenting-youth-family-support-continuity/`

这些域共同把离家/无家可归、寄养出离、少年司法重返、儿童到成人心理健康服务转接、教育就业断线和怀孕育儿青年支持建模为主体成年能力形成前的基础设施。

## Consequences

- `kinship-foster-adoption-care-continuity/` 继续关注儿童安置和 permanency；新增寄养出离域下钻到成年转接、独立生活和保护系统结束后的支持。
- `school-enrollment-attendance-continuity/`、`postsecondary-admissions-transfer-articulation-continuity/` 和 `workforce-employment-services/` 继续关注学校或就业系统本身；新增机会青年域关注断线青年重新进入教育就业路径的复合接口。
- `homelessness-unsheltered-health-continuity/` 继续关注住所缺失的健康连续性；新增离家/无家可归青年域关注未成年与过渡年龄青年特有的安全、家庭、隐私和发展边界。
- `suicide-crisis-response-continuity/` 和 `school-mental-health-counseling-support-continuity/` 继续关注危机和学校支持；新增过渡年龄青年心理健康域关注儿童到成人行为健康系统转接。
- 禁止把这些域转化为逃离路线、庇护所定位、个案法律、法院、缓刑/监管规避、心理危机、诊断治疗、项目申请、就业、福利、育儿、怀孕、托育、住房或家庭冲突建议，也禁止收集或推断未成年人位置、身份、风险状态或家庭信息。

## Verification

- 每个新增域必须包含 `README.md` 和 `AGENTS.md`。
- 根 `README.md`、根 `AGENTS.md`、`domains/README.md`、`domains/AGENTS.md`、`docs/README.md`、`docs/AGENTS.md`、`docs/reference/domain-map.md`、`docs/reference/research-domain-atlas.md`、`docs/reference/research-domain-radar.md`、`docs/reference/applications-and-literature.md` 和 `docs/reference/ethics-and-safety-boundaries.md` 必须同步索引。
- `tools/check_repository.py` 必须登记新增目录、README/AGENTS 和本 ADR。
