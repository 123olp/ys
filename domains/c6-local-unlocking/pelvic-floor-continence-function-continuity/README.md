# Pelvic Floor Continence Function Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/pelvic-floor-continence-function-continuity` |
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

`pelvic-floor-continence-function-continuity/` 研究盆底功能、尿失禁、便失禁、盆腔器官脱垂、产后/老年功能恢复、羞耻和服务可及如何影响主体持续性。

> 核心问题：盆底和控尿控便功能直接影响行动半径、睡眠、社交、工作、照护负担和尊严，是有效时间与社会参与的隐性基础设施。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要可预测的排泄控制、行动半径、睡眠和尊严维持日常任务
  -> 盆底功能障碍会通过失禁、疼痛、感染、跌倒、社交回避和照护负担消耗有效时间
  -> 结果取决于筛查沟通、治疗转介、康复可及、用品可及和非污名环境
  -> 因此盆底与控尿控便功能是身体行动和社会参与之间的关键域
```

## 关注对象

- Pelvic floor function、urinary incontinence、fecal incontinence、pelvic organ prolapse、postpartum recovery, aging continence, pelvic floor physical therapy access, continence supplies, stigma。
- 与 `urogenital-continuity/` 的边界：该域关注泌尿生殖总机制；本域关注盆底、控尿控便和功能参与连续性。
- 与 `fall-risk-prevention-home-safety-continuity/` 的关系：夜尿、急迫性和浴厕环境可放大跌倒风险。

## Human Infra 模型链路

```text
盆底与控尿控便支持系统 T
  -> 改变症状识别、康复可及、用品可及、浴厕环境、羞耻和转介变量 X
  -> 改变行动半径、睡眠、感染风险、社交参与、照护负担和尊严状态 S
  -> 改变有效时间损失、跌倒、隔离、工作退出和生活质量下降 λ(t)
  -> 影响主体日常行动、关系参与、恢复和长期独立性
```

## 非目标

- 不提供个人失禁诊断、盆底训练步骤、用药、器械、手术、产后恢复计划、用品选择或医疗建议。
- 不生成个人症状评分、康复方案、检查排序、家庭处理、保险申诉或临床分诊。
- 不收集个案排泄、性健康、产后、手术、影像、药物、浴厕环境或身份敏感资料。

## Source Signals

- NIDDK urinary incontinence: https://www.niddk.nih.gov/health-information/urologic-diseases/bladder-control-problems
- NIDDK fecal incontinence: https://www.niddk.nih.gov/health-information/digestive-diseases/fecal-incontinence
- HHS OWH urinary incontinence: https://www.womenshealth.gov/a-z-topics/urinary-incontinence

## 下一步

- 建立 Pelvic Floor Continuity Card：symptoms, referral, rehabilitation access, supplies, bathroom environment, stigma, participation。
- 与 `urogenital-continuity/`、`rehabilitation-functioning/` 和 `fall-risk-prevention-home-safety-continuity/` 建立接口。
