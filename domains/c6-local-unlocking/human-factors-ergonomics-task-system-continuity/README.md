# Human Factors Ergonomics Task System Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/human-factors-ergonomics-task-system-continuity` |
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


Human Factors Ergonomics Task System Continuity 研究人的身体、认知、工具、界面、环境和组织流程如何共同构成任务系统，防止任务失败被错误归因于个人能力不足。

> 核心问题：主体持续性不是个体意志问题，而是人、工具、环境和流程是否适配的问题。

## 研究对象

- Human factors、ergonomics、human systems integration、human-centered design、usability engineering 和 task-system design。
- 姿势、力量、可达性、显示控制、环境约束、工作站、界面、流程、训练和组织条件。
- 人因设计如何影响疲劳、错误、损伤、学习成本、恢复成本、行动质量和长期执行能力。

## 先验链路

```text
主体执行任务需要身体、认知、工具和环境匹配
  -> 人因与工效学决定任务是否适配人的能力边界
  -> 适配失败会增加错误、疲劳、损伤、摩擦和学习成本
  -> 任务执行质量下降，恢复成本和事故风险上升
  -> 有效时间、长期行动能力和未来选择权被压缩
  -> 因而人因工效学是主体持续性的任务系统设计层
```

## 关键变量

- 身体负荷、姿势、重复动作、视觉/听觉/触觉输入、控制布局、可达性和环境约束。
- 界面可用性、工作流程、任务复杂度、培训、监督、反馈和恢复机会。
- 过度监控、把适配失败归咎于个人、用工效学语言包装压榨和忽视残障需求的风险。

## 证据入口

- NASA Human Systems Integration / Human Factors materials。
- NIST human factors and human-centered design materials。
- FDA human factors and usability engineering guidance for medical devices。
- ISO 9241-210 human-centred design。

## 非目标

- 本域不提供医疗诊断、工伤法律建议、个体工位评估、设备采购建议或人体实验方案。
- 不提供监控员工、绩效评分、强制姿态纠正、规避 OSHA/安全法规或责任转嫁方案。
- 不收集身体测量、伤病记录、残障资料、工作监控数据或雇主/员工个案资料。

## 上下游

- 上游：`occupational-work-design/`、`assistive-technology-access/`、`public-service-design-accessibility/`。
- 下游：`cognitive-load-workload-measurement-continuity/`、`fatigue-risk-alertness-continuity/`、`automation-bias-mode-confusion-oversight-continuity/`。
