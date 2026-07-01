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
