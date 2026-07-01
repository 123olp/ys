# Causal Inference Target Trial Emulation

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/causal-inference-target-trial-emulation` |
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


## 定位

本域研究因果推断和目标试验模拟如何把 Human Infra 的“技术/干预 T 是否改变主体持续性”从相关性叙事推进到可审查的干预问题。

Human Infra 不能只问某个变量是否和寿命、健康寿命或有效时间相关，而要问：如果改变这个变量，主体未来生命路径的概率分布是否会改变，以及这个判断依赖哪些识别条件。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 必须判断哪些技术和因素真正改变未来生命路径
  -> 必须区分相关信号、选择偏差、幸存者偏差和干预效果
  -> 需要因果图、目标试验模拟和反事实框架
  -> causal-inference-target-trial-emulation
```

## 关注对象

- 因果图、结构因果模型、反事实和 `do()` 干预。
- 时间变化混杂、选择偏差、幸存者偏差、反向因果和中介效应。
- 目标试验模拟、资格标准、时间零点、治疗策略、随访、结局和分析计划。
- 干预 T 对中间变量 X、主体状态 S、风险函数 `lambda(t)`、生存曲线和未来选择权的路径。
- 平均处理效应、异质性处理效应、可迁移性和可推广性。

## Human Infra 模型链路

```text
技术/干预 T
  -> 先被写成明确可执行的干预策略
  -> 用目标试验模拟定义对象、时间零点、比较组、结局和随访
  -> 用因果图识别混杂、选择机制、中介路径和禁止调整变量
  -> 估计 T 对状态转移、风险函数和健康质量积分的因果影响
  -> 再进入生存分析、数字孪生、模型校准和治理审查
```

## 非目标

- 不提供个体治疗、用药、筛查、临床试验入组或健康决策建议。
- 不把观察性相关性包装成因果结论。
- 不用 AI 总结替代研究设计、数据来源、偏差审查和人工判断。
- 不输出个体死亡日期、确定寿命收益或个体风险承诺。

## Source Signals

- Target trial emulation: https://pubmed.ncbi.nlm.nih.gov/36508210/
- Hernan and Robins causal inference book: https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/
- Using big data to emulate a target trial: https://pmc.ncbi.nlm.nih.gov/articles/PMC4832051/
- STROBE reporting guidance: https://www.strobe-statement.org/

## 下一步

- 建立 `intervention -> causal question -> target trial -> estimand -> evidence boundary` 的 Source Card 模板。
- 给山中因子、运动、早筛、AI 医学、可穿戴监测等方向分别写目标试验模拟草案。
- 与 `survival-analysis-healthspan-risk-modeling/` 对接，把因果效应转成风险函数和生存曲线位置。
