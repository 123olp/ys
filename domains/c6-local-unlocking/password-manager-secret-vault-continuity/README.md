# Password Manager Secret Vault Continuity

`password-manager-secret-vault-continuity` 研究密码管理器、密钥库、恢复密钥、紧急访问、共享保险库和机密资料迁移如何影响主体长期账号访问、代理协作和数字遗产连续。

> 核心问题：密码库把分散账号变成可管理资产，也把主密码、恢复密钥和继承机制变成新的单点故障。

## 关注对象

- Password manager、secret vault、master password、recovery key、emergency access、shared vault 和 enterprise vault。
- 密码生成、自动填充、重复密码检测、泄露监测、passkey 支持、导入导出和备份。
- 主密码遗忘、设备损坏、供应商停服、同步失败、家庭/团队共享、离职交接、失能/死亡和数字遗产。
- 单点故障、供应商锁定、加密边界、代理权限、恢复路径和数据可携带。

## Human Infra 链路

```text
密码管理器与密钥库连续
  -> 分散账号凭证、恢复资料和共享机密被集中治理
  -> 凭证丢失、弱密码复用、交接失败和失能后不可访问风险下降
  -> 主体及授权代理保持关键系统访问和迁移能力
  -> 数字资源控制、协作连续和长期恢复能力增强
```

## 非目标

- 不提供个人密码恢复、破解、密钥导出、保险库迁移、紧急访问启用、共享策略、取证或账号接管建议。
- 不替代密码管理器服务商、组织 IT、安全团队、律师、遗产规划专业人士或官方支持渠道。
- 不收集或处理主密码、恢复密钥、导出文件、保险库内容、密钥材料、共享链接、账号清单或紧急访问资料。

## Source Signals

- CISA password manager and secure account guidance: https://www.cisa.gov/secure-our-world
- NIST Digital Identity Guidelines and memorized secret guidance: https://pages.nist.gov/800-63-4/
- FTC password and account security consumer guidance: https://consumer.ftc.gov/
- Major password manager public security and emergency access documentation as implementation examples.

## 下一步

- 建立 `secret vault -> recovery key -> emergency access -> account portfolio continuity` 变量表。
- 区分个人、家庭、团队和企业密码库的所有权与代理边界。
- 与 `mfa-passkey-credential-recovery-continuity`、`digital-legacy-data-succession`、`financial-fiduciary-power-of-attorney-continuity` 和 `cloud-backup-file-sync-data-portability-continuity` 建立边界。
