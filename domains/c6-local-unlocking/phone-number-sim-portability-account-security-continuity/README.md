# Phone Number SIM Portability Account Security Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/phone-number-sim-portability-account-security-continuity` |
| 分级 | `C6` - 局部可能性解锁层 |
| 控制轴 | 局部阻塞解除 |
| 分级理由 | 未命中更高层边界、载体、能力、转换或生态规则，暂归为具体场景的局部可能性解锁。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域解除的是哪一个具体疾病、流程、服务、职业、家庭、社区或专项风险中的局部阻塞？

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

<!-- domain-research-skeleton:start -->
## 研究推进骨架

### 最小问题集

- 界定局部阻塞：某一疾病、流程、服务、职业、家庭、社区或专项风险中的具体失败点。
- 说明受影响任务：它阻碍了主体完成什么行动、服务、照护、转换或恢复过程。
- 记录可测改善：等待时间、错误率、成本、可及性、完成率、伤害率或恢复速度。
- 明确升级边界：何时应转交 C2-C5 的上层生命、能力、转化或基础设施域。
- 避免把局部改良包装成根本性解决方案，必须标注适用范围和外部依赖。

### 变量接口

- 输入变量：本域直接处理的对象、资源、技术、环境、制度或状态。
- 中间机制：变量通过什么因果路径改变主体状态、系统状态或外部条件。
- 状态改变：身体、认知、能力、资源、风险暴露、可及性、时间成本或协作条件如何变化。
- 风险 / 成本函数：死亡风险、失能风险、工程风险、尾部风险、机会成本、维护成本或治理成本如何变化。
- 输出指标：有效寿命、健康寿命、有效时间、主观时间、相对时间、行动能力、恢复能力或未来选择权。

### 证据入口

- 官方 / 原始资料：监管文件、数据库、临床登记、标准、论文原文、项目白皮书或一手报告。
- 综述 / 指南 / 标准：系统综述、领域指南、技术标准、伦理规范和权威机构材料。
- 数据集 / 登记系统：可复核的数据表、代码、实验记录、登记号、版本和采集边界。
- 反例 / 失败案例：负结果、副作用、安全事故、不可复现结果、伦理争议和误用案例。

### 最小产出

- Source Signals：记录候选资料、来源、日期、主张和待核验点。
- Source Cards：提取 claim、变量、机制、证据类型、边界、反证条件和可迁移位置。
- Claim-Evidence Matrix：把每个稳定主张绑定到来源、证据等级、适用范围和不确定性。
- 变量表：列出输入变量、中间变量、状态变量、风险变量、输出指标和可观测代理指标。
- 上下游关系：说明本域依赖哪些更根本域，并向哪些转化、应用或基础设施域输出。
<!-- domain-research-skeleton:end -->

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
