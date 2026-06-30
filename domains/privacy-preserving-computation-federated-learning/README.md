# Privacy Preserving Computation Federated Learning

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
