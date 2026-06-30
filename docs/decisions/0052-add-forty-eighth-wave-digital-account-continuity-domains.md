# 0052 Add Forty Eighth Wave Digital Account Continuity Domains

Date: 2026-06-30

## Status

Accepted

## Context

Human Infra 已覆盖数字身份安全、数据治理、数字遗产、个人档案和在线安全，但这些域仍不足以表达一个更日常的断点：主体在现实服务系统中的行动越来越依赖邮箱、手机号、MFA/passkey、密码库、云备份、联系人图谱、域名/DNS 和平台账号。它们不是抽象网络安全问题，而是医疗、金融、教育、工作、政府、创作和社会关系的登录、通知、恢复、迁移与退出入口。

## Decision

新增第 48 波 8 个数字账户与通信可达连续性域：

- `email-account-recovery-continuity/`
- `phone-number-sim-portability-account-security-continuity/`
- `mfa-passkey-credential-recovery-continuity/`
- `password-manager-secret-vault-continuity/`
- `cloud-backup-file-sync-data-portability-continuity/`
- `messaging-contact-graph-portability-continuity/`
- `domain-dns-web-presence-continuity/`
- `platform-account-suspension-appeals-continuity/`

## Boundary

这些域只研究数字接入、账号恢复、资料可携带、联系人连续、域名可达和平台申诉如何影响主体持续性，不提供个人账号恢复、绕过验证、取证、黑客操作、封禁规避、平台申诉文案、法律策略或具体安全事件处置。

## Consequences

- `README.md`、`docs/README.md`、`domains/README.md`、`docs/reference/domain-map.md`、`docs/reference/research-domain-atlas.md`、`docs/reference/research-domain-radar.md` 和 `tools/check_repository.py` 必须把这 8 个域纳入索引。
- 后续资料卡片应优先回到 NIST、CISA、FCC、FTC、ICANN、IANA、Data Transfer Initiative、DSA/OECD 和主要平台公开文档。
- 高风险账号、通信、平台和密钥内容必须保留禁止用途边界。
