# AI Data Provenance Contamination Drift Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/ai-data-provenance-contamination-drift-continuity` |
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


`ai-data-provenance-contamination-drift-continuity/` 研究 AI 数据来源、数据谱系、训练-评测污染、分布漂移、数据更新、代表性和数据治理，如何决定 AI 能否可靠服务主体持续性。

> 核心问题：AI 的能力和风险高度依赖数据。数据来源不清、污染不可见、分布漂移未监控时，模型输出会失去可解释边界。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要 AI 把数据转化为判断、计划、研究和行动
  -> AI 判断依赖训练数据、评测数据、上下文数据和运行反馈数据
  -> 数据来源不明、污染、偏差、代表性不足和分布漂移会扭曲判断
  -> 因此 AI 数据谱系、污染与漂移治理是模型可信性的资料地基层
```

## 关注对象

- 数据来源、许可、采集语境、版本、清洗、标注、去重、代表性、缺失和更新历史。
- 训练-测试泄漏、benchmark contamination、retrieval contamination、prompt/context contamination 和生产数据漂移。
- 数据漂移监控、异常分布、概念漂移、反馈循环、数据删除和遗忘请求。
- 与 `data-quality-missingness-representativeness/` 的关系：该域关注一般数据质量；本域关注 AI 数据生命周期中的谱系、污染和漂移。
- 与 `ai-training-data-rights-opt-out-provenance/` 的边界：训练数据权利域关注 IP/退出/权利；本域关注技术可信性和数据状态。

## Human Infra 模型链路

```text
AI 数据谱系、污染与漂移治理 T
  -> 改变来源透明度、污染信号、代表性、版本和漂移监控变量 X
  -> 改变模型评测可信度、运行可靠性和输出可解释状态 S
  -> 改变错误推断、偏差放大、失效未发现和反馈污染风险 λ(t)
  -> 影响主体判断质量、AI 协作可靠性和长期任务连续性
```

## 非目标

- 不提供抓取受限数据、绕过 robots/访问控制、重新识别、数据清洗造假或隐匿来源的方法。
- 不保存私有训练数据、受限数据集、敏感个人数据或泄露语料。
- 不把“数据多”写成“数据可靠”，也不把合成或清洗后的数据写成无风险。

## Source Signals

- Datasheets for Datasets: https://arxiv.org/abs/1803.09010
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- Data Provenance Initiative: https://www.dataprovenance.org/
- OWASP LLM Top 10 - Data and Model Supply Chain risks: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- EU AI Act information portal: https://artificialintelligenceact.eu/

## 下一步

- 建立 AI Data Source Card 字段：source, license, collection context, contamination check, drift signal, representativeness, deletion constraint。
- 与 `synthetic-data-generation-validation-continuity/`、`ai-evaluation-benchmark-validity-continuity/` 和 `ai-model-supply-chain-provenance-release-continuity/` 建立数据到模型链路。
