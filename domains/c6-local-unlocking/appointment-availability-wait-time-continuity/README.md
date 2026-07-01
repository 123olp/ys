# Appointment Availability Wait Time Continuity

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
