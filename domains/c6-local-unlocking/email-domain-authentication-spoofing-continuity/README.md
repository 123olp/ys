# Email Domain Authentication Spoofing Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/email-domain-authentication-spoofing-continuity` |
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

Email Domain Authentication Spoofing Continuity 关注电子邮件域名认证、SPF、DKIM、DMARC、BIMI、phishing、通知可达和 spoofing 防护如何影响主体接收可信通知与完成任务。

## 对象

- Email authentication、SPF、DKIM、DMARC、BIMI、phishing、domain spoofing、mail deliverability、quarantine 和 report handling。
- 医疗、金融、法院、学校、雇主、政府、平台、保险和公共服务通知的邮件可信度与可达性。
- 伪造发件人、邮件丢失、认证配置错误、误入垃圾箱、钓鱼链接、附件风险和域名相似攻击。

## Human Infra 价值

```text
主体大量关键任务依赖邮件通知
-> 邮件发件人可以被伪造，真实邮件也可能被拦截或丢失
-> SPF/DKIM/DMARC 等认证机制让域名身份和邮件来源可被验证
-> 主体更能区分真实通知、钓鱼尝试、平台邮件和机构沟通
-> 账号、安全、医疗、金融、法律和公共服务链路更少被伪造邮件打断
```

## 边界

- 本域不提供钓鱼邮件制作、绕过邮件认证、域名仿冒、邮件轰炸、邮箱入侵或 DMARC 规避方法。
- 不配置真实域名、邮件服务器、DNS 记录或投递系统，不判断某封邮件是否安全。
- 不提供营销投递优化、冷邮件、欺骗性 sender identity 或平台规避策略。
- 只整理公开标准、风险变量、验证边界、误判模式和禁止用途。

## 上下游

- 上游：`domain-dns-web-presence-continuity/`、`pki-certificate-cryptographic-trust-continuity/`、`email-account-recovery-continuity/`。
- 下游：`official-web-domain-brand-impersonation-continuity/`、`fraud-scams-consumer-protection/`、`notification-alert-routing-attention-continuity/`。

## Source Signals

- CISA email authentication and phishing guidance.
- NIST cybersecurity and digital identity materials.
- IETF SPF, DKIM and DMARC standards.
- FTC phishing and consumer protection materials.
