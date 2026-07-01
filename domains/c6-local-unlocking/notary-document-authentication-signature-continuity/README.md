# 公证、文件认证与签名连续性

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/notary-document-authentication-signature-continuity` |
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

本域研究公证、签名、电子签名、文件认证、apostille、授权文件和跨机构承认如何让关键声明、授权和记录具备可验证性。它关注的是“文件能被承认”这一制度基础，而不是个人公证、认证、签署或跨境文件办理建议。

## 研究对象

- 公证、见证、签名、电子签名、数字签名、远程在线公证和签署记录。
- 文件认证、apostille、领事认证、法院/政府/学校/商业文件的跨境承认。
- 授权书、同意书、声明、合同、医疗代理、财务代理和教育/家庭文件。
- 签名文件与身份、权限、证据链、合规、档案保存和长期可读性的关系。

## 价值链路

```text
主体需要把意愿、授权和事实变成可被他人承认的记录
  -> 签名、公证和认证机制把文件连接到身份、时间、权限和证据链
  -> 电子签名、远程公证和 apostille 扩展跨地点、跨机构、跨国使用能力
  -> 签署无效、身份无法确认、认证缺失或文件格式失效会让授权和事实不可执行
  -> 文件认证连续性把主体意愿和制度记录转化为可验证、可迁移、可执行的承认链
```

## 关键问题

- 哪些主体持续性文件依赖签名、公证或认证才能跨机构生效？
- 电子签名、远程公证和数字签名如何改变可及性、欺诈风险和长期验证？
- apostille、领事认证和跨境文件承认如何影响迁移、教育、家庭、工作和继承？
- 文件格式、证书、密钥、审计日志和档案保存如何影响几十年尺度的可验证性？

## 上游与下游

- 上游：`digital-identity-security/`、`legal-identity-civil-registration/`、`verifiable-credential-wallet-interoperability/`、`long-term-digital-preservation-format-migration/`。
- 下游：`financial-fiduciary-power-of-attorney-continuity/`、`advance-care-planning-medical-decision-continuity/`、`trust-estate-affairs-succession-continuity/`、`passport-travel-document-mobility-continuity/`、`contract-subscription-billing-consent-continuity/`。

## 非目标

- 不提供个人公证、apostille、认证、签署、电子签名、合同、授权书、移民、学校、继承、法院或法律建议。
- 不判断个人文件是否有效、是否需要公证、是否可认证、是否可跨境使用或是否可替代原件。
- 不协助伪造签名、公证、认证、印章、证书、身份、时间戳、电子签名记录或跨境文件。

## 初始资料入口

- U.S. Department of State: Authentications and apostilles
- State secretary of state / notary public official materials
- FTC / Federal legal materials on electronic signatures and E-SIGN context
- NIST: Digital identity and trust services materials
- Courts, agencies, schools and institutions issuing document-authentication requirements
