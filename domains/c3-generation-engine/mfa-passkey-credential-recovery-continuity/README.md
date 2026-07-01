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

<!-- domain-research-skeleton:start -->
## 研究推进骨架

### 最小问题集

- 界定被放大的通用能力资源：智力、注意力、记忆、学习、判断、执行、反馈或工具使用。
- 说明任务链路：能力变化如何改变问题求解、行动质量、创造密度或学习轮次。
- 识别复利结构：能力增强、工具采用、协作网络、经验积累和自我升级如何互相强化。
- 记录依赖条件：AI、数据、界面、训练、外部工具、社会支持或反馈系统。
- 列出误用、过载、依赖、幻觉、注意力破坏、人格边界和安全风险。

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
