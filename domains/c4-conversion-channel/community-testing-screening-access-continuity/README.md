# Community Testing Screening Access Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/community-testing-screening-access-continuity` |
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

`community-testing-screening-access-continuity/` 研究暴发中的社区检测、筛查、居家检测、检测点可达、结果报告和转介接口如何支撑主体持续性。

> 核心问题：没有可及检测，传播风险、工作学校决策和医疗分流都会退化为猜测。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 暴发期间主体需要知道自身与环境风险
  -> 风险判断依赖检测、筛查、报告和转介接口
  -> 社区检测可达性决定个体行动、组织运营和公共卫生响应是否有观测底座
```

## 关注对象

- 社区检测点、居家检测、筛查项目、检测可负担性、报告接口、阳性转介、阴性不确定性和可达公平。
- 与 `public-health-laboratory-diagnostic-capacity/` 的关系：公共卫生实验室域关注确认能力；本域关注社区层面的检测进入、筛查和报告执行。

## Human Infra 模型链路

```text
社区检测与筛查可达性
  -> 改变感染状态观测、组织决策、医疗分流和公共卫生报告能力
  -> 改变暴发响应中的信息延迟和错误行动概率
  -> 降低盲目传播、过度停摆、医疗挤兑和弱势群体漏检风险
  -> 增强有效行动、学习工作连续性和主体持续性
```

## 非目标

- 不提供检测选择、采样步骤、结果解释、诊断、治疗、隔离天数或旅行合规建议。
- 不提供检测规避、假结果、报告操纵、检测点拥堵利用或医疗资源抢占策略。
- 不把筛查项目写成个人医疗决策工具。

## Source Signals

- CDC testing guidance: https://www.cdc.gov/covid/testing/
- FDA COVID-19 tests: https://www.fda.gov/medical-devices/coronavirus-covid-19-and-medical-devices/covid-19-tests
- CDC public health surveillance: https://www.cdc.gov/surveillance/
- HHS public health emergency and testing resources: https://www.hhs.gov/

## 下一步

- 建立变量表：检测可达、成本、周转时间、报告延迟、筛查覆盖、阴性不确定性、转介路径和公平缺口。
- 与 `public-health-laboratory-diagnostic-capacity/`、`outbreak-case-investigation-contact-tracing-continuity/` 和 `health-data-privacy-governance/` 建立接口。
