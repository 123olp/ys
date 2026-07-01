# PKI Certificate Cryptographic Trust Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/pki-certificate-cryptographic-trust-continuity` |
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
