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
