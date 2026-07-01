# Access Functional Needs Emergency Registry Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/access-functional-needs-emergency-registry-continuity` |
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

Access Functional Needs Emergency Registry Continuity 研究灾害和急救中的 access and functional needs、特殊医疗需求登记、辅助设备、电力依赖、交通协助、避难所可及和恢复服务如何让高脆弱主体不被危机系统排除。

> 核心问题：灾害平均人模型会杀人；需要电力、设备、药物、照护者、语言、交通或无障碍的人，必须在危机前被系统看见。

## 研究对象

- Access and functional needs、special needs registry、medical needs registry、vulnerable populations planning。
- 电力依赖设备、氧疗、冷藏药物、轮椅、听视障、认知障碍、语言服务、照护者和交通协助。
- 登记入口、隐私、数据更新、地方差异、通知、撤离、避难所和恢复服务。

## 先验链路

```text
灾害和停电会放大身体、认知、设备、语言和交通依赖
  -> 标准避难、撤离、通信和服务流程常默认主体可听见、可移动、可理解、可自带补给
  -> access and functional needs 登记把脆弱条件提前暴露给应急系统
  -> 登记缺失、过期、隐私不当或响应不足会导致被困、断药、断电、失联和照护断裂
  -> 因而功能需求急救登记是危机系统识别非平均主体的基础设施
```

## 关键变量

- 功能需求类型、设备/电力依赖、药物冷链、交通需求、照护者、语言和无障碍。
- 登记覆盖、更新频率、隐私保护、地方互操作、响应责任和退出机制。
- 过度监控、污名化、虚假安全感、服务不足和数据泄露风险。

## 证据入口

- Ready.gov disability and medical needs preparedness materials.
- FEMA access and functional needs planning materials.
- CDC emergency preparedness for vulnerable populations materials.
- Local emergency management registry materials.

## 非目标

- 本域不替个人报名 registry、判断资格、制定撤离计划、提供灾害现场建议或推荐避难所。
- 不提供医疗、法律、福利、保险、残障便利、设备、交通或应急处置建议。
- 不收集残障证明、设备、药物、地址、联系方式、定位、照护者、移民状态或健康资料。

## 上下游

- 上游：`household-emergency-preparedness-resilience/`、`healthcare-disability-accommodation-accessibility-continuity/`、`utility-affordability-shutoff-protection-continuity/`。
- 下游：`community-resilience-hub-shelter-center-continuity/`、`public-accommodation-accessibility-service-continuity/`、`emergency-alerts-communications/`。
