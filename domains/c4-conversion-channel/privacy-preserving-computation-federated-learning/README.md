# Privacy Preserving Computation Federated Learning

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/privacy-preserving-computation-federated-learning` |
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

## 定位

本域研究隐私保护计算、差分隐私、联邦学习、安全多方计算、可信执行环境和合成数据等技术，如何让敏感主体数据在不被集中暴露的前提下进入研究、模型训练、风险评估和公共利益场景。

Human Infra 需要健康、组学、神经、行为、照护、位置、生命日志和服务数据来观察主体持续性。但这些数据一旦被集中、滥用或再识别，测量系统就会反过来侵蚀主体权利。本域是“可用数据”和“主体安全”之间的计算治理层。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要跨机构、跨时间、跨主体数据支持预测模型和证据生成
  -> 原始敏感数据集中化会制造隐私、歧视、再识别和权力失衡风险
  -> 需要隐私保护计算在数据不完全暴露的条件下支持学习和审计
  -> privacy-preserving-computation-federated-learning
```

## 关注对象

- 差分隐私、隐私预算、扰动、输出限制和效用损失。
- 联邦学习、协作学习、跨机构训练、模型聚合、客户端漂移和安全聚合。
- 安全多方计算、同态加密、可信执行环境和隐私增强技术。
- 合成数据、匿名化、去标识化、再识别风险和成员推断风险。
- 隐私保护计算如何服务 Human Infra 模型、Source Card、数据卡、模型卡和治理审计。

## Human Infra 模型链路

```text
敏感主体数据
  -> 隐私保护计算与授权治理
  -> 形成可审计的聚合统计、模型参数或受限输出
  -> 支撑因果推断、生存分析、数字孪生和技术评估
  -> 同时降低原始数据泄露、再识别和二次用途风险
```

## 非目标

- 不提供再识别、成员推断、模型反演、数据窃取、隐私绕过或攻击方法。
- 不提供密码协议实现细节、安全参数建议或生产部署指南。
- 不把“去标识化”“合成数据”“联邦学习”写成绝对安全。
- 不替代 `health-data-privacy-governance/`；本域只处理计算机制，权利、同意、用途和退出仍由隐私治理域负责。

## Source Signals

- NIST Privacy Framework: https://www.nist.gov/privacy-framework
- NIST Differential Privacy project: https://csrc.nist.gov/projects/differential-privacy
- NIST Collaborative Learning and Privacy: https://www.nist.gov/itl/applied-cybersecurity/privacy-engineering/collaborative-learning
- NIST Privacy-Enhancing Cryptography: https://csrc.nist.gov/projects/privacy-enhancing-cryptography
- National Academies report on data privacy and utility: https://nap.nationalacademies.org/catalog/13342/protecting-individual-privacy-in-the-struggle-against-terrorists-a-framework

## 下一步

- 建立 Privacy Computation Card：data type、threat model、privacy mechanism、utility loss、attack surface、audit evidence、forbidden claims。
- 与 `data-quality-missingness-representativeness/` 对接，记录隐私机制对偏差、缺失和代表性的影响。
- 与 `model-cards-ai-audit-documentation/` 对接，把隐私机制写入模型卡和审计轨迹。
