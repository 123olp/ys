# Home Care Task Coordination Care Plan Continuity

`home-care-task-coordination-care-plan-continuity/` 研究家庭照护任务、care plan、预约、药物、用品、交通、观察记录、家庭成员分工和跨服务交接如何被协调，防止照护从“有人负责”退化为“人人以为别人负责”。

> 核心问题：家庭照护最常见的失败不是没有爱，而是任务、时间、信息和责任没有可执行的共同真相源。照护任务协调把长期照护从隐性劳动变成可分配、可追踪、可交接的系统。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 长期照护包含大量重复任务、异常观察和跨人交接
  -> 任务必须被记录、分配、提醒、升级和复核
  -> 否则照护系统会在误解、遗漏、重复和责任漂移中失效
```

## 关注对象

- Care plan、家庭任务清单、预约、药物/用品提醒、观察记录、异常升级和责任分工。
- 家庭成员、paid caregiver、home health、primary care、specialist、pharmacy 和社区服务之间的交接。
- 共享日历、纸质 binder、照护 app、隐私、代理访问和数据最小化。
- 与 `personal-automation-integration-workflow-continuity/`、`patient-portal-account-message-continuity/`、`care-transitions-discharge-continuity/` 的接口。

## Human Infra 模型链路

```text
家庭照护任务协调系统
  -> 改变任务可见性、责任分配、提醒、交接、异常升级和复核能力
  -> 改变照护遗漏、重复劳动、家庭冲突、服务断点和再入院风险
  -> 降低药物/预约/用品/观察遗漏和照护者认知负荷
  -> 增加居家持续性、家庭协作和主体未来选择权
```

## 非目标

- 不生成个人 care plan、用药表、预约安排、护理任务、监测指标或家庭分工建议。
- 不接入、存储或同步个人健康数据、家庭日历、患者门户、药房、保险或设备资料。
- 不替代医生、护士、社工、照护经理、药师、家庭会议或法律代理。
- 不提供监控、定位、约束、家庭纠纷裁决或隐私绕过方案。

## Source Signals

- AHRQ Care Coordination: https://www.ahrq.gov/ncepcr/care/coordination.html
- NIA Long-Distance Caregiving: https://www.nia.nih.gov/health/caregiving/long-distance-caregiving
- NIA Caregiving: https://www.nia.nih.gov/health/caregiving
- CMS Home Health Services: https://www.cms.gov/medicare/coverage/home-health-services

## 下一步

- 建立家庭照护任务协调变量表：任务类型、责任人、提醒、异常升级、资料共享、隐私、交接和复核。
- 整理 care coordination、family caregiving, discharge handoff 和 proxy access Source Cards。
