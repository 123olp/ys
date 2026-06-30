# 0025. Add Twenty-First-Wave Rural, Homelessness, Correctional, Disability, Dementia And Infectious Continuity Domains

Date: 2026-06-30

## Status

Accepted

## Context

Human Infra 已经覆盖身体维护、医疗服务、交通、住房、福利、公共服务、急救、药品、检验和道路安全等基础条件，但仍缺少一组“结构性脆弱与连续照护断点”域。

这些断点不是单一疾病或单一技术问题，而是主体进入地点排除、住所缺失、羁押与释放、残障服务、认知衰退和慢性传染病长期照护时，能否继续被服务系统承认、接住、保护和转介的问题。

## Decision

新增第 21 波 6 个正式研究域：

- `domains/rural-health-access-geographic-equity/`
- `domains/homelessness-unsheltered-health-continuity/`
- `domains/correctional-health-reentry-continuity/`
- `domains/disability-services-independent-living/`
- `domains/dementia-cognitive-decline-care-continuity/`
- `domains/chronic-infectious-disease-care-continuity/`

这些域共同处理主体持续性的结构性脆弱窗口：

```text
地点、住房、制度转换、功能状态、认知退行和长期感染
  -> 改变服务可达、身份承认、照护连续性、隐私、去污名和公共卫生屏障
  -> 决定主体是否能在高断裂风险场景中继续存在、行动、恢复和进入未来
```

## Consequences

- 域地图、研究域图谱、研究域雷达、README、AGENTS、伦理边界和仓库检查脚本必须同步包含这 6 个域。
- 每个域先只建立文档骨架，不新增数据目录、脚本、服务或自动化流程。
- 后续扩展必须以 Source Card 方式沉淀官方资料、综述、政策框架和证据边界。

## Non-goals

- 不提供个体医疗、诊断、治疗、用药、筛查、急救、福利、住房、法律、羁押、假释、就业、保险或迁居建议。
- 不提供露宿规避、执法规避、监狱安保规避、传播规避、接触追踪逃避、检测规避、实验室操作或病原体处理方法。
- 不把农村、无家可归、羁押/释放、残障、认知衰退或感染状态写成污名标签、个人失败、治安问题或排除理由。
