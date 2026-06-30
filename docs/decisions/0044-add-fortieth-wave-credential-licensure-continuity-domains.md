# 0044 Add Fortieth Wave Credential Licensure Continuity Domains

Status: Accepted

Date: 2026-06-30

## Context

Human Infra 已经覆盖教育可及、劳动力服务、算法招聘、背景筛查、数字身份和标准计量，但仍缺少一组专门处理“主体如何持续证明自己学过、会做、被授权、仍合规并能跨系统携带证明”的研究域。

这些对象不能只放进教育、就业、身份或标准域：教育记录、职业执照、技能凭证、继续教育、学徒制和可验证凭证钱包各自有独立记录系统、签发机构、核验机制、失效模式、隐私边界、可携带性问题和禁止用途。

## Decision

新增第 40 波 6 个正式研究域：

- `education-record-transcript-verification-continuity/`
- `professional-licensure-certification-continuity/`
- `skills-competency-credentialing-continuity/`
- `continuing-education-recertification-continuity/`
- `apprenticeship-work-based-learning-continuity/`
- `verifiable-credential-wallet-interoperability/`

同步更新根目录 README、AGENTS、`domains/` 索引、`docs/reference/` 地图、radar、atlas、应用文献、安全边界和 `tools/check_repository.py`。

## Boundary

这些域只做教育记录、职业执照、技能/胜任力凭证、继续教育、学徒制和可验证凭证钱包的公开资料、机制、证据、互操作、隐私、纠错、可携带性和禁止用途整理，不提供升学、求职、考试、执照申请、续证、职业合规、培训选择、学历认证、法律、移民、金融、KYC、个人申请、证书购买、伪造、作弊或规避核验建议。

## Consequences

Human Infra 的“主体持续性”从系统准入判定进一步扩展到资格证明层：主体能否把学习、训练、经验和授权持续转化为行动能力，取决于可访问、可核验、可纠错、可携带、可撤销且不滥用的凭证基础设施。
