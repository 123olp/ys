# Data Quality Missingness Representativeness

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/data-quality-missingness-representativeness` |
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

本域研究数据质量、缺失机制、代表性、测量误差和数据治理如何决定 Human Infra 定量模型是否可信。

如果数据本身偏、缺、错、不可迁移，后续因果推断、生存分析、数字孪生和模型校准都会被污染。这个域是所有预测模型进入研究前的数据入口门禁。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要用数据观测主体状态、风险和干预效果
  -> 数据可能缺失、偏倚、不可代表、测量错误或来源不可追溯
  -> 需要数据质量、缺失机制和代表性审查
  -> data-quality-missingness-representativeness
```

## 关注对象

- 缺失数据机制：MCAR、MAR、MNAR，以及失访、删失和选择进入机制。
- 代表性、抽样偏倚、覆盖偏倚、健康志愿者偏倚、幸存者偏差和外部可推广性。
- 测量误差、批次效应、设备差异、标签噪声、编码漂移和数据血缘。
- 公开队列、EHR、wearables、omics、registry、trial、claims 和 survey 数据的适用边界。
- 数据质量如何进入因果、预测、校准和模型治理。

## Human Infra 模型链路

```text
数据源
  -> 数据质量、缺失机制和代表性审查
  -> 决定变量是否可进入因果推断或预测模型
  -> 偏差和缺失传播到风险函数、生存曲线和数字孪生
  -> 模型输出必须继承数据来源的适用边界和禁止用途
```

## 非目标

- 不收集、存储、清洗或发布个人敏感数据。
- 不提供数据再识别、隐私规避、爬取、数据买卖、伪造、补全造假或统计操控方法。
- 不把缺失数据“补完”后伪装成真实观测。
- 不用代表性不足的数据支撑普遍化个体结论。

## Source Signals

- STROBE reporting guidance: https://www.strobe-statement.org/
- RECORD statement for routinely collected health data: https://www.record-statement.org/
- All of Us Research Program: https://allofus.nih.gov/
- UK Biobank: https://www.ukbiobank.ac.uk/
- GTEx Portal: https://gtexportal.org/

## 下一步

- 建立 Human Infra 数据卡字段：source、population、collection process、missingness、measurement error、representativeness、license、privacy boundary。
- 为公开队列和数据库建立 Source Card，先审数据入口再进入模型。
- 与 `uncertainty-quantification-model-calibration/` 对接，把数据质量风险传递到模型可信度。
