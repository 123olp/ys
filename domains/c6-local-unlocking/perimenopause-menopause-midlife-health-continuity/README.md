# Perimenopause Menopause Midlife Health Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/perimenopause-menopause-midlife-health-continuity` |
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

`perimenopause-menopause-midlife-health-continuity/` 研究围绝经期、更年期症状、睡眠、情绪、骨骼、心血管、泌尿生殖健康、工作参与和医疗决策如何影响主体持续性。

> 核心问题：围绝经期不是单一症状事件，而是睡眠、情绪、骨骼、心血管、性健康、工作能力和长期风险重新排序的中年窗口。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体持续性依赖中年阶段的骨骼、睡眠、情绪、代谢、性健康和工作参与维护
  -> 围绝经期/更年期可改变症状负担、恢复能力、风险感知和医疗决策
  -> 结果取决于信息质量、非污名沟通、症状管理可及、风险评估和共享决策
  -> 因此更年期是寿命中段风险转轨和有效时间保护的关键域
```

## 关注对象

- Perimenopause、menopause symptoms、vasomotor symptoms、sleep disruption、mood, bone health, cardiovascular risk, genitourinary syndrome, workplace participation, hormone therapy decision support boundaries。
- 与 `endocrine-hormonal-regulation/` 的边界：该域关注激素调节总机制；本域关注围绝经期到中年健康的执行和决策连续性。
- 与 `osteoporosis-fracture-prevention-bone-health-continuity/` 的关系：骨量和骨折风险是更年期后长期持续性的关键分支。

## Human Infra 模型链路

```text
围绝经期与中年健康支持系统 T
  -> 改变症状识别、睡眠质量、情绪稳定、骨骼风险、泌尿生殖健康和工作支持变量 X
  -> 改变恢复能力、有效时间、关系参与、长期风险感知和医疗决策状态 S
  -> 改变失眠、抑郁、骨折、心血管风险、工作退出和生活质量损失 λ(t)
  -> 影响主体中年到老年阶段的行动能力、健康寿命和未来选择权
```

## 非目标

- 不提供个人激素治疗、补充剂、用药、检查排序、症状诊断、癌症/心血管风险判断或治疗建议。
- 不生成个人更年期评分、处方替代、工作证明、保险路径或临床分诊。
- 不收集个案月经、症状、病史、用药、癌症风险、性健康、工作或身份敏感资料。

## Source Signals

- NIA menopause: https://www.nia.nih.gov/health/menopause/what-menopause
- HHS Office on Women's Health menopause: https://www.womenshealth.gov/menopause
- NIH menopause hormone therapy information: https://www.nia.nih.gov/health/menopause/hormone-therapy-menopause

## 下一步

- 建立 Menopause Continuity Card：symptoms, sleep, mood, bone, cardiovascular, genitourinary, work participation, shared decision boundary。
- 与 `endocrine-hormonal-regulation/`、`osteoporosis-fracture-prevention-bone-health-continuity/` 和 `sleep-circadian-recovery/` 建立接口。
