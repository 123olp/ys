# Health Data Privacy Governance

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
