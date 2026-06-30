# 0050 Add Forty-Sixth Wave School Service Continuity Domains

## Status

Accepted.

## Context

Human Infra 已有教育可及、教育记录、儿童发展、托育、儿童保护、在线安全、交通接入和医疗服务等域，但仍缺少一个关键层：学校作为儿童日常运行场所时，入学、出勤、残障支持、校餐、校医、通学、纪律、心理支持和安全气候如何共同决定学习轮次、服务入口、恢复能力和未来选择权。

这些问题不能只归入 `education-access-lifelong-learning`。教育机会成立以后，还必须回答学生是否能到校、能否持续出勤、能否获得必要便利、是否吃得上饭、健康条件是否能在学校被支持、是否安全到达学校、是否被排除性纪律切断学习日、是否有心理恢复层、是否处于可归属和可报告的安全环境。

## Decision

新增第四十六波 8 个学校服务连续性研究域：

- `school-enrollment-attendance-continuity/`
- `special-education-iep-504-accommodation-continuity/`
- `school-meals-nutrition-access-continuity/`
- `school-health-services-chronic-condition-continuity/`
- `school-transportation-safe-routes-continuity/`
- `school-discipline-exclusion-restraint-continuity/`
- `school-mental-health-counseling-support-continuity/`
- `school-climate-bullying-violence-prevention-continuity/`

每个域先只建立 `README.md` 与 `AGENTS.md`，作为研究域骨架、证据边界和未来资料组织入口，不创建空数据、脚本或个人服务流程。

## Consequences

- 学校服务层被建模为主体持续性的日常运行基础设施，而不是教育主线里的附属说明。
- 新域必须优先使用教育部门、NCES、IDEA/OSEP、OCR、USDA FNS、CDC、SAMHSA、FHWA、NHTSA、StopBullying.gov、州和地方教育机构等公开权威来源。
- 新域不得提供个人入学、出勤、IEP/504、校餐、校医、交通、纪律、心理健康、欺凌、校园安全、医疗、法律或教育个案建议。
- 新域不得收集或处理儿童个人教育记录、健康资料、纪律资料、家庭住址、移民身份、心理健康资料、路线或事件细节。

## Validation

- `tools/check_repository.py` 必须要求 8 个新目录及其 README / AGENTS 存在。
- 根 README、根 AGENTS、`domains/README.md`、`domains/AGENTS.md`、`docs/README.md`、`docs/AGENTS.md`、`docs/reference/domain-map.md`、`docs/reference/research-domain-atlas.md`、`docs/reference/research-domain-radar.md`、`docs/reference/applications-and-literature.md` 和 `docs/reference/ethics-and-safety-boundaries.md` 必须同步索引。
