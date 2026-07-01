# Vestibular Migraine Dizziness Sensory Load Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/vestibular-migraine-dizziness-sensory-load-continuity` |
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

Vestibular migraine dizziness and sensory load continuity studies migraine-linked vertigo, motion sensitivity, light/sound sensitivity, cognitive fog, and episodic disability as a cross-domain burden on effective time.

核心问题：

> 偏头痛相关眩晕不是单纯头痛，也不是单纯平衡问题；它会把光、声、运动、屏幕、通勤和认知任务组合成一组发作性行动限制。

## 先验位置

```text
主体持续性最大化
  -> 主体必须能在感官负荷和空间运动中保持任务能力
  -> 偏头痛相关前庭症状会同时扰动眩晕、光声敏感、注意和恢复
  -> 发作和残余期会压缩工作、学习、出行和社交窗口
  -> 因而前庭性偏头痛是感官负荷与有效时间之间的交叉失效模式
```

## 关注对象

- 前庭性偏头痛、眩晕、运动敏感、光声敏感、脑雾、恶心和发作后疲劳。
- 屏幕任务、会议、驾驶/通勤、学习负担、社交参与和恢复安排。
- 与 `migraine-headache-effective-time-burden/` 的关系：偏头痛域关注总体失能；本域关注眩晕和感官负荷交叉。
- 与 `tinnitus-sound-tolerance-sleep-continuity/` 的关系：耳鸣域关注内源声音；本域关注偏头痛相关声光运动敏感。

## Human Infra 模型链路

```text
识别 / 负荷管理 / 工作学习适配 / 恢复支持 T
  -> 改变眩晕发作、感官敏感、认知雾和恢复时间 X
  -> 改变屏幕工作、出行、学习、社交和休息状态 S
  -> 改变失能天数、事故暴露、孤立和有效时间损耗风险 λ(t)
  -> 影响长期能力积累、角色维持和未来选择权
```

## 非目标

- 不提供前庭性偏头痛诊断、药物、补剂、饮食、触发因素处方、驾驶或工作限制建议。
- 不根据个人症状区分偏头痛、BPPV、梅尼埃病、PPPD 或脑血管事件。
- 不替代神经、耳鼻喉、康复、心理健康或急诊服务。

## Source Signals

- NIDCD balance disorders resources。
- American Migraine Foundation / NIH migraine education as secondary context。
- Vestibular migraine consensus literature as research context。
