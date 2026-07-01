# Cybersecurity Resilience Critical Services

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/cybersecurity-resilience-critical-services` |
| 分级 | `C5` - 可能性生态承载层 |
| 控制轴 | 外部生态承载 |
| 分级理由 | 关键词显示该域主要承载能源、水、食物、住房、治理、经济、通信、灾害或基础设施环境。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何承载主体展开未来的外部世界条件，例如能源、水、食物、住房、通信、治理、经济和基础设施？

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

- 界定外部承载条件：能源、水、食物、住房、通信、交通、治理、经济或公共基础设施。
- 说明它如何改变主体展开未来所需的稳定性、冗余、可获得性和安全边界。
- 记录基础设施依赖：供应链、地理环境、制度、资金、维护能力和公共服务。
- 识别冲击场景：灾害、战争、断供、污染、气候、系统失灵或社会支持崩溃。
- 建立韧性指标：可用率、恢复时间、冗余、成本、覆盖范围、可负担性和风险暴露。

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

`cybersecurity-resilience-critical-services/` 研究网络安全、关键服务韧性、事件响应、身份保护、供应链安全和数字系统恢复如何防止医疗、金融、能源、公共服务和个人数据被攻击截断。

> 核心问题：当医疗、福利、金融、身份、通信和 AI 工具都数字化后，网络攻击不再只是信息技术问题，而是主体持续性、资源可达、照护连续和未来选择权问题。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖数字身份、医疗系统、支付系统、公共服务和 AI 工具
  -> 这些系统必须能抵御攻击、错误配置、勒索、供应链入侵和数据泄露
  -> 网络安全失败会造成服务中断、身份盗用、数据暴露、资源断线和组织瘫痪
  -> 因此网络安全韧性是数字化主体持续性的关键风险域
```

## 关注对象

- 网络安全治理、关键基础设施安全、事件响应、业务连续、勒索软件、供应链攻击、身份与访问管理。
- 医疗、公共服务、金融、能源、通信、教育和科研系统的数字韧性。
- 备份、恢复、漏洞管理、最小权限、监测、通报、演练和跨组织协作。
- 与 `digital-identity-security/` 的边界：数字身份域关注个体身份、账号和凭据；本域关注组织和关键服务的网络安全韧性。
- 与 `supply-chain-continuity/` 的边界：供应链域关注供给链连续；本域关注数字攻击和网络恢复。

## Human Infra 模型链路

```text
网络安全韧性 T
  -> 改变漏洞管理、访问控制、监测、备份、事件响应和服务恢复变量 X
  -> 改变关键数字服务可用性、完整性、保密性和恢复状态 S
  -> 改变服务中断、勒索、身份盗用、数据泄露和级联故障风险 λ(t)
  -> 影响医疗连续性、资源可达、信任、恢复能力和主体持续性
```

## 非目标

- 不提供攻击、入侵、绕过认证、恶意软件、钓鱼、漏洞利用、权限提升或规避检测策略。
- 不提供对具体系统的攻击面分析、目标选择或实操利用步骤。
- 不把网络安全资料写成恐吓、监控扩权或无边界数据收集的理由。

## Source Signals

- NIST Cybersecurity Framework: https://www.nist.gov/cyberframework
- CISA Critical Infrastructure Security and Resilience: https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience
- CISA Cybersecurity Best Practices: https://www.cisa.gov/topics/cybersecurity-best-practices
- ENISA Cybersecurity: https://www.enisa.europa.eu/topics
- OECD Digital Security: https://www.oecd.org/digital/digital-security/

## 下一步

- 建立网络韧性变量表：暴露面、身份访问、备份、恢复时间、事件响应、供应链安全、数据泄露和服务连续性。
- 与 `digital-identity-security/`、`patient-data-interoperability/`、`financial-inclusion-payment-systems/` 和 `ai-agency-safety/` 建立接口。
