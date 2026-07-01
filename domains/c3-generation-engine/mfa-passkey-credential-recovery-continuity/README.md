# MFA Passkey Credential Recovery Continuity

`mfa-passkey-credential-recovery-continuity` 研究 MFA、passkeys、hardware security keys、恢复码、设备绑定、凭证生命周期和身份验证恢复如何影响主体能否继续安全登录关键系统。

> 核心问题：强认证提高安全性，但如果恢复链路设计失败，也会把主体锁在医疗、金融、工作、教育和政府服务之外。

## 关注对象

- MFA methods、passkeys、FIDO security keys、authenticator apps、backup codes、trusted devices 和 recovery contacts。
- Enrollment、binding、rotation、revocation、lost device recovery、account recovery proofing 和 step-up authentication。
- 凭证丢失、设备损坏、恢复码遗失、同步失败、失能/死亡、组织离职和跨设备迁移。
- 安全性、可恢复性、抗钓鱼能力、可访问性、代理访问和隐私边界。

## Human Infra 链路

```text
MFA/passkey 凭证恢复连续
  -> 强认证、设备绑定和恢复码形成可恢复登录链路
  -> 钓鱼、账号接管和不可恢复锁定风险同时下降
  -> 关键系统登录、授权、代理和迁移能力保持稳定
  -> 主体数字行动能力、安全性和未来选择权增强
```

## 非目标

- 不提供个人 MFA 绕过、账号解锁、passkey 迁移、恢复码找回、设备取证、破解、钓鱼或账号接管建议。
- 不替代平台账号恢复、组织 IT、身份验证服务商、安全团队、律师或官方支持渠道。
- 不收集或处理密码、passkey、私钥、恢复码、验证码、安全问题、设备密钥、硬件密钥序列号或登录记录。

## Source Signals

- NIST SP 800-63B / 800-63B-4 authentication guidance: https://pages.nist.gov/800-63-4/
- CISA MFA and phishing-resistant authentication resources: https://www.cisa.gov/secure-our-world
- FIDO Alliance passkeys and security key materials: https://fidoalliance.org/
- Platform public passkey and account recovery documentation as implementation examples.

## 下一步

- 建立 `credential -> authenticator -> recovery proof -> login continuity` 变量表。
- 区分安全增强、可恢复性、可访问性和代理访问之间的权衡。
- 与 `email-account-recovery-continuity`、`phone-number-sim-portability-account-security-continuity`、`password-manager-secret-vault-continuity` 和 `digital-identity-security` 建立边界。
