# AI Evaluation Benchmark Validity Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/ai-evaluation-benchmark-validity-continuity` |
| 分级 | `C3` - 可能性生成引擎层 |
| 控制轴 | 主体能力生成 |
| 分级理由 | 关键词显示该域主要增强认知、学习、工具、AI、技能或沟通能力。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何放大主体生成新路径的能力，例如认知、学习、注意力、记忆、AI、工具和反馈复利？

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


`ai-evaluation-benchmark-validity-continuity/` 研究 AI 评测、基准、任务集、能力边界、鲁棒性、覆盖率、污染风险和指标有效性，如何影响 Human Infra 对 AI 作为主体增强系统的可信判断。

> 核心问题：AI 能增强主体能力，但“模型看起来很强”不等于“在真实任务、真实风险和真实成本下可靠”。若评测失真，主体会把错误能力当作基础设施。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要借助 AI 扩展认知、行动、研究和协作能力
  -> AI 是否可用必须先通过评测、基准和任务验证进入判断
  -> 基准污染、任务错配、指标漂移和过拟合会制造虚假能力信号
  -> 因此 AI 评测与基准有效性是 AI 进入 Human Infra 前的能力校准域
```

## 关注对象

- 模型评测、benchmark、task suite、stress test、鲁棒性评估、校准、覆盖率和失败模式。
- 数据污染、训练-测试泄漏、leaderboard overfitting、任务代表性、指标选择和不确定性记录。
- 能力评测、安全评测、可用性评测、可靠性评测和 Human-AI 任务评测之间的边界。
- 与 `model-cards-ai-audit-documentation/` 的边界：模型卡域记录模型说明和审计文档；本域关注评测设计本身是否有效。
- 与 `uncertainty-quantification-model-calibration/` 的关系：该域提供统计校准语言；本域将校准问题落到 AI benchmark 和任务评估。

## Human Infra 模型链路

```text
AI 评测与基准有效性 T
  -> 改变能力信号、覆盖率、污染检测、失败样本和指标解释变量 X
  -> 改变主体对 AI 工具可靠性、适用边界和风险状态的判断 S
  -> 改变误用、过度信任、任务失败和错误自动化风险 λ(t)
  -> 影响有效时间、任务成功率、认知增强质量和未来选择权
```

## 非目标

- 不提供刷榜、污染测试集、绕过评测、隐藏失败样本或操控 benchmark 的方法。
- 不把单一排行榜、单一分数或厂商宣传写成真实能力证明。
- 不输出个体决策、医疗/法律/金融建议或“某模型绝对可用”的合规保证。

## Source Signals

- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- NIST AI RMF Generative AI Profile: https://www.nist.gov/itl/ai-risk-management-framework/generative-artificial-intelligence-profile
- Stanford HELM: https://crfm.stanford.edu/helm/latest/
- MLCommons AI Safety Benchmark: https://mlcommons.org/benchmarks/ai-safety/
- NIST Dioptra: https://pages.nist.gov/dioptra/

## 下一步

- 建立 AI Evaluation Source Card 字段：task, metric, coverage, contamination risk, uncertainty, failure mode, deployment mismatch。
- 与 `ai-red-teaming-adversarial-testing-continuity/`、`ai-incident-reporting-post-deployment-monitoring-continuity/` 和 `model-cards-ai-audit-documentation/` 建立证据接口。
