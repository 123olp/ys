# Academic Advising Degree Progress Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/academic-advising-degree-progress-continuity` |
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

`academic-advising-degree-progress-continuity` 研究 academic advising、degree audit、课程排序、先修要求、学业预警、注册窗口、学业进度和完成路径如何影响学生把学习时间转化为学位、证书、能力和职业入口。

> 核心问题：学生即使被录取并获得资助，如果课程路径、学位要求、学业预警和 advising 断裂，仍会陷入无效学分、延迟毕业、失去资助和放弃学习路径。

## 关注对象

- 学业 advising、degree audit、program map、课程需求、先修链、注册优先级和课程可得性。
- Academic probation、satisfactory academic progress、early alert、retention intervention、withdrawal 和 re-enrollment。
- 通识、专业、辅修、证书、双学位、临床/实习要求、capstone 和 graduation check。
- 学业进度数据、学分完成率、gateway courses、课程失败率、time-to-degree、completion 和 stop-out。

## Human Infra 链路

```text
学业指导与学位进度连续
  -> 课程选择、学分积累和学位要求保持可理解可追踪
  -> 无效修课、延期毕业、资助资格丢失和学习放弃下降
  -> 学习轮次更稳定地转化为证书、能力和职业入口
  -> 主体长期行动能力、收入机会和未来选择权增强
```

## 非目标

- 不提供个人选课、专业选择、GPA、转专业、退课、停学、毕业审核、职业规划或学业申诉建议。
- 不替代 academic advisor、registrar、department、financial aid office、disability services 或 mental health services。
- 不收集或处理个人成绩、GPA、课程表、学术处分、残障资料、心理资料或资助资料。

## Source Signals

- NCES/IPEDS retention, graduation, completions and outcome measures: https://nces.ed.gov/ipeds/
- College Scorecard completion, cost and outcomes data: https://collegescorecard.ed.gov/
- Federal Student Aid satisfactory academic progress and enrollment status context: https://fsapartners.ed.gov/
- Public institutional catalog, degree audit and advising policy materials.

## 下一步

- 建立 `program map -> course availability -> credit accumulation -> progress warning -> completion` 变量表。
- 区分 advising 服务、学位审计、课程供给、学术风险预警、资助进度要求和毕业审核。
- 与 `learning-skill-acquisition`、`education-record-transcript-verification-continuity`、`student-financial-aid-grant-scholarship-continuity` 和本轮高教域建立边界。
