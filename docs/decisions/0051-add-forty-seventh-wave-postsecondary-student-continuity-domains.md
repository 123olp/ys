# 0051 Add Forty-Seventh Wave Postsecondary Student Continuity Domains

## Status

Accepted.

## Context

Human Infra 已有教育可及、教育记录、职业证照、技能凭证、继续教育、学徒制和 K-12 学校服务域，但高等教育学生生命周期仍缺少独立层：学生被录取以后，是否能完成注册、转换学分、获得资助、持续满足学业进度、接入基本需求支持、获得残障便利、度过心理危机、在校园安全与 Title IX/Clery 框架内得到保护，以及国际学生能否维持 SEVIS 身份。

这些问题不能只归入 `education-access-lifelong-learning` 或 `education-record-transcript-verification-continuity`。高等教育是学籍、资金、课程路径、校园服务、民权、公共安全、移民身份和职业入口耦合的制度基础设施；任一断裂都会把延长学习时间转化为债务、退学、身份风险、健康风险或未来选择权压缩。

## Decision

新增第四十七波 8 个高等教育学生生命周期连续性研究域：

- `postsecondary-admissions-transfer-articulation-continuity/`
- `student-financial-aid-grant-scholarship-continuity/`
- `academic-advising-degree-progress-continuity/`
- `campus-basic-needs-student-support-continuity/`
- `campus-disability-accommodations-accessibility-continuity/`
- `campus-mental-health-crisis-student-support-continuity/`
- `campus-safety-title-ix-clery-continuity/`
- `international-student-sevis-status-continuity/`

每个域先只建立 `README.md` 与 `AGENTS.md`，作为研究域骨架、证据边界和未来资料组织入口，不创建空数据、脚本、个人服务流程或政策解释器。

## Consequences

- 高等教育被建模为主体能力资本、未来职业入口和身份连续性的制度基础设施，而不是普通学习域的附属说明。
- 新域必须优先使用 Federal Student Aid、NCES/IPEDS、College Scorecard、ED OCR、Campus Safety and Security、Clery、ADA/Section 504、SAMHSA、CDC、ICE SEVP/SEVIS、Study in the States、USCIS、Department of State、州高教机构和高校公开资料。
- 新域不得提供个人申请、转学、资助、选课、住宿、残障便利、心理危机、Title IX、校园安全、SEVIS、移民、税务、医疗、法律或个案建议。
- 新域不得收集或处理学生个人教育记录、财务资料、残障资料、心理健康资料、伤害事件资料、移民身份资料、账号、证件或家庭资料。

## Validation

- `tools/check_repository.py` 必须要求 8 个新目录及其 README / AGENTS 存在。
- 根 README、根 AGENTS、`domains/README.md`、`domains/AGENTS.md`、`docs/README.md`、`docs/AGENTS.md`、`docs/decisions/README.md`、`docs/reference/domain-map.md`、`docs/reference/research-domain-atlas.md`、`docs/reference/research-domain-radar.md`、`docs/reference/applications-and-literature.md` 和 `docs/reference/ethics-and-safety-boundaries.md` 必须同步索引。
