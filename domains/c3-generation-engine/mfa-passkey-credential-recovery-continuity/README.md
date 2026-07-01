# MFA Passkey Credential Recovery Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/mfa-passkey-credential-recovery-continuity` |
| 分级 | `C3` - 可能性生成引擎层 |
| 控制轴 | 主体能力生成 |
| 分级理由 | 关键词显示该域主要增强认知、学习、工具、AI、技能或沟通能力。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何放大主体生成新路径的能力，例如认知、学习、注意力、记忆、AI、工具和反馈复利？

```text
研究域对象
  -> 影响变量 / 中间机制
  -> 改变主体状态或外部条件
  -> 改变风险、能力、时间成本或可达性
  -> 改变有效寿命、有效时间或未来选择权
```

### 使用边界

- 本域是研究与建模单元，不是个体医疗、法律、金融、工程、教育或安全操作建议。
- 新增内容必须标明来源、适用对象、证据等级和不确定性；AI 总结不能作为事实源。
- 若内容会改变分级、目录位置或上下游关系，先更新 `domains/_possibility-space-control/classification.tsv`。
<!-- domain-standard:end -->


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
