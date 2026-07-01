# Apraxia Of Speech Motor Planning Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/apraxia-of-speech-motor-planning-continuity` |
| 分级 | `C2` - 可能性源体维护层 |
| 控制轴 | 生命载体维护 |
| 分级理由 | 关键词显示该域主要维护身体、脑、器官、细胞、急性生命风险或衰老损伤控制。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何维护产生可能性的生命载体，例如身体、脑、器官、细胞、急性生命风险或衰老损伤控制？

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

- 界定生命载体变量：细胞、组织、器官、脑、免疫、代谢、急性风险或衰老损伤。
- 说明影响机制：修复、替换、再生、控制、筛查、预防、维持或风险降低。
- 列出可观察状态：功能指标、生物标志物、疾病终点、失能时间、恢复能力或死亡风险。
- 记录副作用、过度干预、癌变、免疫、长期安全性和尾部风险。
- 区分机制合理性、体外证据、动物证据、人体早期数据、临床终点和长期安全性。

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

Apraxia of speech motor planning continuity studies disrupted speech motor planning as a constraint on reliable verbal output, conversational timing, and participation after neurologic or developmental disruption.

核心问题：

> 言语失用不是不知道要说什么，也不一定是肌肉无力，而是把想说的话规划成正确言语动作的程序不稳定；输出越不可预测，沟通越难持续。

## 先验位置

```text
主体持续性最大化
  -> 主体必须能稳定把意图规划成言语动作
  -> 言语运动计划失稳会导致错误、搜索、重试和说话不可靠
  -> 会话节奏、学习表达、工作沟通和关系互动被压缩
  -> 因而言语失用是意图到运动程序之间的规划失效模式
```

## 关注对象

- 成人获得性言语失用、儿童言语失用、言语运动计划、错误一致性、可懂度和练习负担。
- 沟通参与、家庭支持、学校/工作适配和替代通道。
- 与 `dysarthria-speech-intelligibility-continuity/` 的关系：构音障碍偏运动执行；本域偏运动计划。
- 与 `speech-sound-disorder-articulation-phonology-continuity/` 的关系：语音障碍偏发展性语音系统；本域偏言语运动计划。

## Human Infra 模型链路

```text
识别 / 支持 / 练习系统 / 替代通道 T
  -> 改变运动计划稳定性、错误率、可懂度和说话负担 X
  -> 改变会话、学习、工作和社交状态 S
  -> 改变表达失败、参与下降和沟通替代不足风险 λ(t)
  -> 影响主体表达效率、学习机会和未来选择权
```

## 非目标

- 不提供言语失用诊断、训练动作、儿童治疗计划、家庭练习处方或预后判断。
- 不根据个人录音、儿童发音或神经病史判断病因。
- 不替代言语语言治疗、神经、发育儿科、教育或康复服务。

## Source Signals

- ASHA apraxia of speech practice materials。
- NIDCD speech and language development resources。
- Motor speech disorder literature as research context。
