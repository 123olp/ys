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
