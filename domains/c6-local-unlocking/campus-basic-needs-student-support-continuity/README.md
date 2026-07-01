# Campus Basic Needs Student Support Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/campus-basic-needs-student-support-continuity` |
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


`campus-basic-needs-student-support-continuity` 研究高校学生的食物、住房、交通、托育、应急资金、福利导航、书本设备、卫生用品和学生支持服务如何影响学习持续、健康恢复和退学风险。

> 核心问题：高等教育不是纯认知任务；如果学生没有稳定食物、住所、交通、照护、设备和应急缓冲，学习时间会被生存任务吞噬。

## 关注对象

- 校园 food pantry、meal support、SNAP/benefits navigation、housing support、emergency grants 和 short-term aid。
- 交通、托育、书本设备、数字接入、卫生用品、衣物、紧急住宿和社区资源转介。
- Basic needs screening、case management、single stop/navigation、学生事务支持和跨部门转介。
- 基本需求不安全、课程负担、工作小时、缺勤、成绩下降、停学退学、心理压力和健康服务连接。

## Human Infra 链路

```text
校园基本需求与学生支持连续
  -> 食物、住房、交通、托育、设备和应急现金流被接住
  -> 生存性摩擦、缺勤、压力负荷和退学风险下降
  -> 学习时间、恢复能力和校园参与保持稳定
  -> 主体长期能力资本、职业路径和未来选择权增强
```

## 非目标

- 不提供个人福利申请、住房安排、校内资源预约、紧急住宿、食物援助、财务援助、托育或法律建议。
- 不替代高校 student affairs、basic needs office、case manager、counseling、housing office、福利机构或危机服务。
- 不收集或处理个人贫困、住房、食物、家庭、身份、心理、财务或福利资料。

## Source Signals

- U.S. Department of Education postsecondary basic needs and student support resources: https://www.ed.gov/
- Federal Student Aid emergency and institutional aid context: https://studentaid.gov/
- SNAP and public benefit navigation sources such as USDA and USA.gov.
- NCES/IPEDS and College Scorecard institutional context data.

## 下一步

- 建立 `basic needs insecurity -> service navigation -> retention -> effective learning time` 变量表。
- 区分食物、住房、交通、托育、设备、卫生、应急资金、福利导航和社区转介。
- 与 `food-security-nutrition-access`、`housing-built-environment-stability`、`transportation-access-mobility`、`childcare-family-continuity` 和本轮高教域建立边界。
