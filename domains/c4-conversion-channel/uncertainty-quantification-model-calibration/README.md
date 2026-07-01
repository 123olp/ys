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
