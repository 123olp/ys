# Information Integrity Trust

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/information-integrity-trust` |
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


Information Integrity Trust 负责整理信息可信度、证据质量、误导信息、平台传播、专家信任、AI 生成内容和认知污染如何进入主体持续性模型。

核心问题：

> 主体的行动依赖判断；判断依赖信息环境。错误、污染、操控或不可验证的信息会让主体把时间、金钱、健康和未来选择权投入错误路径。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体必须持续做出健康、技术、资源、关系和风险决策
  -> 决策质量依赖信息来源、证据质量、信任链和反操控能力
  -> 误导信息、阴谋叙事、AI 伪造和平台放大会改变主体风险判断
  -> 因此信息完整性与信任是主体持续性的认知环境域
```

## 关注对象

- 信息可信度、事实核验、证据等级、误导信息、健康 misinformation、平台传播、AI 生成内容和来源可追溯性。
- 信息环境如何影响医疗决策、风险感知、技术采用、政治制度、社会信任和资源配置。
- 与 `health-literacy-navigation/` 的边界：健康素养域关注个体理解和服务导航；本域关注更广义的信息生态、证据链和信任基础设施。
- 与 `ai-agency-safety/` 的边界：AI 代理安全关注工具行动控制；本域关注 AI 内容和信息环境对主体判断的影响。

## Human Infra 模型链路

```text
信息完整性因素 T
  -> 改变来源可信度、证据质量、可追溯性、误导暴露和信任链变量 X
  -> 改变主体判断环境状态 S
  -> 改变误判、错误治疗、风险低估、资源错配、操控和社会信任断裂风险 λ(t)
  -> 影响行动质量、有效时间、技术采用和未来选择权
```

## 非目标

- 不提供政治操控、舆论操纵、平台规避、假账号、虚假内容生产或传播策略。
- 不把单一事实核验或权威来源写成绝对真理；必须保留证据等级、适用范围和不确定性。
- 不输出个体医疗、法律、投资或政治建议。

## Source Signals

- WHO infodemic management: https://www.who.int/teams/risk-communication/infodemic-management
- U.S. Surgeon General health misinformation advisory: https://www.hhs.gov/surgeongeneral/reports-and-publications/health-misinformation/index.html
- NIST AI Risk Management Framework Generative AI Profile: https://www.nist.gov/itl/ai-risk-management-framework/ai-risk-management-framework-generative-ai-profile

## 下一步

1. 建立信息完整性变量表：来源可信度、证据等级、可追溯性、误导暴露、AI 生成内容标识和信任链。
2. 与 `health-literacy-navigation/`、`ai-agency-safety/`、`digital-identity-security/` 和 `governance-rights/` 建立交叉边界。
