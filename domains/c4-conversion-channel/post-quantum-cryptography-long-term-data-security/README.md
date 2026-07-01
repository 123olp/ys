# Post Quantum Cryptography Long Term Data Security

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/post-quantum-cryptography-long-term-data-security` |
| 分级 | `C4` - 可能性转换通道层 |
| 控制轴 | 路径转换接口 |
| 分级理由 | 关键词显示该域主要处理研究、数据、模型、服务入口、身份记录、转化或治理接口。 |
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

`post-quantum-cryptography-long-term-data-security/` 研究后量子密码、长周期数据安全、加密迁移、身份凭据寿命和“现在收集、未来解密”风险，如何影响 Human Infra 的数字主体连续性。

> 核心问题：有效永生和主体持续性需要跨几十年甚至更长时间保存身份、医疗、研究、财务、作品和授权记录。若密码体系在未来被量子计算击穿，当前数据连续性会变成长期暴露风险。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 数字身份、医疗记录、研究资料和个人档案必须长期保密、完整和可验证
  -> 长期安全依赖密码算法、密钥管理、迁移计划、库存盘点和协议更新
  -> 若量子威胁或加密迁移失败，未来主体的隐私、身份和资源入口会被反向击穿
  -> 因此后量子密码是长周期数字主体连续性的安全域
```

## 关注对象

- 后量子公钥加密、签名、密钥交换、加密库存、协议迁移和 cryptographic agility。
- “harvest now, decrypt later” 风险、长期医疗/基因/神经数据、研究数据、数字身份和档案安全。
- 与 `cybersecurity-resilience-critical-services/` 的边界：网络安全域关注广义攻防和恢复；本域关注量子威胁下的长期密码迁移。
- 与 `digital-identity-security/` 的边界：数字身份域关注账号和凭据入口；本域关注底层密码算法寿命与迁移。

## Human Infra 模型链路

```text
后量子密码与长期数据安全 T
  -> 改变算法强度、密钥寿命、加密库存、迁移能力、协议敏捷性和长期保密变量 X
  -> 改变身份、医疗、研究、财务和个人档案的保密完整状态 S
  -> 改变未来解密、身份盗用、数据勒索、权限篡改和主体资料失控风险 λ(t)
  -> 影响数字连续性、资源入口、研究信任和主体持续性
```

## 非目标

- 不提供攻击、破解、规避审计、窃取密钥或绕过身份验证方案。
- 不替代组织级密码迁移、合规评估、密钥管理和安全工程审计。
- 不把某个算法或产品写成永久安全承诺。

## Source Signals

- NIST Post-Quantum Cryptography: https://csrc.nist.gov/projects/post-quantum-cryptography
- NIST finalized post-quantum encryption standards: https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards
- CISA Post-Quantum Cryptography Initiative: https://www.cisa.gov/quantum
- NSA CNSA 2.0: https://www.nsa.gov/Press-Room/News-Highlights/Article/Article/3148990/nsa-releases-future-quantum-resistant-qr-algorithm-requirements-for-national-se/

## 下一步

- 建立长期数据安全变量表：数据敏感期、算法、密钥长度、协议、库存、迁移状态、签名寿命和验证路径。
- 与 `digital-identity-security/`、`health-data-privacy-governance/`、`life-logging-personal-archives-continuity/` 和 `long-term-digital-preservation-format-migration/` 建立接口。
