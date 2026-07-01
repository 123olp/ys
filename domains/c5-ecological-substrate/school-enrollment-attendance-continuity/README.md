# School Enrollment Attendance Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/school-enrollment-attendance-continuity` |
| 分级 | `C5` - 可能性生态承载层 |
| 控制轴 | 外部生态承载 |
| 分级理由 | 关键词显示该域主要承载能源、水、食物、住房、治理、经济、通信、灾害或基础设施环境。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何承载主体展开未来的外部世界条件，例如能源、水、食物、住房、通信、治理、经济和基础设施？

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


`school-enrollment-attendance-continuity` 研究入学、转学、出勤、长期缺勤、无家可归学生保护、学籍交接和学校联系信息如何影响儿童与青少年持续学习、服务接入和未来选择权。

> 核心问题：主体在儿童与青少年阶段若无法稳定进入学校、持续出勤或完成学籍交接，学习轮次、营养、健康筛查、残障服务、心理支持和安全报告入口会同步断裂。

## 关注对象

- 入学资格、注册流程、居住地/监护关系证明和无固定住址情况下的入学替代路径。
- 日常出勤、长期缺勤、迟到、转学、迁居、灾后中断和家庭不稳定导致的学习损耗。
- McKinney-Vento 等无家可归学生保护、学籍与成绩资料交接、学校通知和家庭联系信息。
- 出勤数据、早期预警、补课恢复、家庭支持、交通、健康、照护和社会服务转介。

## Human Infra 链路

```text
学校入学与出勤连续
  -> 学习轮次、同伴关系、校内服务和家庭联系入口保持
  -> 长期缺勤、转学断裂和无记录学习损耗下降
  -> 能力积累、健康筛查、营养支持和保护性观察更稳定
  -> 儿童长期主体持续性、未来教育路径和社会参与能力增强
```

## 非目标

- 不提供个人入学、转学、学区、居住证明、出勤申诉、truancy、校规、特殊教育、儿童福利或法律建议。
- 不替代学校、学区、州教育机构、社工、法律援助、医疗或危机服务。
- 不收集或处理儿童个人教育记录、家庭地址、移民身份、健康资料或纪律资料。

## Source Signals

- U.S. Department of Education chronic absenteeism and student engagement resources.
- National Center for Education Statistics attendance, enrollment and school context data.
- National Center for Homeless Education McKinney-Vento legislation and implementation resources.
- State and local education agency enrollment, attendance and school stability guidance.

## 下一步

- 建立 `enrollment -> attendance -> service access -> learning continuity` 变量表。
- 区分普通缺勤、长期缺勤、学校排除、健康缺勤、交通缺勤和家庭不稳定缺勤。
- 与 `education-access-lifelong-learning`、`education-record-transcript-verification-continuity`、`childcare-family-continuity`、`child-protection-family-safety` 和本轮学校服务域建立边界。
