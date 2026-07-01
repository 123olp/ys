# Civic Participation Election Access

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/civic-participation-election-access` |
| 分级 | `C5` - 可能性生态承载层 |
| 控制轴 | 外部生态承载 |
| 分级理由 | 主要提供主体展开未来所需的基础环境、资源、治理或基础设施。 |
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


`civic-participation-election-access/` 研究公民参与、选民登记、投票可及、选举基础设施和公共决策入口能否让主体持续影响共同规则。

> 核心问题：主体不仅需要被制度服务，也需要能够参与制度生成；当登记、投票、无障碍、信任和救济失败时，长期规则会脱离主体利益。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体生活在会分配资源、权利、风险和未来路径的公共制度中
  -> 公民参与、选举接入、无障碍投票、选举可信和权利救济必须可达
  -> 主体才不是公共规则的被动承受者，而是共同规则的持续参与者
```

## 关注对象

- 选民登记、投票可及、选举信息、无障碍投票、海外/流动人口投票和投票权保护。
- 选举设备标准、投票系统安全、审计、透明度、误导信息、信任和争议处理。
- 非选举型公民参与、公共咨询、社区决策、代表性和制度反馈。
- 与法律身份、信息完整性、数字包容、治理权利和司法救济的接口。

## Human Infra 模型链路

```text
公民参与与选举接入
  -> 主体能登记、理解选项、无障碍投票并参与公共反馈
  -> 公共决策更有机会反映真实需求、风险暴露和资源缺口
  -> 权利、福利、环境、医疗、交通、住房和安全规则获得反馈修正
  -> 主体持续性获得公共制度层的长期纠偏能力
```

## 非目标

- 不提供竞选策略、政治说服、微定向动员、舆论操控、虚假信息、投票压制或选举干扰方法。
- 不提供个体投票资格、登记、法律救济或选举争议建议。
- 不把选举基础设施研究写成攻击、绕过、设备篡改或计票操控指南。

## Source Signals

- USA.gov Voter Registration: https://www.usa.gov/register-to-vote
- U.S. Election Assistance Commission Voters: https://www.eac.gov/voters
- NIST Voting: https://www.nist.gov/itl/voting
- International IDEA: https://www.idea.int/

## 下一步

- 建立公民参与变量表：登记可达、投票方式、无障碍、语言、信任、审计、争议处理和参与反馈。
- 整理 USA.gov、EAC、NIST voting、International IDEA、ACE 和选举观察 Source Cards。
- 与 `information-integrity-trust/` 明确分工：本域研究参与入口和制度反馈，后者研究信息环境可信度。
