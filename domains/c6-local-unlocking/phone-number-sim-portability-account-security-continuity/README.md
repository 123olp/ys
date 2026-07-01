# Phone Number SIM Portability Account Security Continuity

`phone-number-sim-portability-account-security-continuity` 研究手机号、SIM/eSIM、号码携转、短信验证、语音验证、运营商账号和 port-out / SIM swap 风险如何影响主体通信可达、账号恢复和服务接入。

> 核心问题：手机号已变成金融、医疗、工作、政府和平台账号的事实恢复通道；号码丢失或被转出会连带破坏多个系统。

## 关注对象

- Phone number ownership、carrier account、SIM/eSIM provisioning、number portability、port-out lock、account PIN 和 device binding。
- SMS/voice OTP、emergency contact、service notification、two-step recovery 和身份校验。
- SIM swap、port-out fraud、号码回收、号码更换、漫游、欠费停机、运营商资料错误和死亡/失能后号码继承。
- 与邮箱、MFA、银行、医疗门户、雇主系统和政府服务的恢复链路。

## Human Infra 链路

```text
手机号与 SIM/携转安全连续
  -> 通信可达、短信验证和账号恢复通道保持稳定
  -> SIM swap、port-out、号码回收和停机导致的连锁账号失控风险下降
  -> 金融、医疗、工作、教育、政府和社交服务恢复能力增强
  -> 主体资源控制、身份安全和行动连续性增强
```

## 非目标

- 不提供个人号码找回、SIM swap 处置、携号转网策略、运营商投诉、追踪定位、短信拦截、验证码转发或账号恢复建议。
- 不替代运营商、FCC、FTC、组织 IT、安全团队、执法、律师或官方账号恢复渠道。
- 不收集或处理电话号码、SIM/eSIM 资料、验证码、运营商 PIN、账单、设备 IMEI/ICCID、定位或通信记录。

## Source Signals

- FCC SIM swap and port-out fraud materials: https://www.fcc.gov/
- FCC wireless local number portability resources: https://www.fcc.gov/
- FTC identity theft and phone account fraud guidance: https://consumer.ftc.gov/
- CISA account security and MFA guidance: https://www.cisa.gov/secure-our-world

## 下一步

- 建立 `phone number -> carrier control -> OTP/recovery -> account access -> continuity` 变量表。
- 区分手机号作为通信地址、验证因子、恢复通道和身份资料的不同模型位置。
- 与 `mfa-passkey-credential-recovery-continuity`、`email-account-recovery-continuity`、`banking-deposit-account-access-continuity` 和 `digital-identity-security` 建立边界。
