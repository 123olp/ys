# Appointment Availability Wait Time Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/appointment-availability-wait-time-continuity` |
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

## 定位

本域研究预约容量、等待时间、取消名单、改期、no-show、同日预约、候补和服务时段如何把名义服务转化为真实发生的医疗接触。

它不是抢号脚本、排队规避、个案预约策略或医疗优先级判断入口。

## 先验问题

```text
服务存在何以成为主体可用时间窗口？
  -> 预约必须在疾病和风险窗口内发生
  -> 等待、改期、取消和缺席必须可治理
  -> 可用时段必须匹配主体交通、工作、照护和恢复约束
  -> 否则名义服务可及会变成实际延误
```

## 研究对象

- Appointment availability、wait time、open access、same-day access 和 cancellation list。
- 改期、提醒、no-show、late cancellation、候补和 referral-to-visit lag。
- 线上预约、电话预约、门户、语言服务、无障碍和交通时间约束。
- 初级照护、专科、检验、影像、操作和复诊预约容量。

## 关键变量

- 第三可用预约时间、referral-to-visit time、cancellation rate 和 no-show rate。
- 改期次数、预约成功率、提醒触达率、候补转化率和超时风险。
- 工作时段、交通距离、照护责任、语言/无障碍支持和数字入口可达性。

## 证据入口

- CMS appointment wait time、network adequacy 和 managed care access 资料。
- VA access to care wait time 方法、AHRQ access and timeliness 资料。
- Open scheduling、access management 和卫生服务运营研究。

## 非目标

- 不提供抢号、刷号、批量占位、候补操纵、预约规避或优先级伪造。
- 不判断个案等待是否安全、是否应急、是否要转急诊或如何加急。
- 不收集预约、诊断、保险、地址、工作安排、照护责任或门户账号资料。

## 上下游

- 上游：`provider-directory-network-adequacy-continuity/`、`primary-care-panel-appointment-access-continuity/`、`specialist-referral-authorization-navigation-continuity/`。
- 下游：`outpatient-laboratory-specimen-result-routing-continuity/`、`diagnostic-imaging-order-scheduling-report-continuity/`、`after-hours-urgent-care-triage-continuity/`。
