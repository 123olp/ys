# Uncertainty Quantification Model Calibration

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/uncertainty-quantification-model-calibration` |
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

本域研究不确定性量化、模型校准、外部验证、漂移监测和报告规范如何防止 Human Infra 的预测模型产生虚假确定性。

Human Infra 可以做生命路径、健康寿命和未来选择权的模型表达，但必须明确模型不知道什么、错在哪里、在什么数据外失效，以及哪些输出不能被用于个体决策。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要预测技术和因素如何改变生命路径
  -> 预测必然包含模型误差、数据误差、分布漂移和未观测变量
  -> 需要不确定性量化、校准和外部验证
  -> uncertainty-quantification-model-calibration
```

## 关注对象

- 校准、区分度、外部验证、再校准、模型漂移和可迁移性。
- 置信区间、可信区间、预测区间、敏感性分析和情景分析。
- Bayesian modeling、ensemble、bootstrap、conformal prediction 和 uncertainty decomposition。
- TRIPOD、PROBAST、PROBAST-AI、AI risk management 和报告边界。
- 不确定性在生命路径图表、NCG、风险函数和 digital twin 中的表达方式。

## Human Infra 模型链路

```text
预测模型输出
  -> 必须附带数据来源、适用人群、校准状态和验证状态
  -> 必须区分 aleatoric uncertainty、epistemic uncertainty 和 model drift
  -> 不确定性决定输出只能用于研究、展示、排序、审查还是必须禁止
  -> 没有校准和外部验证的模型不能进入个体决策
```

## 非目标

- 不输出个体死亡日期、确定寿命预测、临床治疗建议、保险评分或自动化资格判断。
- 不用宽泛不确定性掩盖模型无效，也不用精确数字制造可信错觉。
- 不把大模型生成的解释当成模型验证。
- 不把未校准 toy model 包装成现实预测工具。

## Source Signals

- TRIPOD reporting guidance: https://www.tripod-statement.org/
- PROBAST risk of bias tool: https://www.probast.org/
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- BMJ prediction model reporting resources: https://www.bmj.com/

## 下一步

- 为 Human Infra 所有模型图表添加 `model status`：conceptual、toy、calibration-only、validated、blocked。
- 设计生命路径可视化的校准审查表，防止曲线被误读为个体预测。
- 与 `data-quality-missingness-representativeness/` 对接，明确数据偏差如何传递到模型不确定性。
