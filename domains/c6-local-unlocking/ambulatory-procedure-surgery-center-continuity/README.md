# Ambulatory Procedure Surgery Center Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/ambulatory-procedure-surgery-center-continuity` |
| 分级 | `C6` - 局部可能性解锁层 |
| 控制轴 | 局部阻塞解除 |
| 分级理由 | 未命中更高层边界、载体、能力、转换或生态规则，暂归为具体场景的局部可能性解锁。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域解除的是哪一个具体疾病、流程、服务、职业、家庭、社区或专项风险中的局部阻塞？

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

- 界定局部阻塞：某一疾病、流程、服务、职业、家庭、社区或专项风险中的具体失败点。
- 说明受影响任务：它阻碍了主体完成什么行动、服务、照护、转换或恢复过程。
- 记录可测改善：等待时间、错误率、成本、可及性、完成率、伤害率或恢复速度。
- 明确升级边界：何时应转交 C2-C5 的上层生命、能力、转化或基础设施域。
- 避免把局部改良包装成根本性解决方案，必须标注适用范围和外部依赖。

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

本域研究 ambulatory surgery center、门诊内镜、输注、透析外的门诊操作、术前准备、陪同/接送、麻醉风险筛查、感染控制、恢复观察和 follow-up 如何决定低住院化治疗能否安全发生。

它不是手术建议、术前准备指导、麻醉评估或机构推荐入口。

## 先验问题

```text
门诊操作何以成为安全修复通道？
  -> 操作地点和团队必须可用
  -> 准备、陪同、交通、麻醉筛查和感染控制必须闭合
  -> 操作后恢复和并发症回路必须存在
  -> 否则低住院化会把风险转移给家庭和主体
```

## 研究对象

- Ambulatory surgery center、outpatient procedure、endoscopy、infusion center 和 minor procedure clinic。
- Scheduling、pre-op clearance、patient instructions、escort/transport、NPO、medication hold 和 consent workflow。
- 麻醉支持、感染控制、设备可用、转院协议、恢复观察和 post-procedure follow-up。
- 取消、延期、无陪同、准备失败、授权失败和并发症回路。

## 关键变量

- 预约到操作时间、取消率、准备失败率、无陪同取消率和授权失败率。
- 术后电话/门户 follow-up、非计划急诊/住院、感染事件和转院事件。
- 语言/无障碍支持、交通约束、照护者可用性和说明理解。

## 证据入口

- CMS Ambulatory Surgical Center Quality Reporting、Medicare ASC coverage 和 infection control 资料。
- CDC outpatient settings infection prevention、AHRQ patient safety 和 perioperative safety 资料。
- Joint Commission / AAAHC / ASCA 等门诊操作安全资料。

## 非目标

- 不推荐操作、机构、麻醉、检查、输注、内镜、手术或术前术后处理。
- 不提供 NPO、用药暂停、陪同安排、并发症判断、感染处置或加急建议。
- 不收集病历、操作单、麻醉资料、保险、预约、交通、照护者或健康资料。

## 上下游

- 上游：`appointment-availability-wait-time-continuity/`、`specialist-referral-authorization-navigation-continuity/`、`surgical-anesthesia-perioperative-safety/`。
- 下游：`care-transitions-discharge-continuity/`、`home-health-hospice-palliative-care-continuity/`、`patient-safety-organizational-learning/`。
