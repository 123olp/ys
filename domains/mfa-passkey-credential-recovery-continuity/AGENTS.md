# mfa-passkey-credential-recovery-continuity 目录说明

本目录承载 MFA、passkey、硬件密钥和凭证恢复连续性研究域，关注强认证如何同时影响安全与可恢复登录。

## 目录结构

```text
mfa-passkey-credential-recovery-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义 MFA、passkey、硬件密钥、恢复码、设备绑定和凭证生命周期如何进入 Human Infra 主体持续性模型。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料优先回到 NIST SP 800-63、CISA、FIDO Alliance、平台公开恢复文档和组织身份治理资料。
- 不写 MFA 绕过、账号破解、恢复码找回、passkey 导出、设备取证、钓鱼或个案解锁建议。
- 涉及凭证安全时只讨论变量、权衡和治理边界，不处理密钥、恢复码、验证码、密码、安全问题或登录记录。
- 新增指标必须注明口径：认证强度、恢复可行性、抗钓鱼能力、设备依赖、代理访问或锁定风险。
