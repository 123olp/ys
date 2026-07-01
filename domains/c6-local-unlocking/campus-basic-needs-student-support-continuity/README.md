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
