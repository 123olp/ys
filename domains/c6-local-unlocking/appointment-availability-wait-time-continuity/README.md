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
