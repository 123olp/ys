# Gait Balance Assessment Fall Screening Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/gait-balance-assessment-fall-screening-continuity` |
| 分级 | `C4` - 可能性转换通道层 |
| 控制轴 | 路径转换接口 |
| 分级理由 | 关键词显示该域主要处理研究、数据、模型、服务入口、身份记录、转化或治理接口。 |
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

Gait, balance assessment, and fall screening continuity studies screening instruments, mobility observation, balance confidence, referral, and follow-up as interfaces between vestibular instability and preventable fall-related loss of independence.

核心问题：

> 跌倒不是只在摔倒那一刻发生；它之前通常有步态、平衡、药物、视力、前庭、环境和信心变化。若这些信号没有进入筛查和转介，主体会在风险升高后才被系统看见。

## 先验位置

```text
主体持续性最大化
  -> 主体必须在跌倒和骨折前被识别为行动风险上升
  -> 步态、平衡、前庭、视觉、药物和环境共同决定跌倒暴露
  -> 筛查和转介把隐性风险转成可处理任务
  -> 因而步态平衡筛查是空间行动连续性的预警接口
```

## 关注对象

- 步态、平衡、移动信心、跌倒史、筛查工具、转介、家庭安全和服务衔接。
- 与 `fall-risk-prevention-home-safety-continuity/` 的关系：后者关注家庭防跌倒干预；本域关注平衡/步态信号如何进入筛查。
- 与 `musculoskeletal-integrity/` 的关系：肌骨域关注骨骼、肌肉和骨折后果；本域关注移动稳定信号。
- 与 `vestibular-rehabilitation-balance-compensation-continuity/` 的关系：康复域关注恢复；本域关注识别和转介。

## Human Infra 模型链路

```text
筛查 / 步态观察 / 转介 / 跟踪 T
  -> 改变风险识别、平衡信心、活动计划和服务衔接 X
  -> 改变跌倒暴露、外出频率、家庭活动和照护需求状态 S
  -> 改变跌倒、骨折、失能、恐惧回避和机构化风险 λ(t)
  -> 影响独立生活、行动半径和未来选择权
```

## 非目标

- 不提供个人跌倒评分、步态诊断、助行器选择、家庭改造建议、训练计划或活动许可。
- 不根据传感器、视频、病史或自测结果判断个人风险等级。
- 不替代临床评估、物理治疗、老年医学、职业治疗或家庭安全评估。

## Source Signals

- CDC STEADI fall prevention resources。
- WHO falls and healthy ageing materials。
- NIDCD balance disorders resources。
