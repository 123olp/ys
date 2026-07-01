# Health Data Privacy Governance

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/health-data-privacy-governance` |
| 分级 | `C4` - 可能性转换通道层 |
| 控制轴 | 路径转换接口 |
| 分级理由 | 主要把科学、医疗、数据、制度或技术从潜在能力转成真实可用路径。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何把潜在可能性转成真实可用路径，例如研究、医疗、数据、制度、身份、资金或转化接口？

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

- 界定转化瓶颈：研究发现、数据、临床、制度、身份、资金、可及性或操作接口。
- 说明接口机制：潜在可能性如何经过标准、流程、记录、组织或平台变成可用路径。
- 记录必要证据：登记系统、指南、监管材料、数据库、标准文档或真实世界部署资料。
- 识别摩擦指标：时间成本、资金成本、信息成本、合规成本、可及性和协作成本。
- 列出失败点：证据断裂、监管阻塞、制度排斥、隐私风险、责任不清或资源不可达。

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

`health-data-privacy-governance/` 研究健康、基因、行为、神经和服务使用数据的隐私、同意、安全、共享、二次使用和治理边界。

> 核心问题：Human Infra 越依赖数据，就越必须先保护主体的同意、退出、用途边界、访问控制和被滥用后的恢复路径；否则测量系统会反过来吞噬主体。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体状态需要被观测、记录、建模和反馈
  -> 观测会产生高敏感健康、基因、行为、神经和社会需求数据
  -> 数据治理必须先约束采集、共享、二次使用、安全和退出
  -> 数据系统才能支撑主体持续性，而不是制造控制、歧视和不可逆暴露
```

## 关注对象

- 健康隐私、受试者保护、同意、撤回、访问控制、最小必要使用和用途限制。
- 健康信息共享、信息阻断、基因组数据共享、去标识化风险、再识别风险和数据安全。
- 与 `patient-data-interoperability/` 的关系：患者数据互操作域关注数据是否能随主体流动；本域关注流动时是否有权利、安全和治理边界。
- 与 `digital-identity-security/`、`governance-rights/`、`measurement-feedback/` 和 `synthetic-biology-biosecurity/` 的接口。

## Human Infra 模型链路

```text
健康数据隐私治理基础设施
  -> 改变数据采集、访问、共享、撤回、安全和二次使用边界
  -> 改变主体被测量、被建模、被照护和被研究时的权利状态
  -> 降低隐私暴露、再识别、歧视、越权使用、信任崩塌和系统性排除风险
  -> 增强数据可用性、主体自主性、长期信任和可审查研究能力
```

## 非目标

- 不提供法律意见、合规认证、HIPAA/Common Rule 适用判断或机构合规方案。
- 不提供真实 PHI/基因/神经/行为数据处理架构、去标识化保证、数据共享许可或二次利用建议。
- 不提供账号绕过、授权绕过、隐私规避、数据抓取、渗透攻击或敏感数据交易方法。

## Source Signals

- HHS HIPAA Privacy Rule: https://www.hhs.gov/hipaa/for-professionals/privacy/index.html
- HHS Common Rule: https://www.hhs.gov/ohrp/regulations-and-policy/regulations/common-rule/index.html
- NIST Privacy Framework: https://www.nist.gov/privacy-framework
- NIST Cybersecurity Framework: https://www.nist.gov/cyberframework
- NIH Genomic Data Sharing Policy: https://sharing.nih.gov/genomic-data-sharing-policy
- GA4GH Framework for Responsible Sharing: https://www.ga4gh.org/product/framework-for-responsible-sharing-of-genomic-and-health-related-data/
- ONC Information Blocking: https://healthit.gov/information-blocking/

## 下一步

- 建立健康数据治理变量表：同意、撤回、访问控制、最小必要、用途限制、安全、共享、审计、再识别风险和退出。
- 与 `patient-data-interoperability/` 拆分数据流动和数据治理边界。
- 整理 HIPAA、Common Rule、NIST Privacy、NIST CSF、NIH GDS、GA4GH 和 ONC Information Blocking 的 Source Cards。
