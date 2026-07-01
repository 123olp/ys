# Survival Analysis Healthspan Risk Modeling

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/survival-analysis-healthspan-risk-modeling` |
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

本域研究生存分析、竞争风险、健康寿命和有效时间建模如何成为 Human Infra 定量预测层的数学底座。

Human Infra 关注的不是“某因素好不好”，而是它如何改变死亡风险、疾病发生时间、失能时间、健康状态积分、有效行动窗口和未来选择权。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体持续性必须被表示为随时间展开的随机路径
  -> 寿命、健康寿命、失能和死亡不是静态标签
  -> 需要风险函数、生存曲线、竞争风险和健康质量积分
  -> survival-analysis-healthspan-risk-modeling
```

## 关注对象

- 死亡时间 `T`、生存函数 `S(t)`、风险函数 `lambda(t)`、累计风险和删失。
- 健康寿命、失能时间、疾病发生时间、复发、再入院和多状态模型。
- 竞争风险、联合模型、纵向 biomarker 与事件时间建模。
- 健康质量积分、有效时间、主观时间和相对时间在模型中的位置。
- 人群模型、个体预测模型、校准、外部验证和报告边界。

## Human Infra 模型链路

```text
主体状态 X_t
  -> 状态决定当前风险 lambda(t | X_t)
  -> 风险函数生成生存曲线 S(t)
  -> 疾病、失能和死亡事件改变未来行动窗口
  -> 健康质量积分决定有效寿命和有效时间
  -> 技术/干预的价值表现为风险下降、事件推迟和选择权扩大
```

## 非目标

- 不输出个体死亡日期、寿命承诺、保险定价、临床诊断或治疗建议。
- 不把群体平均风险当成个体命运。
- 不把替代终点、短期 biomarker 或未校准模型当成真实寿命终点。
- 不用图表制造确定性幻觉。

## Source Signals

- Kaplan-Meier estimator: https://www.tandfonline.com/doi/abs/10.1080/01621459.1958.10501452
- Cox proportional hazards model: https://rss.onlinelibrary.wiley.com/doi/10.1111/j.2517-6161.1972.tb00899.x
- Survival analysis in clinical prediction context: https://www.probast.org/
- TRIPOD reporting guidance: https://www.tripod-statement.org/

## 下一步

- 定义 Human Infra 的 `lifespan / healthspan / effective time / subjective time / relative time / option value` 结局字典。
- 建立 toy survival curve，用于展示技术 T 如何改变风险函数而不是给出个体死亡日期。
- 与 `uncertainty-quantification-model-calibration/` 对接，要求所有曲线接受校准和误差审查。
