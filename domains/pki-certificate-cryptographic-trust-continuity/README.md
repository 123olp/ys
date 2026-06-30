# PKI Certificate Cryptographic Trust Continuity

`pki-certificate-cryptographic-trust-continuity` 研究 PKI、TLS 证书、证书颁发机构、密钥管理、吊销、根信任、证书透明度、加密算法迁移和到期管理如何影响主体依赖的 Web、API、软件更新和身份验证持续可信。

> 核心问题：大量数字服务的“能不能安全连接”取决于证书、密钥和根信任链；证书失效会让服务从可用变成不可达或不可信。

## 关注对象

- TLS 证书、CA、根信任、证书透明度、OCSP/CRL、密钥管理、轮换、吊销、到期和自动续期。
- Web、API、软件更新、代码签名、设备身份、邮件安全和组织身份验证中的证书依赖。
- 密钥泄露、证书过期、误签、根信任移除、算法退役、后量子迁移和加密配置错误。
- 证书生命周期监控、密钥保管、分权、审计和灾难恢复。

## Human Infra 链路

```text
PKI 与证书信任连续
  -> Web、API、软件更新和身份验证连接保持可信
  -> 证书过期、密钥泄露、误签和算法退役造成的服务中断下降
  -> 主体依赖的数字服务、资料流和协作入口更稳定
  -> 数字行动和长期数据可信性增强
```

## 非目标

- 不提供伪造证书、绕过 TLS、截获流量、滥用 CA、密钥窃取、证书钓鱼或攻击配置步骤。
- 不替代 CA、组织 PKI、密码工程、应急响应、合规审计或法律建议。
- 不收集私钥、证书请求、内部域名、证书清单、HSM 配置或未公开加密事件。

## Source Signals

- CA/Browser Forum Baseline Requirements: https://cabforum.org/
- NIST key management guidance, including SP 800-57: https://csrc.nist.gov/
- IETF TLS and PKIX standards as protocol references: https://www.ietf.org/
- CISA and vendor certificate management guidance as operational references.

## 下一步

- 建立 `key -> certificate -> trust chain -> renewal -> service continuity` 变量表。
- 区分个人网站、组织服务、软件签名、设备身份和长期数据加密的证书生命周期。
- 与 `post-quantum-cryptography-long-term-data-security`、`domain-dns-web-presence-continuity`、`software-update-vulnerability-patch-continuity` 和 `api-platform-dependency-runtime-continuity` 建立边界。
