# Email Account Recovery Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/email-account-recovery-continuity` |
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

`email-account-recovery-continuity` 研究邮箱账号、恢复邮箱、通知入口、密码重置、身份验证、账号接管和通信记录如何影响主体能否继续接入医疗、金融、教育、工作、政府和社交系统。

> 核心问题：邮箱不是普通通信工具，而是大多数数字身份、账单通知、密码重置、资料导出和服务恢复的上游入口。

## 关注对象

- Primary email、recovery email、alias、mail forwarding、MX/DNS 配置、过滤规则、垃圾邮件误判和账号停用。
- Password reset、account recovery、suspicious login notification、session management、OAuth consent 和第三方登录绑定。
- 邮件归档、账单/医疗/学校/政府通知、工作交接、法律通知、收据和长期检索。
- 账号接管、恢复失败、邮箱提供商停权、域名邮箱过期、恢复资料陈旧和隐私泄露。

## Human Infra 链路

```text
邮箱账号恢复连续
  -> 数字服务通知、密码重置和身份验证入口保持可达
  -> 医疗、金融、教育、工作、政府和社交账户恢复成本下降
  -> 关键服务断联、资料丢失和身份接管风险下降
  -> 主体数字行动能力、资源控制和未来选择权增强
```

## 非目标

- 不提供个人邮箱找回、黑客入侵处置、取证、绕过验证、社工、账号接管或平台申诉建议。
- 不替代邮箱服务商、组织 IT、身份验证团队、执法、律师、FTC IdentityTheft.gov 或官方账号恢复渠道。
- 不收集或处理邮箱地址、密码、验证码、恢复码、邮件内容、登录记录、联系人、设备指纹或账号安全事件细节。

## Source Signals

- FTC hacked email and account recovery guidance: https://consumer.ftc.gov/
- CISA Secure Our World account security resources: https://www.cisa.gov/secure-our-world
- NIST Digital Identity Guidelines: https://pages.nist.gov/800-63-4/
- Google, Microsoft, Apple and major provider public account recovery documentation as implementation examples.

## 下一步

- 建立 `email account -> recovery channel -> service reset -> notification -> continuity` 变量表。
- 区分个人邮箱、工作邮箱、学校邮箱、域名邮箱和恢复邮箱的所有权边界。
- 与 `digital-identity-security`、`platform-account-suspension-appeals-continuity`、`cloud-backup-file-sync-data-portability-continuity` 和 `domain-dns-web-presence-continuity` 建立边界。
