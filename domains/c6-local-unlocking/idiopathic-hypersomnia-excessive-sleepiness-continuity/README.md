# Idiopathic Hypersomnia Excessive Sleepiness Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/idiopathic-hypersomnia-excessive-sleepiness-continuity` |
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

`idiopathic-hypersomnia-excessive-sleepiness-continuity/` 研究特发性嗜睡、白天过度嗜睡、醒后困难、睡眠惯性、诊断不确定性和长期功能损耗如何影响主体持续性。

> 核心问题：特发性嗜睡会让主体拥有足够睡眠时间却仍难以稳定清醒，直接压缩可用行动窗口、任务启动能力和社会解释空间。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要可启动、可维持、可解释的清醒状态执行任务
  -> 特发性嗜睡可造成长睡眠、醒后困难和持续日间嗜睡
  -> 结果取决于诊断排除、睡眠医学可及、学校/工作支持和污名治理
  -> 因此特发性嗜睡是有效时间可用性与清醒启动能力的关键研究域
```

## 关注对象

- Idiopathic hypersomnia、excessive daytime sleepiness、sleep inertia、difficulty awakening、long sleep time、diagnostic uncertainty、school / work participation、stigma。
- 与 `narcolepsy-daytime-sleepiness-continuity/` 的边界：该域关注发作性睡病、猝倒和睡眠发作；本域关注非发作性睡病的持续嗜睡和醒后困难。
- 与 `chronic-insomnia-cbti-access-continuity/` 的关系：失眠域关注睡不着和恢复失败；本域关注睡了仍无法清醒。

## Human Infra 模型链路

```text
特发性嗜睡识别与支持系统 T
  -> 改变日间嗜睡、睡眠惯性、任务启动困难、诊断延迟、解释成本和支持可及变量 X
  -> 改变有效清醒时间、学习/工作启动、社交参与、交通暴露和心理负担 S
  -> 改变失误、旷课/缺勤、就业损耗、污名和有效时间损失 λ(t)
  -> 影响主体行动密度、身份稳定和未来选择权
```

## 非目标

- 不提供个人嗜睡诊断、睡眠检查解释、药物选择、兴奋剂建议、剂量、驾驶限制、学校/工作便利或治疗建议。
- 不生成个人睡眠评分、请假证明、保险/残障材料、用药方案、作息方案或安全许可判断。
- 不收集个案睡眠日志、可穿戴数据、用药、病史、驾驶、学校、工作、心理健康或可识别医疗资料。

## Source Signals

- MedlinePlus idiopathic hypersomnia: https://medlineplus.gov/ency/article/000803.htm
- MedlinePlus sleep disorders: https://medlineplus.gov/ency/article/000800.htm

## 下一步

- 建立 Hypersomnia Continuity Card：sleepiness, awakening difficulty, sleep inertia, diagnostic uncertainty, support access, stigma, safety exposure。
- 与 `sleep-circadian-recovery/`、`narcolepsy-daytime-sleepiness-continuity/` 和 `attention-executive-control/` 建立接口。
