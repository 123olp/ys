# Decontamination Exposure Triage Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/decontamination-exposure-triage-continuity` |
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

`decontamination-exposure-triage-continuity/` 研究危险材料暴露后的去污入口、医疗分流、医院准备、隐私尊严、衣物/财物处理、心理压力和家庭重聚如何影响主体恢复。

> 核心问题：去污和分诊如果只被看成技术动作，会忽略人的尊严、照护依赖、语言理解、残障需求、医院二次污染和家庭接续。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 暴露后主体需要从危险现场转入医疗和恢复系统
  -> 去污、分诊、转运、信息记录和家庭重聚决定伤害是否被放大
  -> 暴露后连续性把污染控制、医疗入口和人的尊严接在一起
```

## 关注对象

- 去污入口、暴露分流、医院去污准备、二次污染风险、衣物/财物、隐私、语言、残障、儿童和家庭重聚。
- 与 `overdose-poisoning-reversal-toxicology-continuity/` 的关系：中毒逆转域关注急性毒性救援窗口；本域关注危险材料暴露后的系统入口和分流连续性。

## Human Infra 模型链路

```text
暴露后去污与分诊连续性
  -> 改变二次污染、就医延迟、尊严损害、家庭断裂和医疗挤兑
  -> 改变急性伤害、长期功能损失、信任和恢复速度
  -> 支撑主体从事故暴露回到可行动状态
```

## 非目标

- 不提供去污步骤、暴露处理、化学品急救、医疗分诊、医院流程设计或现场操作。
- 不提供个体诊断、解毒、药物、剂量、采样、证据保存或法律建议。
- 不提供规避去污、规避医疗、隐藏暴露、污染转移或危险材料处置方法。

## Source Signals

- HHS CHEMM: https://chemm.hhs.gov/
- ATSDR Medical Management Guidelines: https://wwwn.cdc.gov/TSP/MMG/
- OSHA HAZWOPER decontamination context: https://www.osha.gov/hazwoper
- ASPR TRACIE hospital preparedness resources: https://asprtracie.hhs.gov/

## 下一步

- 建立 Exposure Triage Card：exposure context, decontamination interface, medical referral, dignity/privacy, family reunification, hospital surge。
- 与 `healthcare-surge-triage-capacity-continuity/`、`emergency-medical-services-prehospital-care/` 和 `language-access-plain-communication/` 建立接口。
