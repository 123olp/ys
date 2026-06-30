# Email Domain Authentication Spoofing Continuity

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
